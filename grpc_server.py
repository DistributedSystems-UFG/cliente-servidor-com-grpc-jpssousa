import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)
    
    def Add(self, request, context):
        arg1 = request.arg1
        arg2 = request.arg2
        message = f"Received request to calculate {arg1} + {arg2}"
        calc = arg1 + arg2
        result = {'message': message, 'result': calc}

        return pb2.Result(**result)

    def Sub(self, request, context):
        arg1 = request.arg1
        arg2 = request.arg2
        message = f"Received request to calculate {arg1} - {arg2}"
        calc = arg1 - arg2
        result = {'message': message, 'result': calc}

        return pb2.Result(**result)

    def Mult(self, request, context):
        arg1 = request.arg1
        arg2 = request.arg2
        message = f"Received request to calculate {arg1} * {arg2}"
        calc = arg1 * arg2
        result = {'message': message, 'result': calc}

        return pb2.Result(**result)

    def Div(self, request, context):
        arg1 = request.arg1
        arg2 = request.arg2
        message = f"Received request to calculate {arg1} / {arg2}"
        calc = arg1 / arg2
        result = {'message': message, 'result': calc}

        return pb2.Result(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('172.31.89.139:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
