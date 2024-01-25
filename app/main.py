import streamlit as st
from components import remove_background, yt_downloader
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Useful Things',
    page_icon='⚙️',
    menu_items={
        'Get Help': 'https://github.com/Tchez/utils/issues',
        'Report a bug': 'https://github.com/Tchez/utils/issues',
        'About': 'https://github.com/Tchez/utils/blob/main/README.md',
    },
)

with st.sidebar:
    selected = option_menu(
        'Select an option',
        [
            'Download Youtube Videos',
            'Remove Background',
        ],
        icons=[
            'play-circle',
            'image',
        ],
        menu_icon='cast',
    )

match selected:
    case 'Download Youtube Videos':
        yt_downloader()
    case 'Remove Background':
        remove_background()
    case _:
        st.write('Selecione uma opção no menu lateral')
