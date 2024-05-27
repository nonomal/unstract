from rest_framework.exceptions import APIException

from backend.exceptions import UnstractBaseException
from unstract.connectors.exceptions import ConnectorError


class IdIsMandatory(APIException):
    status_code = 400
    default_detail = "ID is Mandatory."


class InValidType(APIException):
    status_code = 400
    default_detail = "Type is not Valid."


class InValidConnectorMode(APIException):
    status_code = 400
    default_detail = "Connector mode is not Valid."


class InValidConnectorId(APIException):
    status_code = 400
    default_detail = "Connector ID is not Valid."


class JSONParseException(APIException):
    status_code = 500
    default_detail = "Exception occured while Parsing JSON Schema."


class OAuthTimeOut(APIException):
    status_code = 408
    default_detail = "Timed Out. Please re authenticate."


class InternalServiceError(APIException):
    status_code = 500
    default_detail = "Internal Service error"


class TestConnectorException(APIException):
    status_code = 500
    default_detail = "Error while testing connector."


class TestConnectorInputException(UnstractBaseException):
    def __init__(self, core_err: ConnectorError) -> None:
        super().__init__(detail=core_err.message, core_err=core_err)
        self.default_detail = core_err.message
        self.status_code = 400


class TestConnectionException(Exception):
    DEFAULT_MESSAGE = "Test connection failed! "

    def __init__(self, message: str = DEFAULT_MESSAGE):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class KeyNotFoundException(APIException):
    def __init__(self, message: str) -> None:
        status_code = 400
        default_detail = (
            "Test connection failed. "
            "The provided parameter {} not found while testing connector."
        )
        detail = default_detail.format(message)
        super().__init__(detail=detail, code=status_code)
