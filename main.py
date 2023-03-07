import streamlit as st
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import random
import string
import requests


cloudinary.config(
  cloud_name = st.secrets['cloud_name'],
  api_key = st.secrets['api_key'],
  api_secret = st.secrets['api_secret'],
  secure = True
)

first_time = []
r_id = []

st.set_page_config(layout="wide", page_title="Expresso")

# main page
st.balloons()
st.write("<h1 style='text-align: center;'>Expresso</h1>", unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>All in one tool to Experiment with your images :)</h3>", unsafe_allow_html=True)
st.write("Choose Input Method:")
my_upload = None
input_method = st.selectbox('Select an input method:', ('Select an option', 'Upload An Image', 'Take Input From Camera'))
if input_method is not None:
    if input_method == 'Upload An Image':
        my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    elif input_method == 'Take Input From Camera':
        my_upload = st.camera_input("Take a picture")
if my_upload is not None:
    operations = st.selectbox('Select an operation to try:', ('Select an option', 'Resize Operations', 'Effects', 'Layer Effects', 'Enhancing Tools', 'Other Helpful Tools'))
    if operations is not None:
        if operations == 'Resize Operations':
            sub_operations = st.selectbox('What opreation would you like to perform from Resize Opreations available:', ('Select an operation', 'Scale', 'Limit Fit', 'Fill', 'Fit', 'Crop', 'Minimum Fit'))
            if sub_operations is not None:
                if sub_operations == 'Scale':
                    st.info("Resize the asset exactly to the specified width and height. All the orginal asset parts are visible, but might be streched or shrunk if the dimension you request have a different aspect ratio than the original.")
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, crop="scale")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Limit Fit':
                    st.info("Same as the fit mode but only if the original asset is larger than the specified limit(width and height), in which case the asset is scaled down so that it takes up as much space as possible within a bounding box defined by the specified width and height parameters. The original aspect ratio is retained(by default) and all of the original asset is visible. This mode doesn't scale up the asset if your requested dimension are larger than the original image size.")
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, crop="limit")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Fill':
                    st.info("Creates an asset with exact specified width and height without distorting the asset.")
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, crop="fill")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Fit':
                    st.info("Scales the asset up or down so that it takes up as much space as possible")
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, crop="fit")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Crop':
                    st.info("Extracts the specified size from the original image without distorting or scaling the delivered asset.")
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                        direction = st.selectbox("Select Direction:", ("Center", "North", "South", "East", "West", "North West", "North East", "South East", "South West"))
                        dict = {"Center": "center", "North":"north", "South": "south", "East": "east", "West": "west", "North West": "north_west", "South West": "south_west", "North East": "north_east", "SouthEast": "south_east"}
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, crop="crop", gravity=dict[direction])
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Minimum Fit':
                    st.info("The minimum fit mode is the same as the fit mode but only if the original image is smaller than than the specified minimum(width and height), in which case the image is scaled up so that it takes up as much space as possible within a bounding box defined by the specified width and height parameters. The original aspect ratio is retained by default and all of the original image is visible. This mode doesn't scale down the image if your requested dimensions are smaller thant the original image's.")
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, crop="mfit")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
        elif operations == 'Effects':
            sub_operations = st.selectbox("What opreation would you like to perform from Effects available:", ('Select an Effect', 'Blur Face', 'Pixelate Portion', 'Convert to Grayscale'))
            if sub_operations is not None:
                if sub_operations == 'Blur Face':
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", effect="blur_faces:2000")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Pixelate Portion':
                    col1, col2 = st.columns(2)
                    with col1:
                        width = st.number_input("Width", min_value=1, max_value=1000, value=100)
                        x = st.number_input("X", min_value=1, max_value=1000, value=100)
                    with col2:
                        height = st.number_input("Height", min_value=1, max_value=1000, value=100)
                        y = st.number_input("Y", min_value=1, max_value=1000, value=100)
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", width=width, height=height, x=x, y=y, crop="fill", effect="pixelate_region")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
                elif sub_operations == 'Convert to Grayscale':
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", effect="grayscale")
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{image["url"]}" download>Download Image</a>', unsafe_allow_html=True)
                    st.image(image['url'])
        elif operations == 'Layer Effects':
            sub_operations = st.selectbox("What opreation would you like to perform from Layers Effects available:", ('Select an Effect', 'Text Layer'))
            if sub_operations is not None:
                if sub_operations == 'Text Layer':
                    col1, col2 = st.columns(2)
                    with col1:
                        font_family = st.selectbox('Select Font Family:', ("Arial", "Georgia", "Roboto", "Times New Roman", "Helvetica", "Open Sans", "Verdana", "Trebuchet Ms", "Courier New"))
                        font_size = st.number_input("Font Size", min_value=1, max_value=1000, value=100)
                        color_code = st.color_picker('Pick Font Color', '#000000')
                        st.write('The current color is', color_code)
                    with col2:
                        position = st.selectbox("Placement Position", ("Center", "North", "South", "East", "West", "North West", "North East", "South East", "South West"))
                        dict = {"Center": "center", "North":"north", "South": "south", "East": "east", "West": "west", "North West": "north_west", "South West": "south_west", "North East": "north_east", "SouthEast": "south_east"}
                        text = st.text_input("Text", "Hello World")
                    r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    while r in r_id:
                        r = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                    r_id.append(r)
                    image = upload(my_upload, public_id=f"test_{r}", color=color_code, overlay={"font_family":font_family, "font_size":font_size, "text":text}, gravity=dict[position])
                    st.write("<h3>Output Image:</h3>", unsafe_allow_html=True)
                    response = requests.get(image['url'])
                    img_data = response.content
                    st.download_button(label="Download Image", data=img_data, file_name="image.jpg", mime="image/jpg")
                    st.image(image['url'])
        elif operations == "Enhancing Tools":
            sub_operations = st.selectbox('What Enchancing opreation would you like to perform from Resize Opreations available:', ('Select an operation', 'Improve', 'Limit Fit', 'Fill', 'Fit', 'Crop', 'Minimum Fit'))
    else:
        pass
else:
    pass
