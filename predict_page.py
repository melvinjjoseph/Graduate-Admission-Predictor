import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pk1','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()
regressor=data["model"]

def show_predict_page():
    st.title("Graduate Admission Predictor")
    st.write("""### Enter the details to predict your chances of getting admission""")

    gre = st.slider("GRE Score (out of 340):", 100, 340, 100, step = 1)
    toefl = st.slider("TOEFL Score (out of 120):", 60, 120, 60, step = 1)
    sop = st.slider("Statement Of Purpose Score (out of 5):", value = 0.0, min_value = 0.0, max_value = 5.0, step = 0.5)
    lor = st.slider("Letter Of Recommendation Score (out to 5):", value = 0.0, min_value = 0.0, max_value = 5.0, step = 0.5)
    resc = st.selectbox('Research Experience:', ("Yes", "No"))
    cgpa = st.slider("Enter CGPA (out of 10):",value=5.0,min_value=5.0,max_value=10.0,step=0.05)

    ok=st.button("Calculate your chance")

    
    if ok:
        if resc=="Yes":
            resc1=1
        else:
            resc1=0
        for rank in range(1,6):
            x=np.array([[gre,toefl,rank,sop,lor,cgpa,resc1]])

            chance=regressor.predict(x)
            if chance<0:
                chance=0
            st.info("You have a %.2f percent chance of getting into a university of rating %d." %(chance*100,rank))
            if chance>= 0.6667:
                st.success('Congratulations! You are eligible to apply for this university!')
            else:
                st.caption('Better Luck Next Time :)')
    
    st.markdown("#")
    st.markdown("#")
    st.markdown("#")
    st.caption('Data source- https://www.kaggle.com/datasets/mohansacharya/graduate-admissions')
    st.info("Melvin J Joseph  [Github](https://github.com/melvinjjoseph) [LinkedIn](https://www.linkedin.com/in/melvin-j-joseph/)")
