# ToDo App with Celery and Channels
TODO app is built using Django, Celery, and Channels with Redis as a message broker and backend. The app allows you to create and delete tasks and also a task filter that you can use to group tasks by date.
It also supports real-time updates such as getting notified when the task time is reached using WebSockets via Channels.

![](https://github.com/Maged-Zaki/ToDo/blob/main/staticfiles/todo_app/images/index.gif)

## Technologies and Libraries used
- **Django** and that includes the built-in libraries
- **Sqlite3** Used as a database engine.
- **Django Channels:** Used for Real-time updates for task status using WebSockets.
- **Celery:** Used for asynchronous task processing. 
- **Redis:** Used as a message broker


# Getting started
```
git clone https://github.com/Maged-Zaki/ToDo.git
```

```
cd ToDo

```

```
pip install -r requirements.txt

```

```
python manage.py runserver
```
**Now the server is running however we need to install Redis and start Celery worker to handle the asynchronous task that sends notifications to the users**

[install Redis docs](https://redis.io/docs/install/install-redis/)

**in a seperate terminal run the following command**.
```
celery -A todo worker --pool=solo -l info
```
**same here in another seperate terminal run the following command**.

```
celery -A todo beat -l info
```

**That's it we are done, we can now create todo tasks and in the case of reaching the finish time we should receive a notifcaiton through the browser.**