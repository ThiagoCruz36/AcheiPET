import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MousePosition
import uuid
import os
import time
from PIL import Image
from achei_pet.utils.db_handler import save_pet
from achei_pet.page.pets_abandonados import show_pet_abandonado
from achei_pet.page.pets_perdidos import show_pet_perdido


def show_add_pet():
    st.markdown("<h2 style='text-align: center;'>Cadastro de Pets</h2>", unsafe_allow_html=True)
    name = st.text_input("Nome")
    filename = None
    color = st.text_input("Cor")
    status = st.selectbox(
        "O Pet encontra-se perdido ou abandonado?",
        ("Abandonado", "Perdido"))
    telefone = st.text_input("Telefone para contato (Com DDD)")
    uploaded_image = st.file_uploader(
        "Selecione a imagem do PET",
        accept_multiple_files=False,
        type=["png", "jpg", "jpeg"])

    orchestrate_map()

    if st.button("Salvar", use_container_width=True):
        if name is None or color is None or telefone is None:
            st.error("Por favor, preencha todos os campos")
        else:
            latitude = st.session_state['last_clicked']['lat']
            longitude = st.session_state['last_clicked']['lng']

            save_dir = os.path.join(os.getcwd(), "images")
            os.makedirs(save_dir, exist_ok=True)

            if uploaded_image:
                img_pil = Image.open(uploaded_image)
                file_extension = img_pil.format.lower()
                filename = str(uuid.uuid4()) + '.' + file_extension
                file_path = os.path.join(save_dir, filename)
                img_pil.save(file_path)

                save_pet(name, color, status, latitude, longitude, filename, telefone)
                st.success("Operação realizada com sucesso!")
                time.sleep(2)
                st.session_state['pagina_atual'] = 'pets_abandonados' if status == 'Abandonado' else 'pets_perdidos'
                st.rerun()
                    
            else:
                st.error("Por favor, forneça uma imagem do Pet")

def orchestrate_map():
    st.markdown("<h4 style='text-align: center;'>Adicione a última localização conhecida do PET:</h4>", unsafe_allow_html=True)
    st.text('')

    # Inicializa o mapa com uma localização padrão ou última clicada
    if 'last_clicked' not in st.session_state:
        st.session_state['last_clicked'] = {'lat': -21.58753132818611, 'lng': -48.074197769165046}

    # Pega a última localização clicada e centraliza o mapa ali
    last_location = st.session_state['last_clicked']
    m = folium.Map(location=[last_location['lat'], last_location['lng']], zoom_start=15)

    # Adiciona um plugin para capturar a posição do mouse
    mouse_position = MousePosition()
    m.add_child(mouse_position)

    # Adiciona o marcador, se existir
    if st.session_state['last_clicked']:
        folium.Marker(
            [last_location['lat'], last_location['lng']],
            popup=f"Coordenadas: {last_location['lat']}, {last_location['lng']}"
        ).add_to(m)

    # Usa o st_folium para renderizar o mapa no Streamlit
    output = st_folium(m, height=350, width=1720)

    # Se o usuário clicou em um novo ponto, atualiza as coordenadas e coloca o marcador
    if output['last_clicked'] is not None:
        lat = output['last_clicked']['lat']
        lon = output['last_clicked']['lng']

        # Atualiza o estado com as novas coordenadas
        st.session_state['last_clicked'] = {'lat': lat, 'lng': lon}

        # Cria um novo mapa com o novo marcador
        m = folium.Map(location=[lat, lon], zoom_start=15)
        folium.Marker([lat, lon], popup=f"Coordenadas: {lat}, {lon}").add_to(m)

        # Exibe o mapa atualizado
        st_folium(m, height=350, width=1720)