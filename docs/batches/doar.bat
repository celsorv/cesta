
@echo off

set token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5MTk3OTIzLCJpYXQiOjE2NjkxOTQzMjMsImp0aSI6ImZmZjdkYzczMWFkMDQ5NjFhYTg3Y2U1NzhlMzQ0YzdiIiwidXNlcl9pZCI6MTJ9.d0wqivShl3g30PMhgJoobDehcTM8ETAgx-0pvjXtfGU
set id_grupo_produto=2

curl -d "{\"produto\":2,\"quantidade\":1}" -H "Content-Type:application/json" -H "Authorization: Bearer %token%" https://celsorv.pythonanywhere.com/api/v1/doacao/doar/%id_grupo_produto%