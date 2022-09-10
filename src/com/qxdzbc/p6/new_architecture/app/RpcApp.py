from pathlib import Path
from typing import Union, Optional

from com.qxdzbc.p6.document_structure.app.BaseApp import BaseApp
from com.qxdzbc.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.qxdzbc.p6.document_structure.util.result.Err import Err
from com.qxdzbc.p6.document_structure.util.result.Ok import Ok
from com.qxdzbc.p6.document_structure.util.result.Result import Result
from com.qxdzbc.p6.document_structure.workbook.WorkBook import Workbook
from com.qxdzbc.p6.document_structure.workbook.key.WorkbookKey import WorkbookKey
from com.qxdzbc.p6.document_structure.worksheet.Worksheet import Worksheet
from com.qxdzbc.p6.new_architecture.common.RpcUtils import RpcUtils
from com.qxdzbc.p6.new_architecture.rpc.StubProvider import RpcStubProvider
from com.qxdzbc.p6.new_architecture.rpc.data_structure.SingleSignalResponse import SingleSignalResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.app.CreateNewWorkbookRequest import CreateNewWorkbookRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.app.CreateNewWorkbookResponse import CreateNewWorkbookResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.app.GetWorkbookRequest import GetWorkbookRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.app.WorkbookKeyWithErrorResponse import \
    WorkbookKeyWithErrorResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.GetWorksheetResponse import GetWorksheetResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.save_wb.SaveWorkbookRequest import SaveWorkbookRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.save_wb.SaveWorkbookResponse import SaveWorkbookResponse
from com.qxdzbc.p6.new_architecture.workbook.RpcWorkbook import RpcWorkbook
from com.qxdzbc.p6.new_architecture.worksheet.RpcWorksheet import RpcWorksheet
from com.qxdzbc.p6.proto.CommonProtos_pb2 import EmptyProto


class RpcApp(BaseApp):

    def saveWorkbookAtPathRs(self, wbKey: WorkbookKey, filePath: Union[str,Path]) -> Result[Workbook, ErrorReport]:
        def f()->Result[Workbook, ErrorReport]:
            p = filePath
            if isinstance(p,Path):
                p = str(filePath.absolute())

            req = SaveWorkbookRequest(
                wbKey=wbKey,path =p
            )
            oProto=self.appSv.saveWorkbookAtPath(request=req.toProtoObj())
            o = SaveWorkbookResponse.fromProto(oProto)
            if o.wbKey:
                return Ok(RpcWorkbook(wbKey=o.wbKey,stubProvider = self.rpcSP))
            else:
                return Err(o.errorReport)
        return self._onAppSvOkRs(f)

    @property
    def activeSheet(self) -> Optional[Worksheet]:
        def f()->Optional[Worksheet]:
            oProto = self.appSv.getActiveWorksheet(request = EmptyProto())
            o:GetWorksheetResponse = GetWorksheetResponse.fromProto(oProto)
            wsId = o.wsId
            if wsId:
                return RpcWorksheet(
                    name = wsId.wsName,
                    wbKey = wsId.wbKey,
                    stubProvider = self.rpcSP
                )
            else:
                return None
        return self._onAppSvOk(f)

    def setActiveWorkbookRs(self, wbKey: WorkbookKey) -> Result[Workbook, ErrorReport]:
        def f()->Result[Workbook, ErrorReport]:
            oProto = self.appSv.setActiveWorkbook(request=wbKey.toProtoObj())
            o = SingleSignalResponse.fromProto(oProto)
            rs:Result[None,ErrorReport] = o.toRs()
            if rs.isOk():
                return Ok(RpcWorkbook(wbKey = wbKey))
            else:
                return Err(rs.err)
        return self._onAppSvOkRs(f)

    @property
    def activeWorkbook(self) -> Optional[Workbook]:
        def f()->Optional[Workbook]:
            req = EmptyProto()
            oProto = self.appSv.getActiveWorkbook(request = req)
            o: WorkbookKeyWithErrorResponse = WorkbookKeyWithErrorResponse.fromProto(oProto)
            if o.errorReport:
                return None
            if o.wbKey:
                return RpcWorkbook(
                    wbKey = o.wbKey
                )
        return self._onAppSvOk(f)
    def __init__(
            self,
            rpcStubProvider: RpcStubProvider
    ):
        self.rpcSP = rpcStubProvider
    def createNewWorkbookRs(self, name: Optional[str] = None) -> Result[Workbook, ErrorReport]:
        def f()-> Result[Workbook, ErrorReport]:
            req = CreateNewWorkbookRequest(
                workbookName = name
            )
            oProto = self.appSv.createNewWorkbook(request=req.toProtoObj())
            o:CreateNewWorkbookResponse = CreateNewWorkbookResponse.fromProto(oProto)
            if o.errorReport:
                return Err(o.errorReport)
            if o.wbKey:
                return Ok(RpcWorkbook(
                    wbKey = o.wbKey,
                ))
        return self._onAppSvOkRs(f)
    @property
    def appSv(self):
        return self.rpcSP.appService

    def _onAppSvOk(self, f):
        return RpcUtils.onServiceOkOrRaise(self.appSv, f)

    def _onAppSvOkRs(self, f):
        return RpcUtils.onServiceOkRs(self.appSv, f)

    def getWorkbookRs(self, key: Union[str, int, WorkbookKey]) -> Result[Workbook, ErrorReport]:
        def f() -> Result[Workbook, ErrorReport]:
            wbk = None
            name = None
            index = None
            if isinstance(key, WorkbookKey):
                wbk = key
            if isinstance(key, str):
                name = key
            if isinstance(key, int):
                index = key
            req = GetWorkbookRequest(
                wbKey = wbk,
                wbName = name,
                wbIndex = index,
            )
            outProto = self.appSv.getWorkbook(request = req.toProtoObj())
            out = WorkbookKeyWithErrorResponse.fromProto(outProto)
            if out.isOk():
                wbKey = out.wbKey
                return Ok(RpcWorkbook(
                    wbKey =wbKey,
                    stubProvider = self.rpcSP
                ))
            else:
                return Err(out.errorReport)
        return self._onAppSvOkRs(f)



