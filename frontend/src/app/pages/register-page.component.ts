import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <section class="page"><div class="container" style="max-width:640px;">
      <form class="card form-grid" style="padding:1.2rem;">
        <h1 style="margin:0;">Registo</h1>
        <label class="field"><span>Nome</span><input></label>
        <label class="field"><span>Email</span><input type="email"></label>
        <label class="field"><span>Palavra-passe</span><input type="password"></label>
        <button class="btn btn-primary" type="button">Criar conta</button>
      </form>
    </div></section>
  `
})
export class RegisterPageComponent {}
