
@echo off

set user=paulo@gmail.com
set pass=teste@teste

curl -X POST -o res.json -d "username=%user%&password=%pass%" https://celsorv.pythonanywhere.com/api/token/