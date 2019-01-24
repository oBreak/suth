'''NOTE: If someone is trying to figure this out, do not use this source, as it doesn't work. I ended
up having to use curl -x post instead.'''

import requests

scanresults = []

def postHackTheBox():  # Things
    dest = 'url here'
    print(dest)
    payload = {'key': 'val'}
    contentType = "application/x-www-form-urlencoded"
    contentType2 = "'application/json'"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(dest)
    txt = r.text
    # scanresults.append(txt)
    print("BEGINNING OUTPUT")
    # print(r.method) <- not a thing

    print(r.status_code)
    print("BEGINNING RESPONSE")
    print(txt)
    return

postHackTheBox()

#print (scanresults)