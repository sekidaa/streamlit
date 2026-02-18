import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# ページ設定
st.set_page_config(
    page_title="BigQuery Country Explorer",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 BigQuery 国別データ探索アプリ")

# --- 1. BigQueryクライアントの初期化 ---
@st.cache_resource
def get_bq_client():
    try:
        # secrets.toml から認証情報を取得
        if "connections" in st.secrets and "bq_conn" in st.secrets["connections"]:
            key_dict = st.secrets["connections"]["bq_conn"]
        else:
            key_dict = st.secrets
            
        creds = service_account.Credentials.from_service_account_info(key_dict)
        client = bigquery.Client(credentials=creds, project=key_dict["project_id"])
        return client
    except Exception as e:
        st.error(f"認証エラー: secrets.toml の設定を確認してください。\n{e}")
        return None

client = get_bq_client()
if not client:
    st.stop()

# --- 2. サイドバー設定 ---
st.sidebar.header("🔍 クエリ設定")

# 国の選択
countries = ['Canada', 'France', 'Germany', 'Mexico', 'United States of America']
selected_country = st.sidebar.selectbox("国を選択", countries, index=3)

# 取得件数
limit_rows = st.sidebar.slider("最大取得件数 (LIMIT)", 10, 1000, 100)

# キャッシュ有効期限
ttl_val = st.sidebar.select_slider(
    "キャッシュ有効期限 (TTL)",
    options=[0, 60, 3600, 86400],
    value=3600,
    format_func=lambda x: f"{x}秒" if x > 0 else "なし (都度実行)"
)

# --- 3. データ取得関数 ---
@st.cache_data(ttl=ttl_val)
def run_query(sql_query):
    return client.query(sql_query).to_dataframe()

# --- 4. メイン処理 ---
# 【修正ポイント】
# 1. カラム名は全て小文字のスネークケース (country, sales, etc.)
# 2. 全てSTRING型なので、数値計算やソートに使うカラムは CAST(... AS FLOAT64) で数値に変換する
sql = f"""
    SELECT
        country,
        product,
        CAST(units_sold AS FLOAT64) AS units_sold,
        CAST(sales AS FLOAT64) AS sales,
        CAST(gross_sales AS FLOAT64) AS gross_sales,
        CAST(profit AS FLOAT64) AS profit
    FROM
        `streamlit-app-project-487816.sample.result`
    WHERE
        country = '{selected_country}'
    ORDER BY
        sales DESC
    LIMIT {limit_rows}
"""

st.markdown("### 🛠 実行するSQL")
st.code(sql, language="sql")

if st.button("🚀 クエリを実行", type="primary"):
    try:
        with st.spinner('BigQueryからデータを取得中...'):
            df = run_query(sql)
        
        st.success(f"取得完了: {len(df)} 件")
        
        if not df.empty:
            # KPI表示
            # SQLで数値に変換済みなので、そのまま合計計算できます
            total_sales = df['sales'].sum()
            total_units = df['units_sold'].sum()
            total_profit = df['profit'].sum()
            
            m1, m2, m3 = st.columns(3)
            m1.metric("対象国", selected_country)
            m2.metric("総売上 ($)", f"{total_sales:,.2f}")
            m3.metric("総利益 ($)", f"{total_profit:,.2f}")
            
            st.divider()

            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("📊 製品別 売上チャート")
                # groupbyで集計
                chart_data = df.groupby("product")["sales"].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)

            with col2:
                st.subheader("📋 詳細データリスト")
                st.dataframe(df, use_container_width=True)
        else:
            st.warning("データが見つかりませんでした。")

    except Exception as e:
        st.error(f"エラーが発生しました:\n{e}")
        st.info("※ STRING型のカラムを数値として計算するために CAST関数を使用しています。")