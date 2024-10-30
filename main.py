import streamlit as st
import pandas as pd

data = {
    '이름' : ['무궁화', '튤립', '해바라기', '아이리스', '수선화'],
    '나라' : ['대한민국', '네덜란드', '러시아', '프랑스', '파키스탄'],
    '개화시기' : [7, 4, 8, 5, 12] 
    }

df = pd.DataFrame(data)

# Streamlit 대시보드 생성
st.title('Flowers Data Dashboard')
st.write('간단히 몇 가지의 꽃들을 소개합니다 :')

# 대시보드에 데이터프레임 표시
st.write(df)

# 개화시기에 관한 간단한 시각화
st.write("꽃들의 개화시기에 관한 그래프")
df.set_index('이름', inplace=True)
st.bar_chart(df['개화시기'])