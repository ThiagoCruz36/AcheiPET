import streamlit as st
from achei_pet.utils.init_session import reset_session
import base64

def config_page():
    # Oculta o menu padrão do Streamlit
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-18e3th9 {padding-top: 0rem; padding-bottom: 0rem;}
        .block-container {
            padding: 0rem 1rem;
        }
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def render_header():
    with open("./data/header.png", "rb") as img_file:
        background_img = base64.b64encode(img_file.read()).decode('utf-8')
    header = f"""
        <style>
            div[class="st-emotion-cache-ocqkz7 e1f1d6gn5"] {{
                background-image: url("data:./data/header;base64,{background_img}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 260px; /* Defina a altura desejada para o cabeçalho */
                display: flex;
                align-items: center;
                justify-content: flex-end;
                padding-right: 20px;
                color: white;
            }}
            div [data-testid="stButton"] {{
                width: 80px;
                margin-top: 0px;
                padding-top: 0px;
                font-size: 12px;
            }}
        </style>
    """
    st.markdown(header, unsafe_allow_html=True)

    # Conteúdo do cabeçalho com imagem de fundo
    with st.container():
        st.markdown('<div class="header-container">', unsafe_allow_html=True)
        col1, col2 = st.columns([8, 1])  # col1 para espaço vazio e col2 para botões
        with col2:
            nav_buttons()
        st.markdown('</div>', unsafe_allow_html=True)

def nav_buttons():
    st.markdown("<div style='text-align: center; margin: 20px;'>", unsafe_allow_html=True)
    if st.session_state['guest_mode']:
        if st.button("Pets Perdidos", key='perdido_1', use_container_width=True):
            st.session_state['pagina_atual'] = "pets_perdidos"
        if st.button("Pets Abandonados", key='abandonado_1', use_container_width=True):
            st.session_state['pagina_atual'] = "pets_abandonados"
        if st.button("Login", use_container_width=True):
            reset_session()
            st.rerun()
    else:
        if st.button("Pets Perdidos", key='perdido_2', use_container_width=True):
            st.session_state['pagina_atual'] = "pets_perdidos"
        if st.button("Pets Abandonados", key='abandonado_2', use_container_width=True):
            st.session_state['pagina_atual'] = "pets_abandonados"
        if st.button("Cadastrar Pet", use_container_width=True):
            st.session_state['pagina_atual'] = "cadastrar_pet"
        if st.button("Logout", use_container_width=True):
            reset_session()
            st.rerun()
