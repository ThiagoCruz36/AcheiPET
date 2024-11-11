import streamlit as st
from achei_pet.utils.db_handler import authenticate_user
import time

# Pages
def login_page(guest_mode=False):
    col1, col2 = st.columns([1,1])
    
    with col1:
        st.image("data/login.png", use_column_width=True)
    
    with col2:
        st.markdown("<h2 style='text-align: center;'>LOGIN</h2>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 10%;'></div>", unsafe_allow_html=True)
        email = st.text_input("E-mail")
        password = st.text_input("Senha", type="password")

        st.markdown("<div style='margin-top: 10%;'></div>", unsafe_allow_html=True)
        if st.button("Login", use_container_width=True):
            time.sleep(1)
            if not (email and password):
                st.error("Por favor, informe seu e-mail e senha")
            elif authenticate_user(email, password):
                st.session_state['authenticated'] = True
                st.session_state['page'] = 'orchestrate_pages'
                st.session_state['pagina_atual'] = 'pets_abandonados'
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos")

        if st.button("Cadastrar-se", use_container_width=True):
            st.session_state['page'] = 'signup'
            st.rerun()
            
        if guest_mode:
            if st.button("Continuar como convidado", use_container_width=True):
                st.session_state['guest_mode'] = True
                st.session_state['authenticated'] = True
                st.session_state['page'] = 'orchestrate_pages'
                st.session_state['pagina_atual'] = 'pets_abandonados'
                st.rerun()
