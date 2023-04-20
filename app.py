import streamlit as st

from widget import location

def app():
    st.set_page_config(
        page_title="맛집 웹이얌",
        page_icon=":bento:",
    )
    
    st.write('''
    외대/회기 지박령 맛집 레쭈고 😋🍳
    ---
    ''')
    location.map()

if __name__ == '__main__':
    app()