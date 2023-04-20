import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
from geopy import distance
import numpy as np
from data import place

center = (37.6001,127.0602)

def map():
    p = place.get_place(st.session_state.get('store',''))
    data = p.rename({
            "name": "식당명",
            "address": "도로명주소",
            "cat1": "대분류",
            "cat2": "소분류",
        }, axis=1).iloc[:,0:3]
    m = folium.Map(
        location=center,
        min_zoom=5,
        max_zoom=30,
        zoom_start=5,
        zoom_control=True,
    )
    add_center_marker(m)
    add_cluster_marker(m)
    st_folium(m, width=800, height=400)
    if 'location' in st.session_state:
        st.write(f"오늘은 **{st.session_state['store']}** 어떠세요?")
        st.button(
            "😉 메뉴 다시 추천 받기", on_click=get_recommend)
    else:
        st.button(
            "😉 메뉴 추천 받기",
            on_click=get_recommend)
    st.subheader("🍜 외대앞역의 맛집 List")

    ds = data.copy()
    ds.index = range(1, len(data) + 1)
    st.dataframe(
        ds, 
        height=300,
        use_container_width=True
    )

def add_center_marker(m):
    folium.Marker(
        center,
        icon=folium.Icon(
            icon='fire',
            color='red'
        ),
        popup=folium.Popup(
            html="외대/회기",
            max_width=200,
        ),
        tooltip="우하하. 재개발 다 되면 여기 내집 예정ㅋ"
    ).add_to(m)

def get_recommend():
    p = place.get_place()
    idx = np.random.randint(len(p))
    item = p.iloc[idx]
    st.session_state['store'] = item['name']
    st.session_state['location'] = (item.lat, item.long)

def add_cluster_marker(m):
    cluster = MarkerCluster().add_to(m)
    data = place.get_place()
    for i in range(len(data)):
        row = data.iloc[i]
        dist = round(distance.geodesic(center, (row.lat, row.long)).meters * 100) / 100
        html = f'''
                <p><b>주소</b> : {row.address}</p>
                <p><b>직경거리</b> : {dist}m</p>
                '''
        if not str(row.naver) == 'nan':
            nv = f"https://m.place.naver.com/restaurant/{str(int(row.naver))}"
            html += f"<p><b>네이버플레이스</b> : <a href={nv} target='blank'>🔗</a></p>"
        if not str(row.kakao) == 'nan':
            kk = f"https://place.map.kakao.com/{str(int(row.kakao))}"
            html += f"<p><b>카카오맵</b> : <a href={kk} target='blank'>🔗</a></p>"
        folium.Marker(
            (row.lat, row.long),
            popup=folium.Popup(
                html=html,
                max_width=200,
            ),
            icon=folium.Icon(
            icon='cutlery',
            color='orange'
            ),
            tooltip=row['name']
        ).add_to(cluster)