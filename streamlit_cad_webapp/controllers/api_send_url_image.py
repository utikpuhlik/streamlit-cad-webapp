import requests
from streamlit_cad_webapp.config.config import settings


def send_request_to_API_URL(
    url: str,
) -> tuple:
    """
    Send request to API
    :param url:
    :return:
    """
    params = {
        "url": url
    }

    response = requests.get(settings.api_endpoint_url, params=params, headers={"apikey": settings.api_key})

    # Get prediction from response
    if response.status_code == 400:
        return "Image is not valid (no vehicle found)", 0.0

    elif response.status_code == 200:
        result = response.json()
        probs = round(max(result["probabilities"]) * 100, 2)
        return result["predicted_class"], probs

    return "Unknown Error, contact support.", 0.0