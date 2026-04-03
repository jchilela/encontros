import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { EventCardComponent } from '../shared/components/event-card.component';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule, EventCardComponent],
  template: `
    <section class="page">
      <div class="container">
        <h1 class="section-title">Explorar eventos</h1>
        <div class="card" style="padding:1rem; margin-bottom:1rem;">
          <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));">
            <label class="field"><span>Palavra-chave</span><input [(ngModel)]="q" placeholder="Pesquisar eventos"></label>
            <label class="field"><span>Cidade</span><select [(ngModel)]="city"><option value="">Todas</option><option>Luanda</option><option>Lisboa</option><option>São Paulo</option></select></label>
            <label class="field"><span>Categoria</span><select [(ngModel)]="category"><option value="">Todas</option><option>Tecnologia</option><option>Design</option><option>Negócios</option></select></label>
            <label class="field"><span>Formato</span><select [(ngModel)]="format"><option value="">Todos</option><option>presencial</option><option>online</option><option>híbrido</option></select></label>
          </div>
        </div>
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
          <app-event-card title="Encontro Tech Luanda" slug="encontro-tech-luanda" city="Luanda" category="Tecnologia" date="12 Mai 2026" price="15 000 Kz" />
          <app-event-card title="UX Meetup São Paulo" slug="ux-meetup-sp" city="São Paulo" category="Design" date="20 Mai 2026" price="R$ 120" />
          <app-event-card title="Cloud & Data Lisboa" slug="cloud-data-lisboa" city="Lisboa" category="Cloud" date="05 Jun 2026" price="€ 40" />
          <app-event-card title="Masterclass Online de Produto" slug="produto-online" city="Online" category="Produto" date="14 Jun 2026" price="$ 25" />
        </div>
      </div>
    </section>
  `
})
export class ExplorePageComponent { q=''; city=''; category=''; format=''; }
