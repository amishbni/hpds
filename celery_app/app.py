import celery_app.settings as settings
from celery import Celery


app = Celery(
    "report",
    backend="redis",
    broker=settings.CELERY_BROKER_URL,
    include=["report.tasks"],
)

app.config_from_object("celery_app.settings")

app.conf.beat_schedule = {
    "report-ram-stats-every-minute": {
        "task": "report.tasks.report_ram_stats_task",
        "schedule": 60.0,
    }
}
