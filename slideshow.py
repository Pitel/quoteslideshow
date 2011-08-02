#!/usr/bin/env python3

import glob, json
from http.server import HTTPServer, BaseHTTPRequestHandler

class slideshow(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith('.json'):
			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()
			self.wfile.write(bytes(json.dumps({'images': glob.glob('*.[jJ][pP][gG]'), 'quotes': open('slideshow.txt').readlines()}), 'utf8'))
		elif self.path.lower().endswith('.jpg'):
			try:
				f = open(self.path[1:], 'rb')
				self.send_response(200)
				self.send_header('Content-type', 'image/jpeg')
				self.end_headers()
				self.wfile.write(bytes(f.read()))
				f.close()
			except IOError:
				self.send_error(404)
		else:
			try:
				f = open(self.path[1:])
				self.send_response(200)
				if self.path.endswith('.js'):
					self.send_header('Content-type', 'application/javascript')
				elif self.path.endswith('.css'):
					self.send_header('Content-type', 'text/css')
				self.end_headers()
				self.wfile.write(bytes(f.read(), 'utf8'))
				f.close()
			except IOError:
				self.send_error(404)

if __name__ == '__main__':
	server = HTTPServer(('', 8000), slideshow)
	print('http://localhost:8000/slideshow.htm')
	server.serve_forever()
