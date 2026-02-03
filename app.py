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
/* 全局 */
.stApp { background-color: #fcfaf2; font-family: "Source Serif Pro", Serif; }
h1, h2, h3, p { margin: 0; }

/* 封面 */
.hero {
    position: relative;
    width: 100%;
    height: 80vh;
    background: url('cover.jpg') center/cover no-repeat;
}
.hero::after {
    content: "";
    position: absolute;
    inset:0;
    background: rgba(0,0,0,0.4);
}
.hero-text {
    position: relative;
    z-index:2;
    height:100%;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    color:#fff;
    text-align:center;
}
.hero-text h1 { font-size: clamp(3rem,6vw,4.5rem); font-family:"Playfair Display", serif; }
.hero-text p { font-size:1.5rem; opacity:0.9; }

/* 艺术家介绍 */
.artist {
    display:grid;
    grid-template-columns: 250px 1fr;
    gap: 50px;
    align-items: center;
    padding: 60px 20px;
    background:#fff;
    border-radius:6px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
    margin: 60px auto;
    max-width: 1000px;
}
.artist img { border-radius:50%; width:250px; box-shadow:0 8px 25px rgba(0,0,0,0.15); }
.artist h2 { font-family:"Playfair Display", serif; font-size:2rem; margin-bottom:15px; }
.artist p { color:#555; font-size:1.05rem; line-height:1.6; }

/* 画廊 */
.gallery {
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(300px,1fr));
    gap: 30px;
    padding: 0 20px 60px 20px;
    max-width:1200px;
    margin:0 auto;
}
.artwork {
    position:relative;
    overflow:hidden;
    border-radius:6px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    background:#fff;
}
.artwork:hover { transform: translateY(-6px); box-shadow:0 15px 40px rgba(0,0,0,0.12); }
.artwork img { width:100%; display:block; }
.artwork h3 {
    position:absolute;
    bottom:0;
    width:100%;
    text-align:center;
    background:rgba(0,0,0,0.45);
    color:#fff;
    padding:10px 0;
    margin:0;
    font-weight:500;
}

/* 音乐播放器 */
.audio-player { text-align:center; margin:40px 0; }

/* 页脚 */
footer { text-align:center; color:#888; padding:50px 20px; font-size:0.9rem; }

/* 响应式 */
@media(max-width:900px) {
    .artist { grid-template-columns: 1fr; text-align:center; }
    .artist img { margin:0 auto; }
}
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
        <div class="audio-player">
            <audio controls autoplay loop style="width:90%;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <p style="color:#888; font-size:0.85rem;">🎼 背景音乐已自动加载，可手动暂停</p >
        </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# -----------------------------
# 4. 侧边栏
# -----------------------------
with st.sidebar:
    st.title("🌿 关于本次展览")
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
# 5. 首页封面
# -----------------------------
st.markdown('<div class="hero"><div class="hero-text"><h1>羽翼之光</h1><p>Gallery of Wings · 个人线上作品展</p ></div></div>', unsafe_allow_html=True)

# -----------------------------
# 6. 艺术家介绍块
# -----------------------------
st.markdown('<div class="artist">'
            f'< img src="artist.jpg">'
            '<div>'
            '<h2>艺术家介绍</h2>'
            '<p>她以鸟为主题进行创作，关注羽翼、姿态与静默中的力量。<br>'
            '在画面中，飞翔并非逃离，而是一种内在秩序的展开。<br>'
            '本次展览《羽翼之光》，是对自然、自由与凝视的个人回应。</p >'
            '</div></div>', unsafe_allow_html=True)

st.divider()

# -----------------------------
# 7. 画廊
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
        for img_name in images:
            img_path = os.path.join(img_dir, img_name)
            title = img_name.split('.')[0].replace("_"," ")
            st.markdown(f"""
                <div class="artwork">
                    < img src="{img_path}">
                    <h3>《{title}》</h3>
                </div>
            """, unsafe_allow_html=True)

# -----------------------------
# 8. 页脚
# -----------------------------
st.markdown('<footer>© 2026 Gallery of Wings · Designed with ❤️ for Her</footer>', unsafe_allow_html=True)
