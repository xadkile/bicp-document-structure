from com.emeraldblast.p6.document_structure.cell.address.CellAddress import CellAddress
from com.emeraldblast.p6.document_structure.cell.address.CellAddresses import CellAddresses
from com.emeraldblast.p6.document_structure.range.address.RangeAddress import RangeAddress
from com.emeraldblast.p6.document_structure.util.ToProto import P
from com.emeraldblast.p6.document_structure.util.Util import typeCheck
from com.emeraldblast.p6.proto.DocProtos_pb2 import RangeAddressProto


class RangeAddressImp(RangeAddress):


    def toProtoObj(self) -> RangeAddressProto:
        proto = RangeAddressProto()
        proto.topLeft.CopyFrom(self.__firstAddress.toProtoObj())
        proto.botRight.CopyFrom(self.__lastAddress.toProtoObj())
        return proto

    def __init__(self, topLeft:CellAddress, botRight:CellAddress):
        typeCheck(topLeft, "topLeft", CellAddress)
        typeCheck(botRight, "botRight", CellAddress)
        self.__firstAddress = None
        self.__lastAddress = None
        rowOk = topLeft.rowIndex <= botRight.rowIndex
        colOk = topLeft.colIndex <= botRight.colIndex
        if rowOk and colOk:
            self.__firstAddress = topLeft
            self.__lastAddress = botRight
        else:
            o = "col"
            if not rowOk:
                o = "row"
            reason = "firstAddress {o} is larger than lastAddress {o}".format(o=o)
            raise ValueError("invalid firstAddress and lastAddress: {reason}".format(reason=reason))

    @property
    def topLeft(self)->CellAddress:
        return self.__firstAddress

    @property
    def botRight(self)->CellAddress:
        return self.__lastAddress

    def rowCount(self)->int:
        return self.botRight.rowIndex - self.topLeft.rowIndex + 1

    def colCount(self)->int:
        return self.botRight.colIndex - self.topLeft.colIndex + 1

    def __str__(self) -> str:
        return "[{fc}:{lc}]".format(fc=str(self.topLeft), lc=str(self.botRight))

    def __eq__(self, o: object) -> bool:
        if isinstance(o, RangeAddressImp):
            sameFirst = self.topLeft == o.topLeft
            sameLast = self.botRight == o.botRight
            return sameFirst and sameLast
        else:
            return False

