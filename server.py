#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import parse_headers
import json
import os
import requests

key = os.environ['MG_KEY']
sandbox = 'sandboxc3791adbe2a945f5a6997005c4c6fdec.mailgun.org'
recipient = 'benjamin@moontowercider.com'
sender = 'postmaster@sandboxc3791adbe2a945f5a6997005c4c6fdec.mailgun.org'
request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)


def send(msg):
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



class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')

        origin = self.headers['Origin']
        sub = ''
        if 'www.moontowercider.com' in origin:
            sub = 'www.'
        self.send_header('Access-Control-Allow-Origin', 'http://{}moontowercider.com'.format(sub))
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.send_response(404)


    def do_POST(self):
        # Send response status code
        data_string = self.rfile.read(int(self.headers['Content-Length']))

        self._set_headers()
        self.send_response(200)
        self.wfile.write(b"thanks")

        try:
            msg = json.loads(str(data_string.decode('utf-8')))
        except:
            print('Error parsing message: {}'.format(data_string))

        try:
            send(msg)
        except:
            print('Error sending to mailgun')

def run():
    print('starting server...')

    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
