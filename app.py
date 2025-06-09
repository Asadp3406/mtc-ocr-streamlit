import streamlit as st
from PIL import Image
import easyocr

st.title("MTC OCR App")
st.write("Upload an image of your MTC certificate below:")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Extract Text"):
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(np.array(image), detail=0)
        st.subheader("Extracted Text:")
        st.text("\n".join(result))
