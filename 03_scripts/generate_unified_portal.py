# -*- coding: utf-8 -*-
"""
Grand Unified Portal Builder for Knowledge Lab.
Features:
- Collapsible Mobile & Desktop Navigation Sidebar (Drawer ☰) containing all 17 topics.
- Auto-closes when a topic is selected.
- Clean Top App Bar on mobile with Hamburger toggle button and active section label.
- Complete removal of clunky horizontal scrollers on mobile (desktop-only).
- Syncs to website/index.html, root index.html, and knowledge_graph_viewer.html.
"""

import os
import re
import shutil
import subprocess

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(ROOT_DIR, "website")
INDEX_PATH = os.path.join(WEBSITE_DIR, "index.html")
CODEX_PATH = os.path.join(WEBSITE_DIR, "Grand_Occult_Cosmology_Codex.html")
ROOT_INDEX = os.path.join(ROOT_DIR, "index.html")
ROOT_VIEWER = os.path.join(ROOT_DIR, "knowledge_graph_viewer.html")

def generate():
    # Always rebuild clean base via graph_builder first to avoid any compounding
    print("Rebuilding pristine base via graph_builder...")
    subprocess.run(["python", os.path.join(ROOT_DIR, "03_scripts", "graph_builder.py")], check=True)

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        idx_content = f.read()

    with open(CODEX_PATH, 'r', encoding='utf-8') as f:
        cdx_content = f.read()

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
    cdx_main_adapted = re.sub(r'switchTab\(', 'switchCodexTab(', cdx_main)

    # --- 3. UNIFIED STYLES & SIDEBAR CSS ---
    unified_styles = """
    /* ========================================================
       MASTER UNIFIED PORTAL & COLLAPSIBLE SIDEBAR STYLING
       ======================================================== */
    :root {
        --wing-active-glow: rgba(255, 209, 102, 0.35);
        --wing-codex-accent: #9d4edd;
        --wing-codex-glow: rgba(157, 78, 221, 0.4);
    }

    body {
        margin: 0;
        padding: 0;
        width: 100%;
        max-width: 100vw;
        overflow-x: hidden;
        -webkit-overflow-scrolling: touch;
    }

    * {
        box-sizing: border-box;
    }

    /* TOP HEADER BAR */
    .master-header-container {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: rgba(3, 7, 18, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 209, 102, 0.25);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
    }

    .master-top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 20px;
        gap: 14px;
    }

    /* HAMBURGER TOGGLE BUTTON */
    .sidebar-toggle-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.2), rgba(255, 209, 102, 0.05));
        border: 1px solid rgba(255, 209, 102, 0.4);
        border-radius: 10px;
        padding: 8px 14px;
        color: var(--gold);
        font-family: 'Tajawal', sans-serif;
        font-size: 0.88rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 0 12px rgba(255, 209, 102, 0.15);
        flex-shrink: 0;
    }

    .sidebar-toggle-btn:hover {
        background: var(--gold);
        color: #030712;
        box-shadow: 0 0 18px rgba(255, 209, 102, 0.4);
    }

    .sidebar-toggle-btn i {
        font-size: 1.1rem;
    }

    .master-brand-box {
        display: flex;
        align-items: center;
        gap: 12px;
        flex-grow: 1;
    }

    .master-brand-logo {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.25), rgba(157, 78, 221, 0.3));
        border: 1px solid rgba(255, 209, 102, 0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        box-shadow: 0 0 14px rgba(255, 209, 102, 0.2);
        flex-shrink: 0;
    }

    .master-brand-text h1 {
        margin: 0;
        font-size: 1.15rem;
        font-family: 'Amiri', serif;
        font-weight: 700;
        background: linear-gradient(135deg, #fff 0%, var(--gold) 60%, #c77dff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 0.3px;
        line-height: 1.25;
    }

    .master-brand-text span {
        font-size: 0.74rem;
        color: #94a3b8;
        font-family: 'Tajawal', sans-serif;
        display: block;
    }

    /* COLLAPSIBLE SIDEBAR (DRAWER) */
    .sidebar-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.75);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        z-index: 2999;
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
        transition: opacity 0.3s ease, visibility 0.3s ease;
    }

    .sidebar-backdrop.active {
        opacity: 1;
        visibility: visible;
        pointer-events: auto;
    }

    .portal-sidebar {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        width: 330px;
        max-width: 86vw;
        background: rgba(5, 9, 19, 0.98);
        border-left: 1px solid rgba(255, 209, 102, 0.3);
        box-shadow: -15px 0 50px rgba(0, 0, 0, 0.9);
        z-index: 3000;
        display: flex;
        flex-direction: column;
        transform: translateX(100%);
        transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .portal-sidebar.open {
        transform: translateX(0);
    }

    .sidebar-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        background: rgba(15, 23, 42, 0.7);
    }

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .sidebar-brand-icon {
        font-size: 1.6rem;
    }

    .sidebar-title {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--gold);
    }

    .sidebar-subtitle {
        font-size: 0.7rem;
        color: #94a3b8;
    }

    .sidebar-close-btn {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #fff;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
    }

    .sidebar-close-btn:hover {
        background: rgba(239, 68, 68, 0.25);
        border-color: #ef4444;
        color: #fca5a5;
    }

    .sidebar-search-box {
        padding: 12px 18px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .sidebar-search-input {
        width: 100%;
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 8px;
        padding: 8px 12px;
        color: #fff;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.84rem;
    }

    .sidebar-search-input:focus {
        outline: none;
        border-color: var(--gold);
    }

    .sidebar-scrollable-body {
        flex-grow: 1;
        overflow-y: auto;
        padding: 14px 16px;
        -webkit-overflow-scrolling: touch;
    }

    .sidebar-group {
        margin-bottom: 22px;
    }

    .sidebar-group-title {
        font-family: 'Amiri', serif;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 10px;
        padding-bottom: 4px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .sidebar-items-list {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .sidebar-item {
        display: flex;
        align-items: center;
        gap: 10px;
        width: 100%;
        text-align: right;
        padding: 10px 14px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        color: #cbd5e1;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.84rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .sidebar-item:hover {
        background: rgba(255, 255, 255, 0.06);
        color: #fff;
        border-color: rgba(255, 209, 102, 0.3);
        transform: translateX(-3px);
    }

    .sidebar-item.active {
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.2), rgba(255, 209, 102, 0.05));
        border-color: rgba(255, 209, 102, 0.5);
        color: var(--gold);
        box-shadow: 0 0 14px rgba(255, 209, 102, 0.2);
    }

    .sidebar-item .s-icon {
        font-size: 1.1rem;
        flex-shrink: 0;
    }

    .sidebar-item .s-text {
        flex-grow: 1;
    }

    /* DESKTOP QUICK WINGS & SUBNAV */
    .master-wings-nav {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(15, 23, 42, 0.85);
        padding: 4px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .master-wing-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 15px;
        border-radius: 8px;
        font-size: 0.84rem;
        font-weight: 700;
        cursor: pointer;
        border: 1px solid transparent;
        color: #94a3b8;
        background: transparent;
        font-family: 'Tajawal', sans-serif;
        transition: all 0.2s;
    }

    .master-wing-btn:hover {
        color: #fff;
        background: rgba(255, 255, 255, 0.05);
    }

    .master-wing-btn.active-atlas {
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.2), rgba(255, 209, 102, 0.05));
        color: var(--gold);
        border-color: rgba(255, 209, 102, 0.5);
    }

    .master-wing-btn.active-codex {
        background: linear-gradient(135deg, rgba(157, 78, 221, 0.25), rgba(157, 78, 221, 0.05));
        color: #d8b4fe;
        border-color: rgba(157, 78, 221, 0.5);
    }

    .master-wing-btn.active-index {
        background: linear-gradient(135deg, rgba(6, 214, 160, 0.2), rgba(6, 214, 160, 0.05));
        color: #6ee7b7;
        border-color: rgba(6, 214, 160, 0.5);
    }

    .master-subnav-bar {
        display: flex;
        align-items: center;
        padding: 6px 20px;
        overflow-x: auto;
        white-space: nowrap;
        gap: 8px;
        scrollbar-width: thin;
        background: rgba(2, 6, 23, 0.7);
    }

    /* RESPONSIVE TOGGLES: HIDE DESKTOP CLUTTER ON MOBILE */
    @media (max-width: 768px) {
        .desktop-only {
            display: none !important;
        }

        .master-top-bar {
            padding: 8px 12px !important;
        }

        .master-brand-text h1 {
            font-size: 1rem !important;
        }

        .master-brand-text span {
            font-size: 0.68rem !important;
        }

        .portal-sidebar {
            width: 88vw !important;
        }
    }
    """

    # --- 4. NEW MASTER HEADER & SIDEBAR HTML ---
    new_header_html = """
    <!-- COLLAPSIBLE NAVIGATION SIDEBAR & BACKDROP -->
    <div class="sidebar-backdrop" id="sidebar-backdrop" onclick="toggleSidebar(false)"></div>
    <aside class="portal-sidebar" id="portal-sidebar">
        <div class="sidebar-header">
            <div class="sidebar-brand">
                <span class="sidebar-brand-icon">🏛️</span>
                <div>
                    <div class="sidebar-title">أبواب المنظومة (17)</div>
                    <div class="sidebar-subtitle">فهرس النواميس والمعرفة الكونية</div>
                </div>
            </div>
            <button class="sidebar-close-btn" onclick="toggleSidebar(false)" title="إغلاق القائمة">✕</button>
        </div>

        <div class="sidebar-search-box">
            <input type="text" id="sidebar-search-input" class="sidebar-search-input" placeholder="🔍 ابحث في الأبواب الـ 17..." oninput="filterSidebarItems(this.value)">
        </div>

        <div class="sidebar-scrollable-body">
            <!-- GROUP 1: ATLAS -->
            <div class="sidebar-group">
                <div class="sidebar-group-title" style="color:var(--gold);">
                    <i class="fa-solid fa-atom"></i> أطلس الكوزمولوجيا القرآنية (8 أروقة)
                </div>
                <div class="sidebar-items-list">
                    <button class="sidebar-item active" data-wing="atlas" data-tab="graph" onclick="navTo('atlas', 'graph')">
                        <span class="s-icon">🕸️</span> <span class="s-text">الشبكة الكونية الكبرى</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="spheres" onclick="navTo('atlas', 'spheres')">
                        <span class="s-icon">🪐</span> <span class="s-text">سلم الأفلاك والأنبياء</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="chakras" onclick="navTo('atlas', 'chakras')">
                        <span class="s-icon">🧘</span> <span class="s-text">مجسم التشاكرات والأنبياء</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="zodiac" onclick="navTo('atlas', 'zodiac')">
                        <span class="s-icon">♈</span> <span class="s-text">دائرة البروج الاثني عشر</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="timeline" onclick="navTo('atlas', 'timeline')">
                        <span class="s-icon">⏳</span> <span class="s-text">تعاقب العصور (2,160 سنة)</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="matrix" onclick="navTo('atlas', 'matrix')">
                        <span class="s-icon">🏛️</span> <span class="s-text">المصفوفة المعمارية الشاملة</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="manuscripts" onclick="navTo('atlas', 'manuscripts')">
                        <span class="s-icon">📜</span> <span class="s-text">أمهات المخطوطات والكتب</span>
                    </button>
                    <button class="sidebar-item" data-wing="atlas" data-tab="critique" onclick="navTo('atlas', 'critique')">
                        <span class="s-icon">⚖️</span> <span class="s-text">ميزان القرآن والتناقضات</span>
                    </button>
                </div>
            </div>

            <!-- GROUP 2: CODEX -->
            <div class="sidebar-group">
                <div class="sidebar-group-title" style="color:#d8b4fe;">
                    <i class="fa-solid fa-scroll"></i> سفر النواميس الباطنية (9 أبواب)
                </div>
                <div class="sidebar-items-list">
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-kings" onclick="navTo('codex', 'tab-kings')">
                        <span class="s-icon">👑</span> <span class="s-text">ملوك الأفلاك والأيام السبعة</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-zodiac-angels" onclick="navTo('codex', 'tab-zodiac-angels')">
                        <span class="s-icon">🌟</span> <span class="s-text">ملائكة الأبراج والـ 36 وجهاً</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-hours" onclick="navTo('codex', 'tab-hours')">
                        <span class="s-icon">⏳</span> <span class="s-text">ساعات الأيام الـ 24 الكلدانية</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-mansions" onclick="navTo('codex', 'tab-mansions')">
                        <span class="s-icon">🌙</span> <span class="s-text">منازل القمر الـ 28</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-letters-magic" onclick="navTo('codex', 'tab-letters-magic')">
                        <span class="s-icon">🪶</span> <span class="s-text">طبائع الحروف والأسحار الـ 4</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-bodies" onclick="navTo('codex', 'tab-bodies')">
                        <span class="s-icon">🧬</span> <span class="s-text">الأجساد السبعة وميكانيكا الاختراق</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-numbers" onclick="navTo('codex', 'tab-numbers')">
                        <span class="s-icon">🔢</span> <span class="s-text">شفرة الأرقام والوفق الغزالي 3×3</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-physics" onclick="navTo('codex', 'tab-physics')">
                        <span class="s-icon">🔊</span> <span class="s-text">فيزياء الذبذبات والمولد الصوتي</span>
                    </button>
                    <button class="sidebar-item" data-wing="codex" data-tab="tab-criterion" onclick="navTo('codex', 'tab-criterion')">
                        <span class="s-icon">⚖️</span> <span class="s-text">ميزان الوحي الإلهي المطلق</span>
                    </button>
                </div>
            </div>

            <!-- GROUP 3: MASTER INDEX -->
            <div class="sidebar-group">
                <button class="sidebar-item" data-wing="index" data-tab="index" onclick="navTo('index', '')" style="background:rgba(6,214,160,0.15); border-color:rgba(6,214,160,0.3); color:#6ee7b7;">
                    <span class="s-icon">📋</span> <span class="s-text"><strong>فهرس المنظومة الشامل (17 باباً)</strong></span>
                </button>
            </div>
        </div>
    </aside>

    <!-- MASTER UNIFIED PORTAL HEADER (SINGLE CLEAN BAR) -->
    <header class="master-header-container">
        <div class="master-top-bar">
            <!-- HAMBURGER BUTTON -->
            <button class="sidebar-toggle-btn" onclick="toggleSidebar(true)" title="فتح قائمة الأبواب">
                <i class="fa-solid fa-bars"></i>
                <span>الأبواب (17)</span>
            </button>

            <!-- BRAND TITLE -->
            <div class="master-brand-box">
                <div class="master-brand-logo">🌌</div>
                <div class="master-brand-text">
                    <h1>بوابة المعرفة والنواميس الكونية</h1>
                    <span id="current-active-section-label">الرواق النشط: الشبكة الكونية الكبرى</span>
                </div>
            </div>

            <!-- DESKTOP QUICK WINGS -->
            <div class="master-wings-nav">
                <button id="master-btn-atlas" class="master-wing-btn active-atlas" onclick="switchMasterWing('atlas')">
                    <i class="fa-solid fa-atom"></i>
                    <span>أطلس الكوزمولوجيا</span>
                </button>
                <button id="master-btn-codex" class="master-wing-btn" onclick="switchMasterWing('codex')">
                    <i class="fa-solid fa-scroll"></i>
                    <span>سفر النواميس</span>
                </button>
                <button id="master-btn-index" class="master-wing-btn" onclick="switchMasterWing('index')">
                    <i class="fa-solid fa-layer-group"></i>
                    <span>فهرس الـ 17</span>
                </button>
            </div>
        </div>
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

        <div class="modules-wing-group">
            <div class="wing-group-header">
                <span style="font-size:1.8rem;">🌌</span>
                <div>
                    <h3 style="color:var(--gold);">الجناح الأول: أطلس الكوزمولوجيا وشبكة المعرفة القرآنية</h3>
                    <span style="color:#94a3b8; font-size:0.85rem;">8 أروقة تفاعلية كبرى ترتكز على محور الوحي والنبوات وتفكيك المخطوطات</span>
                </div>
            </div>
            <div class="modules-grid">
                <div class="module-card" onclick="navTo('atlas', 'graph')">
                    <div class="module-icon-box">🕸️</div>
                    <div class="module-title">الشبكة الكونية الكبرى</div>
                    <div class="module-desc">خريطة تفاعلية كاملة وأطلس مفاهيم نظري يضم مئات العقد الفكرية، الروابط، والمفاهيم الكوزمولوجية مع محرك بحث وتصفية فورية.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'spheres')">
                    <div class="module-icon-box">🪐</div>
                    <div class="module-title">سلم الأفلاك والأنبياء</div>
                    <div class="module-desc">مطابقة بصرية تفاعلية بين السماوات السبع، الأفلاك، والأنبياء (من القمر لآدم إلى زحل لإبراهيم) مع شواهد الإسراء والمعراج.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'chakras')">
                    <div class="module-icon-box">🧘</div>
                    <div class="module-title">مجسم التشاكرات والأنبياء</div>
                    <div class="module-desc">تشريح مراكز الطاقة الحيوية السبعة في الجسد البشري، الغدد الصماء المقابلة، ومقارنتها بسلم الأنبياء ونقد التحريف الفيدانتي.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'zodiac')">
                    <div class="module-icon-box">♈</div>
                    <div class="module-title">دائرة البروج الاثني عشر</div>
                    <div class="module-desc">قبة فلكية دائرية تعرض البروج، منازلها، أربابها، طبائعها الأربعة، وموقع البروج في القرآن الكريم كآيات كوزمولوجية.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'timeline')">
                    <div class="module-icon-box">⏳</div>
                    <div class="module-title">تعاقب العصور الكبرى</div>
                    <div class="module-desc">خط زمني بانورامي لحركة المبادرة المحورية (2,160 سنة لكل عصر فلكي) وتطابقها مع نزول الشرائع الكبرى من الثور إلى الحوت والدلو.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'matrix')">
                    <div class="module-icon-box">🏛️</div>
                    <div class="module-title">المصفوفة المعمارية الشاملة</div>
                    <div class="module-desc">جدول مقارن ضخم يربط كل فلك بصفته القرآنية، نبيه، معدنه، شاكرته، لونه، والحكمة الباطنية المنسوبة له.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'manuscripts')">
                    <div class="module-icon-box">📜</div>
                    <div class="module-title">أمهات المخطوطات والكتب</div>
                    <div class="module-desc">مستودع بحثي موثق لـ 16 من أمهات المخطوطات العالمية (شمس المعارف، غاية الحكيم، كتاب هرمس، السر المكتوم، متون الكابالا).</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card" onclick="navTo('atlas', 'critique')">
                    <div class="module-icon-box">⚖️</div>
                    <div class="module-title">ميزان القرآن والتناقضات</div>
                    <div class="module-desc">تحليل نقدي صارم يفكك دعاوى تأليه الكواكب وعبادة الروحانيات، ويرد الأمور إلى توحيد الخالق المطلق ومنهج القرآن.</div>
                    <div class="module-action-btn"><span>دخول الرواق</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>
            </div>
        </div>

        <div class="modules-wing-group">
            <div class="wing-group-header">
                <span style="font-size:1.8rem;">🔮</span>
                <div>
                    <h3 style="color:#d8b4fe;">الجناح الثاني: سفر النواميس الباطنية والأفلاك والأرقام</h3>
                    <span style="color:#94a3b8; font-size:0.85rem;">9 أبواب عميقة تكشف القوانين الباطنية، ملوك الأيام، ملائكة الأبراج، الساعات، والأوفاق فيزياء الترددات</span>
                </div>
            </div>
            <div class="modules-grid">
                <div class="module-card codex-type" onclick="navTo('codex', 'tab-kings')">
                    <div class="module-icon-box">👑</div>
                    <div class="module-title">ملوك الأفلاك والأيام السبعة</div>
                    <div class="module-desc">المصفوفة المقارنة الموحدة لملوك الأيام والملائكة العلوية والأرضية عبر البابلية، الهرمسية، الكابالا، والكتب التنجيمية الإسلامية.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-zodiac-angels')">
                    <div class="module-icon-box">🌟</div>
                    <div class="module-title">ملائكة الأبراج والـ 36 وجهاً</div>
                    <div class="module-desc">أطلس ملائكة الأبراج الاثني عشر والوجوه الـ 36 (Decans) مع حكامها الكلدانيين، أسمائها العبرية، واليونانية من بيكاتريكس.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-hours')">
                    <div class="module-icon-box">⏳</div>
                    <div class="module-title">ساعات الأيام الـ 24 الكلدانية</div>
                    <div class="module-desc">حاسبة فلكية تفاعلية تحسب أرباب الساعات الـ 24 لكل يوم من أيام الأسبوع الـ 7 نهاراً وليلاً وفق الترتيب الكلداني الفلكي.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-mansions')">
                    <div class="module-icon-box">🌙</div>
                    <div class="module-title">منازل القمر الـ 28</div>
                    <div class="module-desc">الدائرة القمرية الكاملة من الشرطين إلى الرشاء، درجاتها الفلكية (12° 51' 26")، طبائعها، وخواصها الأثيرية في كتب الأقدمين.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-letters-magic')">
                    <div class="module-icon-box">🪶</div>
                    <div class="module-title">طبائع الحروف والأسحار الأربعة</div>
                    <div class="module-desc">تقسيم الحروف الـ 28 على العناصر الأربعة (ناري، هوائي، مائي، ترابي) وتصنيف الأسحار وتطابقها الطاقي مع الأمزجة البشرية.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-bodies')">
                    <div class="module-icon-box">🧬</div>
                    <div class="module-title">الأجساد السبعة وميكانيكا الاختراق</div>
                    <div class="module-desc">تشريح طبقات الوعي البشري (المادي، الأثيري، النجمي، العقلي، السببي، الروحي، الإلهي) وكيف يخترق التردد السلبي الهالة والتحصين.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-numbers')">
                    <div class="module-icon-box">🔢</div>
                    <div class="module-title">شفرة الأرقام والوفق الغزالي 3×3</div>
                    <div class="module-desc">أسرار المربعات السحرية المتوازنة ذات الثابت 15، مراتب الحساب الأثيرية، وتفسير كيف تعمل الهندسة الرقمية كموجّه موجي للذبذبة.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-physics')">
                    <div class="module-icon-box">🔊</div>
                    <div class="module-title">فيزياء الذبذبات والمولد الصوتي</div>
                    <div class="module-desc">مختبر تفاعلي حي بمولد صوتي حقيقي (Web Audio API) يولد ترددات الكواكب الكونية مع شاشة راسم إشارة (Canvas) لتحليل الموجات.</div>
                    <div class="module-action-btn"><span>دخول الباب</span> <i class="fa-solid fa-arrow-left"></i></div>
                </div>

                <div class="module-card codex-type" onclick="navTo('codex', 'tab-criterion')">
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

    # SIDEBAR CONTROLLER JAVASCRIPT
    sidebar_controller_js = """
    // ========================================================
    // SIDEBAR & UNIFIED ROUTER CONTROLLER
    // ========================================================
    const TAB_LABELS = {
        'graph': 'الشبكة الكونية الكبرى',
        'spheres': 'سلم الأفلاك والأنبياء',
        'chakras': 'مجسم التشاكرات والأنبياء',
        'zodiac': 'دائرة البروج الاثني عشر',
        'timeline': 'تعاقب العصور (2,160 سنة)',
        'matrix': 'المصفوفة المعمارية الشاملة',
        'manuscripts': 'أمهات المخطوطات والكتب',
        'critique': 'ميزان القرآن والتناقضات',
        'tab-kings': 'ملوك الأفلاك والأيام السبعة',
        'tab-zodiac-angels': 'ملائكة الأبراج والـ 36 وجهاً',
        'tab-hours': 'ساعات الأيام الـ 24 الكلدانية',
        'tab-mansions': 'منازل القمر الـ 28',
        'tab-letters-magic': 'طبائع الحروف والأسحار الأربعة',
        'tab-bodies': 'الأجساد السبعة وميكانيكا الاختراق',
        'tab-numbers': 'شفرة الأرقام والوفق الغزالي 3×3',
        'tab-physics': 'فيزياء الذبذبات والمولد الصوتي',
        'tab-criterion': 'ميزان الوحي الإلهي المطلق',
        'index': 'فهرس المنظومة الشامل (17 باباً)'
    };

    function toggleSidebar(open) {
        const sidebar = document.getElementById('portal-sidebar');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (!sidebar || !backdrop) return;

        if (open) {
            sidebar.classList.add('open');
            backdrop.classList.add('active');
            document.body.style.overflow = 'hidden'; // lock background scroll while sidebar is open
        } else {
            sidebar.classList.remove('open');
            backdrop.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    function navTo(wing, tabId) {
        // Close sidebar immediately
        toggleSidebar(false);

        // Update active label in header
        const labelEl = document.getElementById('current-active-section-label');
        if (labelEl) {
            const key = tabId || wing;
            labelEl.innerText = 'الباب النشط: ' + (TAB_LABELS[key] || 'أبواب المنظومة');
        }

        // Highlight active sidebar item
        document.querySelectorAll('.sidebar-item').forEach(btn => {
            const bWing = btn.getAttribute('data-wing');
            const bTab = btn.getAttribute('data-tab');
            if (bWing === wing && (bTab === tabId || (!tabId && bWing === 'index'))) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Switch wing & tab
        switchMasterWing(wing);
        if (wing === 'atlas' && tabId) {
            switchTab(tabId);
        } else if (wing === 'codex' && tabId) {
            switchCodexTab(tabId);
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function filterSidebarItems(query) {
        const q = (query || '').trim().toLowerCase();
        document.querySelectorAll('.sidebar-item').forEach(btn => {
            const text = btn.innerText.toLowerCase();
            if (!q || text.includes(q)) {
                btn.style.display = 'flex';
            } else {
                btn.style.display = 'none';
            }
        });
    }

    let currentMasterWing = 'atlas';

    function switchMasterWing(wing) {
        currentMasterWing = wing;
        const btnAtlas = document.getElementById('master-btn-atlas');
        const btnCodex = document.getElementById('master-btn-codex');
        const btnIndex = document.getElementById('master-btn-index');

                
        const wingAtlas = document.getElementById('wing-atlas');
        const wingCodex = document.getElementById('wing-codex');
        const wingIndex = document.getElementById('tab-master-index');

        if (btnAtlas) btnAtlas.className = 'master-wing-btn';
        if (btnCodex) btnCodex.className = 'master-wing-btn';
        if (btnIndex) btnIndex.className = 'master-wing-btn';

        if (wingAtlas) wingAtlas.classList.add('hidden-wing');
        if (wingCodex) wingCodex.classList.add('hidden-wing');
        if (wingIndex) wingIndex.classList.add('hidden-wing');

        if (wing === 'atlas') {
            if (btnAtlas) btnAtlas.classList.add('active-atlas');
            if (wingAtlas) wingAtlas.classList.remove('hidden-wing');
            window.location.hash = '#wing-atlas';
        } else if (wing === 'codex') {
            if (btnCodex) btnCodex.classList.add('active-codex');
            if (wingCodex) wingCodex.classList.remove('hidden-wing');
            window.location.hash = '#wing-codex';
        } else if (wing === 'index') {
            if (btnIndex) btnIndex.classList.add('active-index');
            if (wingIndex) wingIndex.classList.remove('hidden-wing');
            window.location.hash = '#wing-index';
        }
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
                navTo('codex', hash);
            } else if (hash === 'wing-codex') {
                navTo('codex', 'tab-kings');
            } else if (hash === 'wing-index') {
                navTo('index', '');
            }
        }
    });
    """

    body_end_pos = idx_content.rfind('</body>')
    if body_end_pos != -1:
        full_extra_script = f"""
        <script>
        {cdx_script_adapted}
        {sidebar_controller_js}
        </script>
        """
        idx_content = idx_content[:body_end_pos] + full_extra_script + idx_content[body_end_pos:]

    # Write output to website/index.html
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(idx_content)

    # Sync to root index.html and knowledge_graph_viewer.html
    shutil.copyfile(INDEX_PATH, ROOT_INDEX)
    shutil.copyfile(INDEX_PATH, ROOT_VIEWER)

    print("Grand Unified Master Portal successfully generated with Navigation Sidebar!")
    print(f"- website/index.html ({len(idx_content)} chars)")
    print(f"- index.html (root)")
    print(f"- knowledge_graph_viewer.html (root)")

if __name__ == "__main__":
    generate()
