import streamlit as st
import pandas as pd
import plotly.express as px

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

# 그래프 생성 (X축: 연도, Y축: 총 등록 차량 수)
fig_total = px.line(
    data_total,
    x="year",  # X축에 연도
    y="total_registered_vehicles",  # Y축에 총 등록 차량 수
    title="연도별 전국 자동차 등록 현황 합계",
    labels={
        "year": "Year",  # X축 레이블
        "total_registered_vehicles": "Total Registered Vehicles"  # Y축 레이블
    },
)

fig_seoul = px.line(
    data_seoul,
    x="year",  # X축에 연도
    y="total_registered_vehicles",  # Y축에 총 등록 차량 수
    title="연도별 서울 자동차 등록 현황 합계",
    labels={
        "year": "Year",  # X축 레이블
        "total_registered_vehicles": "Total Registered Vehicles"  # Y축 레이블
    },
    
)

# X축을 카테고리형으로 설정하여 소수점 제거
fig_total.update_xaxes(type='category')
fig_seoul.update_xaxes(type='category')

# Y축을 정수로 설정
fig_total.update_yaxes(tickformat="d")
fig_seoul.update_yaxes(tickformat='d')

# 그래프 출력
tab1.plotly_chart(fig_total, use_container_width=True)
tab2.plotly_chart(fig_seoul, use_container_width=True)