import streamlit as st
from PIL import Image
from pydantic_core import ValidationError

from streamlit_cad_webapp.common.download_image_with_url import get_image_from_url
from streamlit_cad_webapp.common.validate_url import URL
from streamlit_cad_webapp.controllers.api_send_binary_image import send_request_to_API
from streamlit_cad_webapp.controllers.api_send_url_image import send_request_to_API_URL

st.set_page_config(
    page_title="Vehicle Crash Detection App",
    page_icon=":camera:",
    initial_sidebar_state='auto'
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write("""
         # Vehicle Crash Detection with Binary Image Classification
         """
         )

tab_img_upload, tab_img_link, tab_info = st.tabs(["Upload Image", "Send link to Image", "Info"])

with tab_img_upload:
    file = st.file_uploader(type=["jpg", "png", "jpeg", "webp"], label="Upload an image")

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        with st.spinner('Processing..'):
            predicted_class, accuracy = send_request_to_API(image)

        st.sidebar.info("Accuracy: " + str(accuracy) + " %")

        string = "Detected Class: " + predicted_class

        if predicted_class == 'clean':
            st.balloons()
            st.sidebar.success(string)
        elif predicted_class == 'damaged':
            st.sidebar.warning(string)

            # Add remedy suggestions based on the predicted class
            if predicted_class == 'damaged':
                st.info(f"Vehicle is damaged with {accuracy} probability.")

        else:
            st.sidebar.error(string)
            st.error("Unknown Error occurred - No vehicle found in the image. Please try again.")

with tab_img_link:
    link_to_image = st.text_input('The URL link to the image')
    button = st.button('Submit')
    if button:
        try:
            url = URL(url=link_to_image).url
            image = get_image_from_url(url)
            if image is None:
                st.error("Failed to download image from URL. Please try again.")
            else:
                st.image(image, use_column_width=True)

                with st.spinner('Processing..'):
                    predicted_class, accuracy = send_request_to_API_URL(url)

                st.sidebar.info("Accuracy: " + str(accuracy) + " %")

                string = "Detected Class: " + predicted_class

                if predicted_class == 'clean':
                    st.balloons()
                    st.sidebar.success(string)
                elif predicted_class == 'damaged':
                    st.sidebar.warning(string)

                    # Add remedy suggestions based on the predicted class
                    if predicted_class == 'damaged':
                        st.info(f"Vehicle is damaged with {accuracy} probability.")

                else:
                    st.sidebar.error(string)
                    st.error("Unknown Error occurred - No vehicle found in the image. Please try again.")

        except ValidationError as e:
            st.error("Please enter a valid URL")


with tab_info:
    st.write("coming soon..")
