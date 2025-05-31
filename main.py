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
# 이미지 URL은 실제 사용 가능한 링크로 대체해야 합니다.
interior_data = {
    "디자인_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "최소_금액": [100, 500, 1000, 200, 600, 1200, 300, 700, 1100, 150, 550, 1050, 650, 1150, 250],
    "최대_금액": [400, 900, 2000, 500, 1000, 2500, 600, 1100, 2200, 450, 950, 2100, 1050, 2050, 550],
    "시공분야": ["도배/장판", "종합리모델링", "부분시공", "도배/장판", "종합리모델링", "부분시공", "종합리모델링", "부분시공", "도배/장판", "종합리모델링", "부분시공", "도배/장판", "종합리모델링", "부분시공", "도배/장판"],
    "방구조_선택": ["원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "원룸", "아파트/빌라", "주택", "원룸"],
    "추구미": ["미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리", "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "러블리"],
    "디자인_이름": [
        "화이트 미니멀 원룸", "모던 아파트 리모델링", "내추럴 주택 베란다", "인더스트리얼 스튜디오",
        "레트로 감성 아파트", "클래식 주택 서재", "북유럽 스타일 거실", "빈티지 카페 스타일",
        "러블리 핑크 원룸", "미니멀 아파트 서재", "모던 주택 욕실", "내추럴 원룸 침실",
        "인더스트리얼 다이닝룸", "레트로 주택 주방", "러블리 미니 거실"
    ],
    "이미지_URL": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Muji_Interior_Design.jpg/640px-Muji_Interior_Design.jpg", # 미니멀
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Modern_Minimalist_Living_Room.jpg/640px-Modern_Minimalist_Living_Room.jpg", # 모던
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Interi%C3%B6r_fr%C3%A5n_Huset_Dreyer.jpg/640px-Interi%C3%B6r_fr%C3%A5n_Huset_Dreyer.jpg", # 내추럴 (나무톤)
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Interior_of_a_loft_apartment_in_the_Meatpacking_District%2C_New_York_City.jpg/640px-Interior_of_a_loft_apartment_in_the_Meatpacking_District%2C_New_York_City.jpg", # 인더스트리얼
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Mid-century_modern_living_room_in_a_house_on_the_south_side_of_Edinburgh.jpg/640px-Mid-century_modern_living_room_in_a_house_on_the_south_side_of_Edinburgh.jpg", # 레트로
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Living_room_interior_design_ideas_%285%29.jpg/640px-Living_room_interior_design_ideas_%285%29.jpg", # 클래식
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Home_interior_photography_%28cropped%29.jpg/640px-Home_interior_photography_%28cropped%29.jpg", # 북유럽
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vintage_Interior_Design_Studio.jpg/640px-Vintage_Interior_Design_Studio.jpg", # 빈티지
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Modern_Minimalist_Living_Room_in_Pink_and_White_Colors.jpg/640px-Modern_Minimalist_Living_Room_in_Pink_and_White_Colors.jpg", # 러블리 (핑크)
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Modern_interior_design_living_room.jpg/640px-Modern_interior_design_living_room.jpg", # 미니멀
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bathroom_with_Modern_Furniture.jpg/640px-Bathroom_with_Modern_Furniture.jpg", # 모던
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Modern_wooden_interior_design.jpg/640px-Modern_wooden_interior_design.jpg", # 내추럴
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Industrial_style_loft_with_exposed_brick_wall_and_high_ceilings.jpg/640px-Industrial_style_loft_with_exposed_brick_wall_and_high_ceilings.jpg", # 인더스트리얼
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Retro_Kitchen_Interior.jpg/640px-Retro_Kitchen_Interior.jpg", # 레트로
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Cute_Room_Interior_Design.jpg/640px-Cute_Room_Interior_Design.jpg" # 러블리
    ],
    "시공분야_링크": [
        "https://blog.naver.com/PostView.naver?blogId=kcc_official&logNo=223363364448", # 도배/장판 예시
        "https://blog.naver.com/PostView.naver?blogId=spacea3&logNo=223348600989", # 종합리모델링 예시
        "https://blog.naver.com/PostView.naver?blogId=hanssem_official&logNo=223389063519", # 부분시공 예시
        "https://blog.naver.com/PostView.naver?blogId=kcc_official&logNo=223363364448",
        "https://blog.naver.com/PostView.naver?blogId=spacea3&logNo=223348600989",
        "https://blog.naver.com/PostView.naver?blogId=hanssem_official&logNo=223389063519",
        "https://blog.naver.com/PostView.naver?blogId=spacea3&logNo=223348600989",
        "https://blog.naver.com/PostView.naver?blogId=hanssem_official&logNo=223389063519",
        "https://blog.naver.com/PostView.naver?blogId=kcc_official&logNo=223363364448",
        "https://blog.naver.com/PostView.naver?blogId=spacea3&logNo=223348600989",
        "https://blog.naver.com/PostView.naver?blogId=hanssem_official&logNo=223389063519",
        "https://blog.naver.com/PostView.naver?blogId=kcc_official&logNo=223363364448",
        "https://blog.naver.com/PostView.naver?blogId=spacea3&logNo=223348600989",
        "https://blog.naver.com/PostView.naver?blogId=hanssem_official&logNo=223389063519",
        "https://blog.naver.com/PostView.naver?blogId=kcc_official&logNo=223363364448"
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

# 2. 시공 분야 선택
field_options = ["상관없음", "도배/장판", "부분시공", "종합리모델링"]
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
            st.write(f"**🔗 시공 분야 관련 정보:** [자세히 알아보기]({design['시공분야_링크']})") # 링크 추가
            st.markdown("---") # 각 추천 디자인 구분선

    if len(filtered_df) > display_count:
        st.info(f"선택하신 조건에 맞는 다른 디자인들도 있습니다. 더 구체적인 조건을 선택하거나 예산 범위를 조절해보세요!")

else:
    st.warning(f"선택하신 조건 (예산 {selected_budget}만원 포함)에 맞는 디자인을 찾을 수 없습니다. 조건을 변경하거나 예산 범위를 조절하여 더 많은 디자인을 살펴보세요.")

st.markdown("---")

# --- 앱 하단 메시지 수정 ---
st.markdown(
    """
    <div style="text-align: center; font-size: 1.1em; color: #6a0dad;">
        😊 저희 사이트를 이용해주셔서 감사합니다! 😊
    </div>
    """,
    unsafe_allow_html=True
)
