import requests
import Validacao
from datetime import date

data = date.today()

year = data.year
month = data.month

url = f"https://api.sienge.com.br/ng7demo/public/api/v1/customer-financial-statements?customerId={Validacao.id}"

payload={}
headers = {
  'Authorization': 'Basic bmc3ZGVtby1sZW9hbWFyYWw6V1FLaXF5NHdGNlJBVmRjekIxOHFUd2NwMHUyYk9adHo='
}

r = requests.request("GET", url, headers=headers, data=payload)

r = r.json()




billReceivableId = r['results'][0]['billsReceivable'][0]['billReceivableId']



r = r['results'][0]['billsReceivable'][0]['installments']


qntd = len(r)

for c in range(0, qntd):
  resultado = r[c]
  if int(resultado['dueDate'][0:4]) == year:
    if int(resultado['dueDate'][5:7]) == month:

      
      installmentId = resultado['installmentId']

      if resultado['generatedBillet'] == True:
        Ok = 'True'


      else:
        Ok = 'False'

