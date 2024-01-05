import os

from django.core.exceptions import ValidationError
from PIL import Image


def validate_icon_image_size(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError(
                    f"The maximum allowed Image size is 70*70, image you provide is: {image.size}"
                )


def validate_image_extension(image):
    ext = os.path.splitext(image.name)[1]
    validate_ext = [".jpg", ".jpeg", ".png", "gif"]

    if not ext.lower() in validate_ext:
        raise ValidationError("Unsupported File Extension")
