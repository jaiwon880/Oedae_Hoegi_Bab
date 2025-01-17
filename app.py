import streamlit as st
from streamlit_option_menu import option_menu
from widget import location

# 후기 페이지에 넣을 거
# from streamlit_disqus import st_disqus
# st_disqus("streamlit-disqus-demo")


def side_bar():
    with st.sidebar:
        choice = option_menu("Menu", ["홈", "검색", "후기"],
                            icons=['house', 'search', 'pencil-square'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
        "container": {"padding": "4!important", "background-color": "#FAFAFA"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#FAFAFA"},
        "nav-link-selected": {"background-color": "#08C7B4"},
})

def app():
    st.set_page_config(
        page_title="맛집 웹이얌",
        page_icon=":bento:",
    )
    
    st.write('''
    ## 외대/회기 지박령 맛집 레쭈고 😋🍳 
    #### (회기 맛집리스트는 넘 많아서 추가중이애오)
    ---
    ''')
    location.map()


if __name__ == '__main__':
    app()
    side_bar()