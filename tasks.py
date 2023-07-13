from celery import app
from report import ram_usage_instance


@app.shared_task
def report_ram_stats_task():
    ram_usage_instance.report_ram_stats()
