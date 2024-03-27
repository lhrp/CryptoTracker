from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os


#url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
url =  'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

parameters = {
  'id' : '12252',
  'convert':'BRL',
  'amount':'1'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '4c65c391-1548-43f2-a9b1-c958be04ef8d',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)

    # print('--------BOMB 1-----------')
    # print(data['data']['12252']['name'])
    # print(data['data']['12252']['symbol'])
    # print(data['data']['12252']['platform']['token_address'])
    # print(data['data']['12252']['platform']['name'])
    # print(data['data']['12252']['platform']['symbol'])
    # print(round(data['data']['12252']['quote']['BRL']['price'], 4))   
    # print('--------BOMB 2-----------')
    # print(data['data']['20921']['name'])
    # print(data['data']['20921']['symbol'])
    # print(data['data']['20921']['platform']['token_address'])
    # print(data['data']['20921']['platform']['name'])
    # print(data['data']['20921']['platform']['symbol'])
    # print(round(data['data']['20921']['quote']['BRL']['price'], 4)) 


except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)