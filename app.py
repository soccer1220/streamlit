import streamlit as st
import openai

openai.api_key = st.secrets['api_key']

st.write('# 형준 홈페이지')
chart_data = [100, 150, 300, 600, 1400]
st.bar_chart(chart_data)

with st.form('name'):
    name_input = st.text_input('이름을 입력하세요')
    birth_input = st.text_input('생년월일(8자리)을 입력하세요')
    user_sumit = st.form_submit_button('입력')
    
    if user_sumit: 
        if name_input and birth_input:
            st.write('환영합니다 {}님!'.format(name_input))
        elif not name_input:
            st.markdown(":red[이름을 다시 입력해주세요!]")
        else:
            st.markdown(":red[생년월일을 다시 입력해주세요!]")
