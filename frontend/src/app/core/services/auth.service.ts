import { inject, Injectable, signal } from '@angular/core';
import { tap } from 'rxjs/operators';
import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private api = inject(ApiService);
  user = signal<{email: string; role: string} | null>(null);

  login(payload: {email: string; password: string}) {
    return this.api.post<{access: string; refresh: string; user: {email: string; role: string}}>('/auth/login/', payload).pipe(
      tap((response) => {
        localStorage.setItem('access_token', response.access);
        localStorage.setItem('refresh_token', response.refresh);
        this.user.set(response.user);
      })
    );
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.user.set(null);
  }
}
