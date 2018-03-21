from sweext.utils.response import error
from ..logger.logger import (
    record_exception,
    record_debug
)
from sweext.exceptions.error_core import NescException


class HttpError(object):
    @staticmethod
    def handle_core(e, http_status_code=200):
        result = error(msg=str(e), error_code=e.error_code) if isinstance(e, NescException) else error(str(e))
        return result, http_status_code

    @staticmethod
    @record_debug
    def handle_401(e):
        return HttpError.handle_core(e)

    @staticmethod
    @record_debug
    def handle_403(e):
        return HttpError.handle_core(e)

    @staticmethod
    def handle_404(e):
        return HttpError.handle_core(e)

    @staticmethod
    @record_debug
    def handle_405(e):
        return HttpError.handle_core(e)

    @staticmethod
    @record_exception
    def handle_500(e):
        return HttpError.handle_core(e)
