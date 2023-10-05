from .middlewares.HandleError import HandleError
from .middlewares.HandleSuccess import HandleSuccess
from rest_framework.renderers import JSONRenderer


class CustomMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        return HandleError.handle(exception)


class CustomJsonRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return HandleSuccess.handle(data)