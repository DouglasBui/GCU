# General import section
import pandas as pd
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import os #File navigation

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax

# App import
import Home_Page
import Instructions
import Patient_Analysis

# Streamlit main page configuration, gotta have that eyeball icon!
st.set_page_config(page_title="Ocular Disease Recognition",
                    page_icon=":eyes:",
                    layout="wide",
                    initial_sidebar_state="expanded",
                    menu_items=None)

# Data object class
class DataObject():
    """
    Data object class holds a dataframe and its byte size.
    """
        
    def __init__(self, df=None, filesize=None):
      """
      The constructor for DataObject class
      :param df: pandas dataframe object, defaults to None
      :type df: pandas.core.frame.DataFrame, optional
      :param filesize: byte size of pandas dataframe, defaults to None
      :type filesize: numpy.int32, optional
      """
      self.df = df
      self.filesize = filesize
        
# Interface class     
class User_Interface():

    def __init__(self):
      """
      Constructor
      """
      pass
      
    def side_bar(self,upload):

      #upload = st.sidebar.file_uploader("Upload a data file",type=(["jpg"]),accept_multiple_files=True)                   
      #if upload is not None:    
        menu = ['Home','Instructions','Patient Analysis']
        navigation = st.sidebar.selectbox(label="Selection Menu", options=menu)
        
        # App pages
        upload = None
        model = None
        
        # Homepage
        if navigation == 'Home':
          with st.container():
           st.markdown(
           '''
           <style>
           body {
           background-image: url("https://i.imgur.com/dwojk7m.png");
           background-size: cover;
           }
           </style>
           ''',
           unsafe_allow_html=True)
           Home_Page.home()
        
        # Runs the Instructions page
        if navigation == 'Instructions':
          with st.container():
           Instructions.instructions()
        
        if navigation == 'Patient Analysis':
          with st.container():
           Patient_Analysis.patient_analysis(upload,model)
           
        # Runs Data Analytics page
        #if navigation == 'Data Analytics':
        #  with st.container():
        #   Patient_Analysis.patient_analysis()
           
           
           
def main():
  """
  Main and its Streamlit configuration
  """
  upload = DataObject()               
  UI = User_Interface()
  UI.side_bar(upload)
# Run Main
if __name__ == '__main__':
  main()