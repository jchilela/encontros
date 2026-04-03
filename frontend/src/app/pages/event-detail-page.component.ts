import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  standalone: true,
  imports: [CommonModule],
  template: `
    <section class="page">
      <div class="container two-col">
        <div class="card" style="overflow:hidden;">
          <div style="height:280px; background: linear-gradient(135deg, #7c3aed, #06b6d4);"></div>
          <div style="padding:1.2rem; display:grid; gap:1rem;">
            <div class="muted">Tecnologia · Luanda · Presencial</div>
            <h1 style="margin:0;">Encontro Tech Luanda 2026</h1>
            <p class="muted">Talks, networking, startups, cloud e inteligência artificial.</p>
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));">
              <div class="card" style="padding:1rem;"><div class="muted">Data</div><strong>12 Mai 2026</strong></div>
              <div class="card" style="padding:1rem;"><div class="muted">Hora</div><strong>18:30</strong></div>
              <div class="card" style="padding:1rem;"><div class="muted">Participantes</div><strong>312</strong></div>
              <div class="card" style="padding:1rem;"><div class="muted">Lotação</div><strong>500</strong></div>
            </div>
            <div class="card" style="padding:1rem;">
              <h3>Descrição</h3>
              <p class="muted">Evento presencial voltado a tecnologia, networking e oportunidades de comunidade.</p>
            </div>
            <div class="card" style="padding:1rem;">
              <h3>Perguntas frequentes</h3>
              <p class="muted">Posso transferir o bilhete? Sim, até 24h antes do evento.</p>
            </div>
          </div>
        </div>
        <aside class="card" style="padding:1.2rem; display:grid; gap:1rem; align-self:start;">
          <div>
            <div class="muted">Preço</div>
            <div style="font-size:2rem; font-weight:800;">15 000 Kz</div>
          </div>
          <button class="btn btn-primary">Comprar bilhete</button>
          <button class="btn btn-secondary">Confirmar presença</button>
          <button class="btn btn-secondary">Guardar evento</button>
          <button class="btn btn-secondary">Falar com o organizador</button>
          <div class="card" style="padding:1rem;">
            <div class="muted">Política de cancelamento</div>
            <p>Reembolso até 7 dias antes do evento.</p>
          </div>
        </aside>
      </div>
    </section>
  `
})
export class EventDetailPageComponent {}
