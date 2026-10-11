# -*- coding: utf-8 -*-
"""
ピタッと環境整備マスター（スマホアプリ版）

  streamlit run streamlit_app.py

・スタッフ用：トップページ（ゲーム。結果画面から記録→ランキングまでアプリ内で完結）
・管理者用 ：/admin（パスワードで保護。全記録の一覧・CSVダウンロード）
"""
import os

import streamlit as st
from PIL import Image

from pitatto import config

HERE = os.path.dirname(os.path.abspath(__file__))
ICON = Image.open(os.path.join(HERE, "src", "assets", "a_bear_happy.webp"))

st.set_page_config(page_title=config.APP_TITLE, page_icon=ICON, layout="wide",
                   initial_sidebar_state="collapsed")

pages = [
    st.Page(os.path.join("views", "game.py"), title=config.APP_TITLE, icon="🧸", default=True),
    st.Page(os.path.join("views", "admin.py"), title="管理者ページ", icon="🔒", url_path="admin"),
]
# メニューは出さない（スタッフには管理者ページの存在を見せない。管理者はURLの末尾に /admin）
st.navigation(pages, position="hidden").run()
