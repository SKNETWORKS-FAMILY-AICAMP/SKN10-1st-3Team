import streamlit as st

# Set up the page
st.set_page_config(page_title="Car Company FAQ", layout="wide")

# Section 5: FAQ Section
st.header("기업 별 FAQ")

# Tabbed layout for car companies
companies = ["회사1", "회사2", "포르쉐"]
selected_company = st.selectbox("Select a Company", companies)

# Placeholder FAQ content for each company
faq_data = {
    "회사1": [
        {"question": "Q1. What is the warranty policy?", "answer": "The warranty covers 3 years or 36,000 miles."},
        {"question": "Q2. What is the return policy?", "answer": "Returns are accepted within 7 days of purchase."},
        {"question": "Q3. Are there any financing options available?", "answer": "Yes, we provide several financing options."},
    ],
    "회사2": [
        {"question": "Q1. What are the service hours?", "answer": "Service is available from 8 AM to 6 PM, Monday through Friday."},
        {"question": "Q2. Are parts covered under warranty?", "answer": "Yes, parts are covered under the basic warranty."},
        {"question": "Q3. Can I schedule a test drive?", "answer": "Yes, you can schedule a test drive online or in person."},
    ],
    "포르쉐": [
        {"question": "Q1. 포르쉐를 어디에서 충전할 수 있나요?", "answer": """
        포르쉐는 집, 도로, 목적지 등 다양한 일상 상황에서 쉽게 충전할 수 있습니다.\n
        다양한 포르쉐 충전 장비를 집에서 충전하는데 사용할 수 있습니다. 
        자신의 필요에 맞는 충전 방법은 포르쉐 충전 사전 체크(https://www.porsche.com/countries/charging-check)를 통해 확인할 수 있습니다. 
        자세한 정보는 포르쉐  공식 서비스 센터에 문의하시기 바랍니다.\n
        """},
        {"question": "Q2. 포르쉐의 주행 거리에 영향을 미치는 요인은 어떤 것이 있나요?", "answer": """
        주행 거리는 주행 스타일, 편의 기능 사용 여부, 공기 역학 및 도로 여건 등의 여러 요인의 영향을 받습니다.\n
        가장 중요한 요인은 운전자의 주행 스타일입니다. 
        주변 환경을 파악하고 예측 운전을 하면 제동 에너지 회생이 향상되어 차량의 주행 가능 거리가 증가합니다.\n
        뿐만 아니라, 에어컨, 히터 등의 편의 기능의 강도를 줄이거나 루프 박스와 같이 공기 역학에 영향을 주는 액세서리를 필요한 경우에만 장착하는 것도 도움을 줄 수 있습니다.
        """},
        {"question": "Q3. 집에서 차량을 충전하려면 어떤 충전 장비를 어디서 구입해야 하나요?", "answer": """
        포르쉐는 포르쉐 모바일 충전기, 포르쉐 모바일 충전기 커넥트 등의 다양한 충전 장비를 선택 사양으로 제공하고 있습니다. 뿐만 아니라, 포르쉐 충전 독 및 포르쉐 컴팩트 충전 스탠드 등의 다양한 장착 옵션도 제공합니다. 이러한 충전 장비는 포르쉐 공식 서비스 센터를 통해 구입할 수 있습니다.
        """},
        {"question": "Q4. 추운 날씨에는 무엇에 유의해야 하나요?", "answer": """
        날씨가 추울 때 사용하는 편의 기능(예: 난방)으로 인해 차량의 주행 가능 거리가 줄어들 수 있습니다. 충전 중에 편리한 사전 온도 설정 기능을 사용하면 난방에 필요한 전력을 파워 그리드에서 공급하기 때문에 이러한 주행 거리 감소 현상을 줄일 수 있습니다. \n 저온에서는 고전압 배터리의 충전 성능도 제한될 수 있습니다. 포르쉐 충전 플래너(판매 국가에 따라 제공 여부 다름)와 배터리 사전 온도 설정 기능을 이용하여 충전 전에 배터리를 예열하여 최적의 충전 상태로 만들어줍니다.
        """},
        {"question": "Q5. 도움이 필요한 경우 어디에 연락해야 하나요?", "answer": """
        포르쉐 충전 하드웨어 제품 및 설치 방법 또는 발생하는 문제에 대해 궁금하신 점이 있으시면 포르쉐 공식 서비스 센터로 문의하시기 바랍니다.\n
        포르쉐 충전 서비스(판매 국가에 따라 제공 여부 다름)에서의 공용 충전에 대한 문의는 언제나 포르쉐 커넥트 지원 서비스를 통해 도움을 받을 수 있습니다. 
        뿐만 아니라 차량에 문제가 생길 경우 포르쉐 어시스턴스 콜 센터를 통해 접수할 수 있습니다.
        """},
    ],
}

# Display FAQ for the selected company
st.subheader(f"FAQ for {selected_company}")

for faq in faq_data[selected_company]:
    with st.expander(faq["question"]):
        st.write(faq["answer"])

# Footer (Optional Section 6)
st.markdown("---")
st.markdown("Section 6")
st.markdown("Additional information can go here, such as disclaimers or links.")