describe('Login', () => {

    it('should be able to login and navigate to dashboard - ADMIN', () => {
        cy.login('admin','admin');

        cy.url().should('include', '/dashboard');
               
        cy.get('h3').should('include.text', 'Malnutrition Dashboard (Admin)');
        cy.get('a.dropdown-item').last().click({force: true});
      });

      it('should be able to login and navigate to dashboard - AANGANWADI', () => {
        cy.login('Raashi Khanna','123');
        
        cy.url().should('include', '/programssummary');
        cy.get('h3').should('contain.text', 'Programs')
        cy.get('p').should('include.text', 'Think Nutrition');
        cy.get('.dropdown-item').click();
      });

      it('should be able to login and navigate to dashboard - NGO', () => {
        cy.login('test','123');

        cy.url().should('include', '/dashboard');
        cy.get('#navbarCollapse').should('contain.text', 'Programs')
        cy.get('a.dropdown-item').last().click({force: true});
      });

  });