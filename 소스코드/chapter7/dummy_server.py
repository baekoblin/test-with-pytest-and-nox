# dummy_server.py
class DummyServer:
    def start(self):
        print("Server started at http://localhost:8000")
        return self

    def stop(self):
        print("Server stopped")

def start_web_server():
    server = DummyServer()
    return server.start()
