# Arquitetura do produto

## Stack escolhida

- **Frontend:** Angular 21, standalone, routing, HTTP client, guards, interceptors.
- **Backend:** Django 6, Django REST Framework 3.16, JWT, OAuth social.
- **DB:** PostgreSQL.
- **Cache/Jobs:** Redis + Celery.
- **Pesquisa:** Meilisearch.
- **Armazenamento:** S3-compatible.
- **Tempo real:** Django Channels ou serviço dedicado numa fase 2.
- **Pagamentos:** Stripe, PayPal e gateway proprietário por callback assinado.
- **Observabilidade:** Sentry, Prometheus, Grafana.

## Arquitetura lógica

```text
Angular Web
  ├─ Área pública
  ├─ Área do membro
  ├─ Área do organizador
  └─ Área do administrador
        |
        v
API Gateway / Nginx
        |
        v
Django REST API
  ├─ auth
  ├─ users
  ├─ taxonomy
  ├─ communities
  ├─ events
  ├─ tickets
  ├─ subscriptions
  ├─ payments
  ├─ messaging
  ├─ notifications
  ├─ moderation
  └─ dashboards
        |
        ├─ PostgreSQL
        ├─ Redis
        ├─ Meilisearch
        ├─ MinIO / S3
        ├─ SMTP
        ├─ Stripe / PayPal
        └─ Gateway proprietário + callbacks
```

## Decisões de produto

### 1. Planos de membro
- **Sem pacote pago**: estado base sem benefícios premium.
- **Gratuito**: plano gratuito com limites controlados.
- **Silver**: descontos, acesso prioritário e grupos/eventos exclusivos.
- **Gold**: experiência premium completa.

### 2. Organização de permissões
- `visitor`
- `member`
- `organizer`
- `coorganizer`
- `moderator`
- `support`
- `admin`

### 3. Estratégia de pagamentos
- Bilhetes e subscrições usam a mesma infraestrutura de pedidos.
- Cada pagamento gera uma transação, reconciliação e eventos de auditoria.
- O gateway proprietário usa **código de referência** + **callback seguro**.

### 4. Escalabilidade
- Pesquisa separada em Meilisearch.
- Redis para cache, rate limit e tasks.
- Possibilidade de separar leitura/escrita e serviços por domínio.

## Segurança

- JWT + refresh token em cookies seguros ou armazenamento seguro no cliente.
- CSRF quando aplicável.
- rate limit por IP e por utilizador.
- verificação de email obrigatória.
- MFA opcional.
- logs de auditoria.
- webhooks com assinatura.
- RBAC por perfis e ownership por recurso.
- isolamento entre áreas admin / organizer / member.

## Jobs assíncronos previstos

- envio de email de verificação
- recuperação de password
- lembrete pré-evento
- promoção da lista de espera
- renovação de subscrição
- downgrade agendado
- reprocessamento de callbacks de pagamento
- geração de relatórios
- sincronização com motor de pesquisa
