import unittest
from pathlib import Path

from com.emeraldblast.p6.document_structure.cell.address.CellAddresses import CellAddresses
from com.emeraldblast.p6.document_structure.communication.event.data_structure.worksheet_event.DeleteCell import \
    DeleteCellRequest
from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKeys import WorkbookKeys


class DeleteCellRequest_test(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.o = DeleteCellRequest(
            workbookKey = WorkbookKeys.fromNameAndPath("AbC", Path("zx").absolute()),
            worksheetName = "S1",
            cellAddress = CellAddresses.fromRowCol(100, 200)
        )

    def test_toProto(self):
        o = self.o
        proto = o.toProtoObj()
        self.assertEqual(o.workbookKey.toProtoObj(), proto.workbookKey)
        self.assertEqual(o.cellAddress.toProtoObj(), proto.cellAddress)
        self.assertEqual(o.worksheetName, proto.worksheetName)

    def test_fromProto(self):
        proto = self.o.toProtoObj()
        o = DeleteCellRequest.fromProtoBytes(proto.SerializeToString())
        self.assertEqual(o.workbookKey, self.o.workbookKey)
        self.assertEqual(o.worksheetName, self.o.worksheetName)
        self.assertEqual(o.cellAddress, self.o.cellAddress)


if __name__ == '__main__':
    unittest.main()
