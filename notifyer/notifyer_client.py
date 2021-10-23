from __future__ import print_function

import logging
from google.protobuf import message

import grpc
import notifyer_pb2 as ntf
import notifyer_pb2_grpc as ntf_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ntf_grpc.NorifyerStub(channel)
        response = stub.SendNotify(ntf.MsgRequest(to="sex",message="jopa"))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
