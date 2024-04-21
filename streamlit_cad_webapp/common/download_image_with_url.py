from typing import Union

import requests
from PIL import Image
from io import BytesIO


class NotValidURL(Exception):
    def __init__(self, message, url):
        self.url = url
        self.message = message
        super().__init__(self.message)


def get_image_from_url(url: str) -> Union[Image.Image, None]:
    try:
        # logger.info("Downloading image from URL")
        response = requests.get(url, timeout=3)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        # logger.info("Image downloaded successfully")
        return image
    except Exception as e:
        # logger.error(f"Failed to download image from URL: {e}")
        return None
        # raise NotValidURL("Failed to download image from URL", url)