# Ambiente de Testes Django

- Docker
- Nginx
- Postgresql
- Cron

## DOCKER

Copiar arquivos de configuração

```
cp .env.example .env
cp .env.prod.example .env.prod
cp .env.prod.db.example .env.prod.db


```

Execute
`
docker-compose up -d
`

Realização migração e criar super usuario

```
docker-compose exec web python manage.py migrate 
docker-compose exec web python manage.py createsuperuser
```

Acesse
`http://django.localtest.me/`