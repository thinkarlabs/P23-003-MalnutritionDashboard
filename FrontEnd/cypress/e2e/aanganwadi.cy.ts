Aanganwadies data on page',() => {
       cy.visit('/aanganwadis');
       //cy.wait('@mockedNgos');
   
       cy.get('#tbl_ch')
         .find('td')
         .should('contain.text', 'Update')
     });
  
     it('should click on add button to navigate and Add an Aanganwadi', () => {
       cy.visit("/aanganwadis");
       cy.get('#addAanganwadi').click();
       
       cy.get('h3').contains('Add Aanganwadi');
  
       cy.get('[placeholder="Aanganwadi Contact Person"]').type('Luisa Zissman');
       cy.get('[placeholder="Phone Number"]').type('1234567890');
       cy.get('[placeholder="Latitude, Longitude Coordinates"]').type('61.62, 62.61');
       cy.get('[placeholder="Password"]').type('P@$$');
       cy.get('[placeholder="Location"]').type('Somewhere');
       
       cy.get('form').submit();
     });
  
     describe('Delete Aanganwadi', () => {
       it('Delete Aanganwadi', () => {
         cy.login('admin','admin')
         cy.visit('/aanganwadis')
         cy.get('#deleteAanganwadi').click();
       })
     });
  
  
     describe('EDIT Aanganwadi', () => {
       it('Edit Aanganwadi', () => {
         cy.login('admin','admin')
         cy.visit('/aanganwadis');
         cy.get('#editAanganwadi').click();
  
         cy.get('#contactPersonName').clear({ force: true }).then(() => {
           cy.wait(100);
           cy.get('#contactPersonName').invoke('val', '').type(`${'Sarah Silverman'}`);        
         });
         cy.get('#location').clear({ force: true }).then(() => {
           cy.get('#location').invoke('val', '').type(`${'Bommannhalli'}`);
         });
         cy.get('#contactPersonPassword').clear({ force: true }).then(() => {
           cy.get('#contactPersonPassword').invoke('val', '').type(`${'P@ss123'}`);
         });
         
         cy.get('#updateAanganwadi').click();
         cy.visit('/aanganwadis');
       })
     });
  
   });