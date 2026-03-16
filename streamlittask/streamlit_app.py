import streamlit as st


st.title("Streamlit Introduction App")


st.markdown("### Basic Streamlit Demo")


st.image("image.png", caption="Python Programming", width=200)


name = st.text_input("Enter your Name")


age = st.number_input("Enter your Age", min_value=1, max_value=100)

course = st.selectbox(
    "Select your Favorite Programming Language",
    ["Python", "Java", "C++", "JavaScript"]
)


rating = st.slider("Rate your Programming Skill", 1, 10)

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Favorite Language:", course)
    st.write("Skill Rating:", rating)

st.write("This app demonstrates basic Streamlit components.")


st.markdown("**Streamlit makes Python web apps very easy!**")