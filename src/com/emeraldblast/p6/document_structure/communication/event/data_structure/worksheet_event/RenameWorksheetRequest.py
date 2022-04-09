from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKey import WorkbookKey
from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKeys import WorkbookKeys
from com.emeraldblast.p6.proto.WorksheetProtos_pb2 import RenameWorksheetRequestProto


class RenameWorksheetRequest:

    def __init__(self, workbookKey:WorkbookKey, oldName:str, newName:str):
        self.newName = newName
        self.oldName = oldName
        self.workbookKey = workbookKey

    @staticmethod
    def fromProto(proto:RenameWorksheetRequestProto)->'RenameWorksheetRequest':
        return RenameWorksheetRequest(
            newName = proto.newName,
            oldName = proto.oldName,
            workbookKey = WorkbookKeys.fromProto(proto.workbookKey)
        )
    @staticmethod
    def fromProtoBytes(data:bytes)->'RenameWorksheetRequest':
        protoRequest = RenameWorksheetRequestProto()
        protoRequest.ParseFromString(data)
        return RenameWorksheetRequest.fromProto(protoRequest)