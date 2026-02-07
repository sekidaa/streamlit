import streamlit as st

st.title('ユーザー入力の処理')

# テキスト入力
user_name = st.text_input('あなたの名前を入力してください', 'ゲスト')

# スライダー入力
age = st.slider('年齢を選択してください', 0, 100, 25)

# ボタンと条件分岐
if st.button('送信'):
    st.write(f'こんにちは、{user_name}さん（{age}歳）！')