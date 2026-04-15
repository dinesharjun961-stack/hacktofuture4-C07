from celery_worker import celery_app

@celery_app.task
def placeholder_blue_task():
    return {"status": "Blue agent tasks — coming in Phase 4"}