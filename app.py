import streamlit as st

from widget import location

def app():
    st.set_page_config(
        page_title="독산 점메추",
        page_icon=":bento:",
    )
    st.title('🥘 독산 점심 메뉴 추천')
    location.map()

if __name__ == '__main__':
    app()