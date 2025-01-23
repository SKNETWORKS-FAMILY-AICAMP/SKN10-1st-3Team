import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# 페이지 기본 설정
st.set_page_config(layout="wide")

# CSS 스타일 적용
st.markdown("""
<style>
    /* 탭 스타일링 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        padding: 0 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        border-radius: 20px;
        padding: 0 20px;
        font-size: 16px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #C890A7;
        color: white;
    }
    
    /* 탭 hover 효과 */
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e0e2e6;
        color: black;
    }
    
    /* 선택된 탭 hover */
    .stTabs [aria-selected="true"]:hover {
        background-color: #C890A7;
        color: white;
            
}
    }
</style>
""", unsafe_allow_html=True)

# 사이드바 메뉴 구현
with st.sidebar:
    st.title("연도별 자동차 현황")
    menu = ["HOME", "연도별 자동차 현황", "FAQ"]
    choice = st.radio("메뉴", menu)

    # 메인 페이지
st.title("연도별 자동차 현황")

# SQL 쿼리를 실행하여 결과를 캐싱하는 함수
@st.cache_data
def load_data(p_select: str):
    # MySQL 연결 설정
    conn = st.connection("1st_mysql", type="sql", autocommit=True)
    
    # SQL 쿼리
    sql_total = """
        select
            year as `연도`,
            sum(total) as `계`
        from
            vehicle_registration_data2
        where 1=1
            and district = '계'
            and month(formatted_date) = 12
        group by
            year
        ;
    """
    
    sql_seoul = '''
        select
            year as `연도`,
            total as `계`
        from
            vehicle_registration_data2
        where 1=1
            and city = '서울'
            and district = '계'
            and month(formatted_date) = 12
        ;
    '''

    sql_gu = '''
        select
            year as `연도`,
            city as `시도명`,
            district as `시군구`,
            total as `계`
        from
            vehicle_registration_data2
        where 1=1
            and city = '서울'
            and district != '계'
            and month(formatted_date) = 12
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

# 천단위 구분기호 넣기
def format_with_commas(value):
    if isinstance(value, (int, float)):
        return f"{value:,}"
    return value

## # 데이터 로드
data_total = load_data('total')
data_seoul = load_data('seoul')
data_seoul_gu = load_data('gu')

# tab 생성
tab1, tab2, tab3 = st.tabs(['전국', '서울', '서울 구'])

# 데이터 로드
## data_total = load_data('total')
# data_total 전치
data_total_transposed = data_total.set_index('연도').transpose()
data_total_transposed.columns = data_total_transposed.columns.astype(str)
## data_seoul = load_data('seoul')
data_seoul_transposed = data_seoul.set_index('연도').transpose()
data_seoul_transposed = data_seoul_transposed.map(format_with_commas)

## data_seoul = load_data('seoul_gu')
data_seoul_gu = load_data('gu')
data_seoul_gu_transposed = data_seoul_gu.pivot_table(values='계', index=['시도명', '시군구'], columns='연도').reset_index()
data_seoul_gu_transposed.columns = data_seoul_gu_transposed.columns.astype(str)

# 데이터프레임 표시
## tab1.header("전국 자동차 등록 현황 합계 데이터")
## tab1.dataframe(data_total)
tab1.header("전국 자동차 등록 현황 합계 데이터")
tab1.dataframe(data_total_transposed, use_container_width=True)

## tab2.header("서울 자동차 등록 현황 합계 데이터")
## tab2.dataframe(data_seoul)
tab2.header("서울 자동차 등록 현황 합계 데이터 ")
tab2.dataframe(data_seoul_transposed, use_container_width=True)

## tab3.header('서울 구별 자동차 등록 현황 합계 데이터')
## tab3.dataframe(data_seoul_gu)
tab3.header('서울 구별 자동차 등록 현황 합계 데이터 ')
tab3.dataframe(data_seoul_gu_transposed, use_container_width=True)


# 전국 그래프 생성
fig_total = go.Figure()

# 선 그래프 추가
fig_total.add_trace(go.Scatter(
    x=data_total['연도'], 
    y=data_total['계'], 
    mode='lines+markers+text',  # 선 + 점 + 텍스트
    text=data_total['계'],  # 텍스트에 데이터 값 추가
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
    title="전국 자동차 등록 현황 합계",
    xaxis_title="연도",
    yaxis_title="총 등록 차량 수",
    xaxis_autorange=True,
    yaxis_autorange=False,
    width=1400,
    height=600,    
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        showline=True,
        linewidth=4,
        linecolor='black',
        mirror='all',
        ticks='outside',
    ),
    yaxis=dict(
        showline=True,
        linewidth=4,
        linecolor='black',
        mirror='all',
        ticks='outside',
        range=[20000000, 27000000]
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    
)
fig_total.update_traces(
    texttemplate='%{text:,.0f}<br>',
    textfont=dict(size=16, color='black')
)

# 서울 그래프 생성
fig_seoul = go.Figure()


fig_seoul.add_trace(go.Scatter(
    x=data_seoul['연도'], 
    y=data_seoul['계'], 
    mode='lines+markers+text',  # 선 + 점 + 텍스트
    text=data_seoul['계'],  # 텍스트에 데이터 값 추가
    textposition='top center',  # 텍스트 위치 설정
    marker=dict(size=8, color='#212121'),  # 점 스타일
    line=dict(width=3, color='#C890A7'),
    texttemplate='%{text:,.0f}<br>',
    textfont=dict(size=16, color='black'),  # 선 스타일
    name="Seoul Registered Vehicles"
))


fig_seoul.data[0].update(
    textposition="top center", 
    textfont=dict(size=16, color='black'),  # 텍스트 크기 조정
    texttemplate='%{text}<br>'  # 텍스트와 점 간격 증가
)

fig_seoul.update_layout(
    title="서울 자동차 등록 현황 합계",
    xaxis_title="연도",
    yaxis_title="총 서울 등록 차량 수",
    xaxis_autorange=True,
    yaxis_autorange=False,
    
    template="plotly_white",
    width=1000,
    height=600,
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        showline=True,
        linewidth=4,
        linecolor='black',
        mirror='all',
        ticks='outside'
    ),
    yaxis=dict(
        showline=True,
        linewidth=4,
        linecolor='black',
        mirror='all',
        ticks='outside',
        range=[3000000, 3230000]

    ),
    plot_bgcolor='white',
    paper_bgcolor='white'
)
fig_seoul.update_traces(
    texttemplate='%{text:,.0f}<br>',
    textfont=dict(size=16, color='black')
)

# 서울 세부 지역별 그래프 생성
# 연도 선택 위젯 추가
years = data_seoul_gu['연도'].unique()
selected_year = tab3.selectbox("연도를 선택하세요:", options=sorted(years))

# 선택한 연도의 데이터 필터링
filtered_data = data_seoul_gu[data_seoul_gu['연도'] == selected_year]

# 그래프 생성
fig_gu = go.Figure()


# 막대 그래프 추가
fig_gu.add_trace(go.Bar(
    x=filtered_data['시군구'],
    y=filtered_data['계'],
    text=filtered_data['계'],
    textposition='outside',
    marker=dict(color='#81d2f2'),
    name=f"{selected_year} 등록 현황"
))

# 레이아웃 설정
fig_gu.update_layout(
    title=f"{selected_year}년 서울 구별 자동차 등록 현황",
    xaxis_title="구",
    yaxis_title="등록 차량 수",
    xaxis=dict(
        tickmode='linear',
        dtick=1,
        showline=True,
        linewidth=4,
        linecolor='black',
        mirror='all',
        ticks='outside',
    ),
    yaxis=dict(
        showline=True,
        linewidth=4,
        linecolor='black',
        mirror='all',
        ticks='outside',
    ),
    template="plotly_white",
    width=1000,
    height=500,
    plot_bgcolor='white',
    paper_bgcolor='white'
)
fig_gu.update_traces(
    texttemplate='%{text:,.0f}<br>',
    textfont=dict(size=16, color='black')
)

# 그래프 출력
tab1.plotly_chart(fig_total, use_container_width=True)
tab2.plotly_chart(fig_seoul, use_container_width=True)
tab3.plotly_chart(fig_gu, use_container_width=True)