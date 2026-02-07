import streamlit as st
import pandas as pd
import numpy as np

st.title('レイアウトの活用')

# サイドバーへの配置
st.sidebar.header('設定')
option = st.sidebar.selectbox(
    '表示するデータを選択',
    ['データセットA', 'データセットB']
)

# カラムによる横並び配置
col1, col2 = st.columns(2)

with col1:
    st.header('左カラム')
    st.write(f'選択中のデータ: {option}')
    # ここに個別のチャートなどを配置可能

with col2:
    st.header('右カラム')
    st.metric(label="現在の気温", value="24 °C", delta="1.2 °C")