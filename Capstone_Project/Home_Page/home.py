import streamlit as st
import os

def main():
    """Home main
    """    
    st.title("Ocular Disease Recognition")
    
    st.subheader("Welcome")
    st.write("""
             This is a web-based app that is designed to help professionals within the medical field by
             analyze singular or mass datasets of ocular fundus images, which are photos that peer inside 
             the eye and displays the optical nerves. These images are then classified into 7 categories of
             diagnosis.
             """)
             
    st.subheader("User Instructions")
    st.write("""
            - Be sure of the quality of the data you are providing. This model has some requirements for its use.
                **Requirements:**
                1. Make sure to provide a patient ID number at the start of each image file that ends with an _left.jpg or _right.jpg
                2. It helps to have your fundus images trimmed to minimize runtime, with in the GitHub 
                link below there is a Datascrub.ipynb that can show you how.
                3. Move to the data analysis tab to analyze the image classificaiton.
                
            - Upload your fundus images file into the top left corner of the sidebar, you are also provided some in a download link below.
             
             
             """)
             
    st.subheader("Classification Types")
    st.markdown("""
                This is the list of classifications within the csv file, following this exact order.
                **(0) Normal:** A Normal Fundus
                
                **(1) Diabetes:** Symptoms are mild and moderate non profliferative retinopathy
                
                **(2) Glaucoma:**
                
                **(3) Cataract:** The image is very blurred.
                
                **(4) Age-related Macular Degeneration (AMD):**
                
                **(5) Hypertension:**
                
                **(6) Pathological Myopia:** This condition normally inflicts both eyes
                
                **(7) Abnormal:** Images that don't match any of the classifications, and require further medical examination.
                """)
                
    st.write("")
    st.subheader("Test Samples for Users")
    st.markdown("""
                Here you can select and download an image file for user interface testing
                """)

                
    st.subheader("For more indepth information on this project take a look at the GitHub Source Code()")
    
    # two remove the previous load of both eyes
   # if os.path.isfile("user_data//user_data.jpg"):
        #os.remove("user_data//*_left.jpg")
        #os.remove("user_data//*_right.jpg")

    # To delete leftover files from the previous runs
    #if os.path.isfile("Smoothing_and_Filtering//Preprocessing dataset.csv"):
        #os.remove("Smoothing_and_Filtering//Preprocessing dataset.csv")
            
    #if os.path.isfile("Smoothing_and_Filtering//Filtered Dataset.csv"):
        #os.remove("Smoothing_and_Filtering//Filtered Dataset.csv")

    #if os.path.isfile("Smoothing_and_Filtering//initial.csv"):
        #os.remove("Smoothing_and_Filtering//initial.csv")