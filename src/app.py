from PIL import Image
import streamlit as st

from model import generate_caption
from preprocess import build_prompt, preprocess_image

st.title("✨ Image Captioning with VLM")

uploaded_file = st.file_uploader("Загрузите изображение", type=["png", "jpg", "jpeg"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Загруженное изображение")

        if st.button("Сгенерировать описание", type="primary"):
            with st.spinner("Модель генерирует описание...", show_time=True):
                image_uri = preprocess_image(image)
                prompt = build_prompt()
                caption = generate_caption(prompt, image_uri)

                st.success("Описание изображения:")
                st.write(caption)

    except Exception as e:
        st.error(f"Произошла ошибка: {e}")
