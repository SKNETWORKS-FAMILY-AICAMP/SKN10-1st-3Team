
import streamlit as st

# Set up the page
st.set_page_config(page_title="Car Company FAQ", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Home")
st.sidebar.markdown("년도별 자동차 현황")
st.sidebar.markdown("기업 별 FAQ")

# Main content
st.title("기업 별 FAQ")

# Section 5: FAQ Section
st.header("기업 별 FAQ")

# Tabbed layout for car companies
companies = ["현대", "회사2", "회사3"]
selected_company = st.selectbox("Select a Company", companies)

# Placeholder FAQ content for each company
faq_data = {
    "현대": [
        {"question": "Q1. 신차 구매 시 타던 차량을 반납하면 신차 할인을 받을 수 있나요?", "answer": "현대 인증중고차의 내차팔기 서비스와 연계하여 신차 할인과 중고차 추가 보상 혜택을 받을 수 있습니다. 자세한 사항은 [이벤트> 진행중 이벤트]를 통해 확인해 주세요."},
        {"question": "Q2. 차량 구입시 신용카드는  복수의 카드로 결제가 가능한가요?", "answer": "예, 가능합니다. 신용카드 갯수에 제한없이 결제가 가능합니다."},
        {"question": "Q3. 할부금을 카드로 결제할 수 있나요?", "answer": "불가능합니다. 할부금은 금전채무로 분리되어 있으며, 여신전문금융업법상 금전채권은 카드로 결제할 수 없게 되어있습니다."},
        {"question": "Q4. 차량계약 후 해지 시 계약금은 환불 받을 수 있습니까?","answer": "차량 출고전 해지요청시에는 계약금 환불이 가능하며, 자세한 사항은 계약하신 지점(대리점)에 문의 바랍니다."},
        {"question": "Q5. 장애인 차량 구입조건에 대해 알고 싶습니다,","answer": "장애인 조건의 차량구입은 장애인 단독명의, 장애인과 주민등록표상 세대를 함께하는 배우자, 직계존비속,형제자매 또는 직계비속의 배우자 공동명의로 구입이 가능합니다. 단, 몇가지 조건이 붙는데 장애인 공동명의 조건으로 구입하신 차량은 차량출고후 5년간 동일조건(주민등록법상 동일세대)를 유지해야 하고 이 조건이 충족되지 않을때 면세받은 금액을 납부하셔야 합니다. 또한 재구입연한이 만 5년으로 되어있어 기간내에 동일차량을 계속 보유하셔야 되며, 이또한 조건 불충족시 면세받으신 세금을 납부하시게 됩니다."},
        ],
    "회사2": [
        {"question": "Q1. What are the service hours?", "answer": "Service is available from 8 AM to 6 PM, Monday through Friday."},
        {"question": "Q2. Are parts covered under warranty?", "answer": "Yes, parts are covered under the basic warranty."},
        {"question": "Q3. Can I schedule a test drive?", "answer": "Yes, you can schedule a test drive online or in person."},
    ],
    "회사3": [
        {"question": "Q1. What are the available car models?", "answer": "We offer SUVs, sedans, and electric vehicles."},
        {"question": "Q2. Are electric vehicle chargers available?", "answer": "Yes, charging stations are available at all locations."},
        {"question": "Q3. What is the process for leasing?", "answer": "Leasing requires an initial deposit and a signed agreement."},
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