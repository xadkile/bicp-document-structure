from zmq import Socket

from bicp_document_structure.message.SocketProvider import SocketProvider


class SocketProviderImp(SocketProvider):

    def __init__(self, reqSocketUI: Socket | None = None, eventServerPort:int | None = None):
        self.__reqSocketUI: Socket = reqSocketUI
        self._eventServerPort: int|None = eventServerPort

    def reqSocketForUIUpdating(self) -> Socket | None:
        return self.__reqSocketUI

    def updateREQSocketForUIUpdating(self, newSocket: Socket | None):
        self.__reqSocketUI = newSocket

    # def eventServerPort(self) -> int:
    #     return self._eventServerPort
    #
    # def updateEventServerPort(self, port):
    #     self._eventServerPort = port