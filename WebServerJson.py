from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import json
class helloHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()
        #self.content = json.dumps({'hello': 'world', 'recieved': 'ok'})

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'recieved': 'ok'}).encode())

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        message = json.loads(self.rfile.read(length))

        message['recieved'] = 'ok'
        print (message)
        #self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'recieved': 'ok'}).encode())
        #self.content = json.dumps(message)

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print('Server running on port %s'%PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
