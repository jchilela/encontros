import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-site-header',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  template: `
    <header class="container" style="padding: 1rem 0; position: sticky; top: 0; z-index: 10; backdrop-filter: blur(18px);">
      <div class="card" style="padding: .9rem 1rem; display:flex; align-items:center; justify-content:space-between; gap:1rem;">
        <a routerLink="/" style="font-weight:900; letter-spacing:.02em;">Comunidade+</a>
        <nav class="toolbar">
          <a routerLink="/explorar" routerLinkActive="active">Explorar eventos</a>
          <a routerLink="/grupos" routerLinkActive="active">Grupos</a>
          <a routerLink="/planos" routerLinkActive="active">Ver planos</a>
          <a routerLink="/organizador" routerLinkActive="active">Organizador</a>
          <a routerLink="/admin" routerLinkActive="active">Admin</a>
          <a routerLink="/login" class="btn btn-secondary">Login</a>
        </nav>
      </div>
    </header>
  `
})
export class SiteHeaderComponent {}
