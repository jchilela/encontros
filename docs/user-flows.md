# Fluxos principais

## 1. Registo + onboarding
1. Utilizador cria conta.
2. Recebe email de verificação.
3. Define cidade, interesses e preferências.
4. Sistema mostra eventos e grupos recomendados.

## 2. RSVP gratuito
1. Utilizador entra no detalhe do evento.
2. Clica em **Confirmar presença**.
3. Sistema valida plano, limite e lotação.
4. Gera RSVP ou entrada em lista de espera.
5. Envia notificação in-app e email.

## 3. Compra de bilhete
1. Utilizador escolhe lote.
2. Checkout calcula preço, desconto, comissão e moeda.
3. Pagamento é executado via Stripe, PayPal ou gateway proprietário.
4. Pedido é confirmado.
5. Bilhete e QR code são emitidos.

## 4. Subscrição Silver/Gold
1. Utilizador abre **Ver planos**.
2. Escolhe ciclo trimestral, semestral ou anual.
3. Efetua pagamento.
4. Plano entra em vigor imediatamente.
5. Em upgrade, aplica-se prorrata.
6. Em downgrade, agenda-se para o próximo ciclo.

## 5. Espera automática
1. Evento enche.
2. Próximos interessados entram na lista de espera.
3. Quando abre vaga, sistema promove utilizador por prioridade do plano e ordem temporal.
4. Utilizador recebe aviso com tempo limite para concluir confirmação, quando aplicável.

## 6. Check-in
1. Membro apresenta QR code.
2. Organizador lê código ou faz check-in manual.
3. Sistema grava presença e alimenta analytics.
