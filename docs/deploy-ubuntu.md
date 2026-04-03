# Deploy no Ubuntu (produção)

## 1. Pacotes base

```bash
apt update && apt upgrade -y
apt install -y python3 python3-venv python3-pip nginx postgresql postgresql-contrib redis-server git build-essential libpq-dev
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
npm install -g @angular/cli@21
```

## 2. PostgreSQL

```bash
sudo -u postgres psql
CREATE DATABASE comunidade;
CREATE USER comunidade WITH PASSWORD 'trocar-esta-password';
GRANT ALL PRIVILEGES ON DATABASE comunidade TO comunidade;
\q
```

## 3. Backend

```bash
mkdir -p /opt/comunidade
cd /opt/comunidade
# copiar pasta backend para aqui
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

## 4. Frontend

```bash
cd /opt/comunidade/frontend
npm install
ng build
mkdir -p /var/www/comunidade-frontend
cp -r dist/comunidade-frontend/browser/* /var/www/comunidade-frontend/
```

## 5. Gunicorn service

Criar `/etc/systemd/system/comunidade-backend.service`:

```ini
[Unit]
Description=Comunidade Backend
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/comunidade/backend
Environment="PATH=/opt/comunidade/backend/.venv/bin"
ExecStart=/opt/comunidade/backend/.venv/bin/gunicorn config.wsgi:application --bind 127.0.0.1:8000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl enable comunidade-backend
systemctl start comunidade-backend
systemctl status comunidade-backend
```

## 6. Nginx

```bash
cp /opt/comunidade/infra/nginx.conf /etc/nginx/sites-available/comunidade
ln -s /etc/nginx/sites-available/comunidade /etc/nginx/sites-enabled/comunidade
nginx -t
systemctl restart nginx
```

## 7. TLS

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d teu-dominio.com -d www.teu-dominio.com
```

## 8. Segurança mínima

- desativar login SSH por root
- usar utilizador administrativo próprio
- ativar UFW
- permitir apenas 22, 80 e 443
- colocar passwords e chaves reais no `.env`
- configurar backups da base de dados
