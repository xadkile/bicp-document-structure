from typing import TypeVar, Generic

from bicp_document_structure.util.result.Result import Result

E = TypeVar("E")

class Err(Result[None,E],Generic[E]):

    def __init__(self, errReport):
        self.__errReport = errReport

    @property
    def err(self)->E:
        return self.__errReport

    def value(self)->None:
        return None

    def isOk(self):
        return False

    def isErr(self):
        return True