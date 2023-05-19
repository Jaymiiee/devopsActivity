import streamlit as st
import tensorflow as tf
from PIL import Image

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('finals11.hdf5')
  return model
model=load_model()

# The side bar that contains radio buttons for selection of charts
with st.sidebar:
    st.header('Select the image that you would like to display')
    chart = st.radio(
    "Select the image that you would like to display",
    ('Lion', 'Cheetah'))

st.title("Lion or Cheetah Classifier")
st.info("An image classifying project that differentiates between two very similar-looking wild cats: Cheetahs and Lion using Python and TensorFlow")

image = Image.open('LionCheetah.png')
st.image(image, caption='Lion vs Cheetah')

    


# This container will be displayed below the text above
    with st.container():
        col1, col2, col3 = st.columns((20,50,20))

    with col2:
        st.header("Global emissions since 1850")
        st.info("""Select a year with the slider to see the intensity
                of emissions change in each country""")
        
#st.write("""
# Lion or Cheetah Classification""")
file=st.file_uploader("Choose photo from computer, must be a lion or cheetah",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(64,64)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Lion','Cheetah']
    string="The picture shown above is a : "+class_names[np.argmax(prediction)]
    st.success(string)
