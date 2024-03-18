import streamlit as st
import requests
import io
from PIL import Image, UnidentifiedImageError
import base64

# Function to convert image to base64
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to convert GIF image to base64
def gif_to_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

# Function to load GIF image to sidebar
def load_gif_to_sidebar(gif_path):
    gif_base64 = gif_to_base64(gif_path)
    st.sidebar.markdown(
        f'<img src="data:image/gif;base64,{gif_base64}" class="cover-glow" width="200">',
        unsafe_allow_html=True,
    )

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

st.title("Text to Image AI Generator")

# Text input
text_input = st.text_input("Enter text for image generation:", "rambo")

# Generate button
if st.button("Generate Image"):
    image_bytes = query({"inputs": text_input})

    # Try to open the image and display it
    try:
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Generated Image", use_column_width=True)
    except UnidentifiedImageError:
        st.error("Failed to generate image. Please try again with different text.")

# Define sidebar content
with st.sidebar:
    st.title("Text to Image Chatapp")
    st.markdown('''
        Chatapp is a user-friendly web application designed to seamlessly generate images from text inputs. With a sleek and intuitive interface, users can effortlessly enter their desired text messages and instantly witness them transformed into captivating images.
    ''')
    # Load GIF to sidebar
    gif_path = "imgs/chatbot2.gif"
    load_gif_to_sidebar(gif_path)

# Custom CSS for glowing effect
st.markdown(
    """
    <style>
    .cover-glow {
        width: 100%;
        height: auto;
        padding: 3px;
        box-shadow: 
            0 0 5px #0066ff,
            0 0 10px #0066ff,
            0 0 15px #0066ff,
            0 0 20px #0066ff,
            0 0 25px #0066ff,
            0 0 30px #0066ff,
            0 0 35px #0066ff;
        position: relative;
        z-index: -1;
        border-radius: 30px;  /* Rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
