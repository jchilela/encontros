import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  standalone: true,
  imports: [CommonModule],
  template: `
    <section class="page"><div class="container two-col">
      <aside class="card" style="padding:1rem;"><strong>Conversas</strong><p class="muted">Organizador · Encontro Tech Luanda</p></aside>
      <div class="card" style="padding:1rem;"><strong>Mensagens</strong><p class="muted">Olá! Tens alguma questão sobre o evento?</p></div>
    </div></section>
  `
})
export class MessagesPageComponent {}
