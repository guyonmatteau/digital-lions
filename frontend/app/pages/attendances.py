import streamlit as st

# this is for debugging purposes
"st.session_state object:", st.session_state

if "stage" not in st.session_state:
    st.session_state.stage = "base_form"

if "workshop_cancelled" not in st.session_state:
    st.session_state.workshop_cancelled = False

def update_state(state):
    st.session_state.stage = state

if st.session_state["stage"] == "base_form":
    with st.form("base_form"):
        # st.write(f"You are filling in the form for {form.date}")
        name = st.text_input("What is your name?")
        st.selectbox(
            label="Which community are you from?",
            options=["Community A", "Community B", "Community C"],
            key='community'
        )
        
        workshop_cancelled = st.checkbox(label="Is the workshop cancelled?", key='workshop_cancelled')
        submitted = st.form_submit_button(
            "Next", on_click=update_state, args=["base_submitted"])

elif st.session_state.stage == "base_submitted" and st.session_state.workshop_cancelled is False:
    st.write("From to submit attendance")
    with st.form("submit_attendance"):
        st.write("This is the attendance form")
        submitted = st.form_submit_button("Submit workshop attendance", on_click=update_state, args=["attendance_submitted"])


elif st.session_state.stage == "attendance_submitted" or st.session_state.workshop_cancelled is True:
    st.write("Thanks for submitting the cancellation of the workshop!")
    st.write("You can now close this tab.")
        
