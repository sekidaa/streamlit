# pages/01_upload.py
import streamlit as st
import pandas as pd

st.title("データのアップロード")

uploaded_file = st.file_uploader("CSVファイルを選択", type=['csv'])

if uploaded_file is not None:
    # データを読み込む
    df = pd.read_csv(uploaded_file)
    
    # 【重要】セッションステートに保存
    st.session_state['shared_df'] = df
    
    st.success(f"{uploaded_file.name} を読み込みました（{len(df)}行）")
    st.dataframe(df.head())
else:
    st.info("分析に使用するファイルをアップロードしてください。")