import asyncio

from app.tasks.celery_app import celery_instance


@celery_instance.task(name="send_email_for_security_user")
def sends_email():
    #asyncio.run(send_email_for_security_user)
    print("send_email_for_security_user успешно завершена!")


