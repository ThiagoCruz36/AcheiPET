import streamlit as st
import re
from achei_pet.utils.db_handler import save_user, verify_duplicate_user
import time

def is_valid_email(email):
    """Check if the provided email is valid using regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def input_field(input_param, type):
    """Render an input field based on the type and store the value in session state."""
    if type == 'text':
        st.session_state[input_param] = st.text_input(input_param)
    elif type == 'number':
        st.session_state[input_param] = st.number_input(input_param, step=1)

def send_new_user():
    st.success("Sucesso")
    time.sleep(1)
    st.session_state['verifying'] = False
    save_user(st.session_state['email'], st.session_state['password'], st.session_state['name'])
    st.session_state['page'] = 'login'
    st.rerun()

def signup_page(extra_input_params=False, confirmPass=False):
    """Render the signup page with optional extra input parameters and password confirmation."""
    if st.session_state['verifying']:
        # Check if the user already exists
        if verify_duplicate_user(st.session_state['email']):
            st.error("Usuário já cadastrado")
            time.sleep(1)
            st.session_state['verifying'] = False
            st.rerun()
                
    else:
        if st.button("Retornar para o Login"):
            st.session_state['page'] = 'login'
            st.rerun()
        
        st.markdown("<h2 style='text-align: center;'>Cadstrar-se</h2>", unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 5%;'></div>", unsafe_allow_html=True)
        st.session_state['name'] = st.text_input("Nome")
        # Email input with validation
        st.session_state['email'] = st.text_input("E-mail")
        if st.session_state['email'] and not is_valid_email(st.session_state['email']):
            st.error("Please enter a valid email address")

        # Password input
        st.session_state['password'] = st.text_input("Senha", type='password')
        
        # Confirm password if required
        if confirmPass:
            confirm_password = st.text_input("Confirme a senha", type='password')
        
        # Extra input fields if any
        if extra_input_params:
            for input_param, type in st.session_state['extra_input_params'].items():
                input_field(input_param, type)
        
        # Validate all required fields before proceeding
        if st.session_state['email'] and st.session_state['password'] and \
            (not confirmPass or (confirmPass and st.session_state['password'] == confirm_password)):
            
            if extra_input_params and not all(st.session_state.get(param) for param in st.session_state['extra_input_params']):
                st.error("Por favor, preencha todos os campos obrigatórios")
            else:
                if st.button("Cadastrar-se", use_container_width=True):
                    st.session_state['verifying'] = True
                    send_new_user()
        else:
            if confirmPass and st.session_state['password'] != confirm_password:
                st.error("Senhas não coincidem")
            elif st.button("Cadastrar-se"):
                st.error("Por favor, preencha todos os campos obrigatórios")
