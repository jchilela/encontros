import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <section class="page"><div class="container">
      <h1 class="section-title">Perfil</h1>
      <form class="card form-grid" style="padding:1.2rem; max-width: 720px;">
        <label class="field"><span>Nome</span><input value="Pamela"></label>
        <label class="field"><span>Bio</span><textarea rows="4">Apaixonada por comunidades e tecnologia.</textarea></label>
        <label class="field"><span>Cidade</span><input value="Luanda"></label>
        <button class="btn btn-primary" type="button">Guardar alterações</button>
      </form>
    </div></section>
  `
})
export class ProfilePageComponent {}
