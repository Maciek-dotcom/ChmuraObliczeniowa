import http.server
import socketserver
from datetime import datetime
import pytz
import sys
import argparse
import json
import urllib.request


class ContainerBackendHandler(http.server.SimpleHTTPRequestHandler):

    def handle(self):
        
        clientIp = self.client_address[0]

        requestUrl = 'http://ip-api.com/json/'
        requestBody = urllib.request.Request(requestUrl + clientIp)
        responseHandler = urllib.request.urlopen(requestBody).read()
        jsonResponseFromGeoApi = json.loads(responseHandler.decode('utf-8'))
        loalDateAndTime = None
        try:
            clientTimezone = jsonResponseFromGeoApi['timezone']
            loalDateAndTime = datetime.now(pytz.timezone(clientTimezone)).strftime('%d-%m-%y %H:%M:%S')
        except:
            loalDateAndTime = datetime.now().strftime('%d-%m-%y %H:%M:%S')
 
        file = open("index.html", "w")
        file.write(f"""<!DOCTYPE html>
<html>
<body>
<h1><center>IP klienta:</center></h2>
<p><center>{clientIp}</center></p>
<h2><center>Data i godzina: </center></h2>
<p><center>{loalDateAndTime}</center></p>
</body>
</html>
"""
)
        file.close()
        return http.server.SimpleHTTPRequestHandler.handle(self)



parser = argparse.ArgumentParser()
parser.add_argument("-ptcp", "--Port")

logs = open("logs", "w")
logs.write(f"""
Autor: Maciej Kobiec
Data:{datetime.now().strftime('%d-%m-%y %H:%M:%S')}
Port: {int(parser.parse_args().Port)}
""")
logs.close() 
httpd = socketserver.TCPServer(("", int(parser.parse_args().Port)), ContainerBackendHandler)
try:
    httpd.serve_forever()
except: 
    httpd.server_close()
    print('')
    print("Logi:")
    logs = open("logs", "r")
    print(logs.read())
    logs.close()
   