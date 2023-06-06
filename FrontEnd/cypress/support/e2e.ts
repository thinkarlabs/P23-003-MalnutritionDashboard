// ***********************************************************
// This example support/index.js is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands'

// Global Declaration for Login Method for Cypress test
declare global {
    namespace Cypress {
      // noinspection JSUnusedGlobalSymbols
      interface Chainable {
        login(): void
      }
    }
  }

  Cypress.Commands.add('login', (username, password) => {
    cy.visit('/')
    cy.get('[type="text"]').type(username)
    cy.get('[type="password"]').type(password)
    cy.get('#login').click()
  });
  

  // This is in place to catch the exception while testing log out in Cypress 
  Cypress.on('uncaught:exception', (err, runnable) => {
    // returning false here prevents Cypress from failing the test
    return false
  })
  

// Alternatively you can use CommonJS syntax:
// require('./commands')
