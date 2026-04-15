from celery_worker import celery_app

@celery_app.task
def placeholder_red_task():
    return {"status": "Red agent tasks — coming in Phase 3"}