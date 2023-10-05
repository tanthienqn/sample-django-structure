from ..contants import ErrorMassage
from django.http import JsonResponse
import logging
import uuid


class HandleError:

    logger = logging.getLogger(__name__)

    @classmethod
    def __logger_error(cls, e):
        cls.logger.error("ERROR: %s" % str(e), exc_info=True)

    @classmethod
    def handle(cls, exception):
        cls.__logger_error(exception)
        transaction_id = uuid.uuid4()
        error_status = ErrorMassage.error_status.get(str(exception), 500)
        error_message = ErrorMassage.error_message.get(str(exception), str(exception))
        error_code = ErrorMassage.error_code.get(str(exception), "ERROR")
        return JsonResponse(dict(
            transaction_id=transaction_id,
            error_status=error_status,
            error_message=error_message,
            error_code=error_code,
            message="ERROR",
        ), status=error_status)
