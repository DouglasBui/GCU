import streamlit as st #streamlit backend
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
import os #File navigation
import h5py

def main(upload):
    """Data Preview main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("Patient ID Input")
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
            st.subheader("Diagnosis:")
            pred1 = predict(img1)
            st.write(pred)
        
        with col4:
            st.subheader("Diagnosis")
            pred2 = predict(img2)
            st.write(pred2)

def predict(img):
    classifier = tf.keras.models.load_model(r'C:\Users\David\OneDrive\Documents\GitHub\Capstone_Project\CNN.h5py')
    shape = ((256,256,3))
    model = tf.keras.Sequential(hub[hub.KerasLayer(classifier, input_shape=shape)])
    test_image = img.resize((256,256))
    test_image = preprocessing.image.img_toarray(test_image)
    test_image = test_image/255.0
    test_image = np.expand_dims(test_image,axis=0)
    class_names = ['Abnormal','AMD','Cataract','Glaucoma','Myopia','Normal']
    prediction = model.predict(test_image)
    scores = tf.nn.softmax(predictions[0])
    scores = scores.numpy()
    image_class = class_names[np.argmax(scores)]
    result = "{}",format(image_class)
    return result
    
# Main
if __name__ == "__main__":
   main()