import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = '44.203.156.19'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)

    def call_add(self, arg1, arg2):
        """
        Client function to call the rpc for Add
        """
        args = pb2.Args(arg1=arg1, arg2=arg2)
        print(f"Calling Add({arg1},{arg2})")
        return self.stub.Add(args)

    def call_sub(self, arg1, arg2):
        """
        Client function to call the rpc for Sub
        """
        args = pb2.Args(arg1=arg1, arg2=arg2)
        print(f"Calling Sub({arg1},{arg2})")
        return self.stub.Sub(args)

    def call_mult(self, arg1, arg2):
        """
        Client function to call the rpc for Mult
        """
        args = pb2.Args(arg1=arg1, arg2=arg2)
        print(f"Calling Mult({arg1},{arg2})")
        return self.stub.Mult(args)

    def call_div(self, arg1, arg2):
        """
        Client function to call the rpc for Div
        """
        args = pb2.Args(arg1=arg1, arg2=arg2)
        print(f"Calling Div({arg1},{arg2})")
        return self.stub.Div(args)



if __name__ == '__main__':
    client = UnaryClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')

    result = client.call_add(2,3)
    print(f'{result}')

    result = client.call_sub(0,6)
    print(f'{result}')

    result = client.call_mult(3,4)
    print(f'{result}')

    result = client.call_div(28,7)
    print(f'{result}')
