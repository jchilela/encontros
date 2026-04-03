import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  standalone: true,
  imports: [CommonModule],
  template: `
    <section class="page"><div class="container">
      <h1 class="section-title">Painel do organizador</h1>
      <div class="kpi-grid">
        <div class="card" style="padding:1rem;"><div class="muted">Eventos criados</div><strong>14</strong></div>
        <div class="card" style="padding:1rem;"><div class="muted">Participantes</div><strong>1 284</strong></div>
        <div class="card" style="padding:1rem;"><div class="muted">Receita</div><strong>€ 12 800</strong></div>
        <div class="card" style="padding:1rem;"><div class="muted">Grupos geridos</div><strong>3</strong></div>
      </div>
    </div></section>
  `
})
export class OrganizerDashboardPageComponent {}
