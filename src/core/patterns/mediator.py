class Mediator:
    def __init__(self, handlers: dict):
        self._handlers = handlers

    async def send(self, request):
        request_type = type(request)
        if request_type not in self._handlers:
            raise Exception(f"No handler registered for {request_type}")

        handler_provider = self._handlers[request_type]
        handler = handler_provider()
        return await handler.handle(request)
