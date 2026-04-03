import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { PlanCardComponent } from '../shared/components/plan-card.component';

@Component({
  standalone: true,
  imports: [CommonModule, PlanCardComponent],
  template: `
    <section class="page"><div class="container">
      <h1 class="section-title">Planos e subscrições</h1>
      <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
        <app-plan-card name="Gratuito" price="0 €" [features]="['Pesquisa de eventos', 'Participação em alguns eventos gratuitos', 'Mensagens limitadas']" cta="Ativar" />
        <app-plan-card name="Silver" price="€ 19 trimestral" [features]="['Acesso ampliado', 'Descontos em eventos', 'Grupos exclusivos Silver', 'Prioridade intermédia']" />
        <app-plan-card name="Gold" price="€ 39 trimestral" [features]="['Acesso premium completo', 'Eventos exclusivos Gold', 'Prioridade máxima', 'Suporte prioritário']" />
      </div>
    </div></section>
  `
})
export class PlansPageComponent {}
