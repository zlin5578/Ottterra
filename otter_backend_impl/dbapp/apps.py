# from django.apps import AppConfig


# class DbappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'dbapp'
from django.apps import AppConfig
import threading

class DbappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dbapp'

    def ready(self):
        # 避免重复启动（只在主线程）
        import os
        if os.environ.get('RUN_MAIN') != 'true':
            return

        from dbapp.views import run_gradio_interface

        def launch_gradio():
            run_gradio_interface().launch(
                server_name="0.0.0.0", 
                server_port=7860, 
                inbrowser=False, 
                share=False
            )

        threading.Thread(target=launch_gradio, daemon=True).start()
