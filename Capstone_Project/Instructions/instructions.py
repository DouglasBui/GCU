import streamlit as st
import os

def main():
    st.title("Instructions")

    st.write("""
            - Be sure of the quality of the data you are providing. This model has some requirements for its use.
                **Requirements:**
                1. Make sure to provide a patient ID number at the start of each image file that ends with an _left.jpg or _right.jpg
                
                2. It helps to have your fundus images trimmed to minimize runtime, with in the GitHub 
                link below that contains fundus images the user can upload to this web app.
                
                3. Upload your fundus images file into the top left corner of the sidebar, you are also provided some in a download link below.
                
                4. Move to the data analysis tab to analyze the image classificaiton.
                
                5. Type in the patient id number you want to see and the images of each patient eye should show below, along with a diagnosis of the classification.
                
                6. The next tab is the "Data Retrieval" tab where a csv file can be download with the information classified for each patient.
                
                7. The final tab is the Reviewing the model, where the user can understand the accuracy and parameters of the model. This is to insure the user of the model's functionality.
             """)
             
    st.subheader("Classification Types")
    st.markdown("""
                This is the list of classifications within the csv file, following this exact order.
                **(0) Normal:** A Normal Fundus
                
                **(1) Diabetes:** Symptoms are mild and moderate non profliferative retinopathy
                
                **(2) Glaucoma:** This condition deals damage to the optic nerve, which is responsible for carrying visual information from the eye to the brain. This damage is often caused by elevated pressure inside the eye, which is called intraocular pressure (IOP).
                
                **(3) Cataract:** These images tend to be very blurred.
                
                **(4) Age-related Macular Degeneration (AMD):**
                
                **(5) Pathological Myopia:** This condition normally inflicts both eyes
                
                **(6) Abnormal:** Images that don't match any of the classifications, and require further medical examination.
                """)
                
    st.write("")
    st.subheader("Test Samples for Users")
    st.markdown("""
                Here you can select and download an image file for user interface testing.
                """)
    st.subheader("(https://github.com/DouglasBui/GCU/tree/main/Capstone_Project)")
    