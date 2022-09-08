import unittest

from com.qxdzbc.p6.document_structure.workbook.WorkbookImp import WorkbookImp

from com.qxdzbc.p6.document_structure.file.P6FileContent import P6FileContent
from com.qxdzbc.p6.document_structure.file.P6FileMetaInfo import P6FileMetaInfo


class P6FileContent_test(unittest.TestCase):
    def test_from_toProto(self):
        o = P6FileContent(
            meta = P6FileMetaInfo(date=123),
            wb = WorkbookImp("Book1"),
        )
        proto = o.toProtoObj()
        self.assertEqual(o.meta.toProtoObj(), proto.meta)
        self.assertEqual(o.wb.toProtoObj(),proto.workbook)
        o2 = P6FileContent.fromProtoBytes(proto.SerializeToString())
        self.assertEqual(o,o2)


if __name__ == '__main__':
    unittest.main()
