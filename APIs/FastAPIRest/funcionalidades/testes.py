#Teste de requisição
import requests

headers = {
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwiZXhwIjoxNzk1MDMzNjk2fQ.FARWlkNlwDO4Cj3Dxgq0tzE5n755vMzr6Ahu4c4Qkvs"
}
requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())