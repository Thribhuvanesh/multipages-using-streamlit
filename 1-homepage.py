import streamlit as st
st.set_page_config(
    page_title="Multipage",
)
st.title("Main Page")
st.sidebar.success("Select a page above")
if "my_input" not in st.session_state:
    st.session_state["my_input"]="" 
my_input = st.text_input("Input a Text Here",st.session_state["my_input"])
submit = st.button("submit")
if submit:
    st.session_state["my_input"]= my_input
    st.write("You Have entred: ",my_input)