import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="세계 시가총액 Top 10 변화", layout="wide")

st.title("🌍 세계 시가총액 Top 10 기업 (최근 3년간 변화)")
st.markdown("💹 아래는 글로벌 시가총액 상위 10개 기업의 시가총액 변화 추이를 나타낸 그래프입니다. 그래프를 확대하거나 마우스를 올려 상세 정보를 확인할 수 있어요!")

# 샘플 기업 리스트
top10_companies = [
    "Apple", "Microsoft", "Saudi Aramco", "Alphabet (Google)",
    "Amazon", "NVIDIA", "Berkshire Hathaway", "Meta (Facebook)",
    "TSMC", "Tesla"
]

# 가상의 연도별 시가총액 데이터 생성 (단위: 조 USD)
years = ["2022", "2023", "2024"]
data = {
    "Apple": [2.4, 2.6, 2.9],
    "Microsoft": [2.2, 2.5, 2.8],
    "Saudi Aramco": [2.0, 2.1, 2.3],
    "Alphabet (Google)": [1.5, 1.7, 2.0],
    "Amazon": [1.4, 1.5, 1.8],
    "NVIDIA": [0.8, 1.3, 2.2],
    "Berkshire Hathaway": [0.7, 0.8, 0.9],
    "Meta (Facebook)": [0.6, 0.9, 1.1],
    "TSMC": [0.5, 0.6, 0.8],
    "Tesla": [0.8, 0.6, 0.7],
}

# 데이터프레임으로 변환
df = pd.DataFrame(data, index=years)

# Plotly 그래프 생성
fig = go.Figure()
for company in top10_companies:
    fig.add_trace(go.Scatter(
        x=years,
        y=df[company],
        mode="lines+markers",
        name=company
    ))

fig.update_layout(
    title="최근 3년간 시가총액 변화 (단위: 조 달러)",
    xaxis_title="연도",
    yaxis_title="시가총액 (조 USD)",
    legend_title="기업명",
    hovermode="x unified"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 참고 링크
st.caption("📊 본 데이터는 예시용이며, 실제 시가총액은 증권사/금융기관 기준 참고 바랍니다.")
