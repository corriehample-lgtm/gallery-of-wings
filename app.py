<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <title>羽翼之光 · Gallery of Wings</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- 字体 -->
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Noto+Serif+SC:wght@400;600&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg: #f8f6f2;
      --ink: #1f2933;
      --muted: #6b7280;
      --accent: #8b5e3c;
      --card: #ffffff;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: "Noto Serif SC", serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.8;
    }

    img {
      max-width: 100%;
      display: block;
    }

    /* ===== HERO 封面 ===== */
    .hero {
      position: relative;
      height: 100vh;
      background: url("hero.jpg") center/cover no-repeat;
    }

    .hero::after {
      content: "";
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.35);
    }

    .hero-content {
      position: relative;
      z-index: 2;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: #fff;
      text-align: center;
      padding: 0 20px;
    }

    .hero h1 {
      font-family: "Playfair Display", serif;
      font-size: clamp(3rem, 6vw, 4.5rem);
      letter-spacing: 0.08em;
      margin-bottom: 20px;
    }

    .hero p {
      font-size: 1.2rem;
      opacity: 0.9;
    }

    /* ===== 通用容器 ===== */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 120px 24px;
    }

    /* ===== 艺术家介绍 ===== */
    .artist {
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 60px;
      align-items: center;
      background: var(--card);
      padding: 80px;
      border-radius: 4px;
    }

    .artist img {
      border-radius: 50%;
      border: 6px solid #fff;
      box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    .artist h2 {
      font-family: "Playfair Display", serif;
      font-size: 2.2rem;
      margin-bottom: 20px;
    }

    .artist p {
      color: var(--muted);
      font-size: 1.05rem;
    }

    /* ===== 展览说明 ===== */
    .section-title {
      text-align: center;
      margin-bottom: 80px;
    }

    .section-title h2 {
      font-family: "Playfair Display", serif;
      font-size: 2.8rem;
      margin-bottom: 16px;
    }

    .section-title p {
      color: var(--muted);
    }

    /* ===== 画廊 ===== */
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 60px;
    }

    .artwork {
      background: var(--card);
      padding: 20px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      transition: transform 0.3s ease;
    }

    .artwork:hover {
      transform: translateY(-6px);
    }

    .artwork h3 {
      text-align: center;
      font-size: 1rem;
      margin-top: 16px;
      color: var(--ink);
      font-weight: 600;
    }

    /* ===== 页脚 ===== */
    footer {
      text-align: center;
      padding: 60px 20px;
      color: var(--muted);
      font-size: 0.9rem;
    }

    /* ===== 响应式 ===== */
    @media (max-width: 900px) {
      .artist {
        grid-template-columns: 1fr;
        text-align: center;
      }

      .artist img {
        margin: 0 auto;
      }
    }
  </style>
</head>

<body>

  <!-- 首页封面 -->
  <section class="hero">
    <div class="hero-content">
      <h1>羽翼之光</h1>
      <p>Gallery of Wings · 个人线上艺术展</p >
    </div>
  </section>

  <!-- 艺术家介绍 -->
  <section class="container">
    <div class="artist">
      < img src="avatar.jpg" alt="艺术家头像">
      <div>
        <h2>艺术家介绍</h2>
        <p>
          她以鸟为主题进行创作，关注羽翼、姿态与静默中的力量。
          在画面中，飞翔并非逃离，而是一种内在秩序的展开。
          <br><br>
          本次展览《羽翼之光》，是对自然、自由与凝视的个人回应。
        </p >
      </div>
    </div>
  </section>

  <!-- 展厅 -->
  <section class="container">
    <div class="section-title">
      <h2>展厅漫步</h2>
      <p>请放慢脚步，观看每一幅作品</p >
    </div>

    <div class="gallery">
      <!-- 示例作品，按这个格式复制即可 -->
      <div class="artwork">
        < img src="images/bird_01.jpg" alt="作品 1">
        <h3>《无题之一》</h3>
      </div>

      <div class="artwork">
        < img src="images/bird_02.jpg" alt="作品 2">
        <h3>《停栖》</h3>
      </div>

      <div class="artwork">
        < img src="images/bird_03.jpg" alt="作品 3">
        <h3>《风的方向》</h3>
      </div>
    </div>
  </section>

  <!-- 页脚 -->
  <footer>
    © 2026 Gallery of Wings · Designed as a gift
  </footer>

</body>
</html>
