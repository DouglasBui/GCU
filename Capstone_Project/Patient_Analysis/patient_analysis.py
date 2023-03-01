import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
import os
import h5py
import zipfile
import tempfile

def main(upload,model):
    
    st.subheader("Upload Fundus Images")
    upload = st.file_uploader("Upload a data file",type=(["jpg"]),accept_multiple_files=True)
    
    st.subheader("Upload Model in ZIP Form")
    model = st.file_uploader('Load in Model here', type='zip')
    
    st.subheader("Patient ID Input")
    sel_col, disp_col = st.columns(2)
    userinput = sel_col.text_input('Please provide a patient ID number.')
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    if len(userinput) !=0:
        left = "{}_left.jpg".format(userinput)
        right = "{}_right.jpg".format(userinput)
        
        for img in upload:
            if img.name == left:
                img1 = Image.open(img)
            elif img.name == right:
                img2 = Image.open(img)
        left = "{}_left.jpg".format(userinput)
        right = "{}_right.jpg".format(userinput)
        
        #stream = st.file_uploader('Load in Model here', type='zip')
        if model is not None:
            myzipfile = zipfile.ZipFile(model)
            with tempfile.TemporaryDirectory() as tmp_dir:
                myzipfile.extractall(tmp_dir)
                root_folder = myzipfile.namelist()[0] # e.g. "model.h5py"
                model_dir = os.path.join(tmp_dir, root_folder)
                #st.info(f'trying to load model from tmp dir {model_dir}...')
                classifier = tf.keras.models.load_model(model_dir)
                
            with col1:
                st.subheader("Left Eye")
                figure = plt.figure()
                plt.imshow(img1)
                plt.axis('off')
                st.pyplot(figure)
         
            with col2:
                st.subheader("Right Eye")
                figure = plt.figure()
                plt.imshow(img2)
                plt.axis('off')
                st.pyplot(figure)
       
            with col3:
                st.subheader("Diagnosis: Left")
                pred1 = predict(img1,classifier)
                st.write(pred1)
        
            with col4:
                st.subheader("Diagnosis: Right")
                pred2 = predict(img2,classifier)
                st.write(pred2)

def predict(img,classifier):
    #classifier = tf.keras.models.load_model(r'C:\Users\David\OneDrive\Documents\GitHub\Capstone_Project\CNN.h5py')
    shape = ((128,128,3))
    #model = tf.keras.Sequential(hub[hub.KerasLayer(classifier, input_shape=shape)])
    test_image = img.resize((128,128))
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image/255.0
    test_image = np.expand_dims(test_image,axis=0)
    class_names = ['Abnormal','AMD','Cataract','Glaucoma','Myopia','Normal']
    prediction = classifier.predict(test_image)
    scores = tf.nn.softmax(prediction[0])
    scores = scores.numpy()
    image_class = class_names[np.argmax(scores)]
    result = "{}",format(image_class)
    return result
    
# Main
if __name__ == "__main__":
   main()