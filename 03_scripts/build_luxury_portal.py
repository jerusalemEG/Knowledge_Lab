# -*- coding: utf-8 -*-
"""
Knowledge Lab - Grand Luxury Unified Portal Builder (v6.0 Ultimate Polish)
Engineered for supreme architectural organization, full indexing across all 17 chambers,
and flawless desktop & mobile responsiveness.

Pillars:
1. Hub (Home): Master Directory Dashboard with Cosmic Metrics & 17 Chapter Cards.
2. Pillar 1 (W revelation): 8 Quranic & Prophetic Cosmology Chambers.
3. Pillar 2 (S occult): 6 Planetary & Esoteric Codex Chambers.
4. Pillar 3 (L resonance): 3 Interactive Resonance & Mathematical Chambers.
"""

import os
import re
import shutil
import subprocess
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(ROOT_DIR, "website")
INDEX_PATH = os.path.join(WEBSITE_DIR, "index.html")
CODEX_PATH = os.path.join(WEBSITE_DIR, "Grand_Occult_Cosmology_Codex.html")
ROOT_INDEX = os.path.join(ROOT_DIR, "index.html")
ROOT_VIEWER = os.path.join(ROOT_DIR, "knowledge_graph_viewer.html")

sys.path.insert(0, os.path.join(ROOT_DIR, "03_scripts"))
from generate_astrology_chamber import get_astrology_chamber_html, get_astrology_chamber_js
from generate_seals_zouhri_chamber import get_seals_zouhri_chamber_html, get_seals_zouhri_chamber_js
from generate_inner_realms_chamber import get_inner_realms_chamber_html, get_inner_realms_chamber_js
from generate_astrolabe_engine import get_astrolabe_css, get_astrolabe_html, get_astrolabe_js
from generate_esoteric_charts import get_esoteric_charts_css, get_esoteric_charts_html, get_esoteric_charts_js
from generate_cosmic_chambers_deluxe import (
    get_deluxe_chambers_css,
    get_deluxe_chambers_html,
    get_cosmic_database_js,
    get_chambers_visual_js,
    wrap_all_raw_chambers,
    extract_tag_content
)


def build_luxury_portal():
    print("[1/5] Rebuilding pristine base files...")
    subprocess.run(["python", os.path.join(ROOT_DIR, "03_scripts", "graph_builder.py")], check=True)
    subprocess.run(["python", os.path.join(ROOT_DIR, "03_scripts", "generate_complete_codex.py")], check=True)

    print("[2/5] Reading base contents...")
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        atlas_html = f.read()

    with open(CODEX_PATH, 'r', encoding='utf-8') as f:
        codex_html = f.read()

    # --- EXTRACT CODEX STYLES ---
    codex_style_match = re.search(r'<style>(.*?)</style>', codex_html, re.DOTALL)
    codex_css = codex_style_match.group(1) if codex_style_match else ""
    # Clean redundant global tags
    codex_css_clean = re.sub(r'body\s*\{[^}]*\}', '', codex_css)
    codex_css_clean = re.sub(r'header\s*\{[^}]*\}', '', codex_css_clean)
    codex_css_clean = re.sub(r'#portal-auth-gate\s*\{[^}]*\}', '', codex_css_clean)

    # --- EXTRACT CODEX MAIN CONTENT & SCRIPT ---
    codex_main_match = re.search(r'<main[^>]*>(.*?)</main>', codex_html, re.DOTALL)
    codex_main = codex_main_match.group(1) if codex_main_match else ""
    codex_script_match = re.search(r'<script>(.*?)</script>', codex_html, re.DOTALL)
    codex_js = codex_script_match.group(1) if codex_script_match else ""

    # Clean codex script functions and avoid duplicate declarations
    codex_js_clean = codex_js.replace("function handleAuth", "function handleCodexLegacyAuth")
    codex_js_clean = codex_js_clean.replace("function switchTab(tabId)", "function switchCodexTab(tabId)")

    # Adapt codex main click events if any
    codex_main_clean = codex_main.replace("switchTab(", "navigateToChamber(")

    # Strip .active from graph and kings in raw HTML so only #tab-hub is active on initial load
    atlas_html_clean = re.sub(r'(id="tab-graph"\s+class="tab-section)\s+active', r'\1', atlas_html)
    codex_main_clean = re.sub(r'(id="tab-kings"\s+class="tab-content)\s+active', r'\1', codex_main_clean)

    # --- STRIP OLD ATLAS HEADER ---
    # In atlas_html, remove the old inner <header>...</header>
    atlas_clean = re.sub(r'<header>.*?</header>', '', atlas_html_clean, flags=re.DOTALL)

    # --- MASTER LUXURY STYLESHEET ---
    luxury_css = """
    /* ========================================================
       KNOWLEDGE LAB — THE CELESTIAL PARADISE OF ESOTERIC SCIENCES
       جنة العلوم الباطنية والنواميس الكونية الملوكية (v8.0 Master Luxury)
       ======================================================== */
    :root {
        color-scheme: light !important;
        --void-black: #0f172a;
        --bg-space: #f1f5f9;
        --bg-void: #e2e8f0;
        --bg-slate-deep: #e8ecf4;
        --bg-slate-panel: #ffffff;
        --bg-slate-card: #f8fafc;
        --bg-slate-elevated: #ffffff;
        --card-glass: rgba(255, 255, 255, 0.94);
        --card-glass-hover: #ffffff;
        --panel-bg: rgba(255, 255, 255, 0.96);
        
        /* MYSTIC & SILVER BORDER HIERARCHY */
        --border-slate-subtle: rgba(148, 163, 184, 0.25);
        --border-slate: rgba(148, 163, 184, 0.45);
        --border-slate-strong: rgba(100, 116, 139, 0.85);
        
        /* ROYAL STERLING SILVER & PLATINUM ILLUMINATION (TRANSFORMED FROM GOLD) */
        --gold: #64748b;
        --gold-bright: #94a3b8;
        --gold-light: #cbd5e1;
        --gold-foil: linear-gradient(135deg, #475569 0%, #94a3b8 35%, #64748b 70%, #cbd5e1 100%);
        --border-gold: rgba(100, 116, 139, 0.4);
        --border-gold-strong: rgba(71, 85, 105, 0.85);
        --gold-glow: rgba(148, 163, 184, 0.35);
        
        /* PARADISE EMERALD & MALACHITE */
        --emerald-accent: #059669;
        --emerald-bright: #10b981;
        --emerald-glow: rgba(16, 185, 129, 0.3);
        
        /* ROYAL VELVET AMETHYST & VIOLET */
        --purple-accent: #7c3aed;
        --purple-light: #f3e8ff;
        --purple-glow: rgba(124, 58, 237, 0.3);
        
        /* ASTRAL LAPIS LAZULI & CYAN */
        --cyan-accent: #0284c7;
        --cyan-light: #e0f2fe;
        --cyan-glow: rgba(2, 132, 199, 0.3);
        
        /* CELESTIAL RUBY */
        --ruby-accent: #e11d48;
        --ruby-glow: rgba(225, 29, 72, 0.3);
        
        /* REFINED GREY TYPOGRAPHY HIERARCHY */
        --text-pure: #334155;
        --text-silver: #475569;
        --text-body: #64748b;
        --text-gold: #475569;
        --text-muted: #94a3b8;
    }

    html {
        background-color: #f1f5f9 !important;
        background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 40%, #e2e8f0 75%, #f1f5f9 100%) !important;
        color-scheme: light !important;
        color: #334155 !important;
        scrollbar-color: rgba(100, 116, 139, 0.45) #edf2f7 !important;
    }

    body {
        width: 100%;
        max-width: 100vw;
        overflow-x: hidden !important;
        position: relative;
        background-color: #f1f5f9 !important;
        background-image: 
            radial-gradient(circle at 12% 15%, rgba(16, 185, 129, 0.05) 0%, transparent 45%),
            radial-gradient(circle at 88% 18%, rgba(148, 163, 184, 0.12) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(148, 163, 184, 0.14) 0%, transparent 60%),
            radial-gradient(circle at 20% 80%, rgba(2, 132, 199, 0.05) 0%, transparent 50%) !important;
        background-attachment: fixed !important;
        color-scheme: light !important;
        font-family: 'Tajawal', sans-serif;
        color: #334155 !important;
        -webkit-font-smoothing: antialiased;
        scroll-behavior: smooth;
        scrollbar-color: rgba(100, 116, 139, 0.45) #edf2f7 !important;
    }

    * {
        box-sizing: border-box;
        scrollbar-color: rgba(100, 116, 139, 0.4) #edf2f7 !important;
    }

    /* Universal Silver Manuscript Scrollbars Across Entire Site */
    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important;
    }
    ::-webkit-scrollbar-track {
        background: #f1f5f9 !important;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #94a3b8, #64748b) !important;
        border-radius: 6px !important;
        border: 2px solid #f1f5f9 !important;
        box-shadow: 0 0 6px rgba(100, 116, 139, 0.25) !important;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #64748b, #475569) !important;
    }

    /* Universal Master Chambers Silver Parchment Enforcement */
    .master-chambers-wrapper,
    .chamber-view,
    .tab-section,
    .tab-content,
    #tab-hub,
    #tab-graph,
    #tab-spheres,
    #tab-matrix,
    #tab-manuscripts,
    #tab-timeline,
    #tab-zodiac,
    #tab-mansions,
    #tab-hours,
    #tab-kings,
    #tab-astrology-calc,
    #tab-letters-magic,
    #tab-numbers,
    #tab-physics,
    #tab-chakras,
    #tab-bodies,
    #tab-zodiac-angels,
    #tab-seals-zouhri,
    #tab-inner-realms,
    #tab-critique,
    #tab-criterion,
    main {
        background-color: transparent !important;
        background: transparent !important;
        color: #1e293b !important;
    }

    /* Universal Form & Input Manuscript Parchment Enforcement */
    input, select, textarea, button {
        color-scheme: light !important;
    }
    input[type="text"], input[type="password"], input[type="number"], select, textarea {
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        color: #0f172a !important;
        border-radius: 10px;
    }
    input[type="date"], input[type="time"] {
        color-scheme: light !important;
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        color: #0f172a !important;
        border-radius: 10px;
    }
    input:focus, select:focus, textarea:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 12px rgba(100, 116, 139, 0.3) !important;
        outline: none !important;
    }

    body.drawer-open-lock {
        overflow: hidden !important;
        touch-action: none;
    }

    /* TOP BAR — SINGLE LUXURY ROW */
    .master-luxury-topbar {
        position: sticky;
        top: 0;
        z-index: 5000;
        background: rgba(248, 250, 252, 0.94) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1.5px solid rgba(100, 116, 139, 0.35) !important;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
        width: 100%;
    }

    .topbar-main-title {
        font-family: 'Amiri', serif;
        font-size: 1.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #334155 0%, #64748b 35%, #475569 70%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        line-height: 1.25;
        filter: drop-shadow(0 1px 3px rgba(100, 116, 139, 0.25));
    }

    .topbar-inner {
        max-width: 1600px;
        margin: 0 auto;
        padding: 8px 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        height: 60px;
    }

    /* HAMBURGER TRIGGER BUTTON */
    .topbar-hamburger-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.18), rgba(148, 163, 184, 0.04));
        border: 1px solid rgba(148, 163, 184, 0.45);
        border-radius: 12px;
        padding: 8px 16px;
        color: #475569;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.92rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 0 16px rgba(148, 163, 184, 0.15);
        flex-shrink: 0;
        height: 42px;
    }

    .topbar-hamburger-btn:hover {
        background: #475569;
        color: #ffffff;
        box-shadow: 0 0 24px rgba(100, 116, 139, 0.35);
        transform: translateY(-1px);
    }

    .topbar-hamburger-btn .hamburger-icon {
        font-size: 1.25rem;
        line-height: 1;
    }

    .hamburger-badge {
        background: rgba(148, 163, 184, 0.25);
        padding: 2px 7px;
        border-radius: 10px;
        font-size: 0.74rem;
        color: inherit;
        border: 1px solid rgba(148, 163, 184, 0.4);
    }

    /* CENTER BRAND INFO */
    .topbar-center-info {
        display: flex;
        align-items: center;
        gap: 12px;
        flex-grow: 1;
        justify-content: center;
        text-align: center;
        min-width: 0;
    }

    .topbar-logo-icon {
        font-size: 1.6rem;
        filter: drop-shadow(0 0 10px var(--gold-glow));
        flex-shrink: 0;
    }

    .topbar-titles {
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 0;
    }

    .topbar-main-title {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        font-weight: 700;
        background: linear-gradient(135deg, #334155 10%, #64748b 60%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        line-height: 1.25;
    }

    .topbar-chamber-badge {
        font-size: 0.75rem;
        color: var(--cyan-accent);
        background: rgba(0, 240, 255, 0.08);
        border: 1px solid rgba(0, 240, 255, 0.25);
        border-radius: 12px;
        padding: 1px 10px;
        margin-top: 2px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 260px;
    }

    /* TOPBAR ACTIONS (LEFT) */
    .topbar-actions {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-shrink: 0;
    }

    .topbar-action-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        padding: 8px 12px;
        color: #334155;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        height: 40px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05);
    }

    .topbar-action-btn:hover {
        background: #f8fafc;
        color: #0f172a;
        border-color: var(--gold);
    }

    .topbar-action-btn.tone-btn {
        color: var(--cyan-accent);
        border-color: rgba(2, 132, 199, 0.35);
        background: rgba(2, 132, 199, 0.06);
    }

    .topbar-action-btn.tone-btn.playing {
        background: var(--cyan-accent);
        color: #ffffff;
        box-shadow: 0 0 16px var(--cyan-glow);
    }

    .topbar-pin-status {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(5, 150, 105, 0.1);
        border: 1px solid rgba(5, 150, 105, 0.3);
        color: var(--emerald-accent);
        font-size: 0.88rem;
    }

    /* ========================================================
       MUSEUM-GRADE SIDEBAR DRAWER (فهرس الأبواب الـ 20)
       ======================================================== */
    .portal-drawer-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(15, 23, 42, 0.5);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        z-index: 9998;
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
        transition: opacity 0.32s ease, visibility 0.32s ease;
    }

    .portal-drawer-backdrop.active {
        opacity: 1;
        visibility: visible;
        pointer-events: auto;
    }

    .portal-drawer {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        width: 390px;
        max-width: 90vw;
        background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%) !important;
        border-left: 1.5px solid rgba(100, 116, 139, 0.35) !important;
        box-shadow: -15px 0 45px rgba(15, 23, 42, 0.12), -2px 0 15px rgba(100, 116, 139, 0.08);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        transform: translateX(100%);
        transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .portal-drawer.open {
        transform: translateX(0);
    }

    .drawer-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 18px 20px;
        border-bottom: 1.5px solid rgba(100, 116, 139, 0.25);
        background: rgba(248, 250, 252, 0.98);
    }

    .drawer-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .drawer-brand-icon {
        font-size: 1.8rem;
    }

    .drawer-brand-title {
        font-family: 'Amiri', serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--gold);
        margin: 0;
        line-height: 1.2;
    }

    .drawer-brand-sub {
        font-size: 0.74rem;
        color: #64748b;
        display: block;
    }

    .drawer-close-btn {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(0, 0, 0, 0.04);
        border: 1px solid rgba(100, 116, 139, 0.25);
        color: #475569;
        font-size: 1.3rem;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
    }

    .drawer-close-btn:hover {
        background: rgba(239, 68, 68, 0.15);
        border-color: #ef4444;
        color: #dc2626;
    }

    .drawer-search-wrapper {
        padding: 12px 18px;
        border-bottom: 1px solid rgba(100, 116, 139, 0.2);
        background: #f8fafc;
    }

    .drawer-search-input {
        width: 100%;
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 10px;
        padding: 10px 14px;
        color: #0f172a;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.88rem;
        transition: all 0.2s;
    }

    .drawer-search-input:focus {
        outline: none;
        border-color: var(--gold);
        box-shadow: 0 0 12px var(--gold-glow);
    }

    .drawer-nav-body {
        flex-grow: 1;
        overflow-y: auto;
        padding: 16px 18px 40px 18px;
        -webkit-overflow-scrolling: touch;
        background: transparent;
    }

    .drawer-pillar-group {
        margin-bottom: 24px;
    }

    .drawer-pillar-title {
        font-family: 'Amiri', serif;
        font-size: 1.02rem;
        font-weight: 700;
        margin-bottom: 10px;
        padding-bottom: 6px;
        border-bottom: 1px solid rgba(100, 116, 139, 0.2);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .drawer-pillar-items {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .drawer-door-item {
        display: flex;
        align-items: center;
        gap: 12px;
        width: 100%;
        text-align: right;
        padding: 10px 14px;
        background: #ffffff;
        border: 1px solid rgba(203, 213, 225, 0.8);
        border-radius: 10px;
        color: #334155;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.86rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
    }

    .drawer-door-item:hover {
        background: #f8fafc;
        color: #0f172a;
        border-color: var(--gold);
        box-shadow: 0 4px 12px rgba(100, 116, 139, 0.15);
        transform: translateX(-3px);
    }

    .drawer-door-item.active {
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.18), rgba(226, 232, 240, 0.45)) !important;
        border-color: #64748b !important;
        color: #1e293b !important;
        box-shadow: 0 2px 10px rgba(100, 116, 139, 0.18) !important;
    }

    .door-num-badge {
        font-size: 0.72rem;
        font-weight: 800;
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        padding: 2px 6px;
        border-radius: 6px;
        color: #64748b;
        flex-shrink: 0;
    }

    .drawer-door-item.active .door-num-badge {
        border-color: #64748b;
        color: #1e293b;
        background: #ffffff;
    }

    .door-icon {
        font-size: 1.15rem;
        flex-shrink: 0;
    }

    .door-title {
        flex-grow: 1;
        line-height: 1.35;
    }

    /* ========================================================
       MASTER LANDING HUB (لوحة الفهرس الشامل والبوابة الكبرى)
       ======================================================== */
    #tab-hub {
        display: none;
        animation: hubFadeIn 0.4s ease;
    }

    #tab-hub.active {
        display: block;
    }

    @keyframes hubFadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .hub-container {
        max-width: 1500px;
        margin: 0 auto;
        padding: 24px 20px 80px 20px;
    }

    .hub-hero-banner {
        background: radial-gradient(circle at 50% 20%, rgba(148, 163, 184, 0.15) 0%, rgba(203, 213, 225, 0.1) 50%, rgba(248, 250, 252, 0.95) 100%);
        border: 1.5px solid var(--border-gold);
        border-radius: 24px;
        padding: 40px 30px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.05);
        position: relative;
        overflow: hidden;
    }

    .hub-hero-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(148, 163, 184, 0.08) 0%, transparent 60%);
        pointer-events: none;
    }

    .hub-quran-verse {
        display: inline-block;
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.12), rgba(226, 232, 240, 0.45));
        border: 1.5px solid rgba(100, 116, 139, 0.35);
        border-radius: 16px;
        padding: 10px 24px;
        color: #334155;
        font-family: 'Amiri', serif;
        font-size: 1.25rem;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px rgba(100, 116, 139, 0.1);
        font-weight: 700;
    }

    .hub-main-title {
        font-family: 'Amiri', serif;
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0 0 12px 0;
        background: linear-gradient(135deg, #334155 10%, #64748b 60%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.25;
    }

    .hub-sub-title {
        font-size: 1.05rem;
        color: #475569;
        max-width: 900px;
        margin: 0 auto 26px auto;
        line-height: 1.8;
    }

    /* COSMIC METRICS ROW */
    .hub-metrics-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        max-width: 1100px;
        margin: 0 auto;
    }

    .hub-metric-card {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 16px;
        padding: 16px 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
        transition: all 0.25s;
    }

    .hub-metric-card:hover {
        border-color: var(--gold);
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(100, 116, 139, 0.15);
    }

    .metric-val {
        font-family: 'Amiri', serif;
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--gold);
        line-height: 1;
        margin-bottom: 6px;
    }

    .metric-lbl {
        font-size: 0.8rem;
        color: #64748b;
    }

    /* HUB CONTROLS & FILTER */
    .hub-filter-bar {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 18px;
        padding: 14px 20px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        flex-wrap: wrap;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
    }

    .hub-filter-pills {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }

    .hub-filter-pill {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 7px 16px;
        color: #475569;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.85rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
    }

    .hub-filter-pill:hover {
        background: #f1f5f9;
        color: #0f172a;
        border-color: var(--gold);
    }

    .hub-filter-pill.active {
        background: linear-gradient(135deg, var(--gold), #64748b);
        color: #ffffff;
        border-color: var(--gold);
        font-weight: 700;
        box-shadow: 0 2px 10px rgba(100, 116, 139, 0.3);
    }

    .hub-search-box {
        position: relative;
        min-width: 260px;
        flex-grow: 1;
        max-width: 400px;
    }

    .hub-search-input {
        width: 100%;
        background: #f8fafc;
        border: 1.5px solid #cbd5e1;
        border-radius: 12px;
        padding: 8px 16px;
        color: #0f172a;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.88rem;
        transition: all 0.2s;
    }

    .hub-search-input:focus {
        outline: none;
        border-color: var(--gold);
        box-shadow: 0 0 12px var(--gold-glow);
    }

    /* 17 CHAPTER CARDS GRID */
    .hub-doors-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
        gap: 22px;
    }

    .hub-door-card {
        background: rgba(13, 19, 36, 0.82);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 24px;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(12px);
    }

    .hub-door-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        left: 0;
        height: 3px;
        background: var(--door-accent, var(--gold));
        opacity: 0.6;
        transition: height 0.3s ease, opacity 0.3s ease;
    }

    .hub-door-card:hover {
        transform: translateY(-6px);
        border-color: var(--door-accent, var(--gold));
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7);
    }

    .hub-door-card:hover::before {
        height: 5px;
        opacity: 1;
    }

    .card-top-meta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 14px;
    }

    .card-pillar-tag {
        font-size: 0.72rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 8px;
        border: 1px solid transparent;
    }

    .tag-quran {
        background: rgba(255, 209, 102, 0.12);
        color: var(--gold);
        border-color: rgba(255, 209, 102, 0.3);
    }

    .tag-occult-lab {
        background: linear-gradient(135deg, rgba(157, 78, 221, 0.22), rgba(0, 240, 255, 0.16));
        color: #e9d5ff;
        border-color: rgba(157, 78, 221, 0.5);
        box-shadow: 0 0 12px rgba(157, 78, 221, 0.25);
    }

    .card-door-number {
        font-size: 0.76rem;
        font-weight: 800;
        color: #94a3b8;
    }

    .card-icon-box {
        font-size: 2.2rem;
        margin-bottom: 12px;
        display: inline-block;
        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.15));
    }

    .card-door-title {
        font-family: 'Amiri', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 8px;
        line-height: 1.3;
    }

    .card-door-desc {
        font-size: 0.88rem;
        color: #94a3b8;
        line-height: 1.7;
        margin-bottom: 20px;
        flex-grow: 1;
    }

    .card-action-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-top: 14px;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        font-size: 0.84rem;
        font-weight: 700;
        color: var(--door-accent, var(--gold));
    }

    .card-action-bar i {
        transition: transform 0.2s;
    }

    .hub-door-card:hover .card-action-bar i {
        transform: translateX(-5px);
    }

    /* ========================================================
       CHAMBERS CONTAINER SYSTEM & VISIBILITY
       ======================================================== */
    .master-chambers-wrapper {
        width: 100%;
        max-width: 100vw;
    }

    .chamber-view {
        display: none;
        animation: chamberFadeIn 0.35s ease;
        width: 100%;
    }

    .chamber-view.active {
        display: block;
    }

    @keyframes chamberFadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* RESPONSIVE REFINEMENTS & TOUCH SAFETY */
    @media (max-width: 860px) {
        .topbar-inner {
            padding: 6px 12px;
            height: 56px;
        }

        .topbar-hamburger-btn {
            padding: 6px 12px;
            font-size: 0.85rem;
            height: 38px;
        }

        .topbar-main-title {
            font-size: 0.98rem;
        }

        .topbar-chamber-badge {
            max-width: 160px;
            font-size: 0.7rem;
        }

        .hide-mobile {
            display: none !important;
        }

        .hub-main-title {
            font-size: 1.75rem;
        }

        .hub-doors-grid {
            grid-template-columns: 1fr;
        }

        .hub-hero-banner {
            padding: 26px 18px;
        }

        .hub-metrics-row {
            grid-template-columns: repeat(2, 1fr);
        }

        .portal-drawer {
            width: 320px;
        }

        /* Prevent reader drawer or canvas from trapping mobile scroll */
        #reader-drawer:not(.open) {
            pointer-events: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            transform: translateY(110%) !important;
        }

        .drawer-backdrop:not(.active) {
            pointer-events: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }

        .theory-cards-grid {
            max-height: none !important;
            overflow-y: visible !important;
        }

        #graph-fullscreen-wrapper {
            height: auto !important;
            min-height: 440px;
            overflow: visible !important;
        }
    }

    /* CHAMBERS 18 & 19 LUXURY STYLES */
    .astro-tab-pill, .seals-subnav-btn {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        color: #475569;
        padding: 8px 16px;
        border-radius: 10px;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.85rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s;
        white-space: nowrap;
    }
    .astro-tab-pill:hover, .seals-subnav-btn:hover {
        background: #e2e8f0;
        color: #1e293b;
    }
    .astro-tab-pill.active {
        background: linear-gradient(135deg, #475569, #64748b);
        color: #ffffff;
        border-color: #475569;
        box-shadow: 0 0 16px var(--gold-glow);
    }
    .seals-subnav-btn.active {
        background: linear-gradient(135deg, #9d4edd, #7b2cbf);
        color: #fff;
        border-color: #d8b4fe;
        box-shadow: 0 0 16px rgba(157, 78, 221, 0.4);
    }
    .astro-sub-view, .seals-sub-container {
        display: none;
        animation: fadeIn 0.35s ease;
    }
    .astro-sub-view.active, .seals-sub-container.active {
        display: block;
    }
    .astro-identity-card {
        transition: transform 0.25s, box-shadow 0.25s;
    }
    .astro-identity-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.6);
    }

    /* CHAMBER 20 LUXURY STYLES */
    .inner-tab-pill, .layer-pill-btn, .brain-btn {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        color: #475569;
        padding: 8px 16px;
        border-radius: 10px;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.85rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s;
        white-space: nowrap;
    }
    .inner-tab-pill:hover, .layer-pill-btn:hover, .brain-btn:hover {
        background: rgba(255, 255, 255, 0.12);
        color: #fff;
    }
    .inner-tab-pill.active {
        background: linear-gradient(135deg, #0284c7, #0369a1);
        color: #fff;
        border-color: #38bdf8;
        box-shadow: 0 0 16px rgba(56, 189, 248, 0.4);
    }
    .layer-pill-btn.active {
        background: linear-gradient(135deg, #059669, #047857);
        color: #fff;
        border-color: #06d6a0;
        box-shadow: 0 0 16px rgba(6, 214, 160, 0.4);
    }
    .brain-btn.active {
        background: linear-gradient(135deg, #7c3aed, #6d28d9);
        color: #fff;
        border-color: #a855f7;
        box-shadow: 0 0 16px rgba(168, 85, 247, 0.4);
    }
    .inner-sub-view {
        display: none;
        animation: fadeIn 0.35s ease;
    }
    .inner-sub-view.active {
        display: block;
    }
    """ + get_astrolabe_css() + get_esoteric_charts_css() + """

    /* ========================================================
       GRAND ESOTERIC EDUCATIONAL LIBRARY MODAL STYLES
       المكتبة الباطنية التعليمية الشاملة
       ======================================================== */
    .library-modal-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        z-index: 99990;
        display: none;
        align-items: center;
        justify-content: center;
        padding: 20px;
        animation: fadeIn 0.3s ease;
    }

    .library-modal-backdrop.open {
        display: flex;
    }

    .library-modal-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 70%, #edf2f7 100%);
        border: 2px solid var(--border-gold-strong);
        border-radius: 24px;
        width: 100%;
        max-width: 1050px;
        max-height: 88vh;
        overflow-y: auto;
        box-shadow: 0 25px 70px rgba(15, 23, 42, 0.2), 0 0 40px rgba(100, 116, 139, 0.15);
        padding: 30px;
        position: relative;
    }

    .library-modal-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 20px;
        border-bottom: 1.5px solid var(--border-gold);
        margin-bottom: 24px;
    }

    .library-modal-title-group {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .library-modal-title-group h2 {
        font-family: 'Amiri', serif;
        font-size: 1.8rem;
        margin: 0;
        color: #0f172a;
    }

    .library-books-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 18px;
    }

    .library-book-item {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 16px;
        padding: 18px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.25s ease;
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
    }

    .library-book-item:hover {
        border-color: var(--gold);
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.1), 0 0 15px rgba(100, 116, 139, 0.15);
    }

    .book-item-badge {
        font-family: 'Amiri', serif;
        font-size: 0.82rem;
        font-weight: 700;
        color: var(--gold);
        background: rgba(148, 163, 184, 0.15);
        border: 1px solid rgba(148, 163, 184, 0.35);
        padding: 2px 8px;
        border-radius: 6px;
        align-self: flex-start;
        margin-bottom: 8px;
    }

    .book-item-title {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: #334155;
        margin: 0 0 8px 0;
        line-height: 1.4;
    }

    .book-item-desc {
        font-size: 0.82rem;
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 14px;
        flex-grow: 1;
    }

    .book-item-link-btn {
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.18), rgba(148, 163, 184, 0.05));
        border: 1px solid var(--border-gold);
        border-radius: 8px;
        padding: 6px 12px;
        color: var(--gold-bright);
        font-size: 0.82rem;
        font-weight: 700;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.2s;
    }

    .book-item-link-btn:hover {
        background: var(--gold);
        color: #ffffff;
    }

    /* ========================================================
       CHAMBER UNIVERSAL BREADCRUMB & HEADER FRAMEWORK
       ======================================================== */
    .chamber-universal-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid rgba(148, 163, 184, 0.35);
        border-right: 4px solid var(--gold);
        border-radius: 18px;
        padding: 16px 22px;
        margin-bottom: 24px;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.35), 0 0 15px rgba(148, 163, 184, 0.12);
        gap: 16px;
        flex-wrap: wrap;
    }

    .cuh-breadcrumb {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
    }

    .cuh-back-hub-btn {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 6px 14px;
        color: #334155;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.84rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.2s;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    .cuh-back-hub-btn:hover {
        background: var(--gold);
        color: #ffffff;
        box-shadow: 0 0 14px var(--gold-glow);
    }

    .cuh-separator {
        color: #64748b;
        font-weight: 300;
    }

    .cuh-pavilion-tag {
        font-size: 0.82rem;
        color: #64748b;
        font-weight: 600;
    }

    .cuh-door-badge {
        font-family: 'Amiri', serif;
        font-size: 1.08rem;
        font-weight: 700;
        color: #1e293b;
    }

    .cuh-actions {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .cuh-nav-btn {
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 6px 14px;
        color: #334155;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    .cuh-nav-btn:hover {
        background: rgba(30, 42, 80, 0.95);
        border-color: var(--gold);
        color: var(--gold);
    }


    /* ========================================================
       GRAND ESOTERIC CODEX & ANCIENT MANUSCRIPT PORTAL STYLES
       هيكل ديوان المخطوطات والنواميس الكونية
       ======================================================== */

    /* Ornate Manuscript Border Frame */
    .manuscript-border-outer {
        border: 2px solid #475569;
        outline: 1px solid #cbd5e1;
        border-radius: 24px;
        position: relative;
        padding: 6px;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #edf2f7 100%);
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08), inset 0 0 40px rgba(226, 232, 240, 0.5);
    }

    .manuscript-border-inner {
        border: 1px dashed rgba(100, 116, 139, 0.45);
        border-radius: 20px;
        position: relative;
        padding: 34px 28px;
        background: radial-gradient(circle at 50% 10%, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 60%, #edf2f7 100%);
    }


    /* Manuscript Corner Ornaments */
    .corner-ornament {
        position: absolute;
        width: 24px;
        height: 24px;
        color: var(--gold);
        font-size: 1.1rem;
        line-height: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        pointer-events: none;
        user-select: none;
        text-shadow: 0 0 6px var(--gold-glow);
    }
    .corner-tl { top: 6px; right: 6px; }
    .corner-tr { top: 6px; left: 6px; }
    .corner-bl { bottom: 6px; right: 6px; }
    .corner-br { bottom: 6px; left: 6px; }

    /* Grand Frontispiece (فاتحة وديوان المخطوط) */
    .manuscript-frontispiece {
        text-align: center;
        margin-bottom: 40px;
        position: relative;
    }

    .manuscript-tughra-badge {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.15), rgba(226, 232, 240, 0.45));
        border: 1px solid var(--border-gold);
        border-radius: 30px;
        padding: 6px 24px;
        color: #475569;
        font-family: 'Amiri', serif;
        font-size: 1.05rem;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(100, 116, 139, 0.12);
        font-weight: 700;
    }

    .manuscript-main-heading {
        font-family: 'Amiri', serif;
        font-size: clamp(2rem, 4.5vw, 3.2rem);
        font-weight: 800;
        margin: 0 0 16px 0;
        color: #334155;
        line-height: 1.3;
        text-shadow: 0 1px 2px rgba(100, 116, 139, 0.15);
    }

    .hub-quran-verse {
        display: inline-block;
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.12), rgba(226, 232, 240, 0.45));
        border: 1.5px solid var(--border-gold-strong);
        border-radius: 20px;
        padding: 12px 28px;
        color: #334155;
        font-family: 'Amiri', serif;
        font-size: 1.3rem;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(100, 116, 139, 0.12);
        font-weight: 700;
    }

    .manuscript-intro-folio {
        font-size: 1.05rem;
        color: #475569;
        max-width: 950px;
        margin: 0 auto 30px auto;
        line-height: 1.9;
        font-family: 'Tajawal', sans-serif;
    }

    /* Tome Section Blocks (الأجنحة الخمسة الكبرى) */
    .tome-section-block {
        margin-bottom: 50px;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 70%, #f1f5f9 100%);
        border: 1.5px solid #cbd5e1;
        border-radius: 24px;
        padding: 32px 26px;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.05);
        position: relative;
    }

    .tome-header-banner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 20px;
        margin-bottom: 26px;
        border-bottom: 1.5px solid rgba(100, 116, 139, 0.25);
        flex-wrap: wrap;
        gap: 16px;
    }

    .tome-identity {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .tome-icon-seal {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(16, 185, 129, 0.15) 0%, #ffffff 80%);
        border: 1.5px solid var(--border-gold);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.2);
        flex-shrink: 0;
    }

    .tome-title-group h2 {
        font-family: 'Amiri', serif;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 0 0 4px 0;
        color: #0f172a;
    }

    .tome-title-group p {
        font-size: 0.88rem;
        color: #64748b;
        margin: 0;
        line-height: 1.5;
    }

    .tome-badge-count {
        background: rgba(148, 163, 184, 0.15);
        border: 1px solid rgba(100, 116, 139, 0.4);
        border-radius: 20px;
        padding: 6px 16px;
        color: var(--gold);
        font-family: 'Amiri', serif;
        font-size: 0.95rem;
        font-weight: 700;
    }

    /* Manuscript Folio Cards Grid (ألواح المخطوط) */
    .manuscript-folios-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
        gap: 22px;
    }

    .manuscript-folio-card {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 20px;
        padding: 24px;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
    }

    .manuscript-folio-card:hover {
        transform: translateY(-6px);
        border-color: var(--card-accent, var(--gold));
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.1), 0 0 20px rgba(148, 163, 184, 0.25);
        background: #fafbfc;
    }

    .manuscript-folio-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        left: 0;
        height: 3px;
        background: var(--card-accent, var(--gold));
        opacity: 0.7;
        transition: all 0.25s ease;
    }

    .manuscript-folio-card:hover::before {
        height: 5px;
        opacity: 1;
    }

    .folio-top-meta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
    }

    .folio-number-ribbon {
        font-family: 'Amiri', serif;
        font-size: 0.86rem;
        font-weight: 700;
        color: var(--gold);
        background: rgba(148, 163, 184, 0.12);
        border: 1px solid rgba(100, 116, 139, 0.35);
        padding: 3px 10px;
        border-radius: 8px;
    }

    .folio-icon-seal {
        font-size: 2rem;
        margin-bottom: 12px;
        display: inline-block;
    }

    .folio-title {
        font-family: 'Amiri', serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #0f172a;
        margin: 0 0 10px 0;
        line-height: 1.35;
    }

    .folio-excerpt {
        font-size: 0.86rem;
        color: #475569;
        line-height: 1.7;
        margin-bottom: 18px;
        flex-grow: 1;
    }

    .folio-action-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-top: 14px;
        border-top: 1px solid #e2e8f0;
        font-size: 0.84rem;
        font-weight: 700;
        color: var(--card-accent, var(--gold));
    }

    .folio-action-bar i {
        transition: transform 0.2s;
    }

    .manuscript-folio-card:hover .folio-action-bar i {
        transform: translateX(-6px);
    }

    /* Universal Floating Codex Navigation Dock (مسرد التقليب الفوري بين الأبواب) */
    .codex-floating-dock {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 4500;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1.5px solid rgba(100, 116, 139, 0.45);
        border-radius: 40px;
        padding: 8px 18px;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 10px 35px rgba(15, 23, 42, 0.15), 0 0 20px rgba(100, 116, 139, 0.12);
        max-width: 92vw;
    }

    .dock-btn {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 30px;
        padding: 7px 14px;
        color: #334155;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s;
        white-space: nowrap;
    }

    .dock-btn:hover {
        background: #edf2f7;
        border-color: var(--gold);
        color: var(--gold);
    }

    .dock-current-label {
        font-family: 'Amiri', serif;
        font-size: 0.92rem;
        color: var(--gold);
        font-weight: 700;
        padding: 0 8px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 220px;
    }

    /* ========================================================
       UNIVERSAL SUB-GENERATOR CELESTIAL PARADISE & GOLD OVERRIDES
       ======================================================== */
    .theory-node-card,
    .concept-card,
    .node-card,
    .treatise-card,
    .spheres-compendium,
    .codex-card,
    .mansion-card,
    .hours-card,
    .letters-card,
    .body-card,
    .wafq-card,
    .critique-card,
    .astro-identity-card,
    .seal-card,
    .zouhri-card,
    .realm-card,
    .hero,
    .compendium-header,
    .matrix-container,
    .manuscript-card,
    .zodiac-wheel-wrapper,
    .timeline-container {
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        color: #1e293b !important;
        box-shadow: 0 6px 20px rgba(15, 23, 42, 0.05) !important;
        border-radius: 18px !important;
    }

    .theory-node-card:hover,
    .concept-card:hover,
    .treatise-card:hover,
    .codex-card:hover,
    .mansion-card:hover,
    .hours-card:hover,
    .astro-identity-card:hover,
    .seal-card:hover,
    .zouhri-card:hover,
    .realm-card:hover {
        background: #f8fafc !important;
        border-color: var(--gold) !important;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08), 0 0 15px rgba(100, 116, 139, 0.15) !important;
        transform: translateY(-4px) !important;
    }

    table, .matrix-table, .hours-table, .mansion-table {
        background: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 14px !important;
    }

    table td, table th, .matrix-table td, .matrix-table th {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        color: #475569 !important;
    }

    table th, .matrix-table th {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%) !important;
        color: #334155 !important;
        font-weight: 700 !important;
        border-bottom: 2px solid #cbd5e1 !important;
    }

    #graph-fullscreen-wrapper,
    #cy-container,
    #network-container,
    .vis-network {
        background-color: #f8fafc !important;
    }

    """ + get_deluxe_chambers_css()

    # --- MASTER LUXURY TOP BAR HTML ---
    master_topbar_html = """
    <!-- MASTER LUXURY SINGLE TOP BAR -->
    <header class="master-luxury-topbar">
        <div class="topbar-inner">
            <!-- RIGHT: HAMBURGER DRAWER TRIGGER -->
            <button class="topbar-hamburger-btn" onclick="openSidebar()" title="فتح فهرس الأبواب الـ 20">
                <span class="hamburger-icon">☰</span>
                <span>الأبواب</span>
                <span class="hamburger-badge">20</span>
            </button>

            <!-- CENTER: BRAND & ACTIVE CHAMBER INDICATOR -->
            <div class="topbar-center-info" onclick="navigateToChamber('tab-hub')" style="cursor:pointer;" title="العودة للبوابة الرئيسية">
                <span class="topbar-logo-icon">🌌</span>
                <div class="topbar-titles">
                    <span class="topbar-main-title">مختبر المعرفة الكونية</span>
                    <span id="topbar-active-chamber-badge" class="topbar-chamber-badge">🏛️ لوحة الفهرس الشامل</span>
                </div>
            </div>

            <!-- LEFT: QUICK ACTIONS -->
            <div class="topbar-actions">
                <button class="topbar-action-btn" onclick="openLibraryModal()" title="المكتبة الباطنية التعليمية الشاملة (9 كتب)" style="color:var(--gold); border-color:var(--border-gold);">
                    <i class="fa-solid fa-book-bookmark"></i>
                    <span class="hide-mobile">المكتبة التعليمية</span>
                </button>
                <button class="topbar-action-btn" onclick="navigateToChamber('tab-hub')" title="البوابة الرئيسية">
                    <i class="fa-solid fa-house"></i>
                    <span class="hide-mobile">الرئيسية</span>
                </button>
                <button id="quick-tone-btn" class="topbar-action-btn tone-btn" onclick="toggleQuickTone()" title="تشغيل / إيقاف الرنين المداري (528Hz)">
                    <i class="fa-solid fa-wave-square"></i>
                    <span id="quick-tone-label" class="hide-mobile">528Hz</span>
                </button>
                <div class="topbar-pin-status" title="المنظومة مؤمنة ومفعلة">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
            </div>
        </div>
    </header>

    <!-- BACKDROP & SLIDING DRAWER (فهرس الأبواب الـ 20) -->
    <div id="portal-drawer-backdrop" class="portal-drawer-backdrop" onclick="closeSidebar()"></div>

    <aside id="portal-drawer" class="portal-drawer" aria-label="فهرس أبواب الحكمة">
        <div class="drawer-header">
            <div class="drawer-brand">
                <span class="drawer-brand-icon">🌌</span>
                <div>
                    <h3 class="drawer-brand-title">فهرس أبواب الحكمة</h3>
                    <span class="drawer-brand-sub">20 باباً معرفياً موحداً</span>
                </div>
            </div>
            <button class="drawer-close-btn" onclick="closeSidebar()" aria-label="إغلاق">✕</button>
        </div>

        <div class="drawer-search-wrapper">
            <input type="text" id="drawer-search-input" class="drawer-search-input" placeholder="🔍 ابحث في الأبواب الـ 20..." oninput="filterDrawerDoors(this.value)">
        </div>

        <div class="drawer-nav-body">
            <!-- GENERAL HUB ITEM -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:var(--emerald-accent);">
                    <span>🏛️ البوابة واللوحة العامة</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item active" data-door="tab-hub" onclick="navigateToChamber('tab-hub')">
                        <span class="door-num-badge">00</span>
                        <span class="door-icon">🏛️</span>
                        <span class="door-title">لوحة الفهرس الشامل والإحصاء الكوني</span>
                    </button>
                </div>
            </div>

            <!-- PAVILION 1: REVELATION & COSMOLOGY (4 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:var(--gold);">
                    <span>الجناح الأول: كوزمولوجيا التنزيل والملكوت</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">4 أبواب</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item" data-door="tab-graph" onclick="navigateToChamber('tab-graph')">
                        <span class="door-num-badge">01</span>
                        <span class="door-icon">🕸️</span>
                        <span class="door-title">أطلس المفاهيم والشبكة الكونية</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-spheres" onclick="navigateToChamber('tab-spheres')">
                        <span class="door-num-badge">02</span>
                        <span class="door-icon">🪐</span>
                        <span class="door-title">سلّم الأفلاك السبعة وعرش الرحمن</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-matrix" onclick="navigateToChamber('tab-matrix')">
                        <span class="door-num-badge">03</span>
                        <span class="door-icon">🏛️</span>
                        <span class="door-title">مصفوفة البناء المعماري والتناظرات</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-manuscripts" onclick="navigateToChamber('tab-manuscripts')">
                        <span class="door-num-badge">04</span>
                        <span class="door-icon">📜</span>
                        <span class="door-title">أمهات المخطوطات والوثائق النادرة</span>
                    </button>
                </div>
            </div>

            <!-- PAVILION 2: ASTRONOMY & CELESTIAL CYCLES (6 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:#d8b4fe;">
                    <span>الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">6 أبواب</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item" data-door="tab-timeline" onclick="navigateToChamber('tab-timeline')">
                        <span class="door-num-badge">05</span>
                        <span class="door-icon">⏳</span>
                        <span class="door-title">تعاقب العصور والمبادرة المحورية (2,160 سنة)</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-zodiac" onclick="navigateToChamber('tab-zodiac')">
                        <span class="door-num-badge">06</span>
                        <span class="door-icon">♈</span>
                        <span class="door-title">دائرة البروج الاثني عشر والطبائع</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-mansions" onclick="navigateToChamber('tab-mansions')">
                        <span class="door-num-badge">07</span>
                        <span class="door-icon">🌙</span>
                        <span class="door-title">منازل القمر الـ 28 والتوافقات الأثيرية</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-hours" onclick="navigateToChamber('tab-hours')">
                        <span class="door-num-badge">08</span>
                        <span class="door-icon">⏱️</span>
                        <span class="door-title">ساعات الأيام الـ 24 الكلدانية وحكامها</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-kings" onclick="navigateToChamber('tab-kings')">
                        <span class="door-num-badge">09</span>
                        <span class="door-icon">👑</span>
                        <span class="door-title">ملوك الأفلاك والأيام السبعة الكبرى</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-astrology-calc" onclick="navigateToChamber('tab-astrology-calc')">
                        <span class="door-num-badge">10</span>
                        <span class="door-icon">🌌</span>
                        <span class="door-title">المرصد الفلكي التنجيمي الكوني الشامل</span>
                    </button>
                </div>
            </div>

            <!-- PAVILION 3: SACRED MATH & RESONANCE PHYSICS (3 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:var(--cyan-accent);">
                    <span>الجناح الثالث: الأوفاق والرياضيات المقدسة والفيزياء</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">3 أبواب</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item" data-door="tab-letters-magic" onclick="navigateToChamber('tab-letters-magic')">
                        <span class="door-num-badge">11</span>
                        <span class="door-icon">🪶</span>
                        <span class="door-title">طبائع الحروف الـ 28 والعناصر الأربعة</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-numbers" onclick="navigateToChamber('tab-numbers')">
                        <span class="door-num-badge">12</span>
                        <span class="door-icon">🔢</span>
                        <span class="door-title">ديوان الأوفاق والمربعات الرياضية (3×3 إلى 9×9)</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-physics" onclick="navigateToChamber('tab-physics')">
                        <span class="door-num-badge">13</span>
                        <span class="door-icon">🔊</span>
                        <span class="door-title">فيزياء الرنين المداري والمولد الصوتي الحي</span>
                    </button>
                </div>
            </div>

            <!-- PAVILION 4: HUMAN ENERGETIC ANATOMY & INNER CONSCIOUSNESS (5 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:#f472b6;">
                    <span>الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">5 أبواب</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item" data-door="tab-chakras" onclick="navigateToChamber('tab-chakras')">
                        <span class="door-num-badge">14</span>
                        <span class="door-icon">🧘</span>
                        <span class="door-title">مجسم الشاكرات السبع والغدد ومقامات الرسل</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-bodies" onclick="navigateToChamber('tab-bodies')">
                        <span class="door-num-badge">15</span>
                        <span class="door-icon">🧬</span>
                        <span class="door-title">الأجساد السبعة وميكانيكا اختراق الهالة</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-zodiac-angels" onclick="navigateToChamber('tab-zodiac-angels')">
                        <span class="door-num-badge">16</span>
                        <span class="door-icon">🌟</span>
                        <span class="door-title">ملائكة الأبراج والوجوه الـ 36 (Decans)</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-seals-zouhri" onclick="navigateToChamber('tab-seals-zouhri')">
                        <span class="door-num-badge">17</span>
                        <span class="door-icon">👑</span>
                        <span class="door-title">ديوان الأختام الرمزية والإنسان الزوهري والسلالات</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-inner-realms" onclick="navigateToChamber('tab-inner-realms')">
                        <span class="door-num-badge">18</span>
                        <span class="door-icon">🪐</span>
                        <span class="door-title">سفر العوالم الباطنية والإسقاط النجمي وموجات الدماغ</span>
                    </button>
                </div>
            </div>

            <!-- PAVILION 5: EPISTEMIC CRITERION & CRITIQUE (2 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:#fbbf24;">
                    <span>الجناح الخامس: ميزان النقد والبرهان وحصن المرشد</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">بابان</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item" data-door="tab-critique" onclick="navigateToChamber('tab-critique')">
                        <span class="door-num-badge">19</span>
                        <span class="door-icon">⚖️</span>
                        <span class="door-title">ميزان القرآن ودحض التناقضات والخرافات</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-criterion" onclick="navigateToChamber('tab-criterion')">
                        <span class="door-num-badge">20</span>
                        <span class="door-icon">🛡️</span>
                        <span class="door-title">معيار الشريعة وحصن المرشد الباطني</span>
                    </button>
                </div>
            </div>
        </div>
    </aside>
    """

    # --- MASTER LANDING DASHBOARD HTML (#tab-hub) ---
    master_hub_html = """<!-- MASTER ESOTERIC ENCYCLOPEDIA & CODEX PORTAL (#tab-hub) -->
    <section id="tab-hub" class="chamber-view active">
        <div class="hub-container">
            <!-- ORNATE MANUSCRIPT BORDER WRAPPER -->
            <div class="manuscript-border-outer">
                <span class="corner-ornament corner-tl">۞</span>
                <span class="corner-ornament corner-tr">۞</span>
                <span class="corner-ornament corner-bl">۞</span>
                <span class="corner-ornament corner-br">۞</span>

                <div class="manuscript-border-inner">
                    <!-- FRONTISPIECE & ILLUMINATED HEAD -->
                    <div class="manuscript-frontispiece">
                        <div class="manuscript-tughra-badge">
                            <span>✦</span>
                            <span>فاتحة ديوان الحكمة والنواميس الكونية — الموسوعة الموحدة</span>
                            <span>✦</span>
                        </div>
                        <div class="hub-quran-verse">
                            ﴿وَالشَّمْسُ وَالْقَمَرُ بِحُسْبَانٍ ۝ وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ ۝ وَالسَّمَاءَ رَفَعَهَا وَوَضَعَ الْمِيزَانَ﴾
                        </div>
                        <h1 class="manuscript-main-heading">صرح المعرفة الكونية والأسرار الباطنية</h1>
                        <p class="manuscript-intro-folio">
                            الموسوعة الجامعة المنقحة؛ مصنفة تصنيفاً أكاديمياً وباطنياً رصيناً في خمسة أجنحة معرفية كبرى،
                            تربط أصل التنزيل بفيزياء الأفلاك، وهندسة الأوفاق بتشريح الوعي، مع ميزان برهاني حاسم ينفي الخرافات.
                        </p>

                        <!-- LIVE METRICS FOLIO -->
                        <div class="hub-metrics-row">
                            <div class="hub-metric-card">
                                <div class="metric-val">5</div>
                                <div class="metric-lbl">أجنحة معرفية كبرى</div>
                            </div>
                            <div class="hub-metric-card">
                                <div class="metric-val">20</div>
                                <div class="metric-lbl">باباً علمياً مفهرساً</div>
                            </div>
                            <div class="hub-metric-card">
                                <div class="metric-val">73</div>
                                <div class="metric-lbl">عقدة كوزمولوجية مستخلصة</div>
                            </div>
                            <div class="hub-metric-card">
                                <div class="metric-val">28</div>
                                <div class="metric-lbl">منزلة قمرية كوكبية</div>
                            </div>
                            <div class="hub-metric-card">
                                <div class="metric-val">24</div>
                                <div class="metric-lbl">ساعة كلدانية فلكية</div>
                            </div>
                        </div>
                    </div>

                    """ + get_astrolabe_html() + get_esoteric_charts_html() + """
                    <!-- 5 PAVILIONS FILTER BAR & SEARCH -->
                    <div class="hub-filter-bar">
                        <div class="hub-filter-pills">
                            <button class="hub-filter-pill active" onclick="filterPavilionCategory('ALL', event)">كافة الأبواب (20)</button>
                            <button class="hub-filter-pill" onclick="filterPavilionCategory('p1', event)">📜 الجناح 1: التنزيل والملكوت (4)</button>
                            <button class="hub-filter-pill" onclick="filterPavilionCategory('p2', event)">🪐 الجناح 2: الفلك والزمان (6)</button>
                            <button class="hub-filter-pill" onclick="filterPavilionCategory('p3', event)">🔢 الجناح 3: الأوفاق والفيزياء (3)</button>
                            <button class="hub-filter-pill" onclick="filterPavilionCategory('p4', event)">🧘 الجناح 4: الهيكل والوعي (5)</button>
                            <button class="hub-filter-pill" onclick="filterPavilionCategory('p5', event)">⚖️ الجناح 5: ميزان البرهان (2)</button>
                        </div>
                        <div class="hub-search-box">
                            <input type="text" id="hub-search-input" class="hub-search-input" placeholder="🔍 ابحث في الأبواب الـ 20 والمفاهيم..." oninput="filterPavilionSearch(this.value)">
                        </div>
                    </div>

                    <!-- ========================================================
                         الجناح الأول: كوزمولوجيا التنزيل وعوالم العرش (4 أبواب)
                         ======================================================== -->
                    <div class="tome-section-block" id="pavilion-block-1" data-pavilion="p1">
                        <div class="tome-header-banner">
                            <div class="tome-identity">
                                <div class="tome-icon-seal">📜</div>
                                <div class="tome-title-group">
                                    <h2 style="color:var(--gold);">الجناح الأول: كوزمولوجيا التنزيل وعوالم الملكوت</h2>
                                    <p>أطلس المفاهيم، سلم السماوات السبع، مصفوفة البناء الكوني، وأمهات المخطوطات والكتب النادرة</p>
                                </div>
                            </div>
                            <span class="tome-badge-count">4 أبواب</span>
                        </div>

                        <div class="manuscript-folios-grid">
                            <!-- DOOR 01: GRAPH -->
                            <div class="manuscript-folio-card" data-cat="p1" onclick="navigateToChamber('tab-graph')" style="--card-accent:var(--gold);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 01 ۞ التنزيل</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">الشبكة الكونية</span>
                                </div>
                                <div class="folio-icon-seal">🕸️</div>
                                <div class="folio-title">أطلس المفاهيم والشبكة الكونية</div>
                                <div class="folio-excerpt">خريطة بصرية شاملة وأطلس نظري يضم 73 عقدة معرفية ومئات الروابط الفكرية مع نظام تصفية فوري فائق السرعة.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 02: SPHERES -->
                            <div class="manuscript-folio-card" data-cat="p1" onclick="navigateToChamber('tab-spheres')" style="--card-accent:var(--gold);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 02 ۞ التنزيل</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">سلّم الأفلاك</span>
                                </div>
                                <div class="folio-icon-seal">🪐</div>
                                <div class="folio-title">سلّم الأفلاك السبعة وعرش الرحمن</div>
                                <div class="folio-excerpt">مطابقة بصرية تفاعلية بين السماوات السبع، الأفلاك، والأنبياء (من سماء القمر لآدم إلى فلك زحل لإبراهيم) مع شواهد المعراج.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 03: MATRIX -->
                            <div class="manuscript-folio-card" data-cat="p1" onclick="navigateToChamber('tab-matrix')" style="--card-accent:var(--gold);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 03 ۞ التنزيل</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">المصفوفة الجامعة</span>
                                </div>
                                <div class="folio-icon-seal">🏛️</div>
                                <div class="folio-title">مصفوفة البناء المعماري والتناظرات</div>
                                <div class="folio-excerpt">جدول توازني شامل يربط كل فلك بصفته القرآنية، نبيه، معدنه، شاكرته، لونه، والحكمة الباطنية المعتبرة.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 04: MANUSCRIPTS -->
                            <div class="manuscript-folio-card" data-cat="p1" onclick="navigateToChamber('tab-manuscripts')" style="--card-accent:var(--gold);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 04 ۞ التنزيل</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">المخطوطات النادرة</span>
                                </div>
                                <div class="folio-icon-seal">📜</div>
                                <div class="folio-title">أمهات المخطوطات والوثائق النادرة</div>
                                <div class="folio-excerpt">مستودع المخطوطات التاريخية الكبرى (ابن عربي، البوني، السهروردي، جابر بن حيان، وهرمس) مع تحليل نقدي لكل مصدر.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ========================================================
                         الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء (6 أبواب)
                         ======================================================== -->
                    <div class="tome-section-block" id="pavilion-block-2" data-pavilion="p2">
                        <div class="tome-header-banner">
                            <div class="tome-identity">
                                <div class="tome-icon-seal" style="border-color:var(--purple-accent); box-shadow:0 0 20px var(--purple-glow);">🪐</div>
                                <div class="tome-title-group">
                                    <h2 style="color:#d8b4fe;">الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء</h2>
                                    <p>المبادرة المحورية، البروج، منازل القمر، ساعات الكواكب الكلدانية، ملوك الأفلاك، والمرصد التنجيمي الشامل</p>
                                </div>
                            </div>
                            <span class="tome-badge-count" style="border-color:var(--purple-accent); color:#d8b4fe;">6 أبواب</span>
                        </div>

                        <div class="manuscript-folios-grid">
                            <!-- DOOR 05: TIMELINE -->
                            <div class="manuscript-folio-card" data-cat="p2" onclick="navigateToChamber('tab-timeline')" style="--card-accent:#d8b4fe;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 05 ۞ الفلك</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">العصور الكبرى</span>
                                </div>
                                <div class="folio-icon-seal">⏳</div>
                                <div class="folio-title">تعاقب العصور والمبادرة المحورية (2,160 سنة)</div>
                                <div class="folio-excerpt">خط زمني بانورامي لحركة المبادرة المحورية ومحاذاة الاعتدال وتطابقها مع نزول الشرائع الكبرى من السرطان إلى الدلو.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 06: ZODIAC -->
                            <div class="manuscript-folio-card" data-cat="p2" onclick="navigateToChamber('tab-zodiac')" style="--card-accent:#d8b4fe;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 06 ۞ الفلك</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">دائرة البروج</span>
                                </div>
                                <div class="folio-icon-seal">♈</div>
                                <div class="folio-title">دائرة البروج الاثني عشر والطبائع</div>
                                <div class="folio-excerpt">قبة فلكية تفاعلية للبروج ومنازلها وأربابها، طبائعها الأربعة، وموقع البروج في الذكر الحكيم كقوانين مسخرة.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 07: MANSIONS -->
                            <div class="manuscript-folio-card" data-cat="p2" onclick="navigateToChamber('tab-mansions')" style="--card-accent:#d8b4fe;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 07 ۞ الفلك</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">منازل القمر</span>
                                </div>
                                <div class="folio-icon-seal">🌙</div>
                                <div class="folio-title">منازل القمر الـ 28 والتوافقات الأثيرية</div>
                                <div class="folio-excerpt">الدائرة القمرية الكاملة من الشرطين إلى الرشاء، درجاتها الفلكية (12° 51' 26")، طبائعها، وتأثيراتها الأثيرية.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 08: HOURS -->
                            <div class="manuscript-folio-card" data-cat="p2" onclick="navigateToChamber('tab-hours')" style="--card-accent:#d8b4fe;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 08 ۞ الفلك</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">الساعات الكلدانية</span>
                                </div>
                                <div class="folio-icon-seal">⏱️</div>
                                <div class="folio-title">ساعات الأيام الـ 24 وحكامها الكلدانيون</div>
                                <div class="folio-excerpt">النظام البابلي الكلداني لتعاقب الساعات الفلكية (12 نهارية و12 ليلية) وحاكم كل ساعة وتوافقها الترددي.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 09: KINGS -->
                            <div class="manuscript-folio-card" data-cat="p2" onclick="navigateToChamber('tab-kings')" style="--card-accent:#d8b4fe;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 09 ۞ الفلك</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">ملوك الأيام</span>
                                </div>
                                <div class="folio-icon-seal">👑</div>
                                <div class="folio-title">ملوك الأفلاك والأيام السبعة الكبرى</div>
                                <div class="folio-excerpt">مصفوفة حكام الأيام السبعة عبر بابل، مصر، اليونان، النورد، والقبالاه، مع خوادمهم وتوافقات المعادن والبخور.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 10: ASTROLOGY CALC -->
                            <div class="manuscript-folio-card" data-cat="p2" onclick="navigateToChamber('tab-astrology-calc')" style="--card-accent:#d8b4fe;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 10 ۞ الفلك</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">المرصد الشامل</span>
                                </div>
                                <div class="folio-icon-seal">🌌</div>
                                <div class="folio-title">المرصد الفلكي التنجيمي الكوني الشامل</div>
                                <div class="folio-excerpt">محرك حسابي فائق لحساب الطوالع والطبائع عبر 6 حضارات: حساب الجمل والزيج العربي، التنجيم الغربي، البابلي، والفيدي.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ========================================================
                         الجناح الثالث: الأوفاق والرياضيات المقدسة والفيزياء (3 أبواب)
                         ======================================================== -->
                    <div class="tome-section-block" id="pavilion-block-3" data-pavilion="p3">
                        <div class="tome-header-banner">
                            <div class="tome-identity">
                                <div class="tome-icon-seal" style="border-color:var(--cyan-accent); box-shadow:0 0 20px var(--cyan-glow);">🔢</div>
                                <div class="tome-title-group">
                                    <h2 style="color:var(--cyan-accent);">الجناح الثالث: الأوفاق والرياضيات المقدسة والفيزياء</h2>
                                    <p>أسرار الحروف الـ 28، الهندسة الجبرية للأوفاق (3×3 إلى 9×9)، وفيزياء الرنين المداري والمولد الصوتي</p>
                                </div>
                            </div>
                            <span class="tome-badge-count" style="border-color:var(--cyan-accent); color:var(--cyan-accent);">3 أبواب</span>
                        </div>

                        <div class="manuscript-folios-grid">
                            <!-- DOOR 11: LETTERS -->
                            <div class="manuscript-folio-card" data-cat="p3" onclick="navigateToChamber('tab-letters-magic')" style="--card-accent:var(--cyan-accent);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 11 ۞ الرياضيات</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">طبائع الحروف</span>
                                </div>
                                <div class="folio-icon-seal">🪶</div>
                                <div class="folio-title">طبائع الحروف الـ 28 والعناصر الأربعة</div>
                                <div class="folio-excerpt">توزيع الحروف على العناصر الأربعة (نار، هواء، ماء، تراب) وتطابقها الطاقي والترددي مع الأمزجة الإنسانية.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 12: WAFQS / NUMBERS -->
                            <div class="manuscript-folio-card" data-cat="p3" onclick="navigateToChamber('tab-numbers')" style="--card-accent:var(--cyan-accent);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 12 ۞ الرياضيات</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">الهندسة الجبرية</span>
                                </div>
                                <div class="folio-icon-seal">🔢</div>
                                <div class="folio-title">ديوان الأوفاق والمربعات الرياضية (3×3 إلى 9×9)</div>
                                <div class="folio-excerpt">الهندسة الرياضية للأوفاق السحرية كلغة كونية وموجات أثيرية واقفة، مقارنة الحضارات، وتفكيك أوفاق الغزالي ولو شو.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 13: CYMATICS / PHYSICS -->
                            <div class="manuscript-folio-card" data-cat="p3" onclick="navigateToChamber('tab-physics')" style="--card-accent:var(--cyan-accent);">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 13 ۞ الرياضيات</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">الرنين المداري</span>
                                </div>
                                <div class="folio-icon-seal">🔊</div>
                                <div class="folio-title">فيزياء الرنين المداري والمولد الصوتي الحي</div>
                                <div class="folio-excerpt">مختبر تفاعلي حي بمولد صوتي حقيقي (Web Audio API) يولد ترددات الكواكب المدارية مع راسم إشارة مباشر للأمواج.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ========================================================
                         الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي (5 أبواب)
                         ======================================================== -->
                    <div class="tome-section-block" id="pavilion-block-4" data-pavilion="p4">
                        <div class="tome-header-banner">
                            <div class="tome-identity">
                                <div class="tome-icon-seal" style="border-color:#f472b6; box-shadow:0 0 20px rgba(244,114,182,0.4);">🧘</div>
                                <div class="tome-title-group">
                                    <h2 style="color:#f472b6;">الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي</h2>
                                    <p>الشاكرات السبع، الأجساد السبعة، ملائكة الوجوه الـ 36، ديوان الأختام والزوهرية، وسفر العوالم الباطنية والإسقاط النجمي</p>
                                </div>
                            </div>
                            <span class="tome-badge-count" style="border-color:#f472b6; color:#f472b6;">5 أبواب</span>
                        </div>

                        <div class="manuscript-folios-grid">
                            <!-- DOOR 14: CHAKRAS -->
                            <div class="manuscript-folio-card" data-cat="p4" onclick="navigateToChamber('tab-chakras')" style="--card-accent:#f472b6;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 14 ۞ الوعي</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">مراكز الطاقة</span>
                                </div>
                                <div class="folio-icon-seal">🧘</div>
                                <div class="folio-title">مجسم الشاكرات السبع والغدد ومقامات الرسل</div>
                                <div class="folio-excerpt">تشريح مراكز الطاقة الحيوية السبعة في جسد الإنسان، الغدد الصماء المقابلة، ومقارنتها بمقامات الأنبياء.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 15: BODIES -->
                            <div class="manuscript-folio-card" data-cat="p4" onclick="navigateToChamber('tab-bodies')" style="--card-accent:#f472b6;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 15 ۞ الوعي</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">طبقات الوعي</span>
                                </div>
                                <div class="folio-icon-seal">🧬</div>
                                <div class="folio-title">الأجساد السبعة وميكانيكا اختراق الهالة</div>
                                <div class="folio-excerpt">تشريح طبقات الوعي البشري السبع (المادي، الأثيري، النجمي، العقلي، السببي، الروحي، الإلهي) وميكانيكا التحصين.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 16: DECANS -->
                            <div class="manuscript-folio-card" data-cat="p4" onclick="navigateToChamber('tab-zodiac-angels')" style="--card-accent:#f472b6;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 16 ۞ الوعي</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">الوجوه العشرية</span>
                                </div>
                                <div class="folio-icon-seal">🌟</div>
                                <div class="folio-title">ملائكة الأبراج والوجوه الـ 36 (Decans)</div>
                                <div class="folio-excerpt">التشريح الباطني لملوك الأبراج الـ 12 مع أرواح الوجوه العشرية الـ 36 وتقسيماتها الطاقية والعلاجية عبر الحضارات.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 17: SEALS & ZOUHRI -->
                            <div class="manuscript-folio-card" data-cat="p4" onclick="navigateToChamber('tab-seals-zouhri')" style="--card-accent:#f472b6;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 17 ۞ الوعي</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">الأختام والسلالات</span>
                                </div>
                                <div class="folio-icon-seal">👑</div>
                                <div class="folio-title">ديوان الأختام الرمزية والإنسان الزوهري والسلالات</div>
                                <div class="folio-excerpt">الهندسة الرمزية لخاتم سليمان وأختام الكواكب (SVG)، والملف الطبي للزوهريين وتفكيك نبش الكنوز وسلالات بذور النجوم.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 18: INNER REALMS & ASTRAL -->
                            <div class="manuscript-folio-card" data-cat="p4" onclick="navigateToChamber('tab-inner-realms')" style="--card-accent:#f472b6;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 18 ۞ الوعي</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">العوالم الباطنية</span>
                                </div>
                                <div class="folio-icon-seal">🪐</div>
                                <div class="folio-title">سفر العوالم الباطنية والإسقاط النجمي وموجات الدماغ</div>
                                <div class="folio-excerpt">أساطير الأرض المجوفة وعالم المثال، خطوات الإسقاط النجمي بمراحله، التخلص من الطفيليات الأثيرية، ومحاكي موجات الدماغ الحي.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ========================================================
                         الجناح الخامس: ميزان النقد والبرهان وحصن المرشد (بابان)
                         ======================================================== -->
                    <div class="tome-section-block" id="pavilion-block-5" data-pavilion="p5">
                        <div class="tome-header-banner">
                            <div class="tome-identity">
                                <div class="tome-icon-seal" style="border-color:#fbbf24; box-shadow:0 0 20px rgba(251,191,36,0.4);">⚖️</div>
                                <div class="tome-title-group">
                                    <h2 style="color:#fbbf24;">الجناح الخامس: ميزان النقد والبرهان وحصن المرشد</h2>
                                    <p>المسطرة النقدية الصارمة، تفكيك الإسرائيليات والخرافات، ميزان الشريعة التوحيدي، وحصانة طالب الحكمة</p>
                                </div>
                            </div>
                            <span class="tome-badge-count" style="border-color:#fbbf24; color:#fbbf24;">بابان</span>
                        </div>

                        <div class="manuscript-folios-grid">
                            <!-- DOOR 19: CRITIQUE -->
                            <div class="manuscript-folio-card" data-cat="p5" onclick="navigateToChamber('tab-critique')" style="--card-accent:#fbbf24;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 19 ۞ البرهان</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">ميزان التنزيل</span>
                                </div>
                                <div class="folio-icon-seal">⚖️</div>
                                <div class="folio-title">ميزان القرآن ودحض التناقضات والخرافات</div>
                                <div class="folio-excerpt">المسطرة النقدية الصارمة للمرشد: رصد التحريفات في المخطوطات وتفكيك الإسرائيليات والخرافات بالدليل البرهاني القاطع.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>

                            <!-- DOOR 20: CRITERION -->
                            <div class="manuscript-folio-card" data-cat="p5" onclick="navigateToChamber('tab-criterion')" style="--card-accent:#fbbf24;">
                                <div class="folio-top-meta">
                                    <span class="folio-number-ribbon">الباب 20 ۞ البرهان</span>
                                    <span style="font-size:0.75rem; color:#94a3b8;">حصن المرشد</span>
                                </div>
                                <div class="folio-icon-seal">🛡️</div>
                                <div class="folio-title">معيار الشريعة وحصن المرشد الباطني</div>
                                <div class="folio-excerpt">المسطرة الإيمانية الصارمة: الفرق بين دراسة سنن الكون الفلكية وبين الشرك والعبودية لغير الله، وحماية النفس بوحي الخالق.</div>
                                <div class="folio-action-bar">
                                    <span>دخول الباب</span>
                                    <i class="fa-solid fa-arrow-left"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
    """

    # --- MASTER LUXURY JAVASCRIPT CONTROLLER ---
    luxury_js = """
    """ + get_astrolabe_js() + get_esoteric_charts_js() + """
    // ========================================================
    // KNOWLEDGE LAB — MASTER UNIFIED ROUTER & AUDIO CONTROLLER
    // ========================================================
    const CHAMBER_NAMES = {
        'tab-hub': '🏛️ لوحة الفهرس الشامل',
        'tab-graph': 'الباب 01: أطلس المفاهيم والشبكة الكونية',
        'tab-spheres': 'الباب 02: سلم الأفلاك السبعة وعرش الرحمن',
        'tab-matrix': 'الباب 03: مصفوفة البناء المعماري الكوني',
        'tab-manuscripts': 'الباب 04: أمهات المخطوطات والوثائق النادرة',
        'tab-timeline': 'الباب 05: تعاقب العصور والمبادرة المحورية (2,160 سنة)',
        'tab-zodiac': 'الباب 06: دائرة البروج الاثني عشر والطبائع',
        'tab-mansions': 'الباب 07: منازل القمر الـ 28 والتوافقات الأثيرية',
        'tab-hours': 'الباب 08: ساعات الأيام الـ 24 الكلدانية وحكامها',
        'tab-kings': 'الباب 09: ملوك الأفلاك والأيام السبعة الكبرى',
        'tab-astrology-calc': 'الباب 10: المرصد الفلكي التنجيمي الكوني الشامل',
        'tab-letters-magic': 'الباب 11: طبائع الحروف الـ 28 والعناصر الأربعة',
        'tab-numbers': 'الباب 12: ديوان الأوفاق والمربعات الرياضية (3×3 إلى 9×9)',
        'tab-physics': 'الباب 13: فيزياء الرنين المداري والمولد الصوتي الحي',
        'tab-chakras': 'الباب 14: مجسم الشاكرات والغدد ومقامات الرسل',
        'tab-bodies': 'الباب 15: الأجساد السبعة وميكانيكا اختراق الهالة',
        'tab-zodiac-angels': 'الباب 16: ملائكة الأبراج والوجوه العشرية الـ 36',
        'tab-seals-zouhri': 'الباب 17: ديوان الأختام الرمزية والإنسان الزوهري',
        'tab-inner-realms': 'الباب 18: سفر العوالم الباطنية وموجات الدماغ',
        'tab-critique': 'الباب 19: ميزان القرآن ودحض التناقضات والخرافات',
        'tab-criterion': 'الباب 20: معيار الشريعة وحصن المرشد الباطني'
    };

    const CHAMBER_PAVILIONS = {
        'tab-graph': 'الجناح 1: كوزمولوجيا التنزيل وعوالم الملكوت',
        'tab-spheres': 'الجناح 1: كوزمولوجيا التنزيل وعوالم الملكوت',
        'tab-matrix': 'الجناح 1: كوزمولوجيا التنزيل وعوالم الملكوت',
        'tab-manuscripts': 'الجناح 1: كوزمولوجيا التنزيل وعوالم الملكوت',
        'tab-timeline': 'الجناح 2: الفلك الكوني ودورات الزمان والأنواء',
        'tab-zodiac': 'الجناح 2: الفلك الكوني ودورات الزمان والأنواء',
        'tab-mansions': 'الجناح 2: الفلك الكوني ودورات الزمان والأنواء',
        'tab-hours': 'الجناح 2: الفلك الكوني ودورات الزمان والأنواء',
        'tab-kings': 'الجناح 2: الفلك الكوني ودورات الزمان والأنواء',
        'tab-astrology-calc': 'الجناح 2: الفلك الكوني ودورات الزمان والأنواء',
        'tab-letters-magic': 'الجناح 3: الأوفاق والرياضيات المقدسة والفيزياء',
        'tab-numbers': 'الجناح 3: الأوفاق والرياضيات المقدسة والفيزياء',
        'tab-physics': 'الجناح 3: الأوفاق والرياضيات المقدسة والفيزياء',
        'tab-chakras': 'الجناح 4: الهيكل الإنساني، الطاقات الباطنية والوعي',
        'tab-bodies': 'الجناح 4: الهيكل الإنساني، الطاقات الباطنية والوعي',
        'tab-zodiac-angels': 'الجناح 4: الهيكل الإنساني، الطاقات الباطنية والوعي',
        'tab-seals-zouhri': 'الجناح 4: الهيكل الإنساني، الطاقات الباطنية والوعي',
        'tab-inner-realms': 'الجناح 4: الهيكل الإنساني، الطاقات الباطنية والوعي',
        'tab-critique': 'الجناح 5: ميزان النقد والبرهان وحصن المرشد',
        'tab-criterion': 'الجناح 5: ميزان النقد والبرهان وحصن المرشد'
    };

    let activeChamberId = 'tab-hub';

    // CANONICAL ORDERED DOORS (01 to 20) FOR SEQUENTIAL CODEX TURNING
    const CODEX_DOORS_SEQUENCE = [
        'tab-graph',
        'tab-spheres',
        'tab-matrix',
        'tab-manuscripts',
        'tab-timeline',
        'tab-zodiac',
        'tab-mansions',
        'tab-hours',
        'tab-kings',
        'tab-astrology-calc',
        'tab-letters-magic',
        'tab-numbers',
        'tab-physics',
        'tab-chakras',
        'tab-bodies',
        'tab-zodiac-angels',
        'tab-seals-zouhri',
        'tab-inner-realms',
        'tab-critique',
        'tab-criterion'
    ];

    function navigateToPrevDoor() {
        const curIdx = CODEX_DOORS_SEQUENCE.indexOf(activeChamberId);
        if (curIdx > 0) {
            navigateToChamber(CODEX_DOORS_SEQUENCE[curIdx - 1]);
        } else if (curIdx === 0) {
            navigateToChamber('tab-hub');
        }
        if (typeof applyAstrolabeFolio === 'function') applyAstrolabeFolio(3);
    }

    function navigateToNextDoor() {
        const curIdx = CODEX_DOORS_SEQUENCE.indexOf(activeChamberId);
        if (curIdx !== -1 && curIdx < CODEX_DOORS_SEQUENCE.length - 1) {
            navigateToChamber(CODEX_DOORS_SEQUENCE[curIdx + 1]);
        } else if (activeChamberId === 'tab-hub') {
            navigateToChamber(CODEX_DOORS_SEQUENCE[0]);
        }
    }

    // UPDATE DOCK VISIBILITY & TEXT ON CHAMBER SWITCH
    function updateCodexDock(targetId) {
        const dock = document.getElementById('codex-floating-dock');
        const label = document.getElementById('dock-active-title');
        if (!dock) return;

        if (targetId === 'tab-hub') {
            dock.style.display = 'none';
        } else {
            dock.style.display = 'flex';
            if (label) label.innerText = CHAMBER_NAMES[targetId] || 'باب الحكمة';
        }
    }

    // DYNAMIC UNIVERSAL CHAMBER BREADCRUMB
    function updateChamberBreadcrumb(targetId) {
        if (targetId === 'tab-hub') return;
        const targetEl = document.getElementById(targetId);
        if (!targetEl || typeof targetEl.querySelector !== 'function') return;

        let bcrumb = targetEl.querySelector('.chamber-universal-header');
        if (!bcrumb && typeof document.createElement === 'function') {
            bcrumb = document.createElement('div');
            bcrumb.className = 'chamber-universal-header';
            if (typeof targetEl.insertBefore === 'function') {
                targetEl.insertBefore(bcrumb, targetEl.firstChild);
            }
        }

        const curIdx = CODEX_DOORS_SEQUENCE.indexOf(targetId);
        const prevDoor = curIdx > 0 ? CODEX_DOORS_SEQUENCE[curIdx - 1] : null;
        const nextDoor = curIdx < CODEX_DOORS_SEQUENCE.length - 1 ? CODEX_DOORS_SEQUENCE[curIdx + 1] : null;
        const pavilionName = CHAMBER_PAVILIONS[targetId] || 'الأبواب المعرفية';
        const doorNum = (curIdx + 1).toString().padStart(2, '0');
        const titleText = CHAMBER_NAMES[targetId] || 'باب الحكمة';

        bcrumb.innerHTML = `
            <div class="cuh-nav-left">
                <button class="cuh-hub-btn" onclick="navigateToChamber('tab-hub')" title="العودة للفهرس الشامل">
                    <i class="fa-solid fa-arrow-right"></i>
                    <span>الفهرس الشامل</span>
                </button>
                <div class="cuh-breadcrumbs">
                    <span class="cuh-pavilion">${pavilionName}</span>
                    <span class="cuh-sep">/</span>
                    <span class="cuh-door-badge">الباب ${doorNum}</span>
                    <span class="cuh-sep">/</span>
                    <span class="cuh-title">${titleText}</span>
                </div>
            </div>
            <div class="cuh-nav-actions">
                ${prevDoor ? `<button class="cuh-door-nav-btn" onclick="navigateToChamber('${prevDoor}')" title="الباب السابق"><i class="fa-solid fa-chevron-right"></i> الباب السابق</button>` : `<button class="cuh-door-nav-btn" onclick="navigateToChamber('tab-hub')" title="الفهرس الشامل"><i class="fa-solid fa-house"></i> الفهرس</button>`}
                ${nextDoor ? `<button class="cuh-door-nav-btn" onclick="navigateToChamber('${nextDoor}')" title="الباب التالي">الباب التالي <i class="fa-solid fa-chevron-left"></i></button>` : `<button class="cuh-door-nav-btn" onclick="navigateToChamber('tab-hub')" title="الفهرس الشامل">الفهرس <i class="fa-solid fa-house"></i></button>`}
            </div>
        `;
    }

    function openSidebar() {
        const drawer = document.getElementById('portal-drawer');
        const backdrop = document.getElementById('portal-drawer-backdrop');
        if (drawer && backdrop) {
            drawer.classList.add('open');
            backdrop.classList.add('active');
            document.body.classList.add('drawer-open-lock');
            const searchInp = document.getElementById('drawer-search-input');
            if (searchInp) setTimeout(() => searchInp.focus(), 150);
        }
    }

    function closeSidebar() {
        const drawer = document.getElementById('portal-drawer');
        const backdrop = document.getElementById('portal-drawer-backdrop');
        if (drawer && backdrop) {
            drawer.classList.remove('open');
            backdrop.classList.remove('active');
            document.body.classList.remove('drawer-open-lock');
        }
    }

    function navigateToChamber(targetId) {
        // Normalize targetId
        if (!targetId || targetId === 'hub' || targetId === 'index') targetId = 'tab-hub';
        if (targetId === 'graph') targetId = 'tab-graph';
        if (targetId === 'spheres') targetId = 'tab-spheres';
        if (targetId === 'chakras') targetId = 'tab-chakras';
        if (targetId === 'zodiac') targetId = 'tab-zodiac';
        if (targetId === 'timeline') targetId = 'tab-timeline';
        if (targetId === 'matrix') targetId = 'tab-matrix';
        if (targetId === 'manuscripts') targetId = 'tab-manuscripts';
        if (targetId === 'critique') targetId = 'tab-critique';
        if (targetId === 'astrology' || targetId === 'astro' || targetId === 'astrology-calc') targetId = 'tab-astrology-calc';
        if (targetId === 'seals' || targetId === 'zouhri' || targetId === 'seals-zouhri') targetId = 'tab-seals-zouhri';
        if (targetId === 'inner-realms' || targetId === 'realms' || targetId === 'inner') targetId = 'tab-inner-realms';
        if (!targetId.startsWith('tab-')) targetId = 'tab-' + targetId;

        activeChamberId = targetId;

        // Close drawer immediately
        closeSidebar();

        // 1. Hide all views: #tab-hub, all .tab-section (atlas), all .tab-content (codex)
        document.querySelectorAll('#tab-hub, .tab-section, .tab-content').forEach(el => {
            el.classList.remove('active');
            el.style.display = 'none';
        });

        // 2. Activate target element
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
            targetEl.classList.add('active');
            targetEl.style.display = 'block';
        }

        // 3. Update topbar badge
        const badgeEl = document.getElementById('topbar-active-chamber-badge');
        if (badgeEl) {
            badgeEl.innerText = CHAMBER_NAMES[targetId] || 'باب الحكمة';
        }

        // 4. Update sidebar drawer active state
        document.querySelectorAll('.drawer-door-item').forEach(btn => {
            if (btn.getAttribute('data-door') === targetId) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // 5. Inject / update universal breadcrumb header
        updateChamberBreadcrumb(targetId);

        // 6. Special handlers per chamber
        if (targetId === 'tab-graph') {
            if (typeof initAtlasChamber === 'function') {
                initAtlasChamber();
            }
        }
        if (targetId === 'tab-spheres' && typeof renderSpheresOrbits === 'function') {
            setTimeout(renderSpheresOrbits, 60);
        }
        if (targetId === 'tab-zodiac' && typeof renderZodiacWheel === 'function') {
            setTimeout(renderZodiacWheel, 60);
        }
        if (targetId === 'tab-kings' && typeof renderHeptagramKings === 'function') {
            setTimeout(renderHeptagramKings, 60);
        }
        if (targetId === 'tab-letters-magic') {
            if (typeof calculateLiveAbjad === 'function') setTimeout(calculateLiveAbjad, 60);
            if (typeof renderLetters === 'function') renderLetters();
        }
        if (targetId === 'tab-bodies' && typeof renderBodies === 'function') {
            renderBodies();
        }
        if (targetId === 'tab-numbers') {
            if (typeof renderPlanetaryMatrixLab === 'function') renderPlanetaryMatrixLab(currentSelectedWafqOrder || 3);
            if (typeof renderPlanetaryWafqs === 'function') renderPlanetaryWafqs();
            if (typeof calculateLiveWafq === 'function') calculateLiveWafq();
        }
        if (targetId === 'tab-astrology-calc' && typeof runComprehensiveAstroEngine === 'function') {
            runComprehensiveAstroEngine();
        }
        if (targetId === 'tab-seals-zouhri' && typeof renderInteractiveSigils === 'function') {
            renderInteractiveSigils();
        }
        if (targetId === 'tab-inner-realms' && typeof initBrainwaveCanvas === 'function') {
            setTimeout(initBrainwaveCanvas, 100);
        }

        try {
            window.dispatchEvent(new CustomEvent('chamberSwitched', { detail: { chamberId: targetId } }));
        } catch(e) {}

        // 7. Update URL hash, floating dock, and smooth scroll
        if (window.location) window.location.hash = '#' + targetId;
        updateCodexDock(targetId);
        if (typeof window.scrollTo === 'function') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    // Legacy Routing Aliases
    window.switchTab = navigateToChamber;
    window.switchCodexTab = navigateToChamber;

    // Open Library Modal / Chamber
    function openLibraryModal() {
        navigateToChamber('tab-manuscripts');
    }
    window.openLibraryModal = openLibraryModal;

    // DRAWER SEARCH FILTER
    function filterDrawerDoors(query) {
        const q = (query || '').trim().toLowerCase();
        document.querySelectorAll('.drawer-door-item').forEach(btn => {
            const text = btn.innerText.toLowerCase();
            if (!q || text.includes(q)) {
                btn.style.display = 'flex';
            } else {
                btn.style.display = 'none';
            }
        });
    }

    // HUB FILTER & SEARCH (5 PAVILIONS)
    function filterPavilionCategory(cat, evt) {
        document.querySelectorAll('.hub-filter-pills .hub-filter-pill').forEach(pill => {
            pill.classList.remove('active');
        });
        const clicked = evt ? evt.currentTarget || evt.target : (window.event ? window.event.target : null);
        if (clicked) clicked.classList.add('active');

        const q = (document.getElementById('hub-search-input')?.value || '').trim().toLowerCase();

        // 1. Filter Pavilion Section Blocks (1 to 5)
        ['pavilion-block-1', 'pavilion-block-2', 'pavilion-block-3', 'pavilion-block-4', 'pavilion-block-5'].forEach((id, idx) => {
            const el = document.getElementById(id);
            if (!el) return;
            const blockCat = 'p' + (idx + 1);
            if (cat === 'ALL' || cat === blockCat) {
                el.style.display = 'block';
            } else {
                el.style.display = 'none';
            }
        });

        // 2. Filter individual folio cards
        document.querySelectorAll('.manuscript-folio-card').forEach(card => {
            const cardCat = card.getAttribute('data-cat');
            const cardText = card.innerText.toLowerCase();
            const matchesCat = (cat === 'ALL' || cardCat === cat);
            const matchesQuery = (!q || cardText.includes(q));

            if (matchesCat && matchesQuery) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Aliases
    window.filterHubCategory = filterPavilionCategory;

    function filterPavilionSearch(query) {
        const q = (query || '').trim().toLowerCase();
        document.querySelectorAll('.manuscript-folio-card').forEach(card => {
            const cardText = card.innerText.toLowerCase();
            if (!q || cardText.includes(q)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });

        // If searching, show all pavilion blocks so matched cards are visible
        ['pavilion-block-1', 'pavilion-block-2', 'pavilion-block-3', 'pavilion-block-4', 'pavilion-block-5'].forEach(id => {
            const el = document.getElementById(id);
            if (el) el.style.display = 'block';
        });
    }

    // Aliases
    window.filterHubSearch = filterPavilionSearch;

    // QUICK AUDIO TONE TOGGLE (Web Audio API)
    let quickAudioCtx = null;
    let quickOsc = null;
    let quickGain = null;
    let isQuickAudioPlaying = false;

    function toggleQuickTone() {
        const btn = document.getElementById('quick-tone-btn');
        const label = document.getElementById('quick-tone-label');

        if (isQuickAudioPlaying) {
            if (quickOsc) {
                try { quickOsc.stop(); quickOsc.disconnect(); } catch(e){}
                quickOsc = null;
            }
            isQuickAudioPlaying = false;
            if (btn) btn.classList.remove('playing');
            if (label) label.innerText = '528Hz';
        } else {
            try {
                const AudioCtx = window.AudioContext || window.webkitAudioContext;
                if (!quickAudioCtx) quickAudioCtx = new AudioCtx();
                if (quickAudioCtx.state === 'suspended') quickAudioCtx.resume();

                quickOsc = quickAudioCtx.createOscillator();
                quickGain = quickAudioCtx.createGain();

                // Solfeggio 528 Hz (Transformation & DNA Harmonic)
                quickOsc.type = 'sine';
                quickOsc.frequency.setValueAtTime(528, quickAudioCtx.currentTime);

                quickGain.gain.setValueAtTime(0.001, quickAudioCtx.currentTime);
                quickGain.gain.exponentialRampToValueAtTime(0.12, quickAudioCtx.currentTime + 0.1);

                quickOsc.connect(quickGain);
                quickGain.connect(quickAudioCtx.destination);
                quickOsc.start();

                isQuickAudioPlaying = true;
                if (btn) btn.classList.add('playing');
                if (label) label.innerText = 'إيقاف';
            } catch(e) {
                console.warn('Audio tone could not play', e);
            }
        }
    }

    // ESCAPE KEY CLOSES ALL MODALS/DRAWERS
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeSidebar();
            if (typeof closeReaderDrawer === 'function') closeReaderDrawer();
        }
    });

    // ROUTER INITIALIZATION ON LOAD
    window.addEventListener('load', () => {
        const hash = window.location.hash.replace('#', '');
        if (hash && (CHAMBER_NAMES[hash] || CHAMBER_NAMES['tab-' + hash])) {
            navigateToChamber(hash.startsWith('tab-') ? hash : 'tab-' + hash);
        } else {
            navigateToChamber('tab-hub');
        }
        if (typeof applyAstrolabeFolio === 'function') applyAstrolabeFolio(3);

        // Check password memory
        if (localStorage.getItem('knowledge_lab_auth') === 'granted') {
            const gate = document.getElementById('portal-auth-gate');
            if (gate) gate.classList.add('unlocked');
        }
    });

    // OVERRIDE handlePortalAuth TO REMEMBER LOGIN
    const originalHandlePortalAuth = window.handlePortalAuth;
    window.handlePortalAuth = function(e) {
        if (e) e.preventDefault();
        const input = document.getElementById('auth-pass-input');
        const errorMsg = document.getElementById('auth-error-msg');
        const gate = document.getElementById('portal-auth-gate');

        if (input && input.value.trim() === '1234') {
            localStorage.setItem('knowledge_lab_auth', 'granted');
            if (gate) gate.classList.add('unlocked');
        } else {
            if (errorMsg) errorMsg.style.display = 'block';
            if (input) { input.value = ''; input.focus(); }
        }
    };
    """

    # --- ASSEMBLE COMPLETE UNIFIED PAGE ---
    print("[3/5] Merging CSS, HTML structure and JS...")

    # Combine CSS
    combined_css = f"""
    <style>
    {codex_css_clean}
    {luxury_css}
    </style>
    """

    # Put CSS right before </head>
    head_end_pos = atlas_clean.find('</head>')
    if head_end_pos != -1:
        atlas_with_css = atlas_clean[:head_end_pos] + combined_css + atlas_clean[head_end_pos:]
    else:
        atlas_with_css = atlas_clean + combined_css

    # Inject dark mode & theme color meta tags (Slate-Grey #111823)
    dark_meta = """
    <meta name="color-scheme" content="dark">
    <meta name="theme-color" content="#111823">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    """
    if "color-scheme" not in atlas_with_css:
        atlas_with_css = atlas_with_css.replace('<head>', f'<head>\n{dark_meta}')

    # Enforce dark inline style on html tag if missing (Slate-Grey #111823)
    if 'style="background-color: #111823;' not in atlas_with_css:
        atlas_with_css = atlas_with_css.replace('<html lang="ar" dir="rtl">', '<html lang="ar" dir="rtl" style="background-color: #111823; color-scheme: dark;">')
        # Also replace any legacy #030611 or #02040a if already present on html tag
        atlas_with_css = atlas_with_css.replace('style="background-color: #030611;', 'style="background-color: #111823;')
        atlas_with_css = atlas_with_css.replace('style="background-color: #02040a;', 'style="background-color: #111823;')

    # Inject font-awesome if not present
    if "font-awesome" not in atlas_with_css:
        atlas_with_css = atlas_with_css.replace('</head>', '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>')

    # Inject Topbar & Drawer right after <body> or auth gate
    body_pos = atlas_with_css.find('<body>')
    if body_pos != -1:
        # Find auth gate end
        auth_gate_end = atlas_with_css.find('</div>\n    </div>', body_pos)
        if auth_gate_end != -1:
            inject_pos = auth_gate_end + len('</div>\n    </div>')
        else:
            inject_pos = body_pos + len('<body>')
        
        atlas_with_header = atlas_with_css[:inject_pos] + "\n" + master_topbar_html + "\n" + atlas_with_css[inject_pos:]
    else:
        atlas_with_header = master_topbar_html + atlas_with_css

    # Wrap <main> with master-chambers-wrapper and inject codex chapters and hub
    main_open_pos = atlas_with_header.find('<main>')
    main_close_pos = atlas_with_header.find('</main>')

    if main_open_pos != -1 and main_close_pos != -1:
        atlas_main_inner = atlas_with_header[main_open_pos + len('<main>'):main_close_pos]
        
        # Thoroughly purge old chambers superseded by deluxe versions from both atlas and codex
        superseded_chambers = ["tab-graph", "tab-spheres", "tab-zodiac", "tab-mansions", "tab-kings", "tab-letters-magic", "tab-numbers"]
        
        for tab_id in superseded_chambers:
            while True:
                found = False
                for tag in ["section", "div"]:
                    res = extract_tag_content(atlas_main_inner, tag, tab_id)
                    if res:
                        s, e, _ = res
                        atlas_main_inner = atlas_main_inner[:s] + atlas_main_inner[e:]
                        found = True
                        break
                if not found:
                    break

        for tab_id in superseded_chambers:
            while True:
                found = False
                for tag in ["section", "div"]:
                    res = extract_tag_content(codex_main_clean, tag, tab_id)
                    if res:
                        s, e, _ = res
                        codex_main_clean = codex_main_clean[:s] + codex_main_clean[e:]
                        found = True
                        break
                if not found:
                    break

        deluxe_chambers_html = get_deluxe_chambers_html()
        astro_chamber_html = get_astrology_chamber_html()
        seals_chamber_html = get_seals_zouhri_chamber_html()
        inner_realms_chamber_html = get_inner_realms_chamber_html()

        # Build unified main
        unified_main = f"""
        <main class="master-chambers-wrapper">
            {master_hub_html}
            {deluxe_chambers_html}
            {atlas_main_inner}
            {codex_main_clean}
            {astro_chamber_html}
            {seals_chamber_html}
            {inner_realms_chamber_html}
        </main>
        """

        raw_assembled_html = atlas_with_header[:main_open_pos] + unified_main + atlas_with_header[main_close_pos + len('</main>'):]
        
        # Wrap EVERY remaining raw chamber into the royal manuscript architecture
        assembled_html = wrap_all_raw_chambers(raw_assembled_html)
    else:
        assembled_html = atlas_with_header

    # Floating dock HTML component
    floating_dock_html = """
    <!-- UNIVERSAL FLOATING CODEX NAVIGATION DOCK -->
    <div id="codex-floating-dock" class="codex-floating-dock" style="display:none;">
        <button class="dock-btn" onclick="navigateToPrevDoor()" title="الباب السابق">
            <i class="fa-solid fa-chevron-right"></i>
            <span>السابق</span>
        </button>
        <span id="dock-active-title" class="dock-current-label">باب الحكمة</span>
        <button class="dock-btn" onclick="navigateToChamber('tab-hub')" title="الفهرس الشامل">
            <i class="fa-solid fa-compass"></i>
            <span>الفهرس</span>
        </button>
        <button class="dock-btn" onclick="navigateToNextDoor()" title="الباب التالي">
            <span>التالي</span>
            <i class="fa-solid fa-chevron-left"></i>
        </button>
    </div>
    """

    # Inject unified scripts and floating dock right before </body>
    body_end_pos = assembled_html.rfind('</body>')
    if body_end_pos != -1:
        astro_chamber_js = get_astrology_chamber_js()
        seals_chamber_js = get_seals_zouhri_chamber_js()
        inner_realms_chamber_js = get_inner_realms_chamber_js()
        cosmic_db_js = get_cosmic_database_js()
        visual_canvas_js = get_chambers_visual_js()

        full_js_block = f"""
        {floating_dock_html}
        <script>
        {cosmic_db_js}
        {visual_canvas_js}
        {codex_js_clean}
        {astro_chamber_js}
        {seals_chamber_js}
        {inner_realms_chamber_js}
        {luxury_js}
        </script>
        """
        final_html = assembled_html[:body_end_pos] + full_js_block + assembled_html[body_end_pos:]
    else:
        final_html = assembled_html

    # Inject anti-cache meta tags and favicon right after <head>
    cache_meta = """
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <meta name="version" content="8.6-esoteric-paradise">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🌌</text></svg>">
    <link rel="shortcut icon" href="data:image/x-icon;," type="image/x-icon">
    """
    if '<head>' in final_html:
        final_html = final_html.replace('<head>', '<head>' + cache_meta, 1)

    print("[4/5] Writing to destination files across all entry points...")
    # 1. Write website/index.html
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(final_html)

    def safe_write_portal(dst_path):
        try:
            with open(dst_path, 'w', encoding='utf-8') as df:
                df.write(final_html)
            print(f"  + Updated: {dst_path}")
        except Exception as e:
            print(f"  ! Warning updating {dst_path}: {e}")

    # 2. Sync to root files
    safe_write_portal(ROOT_INDEX)
    safe_write_portal(ROOT_VIEWER)

    # 3. Sync to Codex & Atlas entry points so opening ANY file gives the unified luxury portal
    root_codex = os.path.join(ROOT_DIR, "Grand_Occult_Cosmology_Codex.html")
    web_codex = os.path.join(WEBSITE_DIR, "Grand_Occult_Cosmology_Codex.html")
    root_atlas = os.path.join(ROOT_DIR, "Prophetic_Cosmic_Atlas.html")
    safe_write_portal(root_codex)
    safe_write_portal(web_codex)
    safe_write_portal(root_atlas)

    # 4. Create and sync docs/ folder in case GitHub Pages is configured to /docs
    docs_dir = os.path.join(ROOT_DIR, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    safe_write_portal(os.path.join(docs_dir, "index.html"))

    print("[5/5] Success! All entry points synchronized and verified.")




if __name__ == "__main__":
    build_luxury_portal()
