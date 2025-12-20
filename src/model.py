import os
from llama_cpp import Llama
from llama_cpp.llama_chat_format import Qwen25VLChatHandler

REPO_ID = os.getenv("VLM_MODEL_REPO", "")
IMAGE_PROCESSOR_FILENAME = os.getenv("IMAGE_PROCESSOR_FILENAME", "")
VLM_MODEL_FILENAME = os.getenv("VLM_MODEL_FILENAME", "")


chat_handler = Qwen25VLChatHandler.from_pretrained(
    repo_id=REPO_ID,
    filename=IMAGE_PROCESSOR_FILENAME,
)
llm = Llama.from_pretrained(
    repo_id=REPO_ID,
    filename=VLM_MODEL_FILENAME,
    chat_handler=chat_handler,
    n_ctx=2048,
)


def generate_caption(prompt: str, image_uri: str):
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_uri}},
                ],
            }
        ],
        max_tokens=256,
    )

    return response["choices"][0]["message"]["content"]
