import streamlit as st
from utils import api, communities

st.set_page_config(page_title="Digital Lions")
st.title("Children")
st.write("On this page you can add a child to the database.")

# this is for debugging purposes
"st.session_state object:", st.session_state

def update_state(state):
    st.session_state.stage = state
    # st.session_state.name = 

st.session_state.page = "children"

if "stage" not in st.session_state and st.session_state.page == "children":
    st.session_state.stage = "add"

if st.session_state.stage == "submitted" and st.session_state.page == "children":
    st.write(f"{st.session_state.first_name} {st.session_state.last_name} has been added to the database.")
    st.button(
            "Add another one", on_click=update_state, args=["add"]
        )

if st.session_state.stage == "add" and st.session_state.page == "children":

    with st.form("child_form"):
        st.text_input("First name", key="first_name")
        st.text_input("Last name", key="last_name")
        st.selectbox("Community", key="community", options=communities)
        submitted = st.form_submit_button(
                "Add", on_click=update_state, args=["submitted"]
            )
