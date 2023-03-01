import streamlit as st
import os

def main():
    """
    Home main
    """   
    # Streamlit main page configuration, gotta have that eyeball icon!
    #st.set_page_config(page_title="Ocular Disease Recognition",
    #                page_icon=":eye:",
    #                layout="wide",
    #                initial_sidebar_state="expanded",
    #                menu_items=None)
                    
    st.title("Ocular Disease Recognition")
    
    st.markdown(
        '''
        <style>
        body {
        background-image: url("https://i.imgur.com/dwojk7m.png");
        background-size: cover;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
        
    st.subheader("Welcome")
    st.write("""
             This is a web-based app that is designed to help volunteers within the medical field by
             analyze singular or mass datasets of ocular fundus images, which are photos that peer inside 
             the eye and displays the optical nerves. These images are then classified into 7 categories of
             diagnosis.
             """
    )
             
    st.subheader("Mission Statement")
    st.write("""
            - The primary goal of this project is to successfully train a machine learning algorithm that can differentiate between multiple classifications of diseases that cause visual impairment. The classifications that are most important are for early detection, since most visual impairments are preventable today, and early detection can be rather difficult find for many practitioners.
            """
    )

    