import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import time
import json
import requests
from streamlit_lottie import st_lottie

def absolute_value(X):
    return (X**2) ** 0.5

with st.sidebar:
    selected_option = option_menu("Silahkan Pilih", option=["Beranda","Kenalan yuk", "Apa sih konfigurasi elektron itu?", "Konfigurasi elektron"])

if selected_option == 'Beranda':
    # Tulis konten halaman sambutan
    # Menampilkan teks dengan markdown yang telah diatur ukuran dan gayanya
    st.markdown("<h1 style='text-align: center; font-weight: bold;'> Welcome to our Application!</h1>", unsafe_allow_html=True)

    #Tambahkan animasi
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
        
    
    lottie_coding= load_lottiefile("c:\Users\salma\Downloads\atom-6387470-5275259.mp4")

    st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)
st_lottie(lottie_coding, key="hello")