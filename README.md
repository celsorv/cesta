# Sistema web para organizar as doações de alimentos em uma igreja


<br>

## **Instalação e Setup**

### Rodando com docker
```
docker-compose up -d
```
### Rodando sem docker (é recomendado o uso de uma venv)
```
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver 0.0.0.0:8000
```

O website ficara aberto em localhost:8000

Para logar como admin, usar as credenciais:
```
admin@admin.com
admin12345
```

Para popular o banco com dados fake para testes, é possivel utilizar o comando (recomendado uso de venv):
```
python manage.py populate_database
```

O mesmo irá criar uma quantidade aleatória(entre 50 a 1500) de registros para usuários(doadores), doações agendadas e doações recebidas


## __UNIVESP__
Universidade Virtual do Estado de São Paulo

### Solução desenvolvida em Python e Django atendendo aos requisitos do Projeto Integrador I

[YOUTUBE: Vídeo explicativo da solução e as tecnologias empregadas](https://www.youtube.com/watch?v=YxeufeAI6jA)

<!-- ![tumbnail-PI-git](https://user-images.githubusercontent.com/73009024/146322712-105f7502-f54f-4c15-bc89-2e6a0fd42e87.jpg) -->



#### TODO:
- ZeroDivisionError/DivisionUndefined -> após finalizar uma doacao, a pagina esta quebrando