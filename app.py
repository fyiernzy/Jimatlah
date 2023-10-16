import streamlit as st
import pandas as pd
import numpy as np

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))
# Create a text input field
user_input = st.text_input("Enter your name:")

# Create a submit button
if st.button("Submit"):
    # Process the user's input
    st.write(f"Hello, {user_input}!")