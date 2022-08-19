import requests
import BoletoMaisProximo


url = f"https://api.sienge.com.br/ng7demo/public/api/v1/payment-slip-notification/?billReceivableId={BoletoMaisProximo.billReceivableId}&installmentId={BoletoMaisProximo.installmentId}"

headers = {
  'Content-Type': 'application/json',
  'Content-Type': 'Accept',
  'Authorization': 'Basic bmc3ZGVtby1sZW9hbWFyYWw6V1FLaXF5NHdGNlJBVmRjekIxOHFUd2NwMHUyYk9adHo='
}

response = requests.request("GET", url, headers=headers)

r = response.json()
url = r['results'][0]['urlReport']
print(f'O link do seu boleto é: {url}')
