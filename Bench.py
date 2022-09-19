import unittest
from dataclasses import dataclass

from typing import Optional

from com.qxdzbc.p6.app.App import App
from com.qxdzbc.p6.app.GlobalScope import setIPythonGlobals
from com.qxdzbc.p6.app.RpcApp import RpcApp
from com.qxdzbc.p6.app.TopLevel import getApp
from com.qxdzbc.p6.cell.address.CellAddresses import CellAddresses
from com.qxdzbc.p6.proto.WorksheetProtos_pb2 import LoadDataRequestProto
from com.qxdzbc.p6.rpc.StubProvider import RpcStubProvider
from com.qxdzbc.p6.workbook.RpcWorkbook import RpcWorkbook
from com.qxdzbc.p6.workbook.WorkBook import Workbook
from com.qxdzbc.p6.workbook.key.WorkbookKeys import WorkbookKeys
from com.qxdzbc.p6.worksheet.RpcWorksheet import RpcWorksheet
from com.qxdzbc.p6.worksheet.LoadType import LoadType
from com.qxdzbc.p6.worksheet.Worksheet import Worksheet


@dataclass
class B:
    x: int
    v: Optional[str] = "Default v"


class Bench(unittest.TestCase):

    def test_q(self):
        import pandas as pd
        import numpy as np
        df = pd.DataFrame([[5, 2, np.nan], [9, 2, 4], [9, 2, 4]])
        print(df)
        print("====")
        for c in df:
            for num in df[c]:
                print(num)


    def test_configRpc(self):
        from com.qxdzbc.p6.rpc.RpcInfo import RpcInfo
        setIPythonGlobals(globals())
        app: RpcApp = getApp()
        rpcSP:RpcStubProvider = app.rpcSP
        port = 52533
        rpcInfo = RpcInfo(
            host="localhost",
            port=port
        )
        rpcSP.setRpcInfo(
            rpcInfo
        )

        # wb0:Workbook=app.getWorkbook(1)
        awb = app.activeWorkbook

        for ws in awb.worksheets:
            awb.removeWorksheet(ws.name)

        # for x in range(20):
        #     awb.createNewWorksheet()

        # ar1=[
        #     [1,2,3],
        #     [4,5,6]
        # ]
        # import pandas as pd
        # df = pd.DataFrame({
        #     "a":ar1[0],
        #     "b":ar1[1]
        # })
        # aws.loadDataFrame(df,loadType = LoadType.OVERWRITE,keepHeader = False)

        # aws.load2DArray(
        #     [
        #         [100, 200, 300],
        #         [400, 500, 600]
        #     ],
        #     anchorCell = CellAddresses.fromLabel("B1"),
        #     loadType = LoadType.OVERWRITE
        # )


        # app.printWorkbookSummary()
        # o = app.closeWorkbook(WorkbookKeys.fromNameAndPath("Book1"))
        # app.createNewWorkbook("WBBBB")
        # app.setActiveWorkbook(WorkbookKeys.fromNameAndPath("WBBBB"))
        # print(app.activeWorkbook)

        # app.loadWorkbookRs("/home/abc/Documents/gits/project2/p6/p6-app/src/test/resources/sampleWb/w1.txt")
        # wbk = WorkbookKeys.fromNameAndPath("w1.txt","/home/abc/Documents/gits/project2/p6/p6-app/src/test/resources/sampleWb/w1.txt")
        # app.saveWorkbookAtPath(wbk,"/home/abc/Documents/gits/project2/p6/p6-app/src/test/resources/sampleWb/w2.txt")
