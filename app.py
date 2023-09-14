
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:21:22 2022

@author: Ammar
"""

import streamlit as st
import joblib


def main():
    
    html_temp="""
    <div style ="background-color:lightblue;padding:16px">
    <h2 style ="color:blue;text-align=center">Churn for Bank Custumers Prodiction Using ML</h2>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
  
  
    model = joblib.load('bankCustmers_cf.sav')
  
    p1 =st.number_input("Enter the Credit Score")
    p2 = st.slider("Enter  the Age",18,100)
    p3 = st.slider("Enter the Tenure",0,10)
    p4 = st.number_input("Enter the Balance") 
    p5 = st.slider("Enter Number of product",1,4) 
    s1=st.selectbox("Has he Credit Card ?",("Yes","No"))
    if s1=="Yes":
     p6=1
    else:
     p6=0
    s2=st.selectbox("Is he a Active Member ?",("Yes","No"))
    if s2=="Yes":
     p7=1
    else:
     p7=0
     
    p8 =st.number_input("Enter the Estimated Salary")
  
    s3=st.selectbox("is he from Germany ?",("Yes","No"))
    if s3=="Yes":
     p9=1
    else:
     p9=0
  
    s4=st.selectbox("is he from Spain ?",("Yes","No"))
    if s4=="Yes":
     p10=1
    else:
     p10=0
  
    s5=st.selectbox("Sex",("Male","Female"))
    if s5=="Male":
        p11=1
    else:
       p11=0
  
    
        
    if st.button('Predict'):
        
     features=[[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]]
     print(features)
     prediction = model.predict(features)
     lc=[str(i)for i in prediction] 
     ans=int("".join(lc))  
     
     if (ans == 0):
             st.error('The Customer will not leave the bank ')
     else:      
             st.success('The Customer will leave the bank ')
                             
           
if __name__ == '__main__':
    main()
    
    

  
    
   
 
       
