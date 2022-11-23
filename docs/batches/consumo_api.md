
# Consumo da API com o comando Curl

## Obter um token
### _Resultado é gravado no arquivo res.json_

```bat
@echo off

set user=usuario@email.com
set pass=senha_usuario

curl -X POST -o res.json -d "username=%user%&password=%pass%" https://celsorv.pythonanywhere.com/api/token/

```
  

## Obter os produtos de um dado grupo

```bat
@echo off

set token=access_token_arquivo_res_json
set id_grupo_pesquisa=4

curl -X GET -H "Content-Type:application/json" -H "Authorization: Bearer %token%" https://celsorv.pythonanywhere.com/api/v1/doacao/grupo/%id_grupo_pesquisa%

```

## Obter o mapa das doações

```bat

@echo off

set token=access_token_arquivo_res_json

curl -X GET -H "Content-Type:application/json" -H "Authorization: Bearer %token%" https://celsorv.pythonanywhere.com/api/v1/doacao/
```


## Registrar uma doação

```bat

@echo off

set token=access_token_arquivo_res_json
set id_grupo_produto=2

curl -d "{\"produto\":2,\"quantidade\":1}" -H "Content-Type:application/json" -H "Authorization: Bearer %token%" https://celsorv.pythonanywhere.com/api/v1/doacao/doar/%id_grupo_produto%
```