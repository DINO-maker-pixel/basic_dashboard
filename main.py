import streamlit as st
import pandas as pd

# 데이터 생성
data = {
    '이름': ['무궁화', '튤립', '해바라기', '아이리스', '수선화'],
    '나라': ['대한민국', '네덜란드', '러시아', '프랑스', '파키스탄'],
    '개화시기': [7, 4, 8, 5, 12]
}

df = pd.DataFrame(data)

# Streamlit 대시보드 생성
st.title('Flowers Data Dashboard')
st.write('간단히 몇 가지의 꽃들을 소개합니다 :')

# 나라 선택 기능 추가
selected_country = st.selectbox("나라를 선택하세요", df['나라'].unique())
filtered_df = df[df['나라'] == selected_country]
st.write(f"{selected_country}의 꽃 정보:")
st.write(filtered_df)

# 개화시기에 관한 간단한 시각화
st.write("꽃들의 개화시기에 관한 그래프")
df.set_index('이름', inplace=True)
st.bar_chart(df['개화시기'])