from PIL import Image
import requests
from streamlit_cad_webapp.common.image_utils import convert_image_to_binary
from streamlit_cad_webapp.config.config import settings


def send_request_to_API(image: Image.Image) -> tuple:
    """
    Send request to API
    :param image:
    :return:
    """
    # Convert image to binary
    binary_image = convert_image_to_binary(image)

    payload = {
        "data": binary_image
    }

    response = requests.post(settings.api_endpoint_binary, json=payload, headers={"apikey": settings.api_key})

    # Get prediction from response
    if response.status_code == 400:
        return "Image is not valid (no vehicle found)", 0.0

    elif response.status_code == 200:
        result = response.json()
        probs = round(max(result["probabilities"]) * 100, 2)
        return result["predicted_class"], probs

    return "Unknown Error, contact support.", 0.0
