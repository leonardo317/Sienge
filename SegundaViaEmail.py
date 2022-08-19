import requests
import json
import BoletoMaisProximo, Validacao

url = "https://api.sienge.com.br/ng7demo/public/api/v1/payment-slip-notification/"

payload = json.dumps({
  "receivableBillId": f'{BoletoMaisProximo.billReceivableId}',
  "installmentId": f'{BoletoMaisProximo.installmentId}',
  "emailCustomer": f"{Validacao.email}",
  "emailTitle": "Segunda via ",
  "emailBody": "Segue a segunda via do seu boleto. Leonardo Amaral"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic bmc3ZGVtby1sZW9hbWFyYWw6V1FLaXF5NHdGNlJBVmRjekIxOHFUd2NwMHUyYk9adHo='
}

response = requests.request("POST", url, headers=headers, data=payload)

print('Boleto enviado')
