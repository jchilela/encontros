import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <section class="page">
      <div class="container two-col">
        <form class="card form-grid" style="padding:1.2rem;">
          <h1 style="margin:0;">Checkout</h1>
          <label class="field"><span>Nome no bilhete</span><input></label>
          <label class="field"><span>Email</span><input type="email"></label>
          <label class="field"><span>Método de pagamento</span>
            <select [(ngModel)]="provider" name="provider">
              <option value="stripe">Stripe</option>
              <option value="paypal">PayPal</option>
              <option value="proprietary">Referência proprietária</option>
            </select>
          </label>
          <button class="btn btn-primary" type="button">Pagar agora</button>
        </form>
        <aside class="card" style="padding:1.2rem; display:grid; gap:1rem; align-self:start;">
          <h3 style="margin:0;">Resumo</h3>
          <div style="display:flex; justify-content:space-between;"><span>Bilhete Early Bird</span><strong>€ 40</strong></div>
          <div style="display:flex; justify-content:space-between;"><span>Desconto Silver</span><strong>- € 4</strong></div>
          <div style="display:flex; justify-content:space-between;"><span>Taxas</span><strong>€ 2</strong></div>
          <hr style="border-color: rgba(255,255,255,.08); width:100%;">
          <div style="display:flex; justify-content:space-between;"><span>Total</span><strong>€ 38</strong></div>
        </aside>
      </div>
    </section>
  `
})
export class CheckoutPageComponent { provider = 'stripe'; }
