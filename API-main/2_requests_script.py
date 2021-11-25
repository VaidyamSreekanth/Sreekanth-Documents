import requests

## To get all customers details
res_obj = requests.get('http://127.0.0.1:5000/get')

## If Credentials required
#res = requests.get('http://127.0.0.1:5000/login', auth=HTTPBasicAuth('uname', 'password'))

print('\n response code is  :', res_obj.status_code)
print('\n CUST details are  :', res_obj.json())

## To create new customer record
r = requests.post('http://127.0.0.1:5000/create', json={"cust3":"SRI"})
print('\n response code is :', r.status_code)
print('\n response DATA is :', r.json())

## To Update emp 
r = requests.put('http://127.0.0.1:5000/update', json={"cust2":"Ramesh"})
print('\n response code is :', r.status_code)
print('\n update is :', r.text)


## To Delete emp
r = requests.delete('http://127.0.0.1:5000/delete', json={"cust2":"Ramesh"})
print('\n response code is :', r.status_code)
print('\n Deleted is :', r.text)

