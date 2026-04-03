import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { EventCardComponent } from '../shared/components/event-card.component';
import { PlanCardComponent } from '../shared/components/plan-card.component';

@Component({
  standalone: true,
  imports: [CommonModule, RouterLink, EventCardComponent, PlanCardComponent],
  template: `
    <section class="hero page">
      <div class="container two-col">
        <div class="card" style="padding:1.4rem; display:grid; gap:1rem;">
          <span class="muted">Eventos, comunidades e subscrições em português</span>
          <h1 style="font-size: clamp(2rem, 5vw, 4rem); margin:0;">Descobre eventos, entra em grupos e cresce com a tua comunidade.</h1>
          <p class="muted">Pesquisa por cidade, categoria e data. Compra bilhetes, confirma presença, fala com organizadores e gere o teu plano Silver ou Gold.</p>
          <div class="toolbar">
            <a routerLink="/explorar" class="btn btn-primary">Explorar eventos</a>
            <a routerLink="/planos" class="btn btn-secondary">Ver planos</a>
          </div>
        </div>
        <div class="card" style="padding:1.2rem; display:grid; gap:1rem;">
          <div class="kpi-grid">
            <div class="card" style="padding:1rem;"><div class="muted">Eventos ativos</div><strong style="font-size:1.8rem;">1 284</strong></div>
            <div class="card" style="padding:1rem;"><div class="muted">Grupos</div><strong style="font-size:1.8rem;">368</strong></div>
            <div class="card" style="padding:1rem;"><div class="muted">Membros Gold</div><strong style="font-size:1.8rem;">1 902</strong></div>
          </div>
          <div class="card" style="padding:1rem;">
            <div class="muted">Próximo destaque</div>
            <h3>Encontro Tech Luanda 2026</h3>
            <p class="muted">Presencial · Luanda · Networking, talks e startups.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="page">
      <div class="container">
        <h2 class="section-title">Eventos em destaque</h2>
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
          <app-event-card title="Encontro Tech Luanda" slug="encontro-tech-luanda" city="Luanda" category="Tecnologia" date="12 Mai 2026" price="15 000 Kz" />
          <app-event-card title="UX Meetup São Paulo" slug="ux-meetup-sp" city="São Paulo" category="Design" date="20 Mai 2026" price="R$ 120" />
          <app-event-card title="Cloud & Data Lisboa" slug="cloud-data-lisboa" city="Lisboa" category="Cloud" date="05 Jun 2026" price="€ 40" />
        </div>
      </div>
    </section>

    <section class="page">
      <div class="container">
        <h2 class="section-title">Planos de membro</h2>
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
          <app-plan-card name="Gratuito" price="0 €" [features]="['Exploração básica', 'RSVP limitado', 'Grupos limitados']" cta="Começar" />
          <app-plan-card name="Silver" price="€ 19 / trimestre" [features]="['Descontos em eventos', 'Prioridade intermédia', 'Grupos Silver']" />
          <app-plan-card name="Gold" price="€ 39 / trimestre" [features]="['Eventos exclusivos', 'Prioridade máxima', 'Suporte prioritário']" />
        </div>
      </div>
    </section>
  `
})
export class HomePageComponent {}
