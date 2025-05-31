import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(layout="wide", page_title="✨ 맞춤형 인테리어 디자인 추천 ✨")

# 앱 제목
st.title("🏡 당신의 꿈의 공간을 찾아보세요! ✨")
st.markdown("---")

st.write(
    """
    원하는 인테리어 스타일과 조건을 선택하여, 당신에게 딱 맞는 맞춤형 디자인을 추천받고
    관련 시공 분야에 대한 정보를 확인해보세요.
    """
)

# --- 인테리어 디자인 데이터 (예시) ---
# 모든 리스트의 길이를 20개로 일치시켰습니다.
interior_data = {
    "디자인_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "최소_금액": [100, 500, 1000, 200, 600, 1200, 300, 700, 1100, 150, 550, 1050, 650, 1150, 250, 400, 800, 900, 1300, 350],
    "최대_금액": [400, 900, 2000, 500, 1000, 2500, 600, 1100, 2200, 450, 950, 2100, 1050, 2050, 550, 750, 1250, 1500, 2800, 650],
    "시공분야": [
        "도배/장판", "종합리모델링", "부분시공", "벽", "화장실", "부엌", "공부방", "안방", "침실",
        "도배/장판", "벽", "화장실", "부엌", "공부방", "안방", "침실", "종합리모델링", "부분시공", "종합리모델링", "벽"
    ],
    "방구조_선택": [
        "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "아파트/빌라", "주택", "원룸",
        "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택"
    ],
    "추구미": [
        "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리",
        "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리", "모던", "미니멀" # 추구미 항목 1개 추가 (총 20개)
    ],
    "디자인_이름": [
        "화이트 미니멀 원룸 도배", "모던 아파트 종합리모델링", "내추럴 주택 부분시공", "인더스트리얼 벽 포인트",
        "레트로 화장실 리모델링", "클래식 부엌 디자인", "북유럽 공부방 꾸미기", "빈티지 안방 스타일링",
        "러블리 침실 인테리어", "미니멀 원룸 도배", "모던 주택 벽면", "내추럴 화장실 리모델링",
        "인더스트리얼 부엌", "레트로 공부방", "클래식 안방", "북유럽 침실",
        "빈티지 아파트 종합", "러블리 원룸 부분", "모던 주택 종합", "미니멀 벽"
    ],
    "이미지_URL": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Muji_Interior_Design.jpg/640px-Muji_Interior_Design.jpg", # 미니멀
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Modern_Minimalist_Living_Room.jpg/640px-Modern_Minimalist_Living_Room.jpg", # 모던
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Interi%C3%B6r_fr%C3%A5n_Huset_Dreyer.jpg/640px-Interi%C3%B6r_fr%C3%A5n_Huset_Dreyer.jpg", # 내추럴 (나무톤)
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Interior_of_a_loft_apartment_in_the_Meatpacking_District%2C_New_York_City.jpg/640px-Interior_of_a_loft_apartment_in_the_Meatpacking_District%2C_New_York_City.jpg", # 인더스트리얼 (벽)
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bathroom_with_Modern_Furniture.jpg/640px-Bathroom_with_Modern_Furniture.jpg", # 화장실
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Retro_Kitchen_Interior.jpg/640px-Retro_Kitchen_Interior.jpg", # 부엌
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Home_office_interior_design_ideas_%282%29.jpg/640px-Home_office_interior_design_ideas_%282%29.jpg", # 공부방
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vintage_Interior_Design_Studio.jpg/640px-Vintage_Interior_Design_Studio.jpg", # 안방 (빈티지)
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Cute_Room_Interior_Design.jpg/640px-Cute_Room_Interior_Design.jpg", # 침실 (러블리)
        "
