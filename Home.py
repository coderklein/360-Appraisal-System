import streamlit as st
from PIL import Image
from pathlib import Path

from streamlit_login_auth_ui.widgets import __login__

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='360° Appraisal System', page_icon='⚖️⭐', layout="centered", initial_sidebar_state="collapsed")

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CSS.

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# LOGO.

logo = current_dir / "assets" / "logo.jpg"
logo = Image.open(logo)

st.title("360° Appraisal System.")
st.image(logo, use_column_width=True)

__login__obj = __login__(auth_token = "courier_auth_token",
                         company_name = "",
                         width = 200, height = 250,
                         logout_button_name = 'Logout', hide_menu_bool = False,
                         hide_footer_bool = False,
                         lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

is_logged_in = __login__obj.build_login_ui()

if is_logged_in:
    st.markown("The Application Begins here!")
