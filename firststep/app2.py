import streamlit as st
import pandas as pd
import numpy as np

st.title('データの可視化')

# ダミーデータの作成
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.subheader('データフレームの表示')
# データフレームを表示（ソートや列幅調整が可能）
st.dataframe(df)

st.subheader('ラインチャートの表示')
# 自動的にグラフを描画
st.line_chart(df)