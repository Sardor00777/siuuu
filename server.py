from wsgiref.simple_server import make_server
from main import app

if __name__ == "__main__":
    with make_server('', 8000, app) as server:
        print("Server http://localhost:8000 da ishlayapti...")
        server.serve_forever()
