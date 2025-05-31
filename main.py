import streamlit as st

st.title("MBTI별 잘 어울리는 직업 추천")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti_jobs = {
    "ISTJ": ["회계사", "관리자", "군인"],
    "ISFJ": ["간호사", "초등교사", "사회복지사"],
    "INFJ": ["상담가", "심리학자", "작가"],
    "INTJ": ["전략기획가", "과학자", "데이터 분석가"],
    "ISTP": ["엔지니어", "기술자", "파일럿"],
    "ISFP": ["디자이너", "예술가", "수의사"],
    "INFP": ["작가", "예술가", "상담사"],
    "INTP": ["개발자", "이론물리학자", "철학자"],
    "ESTP": ["기업가", "마케터", "스포츠 트레이너"],
    "ESFP": ["연예인", "이벤트 기획자", "유튜버"],
    "ENFP": ["기획자", "광고 AE", "작가"],
    "ENTP": ["창업가", "변호사", "기획자"],
    "ESTJ": ["경영자", "행정직", "감독관"],
    "ESFJ": ["간호사", "교사", "호텔 매니저"],
    "ENFJ": ["교사", "상담가", "리더십 강사"],
    "ENTJ": ["CEO", "전략가", "프로젝트 매니저"]
}

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

if selected_mbti:
    st.subheader(f"{selected_mbti} 유형에게 어울리는 직업은:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
