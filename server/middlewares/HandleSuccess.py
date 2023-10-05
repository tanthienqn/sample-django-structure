from django.http import JsonResponse
import uuid


class HandleSuccess:

    @classmethod
    def handle(cls, data):
        transaction_id = uuid.uuid4()
        status_code = 200
        message = "SUCCESS"
        return JsonResponse(dict(
            transaction_id=transaction_id,
            status_code=status_code,
            message=message,
            data=data
        ), status=200)
