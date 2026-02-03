import streamlit as st
import os
import base64

# --- 1. 页面配置 ---
st.set_page_config(page_title="Gallery of Wings", layout="wide")

# --- 2. 状态管理 ---
if 'page' not in st.session_state:
    st.session_state.page = 'cover'


# --- 3. 辅助函数 ---
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


cover_b64 = get_base64("cover.jpg")

# --- 4. 暴力物理中心锚定 CSS ---
st.markdown(f"""
    <style>
        /* 屏蔽原生组件 */
        header, footer, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{ display: none !important; }}

        .block-container {{ 
            max-width: 100vw !important; 
            padding: 0 !important; 
            margin: 0 !important; 
        }}

        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9)), 
                        url("data:image/jpg;base64,{cover_b64}");
            background-size: cover; background-position: center; background-attachment: fixed;
        }}

        /* 按钮暴力居中 */
        div.stButton {{
            display: flex !important;
            justify-content: center !important;
            width: 100vw !important; 
            position: relative !important;
            left: 50% !important;
            transform: translateX(-50%) !important; 
        }}

        div.stButton > button {{
            background-color: transparent !important;
            color: #D4AF37 !important;
            border: 2px solid #D4AF37 !important;
            padding: 12px 60px !important;
            letter-spacing: 10px !important;
            font-size: 1.4rem !important;
            border-radius: 0px !important;
            margin: 20px auto !important;
        }}

        .full-center {{ width: 100vw; text-align: center; display: block; }}

        /* 优化音乐播放器样式，让它稍微美观一点挂在顶部或底部 */
        .stAudio {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
            width: 300px !important;
            opacity: 0.6;
            transition: 0.3s;
        }}
        .stAudio:hover {{ opacity: 1; }}
    </style>
""", unsafe_allow_html=True)

# --- 5. 全局背景音乐 (放在这里确保每一页都有，且不会因切换页面而停止) ---
if os.path.exists("music.mp3"):
    st.audio("music.mp3", format="audio/mp3", autoplay=True)

# --- 6. 页面逻辑 ---

# 第一页：封面
if st.session_state.page == 'cover':
    st.markdown('<div style="height: 35vh;"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="full-center"><h1 style="font-size: 6rem; color: #D4AF37; letter-spacing: 20px; margin: 0;">羽翼之境</h1><p style="color: #888; letter-spacing: 10px; font-size: 1.5rem; margin-top: 20px;">ECHOES IN THE ETHER</p ></div>',
        unsafe_allow_html=True)
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    if st.button("ENTER GALLERY"):
        st.session_state.page = 'artist'
        st.rerun()

# 第二页：艺术家
elif st.session_state.page == 'artist':
    st.markdown('<div style="height: 10vh;"></div>', unsafe_allow_html=True)
    _, col_mid, _ = st.columns([1, 0.8, 1])
    with col_mid:
        artist_b64 = get_base64("artist.jpg") or get_base64("atist.jpg")
        if artist_b64:
            st.image(f"data:image/jpg;base64,{artist_b64}", use_container_width=True)

    st.markdown(
        '<div class="full-center"><h2 style="color: #D4AF37; font-size: 3rem; letter-spacing: 10px; margin-top: 20px;">艺术家 | 藤壶</h2><p style="color: #DDD; line-height: 2.2; font-size: 1.2rem; max-width: 800px; margin: 20px auto; padding: 0 40px;">藤壶笔下的羽翼，不只是飞翔的工具，更是灵魂的切片。</p ></div>',
        unsafe_allow_html=True)

    if st.button("VIEW THE WINGS"):
        st.session_state.page = 'gallery'
        st.rerun()

# 第三页：画廊
elif st.session_state.page == 'gallery':
    st.markdown(
        '<h1 style="text-align: center; color: #D4AF37; padding: 40px 0 20px 0; font-size: 3rem; letter-spacing: 15px;">羽翼馆藏</h1>',
        unsafe_allow_html=True)

    if st.button("← RETURN"):
        st.session_state.page = 'cover'
        st.rerun()

    img_dir = "images"
    works = ["丽色军舰鸟", "苍鹭", "仓鸮"]
    if os.path.exists(img_dir):
        images = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        cols = st.columns(3)
        for i, img_name in enumerate(images):
            if i < 3:
                with cols[i]:
                    st.image(os.path.join(img_dir, img_name), use_container_width=True)
                    st.markdown(
                        f"<div style='text-align:center; color:#D4AF37; margin-top:15px;'><h3>《{works[i]}》</h3></div>",
                        unsafe_allow_html=True)