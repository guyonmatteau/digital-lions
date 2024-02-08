"""Main entrypoint of simple Form"""
from dataclasses import dataclass
from datetime import datetime

import streamlit as st

st.title("Big Hippo Attendance")


@dataclass
class Form:
    name: str = None
    community: str = None
    datetime: datetime = datetime.today()
    date: datetime = datetime.today().strftime("%A %d %B %Y")


form = Form()

with st.form("form"):
    st.write(f"You are filling in the form for {form.date}")
    name = st.text_input("What is your name?")  # to be replaced with login
    community = st.selectbox(
        label="Which community are you from?",
        options=["Community A", "Community B", "Community C"],
    )
    cancelled = st.checkbox("Is this workshop cancelled due to weather?")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Name", name)
        st.write("Community", community)
        st.write("Cancelled?", cancelled)
