# Comunidade+ — plataforma de eventos e comunidades em português

Monorepo inicial pronto para evolução, com:

- **Frontend:** Angular 21, standalone components, SCSS, layout mobile-first.
- **Backend:** Django 6 + Django REST Framework 3.16.
- **Base de dados:** PostgreSQL.
- **Cache / filas curtas / notificações:** Redis.
- **Pesquisa:** Meilisearch.
- **Uploads:** armazenamento S3-compatible (MinIO no ambiente local).
- **Pagamentos:** Stripe, PayPal e gateway proprietário por callback.
- **Mapas:** Mapbox.
- **Deploy:** Docker Compose + Nginx.

## Estrutura

```text
backend/   API Django REST
frontend/  SPA Angular
infra/     Docker, Nginx, env examples
docs/      Arquitetura, fluxos, permissões, APIs, roadmap, monetização
```

## Módulos de negócio

- Autenticação e perfis
- Eventos, grupos e RSVPs
- Bilhetes, pedidos, pagamentos e reembolsos
- Planos Gratuito, Silver e Gold
- Mensagens, notificações e moderação
- Dashboards de membro, organizador e administrador

## Execução local

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2) Frontend

```bash
cd frontend
npm install
npm start
```

### 3) Stack local opcional com Docker

```bash
cd infra
cp .env.example .env
docker compose up -d --build
```

## Produção no Ubuntu

1. Criar utilizador de deploy e **desativar SSH por root**.
2. Configurar domínio e TLS.
3. Preencher `.env` com chaves reais (Stripe, PayPal, SMTP, OAuth, S3, Mapbox).
4. Fazer build do frontend e servir estático via Nginx.
5. Servir o backend com Gunicorn + Nginx.
6. Agendar jobs recorrentes para expiração, reminders e reconciliação de pagamentos.

## Estado desta entrega

Esta entrega inclui uma base sólida de produto, arquitetura, modelo de dados, permissões, rotas, APIs iniciais, dashboards e estrutura de código pronta para expansão. Alguns fluxos avançados (websocket em tempo real, antifraude avançado, billing prorrata detalhado, push mobile nativo e reconciliação financeira profunda) estão documentados e parcialmente preparados, mas exigem integração com credenciais e infra reais para ficarem 100% operacionais.
