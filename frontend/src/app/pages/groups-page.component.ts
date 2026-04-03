import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <section class="page">
      <div class="container">
        <div style="display:flex; justify-content:space-between; align-items:center; gap:1rem; flex-wrap:wrap;">
          <h1 class="section-title">Grupos</h1>
          <a routerLink="/organizador" class="btn btn-primary">Criar grupo</a>
        </div>
        <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
          <a routerLink="/grupos/cloud-luanda" class="card" style="padding:1rem; display:grid; gap:.75rem;">
            <strong>Cloud Luanda</strong>
            <span class="muted">Infraestrutura, cloud e comunidade técnica.</span>
            <span>1 240 membros</span>
          </a>
          <a routerLink="/grupos/design-sp" class="card" style="padding:1rem; display:grid; gap:.75rem;">
            <strong>Design SP</strong>
            <span class="muted">UX, UI e produto.</span>
            <span>950 membros</span>
          </a>
        </div>
      </div>
    </section>
  `
})
export class GroupsPageComponent {}
