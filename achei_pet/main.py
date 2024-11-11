import streamlit as st
from achei_pet.utils.init_session import init_session
from achei_pet.utils.styles import config_page
from achei_pet.page.signup_page import signup_page
from achei_pet.utils.init_session import init_session, reset_session
from achei_pet.page.orchestrate_pages import orchestrate
from achei_pet.page.login_page import login_page

init_session()
try:
    st.set_page_config(
        page_title="AcheiPet",
        layout="wide",
        page_icon='data/logo.png')
except Exception as e:
    print(e)

config_page()

if st.session_state['authenticated']:
    orchestrate()
else:
    if st.session_state['page'] == 'login':
        reset_session()
        login_page(guest_mode=True)
    elif st.session_state['page'] == 'signup':
        signup_page(
            extra_input_params=True,
            confirmPass = True
        )