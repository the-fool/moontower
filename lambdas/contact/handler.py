import requests
import os

def pretty(kind, name, email, message):
    return """
    kind: {0}

    name: {1}

    email: {2}

    message: 
    {3}
    """.format(kind, name, email, message)


def lambda_handler(event, context):
    name = event['name']
    message = event['message']
    kind = event['kind']
    email = event['email']

    msg = pretty(kind, name, email, message)

    mg_key = os.environ['MG_KEY']

    sandbox = 'sandboxc3791adbe2a945f5a6997005c4c6fdec.mailgun.org'
    recipient = 'benjamin@moontowercider.com, justin@moontowercider.com'
    sender = 'postmaster@sandboxc3791adbe2a945f5a6997005c4c6fdec.mailgun.org'
    request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)

    res = requests.post(request_url,
                  auth=('api', mg_key),
                  data={
                      'from': sender,
                      'to': recipient,
                      'subject': 'MTC Mail',
                      'text': str(msg)
                  })


    if res.status_code is not 200:
        raise Exception('{0}: {1}'.format(res.status_code, res.text))

    return res.status_code
