from django.apps import AppConfig


class Task1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task1'

    def ready(self):
       
        from task1.populate_db import run
        try:
            run()  
        except Exception as e:
            print(f"Ошибка при запуске populate_db: {e}")
