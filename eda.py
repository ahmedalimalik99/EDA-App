# import libraries
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp tittle
st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by Ahmed Ali Malik
''')

# how to upload a file from pc
with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    # st.sidebar.markdown("[Example CSV file](df)")

# profiling report for pandas

if uploaded_file is not None:
    st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file, kindly upload file!')
    if st.button('Press to use example data'):
        # example dataset
        st.cache_data
        def load_data():
            a = pd.DataFrame( np.random.rand(100,5),
                             columns=['A','B','C','D','E'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)