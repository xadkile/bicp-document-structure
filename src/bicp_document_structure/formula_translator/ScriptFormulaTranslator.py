import re

from bicp_document_structure.error.ErrorReport import ErrorReport
from bicp_document_structure.formula_translator.FormulaTranslator import FormulaTranslator
from bicp_document_structure.formula_translator.errors.TranslatorErrors import TranslatorErrors
from bicp_document_structure.util.result.Err import Err
from bicp_document_structure.util.result.Ok import Ok
from bicp_document_structure.util.result.Result import Result


class ScriptFormulaTranslator(FormulaTranslator):
    codePatter = re.compile("\\s*=\\s*SCRIPT\\s*\\(.*\\)\\s*",
                            re.IGNORECASE | re.DOTALL | re.MULTILINE | re.UNICODE)

    def translate(self, formula: str) -> Result:
        isMatch = ScriptFormulaTranslator.codePatter.fullmatch(formula.upper()) is not None
        if isMatch:
            trimmed: str = formula.strip()
            startIndex = 0
            for c in trimmed:
                startIndex += 1
                if c == '(':
                    break
            rt: str = trimmed[startIndex:len(trimmed) - 1]
            return Ok(rt)
        else:
            return Err(
                ErrorReport(
                    TranslatorErrors.NotAScriptCallHeader,
                    TranslatorErrors.NotAScriptCallData(formula),
                    loc=""
                )
            )
