import unittest
from unittest.mock import MagicMock

from com.emeraldblast.p6.document_structure.communication.event_server.reactors.app_event.LoadWorkbookReactor import \
    LoadWorkbookReactor
from com.emeraldblast.p6.document_structure.util.Util import makeGetter
from com.emeraldblast.p6.document_structure.util.report.error.ErrorHeader import ErrorHeader
from com.emeraldblast.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.emeraldblast.p6.document_structure.util.result.Err import Err
from com.emeraldblast.p6.document_structure.util.result.Ok import Ok
from com.emeraldblast.p6.document_structure.workbook.WorkbookImp import WorkbookImp


class LoadWorkbookReactor_test(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.app = MagicMock()
        self.reactor = LoadWorkbookReactor(
            makeGetter(self.app)
        )

    def test_react(self):
        self.app.loadWorkbookRsNoEvent = MagicMock()
        self.reactor.react(b"")
        self.assertEqual(1,self.app.loadWorkbookRsNoEvent.call_count)

    def test_react_ok(self):
        loadRs = Ok(WorkbookImp(""))
        self.app.loadWorkbookRsNoEvent = MagicMock(return_value=loadRs)
        out = self.reactor.react(b"")
        self.assertEqual(1,self.app.loadWorkbookRsNoEvent.call_count)
        self.assertFalse(out.isError)
        self.assertEqual(loadRs.value, out.workbook)
        self.assertEqual(None, out.errorReport)

    def test_react_err(self):
        loadRs = Err(errReport = ErrorReport(
            header=ErrorHeader("12","qwe")
        ))
        self.app.loadWorkbookRsNoEvent = MagicMock(return_value=loadRs)
        out = self.reactor.react(b"")
        self.assertEqual(1,self.app.loadWorkbookRsNoEvent.call_count)
        self.assertTrue(out.isError)
        self.assertEqual(None, out.workbook)
        self.assertEqual(loadRs.err, out.errorReport)



if __name__ == '__main__':
    unittest.main()
