#!/usr/bin/python
# coding: utf-8

import thread
import urllib
import urlparse
import warnings
import webbrowser
import BaseHTTPServer
import json
import facebook


# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)

class FacebookConnection(object):
    # Create a connection object
    def __init__(self):
        self.app_id = '394484357378910'
        self.app_secret = 'bafe107033d99381f63cfc97ffade902'
        self.client_token = '56b8254aa1680260ed1c9b5e81c0fee0'
        self.profile = json.load(urllib.urlopen('http://graph.facebook.com/nicolas.grislain'))
        self.port = 8910
        self.oauth_args = dict(client_id=self.app_id, client_secret=self.app_secret,
                          redirect_uri='http://127.0.0.1:{}/'.format(self.port))
    # Login 
    def login(self):
        def set_code(code):
            self.oauth_args['code'] = code
        # Define a local server to get the redirect
        class HTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
            def do_GET(self):
                query = urlparse.parse_qs(urlparse.urlparse(self.path).query)
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write("Authentication successful\n")
                self.wfile.write(json.dumps(query))
                if 'code' in query:
                    set_code(query['code'][0])
        httpd = BaseHTTPServer.HTTPServer(('', self.port), HTTPRequestHandler)
        webbrowser.open('https://www.facebook.com/dialog/oauth?'+urllib.urlencode(self.oauth_args))
        httpd.handle_request()
        self.access_token = urlparse.parse_qs(urllib.urlopen('https://graph.facebook.com/oauth/access_token?'+urllib.urlencode(self.oauth_args)).read())['access_token'][0]
    
fc = FacebookConnection()
fc.login()
 
facebook_graph = facebook.GraphAPI(fc.access_token)
profile = facebook_graph.get_object('me')
friends = facebook_graph.get_connections('me', 'friends')

friend_list = [friend['name'] for friend in friends['data']]

print friend_list
