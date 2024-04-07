from datetime import datetime

import streamlit as st


st.set_page_config(page_title="Digital Lions")
st.title("Workshop attendance")
st.write("On this page you can cancel or submit the attendance for a workshop.")

children = ["Pietje", "Klaasje", "Jantje"]
coaches = ["Anne", "Stijn", "Nomfundo"]
communities = ["Community A", "Community B", "Community C"]

# this is for debugging purposes
"st.session_state object:", st.session_state

if "date" not in st.session_state:
    datetime: datetime = datetime.today()
    date: datetime = datetime.today().strftime("%A %-d %B %Y")
    st.session_state.datetime = datetime
    st.session_state.date = date

if "stage" not in st.session_state:
    st.session_state.stage = "base_form"

if "workshop_cancelled" not in st.session_state:
    st.session_state.workshop_cancelled = False

if "community" not in st.session_state:
    st.session_state.community = None

if "name" not in st.session_state:
    st.session_state.name = None

def update_state(state):
    st.session_state.stage = state

if st.session_state["stage"] == "base_form":
    with st.form("base_form"):
        st.write(f"Today is {st.session_state.date}")
        st.selectbox(label="What is your name?", options=coaches, key='name')
        st.selectbox(
            label="Which community are you from?",
            options=communities,
            key='community'
        )
        
        workshop_cancelled = st.checkbox(label="Is the workshop cancelled?", key='workshop_cancelled')
        submitted = st.form_submit_button(
            "Next", on_click=update_state, args=["base_submitted"])

elif st.session_state.stage == "base_submitted" and st.session_state.workshop_cancelled is False:
    with st.form("submit_attendance"):
        community = st.session_state.community
        
        st.write(f"Please tick the children that attended the workshop in {st.session_state.community} today.")

        for child in children:
            st.checkbox(label=child, key=f"attendance_{child}")


        submitted = st.form_submit_button("Submit workshop attendance", on_click=update_state, args=["attendance_submitted"])
        

elif st.session_state.stage == "attendance_submitted" or st.session_state.workshop_cancelled is True:
    st.write(f"You have successfully cancelled the workshop in {st.session_state.community} for {st.session_state.date}.")
    st.write("You can now close this tab.")
 
elif st.session_state.stage == "attendance_submitted" and st.session_state.workshop_cancelled is False:
    st.write("Thanks for submitting the attendance for today.")
    st.write("You can now close this tab.")
        
