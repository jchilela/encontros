import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  standalone: true,
  imports: [CommonModule],
  template: `
    <section class="page">
      <div class="container two-col">
        <div class="card" style="padding:1.2rem; display:grid; gap:1rem;">
          <h1 style="margin:0;">Cloud Luanda</h1>
          <p class="muted">Grupo público focado em cloud, networking, data e comunidades técnicas.</p>
          <div class="toolbar">
            <button class="btn btn-primary">Entrar no grupo</button>
            <button class="btn btn-secondary">Partilhar</button>
          </div>
          <div class="card" style="padding:1rem;">
            <h3>Próximos eventos</h3>
            <p class="muted">Encontro Tech Luanda · 12 Mai 2026</p>
          </div>
          <div class="card" style="padding:1rem;">
            <h3>Discussões</h3>
            <p class="muted">Que temas querem ver no próximo meetup?</p>
          </div>
        </div>
        <aside class="card" style="padding:1.2rem; align-self:start;">
          <div class="kpi-grid">
            <div class="card" style="padding:1rem;"><div class="muted">Membros</div><strong>1 240</strong></div>
            <div class="card" style="padding:1rem;"><div class="muted">Organizadores</div><strong>4</strong></div>
            <div class="card" style="padding:1rem;"><div class="muted">Plano</div><strong>Aberto</strong></div>
          </div>
        </aside>
      </div>
    </section>
  `
})
export class GroupDetailPageComponent {}
