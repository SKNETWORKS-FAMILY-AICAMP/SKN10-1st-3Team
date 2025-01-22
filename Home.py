import streamlit as st

# Set up the page
st.set_page_config(page_title="Home", layout="wide")

title_alignment="""
<h1 style='text-align: center;'>
Mini Project
</h1>
"""

st.markdown(title_alignment, unsafe_allow_html=True)
st.markdown('---')

project_introduce="""
### 🚗 프로젝트 소개

>전국 자동차의 2015~2024년까지의 등록 현황을 **시각적으로 분석**하고, 대표적인 자동차 기업들의 **자주 묻는 질문(FAQ) 5가지를 제공**하는 시스템입니다.  
이 프로젝트를 통해 사용자들은 **자동차 등록 현황**을 쉽게 이해하고, **자동차 기업들의 주요 정보**를 신속하게 확인할 수 있습니다.
"""
st.markdown("")
st.markdown(project_introduce)

feature1="""
### 🧑‍💻기능

1. **자동차 등록 현황 시각화 📈**  
    - 2015년부터 2024년까지의 등록 데이터를 기반으로 한 그래프 제공
    - 연도별 지역별, 차종별 분석 기능   
"""
st.markdown(feature1)
st.markdown("")
feature2="""
2. **대표 자동차 기업 FAQ 제공 🔍**
    - 주요 자동차 기업의 대표적인 FAQ 조회
    - 각 기업별 자주 묻는 질문 및 답변 제공
"""

st.markdown(feature2)

skill_stack="""

"""

st.markdown(skill_stack)

# 팀 소개
st.subheader('👯‍♂️ 팀원')

team="""
|이종원|박현준|남궁승원|문승기|이태수|장윤홍|
|:---:|:----:|:-----:|:----:|:---:|:----:|
|img|img|img|img|img|img|
|ljw8373@gamil.com|@phjoon1012|dudalapfhd@gmail.com|moon010103@naver.com|beartaesu@naver.com|ccbb15379@naver.com|
"""

st.markdown(team)