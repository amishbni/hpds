from report.models import ram_usage_instance
from celery_app.app import app


@app.task
def report_ram_stats_task():
    ram_usage_instance.set_ram_stats()
