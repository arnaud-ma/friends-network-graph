import http.server
import socketserver
import webbrowser


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


def connect():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        webbrowser.open('http://localhost:8000/page/graph.html')
        httpd.serve_forever()
