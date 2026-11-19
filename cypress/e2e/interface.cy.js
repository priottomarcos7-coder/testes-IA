describe('Hub de Leitura — interface demonstrativa',()=>{
  beforeEach(()=>cy.request('POST','/api/test/reset'));
  it('CT07 - tela de perfil exibe situação do usuário',()=>{cy.request({method:'POST',url:'/api/admin/process',headers:{'x-role':'admin'}});cy.visit('/profile.html?id=2');cy.get('#status').should('contain','Bloqueado');cy.get('#reason').should('contain','atraso')});
  it('CT08 - painel administrativo carrega o resumo e a lista',()=>{cy.request({method:'POST',url:'/api/admin/process',headers:{'x-role':'admin'}});cy.visit('/admin.html');cy.get('#summary').should('contain','Bloqueados');cy.get('#blocked').should('contain','Bruno Atrasado')});
  it('CT09 - lista administrativa mostra usuários bloqueados',()=>{cy.request({method:'POST',url:'/api/admin/process',headers:{'x-role':'admin'}});cy.visit('/admin.html');cy.get('#refresh').click();cy.get('#blocked').should('contain','Diego Bloqueado')});
  it('CT18 - interface informa o motivo do bloqueio no perfil',()=>{cy.request({method:'POST',url:'/api/admin/process',headers:{'x-role':'admin'}});cy.visit('/profile.html?id=2');cy.get('#reason').should('contain','Empréstimo em atraso')});
});
