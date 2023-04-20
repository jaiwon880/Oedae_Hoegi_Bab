import streamlit as st

from widget import location

def app():
    st.set_page_config(
        page_title="헉",
        page_icon=":bento:",
    )
    st.title('🍜🍗 외대/회기 지박령 맛집 레쭈고 😋🍳')
    location.map()

if __name__ == '__main__':
    app()