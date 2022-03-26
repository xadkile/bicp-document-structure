from bicp_document_structure.message.proto.WorkbookProto_pb2 import RenameWorksheetOkProto
from bicp_document_structure.util.ToProto import ToProto
from bicp_document_structure.workbook.key.WorkbookKey import WorkbookKey


class RenameWorksheetOkData(ToProto[RenameWorksheetOkProto]):
    def __init__(self, workbookKey: WorkbookKey, oldName, newName, index):
        self.workbookKey = workbookKey
        self.oldName = oldName
        self.index = index
        self.newName = newName

    def toProtoObj(self) -> RenameWorksheetOkProto:
        rt = RenameWorksheetOkProto()
        rt.oldName = self.oldName
        rt.newName = self.newName
        rt.index = self.index
        rt.workbookKey.CopyFrom(self.workbookKey.toProtoObj())
        return rt