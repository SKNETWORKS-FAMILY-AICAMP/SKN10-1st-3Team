import streamlit as st

# Set up the page
st.set_page_config(page_title="Car Company FAQ", layout="wide")

# Section 5: FAQ Section
st.header("기업 별 FAQ")

# Tabbed layout for car companies
companies = ["기아", "현대", "제네시스", "포르쉐"]
selected_company = st.selectbox("회사를 선택해주세요", companies)

faq_data = {
    "기아": [
        {"question": "직영 서비스센터 운영 시간은 어떻게 됩니까?", "answer": "직영 서비스센터의 업무시간은 평일 08:30 - 17:30까지 이며, 중식시간은 12:30~13:30 입니다. \n 직영서비스센터는 예약제로 운영되므로 방문 전 사전 예약 바랍니다. 토탈 예약 센터 안내 (1899-0200) 전화 한통으로 고객님과 가장 가까운 서비스 네트워크에서 정비서비스를 받을 수 있도록 사전 예약을 접수하고 있습니다."},
        {"question": "일반 리모컨 또는 스마트 키 차량의 핸들 락(잠김) 해제 방법을 알려주세요", "answer": "일반 리모컨 적용 차량 또는 이모빌라이져 적용 차량의 핸들락(잠김) 해제방법 ① 왼손으로 핸들을 잡고 오른손으로 키셋트에 키를 꽂는다 ② 핸들을 좌우로 힘껏 움직이면서 동시에 ACC 방향으로 키를 돌린다. 스마트키 차량의 경우 시동과 동시에 핸들락(잠김)이 해제됩니다."},
        {"question": "전자식 파킹 브레이크(EPB) 기능이 무엇인가요?", "answer": "전자 파킹 브레이크(EPB : Electronic Parking Brake)는 페달 또는 레버로 케이블을 당겨 파킹 브레이크를 작동시키는 대신 스위치 조작으로 모터 구동을 통해 파킹 브레이크를 작동함으로써 운전자 편의성 향상을 도모하는 시스템입니다. "},
        {"question": "스마트 키 배터리 교환방법에 대해 알려주세요", "answer": "스마트 키의 사용횟수와 기간에 따라 배터리 성능이 저하되었을 경우 배터리 교환이 필요합니다. 배터리 교환 시 차종별 스마트 키 배터리 용량을 확인 후 배터리를 구입하여 교환하시면 됩니다. "},
        {"question": "내비게이션 업데이트는 어디서, 어떻게 하나요?", "answer": "내비게이션 업데이트는 기아멤버스 홈페이지에 접속하시어 이용하실 수 있습니다. "},
    ],
    "현대": [
        {"question": "Q1. 신차 구매 시 타던 차량을 반납하면 신차 할인을 받을 수 있나요?", "answer": "현대 인증중고차의 내차팔기 서비스와 연계하여 신차 할인과 중고차 추가 보상 혜택을 받을 수 있습니다. 자세한 사항은 [이벤트> 진행중 이벤트]를 통해 확인해 주세요."},
        {"question": "Q2. 차량 구입시 신용카드는  복수의 카드로 결제가 가능한가요?", "answer": "예, 가능합니다. 신용카드 갯수에 제한없이 결제가 가능합니다."},
        {"question": "Q3. 할부금을 카드로 결제할 수 있나요?", "answer": "불가능합니다. 할부금은 금전채무로 분리되어 있으며, 여신전문금융업법상 금전채권은 카드로 결제할 수 없게 되어있습니다."},
        {"question": "Q4. 차량계약 후 해지 시 계약금은 환불 받을 수 있습니까?","answer": "차량 출고전 해지요청시에는 계약금 환불이 가능하며, 자세한 사항은 계약하신 지점(대리점)에 문의 바랍니다."},
        {"question": "Q5. 장애인 차량 구입조건에 대해 알고 싶습니다,","answer": """장애인 조건의 차량구입은 장애인 단독명의, 장애인과 주민등록표상 세대를 함께하는 배우자, 직계존비속,형제자매 또는 직계비속의 배우자 공동명의로 구입이 가능합니다.   
        단, 몇가지 조건이 붙는데 장애인 공동명의 조건으로 구입하신 차량은 차량출고후 5년간 동일조건(주민등록법상 동일세대)를 유지해야 하고 이 조건이 충족되지 않을때 면세받은 금액을 납부하셔야 합니다. 또한 재구입연한이 만 5년으로 되어있어 기간내에 동일차량을 계속 보유하셔야 되며, 이또한 조건 불충족시 면세받으신 세금을 납부하시게 됩니다."""},
        ],
    "제네시스": [
        {"question": "[차량 구매] 제네시스 구입 후 세금계산서 발급받으려고 하는데 어떻게 해야 하나요?", "answer": "[개인사업자 및 법인사업자 구입고객] 2010년 7월 1일부터 세금계산서가 서면이 아닌 전자 세금계산서로 발행이 됩니다. 사이트( http://e-vat.hyundai.com ) 에서 발급받으시면 됩니다."},
        {"question": "[차량 구매/일반]제네시스 차량을 구입하려면 어떻게 해야하나요?", "answer": "제네시스에서는 전국 정식 지점/대리점을 통해서만 차량을 판매하고 있습니다. 자세한 지점/대리점 위치는 홈페이지 전시장 / 센터 찾기에서 확인하실 수 있습니다. 그 이외의 유통경로(인터넷 등)로는 차량 공급이 되지 않사오니 차량 구입시 주의해주시기 바라며 전국 어느 곳에서나 같은 제품,같은 가격으로 바른거래를 실천하고 있습니다. 참고로, 제네시스 홈페이지 구매상담 신청을 이용시 고객님께서 원하시는 지점, 대리점을 선택하여 상담신청을 하시면 전문영업사원이 신속하고 친절하게 차량구매에 관한 모든 궁금증을 해결해 드리겠습니다.​"},
        {"question": "[차량 구매/일반]차량구입에 관련된 금액은 어떠한 결제방식이 있나요?", "answer": "차량구입에 관련된 금액의 결제는 현금, 신용카드 및 할부이용 등의 방법이 있습니다. 그 이외 현재 보유차량 매각대금 대체 및 직불카드 등의 이용은 불가합니다."},
        {"question": "[차량 구매/일반]제네시스에서 중고차를 구입할 수 있나요?", "answer": "현재 저희 현대자동차는 현대·제네시스 인증 중고차(Hyundai Certified·GENESIS CERTIFIED) 매입 및 판매를 시행하고 있습니다. ※ 고객분들의 편리하고 안전한 중고차 거래를 위해 제네시스 인증 중고차 사이트(https://certified.hyundai.com)를 운영 중이니 참고하시기 바랍니다."},
        {"question": "[차량 구매/카드 결제]제네시스 구입 시 차량대금을 신용카드로 결제할 경우 소득공제가 가능한가요?", "answer": "불가능합니다. 조세특례제한법 제126조 3항 3호에 의거하여 신규로 출고되는 자동차 구입시 사용한 신용카드 금액은 소득공제 대상에서 제외됩니다.(2002년 12월1일 승인분부터 적용)​"},
    ],
    "포르쉐": [
        {"question": "Q1. 포르쉐를 어디에서 충전할 수 있나요?", "answer": "포르쉐는 집, 도로, 목적지 등 다양한 일상 상황에서 쉽게 충전할 수 있습니다. \n 다양한 포르쉐 충전 장비를 집에서 충전하는데 사용할 수 있습니다. 자신의 필요에 맞는 충전 방법은 포르쉐 충전 사전 체크(https://www.porsche.com/countries/charging-check)를 통해 확인할 수 있습니다. 자세한 정보는 포르쉐  공식 서비스 센터에 문의하시기 바랍니다.\n"},
        {"question": "Q2. 포르쉐의 주행 거리에 영향을 미치는 요인은 어떤 것이 있나요?", "answer": "주행 거리는 주행 스타일, 편의 기능 사용 여부, 공기 역학 및 도로 여건 등의 여러 요인의 영향을 받습니다. \n 가장 중요한 요인은 운전자의 주행 스타일입니다. 주변 환경을 파악하고 예측 운전을 하면 제동 에너지 회생이 향상되어 차량의 주행 가능 거리가 증가합니다. \n 뿐만 아니라, 에어컨, 히터 등의 편의 기능의 강도를 줄이거나 루프 박스와 같이 공기 역학에 영향을 주는 액세서리를 필요한 경우에만 장착하는 것도 도움을 줄 수 있습니다."},
        {"question": "Q3. 집에서 차량을 충전하려면 어떤 충전 장비를 어디서 구입해야 하나요?", "answer": "포르쉐는 포르쉐 모바일 충전기, 포르쉐 모바일 충전기 커넥트 등의 다양한 충전 장비를 선택 사양으로 제공하고 있습니다. 뿐만 아니라, 포르쉐 충전 독 및 포르쉐 컴팩트 충전 스탠드 등의 다양한 장착 옵션도 제공합니다. 이러한 충전 장비는 포르쉐 공식 서비스 센터를 통해 구입할 수 있습니다."},
        {"question": "Q4. 추운 날씨에는 무엇에 유의해야 하나요?", "answer": "날씨가 추울 때 사용하는 편의 기능(예: 난방)으로 인해 차량의 주행 가능 거리가 줄어들 수 있습니다. 충전 중에 편리한 사전 온도 설정 기능을 사용하면 난방에 필요한 전력을 파워 그리드에서 공급하기 때문에 이러한 주행 거리 감소 현상을 줄일 수 있습니다. \n 저온에서는 고전압 배터리의 충전 성능도 제한될 수 있습니다. 포르쉐 충전 플래너(판매 국가에 따라 제공 여부 다름)와 배터리 사전 온도 설정 기능을 이용하여 충전 전에 배터리를 예열하여 최적의 충전 상태로 만들어줍니다."},
        {"question": "Q5. 도움이 필요한 경우 어디에 연락해야 하나요?", "answer": "포르쉐 충전 하드웨어 제품 및 설치 방법 또는 발생하는 문제에 대해 궁금하신 점이 있으시면 포르쉐 공식 서비스 센터로 문의하시기 바랍니다. \n 포르쉐 충전 서비스(판매 국가에 따라 제공 여부 다름)에서의 공용 충전에 대한 문의는 언제나 포르쉐 커넥트 지원 서비스를 통해 도움을 받을 수 있습니다. 뿐만 아니라 차량에 문제가 생길 경우 포르쉐 어시스턴스 콜 센터를 통해 접수할 수 있습니다."},
    ],
}

st.subheader(f"FAQ for {selected_company}")

for faq in faq_data[selected_company]:
    with st.expander(faq["question"]):
        st.write(faq["answer"])
