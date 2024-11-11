import streamlit as st
from achei_pet.utils.db_handler import get_pets_abandonados
import folium
from streamlit_folium import st_folium


def show_pet_abandonado():
    st.markdown("<h2 style='text-align: center;'>PETS em situação de abandono</h2>", unsafe_allow_html=True)
    pets = get_pets_abandonados()
    if pets:
        show_pet_feed(pets)

def show_pet_feed(pets_data):    
    for pet in pets_data:
        id, nome, cor, lat, lon, filename, _, telefone = pet  # Ignora o status
        # Exibir o nome e a cor
        st.markdown(f"### {nome}")
        st.markdown(f"**Cor**: {cor}")
        st.markdown(f"**Contato**: {telefone}")
        
        # Exibir imagem do pet
        st.image(f'images/{filename}',use_column_width =True)
        
        with st.popover("Visualizar local onde foi encontrado", use_container_width=True):
            # Mapa com o marcador do pet
            m = folium.Map(location=[lat, lon], zoom_start=15)
            folium.Marker([lat, lon], popup=id).add_to(m)
            st_folium(m, height=250, width=1720)
        
        # Separador entre os pets
        st.markdown("<hr>", unsafe_allow_html=True)
