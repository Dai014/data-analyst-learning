from flask import Flask
from concurrent import futures
import grpc
import your_grpc_service_pb2_grpc  # Import your gRPC service definitions
import your_grpc_service_pb2  # Import your gRPC message definitions

app = Flask(__name__)

class YourService(your_grpc_service_pb2_grpc.YourServiceServicer):
    def YourMethod(self, request, context):
        # Implement your gRPC method logic here
        response = your_grpc_service_pb2.YourResponse()
        response.message = "Hello from gRPC!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    your_grpc_service_pb2_grpc.add_YourServiceServicer_to_server(YourService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    return server

@app.route('/')
def hello():
    return "Hello from Flask!"

if __name__ == '__main__':
    grpc_server = serve()
    try:
        app.run(port=5000)
    finally:
        grpc_server.stop(0)