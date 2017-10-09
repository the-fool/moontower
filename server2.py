from flask import Flask, request, Response

import json
import os
import requests

key = os.environ['MG_KEY']
sandbox = 'sandboxc3791adbe2a945f5a6997005c4c6fdec.mailgun.org'
recipient = 'benjamin@moontowercider.com'
sender = 'postmaster@sandboxc3791adbe2a945f5a6997005c4c6fdec.mailgun.org'
request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)

app = Flask(__name__)


def send_to_mg(msg):
    request = requests.post(
        request_url,
        auth=('api', key),
        data={
            'from': sender,
            'to': recipient,
            'subject': 'MTC Mail',
            'text': str(msg)
        })
    print('Status: {0}'.format(request.status_code))
    print('Body:   {0}'.format(request.text))


@app.route('/', methods=['POST'])
def main():
    print(request.form, request.get_json())
    resp = Response('')
    origin = request.environ.get('HTTP_ORIGIN', '')
    sub = ''
    if 'www.moontowercider.com' in origin:
        sub = 'www.'
    resp.headers['Access-Control-Allow-Origin'] = 'http://{}moontowercider.com'.format(sub)
    return resp
    """
    try:
        msg = json.loads(str(data_string.decode('utf-8')))
    except:
        print('Error parsing message: {}'.format(data_string))

    try:
        send(msg)
    except:
        print('Error sending to mailgun')

    """
