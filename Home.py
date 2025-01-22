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

st.image("https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/7ea63fc3-95f0-44d5-a0f0-cf431cae34f1")

# 프로젝트 소개
project_introduce="""
### 💡 프로젝트 소개

>전국 자동차의 2015~2024년까지의 등록 현황을 **시각적으로 분석**하고, 대표적인 자동차 기업들의 **자주 묻는 질문(FAQ) 5가지를 제공**하는 시스템입니다.  
이 프로젝트를 통해 사용자들은 **자동차 등록 현황**을 쉽게 이해하고, **자동차 기업들의 주요 정보**를 신속하게 확인할 수 있습니다.
"""
st.markdown("")
st.markdown(project_introduce)

# 기능
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

# 기술 스택
skill_stack="./images/skill_stack.png"
st.subheader("🔧 기술 스택")
st.image(skill_stack)

# 데이터 정재 및 가져오기
st.subheader("데이터 정재 및 가져오기")
data_image = "./images/DBeaver.png"
st.image(data_image)
data_reconstruction = """
[database.sql](./files/sql.sql) 파일을 실행하여 데이터베이스 파일인 [vehicle_registration_data2.csv](./files/vehicle_registration_data2.csv)를 생성
"""
st.markdown(data_reconstruction)

# 설치 및 실행 방법
st.subheader("설치 및 실행 방법")
install_start = """
1. 저장소 클론

```bash
git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN10-1st-3Team.git
cd SKN10-1st-3Team
```

2. 프론트엔드 서버 실행

```bash
streamlit run Home.py
```
"""
st.markdown(install_start)

# 데이터 출처
st.subheader("데이터 출처")
data_source = """
- 자동차 등록 데이터: 국토교통부 통계누리
"""
st.markdown(data_source)
st.image("./images/data_1.png")
FAQ_source = """
- 자동차 기업 FAQ: 해당 기업의 공식 웹사이트   
[Hyundai FAQ]: https://www.hyundai.com/kr/ko/e/customer/center/faq   
[Kia FAQ]: https://www.kia.com/kr/customer-service/center/faq   
[Genesis]: https://www.genesis.com/kr/ko/support/faq.html   
[Porsche]: https://www.porsche.com/korea/ko/aboutporsche/e-performance/faq/
"""
st.markdown(FAQ_source)

# 화면 설계도
st.subheader("화면 설계도")
st.image("./images/screen.png")

# 팀 소개
st.subheader('👯‍♂️ 팀원')

team="""
|이종원|박현준|남궁승원|문승기|이태수|장윤홍|
|:---:|:----:|:-----:|:----:|:---:|:----:|
|img|img|img|img|img|img|
|ljw8373@gamil.com|@phjoon1012|dudalapfhd@gmail.com|moon010103@naver.com|beartaesu@naver.com|ccbb15379@naver.com|
"""

st.markdown(team)