import asyncio

from app.tasks.celery_app import celery_instance


@celery_instance.task(name="cheek_vips")
def cheek_vips_everyday():
    #asyncio.run()
    print("cheek_vips_everyday успешно завершена!")


@celery_instance.task(name="update_player_info")
def update_player_info_task():
    #asyncio.run()
    print("update_player_info_task успешно завершена!")


@celery_instance.task(name="update_fraction_info")
def update_fraction_info_task():
    #asyncio.run()
    print("update_fraction_info_task успешно завершена!")


@celery_instance.task(name="add_vip")
def add_vip_task(steam_id, vip_lvl):
    #asyncio.run()
    print("k успешно завершена!")

