import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../core/services/auth.service';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <section class="page"><div class="container" style="max-width:540px;">
      <form class="card form-grid" style="padding:1.2rem;" (ngSubmit)="submit()">
        <h1 style="margin:0;">Login</h1>
        <label class="field"><span>Email</span><input [(ngModel)]="email" name="email" type="email"></label>
        <label class="field"><span>Palavra-passe</span><input [(ngModel)]="password" name="password" type="password"></label>
        <button class="btn btn-primary" type="submit">Entrar</button>
      </form>
    </div></section>
  `
})
export class LoginPageComponent {
  private auth = inject(AuthService);
  email = '';
  password = '';
  submit() { this.auth.login({ email: this.email, password: this.password }).subscribe(); }
}
