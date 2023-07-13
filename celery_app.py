import settings
from celery import Celery


app = Celery(
    "report",
    backend="redis",
    broker=settings.CELERY_BROKER_URL,
    include=["tasks"],
)

app.config_from_object("settings")

app.conf.beat_schedule = {
    "report-ram-stats-every-minute": {
        "task": "tasks.report_ram_stats_task",
        "schedule": 60.0,
    }
}
