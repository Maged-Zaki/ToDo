from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import ConnectedUsers

@shared_task
def check_finish_time():
    current_date_time = timezone.now() + timedelta(hours=3)

    tasks = Task.objects.filter(finish_time__lte=current_date_time, date_reached=False)

    for task in tasks:
        task.date_reached = True
        task.save()

        connected_user = ConnectedUsers.objects.get(user_id=task.user.id)
        print(connected_user)

        if connected_user:
            # To obtain the channel layer
            channel_layer = get_channel_layer()

            #send message to the channel with the corresponding user
            async_to_sync(channel_layer.send)(connected_user.user_channel, {
                "type": "send_message",
                "task_content": task.content,
                "task_id": task.id
            })


