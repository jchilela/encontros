import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-plan-card',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article class="card" style="padding:1.2rem; display:grid; gap:1rem;">
      <div>
        <div class="muted">Plano</div>
        <h3 style="margin:.25rem 0 0;">{{ name }}</h3>
      </div>
      <div style="font-size:2rem; font-weight:800;">{{ price }}</div>
      <ul style="margin:0; padding-left:1rem; display:grid; gap:.45rem;">
        <li *ngFor="let item of features">{{ item }}</li>
      </ul>
      <button class="btn btn-primary">{{ cta }}</button>
    </article>
  `
})
export class PlanCardComponent {
  @Input() name = '';
  @Input() price = '';
  @Input() cta = 'Atualizar plano';
  @Input() features: string[] = [];
}
