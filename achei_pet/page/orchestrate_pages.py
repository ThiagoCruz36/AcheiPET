import streamlit as st
from achei_pet.utils.styles import render_header
from achei_pet.page.login_page import login_page
from achei_pet.page.signup_page import signup_page
from achei_pet.utils.init_session import init_session, reset_session
from achei_pet.page.add_new_pet import show_add_pet
from achei_pet.page.pets_abandonados import show_pet_abandonado
from achei_pet.page.pets_perdidos import show_pet_perdido

def orchestrate():
    render_header()

    if st.session_state['authenticated']:
        if st.session_state['pagina_atual'] == 'pets_perdidos':
            show_pet_perdido()
        elif st.session_state['pagina_atual'] == 'pets_abandonados':
            show_pet_abandonado()
        elif st.session_state['pagina_atual'] == 'cadastrar_pet':
            show_add_pet()
    else:
        if st.session_state['page'] == 'login':
            reset_session()
            login_page(guest_mode=True)
        elif st.session_state['pagina_atual'] == 'pets_perdidos':
            show_pet_perdido()
        elif st.session_state['pagina_atual'] == 'pets_abandonados':
            show_pet_abandonado()
        elif st.session_state['page'] == 'signup':
            signup_page(
                extra_input_params=True,
                confirmPass = True
            )
