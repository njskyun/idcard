from tasks.celery_app import celery_app

@celery_app.task(name="tasks.async_recognize_text")
def async_recognize_text(image_path):
    from app.services.paddleocr_service import recognize_text
    return recognize_text(image_path)
 
@celery_app.task(name="tasks.async_cartoonize_gan")
def async_cartoonize_gan(image_path):
    from app.services.cartoonize_service import cartoonize_with_cartoon_gan
    return cartoonize_with_cartoon_gan(image_path)

@celery_app.task(name="tasks.async_generate_id_photo")
def async_generate_id_photo(image_path):
    from app.services.photo_id_service import generate_id_photo_hivision
    return generate_id_photo_hivision(image_path)

