import json
from typing import Union

from com.emeraldblast.p6.document_structure.util.report.ReportJsonStrMaker import ReportJsonStrMaker
from com.emeraldblast.p6.document_structure.util.report.error.ErrorHeader import ErrorHeader
from com.emeraldblast.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKey import WorkbookKey

APPErr = "APPErr"

def errPrefix():
    return APPErr

class AppErrors:
    class WorkbookAlreadyExist:
        header = ErrorHeader(errPrefix()+"1","workbook already exist")
        class Data:
            def __init__(self,nameOrIndexOrKey: Union[str, int, WorkbookKey]):
                if isinstance(nameOrIndexOrKey,str):
                    self.name = nameOrIndexOrKey
                if isinstance(nameOrIndexOrKey, int):
                    self.index=nameOrIndexOrKey
                if isinstance(nameOrIndexOrKey, WorkbookKey):
                    self.key = nameOrIndexOrKey

    class WorkbookNotExist(ErrorReport):
        header = ErrorHeader(errPrefix() + "0", "workbook does not exist")
        class Data(ReportJsonStrMaker):
            def __init__(self, nameOrIndexOrKey: Union[str, int, WorkbookKey]):
                self.wbName = None
                self.wbIndex = None
                self.wbKey=None

                if isinstance(nameOrIndexOrKey, str):
                    self.wbName: str = nameOrIndexOrKey
                if isinstance(nameOrIndexOrKey, int):
                    self.wbIndex = nameOrIndexOrKey
                if isinstance(nameOrIndexOrKey, WorkbookKey):
                    self.wbKey = nameOrIndexOrKey
            def __str__(self):
                if self.wbIndex is not None:
                    return "Workbook at index: "+str(self.wbIndex)
                if self.wbName is not None:
                    return "Workbook named "+ self.wbName
                if self.wbKey is not None:
                    return "Workbook at key:\n"+str(self.wbKey)
                return ""
            def reportJsonStr(self):
                return json.dumps(self.__dict__)
        def __init__(self,nameOrIndexOrKey: Union[str, int, WorkbookKey]):
            super().__init__(
                header = AppErrors.WorkbookNotExist.header,
                data = AppErrors.WorkbookNotExist.Data(nameOrIndexOrKey)
            )