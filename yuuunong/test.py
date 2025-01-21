import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# SQL 쿼리를 실행하여 결과를 캐싱하는 함수
@st.cache_data
def load_data(p_select: str):
    # MySQL 연결 설정
    conn = st.connection("mini_proj_mysql", type="sql", autocommit=True)
    
    # SQL 쿼리
    sql_total = """
        SELECT 
            YEAR(formatted_date) AS year, 
            SUM(total) AS total_registered_vehicles
        FROM 
            vehicle_registration_data
        WHERE 1=1
            and MONTH(formatted_date) = 12
        GROUP BY YEAR(formatted_date)
        ORDER BY YEAR(formatted_date)
        ;
    """
    
    sql_seoul = """
        SELECT 
            YEAR(formatted_date) AS year, 
            SUM(total) AS total_registered_vehicles
        FROM 
            vehicle_registration_data
        WHERE 1=1
            and city = '서울'
            and MONTH(formatted_date) = 12
        GROUP BY YEAR(formatted_date)
        ORDER BY YEAR(formatted_date)
        ;
    """

    # SQL 쿼리 실행 및 결과 반환
    if p_select == 'total':
        result = conn.query(sql=sql_total, ttl=3600)
        return pd.DataFrame(result)  # Pandas DataFrame으로 반환
    
    if p_select == 'seoul':
        result = conn.query(sql=sql_seoul, ttl=3600)
        return pd.DataFrame(result)  # Pandas DataFrame으로 반환

# tab 생성
tab1, tab2 = st.tabs(['전국', '서울'])

# 데이터 로드
data_total = load_data('total')
data_seoul = load_data('seoul')

# 연도 데이터를 정수형으로 변환
data_total['year'] = data_total['year'].astype(int)
data_seoul['year'] = data_seoul['year'].astype(int)

# 데이터프레임 표시
tab1.header("연도별 전국 자동차 등록 현황 합계 데이터")
tab1.dataframe(data_total)

tab2.header("연도별 서울 자동차 등록 현황 합계 데이터")
tab2.dataframe(data_seoul)


# 전국 그래프 생성
fig_total = go.Figure()

# 선 그래프 추가
fig_total.add_trace(go.Scatter(
    x=data_total['year'], 
    y=data_total['total_registered_vehicles'], 
    mode='lines+markers+text',  # 선 + 점 + 텍스트
    text=data_total['total_registered_vehicles'],  # 텍스트에 데이터 값 추가
    textposition='top center',  # 텍스트 위치 설정
    marker=dict(size=8, color='#212121'),  # 점 스타일
    line=dict(width=3, color='#C890A7'),  # 선 스타일
    name="Total Registered Vehicles"
))

# 텍스트 위치를 수동으로 조정
fig_total.data[0].update(
    textposition="top center", 
    textfont=dict(size=16, color='black'),  # 텍스트 크기 조정
    texttemplate='%{text}<br>'  # 텍스트와 점 간격 증가
)

# 레이아웃 설정
fig_total.update_layout(
    title="연도별 전국 자동차 등록 현황 합계",
    xaxis_title="연도",
    yaxis_title="총 등록 차량 수",
    xaxis=dict(type='category'),  # X축을 카테고리형으로 설정
    yaxis=dict(range=[45000000, 55000000]),  # Y축 범위 설정
    template="plotly_white",  # 그래프 테마
    width=1000,
    height=500
)


fig_seoul = go.Figure()

fig_seoul.add_trace(go.Scatter(
    x=data_seoul['year'], 
    y=data_seoul['total_registered_vehicles'], 
    mode='lines+markers+text',  # 선 + 점 + 텍스트
    text=data_seoul['total_registered_vehicles'],  # 텍스트에 데이터 값 추가
    textposition='top center',  # 텍스트 위치 설정
    marker=dict(size=8, color='#212121'),  # 점 스타일
    line=dict(width=3, color='#C890A7'),  # 선 스타일
    name="Seoul Registered Vehicles"
))

fig_seoul.data[0].update(
    textposition="top center", 
    textfont=dict(size=16, color='black'),  # 텍스트 크기 조정
    texttemplate='%{text}<br>'  # 텍스트와 점 간격 증가
)

fig_seoul.update_layout(
    title="연도별 서울 자동차 등록 현황 합계",
    xaxis_title="연도",
    yaxis_title="총 등록 차량 수",
    xaxis=dict(type='category'),  # X축을 카테고리형으로 설정
    yaxis=dict(range=[6300000, 6400000]),  # Y축 범위 설정
    template="plotly_white",  # 그래프 테마
    width=1000,
    height=500
)

# X축을 카테고리형으로 설정하여 소수점 제거
fig_total.update_xaxes(type='category')
fig_seoul.update_xaxes(type='category')

# Y축을 정수로 설정
fig_total.update_yaxes(tickformat="~s")
fig_seoul.update_yaxes(tickformat='~s')

# 그래프 출력
tab1.plotly_chart(fig_total, use_container_width=True)
tab2.plotly_chart(fig_seoul, use_container_width=True)