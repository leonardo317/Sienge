import requests
import json

url = "https://api.sienge.com.br/ng7demo/public/api/v1/customers?cpf=54316545434"

payload = ""
headers = {
  'Content-Type': 'Accept',
  'Content-Type': 'application/json',
  'Authorization': 'Basic bmc3ZGVtby1sZW9hbWFyYWw6V1FLaXF5NHdGNlJBVmRjekIxOHFUd2NwMHUyYk9adHo='
}

response = requests.request("GET", url, headers=headers, data=payload)

r = response.json()
id = r['results'][0]['id']

email = r['results'][0]['email']

