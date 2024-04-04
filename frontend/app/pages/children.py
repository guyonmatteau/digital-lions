import streamlit as st
from dataclasses import dataclass
from datetime import datetime


"st.session_state object:", st.session_state

# start condition
if "stage" not in st.session_state:
    st.session_state.stage = "base_form"

if "workshop_cancelled" not in st.session_state:
    st.session_state.workshop_cancelled = False

def update_state(state, community, workshop_cancelled):
    # print(f"Updating state to: {state}, {workshop_cancelled}")
    st.session_state.stage = state
    st.session_state.community =st.session_state.my_key
    st.session_state.workshop_cancelled = st.session_state.my_key_cancelled

# def submit_attendance():
    # st.session_state["stage"] = "attendance_submitted"


if st.session_state["stage"] == "base_form":
    with st.form("base_form"):
        # st.write(f"You are filling in the form for {form.date}")
        name = st.text_input("What is your name?")
        community = st.selectbox(
            label="Which community are you from?",
            options=["Community A", "Community B", "Community C"],
            key='my_key'
    )
        
        workshop_cancelled = st.checkbox(label="Is the workshop cancelled?", key='my_key_cancelled')
        submitted = st.form_submit_button(
            "Next", on_click=update_state, args=("base_submitted", community, workshop_cancelled))
        print(community)
        # if submitted:
            # update_state("base_submitted", community, workshop_cancelled)
            # st.session_state.workshop_cancelled = st.session_state.workshop_is_cancelled

elif st.session_state["stage"] == "base_submitted":
    st.write("Thanks for submitting the cancellation of the workshop!")
    st.write("You can now close this tab.")

# elif st.session_state["stage"] == "submit_attendance":
    # with st.form("submit_attendance"):
        # st.write("This is the attendance form")
        # submitted = st.form_submit_button("Submit workshop attendance", on_click=submit_attendance)

# elif st.session_state["stage"] == "attendance_submitted":
    # st.write("Thanks for submitting the attendance!")

        

