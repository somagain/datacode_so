import streamlit as st
import pandas as pd
import math
from pathlib import Path
from PIL import Image    
import numpy as np
import plotly.figure_factory as ff


raw_ds_df = pd.read_csv(r'C:\Users\HP\Desktop\DATALAB\pythonclasses\Data-code.streamlit.io\data\ds_data.csv')

raw_ds_df.rename(columns=lambda x: 
                     x.replace('Year_', ''), inplace= True)
    

st.table(raw_ds_df)
raw_ds_df.to_csv(r'C:\Users\HP\Desktop\DATALAB\pythonclasses\Data-code.streamlit.io\data', index=False)    