from dataclasses import dataclass
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Workshop attendance")
st.title("Workshop attendance")


if 'stage' not in st.session_state:
    st.session_state.stage = 0
 
def set_stage(stage):
    st.session_state.stage = stage


@dataclass
class Form:
    name: str = None
    community: str = None
    datetime: datetime = datetime.today()
    date: datetime = datetime.today().strftime("%A %-d %B %Y")


form = Form()
cancelled = True

with st.form("workshop_cancelled"):
    st.write(f"You are filling in the form for {form.date}")
    name = st.text_input("What is your name?")  # to be replaced with login
    community = st.selectbox(
        label="Which community are you from?",
        options=["Community A", "Community B", "Community C"],
    )
    cancelled = st.checkbox("Is this workshop cancelled due to weather?")

    submitted = st.form_submit_button("Next")


if not cancelled:
    with st.form("attendance"):
        st.write("This is the form for submitting the attendance")
        submitted_attendance = st.form_submit_button("Submit", on_click=set_stage, args=(2,))

if st.session_state.stage > 1:
    st.write("Thanks for submitting the form")
