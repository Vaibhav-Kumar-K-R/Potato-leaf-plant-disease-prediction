import numpy as np
import PIL.Image as Image
import tensorflow as tf
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from warnings import filterwarnings
import google.generativeai as genai

filterwarnings('ignore')


def streamlit_config():

    # page configuration
    st.set_page_config(page_title='Classification', layout='centered')

    # page header transparent color
    page_background_color = """
    <style>

    [data-testid="stHeader"] 
    {
    background: rgba(0,0,0,0);
    }

    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)

    # title and position
    st.markdown(f'<h1 style="text-align: center;">Potato Disease Classification</h1>',
                unsafe_allow_html=True)
    add_vertical_space(4)


# Streamlit Configuration Setup
streamlit_config()


# Gemini Suggestion Cache
gemini_cache = {}


# Gemini Suggestion Function
def get_gemini_suggestion(disease_class):
    if disease_class in gemini_cache:
        return gemini_cache[disease_class]

    genai.configure(api_key="")

    prompt = f"""
A potato leaf has been classified as '{disease_class}'.
Give 3 bullet points of clear, simple, and practical suggestions for Indian farmers to handle or treat this disease.
Keep the language easy to understand.
"""

    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
        response = model.generate_content(prompt)
        suggestion = response.text.strip()
        gemini_cache[disease_class] = suggestion
        return suggestion
    except Exception as e:
        return f"Error getting Gemini suggestion: {str(e)}"


def prediction(image_path, class_names=['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']):
    # Open the image
    img = Image.open(image_path)

    # Convert RGBA or grayscale to RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Resize image
    img_resized = img.resize((256, 256))

    # Convert image to array
    img_array = tf.keras.preprocessing.image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)

    # Load model and predict
    model = tf.keras.models.load_model(r'model.h5')
    prediction = model.predict(img_array)

    # Get predicted class and confidence
    predicted_class = class_names[np.argmax(prediction)]
    confidence = round(np.max(prediction)*100, 2)

    # Display results
    add_vertical_space(1)
    st.markdown(f'<h4 style="color: orange;">Predicted Class : {predicted_class}<br>Confident : {confidence}%</h3>',
                unsafe_allow_html=True)

    add_vertical_space(1)
    st.image(img.resize((400, 300)))

    # Gemini Suggestion
    suggestion = get_gemini_suggestion(predicted_class)
    st.markdown("<h4 style='color: green;'>Farming Advice:</h4>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#f0f0f5;padding:10px;border-radius:5px;'>{suggestion}</div>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([0.1, 0.9, 0.1])
with col2:
    input_image = st.file_uploader(label='Upload the Image', type=['jpg', 'jpeg', 'png'])


if input_image is not None:
    col1, col2, col3 = st.columns([0.2, 0.8, 0.2])
    with col2:
        prediction(input_image)
