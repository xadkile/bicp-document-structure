import unittest

from com.emeraldblast.p6.document_structure.communication.event.data_structure.app_event.CreateNewWorkbookRequest import \
    CreateNewWorkbookRequest
from com.emeraldblast.p6.proto.AppEventProtos_pb2 import CreateNewWorkbookRequestProto


class CreateNewWorkbookRequest_test(unittest.TestCase):
    def test_fromProtoBytes(self):
        proto = CreateNewWorkbookRequestProto(windowId="12345")
        o = CreateNewWorkbookRequest.fromProtoBytes(proto.SerializeToString())
        self.assertEqual(proto.windowId, o.windowId)

    def test_fromProtoBytes_noneId(self):
        proto = CreateNewWorkbookRequestProto()
        o = CreateNewWorkbookRequest.fromProtoBytes(proto.SerializeToString())
        self.assertEqual(None, o.windowId)






if __name__ == '__main__':
    unittest.main()
