const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const DB_FILE = path.join(__dirname, 'data.json');
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const seed = () => ({
  users: [
    { id: 1, name: 'Ana Leitora', email: 'ana@hub.test', role: 'user', blocked: false, blockReason: null },
    { id: 5, name: 'Elisa no Limite', email: 'elisa@hub.test', role: 'user', blocked: false, blockReason: null },
    { id: 2, name: 'Bruno Atrasado', email: 'bruno@hub.test', role: 'user', blocked: false, blockReason: null },
    { id: 3, name: 'Carla Regular', email: 'carla@hub.test', role: 'user', blocked: false, blockReason: null },
    { id: 4, name: 'Diego Bloqueado', email: 'diego@hub.test', role: 'user', blocked: true, blockReason: 'Empréstimo em atraso há 9 dias' }
  ],
  loans: [
    { id: 101, userId: 2, title: 'Livro em atraso', overdueDays: 8, returned: false },
    { id: 102, userId: 3, title: 'Livro no limite', overdueDays: 7, returned: false },
    { id: 105, userId: 1, title: 'Livro regular', overdueDays: 0, returned: false },
    { id: 106, userId: 5, title: 'Livro com seis dias', overdueDays: 6, returned: false },
    { id: 103, userId: 4, title: 'Livro bloqueador', overdueDays: 9, returned: false },
    { id: 104, userId: 4, title: 'Segundo livro', overdueDays: 10, returned: false }
  ],
  reservations: [], audit: [], failures: []
});
let db;
function save() { fs.writeFileSync(DB_FILE, JSON.stringify(db, null, 2)); }
function reset() { db = seed(); save(); }
if (fs.existsSync(DB_FILE)) { try { db = JSON.parse(fs.readFileSync(DB_FILE)); } catch { reset(); } } else reset();

const user = id => db.users.find(u => u.id === Number(id));
const loansFor = id => db.loans.filter(l => l.userId === Number(id) && !l.returned);
const isEligible = id => loansFor(id).some(l => l.overdueDays > 7);
function audit(actor, action, userId, reason) {
  db.audit.push({ id: db.audit.length + 1, actor, action, userId: Number(userId), reason, at: new Date().toISOString() });
}
function requireAdmin(req,res,next) {
  if (req.header('x-role') !== 'admin') return res.status(403).json({ message: 'Permissão administrativa necessária.' });
  next();
}
app.get('/api/health', (_req,res) => res.json({ status: 'ok' }));
app.post('/api/test/reset', (_req,res) => { reset(); res.json({ message: 'Massa de dados reiniciada.' }); });
app.post('/api/test/failure/:kind', (req,res) => {
  if (!['calculation','processing'].includes(req.params.kind)) return res.status(400).json({message:'Falha desconhecida.'});
  db.failures.push(req.params.kind); save(); res.json({message:'Falha preparada.'});
});
app.get('/api/users/:id', (req,res) => {
  const u = user(req.params.id); if (!u) return res.status(404).json({message:'Usuário não encontrado.'});
  res.json({ ...u, loans: loansFor(u.id) });
});
app.get('/api/admin/users', requireAdmin, (_req,res) => res.json({ users: db.users.map(u=>({...u, loans:loansFor(u.id)})) }));
app.get('/api/admin/dashboard', requireAdmin, (_req,res) => res.json({ totalUsers:db.users.length, blockedUsers:db.users.filter(u=>u.blocked).length }));
app.get('/api/admin/blocked', requireAdmin, (_req,res) => res.json({ users:db.users.filter(u=>u.blocked).map(u=>({...u, overdueLoans:loansFor(u.id).filter(l=>l.overdueDays>7)})) }));
app.get('/api/audit', requireAdmin, (_req,res) => res.json({ events:db.audit }));
app.post('/api/admin/process', requireAdmin, (_req,res) => {
  if (db.failures.includes('processing')) { db.failures = db.failures.filter(x=>x!=='processing'); db.failures.push('processing-recorded'); save(); return res.status(503).json({message:'Rotina temporariamente indisponível. Tente novamente.'}); }
  if (db.failures.includes('calculation')) { db.failures = db.failures.filter(x=>x!=='calculation'); db.failures.push('calculation-recorded'); save(); return res.status(422).json({message:'Não foi possível calcular o atraso; nenhum bloqueio foi aplicado.'}); }
  const changed=[];
  db.users.forEach(u=>{
    if (isEligible(u.id) && !u.blocked) { u.blocked=true; u.blockReason='Empréstimo em atraso há mais de 7 dias'; audit('system','BLOCK',u.id,u.blockReason); changed.push(u.id); }
    if (!isEligible(u.id) && u.blocked && u.blockReason?.startsWith('Empréstimo')) { u.blocked=false; u.blockReason=null; audit('system','UNBLOCK',u.id,'Nenhum empréstimo elegível em atraso'); changed.push(u.id); }
  });
  save(); res.json({message:'Processamento concluído.', changedUsers:changed});
});
app.post('/api/users/:id/reservations', (req,res) => {
  const u=user(req.params.id); if(!u) return res.status(404).json({message:'Usuário não encontrado.'});
  if(u.blocked) return res.status(403).json({message:'Reserva não permitida: usuário bloqueado por atraso de empréstimo.'});
  const item={id:db.reservations.length+1,userId:u.id,title:req.body.title||'Livro reservado'}; db.reservations.push(item); save(); res.status(201).json(item);
});
app.post('/api/users/:id/loans/:loanId/renew', (req,res) => {
  const u=user(req.params.id); if(!u) return res.status(404).json({message:'Usuário não encontrado.'});
  if(u.blocked) return res.status(403).json({message:'Renovação não permitida: usuário bloqueado por atraso de empréstimo.'});
  const loan=loansFor(u.id).find(l=>l.id===Number(req.params.loanId)); if(!loan) return res.status(404).json({message:'Empréstimo não encontrado.'});
  res.json({message:'Renovação realizada com sucesso.'});
});
app.post('/api/users/:id/loans/:loanId/return', (req,res) => {
  const u=user(req.params.id); const loan=db.loans.find(l=>l.id===Number(req.params.loanId)&&l.userId===Number(req.params.id));
  if(!u||!loan||loan.returned) return res.status(404).json({message:'Empréstimo não encontrado.'});
  loan.returned=true; save(); res.json({message:'Devolução registrada. Execute o processamento para atualizar o bloqueio.'});
});
app.post('/api/admin/users/:id/unblock', requireAdmin, (req,res) => {
  const u=user(req.params.id); if(!u) return res.status(404).json({message:'Usuário não encontrado.'});
  if(!u.blocked) return res.status(409).json({message:'Usuário já está desbloqueado.'});
  u.blocked=false; u.blockReason=null; audit('admin','MANUAL_UNBLOCK',u.id,req.body.reason||'Desbloqueio manual'); save();
  res.json({message:'Bloqueio removido manualmente.'});
});
app.get('/api/users/:id/profile', (req,res) => {
  const u=user(req.params.id); if(!u) return res.status(404).json({message:'Usuário não encontrado.'});
  res.json({id:u.id,name:u.name,status:u.blocked?'Bloqueado':'Ativo',blocked:u.blocked,reason:u.blockReason});
});
app.get('/api/ui/admin', requireAdmin, (_req,res)=>res.sendFile(path.join(__dirname,'public','admin.html')));
app.get('/api/ui/profile/:id', (_req,res)=>res.sendFile(path.join(__dirname,'public','profile.html')));
app.use((err,_req,res,_next)=>{ console.error(err); res.status(500).json({message:'Erro interno.'}); });
app.listen(PORT,()=>console.log('Hub de Leitura disponível em http://localhost:'+PORT));
