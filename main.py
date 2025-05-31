   import streamlit as st

st.title("MBTI별 공부법 추천")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

study_tips = {
    "ISTJ": "체계적인 계획표를 만들어 따라가며 공부하면 효율적입니다.",
    "ISFJ": "조용한 공간에서 혼자 정리하며 복습하는 공부법이 잘 맞습니다.",
    "INFJ": "개념의 깊은 이해와 스스로 정리하는 시간이 중요합니다.",
    "INTJ": "장기 목표를 세우고 전략적으로 공부하는 것이 효과적입니다.",
    "ISTP": "실습과 문제풀이를 통해 배우는 방식이 효과적입니다.",
    "ISFP": "감각적으로 느끼는 공부—색깔, 도식화—를 활용해보세요.",
    "INFP": "의미와 가치를 느낄 수 있는 방식으로 공부할 때 몰입할 수 있습니다.",
    "INTP": "논리적 흐름을 이해하고 스스로 설명해보는 것이 중요합니다.",
    "ESTP": "짧고 집중도 높은 학습 세션과 실전 문제 풀이가 잘 맞습니다.",
    "ESFP": "친구와 함께 이야기하며 배우거나, 활동적인 학습법이 효과적입니다.",
    "ENFP": "다양한 자료를 이용해 지루하지 않게 학습하는 게 좋습니다.",
    "ENTP": "토론하고 새로운 시각으로 접근해보는 방식이 잘 맞습니다.",
    "ESTJ": "체계적인 일정과 반복 학습으로 확실하게 실력을 다질 수 있습니다.",
    "ESFJ": "계획에 따라 공부하고, 다른 사람에게 설명해보는 것도 효과적입니다.",
    "ENFJ": "그룹 스터디를 하거나 사람들과 함께 학습하며 동기부여를 얻습니다.",
    "ENTJ": "목표 설정 후 성과 중심으로 학습 계획을 실행하는 것이 효율적입니다."
}

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

if selected_mbti:
    st.subheader(f"{selected_mbti} 유형의 공부법 추천")
    st.write(study_tips[selected_mbti])
