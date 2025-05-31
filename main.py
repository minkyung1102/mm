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
# '색상_선택' 컬럼을 추가하고 각 디자인에 어울리는 색상 리스트를 할당했습니다.
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
        "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리", "모던", "미니멀"
    ],
    "색상_선택": [ # 각 디자인에 어울리는 색상 리스트 (복수 선택 가능성을 고려)
        ["화이트", "그레이"], ["블랙", "그레이", "화이트"], ["베이지", "브라운"], ["그레이", "블랙"], ["레드", "브라운", "아이보리"],
        ["골드", "다크우드"], ["화이트", "그레이", "스카이블루"], ["브라운", "블랙", "오렌지"], ["핑크", "화이트"],
        ["화이트", "아이보리"], ["블랙", "그레이"], ["베이지", "화이트"], ["그레이", "블랙", "우드"], ["오렌지", "브라운"],
        ["다크우드", "골드"], ["베이지", "아이보리", "화이트"], ["브라운", "그린"], ["핑크", "화이트"], ["그레이", "네이비"], ["화이트", "블랙"]
    ],
    "디자인_이름": [
        "화이트 미니멀 원룸 도배", "모던 아파트 종합리모델링", "내추럴 주택 부분시공", "인더스트리얼 벽 포인트",
        "레트로 화장실 리모델링", "클래식 부엌 디자인", "북유럽 공부방 꾸미기", "빈티지 안방 스타일링",
        "러블리 침실 인테리어", "미니멀 원룸 도배", "모던 주택 벽면", "내추럴 화장실 리모델링",
        "인더스트리얼 부엌", "레트로 공부방", "클래식 안방", "북유럽 침실",
        "빈티지 아파트 종합", "러블리 원룸 부분", "모던 주택 종합", "미니멀 벽"
    ],
    "이미지_URL": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Muji_Interior_Design.jpg/640px-Muji_Interior_Design.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Modern_Minimalist_Living_Room.jpg/640px-Modern_Minimalist_Living_Room.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Interi%C3%B6r_fr%C3%A5n_Huset_Dreyer.jpg/640px-Interi%C3%B6r_fr%C3%A5n_Huset_Dreyer.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Interior_of_a_loft_apartment_in_the_Meatpacking_District%2C_New_York_City.jpg/640px-Interior_of_a_loft_apartment_in_the_Meatpacking_District%2C_New_York_City.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bathroom_with_Modern_Furniture.jpg/640px-Bathroom_with_Modern_Furniture.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Retro_Kitchen_Interior.jpg/640px-Retro_Kitchen_Interior.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Home_office_interior_design_ideas_%282%29.jpg/640px-Home_office_interior_design_ideas_%282%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vintage_Interior_Design_Studio.jpg/640px-Vintage_Interior_Design_Studio.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Cute_Room_Interior_Design.jpg/640px-Cute_Room_Interior_Design.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Modern_interior_design_living_room.jpg/640px-Modern_interior_design_living_room.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Industrial_style_loft_with_exposed_brick_wall_and_high_ceilings.jpg/640px-Industrial_style_loft_with_exposed_brick_wall_and_high_ceilings.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Modern_bathroom_design.jpg/640px-Modern_bathroom_design.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Kitchen_Interior.jpg/640px-Kitchen_Interior.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Home_Office_with_Desk%2C_Chair%2C_and_Bookshelves.jpg/640px-Home_Office_with_Desk%2C_Chair%2C_and_Bookshelves.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bedroom_Interior_Design_Ideas_%281%29.jpg/640px-Bedroom_Interior_Design_Ideas_%281%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Minimalist_Bedroom_with_Wooden_Furniture.jpg/640px-Minimalist_Bedroom_with_Wooden_Furniture.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Living_Room_Interior_Design.jpg/640px-Living_Room_Interior_Design.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Modern_Minimalist_Living_Room_in_Pink_and_White_Colors.jpg/640px-Modern_Minimalist_Living_Room_in_Pink_and_White_Colors.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Modern_Living_Room_Design.jpg/640px-Modern_Living_Room_Design.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Colorful_Interior_Design.jpg/640px-Colorful_Interior_Design.jpg"
    ],
    "시공분야_링크": [
        "https://ohou.se/projects?query=%EB%8F%84%EB%B0%B0%EC%9E%A5%ED%8C%90",
        "https://ohou.se/projects?query=%EC%A2%85%ED%95%A9%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81",
        "https://ohou.se/projects?query=%EB%B6%80%EB%B6%84%EC%8B%9C%EA%B3%B5",
        "https://ohou.se/projects?query=%EB%B2%BD%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%ED%99%94%EC%9E%A5%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EB%B6%80%EC%97%87%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EA%B3%B5%EB%B6%80%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EC%95%88%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
        "https://ohou.se/projects?query=%EC%B9%A8%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
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

# 시공 분야별 오늘의 집 기본 링크 맵핑
ohou_links_by_field = {
    "도배/장판": "https://ohou.se/projects?query=%EB%8F%84%EB%B0%B0%EC%9E%A5%ED%8C%90",
    "벽": "https://ohou.se/projects?query=%EB%B2%BD%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
    "화장실": "https://ohou.se/projects?query=%ED%99%94%EC%9E%A5%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
    "부엌": "https://ohou.se/projects?query=%EB%B6%80%EC%97%87%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
    "공부방": "https://ohou.se/projects?query=%EA%B3%B5%EB%B6%80%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
    "안방": "https://ohou.se/projects?query=%EC%95%88%EB%B0%A9%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
    "침실": "https://ohou.se/projects?query=%EC%B9%A8%EC%8B%A4%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4",
    "부분시공": "https://ohou.se/projects?query=%EB%B6%80%EB%B6%84%EC%8B%9C%EA%B3%B5",
    "종합리모델링": "https://ohou.se/projects?query=%EC%A2%85%ED%95%A9%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81"
}


st.markdown("---")

# --- 사용자 입력 섹션 ---
st.subheader("💡 원하는 인테리어 조건을 선택해주세요!")

# 1. 예상 금액 입력 (숫자 입력)
st.write("💰 예상 금액은 어느 정도이신가요? (단위: 만 원)")
selected_budget = st.number_input(
    "금액을 입력하세요:",
    min_value=100,
    max_value=10000,
    value=500,
    step=50,
    format="%d"
)

# 2. 시공 분야 선택
field_options = [
    "상관없음", "도배/장판", "벽", "화장실", "부엌", "공부방", "안방", "침실",
    "부분시공", "종합리모델링"
]
selected_field = st.selectbox("🔨 어떤 시공 분야에 관심 있으신가요?", field_options)

# 3. 방 구조 선택
room_options = ["상관없음", "원룸", "아파트/빌라", "주택"]
selected_room_structure = st.selectbox("🏠 어떤 방 구조를 인테리어하시나요?", room_options)

# 4. 추구미 (스타일) 선택
style_options = ["상관없음", "미니멀", "모던", "내추럴", "인더스트리얼", "레트로", "클래식", "북유럽", "빈티지", "러블리"]
selected_style = st.selectbox("🎨 어떤 인테리어 스타일을 추구하시나요?", style_options)

# 5. 색상 선택 (새로 추가)
color_options = [
    "상관없음", "화이트", "그레이", "블랙", "베이지", "브라운", "우드", "레드", "오렌지",
    "아이보리", "골드", "다크우드", "스카이블루", "핑크", "그린", "네이비" # 추가 가능한 색상
]
selected_colors = st.multiselect("🌈 어떤 색상을 원하시나요? (복수 선택 가능)", color_options)

st.markdown("---")

# --- 추천 결과 섹션 ---
st.subheader("🎉 당신에게 추천하는 맞춤형 인테리어 디자인! 🎉")

# 필터링 로직
filtered_df = df_interiors.copy()

# 금액대 필터링
filtered_df = filtered_df[
    (filtered_df["최소_금액"] <= selected_budget) &
    (filtered_df["최대_금액"] >= selected_budget)
]

# 시공 분야 필터링
if selected_field != "상관없음":
    if selected_field == "부분시공":
        filtered_df = filtered_df[filtered_df["시공분야"].isin(["벽", "화장실", "부엌", "공부방", "안방", "침실", "도배/장판", "부분시공"])]
    elif selected_field == "종합리모델링":
        filtered_df = filtered_df[filtered_df["시공분야"].isin(field_options[1:])]
    else:
        filtered_df = filtered_df[filtered_df["시공분야"] == selected_field]

# 방 구조 필터링
if selected_room_structure != "상관없음":
    filtered_df = filtered_df[filtered_df["방구조_선택"] == selected_room_structure]

# 추구미 (스타일) 필터링
if selected_style != "상관없음":
    filtered_df = filtered_df[filtered_df["추구미"] == selected_style]

# 색상 필터링 (복수 선택 처리)
if "상관없음" not in selected_colors and selected_colors: # '상관없음'이 선택되지 않고, 뭔가 선택되었을 때
    # 디자인이 선택된 색상 중 하나라도 포함하는지 확인
    filtered_df = filtered_df[
        filtered_df["색상_선택"].apply(lambda design_colors: any(color in design_colors for color in selected_colors))
    ]


# 추천 결과 표시
if not filtered_df.empty:
    st.write(f"예상하신 **{selected_budget}만원** 예산, 선택하신 조건, 그리고 **선택하신 색상({', '.join(selected_colors)})**에 맞는 디자인들을 찾았습니다:")

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
            st.write(f"**🌈 주요 색상:** {', '.join(design['색상_선택'])}") # 색상 정보 표시
            st.write(f"**🔗 시공 분야 관련 정보:** [오늘의 집에서 더 알아보기]({design['시공분야_링크']})")
            st.markdown("---")

    if len(filtered_df) > display_count:
        st.info(f"선택하신 조건에 맞는 다른 디자인들도 있습니다. 더 구체적인 조건을 선택하거나 예산 범위를 조절해보세요!")

else:
    st.warning(f"선택하신 조건 (예산 **{selected_budget}만원**, 색상 **{', '.join(selected_colors) if selected_colors else '선택 안함'}** 포함)에 맞는 디자인을 찾을 수 없습니다.")
    
    if selected_field != "상관없음" and selected_field in ohou_links_by_field:
        st.write(f"하지만 **'{selected_field}'** 관련 디자인은 오늘의 집에서 더 찾아볼 수 있습니다:")
        st.markdown(f"**🔗 오늘의 집에서 {selected_field} 찾아보기:** [{ohou_links_by_field[selected_field]}]({ohou_links_by_field[selected_field]})")
    else:
        st.write("다양한 인테리어 아이디어를 얻으려면 오늘의 집을 방문해보세요:")
        st.markdown("**🔗 오늘의 집 바로가기:** [https://ohou.se/](https://ohou.se/)")
    
    st.info("조건을 변경하거나 '상관없음'을 선택하여 더 많은 디자인을 살펴보세요.")


st.markdown("---")

# --- 앱 하단 메시지 ---
st.markdown(
    """
    <div style="text-align: center; font-size: 1.1em; color: #6a0dad;">
        😊 저희 사이트를 이용해주셔서 감사합니다! 😊
    </div>
    """,
    unsafe_allow_html=True
)
