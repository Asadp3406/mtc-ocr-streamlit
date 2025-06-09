import streamlit as st
from PIL import Image
import pytesseract

st.title("MTC OCR Web App")
st.write("Upload an image of an MTC (Material Test Certificate) to extract text.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Extract Text"):
        with st.spinner("Processing..."):
            text = pytesseract.image_to_string(image)
            st.subheader("Extracted Text:")
            st.text_area("Text", text, height=300)
