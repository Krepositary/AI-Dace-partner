import streamlit as st
import os
from PIL import Image
import numpy as np
from gan_generate import generate_images  # Adjust if the function is different in your repo

# Set page title
st.set_page_config(page_title="AI Dancer - GAN Generator", page_icon=":guardsman:", layout="wide")

def main():
    st.title("AI Dancer - GAN Image Generation")
    st.write("This app generates images using a Generative Adversarial Network (GAN) model.")

    # File uploader for user to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Convert the uploaded image to a format that can be processed by the model (if needed)
        input_image = Image.open(uploaded_file)

        # Call the GAN generation function
        generated_image = generate_images(input_image)  # Replace with your actual function

        # Display the generated image
        st.image(generated_image, caption="Generated Image", use_column_width=True)

    # If the user wants to use a default image or some predefined dataset
    st.write("Alternatively, you can try a predefined image from the 'assets' folder.")
    default_image = st.selectbox("Select a predefined image", os.listdir("assets"))

    if default_image:
        # Load and display a default image
        image_path = os.path.join("assets", default_image)
        image = Image.open(image_path)
        st.image(image, caption=f"Predefined Image: {default_image}", use_column_width=True)

        # Generate an image using the selected default image
        generated_image = generate_images(image)  # Replace with your actual function
        st.image(generated_image, caption="Generated Image from Predefined Input", use_column_width=True)

if __name__ == "__main__":
    main()
