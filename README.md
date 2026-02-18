# StreamlitでWebアプリケーションを作成する

このリポジトリは、PythonのStreamlitフレームワークを用いたWebアプリケーション開発の学習記録と、その成果物である「CSV分析ツール」および「BigQuery連携アプリケーション」のソースコードです。
基礎的な機能実装から、実務を想定したマルチページアプリケーション（MPA）の構築、クラウドデータベース（BigQuery）との連携までを段階的に実装しています。

## 🌐 デモサイト
学習の成果物として作成したアプリケーションは、以下のURLで公開されています。

### 1. CSV分析ツール
**URL:** https://app-uploadcsv.streamlit.app/

### 2. BigQuery連携アプリケーション
**URL:** https://app-3t8sp8si4wk7ikzaappztgp.streamlit.app/

---

## 📂 ディレクトリ構成と学習ステップ

本リポジトリは、学習段階ごとのファイル (`firststep/`) と、本番運用を想定したアプリケーション (`my_app/`, `bq_app/`) で構成されています。

```text
.
├── firststep/           # Streamlitの基本機能を段階的に実装した学習用ファイル
│   ├── app.py           
│   ├── app2.py          
│   ├── app3.py          
│   └── app4.py          
│
├── my_app/              # 【Web公開中】CSV分析用マルチページアプリケーション
│   ├── home.py          # メインページ（アプリのエントリーポイント）
│   ├── pages/           # 機能ごとにページを分割
│   │   ├── 01_Upload.py # CSVアップロード機能（Session Stateによるデータ保持）
│   │   └── 02_Analysis.py # データの統計・可視化機能
│   └── requirements.txt # デプロイ用依存ライブラリ定義
│
├── bq_app/              # 【Web公開中】BigQuery連携アプリケーション
│   ├── main.py          # BigQueryデータ取得・可視化ロジック
│   ├── .streamlit/      # 接続設定（secrets.tomlなど ※Git管理対象外）
│   └── requirements.txt # google-cloud-bigquery等を含む依存定義
│
└── README.md