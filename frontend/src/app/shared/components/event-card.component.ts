import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-event-card',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <article class="card" style="overflow:hidden;">
      <div style="height: 180px; background: linear-gradient(135deg, #7c3aed, #06b6d4);"></div>
      <div style="padding: 1rem; display:grid; gap:.65rem;">
        <div class="muted">{{ category }} · {{ city }}</div>
        <h3 style="margin:0; font-size:1.1rem;">{{ title }}</h3>
        <div class="muted">{{ date }}</div>
        <div style="display:flex; justify-content:space-between; align-items:center; gap:1rem;">
          <strong>{{ price }}</strong>
          <a [routerLink]="['/eventos', slug]" class="btn btn-primary">Ver evento</a>
        </div>
      </div>
    </article>
  `
})
export class EventCardComponent {
  @Input() title = '';
  @Input() slug = '';
  @Input() city = '';
  @Input() category = '';
  @Input() date = '';
  @Input() price = '';
}
