# General import section
import pandas as pd 
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import os #File navigation

# Streamlit main page configuration, gotta have that eyeball icon!
st.set_page_config(page_title="Ocular Disease Recognition",
                    page_icon=":eye:",
                    layout="wide",
                    initial_sidebar_state="expanded",
                    menu_items=None)

# App import
import Home_Page
import Patient_Analysis

# Data object class
class DataObject():
    """
    Data object class holds a dataframe and its byte size.
    """
    def __init__(self, df=None, filesize=None):
      """The constructor for DataObject class

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
    
    def side_bar(self, userimgs):
      """Sidebar configuration and file picker

      :param dt_obj: pandas dataframe object
      :type dt_obj: pandas.core.frame.DataFrame
      """
    
      upload = st.sidebar.file_uploader("Upload a data file",type=(["jpg"]),accept_multiple_files=True)                   
      if upload is not None: #file uploader selected a file      
        menu = ['Home','Patient Analysis','Data Analysis','Classification','Regression']
        navigation = st.sidebar.selectbox(label="Selection Menu", options=menu)

        # App pages

        # Introduction
        if navigation == 'Home':
          with st.container():
           Home_Page.home()

        # Runs 'Data Preview' app
        if navigation == 'Patient Analysis':
          with st.container():
           Patient_Analysis.patient_analysis(upload)

        # Runs 'Data Preparation' app
        if navigation == 'Data Analysis':
          with st.container():
           Data_Preparation.data_prep(dt_obj)

        # Runs 'Smoothing and filtering' app
        #if navigation == 'Smoothing and filtering':
        #  Smoothing_and_Filtering.smoothing_and_filtering(dt_obj)
        
        # Runs 'Classification' app
        if navigation == 'Classification':
          Classification.classification(dt_obj)  

        # Runs 'Regression' app
        if navigation == 'Regression':
          Regression.regression(dt_obj)
      
      # Initial Home page when there is no file selected
      else:
        Home_Page.home()
        # It deletes Preprocessing and initial datasets from the last run
        #if os.path.isfile("Smoothing_and_Filtering//Preprocessing dataset.csv"):
        #   os.remove("Smoothing_and_Filtering//Preprocessing dataset.csv")
        #if os.path.isfile("Smoothing_and_Filtering//initial.csv"):
        #   os.remove("Smoothing_and_Filtering//initial.csv")

def main():
  """
  Main and its Streamlit configuration
  """

  # Creating an instance of the original dataframe data object                   
  userimgs = DataObject()
  # Creating an instance of the main interface
  UI = User_Interface()
  UI.side_bar(userimgs)


# Run Main
if __name__ == '__main__':
  main()