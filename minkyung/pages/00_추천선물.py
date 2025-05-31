import streamlit as st

st.title("MBTI별 선물 추천")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

gift_suggestions = {
    "ISTJ": "고급 펜, 다이어리, 실용적인 전자기기",
    "ISFJ": "포근한 담요, 손편지, 따뜻한 머그컵",
    "INFJ": "감성적인 책, 향초, 명상 관련 아이템",
    "INTJ": "퍼즐, 고급 노트북 스탠드, 자기계발서",
    "ISTP": "멀티툴, 이어폰, 드론 같은 IT 장난감",
    "ISFP": "예쁜 무드등, 아트용품, 향수",
    "INFP": "감성 포스터, 문구류, 핸드메이드 아이템",
    "INTP": "두뇌 자극 보드게임, 테크 가젯, 철학서",
    "ESTP": "스마트워치, 스포츠 용품, 최신 트렌드 상품",
    "ESFP": "패션 액세서리, 인테리어 소품, 콘서트 티켓",
    "ENFP": "여행용 아이템, 독특한 소품, 감성 다이어리",
    "ENTP": "재미있는 책, 창의적인 키트, 대화 주제 카드",
    "ESTJ": "비즈니스 가방, 고급 다이어리, 정장 액세서리",
    "ESFJ": "꽃다발, 감동적인 카드, 홈베이킹 세트",
    "ENFJ": "힐링 도구, 감사 카드, 커피 머신",
    "ENTJ": "프리미엄 다이어리, 전략 보드게임, 리더십 도서"
}

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

if selected_mbti:
    st.subheader(f"{selected_mbti} 유형에게 추천하는 선물은?")
    st.write(f"🎁 {gift_suggestions[selected_mbti]}")
