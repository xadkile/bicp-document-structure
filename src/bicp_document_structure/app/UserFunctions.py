from typing import Optional, Union, Tuple

from bicp_document_structure.app import App
from bicp_document_structure.app.GlobalScope import getGlobals
from bicp_document_structure.app.SingleBookApp import SingleBookApp
from bicp_document_structure.cell.Cell import Cell
from bicp_document_structure.cell.address.CellAddress import CellAddress
from bicp_document_structure.range.Range import Range
from bicp_document_structure.range.address.RangeAddress import RangeAddress
from bicp_document_structure.workbook.WorkBook import Workbook
from bicp_document_structure.workbook.WorkbookKey import WorkbookKey
from bicp_document_structure.worksheet.Worksheet import Worksheet

"""
This module contains functions to be used by users to control the application.
"""
appKey = "__appInstance"

def startApp():
    """create the app singleton"""
    getApp()

def stopApp():
    """ stop the app, clear everything """
    g = getGlobals()
    if appKey in g.keys():
        del g[appKey]


def restartApp():
    """restart the app"""
    stopApp()
    startApp()


def getApp() -> App:
    """get the singleton App instance"""
    g = getGlobals()
    if appKey not in g.keys():
        g[appKey] = SingleBookApp()
    return g[appKey]


def getActiveWorkbook() -> Optional[Workbook]:
    return getApp().activeWorkbook


def setActiveWorkbook(indexOrName):
    getApp().setActiveWorkbook(indexOrName)


def getActiveSheet() -> Optional[Worksheet]:
    return getActiveWorkbook().activeSheet


def setActiveSheet(indexOrName: Union[str, int]):
    getActiveWorkbook().setActiveSheet(indexOrName)


def getSheet(nameOrIndex: Union[str, int]) -> Optional[Worksheet]:
    return getActiveWorkbook().getSheet(nameOrIndex)


def getRange(rangeAddress: Union[str, RangeAddress, Tuple[CellAddress, CellAddress]]) -> Range:
    return getActiveSheet().range(rangeAddress)


def cell(address: Union[str, CellAddress, Tuple[int, int]]) -> Cell:
    """get a cell from the current active sheet"""
    return getActiveSheet().cell(address)


def getWorkbook(nameOrIndexOrKey: Union[str, int, WorkbookKey]) -> Workbook:
    app: App = getApp()
    wb = app.getWorkbook(nameOrIndexOrKey)
    return wb
