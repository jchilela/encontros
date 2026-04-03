import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  standalone: true,
  imports: [CommonModule],
  template: `
    <section class="page"><div class="container">
      <h1 class="section-title">Notificações</h1>
      <div class="card" style="padding:1rem; display:grid; gap:.75rem;">
        <div class="card" style="padding:1rem;">O teu plano Silver renova em 7 dias.</div>
        <div class="card" style="padding:1rem;">Abriram novas vagas no evento Cloud & Data Lisboa.</div>
        <div class="card" style="padding:1rem;">O organizador enviou um anúncio ao grupo Cloud Luanda.</div>
      </div>
    </div></section>
  `
})
export class NotificationsPageComponent {}
