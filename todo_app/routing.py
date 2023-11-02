from django.urls import path


from . import consumers

websocket_urlpatterns = [
    path('ws/my_tasks', consumers.NotficationHandler.as_asgi())
]