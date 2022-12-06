

import streamlit as st

# tittle
st.title('Tasty Express 247')
st.text('Taste you\'ll Remember')



Breakfast, Lunch, Dinner = st.tabs(["Breakfast", "Lunch", "Dinner"])


with Breakfast:
   st.header("Breakfast Subscribers List")
   Special_Breakfast , Normal_Breakfast = st.tabs(["Special Breakfast", "Normal Breakfast"])

   col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with Lunch:
   st.header("Lunch Subscribers List")
   Special_Lunch , Normal_Lunch = st.tabs(["Special Lunch", "Normal Lunch"])

#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with Dinner:
   st.header("Dinner Subscribers List")
   Special_Dinner , Normal_Dinner = st.tabs(["Special Dinner", "Normal Dinner"])

#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)