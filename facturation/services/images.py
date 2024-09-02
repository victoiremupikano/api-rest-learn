import uuid
from base64 import b64decode
from django.core.files.base import ContentFile
def add_photo(image_base64):
    extension=image_base64.split(';')[0].split('/')[1]
    base64=image_base64.split(',')[1]
    image_data=b64decode(base64)
    image_name=str(uuid.uuid4())+"."+extension
    photo_image=ContentFile(image_data,image_name)
    return photo_image