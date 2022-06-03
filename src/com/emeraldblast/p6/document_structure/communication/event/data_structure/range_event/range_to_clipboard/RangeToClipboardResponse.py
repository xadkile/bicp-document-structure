from com.emeraldblast.p6.document_structure.communication.event.data_structure.common.ErrorIndicator import \
    ErrorIndicator
from com.emeraldblast.p6.document_structure.communication.event.data_structure.range_event.RangeId import RangeId
from com.emeraldblast.p6.document_structure.util.ToProto import ToProto, P
from com.emeraldblast.p6.proto.RangeProtos_pb2 import RangeToClipboardResponseProto


class RangeToClipboardResponse(ToProto[RangeToClipboardResponseProto]):

    def __init__(self, errorIndicator: ErrorIndicator, rangeId: RangeId, windowId: str | None):
        self.windowId = windowId
        self.errorIndicator = errorIndicator
        self.rangeId = rangeId

    def toProtoObj(self) -> RangeToClipboardResponseProto:
        proto = RangeToClipboardResponseProto(
            errorIndicator = self.errorIndicator.toProtoObj(),
            rangeId = self.rangeId.toProtoObj()
        )
        if self.windowId:
            proto.windowId = self.windowId
        return proto
