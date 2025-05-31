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
# 금액대를 실제 숫자로 추가했습니다. (단위: 만 원)
# 시공 분야 옵션을 상세하게 변경했습니다.
# 이미지 URL은 실제 사용 가능한 링크로 대체해야 합니다.
# 시공분야_링크를 '오늘의 집' 관련 페이지로 변경했습니다.
interior_data = {
    "디자인_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "최소_금액": [100, 500, 1000, 200, 600, 1200, 300, 700, 1100, 150, 550, 1050, 650, 1150, 250, 400, 800, 900, 1300, 350],
    "최대_금액": [400, 900, 2000, 500, 1000, 2500, 600, 1100, 2200, 450, 950, 2100, 1050, 2050, 550, 750, 1250, 1500, 2800, 650],
    "시공분야": [
        "도배/장판", "종합리모델링", "부분시공", "벽", "화장실", "부엌", "공부방", "안방", "침실",
        "도배/장판", "벽", "화장실", "부엌", "공부방", "안방", "침실", "종합리모델링", "부분시공", "벽"
    ],
    "방구조_선택": [
        "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "아파트/빌라", "주택", "원룸",
        "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택"
    ],
    "추구미": [
        "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리",
        "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리", "모던", "미니멀"
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
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Modern_interior_design_living_room.jpg/640px-Modern_interior_design_living_room.jpg", # 미니멀
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Industrial_style_loft_with_exposed_brick_wall_and_high_ceilings.jpg/640px-Industrial_style_loft_with_exposed_brick_wall_and_high_ceilings.jpg", # 벽
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Modern_bathroom_design.jpg/640px-Modern_bathroom_design.jpg", # 화장실
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Kitchen_Interior.jpg/640px-Kitchen_Interior.jpg", # 부엌
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Home_Office_with_Desk%2C_Chair%2C_and_Bookshelves.jpg/640px-Home_Office_with_Desk%2C_Chair%2C_and_Bookshelves.jpg", # 공부방
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bedroom_Interior_Design_Ideas_%281%29.jpg/640px-Bedroom_Interior_Design_Ideas_%281%29.jpg", # 안방
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Minimalist_Bedroom_with_Wooden_Furniture.jpg/640px-Minimalist_Bedroom_with_Wooden_Furniture.jpg", # 침실
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Living_Room_Interior_Design.jpg/640px-Living_Room_Interior_Design.jpg", # 종합리모델링
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Modern_Minimalist_Living_Room_in_Pink_and_White_Colors.jpg/640px-Modern_Minimalist_Living_Room_in_Pink_and_White_Colors.jpg", # 부분시공 (거실 일부)
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Modern_Living_Room_Design.jpg/640px-Modern_Living_Room_Design.jpg", # 종합리모델링
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Colorful_Interior_Design.jpg/640px-Colorful_Interior_Design.jpg" # 벽
    ],
    "시공분야_링크": [
        "https://ohou.se/projects?query=%EB%8F%84%EB%B0%B0%EC%9E%A5%ED%8C%90", # 오늘의 집 - 도배장판
        "https://ohou.se/projects?query=%EC%A2%85%ED%95%A9%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81", # 오늘의 집 - 종합리모델링
        "https://ohou.se/projects?query=%EB%B6%80%EB%B6%84%EC%8B%9C%EA%B3%B5", # 오늘의 집 - 부분시공
        "https://ohou.se/projects?query=%EB%B2%BD%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4", # 오늘의 집 - 벽 인테리어
        "https://ohou.se/projects?query=%ED%99%94%EC%9E%A5%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4", # 오늘의 집 - 화장실 인테리어
        "https://ohou.se/projects?query=%EB%B6%80%EC%97%87%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4", # 오늘의 집 - 부엌 인테리어
        "https://ohou.se/projects?query=%EA%B3%B5%EB%B6%80%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4", # 오늘의 집 - 공부방 인테리어
        "https://ohou.se/projects?query=%EC%95%88%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4", # 오늘의 집 - 안방 인테리어
        "https://ohou.se/projects?query=%EC%B9%A8%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4", # 오늘의 집 - 침실 인테리어
        "https://ohou.se/projects?query=%EB%8F%84%EB%B0%B0%EC%9E%A5%ED%8C%90",
        "https://ohou.se/projects?query=%EB%B2%BD%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%ED%99%94%EC%9E%A5%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EB%B6%80%EC%97%87%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EA%B3%B5%EB%B6%80%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EC%95%88%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EC%B9%A8%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EC%A2%85%ED%95%A9%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81",
        "https://ohou.se/projects?query=%EB%B6%80%EB%B6%84%EC%8B%9C%EA%B3%B5",
        "https://ohou.se/projects?query=%EC%A2%85%ED%95%A9%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81",
        "https://ohou.se/projects?query=%EB%B2%BD%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4"
    ]
}

df_interiors = pd.DataFrame(interior_data)

st.markdown("---")

# --- 사용자 입력 섹션 ---
st.subheader("💡 원하는 인테리어 조건을 선택해주세요!")

# 1. 예상 금액 입력 (숫자 입력)
st.write("💰 예상 금액은 어느 정도이신가요? (단위: 만 원)")
selected_budget = st.number_input(
    "금액을 입력하세요:",
    min_value=100,      # 최소 100만원부터 시작
    max_value=10000,    # 최대 1억 (10000만원)으로 제한
    value=500,          # 기본값 500만원
    step=50,            # 50만원 단위로 조절 가능
    format="%d"
)

# 2. 시공 분야 선택 (상세 옵션으로 변경)
field_options = [
    "상관없음",
    "도배/장판",
    "벽",
    "화장실",
    "부엌",
    "공부방",
    "안방",
    "침실",
    "부분시공", # 위의 상세 항목들을 포함할 수 있는 개념
    "종합리모델링" # 전체 리모델링
]
selected_field = st.selectbox("🔨 어떤 시공 분야에 관심 있으신가요?", field_options)

# 3. 방 구조 선택
room_options = ["상관없음", "원룸", "아파트/빌라", "주택"]
selected_room_structure = st.selectbox("🏠 어떤 방 구조를 인테리어하시나요?", room_options)

# 4. 추구미 (스타일) 선택
style_options = ["상관없음", "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리"]
selected_style = st.selectbox("🎨 어떤 인테리어 스타일을 추구하시나요?", style_options)

st.markdown("---")

# --- 추천 결과 섹션 ---
st.subheader("🎉 당신에게 추천하는 맞춤형 인테리어 디자인! 🎉")

# 필터링 로직
filtered_df = df_interiors.copy()

# 금액대 필터링: 입력된 금액이 디자인의 최소/최대 금액 범위 안에 있는 경우
filtered_df = filtered_df[
    (filtered_df["최소_금액"] <= selected_budget) &
    (filtered_df["최대_금액"] >= selected_budget)
]

if selected_field != "상관없음":
    # '부분시공'이나 '종합리모델링'이 선택된 경우, 그 외의 상세 시공 분야도 포함되도록
    if selected_field == "부분시공":
        # '부분시공'에 해당하는 모든 세부 시공을 포함하도록 데이터 확장
        filtered_df = filtered_df[filtered_df["시공분야"].isin(["벽", "화장실", "부엌", "공부방", "안방", "침실", "도배/장판", "부분시공"])]
    elif selected_field == "종합리모델링":
        # '종합리모델링'에 해당하는 모든 시공을 포함하도록 데이터 확장
        filtered_df = filtered_df[filtered_df["시공분야"].isin(field_options[1:])] # '상관없음' 제외 모든 시공 분야
    else:
        # 특정 시공 분야가 선택된 경우
        filtered_df = filtered_df[filtered_df["시공분야"] == selected_field]

if selected_room_structure != "상관없음":
    filtered_df = filtered_df[filtered_df["방구조_선택"] == selected_room_structure]
if selected_style != "상관없음":
    filtered_df = filtered_df[filtered_df["추구미"] == selected_style]

# 추천 결과 표시
if not filtered_df.empty:
    st.write(f"예상하신 **{selected_budget}만원** 예산과 선택하신 조건에 맞는 디자인들을 찾았습니다:")

    # 결과를 무작위로 섞어서 매번 다른 추천처럼 보이게 함 (선택 사항)
    # filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    # 최대 3개까지만 보여주기 (너무 많으면 페이지가 길어지므로)
    display_count = min(3, len(filtered_df))
    for i in range(display_count):
        design = filtered_df.iloc[i]
        st.markdown(f"#### {i + 1}. {design['디자인_이름']} ({design['추구미']} 스타일)")
        
        col_img, col_info = st.columns([1, 2])
        with col_img:
            st.image(design['이미지_URL'], caption=design['디자인_이름'], use_column_width=True)
        with col_info:
            st.write(f"**💰 예상 비용:** {design['최소_금액']}만원 ~ {design['최대_금액']}만원")
            st.write(f"**🔨 시공 분야:** {design['시공분야']}")
            st.write(f"**🏠 방 구조:** {design['방구조_선택']}")
            st.write(f"**🔗 시공 분야 관련 정보:** [오늘의 집에서 더 알아보기]({design['시공분야_링크']})") # 링크 변경
            st.markdown("---") # 각 추천 디자인 구분선

    if len(filtered_df) > display_count:
        st.info(f"선택하신 조건에 맞는 다른 디자인들도 있습니다. 더 구체적인 조건을 선택하거나 예산 범위를 조절해보세요!")

else:
    st.warning(f"선택하신 조건 (예산 {selected_budget}만원 포함)에 맞는 디자인을 찾을 수 없습니다. 조건을 변경하거나 예산 범위를 조절하여 더 많은 디자인을 살펴보세요.")

st.markdown("---")

# --- 앱 하단 메시지 (스마일 얼굴 추가) ---
st.markdown(
    """
    <div style="text-align: center; font-size: 1.1em; color: #6a0dad;">
        😊 저희 사이트를 이용해주셔서 감사합니다! 😊
    </div>
    """,
    unsafe_allow_html=True
)
