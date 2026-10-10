# -*- coding: utf-8 -*-
"""
Grand Unified Portal Builder for Knowledge Lab (Idempotent & Clean).
Merges:
1. Quranic Cosmic Atlas & Vis.js Knowledge Graph (8 Modules) from graph_builder output
2. Grand Occult Cosmology & Esoteric Codex (9 Modules)
3. Master Wing Switcher & Full 17-Module Directory Grid
4. Unified PIN Authentication ('1234')
5. Syncs to website/index.html, root index.html, and knowledge_graph_viewer.html
"""

import os
import re
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(ROOT_DIR, "website")
INDEX_PATH = os.path.join(WEBSITE_DIR, "index.html")
CODEX_PATH = os.path.join(WEBSITE_DIR, "Grand_Occult_Cosmology_Codex.html")
ROOT_INDEX = os.path.join(ROOT_DIR, "index.html")
ROOT_VIEWER = os.path.join(ROOT_DIR, "knowledge_graph_viewer.html")

def generate():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        idx_content = f.read()

    with open(CODEX_PATH, 'r', encoding='utf-8') as f:
        cdx_content = f.read()

    # If idx_content already has master-header-container, strip out previous injections
    # Or start from a clean base
    # Check if previously injected
    if 'class="master-header-container"' in idx_content:
        print("Detected previously merged index.html. Rebuilding clean base via graph_builder first...")
        import subprocess
        subprocess.run(["python", os.path.join(ROOT_DIR, "03_scripts", "graph_builder.py")], check=True)
        with open(INDEX_PATH, 'r', encoding='utf-8') as f:
            idx_content = f.read()

    # --- 1. EXTRACT CODEX STYLES ---
    cdx_style = re.search(r'<style>(.*?)</style>', cdx_content, re.DOTALL).group(1)
    cdx_style_cleaned = re.sub(r'body\s*\{[^}]*\}', '', cdx_style)
    cdx_style_cleaned = re.sub(r'header\s*\{[^}]*\}', '', cdx_style_cleaned)

    # --- 2. EXTRACT CODEX MAIN CONTENT & SCRIPTS ---
    cdx_main = re.search(r'<main[^>]*>(.*?)</main>', cdx_content, re.DOTALL).group(1)
    cdx_script = re.search(r'<script>(.*?)</script>', cdx_content, re.DOTALL).group(1)

    # Adapt codex script functions
    cdx_script_adapted = cdx_script.replace("function switchTab(tabId)", "function switchCodexTab(tabId)")
    cdx_script_adapted = cdx_script_adapted.replace("handleAuth", "handleCodexLegacyAuth")
    # Change onclicks in codex main
    cdx_main_adapted = re.sub(r'switchTab\(', 'switchCodexTab(', cdx_main)

    # --- 3. UNIFIED STYLES ---
    unified_styles = """
    /* MASTER UNIFIED PORTAL STYLING & WING SWITCHER */
    :root {
        --wing-active-glow: rgba(255, 209, 102, 0.35);
        --wing-codex-accent: #9d4edd;
        --wing-codex-glow: rgba(157, 78, 221, 0.4);
    }

    .master-header-container {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: rgba(3, 7, 18, 0.94);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border-bottom: 1px solid rgba(255, 209, 102, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }

    .master-top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 24px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        gap: 16px;
        flex-wrap: wrap;
    }

    .master-brand-box {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .master-brand-logo {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.2), rgba(157, 78, 221, 0.3));
        border: 1px solid rgba(255, 209, 102, 0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        box-shadow: 0 0 16px rgba(255, 209, 102, 0.2);
    }

    .master-brand-text h1 {
        margin: 0;
        font-size: 1.25rem;
        font-family: 'Amiri', serif;
        font-weight: 700;
        background: linear-gradient(135deg, #fff 0%, var(--gold) 50%, #c77dff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 0.5px;
    }

    .master-brand-text span {
        font-size: 0.75rem;
        color: #94a3b8;
        font-family: 'Tajawal', sans-serif;
        display: block;
    }

    .master-wings-nav {
        display: flex;
        align-items: center;
        gap: 10px;
        background: rgba(15, 23, 42, 0.85);
        padding: 5px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .master-wing-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 9px 18px;
        border-radius: 10px;
        font-size: 0.88rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid transparent;
        color: #94a3b8;
        background: transparent;
        font-family: 'Tajawal', sans-serif;
    }

    .master-wing-btn:hover {
        color: #fff;
        background: rgba(255, 255, 255, 0.05);
    }

    .master-wing-btn.active-atlas {
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.2), rgba(255, 209, 102, 0.05));
        color: var(--gold);
        border-color: rgba(255, 209, 102, 0.5);
        box-shadow: 0 0 16px var(--wing-active-glow);
    }

    .master-wing-btn.active-codex {
        background: linear-gradient(135deg, rgba(157, 78, 221, 0.25), rgba(157, 78, 221, 0.05));
        color: #d8b4fe;
        border-color: rgba(157, 78, 221, 0.5);
        box-shadow: 0 0 16px var(--wing-codex-glow);
    }

    .master-wing-btn.active-index {
        background: linear-gradient(135deg, rgba(6, 214, 160, 0.2), rgba(6, 214, 160, 0.05));
        color: #6ee7b7;
        border-color: rgba(6, 214, 160, 0.5);
        box-shadow: 0 0 16px rgba(6, 214, 160, 0.3);
    }

    .wing-pill-count {
        font-size: 0.7rem;
        padding: 2px 7px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.1);
        font-weight: 600;
    }

    .master-subnav-bar {
        display: flex;
        align-items: center;
        padding: 8px 24px;
        overflow-x: auto;
        white-space: nowrap;
        gap: 8px;
        scrollbar-width: thin;
        scrollbar-color: rgba(255, 209, 102, 0.3) transparent;
        background: rgba(2, 6, 23, 0.6);
    }

    .master-subnav-bar::-webkit-scrollbar {
        height: 4px;
    }
    .master-subnav-bar::-webkit-scrollbar-thumb {
        background: rgba(255, 209, 102, 0.3);
        border-radius: 4px;
    }

    .codex-tab-btn {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 7px 15px;
        border-radius: 8px;
        font-size: 0.84rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: rgba(15, 23, 42, 0.6);
        color: #94a3b8;
        font-family: 'Tajawal', sans-serif;
    }

    .codex-tab-btn:hover {
        color: #fff;
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(157, 78, 221, 0.3);
    }

    .codex-tab-btn.active {
        background: linear-gradient(135deg, rgba(157, 78, 221, 0.25), rgba(157, 78, 221, 0.1));
        color: #e9d5ff;
        border-color: #c084fc;
        box-shadow: 0 0 14px rgba(192, 132, 252, 0.3);
    }

    #tab-master-index {
        padding: 30px 24px;
        max-width: 1400px;
        margin: 0 auto;
    }

    .index-hero-banner {
        text-align: center;
        padding: 40px 20px;
        margin-bottom: 36px;
        border-radius: 20px;
        background: radial-gradient(circle at 50% 20%, rgba(157, 78, 221, 0.15), rgba(3, 7, 18, 0.95));
        border: 1px solid rgba(255, 209, 102, 0.2);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }

    .index-hero-banner h2 {
        font-family: 'Amiri', serif;
        font-size: 2.2rem;
        margin-bottom: 12px;
        background: linear-gradient(135deg, #ffd166, #fff, #c77dff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .index-hero-banner p {
        color: #94a3b8;
        font-size: 1.05rem;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.8;
    }

    .modules-wing-group {
        margin-bottom: 40px;
    }

    .wing-group-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid rgba(255, 255, 255, 0.08);
    }

    .wing-group-header h3 {
        font-size: 1.4rem;
        font-family: 'Amiri', serif;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .modules-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 20px;
    }

    .module-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 20px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
    }

    .module-card:hover {
        transform: translateY(-4px);
        border-color: rgba(255, 209, 102, 0.4);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(255, 209, 102, 0.15);
    }

    .module-card.codex-type:hover {
        border-color: rgba(192, 132, 252, 0.5);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(192, 132, 252, 0.2);
    }

    .module-icon-box {
        font-size: 2rem;
        margin-bottom: 12px;
    }

    .module-title {
        font-size: 1.15rem;
        font-family: 'Amiri', serif;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 8px;
    }

    .module-desc {
        font-size: 0.88rem;
        color: #94a3b8;
        line-height: 1.6;
        margin-bottom: 16px;
        flex-grow: 1;
    }

    .module-action-btn {
        display: inline-flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 0.82rem;
        font-weight: 700;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #e2e8f0;
        transition: all 0.2s;
    }

    .module-card:hover .module-action-btn {
        background: var(--gold);
        color: #020617;
        border-color: var(--gold);
    }

    .module-card.codex-type:hover .module-action-btn {
        background: #c084fc;
        color: #020617;
        border-color: #c084fc;
    }

    .wing-container {
        display: block;
        min-height: calc(100vh - 120px);
    }

    .wing-container.hidden-wing {
        display: none !important;
    }

    /* ========================================================
       ULTRA-RESPONSIVE MOBILE ENGINE (PHONES & TABLETS)
       ======================================================== */
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        position: relative;
        -webkit-tap-highlight-color: transparent;
    }

    * {
        box-sizing: border-box;
    }

    /* Horizontal scroll containers touch momentum */
    .master-subnav-bar, .pills-container, .synth-buttons, .table-container, .timeline-horizontal-scroll {
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }
    .master-subnav-bar::-webkit-scrollbar, 
    .pills-container::-webkit-scrollbar, 
    .synth-buttons::-webkit-scrollbar {
        display: none;
    }

    /* Mobile screens <= 768px */
    @media (max-width: 768px) {
        .master-top-bar {
            padding: 8px 12px !important;
            flex-direction: column !important;
            align-items: stretch !important;
            gap: 10px !important;
        }

        .master-brand-box {
            justify-content: center !important;
            text-align: center !important;
            gap: 10px !important;
        }

        .master-brand-logo {
            width: 36px !important;
            height: 36px !important;
            font-size: 1.25rem !important;
            border-radius: 10px !important;
        }

        .master-brand-text h1 {
            font-size: 1.05rem !important;
            line-height: 1.3 !important;
        }

        .master-brand-text span {
            font-size: 0.68rem !important;
        }

        /* Segmented Controller Wings on Mobile */
        .master-wings-nav {
            display: grid !important;
            grid-template-columns: 1fr 1fr 1fr !important;
            padding: 4px !important;
            gap: 4px !important;
            width: 100% !important;
        }

        .master-wing-btn {
            padding: 8px 4px !important;
            font-size: 0.72rem !important;
            justify-content: center !important;
            text-align: center !important;
            flex-direction: column !important;
            gap: 3px !important;
            border-radius: 8px !important;
        }

        .master-wing-btn i {
            font-size: 0.95rem !important;
        }

        .master-wing-btn span {
            font-size: 0.72rem !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            max-width: 85px !important;
        }

        .wing-pill-count {
            display: none !important;
        }

        /* Subnav Bars */
        .master-subnav-bar {
            padding: 6px 10px !important;
            gap: 6px !important;
        }

        .nav-btn, .codex-tab-btn {
            padding: 6px 12px !important;
            font-size: 0.78rem !important;
            border-radius: 8px !important;
            white-space: nowrap !important;
            flex-shrink: 0 !important;
        }

        /* Main Workspace & Hero */
        main, .wing-container {
            padding: 12px 8px !important;
        }

        .hero-banner, .index-hero-banner {
            padding: 20px 14px !important;
            margin-bottom: 20px !important;
            border-radius: 14px !important;
        }

        .index-hero-banner h2, .hero-banner h2 {
            font-size: 1.35rem !important;
            line-height: 1.4 !important;
        }

        .index-hero-banner p, .hero-banner p {
            font-size: 0.82rem !important;
            line-height: 1.6 !important;
        }

        .modules-grid {
            grid-template-columns: 1fr !important;
            gap: 14px !important;
        }

        .module-card {
            padding: 16px !important;
        }

        /* Force Graph Container on Mobile */
        #graph-fullscreen-wrapper {
            height: calc(100vh - 190px) !important;
            min-height: 460px !important;
        }

        #cosmic-network-canvas {
            height: 100% !important;
            min-height: 440px !important;
        }

        .graph-top-filters {
            padding: 8px 10px !important;
            flex-direction: column !important;
            gap: 8px !important;
        }

        .pills-container {
            width: 100% !important;
        }

        .search-box {
            width: 100% !important;
            font-size: 0.82rem !important;
            padding: 8px 12px !important;
        }

        /* Reader Drawer as Bottom Sheet on Mobile */
        #reader-drawer {
            width: 100% !important;
            max-width: 100% !important;
            right: 0 !important;
            left: 0 !important;
            border-left: none !important;
            border-top: 2px solid var(--gold) !important;
            top: auto !important;
            bottom: 0 !important;
            height: 75vh !important;
            border-radius: 20px 20px 0 0 !important;
            box-shadow: 0 -12px 40px rgba(0,0,0,0.85) !important;
            z-index: 2000 !important;
        }

        /* 3D Visualizers / Grids */
        .chakras-visualizer-container, .spheres-view-container {
            grid-template-columns: 1fr !important;
            gap: 16px !important;
        }

        .chakra-3d-box, .spheres-ladder-box {
            min-height: 340px !important;
        }

        /* Wafq Live Calculator */
        .magic-grid-3x3 {
            grid-template-columns: repeat(3, 1fr) !important;
            gap: 6px !important;
            max-width: 290px !important;
            margin: 0 auto !important;
        }

        .magic-cell {
            padding: 8px 4px !important;
            min-height: 56px !important;
        }

        .magic-cell span {
            font-size: 1rem !important;
        }

        .cell-letter {
            font-size: 0.64rem !important;
        }

        #wafq-input {
            width: 100% !important;
        }

        /* Responsive Tables */
        .table-container {
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch !important;
            border-radius: 12px !important;
            margin-bottom: 18px !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
        }

        .planetary-table {
            min-width: 620px !important;
            font-size: 0.76rem !important;
        }

        .planetary-table th, .planetary-table td {
            padding: 7px 9px !important;
        }

        /* Synth Bar & Canvas Wave */
        .audio-synth-bar {
            flex-direction: column !important;
            align-items: stretch !important;
            padding: 10px 12px !important;
            gap: 8px !important;
        }

        .synth-buttons {
            overflow-x: auto !important;
            padding-bottom: 4px !important;
            flex-wrap: nowrap !important;
        }

        .synth-btn {
            padding: 6px 12px !important;
            font-size: 0.74rem !important;
            flex-shrink: 0 !important;
        }

        .wave-canvas-wrapper canvas {
            height: 180px !important;
        }

        .canvas-controls {
            flex-direction: column !important;
            align-items: stretch !important;
            gap: 8px !important;
        }

        .canvas-controls div {
            flex-wrap: wrap !important;
        }

        .wave-mode-btn {
            padding: 5px 9px !important;
            font-size: 0.72rem !important;
        }

        /* Password Gate on Mobile */
        .auth-card {
            padding: 24px 16px !important;
            max-width: 92vw !important;
        }

        .auth-title {
            font-size: 1.25rem !important;
        }

        .auth-subtitle {
            font-size: 0.82rem !important;
        }

        .auth-password-input {
            font-size: 1.1rem !important;
            padding: 10px !important;
        }
    }

    /* Extra Small screens <= 480px */
    @media (max-width: 480px) {
        .master-brand-text h1 {
            font-size: 0.95rem !important;
        }
        .master-wing-btn span {
            font-size: 0.66rem !important;
            max-width: 70px !important;
        }
        .magic-grid-3x3 {
            max-width: 260px !important;
            gap: 4px !important;
        }
        .magic-cell {
            min-height: 50px !important;
            padding: 4px 2px !important;
        }
    }
    
    """

    # --- 4. NEW MASTER HEADER HTML ---
    new_header_html = """
    <!-- MASTER UNIFIED PORTAL HEADER -->
    <header class="master-header-container">
        <div class="master-top-bar">
            <div class="master-brand-box">
                <div class="master-brand-logo">🌌</div>
                <div class="master-brand-text">
                    <h1>بوابة المعرفة والنواميس الكونية الموحدة</h1>
                    <span>Quranic Cosmic Atlas & Grand Esoteric Cosmology Portal • 17 باباً معرفياً موحداً</span>
                </div>
            </div>

            <!-- MASTER WING SELECTOR -->
            <div class="master-wings-nav">
                <button id="master-btn-atlas" class="master-wing-btn active-atlas" onclick="switchMasterWing('atlas')">
                    <i class="fa-solid fa-atom"></i>
                    <span>أطلس الكوزمولوجيا وشبكة المعرفة</span>
                    <span class="wing-pill-count">8 أروقة</span>
                </button>
                <button id="master-btn-codex" class="master-wing-btn" onclick="switchMasterWing('codex')">
                    <i class="fa-solid fa-scroll"></i>
                    <span>سفر النواميس الباطنية والأفلاك</span>
                    <span class="wing-pill-count">9 أبواب</span>
                </button>
                <button id="master-btn-index" class="master-wing-btn" onclick="switchMasterWing('index')">
                    <i class="fa-solid fa-layer-group"></i>
                    <span>فهرس الأبواب الـ 17</span>
                </button>
            </div>
        </div>

        <!-- ATLAS SUB-NAV (8 TABS) -->
        <nav id="subnav-atlas" class="master-subnav-bar">
            <button class="nav-btn active" onclick="switchTab('graph')">الشبكة الكونية الكبرى 🕸️</button>
            <button class="nav-btn" onclick="switchTab('spheres')">سلم الأفلاك والأنبياء 🪐</button>
            <button class="nav-btn" style="border: 1px solid #00f0ff; color: #00f0ff;" onclick="switchTab('chakras')">مجسم التشاكرات والأنبياء 🧘</button>
            <button class="nav-btn" onclick="switchTab('zodiac')">دائرة البروج الاثني عشر ♈</button>
            <button class="nav-btn" onclick="switchTab('timeline')">تعاقب العصور (2,160 سنة) ⏳</button>
            <button class="nav-btn" onclick="switchTab('matrix')">المصفوفة المعمارية الشاملة 🏛️</button>
            <button class="nav-btn" onclick="switchTab('manuscripts')">أمهات المخطوطات والكتب 📜</button>
            <button class="nav-btn" style="border: 1px solid #ff3366; color: #ff3366;" onclick="switchTab('critique')">ميزان القرآن والتناقضات (للمرشد) ⚖️</button>
        </nav>

        <!-- CODEX SUB-NAV (9 TABS) -->
        <nav id="subnav-codex" class="master-subnav-bar" style="display:none;">
            <button class="codex-tab-btn active" onclick="switchCodexTab('tab-kings')"><i class="fa-solid fa-crown"></i> ملوك الأفلاك والأيام</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-zodiac-angels')"><i class="fa-solid fa-star-and-crescent"></i> ملائكة الأبراج والـ 36 وجهاً</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-hours')"><i class="fa-solid fa-clock"></i> ساعات الأيام الـ 24 الكلدانية</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-mansions')"><i class="fa-solid fa-moon"></i> منازل القمر الـ 28</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-letters-magic')"><i class="fa-solid fa-fire-burner"></i> طبائع الحروف والأسحار الأربعة</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-bodies')"><i class="fa-solid fa-person-rays"></i> الأجساد السبعة وميكانيكا الاختراق</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-numbers')"><i class="fa-solid fa-cubes-stacked"></i> شفرة الأرقام والوفق الغزالي 3×3</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-physics')"><i class="fa-solid fa-wave-square"></i> فيزياء الذبذبات والمولد الصوتي</button>
            <button class="codex-tab-btn" onclick="switchCodexTab('tab-criterion')"><i class="fa-solid fa-scale-balanced"></i> ميزان الوحي الإلهي المطلق</button>
        </nav>
    </header>
    """

    # --- 5. MASTER INDEX SECTION HTML ---
    master_index_html = """
    <!-- TAB: MASTER INDEX (17 MODULES DIRECTORY) -->
    <section id="tab-master-index" class="wing-container hidden-wing">
        <div class="index-hero-banner">
            <h2>فهرس المنظومة الشامل — 17 باباً معرفياً موحداً</h2>
            <p>
                مرجع كوني وباطني فائق الدقة يربط كوزمولوجيا الوحي القرآني بشبكة النبوات والمخطوطات، 
                ويكشف الهندسة الأثيرية للأفلاك، ساعات الأيام، منازل القمر، طبائع الحروف، شفرة الأرقام، وفيزياء الترددات.
            </p>
        </div>

        <!-- WING 1 MODULES -->
        <div class="modules-wing-group">
            <div class="wing-group-header">
                <span style="font-size:1.8rem;">🌌</span>
                <div>
                    <h3 style="color:var(--gold);">الجناح الأول: أطلس الكوزمولوجيا وشبكة المعرفة القرآنية</h3>
                    <span style="color:#94a3b8; font-size:0.85rem;">8 أروقة تفاعلية كبرى ترتكز على محور الوحي والنبوات وتفكيك المخطوطات</span>
                </div>
            </div>
            <div class="modules-grid">
                <div class="module-card" onclick="jumpToModule('atlas', 'graph')">
                    <div class="module-icon-box">🕸️</div>
                    <div class="module-title">الشبكة الكونية الكبرى</div>
                    <div class="module-desc">خريطة تفاعلية كاملة (Force Graph) تضم مئات العقد الفكرية، الروابط، والمفاهيم الكوزمولوجية مع محرك بحث وتصفية فورية.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'spheres')">
                    <div class="module-icon-box">🪐</div>
                    <div class="module-title">سلم الأفلاك والأنبياء</div>
                    <div class="module-desc">مطابقة بصرية تفاعلية بين السماوات السبع، الأفلاك، والأنبياء (من القمر لآدم إلى زحل لإبراهيم) مع شواهد الإسراء والمعراج.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'chakras')">
                    <div class="module-icon-box">🧘</div>
                    <div class="module-title">مجسم التشاكرات والأنبياء</div>
                    <div class="module-desc">تشريح مراكز الطاقة الحيوية السبعة في الجسد البشري، الغدد الصماء المقابلة، ومقارنتها بسلم الأنبياء ونقد التحريف الفيدانتي.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'zodiac')">
                    <div class="module-icon-box">♈</div>
                    <div class="module-title">دائرة البروج الاثني عشر</div>
                    <div class="module-desc">قبة فلكية دائرية تعرض البروج، منازلها، أربابها، طبائعها الأربعة، وموقع البروج في القرآن الكريم كآيات كوزمولوجية.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'timeline')">
                    <div class="module-icon-box">⏳</div>
                    <div class="module-title">تعاقب العصور الكبرى</div>
                    <div class="module-desc">خط زمني بانورامي لحركة المبادرة المحورية (2,160 سنة لكل عصر فلكي) وتطابقها مع نزول الشرائع الكبرى من الثور إلى الحوت والدلو.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'matrix')">
                    <div class="module-icon-box">🏛️</div>
                    <div class="module-title">المصفوفة المعمارية الشاملة</div>
                    <div class="module-desc">جدول مقارن ضخم يربط كل فلك بصفته القرآنية، نبيه، معدنه، شاكرته، لونه، والحكمة الباطنية المنسوبة له.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'manuscripts')">
                    <div class="module-icon-box">📜</div>
                    <div class="module-title">أمهات المخطوطات والكتب</div>
                    <div class="module-desc">مستودع بحثي موثق لـ 16 من أمهات المخطوطات العالمية (شمس المعارف، غاية الحكيم، كتاب هرمس، السر المكتوم، متون الكابالا).</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="jumpToModule('atlas', 'critique')">
                    <div class="module-icon-box">⚖️</div>
                    <div class="module-title">ميزان القرآن والتناقضات</div>
                    <div class="module-desc">تحليل نقدي صارم يفكك دعاوى تأليه الكواكب وعبادة الروحانيات، ويرد الأمور إلى توحيد الخالق المطلق ومنهج القرآن.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>
            </div>
        </div>

        <!-- WING 2 MODULES -->
        <div class="modules-wing-group">
            <div class="wing-group-header">
                <span style="font-size:1.8rem;">🔮</span>
                <div>
                    <h3 style="color:#d8b4fe;">الجناح الثاني: سفر النواميس الباطنية والأفلاك والأرقام</h3>
                    <span style="color:#94a3b8; font-size:0.85rem;">9 أبواب عميقة تكشف القوانين الباطنية، ملوك الأيام، ملائكة الأبراج، الساعات، والأوفاق فيزياء الترددات</span>
                </div>
            </div>
            <div class="modules-grid">
                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-kings')">
                    <div class="module-icon-box">👑</div>
                    <div class="module-title">ملوك الأفلاك والأيام السبعة</div>
                    <div class="module-desc">المصفوفة المقارنة الموحدة لملوك الأيام والملائكة العلوية والأرضية عبر البابلية، الهرمسية، الكابالا، والكتب التنجيمية الإسلامية.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-zodiac-angels')">
                    <div class="module-icon-box">🌟</div>
                    <div class="module-title">ملائكة الأبراج والـ 36 وجهاً</div>
                    <div class="module-desc">أطلس ملائكة الأبراج الاثني عشر والوجوه الـ 36 (Decans) مع حكامها الكلدانيين، أسمائها العبرية، واليونانية من بيكاتريكس.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-hours')">
                    <div class="module-icon-box">⏳</div>
                    <div class="module-title">ساعات الأيام الـ 24 الكلدانية</div>
                    <div class="module-desc">حاسبة فلكية تفاعلية تحسب أرباب الساعات الـ 24 لكل يوم من أيام الأسبوع الـ 7 نهاراً وليلاً وفق الترتيب الكلداني الفلكي.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-mansions')">
                    <div class="module-icon-box">🌙</div>
                    <div class="module-title">منازل القمر الـ 28</div>
                    <div class="module-desc">الدائرة القمرية الكاملة من الشرطين إلى الرشاء، درجاتها الفلكية (12° 51' 26")، طبائعها، وخواصها الأثيرية في كتب الأقدمين.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-letters-magic')">
                    <div class="module-icon-box">🪶</div>
                    <div class="module-title">طبائع الحروف والأسحار الأربعة</div>
                    <div class="module-desc">تقسيم الحروف الـ 28 على العناصر الأربعة (ناري، هوائي، مائي، ترابي) وتصنيف الأسحار وتطابقها الطاقي مع الأمزجة البشرية.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-bodies')">
                    <div class="module-icon-box">🧬</div>
                    <div class="module-title">الأجساد السبعة وميكانيكا الاختراق</div>
                    <div class="module-desc">تشريح طبقات الوعي البشري (المادي، الأثيري، النجمي، العقلي، السببي، الروحي، الإلهي) وكيف يخترق التردد السلبي الهالة والتحصين.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-numbers')">
                    <div class="module-icon-box">🔢</div>
                    <div class="module-title">شفرة الأرقام والوفق الغزالي 3×3</div>
                    <div class="module-desc">أسرار المربعات السحرية المتوازنة ذات الثابت 15، مراتب الحساب الأثيرية، وتفسير كيف تعمل الهندسة الرقمية كموجّه موجي للذبذبة.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-physics')">
                    <div class="module-icon-box">🔊</div>
                    <div class="module-title">فيزياء الذبذبات والمولد الصوتي</div>
                    <div class="module-desc">مختبر تفاعلي حي بمولد صوتي حقيقي (Web Audio API) يولد ترددات الكواكب الكونية مع شاشة راسم إشارة (Canvas) لتحليل الموجات.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="jumpToModule('codex', 'tab-criterion')">
                    <div class="module-icon-box">⚖️</div>
                    <div class="module-title">ميزان الوحي الإلهي المطلق</div>
                    <div class="module-desc">المسطرة الإيمانية الصارمة: الفرق بين دراسة سنن الكون الفلكية وبين الشرك والعبودية لغير الله، وحماية النفس بوحي الخالق.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>
            </div>
        </div>
    </section>
    """

    # --- 6. ASSEMBLE HTML ---
    if "font-awesome" not in idx_content:
        idx_content = idx_content.replace('</head>', '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>')

    style_end_pos = idx_content.rfind('</style>')
    if style_end_pos != -1:
        combined_css = "\n" + cdx_style_cleaned + "\n" + unified_styles + "\n"
        idx_content = idx_content[:style_end_pos] + combined_css + idx_content[style_end_pos:]

    header_regex = r'<header>.*?</header>'
    idx_content = re.sub(header_regex, new_header_html, idx_content, flags=re.DOTALL)

    main_start = idx_content.find('<main>')
    main_end = idx_content.find('</main>')
    if main_start != -1 and main_end != -1:
        atlas_body = idx_content[main_start:main_end+7]
        wrapped_wings = f"""
        <div id="wing-atlas" class="wing-container">
            {atlas_body}
        </div>

        <div id="wing-codex" class="wing-container hidden-wing">
            <main>
                {cdx_main_adapted}
            </main>
        </div>

        {master_index_html}
        """
        idx_content = idx_content[:main_start] + wrapped_wings + idx_content[main_end+7:]

    master_switcher_js = """
    // ========================================================
    // MASTER UNIFIED PORTAL CONTROLLER (WINGS & TABS)
    // ========================================================
    let currentMasterWing = 'atlas';

    function switchMasterWing(wing) {
        currentMasterWing = wing;
        const btnAtlas = document.getElementById('master-btn-atlas');
        const btnCodex = document.getElementById('master-btn-codex');
        const btnIndex = document.getElementById('master-btn-index');

        const subnavAtlas = document.getElementById('subnav-atlas');
        const subnavCodex = document.getElementById('subnav-codex');

        const wingAtlas = document.getElementById('wing-atlas');
        const wingCodex = document.getElementById('wing-codex');
        const wingIndex = document.getElementById('tab-master-index');

        btnAtlas.className = 'master-wing-btn';
        btnCodex.className = 'master-wing-btn';
        btnIndex.className = 'master-wing-btn';

        wingAtlas.classList.add('hidden-wing');
        wingCodex.classList.add('hidden-wing');
        wingIndex.classList.add('hidden-wing');

        if (wing === 'atlas') {
            btnAtlas.classList.add('active-atlas');
            subnavAtlas.style.display = 'flex';
            subnavCodex.style.display = 'none';
            wingAtlas.classList.remove('hidden-wing');
            window.location.hash = '#wing-atlas';
        } else if (wing === 'codex') {
            btnCodex.classList.add('active-codex');
            subnavAtlas.style.display = 'none';
            subnavCodex.style.display = 'flex';
            wingCodex.classList.remove('hidden-wing');
            window.location.hash = '#wing-codex';
        } else if (wing === 'index') {
            btnIndex.classList.add('active-index');
            subnavAtlas.style.display = 'none';
            subnavCodex.style.display = 'none';
            wingIndex.classList.remove('hidden-wing');
            window.location.hash = '#wing-index';
        }
    }

    function jumpToModule(wing, targetTabId) {
        switchMasterWing(wing);
        if (wing === 'atlas') {
            switchTab(targetTabId);
        } else if (wing === 'codex') {
            switchCodexTab(targetTabId);
        }
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function switchCodexTab(tabId) {
        document.querySelectorAll('#wing-codex .content-section').forEach(sec => {
            sec.classList.remove('active');
        });
        document.querySelectorAll('#subnav-codex .codex-tab-btn').forEach(btn => {
            btn.classList.remove('active');
        });

        const target = document.getElementById(tabId);
        if (target) {
            target.classList.add('active');
        }

        const activeBtn = Array.from(document.querySelectorAll('#subnav-codex .codex-tab-btn'))
            .find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes(tabId));
        if (activeBtn) {
            activeBtn.classList.add('active');
        }

        window.location.hash = '#' + tabId;
    }

    window.addEventListener('load', () => {
        const hash = window.location.hash.replace('#', '');
        if (hash) {
            if (hash.startsWith('tab-') && (hash.includes('kings') || hash.includes('zodiac') || hash.includes('hours') || hash.includes('mansions') || hash.includes('letters') || hash.includes('bodies') || hash.includes('numbers') || hash.includes('physics') || hash.includes('criterion'))) {
                jumpToModule('codex', hash);
            } else if (hash === 'wing-codex') {
                switchMasterWing('codex');
            } else if (hash === 'wing-index') {
                switchMasterWing('index');
            }
        }
    });
    """

    body_end_pos = idx_content.rfind('</body>')
    if body_end_pos != -1:
        full_extra_script = f"""
        <script>
        {cdx_script_adapted}
        {master_switcher_js}
        </script>
        """
        idx_content = idx_content[:body_end_pos] + full_extra_script + idx_content[body_end_pos:]

    # Write output to website/index.html
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(idx_content)

    # Sync to root index.html and knowledge_graph_viewer.html
    shutil.copyfile(INDEX_PATH, ROOT_INDEX)
    shutil.copyfile(INDEX_PATH, ROOT_VIEWER)

    print(f"Grand Unified Master Portal successfully generated and synchronized!")
    print(f"- website/index.html ({len(idx_content)} chars)")
    print(f"- index.html (root)")
    print(f"- knowledge_graph_viewer.html (root)")

if __name__ == "__main__":
    generate()
