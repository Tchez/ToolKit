import streamlit as st
from components import remove_background, yt_downloader
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Useful Tools',
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
            'Download YouTube Videos',
            'Remove Background',
        ],
        icons=[
            'play-circle',
            'image',
        ],
        menu_icon='cast',
    )

match selected:
    case 'Download YouTube Videos':
        yt_downloader()
    case 'Remove Background':
        remove_background()
    case _:
        st.write('Please select an option from the sidebar')
