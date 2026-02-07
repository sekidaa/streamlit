import streamlit as st
import pandas as pd
import time

st.title('CSVアップロードとキャッシュ処理')

# --- 関数定義 ---

# @st.cache_data: データ変換やロードなど、結果をシリアライズ可能な処理に使用
# この関数は引数（file）が変わらない限り、2回目以降は実行されず結果だけが返されます
@st.cache_data
def load_data(file):
    # 重い処理をシミュレーション（3秒待機）
    time.sleep(3)
    
    # CSVを読み込む
    df = pd.read_csv(file)
    return df

# --- メイン処理 ---

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=['csv'])

if uploaded_file is not None:
    st.write("ファイル読み込み開始...")
    
    # キャッシュ有効化された関数を呼び出す
    # 1回目は3秒かかるが、2回目以降（ボタン操作時など）は一瞬で終わる
    df = load_data(uploaded_file)
    
    st.success("読み込み完了！")
    
    # データ情報の表示
    st.write(f"形状: {df.shape}")
    st.dataframe(df.head())

    # フィルタリング（キャッシュ効果の確認用）
    # スライダーを動かして再実行されても、load_dataはスキップされるため高速
    if not df.empty and df.select_dtypes(include='number').shape[1] > 0:
        target_col = df.select_dtypes(include='number').columns[0]
        max_val = float(df[target_col].max())
        min_val = float(df[target_col].min())
        
        threshold = st.slider(
            f"{target_col} の閾値",
            min_value=min_val,
            max_value=max_val,
            value=min_val
        )
        
        filtered_df = df[df[target_col] > threshold]
        st.write(f"フィルタ後の件数: {len(filtered_df)}")
        st.line_chart(filtered_df[target_col])
else:
    st.info("CSVファイルをアップロードすると、ここにデータが表示されます。")