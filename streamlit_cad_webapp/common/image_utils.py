from io import BytesIO
import base64
from PIL import Image


def convert_image_to_binary(image: Image) -> str:
    """
    Convert image to binary without saving it
    :param image: PIL image object
    :return: base64 encoded binary data (string)
    """
    # Create an in-memory buffer
    buffer = BytesIO()

    # Save the image to the buffer in binary mode
    image.save(buffer, format=image.format)

    # Reset the buffer position to the beginning
    buffer.seek(0)

    # Read binary data from the buffer
    data = buffer.read()

    # Encode the binary data to base64 string
    encoded_data = base64.b64encode(data).decode("utf-8")

    # Close the buffer (optional)
    buffer.close()

    return encoded_data
