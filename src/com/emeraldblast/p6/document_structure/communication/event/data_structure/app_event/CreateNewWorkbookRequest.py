from typing import Optional

from com.emeraldblast.p6.proto.AppEventProtos_pb2 import CreateNewWorkbookRequestProto


class CreateNewWorkbookRequest:
    def __init__(self, windowId: str | None = None):
        self.windowId = windowId

    @staticmethod
    def fromProtoBytes(data: bytes) -> 'CreateNewWorkbookRequest':
        proto = CreateNewWorkbookRequestProto()
        proto.ParseFromString(data)
        rt= CreateNewWorkbookRequest()
        if proto.HasField("windowId"):
            rt.windowId = proto.windowId
        return rt

