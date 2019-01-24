import requests

scanresults = []

def postHackTheBox():  # Things
    url1 = 'http://hackthebox.eu/api/invite/generate'
    # payload = {'key': 'val'}
    payload = {}
    headers = {}
    res = requests.post(url1, data=payload, headers=headers)
    txt = res.text
    scanresults.append(txt)
    return

postHackTheBox()

print (scanresults)