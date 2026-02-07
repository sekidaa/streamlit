# pages/02_analysis.py
import streamlit as st

st.title("データ分析")

# セッションステートからデータを取得
df = st.session_state.get('shared_df')

if df is not None:
    st.write("### データの統計情報")
    st.write(df.describe())

    # 数値カラムの可視化
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        selected_col = st.selectbox("グラフ化するカラムを選択", numeric_cols)
        st.line_chart(df[selected_col])
    else:
        st.warning("数値データが含まれていません。")
else:
    st.warning("データがロードされていません。「01_upload」ページでCSVをアップロードしてください。")