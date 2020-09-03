
# !pip install streamlit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from wordcloud import WordCloud

# from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import requests

import streamlit as st
import os

def main():

    df = read_csv("profiles_skills.csv")
    mask = read_image("image.png")
    skills = read_csv("skills.csv")

    # comment_words = '' 
    # stopwords = set(STOPWORDS) 

    st.title(
        """
        Skills 
        """ 
        )
    
    st.markdown("---")

    page = st.sidebar.selectbox("Choose a Profile", skills)

    if page=="ASP .NET MVC":
      image = Image.open('ASP .NET MVC.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Blockchain":
      image = Image.open('Blockchain.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Consultant":
      image = Image.open('Consultant.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="FULL STACK":
      image = Image.open('FULL STACK.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="ML AI DL":
      image = Image.open('ML AI DL.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="ORACLE D2K":
      image = Image.open('ORACLE D2K.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="ORACLE Erp App":
      image = Image.open('ORACLE Erp App.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="ORACLE PLSQL":
      image = Image.open('ORACLE PLSQL.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Public Relations":
      image = Image.open('Public Relations.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Purchase":
      image = Image.open('Purchase-copy.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Quality Assurance and Testing":
      image = Image.open('Quality Assurance and Testing-copy.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Sales":
      image = Image.open('Sales.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Reenforcements AI Architect":
      image = Image.open('Reenforcements AI Architect.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Retail":
      image = Image.open('Retail.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Social Media":
      image = Image.open('Social Media.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="System and network admin":
      image = Image.open('System and network admin-copy.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Web Designer":
      image = Image.open('Web Designer.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="AI Architect":
      image = Image.open('AI Architect.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
    elif page=="Banking":
      image = Image.open('Banking.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="OpenCV":
      image = Image.open('OpenCV.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Data Science":
      image = Image.open('Data Science.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Finance":
      image = Image.open('Finance.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Human resource":
      image = Image.open('Human resource.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Insurance":
      image = Image.open('Insurance.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="JavaJ2EE":
      image = Image.open('JavaJ2EE.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Market research":
      image = Image.open('Market research.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    elif page=="Marketing Mix Modelling":
      image = Image.open('Marketing Mix Modelling.png')

    elif page=="JAVA":
      image = Image.open('JAVA.png')

      st.image(image, caption='Most popular Skills',
                use_column_width=True)
      
    else:
      print("Wrong choice")

  
    
def skills_csv(name):
    df = pd.read_csv(os.getcwd() + "/" + name)
    return df['Profile']
     

def read_csv(name):
    return pd.read_csv(os.getcwd() + "/" + name)


def read_image(name):
    # return pd.read_csv(os.getcwd() + "/" + name)
    return np.array(Image.open(os.getcwd() + "/" + name))
 


if __name__ == "__main__":
    main()
