from concurrent import futures
import logging

import grpc
import notifyer_pb2 as ntf
import notifyer_pb2_grpc as ntf_grpc


class Notifyer(ntf_grpc.NorifyerServicer):

    def SendNotify(self, request, context):
        return ntf.SendNotify(message='Hello, %s!' % request.message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ntf_grpc.add_NorifyerServicer_to_server(Notifyer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
