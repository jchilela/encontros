import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  standalone: true,
  imports: [CommonModule],
  template: `
    <section class="page"><div class="container">
      <h1 class="section-title">Dashboard do membro</h1>
      <div class="kpi-grid">
        <div class="card" style="padding:1rem;"><div class="muted">Plano atual</div><strong>Silver</strong></div>
        <div class="card" style="padding:1rem;"><div class="muted">Próxima cobrança</div><strong>18 Jul 2026</strong></div>
        <div class="card" style="padding:1rem;"><div class="muted">Eventos inscritos</div><strong>12</strong></div>
        <div class="card" style="padding:1rem;"><div class="muted">Grupos aderidos</div><strong>7</strong></div>
      </div>
    </div></section>
  `
})
export class MemberDashboardPageComponent {}
