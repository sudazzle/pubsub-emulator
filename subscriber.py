from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import ssl

class HttpsRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(b'Hello World!')
  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    body = self.rfile.read(content_length)
    self.send_response(200)
    self.end_headers()
    response = BytesIO()
    response.write(b'This is POST request.')
    response.write(b'Received: ')
    response.write(body)
    self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', 3333), HttpsRequestHandler)
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain('https-key-cert/subscriber-private.crt', 'https-key-cert/subscriber-private.key')
# httpd.socket = context.wrap_socket (
#   httpd.socket,
#   server_side=True
# )

httpd.serve_forever()