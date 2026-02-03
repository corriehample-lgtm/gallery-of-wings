import streamlit as st
import os
import base64

# -----------------------------
# 1. 页面基础设置
# -----------------------------
st.set_page_config(
    page_title="羽翼之光 | Gallery of Wings",
    page_icon="🕊️",
    layout="wide"
)

# -----------------------------
# 2. 自定义 CSS 样式
# -----------------------------
st.markdown("""
<style>
/* 全局背景和字体 */
.stApp {
    background-color: #fcfaf2;
    font-family: "Source Serif Pro", Serif;
}

/* 主标题 */
.main-title {
    font-size: 3.5em;
    color: #2c3e50;
    text-align: center;
    font-weight: bold;
    margin-bottom: 0.2em;
}
.sub-title {
    font-size: 1.5em;
    color: #7f8c8d;
    text-align: center;
    margin-bottom: 2em;
    font-style: italic;
}

/* 图片样式 */
[data-testid="stImage"] {
    border: 6px solid #fff;
    box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    transition: transform 0.3s ease;
}
[data-testid="stImage"]:hover {
     transform: scale(1.02);
}

/* 隐藏默认菜单和页脚 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 3. 音乐播放器函数
# -----------------------------
def get_audio_player(file_path):
    if not os.path.exists(file_path):
        return st.warning("🎵 提示：缺少 music.mp3 文件")
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    html = f"""
        <audio controls autoplay loop style="width: 100%; margin-top: 20px;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <p style="text-align: center; color: gray; font-size: 0.8em;">
        🎼 背景音乐已自动加载，可手动暂停</p >
    """
    st.markdown(html, unsafe_allow_html=True)

# -----------------------------
# 4. 侧边栏：艺术家介绍 + 音乐
# -----------------------------
with st.sidebar:
    st.title("🌿 关于本次展览")
    
    # 艺术家头像
    if os.path.exists("artist.jpg"):
        st.image("artist.jpg", caption="艺术家本尊", use_column_width=True)
    
    st.markdown("""
    ### 👩‍🎨 藤壶
    她以鸟为主题进行创作，关注羽翼、姿态与静默中的力量。
    在画面中，飞翔并非逃离，而是一种内在秩序的展开。
    
    本次展览《羽翼之光》，是对自然、自由与凝视的个人回应。
    """)
    
    st.markdown("---")
    st.header("🎧 背景音乐")
    get_audio_player("music.mp3")

# -----------------------------
# 5. 顶部封面 + 标题
# -----------------------------
st.markdown('<p class="main-title">羽翼之光</p >', unsafe_allow_html=True)
st.markdown('<p class="sub-title">—— 献给爱画鸟的你 · 个人线上作品展 ——</p >', unsafe_allow_html=True)

if os.path.exists("cover.jpg"):
    st.image("cover.jpg", use_column_width=True)
    st.caption("飞翔始于笔尖")

st.divider()

# -----------------------------
# 6. 画廊
# -----------------------------
st.header("🖼️ 展厅漫步")
st.write("请慢慢向下滑动，欣赏每一幅作品。")

img_dir = "images"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)
    st.error("请将画作放入 images 文件夹中！")
else:
    images = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    
    if not images:
        st.info("🎨 画廊正在布置中... (请在 images 文件夹放入图片)")
    else:
        cols = st.columns(2)
        for i, img_name in enumerate(images):
            col = cols[0] if i % 2 == 0 else cols[1]
            with col:
                st.markdown("<br>", unsafe_allow_html=True)
                img_path = os.path.join(img_dir, img_name)
                title = img_name.split('.')[0].replace("_", " ")
                st.image(img_path, use_column_width=True)
                st.markdown(f"<h3 style='text-align: center;'>《{title}》</h3>", unsafe_allow_html=True)
                
                c1, c2, c3 = st.columns([1,2,1])
                with c2:
                    if st.button(f"🌹 送上一朵小红花", key=f"fav_{i}", use_container_width=True):
                        st.balloons()
                        st.toast(f"收到！已传达对《{title}》的喜爱！🎉")
                st.divider()

# -----------------------------
# 7. 页脚
# -----------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align: center; color: gray;">
    Designed with ❤️ for Her. <br> 
    2026 Online Art Exhibition.
</p >
""", unsafe_allow_html=True)
