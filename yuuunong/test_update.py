import streamlit as st
import pandas as pd
import plotly.graph_objects as go



# SQL 쿼리를 실행하여 결과를 캐싱하는 함수
@st.cache_data
def load_data(p_select: str):
    # MySQL 연결 설정
    conn = st.connection("mini_proj_mysql", type="sql", autocommit=True)
    
    # SQL 쿼리
    sql_total = """
        select
            substring(`월(Monthly)`,1,4) as `연도`,
            sum(`계_4`) as `계`
        from
            vehicle_registration_data vrd
        where 1=1
            and `시군구` = '계'
            and substring(`월(Monthly)`,6,2) = '12'
        group by
            `연도`
        ;
    """
    
    sql_seoul = '''
        select
            substring(`월(Monthly)`,1,4) as `연도`,
            `시도명`,
            `계_4` as `계`
        from
            vehicle_registration_data vrd
        where 1=1
            and `시도명` = '서울'
            and `시군구` = '계'
            and substring(`월(Monthly)`,6,2) = '12'
        ;
    '''

    sql_gu = '''
        select
            substring(`월(Monthly)`,1,4) as `연도`,
            `시도명`,
            `시군구`,
            `계_4` as `계`
        from
            vehicle_registration_data vrd
        where 1=1
            and `시도명` = '서울'
            and `시군구` != '계'
            and substring(`월(Monthly)`,6,2) = '12'
        ;
    '''

    # SQL 쿼리 실행 및 결과 반환
    if p_select == 'total':
        result = conn.query(sql=sql_total, ttl=3600)
        return pd.DataFrame(result)  # Pandas DataFrame으로 반환
    
    if p_select == 'seoul':
        result = conn.query(sql=sql_seoul, ttl=3600)
        return pd.DataFrame(result)  # Pandas DataFrame으로 반환
    
    if p_select == 'gu':
        result = conn.query(sql=sql_gu, ttl=3600)
        return pd.DataFrame(result)

# tab 생성
tab1, tab2, tab3 = st.tabs(['전국', '서울', '서울 구'])

# 데이터 로드
data_total = load_data('total')
data_seoul = load_data('seoul')
data_seoul_gu = load_data('gu')

# 데이터프레임 표시
tab1.header("전국 자동차 등록 현황 합계 데이터")
tab1.dataframe(data_total)

tab2.header("서울 자동차 등록 현황 합계 데이터")
tab2.dataframe(data_seoul)

tab3.header('서울 구별 자동차 등록 현황 합계 데이터')
tab3.dataframe(data_seoul_gu)


# 전국 그래프 생성
fig_total = go.Figure()

# 선 그래프 추가
fig_total.add_trace(go.Scatter(
    x=data_total['연도'], 
    y=data_total['계'], 
    mode='lines+markers+text',  # 선 + 점 + 텍스트
    text=data_total['계'],  # 텍스트에 데이터 값 추가
    textposition='bottom center',  # 텍스트 위치 설정
    marker=dict(size=8, color='#212121'),  # 점 스타일
    line=dict(width=3, color='#C890A7'),  # 선 스타일
    name="Total Registered Vehicles"
))

# 텍스트 위치를 수동으로 조정
fig_total.data[0].update(
    textposition="bottom center", 
    textfont=dict(size=16, color='black'),  # 텍스트 크기 조정
    texttemplate='%{text}<br>'  # 텍스트와 점 간격 증가
)

# 레이아웃 설정
fig_total.update_layout(
    title="전국 자동차 등록 현황 합계",
    xaxis_title="연도",
    yaxis_title="총 등록 차량 수",
    xaxis_autorange=True,
    yaxis_autorange=True,
    template="plotly_white",  # 그래프 테마
    width=1000,
    height=500
)

# 서울 그래프 생성
fig_seoul = go.Figure()

fig_seoul.add_trace(go.Scatter(
    x=data_seoul['연도'], 
    y=data_seoul['계'], 
    mode='lines+markers+text',  # 선 + 점 + 텍스트
    text=data_seoul['계'],  # 텍스트에 데이터 값 추가
    textposition='bottom center',  # 텍스트 위치 설정
    marker=dict(size=8, color='#212121'),  # 점 스타일
    line=dict(width=3, color='#C890A7'),  # 선 스타일
    name="Seoul Registered Vehicles"
))

fig_seoul.data[0].update(
    textposition="bottom center", 
    textfont=dict(size=16, color='black'),  # 텍스트 크기 조정
    texttemplate='%{text}<br>'  # 텍스트와 점 간격 증가
)

fig_seoul.update_layout(
    title="서울 자동차 등록 현황 합계",
    xaxis_title="연도",
    yaxis_title="총 서울 등록 차량 수",
    xaxis_autorange=True,
    yaxis_autorange=True,
    template="plotly_white",  # 그래프 테마
    width=1000,
    height=500
)


# 그래프 출력
tab1.plotly_chart(fig_total, use_container_width=True)
tab2.plotly_chart(fig_seoul, use_container_width=True)
tab3.bar_chart(data_seoul_gu, x="연도", y="계", color="시군구", stack=False, use_container_width = False)