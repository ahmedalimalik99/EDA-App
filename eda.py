# Import libraries
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown("""
# **Exploratory Data Analysis Web Application**
This app is developed by Ahmed Ali Malik
""")

# Sidebar - File Uploader
with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=['csv'])
    st.sidebar.markdown("---")
    st.sidebar.write("Or use example datasets below:")

# Load default dataset (Titanic)
df = sns.load_dataset('titanic')

# Function to load user-uploaded CSV
@st.cache_data
def load_csv(file):
    csv = pd.read_csv(file)
    return csv

# Main Logic
if uploaded_file is not None:
    df = load_csv(uploaded_file)
    pr = ProfileReport(df, explorative=True)
    st.header("**Input DataFrame**")
    st.write(df)
    st.write("---")
    st.header("**Pandas Profiling Report**")
    st_profile_report(pr)

else:
    st.info("👆 Please upload a CSV file to start the analysis.")
    if st.button("Or Press to Use Example Random Data"):
        @st.cache_data
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5), columns=['A', 'B', 'C', 'D', 'E'])
            return a

        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header("**Example Input DataFrame**")
        st.write(df)
        st.write("---")
        st.header("**Pandas Profiling Report**")
        st_profile_report(pr)
