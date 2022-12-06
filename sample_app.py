import streamlit as st

# tittle
st.title('Tasty Express 247')
st.text('Taste you\'ll Remember')

# header
st.header('Tasty Express 247')

# this is subheader
st.subheader('This is a subheader')


st.caption('This is a string that explains something above.(caption)')





# copy code
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


# to display mathametical expressions
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')




tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)