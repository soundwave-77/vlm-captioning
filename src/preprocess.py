import io
import base64
from PIL import Image

CAPTION_PROMPT = (
    "Дай точное, полное и объективное описание изображения на русском языке."
)


def build_prompt() -> str:
    return CAPTION_PROMPT


def image_to_base64_data_uri(image: Image.Image) -> str:
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    base64_data = base64.b64encode(img_bytes).decode("utf-8")

    return f"data:image/png;base64,{base64_data}"


def preprocess_image(image: Image.Image) -> str:
    image.thumbnail((256, 256))
    return image_to_base64_data_uri(image)
