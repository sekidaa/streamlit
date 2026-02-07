# Home.py
import streamlit as st

st.set_page_config(
    page_title="データ分析ポータル",
    page_icon="🏠",
)

st.title("データ分析ポータルへようこそ")

st.markdown("""
### アプリケーション構成
サイドバーからページを選択してください。

1. **Upload**: 分析用CSVデータのアップロード
2. **Analysis**: データの可視化と集計
""")

# セッションステートの初期化（未定義の場合のみ）
if 'shared_df' not in st.session_state:
    st.session_state['shared_df'] = None