import configparser
import requests
import base64
import os
import sys



conf = configparser.ConfigParser()
conf.read('conf/conf.ini')

twconsumer_key        = conf['twitter-consumer-api-key']['value']
twconsumer_secret     = conf['twitter-consumer-secret']['value']
twaccesstoken         = conf['twitter-access-token']['value']
twaccesstokensecret   = conf['twitter-access-token-secret']['value']

print(twconsumer_key)
print(twconsumer_secret)
print(twaccesstoken)
print(twaccesstokensecret)

# base64 encode the consumer key:secret pair
key_secret          = base64.urlsafe_b64encode('{}:{}'.format(twconsumer_key, twconsumer_secret).encode('UTF-8')).decode('UTF-8')

# set the url
base_url            = 'https://api.twitter.com/'
auth_url            = '{}oauth2/token'.format(base_url)

# set auth headers
auth_headers = {
    'Authorization': 'Basic {}'.format(key_secret),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
if auth_resp.status_code == 200:
    print('200 code response!')
    print('Operation successful retrieval of bearer token.')
    bearer_token = auth_resp.json()['access_token']