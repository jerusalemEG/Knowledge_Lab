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
       KNOWLEDGE LAB — GRAND ESOTERIC ENCYCLOPEDIA (v7.0 PREMIUM)
       موسوعة باطنية حكيمة — Architecture Upgrade
       ======================================================== */
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Tajawal:wght@300;400;500;600;700;800;900&display=swap');

    :root {
        color-scheme: dark !important;
        --void-black: #030611;
        --bg-space: #030611;
        --bg-void: #030611;
        --card-glass: rgba(8, 13, 28, 0.92);
        --card-glass-2: rgba(12, 18, 38, 0.88);
        --border-gold: rgba(212, 170, 55, 0.3);
        --border-gold-strong: rgba(212, 170, 55, 0.55);
        --gold: #d4aa37;
        --gold-light: #f0c84a;
        --gold-dim: rgba(212, 170, 55, 0.15);
        --gold-glow: rgba(212, 170, 55, 0.5);
        --purple-accent: #8b5cf6;
        --purple-light: #c4b5fd;
        --purple-glow: rgba(139, 92, 246, 0.45);
        --cyan-accent: #22d3ee;
        --cyan-glow: rgba(34, 211, 238, 0.4);
        --emerald-accent: #10b981;
        --emerald-glow: rgba(16, 185, 129, 0.4);
        --rose-accent: #fb7185;
        --text-primary: #f0f4ff;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --section-max: 1480px;
        --radius-sm: 10px;
        --radius-md: 16px;
        --radius-lg: 22px;
        --radius-xl: 30px;
        --shadow-card: 0 8px 32px rgba(0,0,0,0.6);
        --shadow-deep: 0 20px 60px rgba(0,0,0,0.8);
        --transition-smooth: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    html {
        background-color: #030611 !important;
        background: #030611 !important;
        color-scheme: dark !important;
        color: var(--text-primary) !important;
        scrollbar-color: rgba(212, 170, 55, 0.3) #030611 !important;
        font-size: 16px;
    }

    body {
        width: 100%;
        max-width: 100vw;
        overflow-x: hidden !important;
        position: relative;
        background-color: #030611 !important;
        background-image: 
            radial-gradient(ellipse at 15% 10%, rgba(34, 211, 238, 0.04) 0%, transparent 55%),
            radial-gradient(ellipse at 85% 90%, rgba(212, 170, 55, 0.05) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(139, 92, 246, 0.03) 0%, transparent 65%),
            radial-gradient(ellipse at 78% 18%, rgba(16, 185, 129, 0.025) 0%, transparent 40%) !important;
        background-attachment: fixed !important;
        color-scheme: dark !important;
        font-family: 'Tajawal', sans-serif;
        font-size: 16px;
        line-height: 1.7;
        color: var(--text-primary) !important;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
        scroll-behavior: smooth;
        scrollbar-color: rgba(212, 170, 55, 0.3) #030611 !important;
    }

    * {
        box-sizing: border-box;
        scrollbar-color: rgba(212, 170, 55, 0.3) #030611 !important;
    }

    /* Premium Dark Scrollbars */
    ::-webkit-scrollbar {
        width: 7px !important;
        height: 7px !important;
    }
    ::-webkit-scrollbar-track {
        background: rgba(2, 4, 14, 0.95) !important;
        border-radius: 8px !important;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, rgba(212, 170, 55, 0.45), rgba(212, 170, 55, 0.18)) !important;
        border-radius: 8px !important;
        border: 1.5px solid #030611 !important;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, rgba(212, 170, 55, 0.75), rgba(212, 170, 55, 0.45)) !important;
    }

    /* Universal Master Chambers Dark Void Enforcement */
    .master-chambers-wrapper,
    .chamber-view,
    .tab-section,
    .tab-content,
    #tab-hub,
    #tab-graph,
    #tab-spheres,
    #tab-chakras,
    #tab-zodiac,
    #tab-timeline,
    #tab-matrix,
    #tab-manuscripts,
    #tab-mizan,
    #tab-kings,
    #tab-decans,
    #tab-hours,
    #tab-mansions,
    #tab-letters-magic,
    #tab-bodies,
    #tab-numbers,
    #tab-cymatics,
    #tab-murshid,
    #tab-astrology-calc,
    #tab-seals-zouhri,
    #tab-inner-realms,
    main {
        background-color: #030611 !important;
        color: var(--text-primary) !important;
    }

    /* Universal Form & Input Dark Enforcement */
    input, select, textarea, button {
        color-scheme: dark !important;
    }
    input[type="date"], input[type="time"] {
        color-scheme: dark !important;
        background: rgba(0, 0, 0, 0.6) !important;
        color: #f1f5f9 !important;
    }

    body.drawer-open-lock {
        overflow: hidden !important;
        touch-action: none;
    }

    /* =====================================================
       PREMIUM TOPBAR — ESOTERIC ENCYCLOPEDIA v7
       ===================================================== */
    .master-luxury-topbar {
        position: sticky;
        top: 0;
        z-index: 5000;
        background: rgba(3, 5, 16, 0.97);
        backdrop-filter: blur(32px) saturate(1.5);
        -webkit-backdrop-filter: blur(32px) saturate(1.5);
        border-bottom: 1px solid rgba(212, 170, 55, 0.15);
        box-shadow: 
            inset 0 -1px 0 rgba(212, 170, 55, 0.08),
            0 20px 60px rgba(0, 0, 0, 0.98);
        width: 100%;
    }

    .topbar-inner {
        max-width: var(--section-max);
        margin: 0 auto;
        padding: 10px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 14px;
        height: 64px;
    }

    /* HAMBURGER TRIGGER BUTTON */
    .topbar-hamburger-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(135deg, rgba(255, 209, 102, 0.18), rgba(255, 209, 102, 0.04));
        border: 1px solid rgba(255, 209, 102, 0.45);
        border-radius: 12px;
        padding: 8px 16px;
        color: var(--gold);
        font-family: 'Tajawal', sans-serif;
        font-size: 0.92rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 0 16px rgba(255, 209, 102, 0.18);
        flex-shrink: 0;
        height: 42px;
    }

    .topbar-hamburger-btn:hover {
        background: var(--gold);
        color: #030712;
        box-shadow: 0 0 24px var(--gold-glow);
        transform: translateY(-1px);
    }

    .topbar-hamburger-btn .hamburger-icon {
        font-size: 1.25rem;
        line-height: 1;
    }

    .hamburger-badge {
        background: rgba(255, 209, 102, 0.25);
        padding: 2px 7px;
        border-radius: 10px;
        font-size: 0.74rem;
        color: inherit;
        border: 1px solid rgba(255, 209, 102, 0.4);
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
        font-size: 1.18rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold) 55%, var(--purple-light) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        line-height: 1.3;
        letter-spacing: 0.02em;
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
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 10px;
        padding: 8px 12px;
        color: #e2e8f0;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        height: 40px;
    }

    .topbar-action-btn:hover {
        background: rgba(255, 255, 255, 0.12);
        color: #fff;
        border-color: rgba(255, 209, 102, 0.4);
    }

    .topbar-action-btn.tone-btn {
        color: var(--cyan-accent);
        border-color: rgba(0, 240, 255, 0.35);
        background: rgba(0, 240, 255, 0.08);
    }

    .topbar-action-btn.tone-btn.playing {
        background: var(--cyan-accent);
        color: #030611;
        box-shadow: 0 0 16px var(--cyan-glow);
    }

    .topbar-pin-status {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(6, 214, 160, 0.1);
        border: 1px solid rgba(6, 214, 160, 0.3);
        color: var(--emerald-accent);
        font-size: 0.88rem;
    }

    /* ========================================================
       MUSEUM-GRADE SIDEBAR DRAWER (فهرس الأبواب الـ 17)
       ======================================================== */
    .portal-drawer-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(1, 3, 8, 0.82);
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
        background: rgba(4, 7, 20, 0.99);
        border-left: 1px solid rgba(212, 170, 55, 0.18);
        box-shadow: -24px 0 80px rgba(0, 0, 0, 0.98), inset 1px 0 0 rgba(212, 170, 55, 0.08);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        transform: translateX(100%);
        transition: transform 0.38s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .portal-drawer.open {
        transform: translateX(0);
    }

    .drawer-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 18px 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        background: rgba(15, 23, 42, 0.8);
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
        font-size: 1.22rem;
        font-weight: 700;
        color: var(--gold);
        margin: 0;
        line-height: 1.2;
    }

    .drawer-brand-sub {
        font-size: 0.72rem;
        color: #94a3b8;
        display: block;
    }

    .drawer-close-btn {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #cbd5e1;
        font-size: 1.3rem;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
    }

    .drawer-close-btn:hover {
        background: rgba(239, 68, 68, 0.2);
        border-color: #ef4444;
        color: #fca5a5;
    }

    .drawer-search-wrapper {
        padding: 12px 18px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        background: rgba(3, 7, 18, 0.5);
    }

    .drawer-search-input {
        width: 100%;
        background: rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 10px;
        padding: 10px 14px;
        color: #fff;
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
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
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
        padding: 11px 14px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: var(--radius-sm);
        color: var(--text-secondary);
        font-family: 'Tajawal', sans-serif;
        font-size: 0.86rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.22s ease;
    }

    .drawer-door-item:hover {
        background: rgba(255, 255, 255, 0.07);
        color: var(--text-primary);
        border-color: rgba(212, 170, 55, 0.3);
        transform: translateX(-4px);
    }

    .drawer-door-item.active {
        background: linear-gradient(135deg, rgba(212, 170, 55, 0.18), rgba(212, 170, 55, 0.04));
        border-color: rgba(212, 170, 55, 0.5);
        color: var(--gold-light);
        box-shadow: 0 0 16px rgba(212, 170, 55, 0.15);
    }

    .door-num-badge {
        font-size: 0.72rem;
        font-weight: 800;
        background: rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 2px 6px;
        border-radius: 6px;
        color: #94a3b8;
        flex-shrink: 0;
    }

    .drawer-door-item.active .door-num-badge {
        border-color: var(--gold);
        color: var(--gold);
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
        max-width: var(--section-max);
        margin: 0 auto;
        padding: 32px 24px 100px 24px;
    }

    .hub-hero-banner {
        background: 
            radial-gradient(ellipse at 50% 0%, rgba(212, 170, 55, 0.1) 0%, transparent 55%),
            radial-gradient(ellipse at 15% 80%, rgba(139, 92, 246, 0.08) 0%, transparent 45%),
            radial-gradient(ellipse at 85% 80%, rgba(34, 211, 238, 0.06) 0%, transparent 45%),
            rgba(6, 10, 24, 0.96);
        border: 1px solid rgba(212, 170, 55, 0.2);
        border-radius: var(--radius-xl);
        padding: 52px 36px 44px;
        text-align: center;
        margin-bottom: 32px;
        box-shadow: 
            var(--shadow-deep),
            inset 0 1px 0 rgba(212, 170, 55, 0.15),
            inset 0 0 60px rgba(139, 92, 246, 0.04);
        position: relative;
        overflow: hidden;
    }

    .hub-hero-banner::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(212, 170, 55, 0.5), rgba(139, 92, 246, 0.4), transparent);
        pointer-events: none;
    }

    .hub-hero-banner::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(34, 211, 238, 0.2), transparent);
        pointer-events: none;
    }

    .hub-quran-verse {
        display: inline-block;
        background: linear-gradient(135deg, rgba(212, 170, 55, 0.12), rgba(212, 170, 55, 0.05));
        border: 1px solid rgba(212, 170, 55, 0.35);
        border-radius: 20px;
        padding: 12px 28px;
        color: var(--gold-light);
        font-family: 'Amiri', serif;
        font-size: 1.3rem;
        line-height: 1.8;
        margin-bottom: 22px;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5), 0 0 30px rgba(212, 170, 55, 0.08);
        letter-spacing: 0.02em;
    }

    .hub-main-title {
        font-family: 'Amiri', serif;
        font-size: clamp(1.8rem, 4vw, 2.8rem);
        font-weight: 700;
        margin: 0 0 16px 0;
        background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold) 45%, var(--purple-light) 80%, var(--cyan-accent) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.3;
        letter-spacing: 0.01em;
    }

    .hub-sub-title {
        font-size: 1.05rem;
        color: rgba(203, 213, 225, 0.85);
        max-width: 820px;
        margin: 0 auto 32px auto;
        line-height: 1.9;
        font-weight: 300;
        letter-spacing: 0.01em;
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
        background: rgba(10, 15, 35, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: var(--radius-md);
        padding: 20px 14px;
        text-align: center;
        backdrop-filter: blur(14px);
        transition: var(--transition-smooth);
        position: relative;
        overflow: hidden;
    }

    .hub-metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--gold-dim), transparent);
        transition: opacity 0.3s;
        opacity: 0;
    }

    .hub-metric-card:hover {
        border-color: rgba(212, 170, 55, 0.35);
        transform: translateY(-4px);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.65), 0 0 20px rgba(212, 170, 55, 0.06);
    }

    .hub-metric-card:hover::before {
        opacity: 1;
    }

    .metric-val {
        font-family: 'Amiri', serif;
        font-size: 2rem;
        font-weight: 700;
        color: var(--gold);
        line-height: 1;
        margin-bottom: 8px;
        text-shadow: 0 0 20px rgba(212, 170, 55, 0.3);
    }

    .metric-lbl {
        font-size: 0.78rem;
        color: var(--text-secondary);
        font-weight: 500;
        line-height: 1.4;
    }

    /* HUB CONTROLS & FILTER */
    .hub-filter-bar {
        background: rgba(8, 12, 30, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: var(--radius-lg);
        padding: 16px 22px;
        margin-bottom: 28px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        flex-wrap: wrap;
        backdrop-filter: blur(12px);
    }

    .hub-filter-pills {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }

    .hub-filter-pill {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 7px 16px;
        color: #cbd5e1;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.85rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
    }

    .hub-filter-pill:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #fff;
    }

    .hub-filter-pill.active {
        background: linear-gradient(135deg, var(--gold), #d49300);
        color: #030611;
        border-color: var(--gold);
        font-weight: 700;
        box-shadow: 0 0 14px var(--gold-glow);
    }

    .hub-search-box {
        position: relative;
        min-width: 260px;
        flex-grow: 1;
        max-width: 400px;
    }

    .hub-search-input {
        width: 100%;
        background: rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 12px;
        padding: 8px 16px;
        color: #fff;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.88rem;
        transition: all 0.2s;
    }

    .hub-search-input:focus {
        outline: none;
        border-color: var(--gold);
        box-shadow: 0 0 14px var(--gold-glow);
    }

    /* 17 CHAPTER CARDS GRID */
    .hub-doors-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
        gap: 24px;
    }

    .hub-door-card {
        background: var(--card-glass);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: var(--radius-lg);
        padding: 26px 24px;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: var(--transition-smooth);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(16px);
        box-shadow: var(--shadow-card);
    }

    .hub-door-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        left: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, var(--door-accent, var(--gold)) 40%, var(--door-accent, var(--gold)) 60%, transparent 100%);
        opacity: 0.5;
        transition: height 0.3s ease, opacity 0.3s ease;
    }

    .hub-door-card:hover {
        transform: translateY(-7px);
        border-color: var(--door-accent, var(--gold));
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0,0,0,0.2);
    }

    .hub-door-card:hover::before {
        height: 3px;
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
        background: rgba(212, 170, 55, 0.1);
        color: var(--gold-light);
        border-color: rgba(212, 170, 55, 0.28);
    }

    .tag-occult-lab {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.18), rgba(34, 211, 238, 0.12));
        color: var(--purple-light);
        border-color: rgba(139, 92, 246, 0.4);
        box-shadow: 0 0 10px rgba(139, 92, 246, 0.2);
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
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 10px;
        line-height: 1.35;
        letter-spacing: 0.01em;
    }

    .card-door-desc {
        font-size: 0.87rem;
        color: var(--text-secondary);
        line-height: 1.75;
        margin-bottom: 22px;
        flex-grow: 1;
        font-weight: 400;
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


    /* =====================================================
       ENCYCLOPEDIC TYPOGRAPHY SYSTEM — GLOBAL HEADINGS
       ===================================================== */
    .enc-chapter-header {
        background: linear-gradient(135deg, rgba(10, 15, 35, 0.98), rgba(6, 10, 22, 0.95));
        border-bottom: 1px solid rgba(212, 170, 55, 0.2);
        padding: 36px 32px 30px;
        position: relative;
        overflow: hidden;
    }

    .enc-chapter-header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, transparent 0%, var(--gold) 30%, var(--purple-accent) 70%, transparent 100%);
    }

    .enc-chapter-eyebrow {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        color: var(--cyan-accent);
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .enc-chapter-eyebrow::after {
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, rgba(34, 211, 238, 0.3), transparent);
    }

    .enc-chapter-title {
        font-family: 'Amiri', serif;
        font-size: clamp(1.6rem, 3vw, 2.5rem);
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 10px;
        line-height: 1.3;
    }

    .enc-chapter-subtitle {
        font-size: 0.95rem;
        color: var(--text-secondary);
        line-height: 1.7;
        max-width: 700px;
    }

    /* Global table improvements */
    table {
        border-collapse: collapse;
        width: 100%;
    }

    th {
        font-family: 'Amiri', serif;
        font-size: 0.9rem;
        font-weight: 700;
        color: var(--gold-light);
        background: rgba(10, 15, 35, 0.9);
        padding: 12px 16px;
        border: 1px solid rgba(255, 255, 255, 0.07);
        text-align: right;
    }

    td {
        padding: 11px 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: var(--text-secondary);
        font-size: 0.88rem;
        line-height: 1.6;
        background: rgba(6, 10, 22, 0.6);
    }

    tr:hover td {
        background: rgba(10, 16, 36, 0.9);
        color: var(--text-primary);
    }

    /* Selection highlight */
    ::selection {
        background: rgba(212, 170, 55, 0.25);
        color: var(--gold-light);
    }

    /* Premium section dividers */
    .enc-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(212, 170, 55, 0.25), rgba(139, 92, 246, 0.2), transparent);
        margin: 36px 0;
        border: none;
    }

    /* Responsive grid */
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
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #cbd5e1;
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
        background: rgba(255, 255, 255, 0.12);
        color: #fff;
    }
    .astro-tab-pill.active {
        background: linear-gradient(135deg, var(--gold), #d49300);
        color: #030611;
        border-color: var(--gold);
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
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #cbd5e1;
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
    """

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

            <!-- PILLAR 1: QURANIC & PROPHETIC COSMOLOGY (8 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:var(--gold);">
                    <span>الركن الأول: كوزمولوجيا الوحي والنبوات</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">8 أبواب</span>
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
                        <span class="door-title">سلم الأفلاك السبعة وعرش الرحمن</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-chakras" onclick="navigateToChamber('tab-chakras')">
                        <span class="door-num-badge">03</span>
                        <span class="door-icon">🧘</span>
                        <span class="door-title">مجسم التشاكرات والأنبياء</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-zodiac" onclick="navigateToChamber('tab-zodiac')">
                        <span class="door-num-badge">04</span>
                        <span class="door-icon">♈</span>
                        <span class="door-title">دائرة البروج الاثني عشر</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-timeline" onclick="navigateToChamber('tab-timeline')">
                        <span class="door-num-badge">05</span>
                        <span class="door-icon">⏳</span>
                        <span class="door-title">تعاقب العصور الكبرى (2,160 سنة)</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-matrix" onclick="navigateToChamber('tab-matrix')">
                        <span class="door-num-badge">06</span>
                        <span class="door-icon">🏛️</span>
                        <span class="door-title">المصفوفة المعمارية الشاملة</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-manuscripts" onclick="navigateToChamber('tab-manuscripts')">
                        <span class="door-num-badge">07</span>
                        <span class="door-icon">📜</span>
                        <span class="door-title">أمهات المخطوطات والوثائق النادرة</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-critique" onclick="navigateToChamber('tab-critique')">
                        <span class="door-num-badge">08</span>
                        <span class="door-icon">⚖️</span>
                        <span class="door-title">ميزان القرآن ودحض التناقضات</span>
                    </button>
                </div>
            </div>

            <!-- MERGED PILLAR 2: OCCULT CODEX & INTERACTIVE LAB (11 DOORS) -->
            <div class="drawer-pillar-group">
                <div class="drawer-pillar-title" style="color:#d8b4fe;">
                    <span>الركن الثاني: سفر النواميس والمختبر الرياضي التفاعلي</span>
                    <span style="font-size:0.75rem; color:#94a3b8;">12 باباً</span>
                </div>
                <div class="drawer-pillar-items">
                    <button class="drawer-door-item" data-door="tab-kings" onclick="navigateToChamber('tab-kings')">
                        <span class="door-num-badge">09</span>
                        <span class="door-icon">👑</span>
                        <span class="door-title">ملوك الأفلاك والأيام السبعة الكبرى</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-zodiac-angels" onclick="navigateToChamber('tab-zodiac-angels')">
                        <span class="door-num-badge">10</span>
                        <span class="door-icon">🌟</span>
                        <span class="door-title">ملائكة الأبراج والوجوه الـ 36 (Decans)</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-hours" onclick="navigateToChamber('tab-hours')">
                        <span class="door-num-badge">11</span>
                        <span class="door-icon">⏱️</span>
                        <span class="door-title">ساعات الأيام الـ 24 الكلدانية</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-mansions" onclick="navigateToChamber('tab-mansions')">
                        <span class="door-num-badge">12</span>
                        <span class="door-icon">🌙</span>
                        <span class="door-title">منازل القمر الـ 28 والتوافقات</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-letters-magic" onclick="navigateToChamber('tab-letters-magic')">
                        <span class="door-num-badge">13</span>
                        <span class="door-icon">🪶</span>
                        <span class="door-title">طبائع الحروف الأربعة والأسحار</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-bodies" onclick="navigateToChamber('tab-bodies')">
                        <span class="door-num-badge">14</span>
                        <span class="door-icon">🧬</span>
                        <span class="door-title">الأجساد السبعة وميكانيكا الاختراق</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-numbers" onclick="navigateToChamber('tab-numbers')">
                        <span class="door-num-badge">15</span>
                        <span class="door-icon">🔢</span>
                        <span class="door-title">الأوفاق الكونية والمربعات السحرية (3×3 إلى 9×9)</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-physics" onclick="navigateToChamber('tab-physics')">
                        <span class="door-num-badge">16</span>
                        <span class="door-icon">🔊</span>
                        <span class="door-title">فيزياء الذبذبات والمولد الصوتي الحي</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-criterion" onclick="navigateToChamber('tab-criterion')">
                        <span class="door-num-badge">17</span>
                        <span class="door-icon">⚖️</span>
                        <span class="door-title">ميزان الشريعة وحصن المرشد</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-astrology-calc" onclick="navigateToChamber('tab-astrology-calc')">
                        <span class="door-num-badge">18</span>
                        <span class="door-icon">🌌</span>
                        <span class="door-title">المرصد الفلكي التنجيمي الكوني الشامل</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-seals-zouhri" onclick="navigateToChamber('tab-seals-zouhri')">
                        <span class="door-num-badge">19</span>
                        <span class="door-icon">👑</span>
                        <span class="door-title">ديوان الأختام والزوهرية والسلالات الروحية</span>
                    </button>
                    <button class="drawer-door-item" data-door="tab-inner-realms" onclick="navigateToChamber('tab-inner-realms')">
                        <span class="door-num-badge">20</span>
                        <span class="door-icon">🪐</span>
                        <span class="door-title">سفر العوالم الباطنية، الجسد الأثيري، وأسرار الوعي</span>
                    </button>
                </div>
            </div>
        </div>
    </aside>
    """

    # --- MASTER LANDING DASHBOARD HTML (#tab-hub) ---
    master_hub_html = """
    <!-- MASTER LANDING DASHBOARD (#tab-hub) -->
    <section id="tab-hub" class="chamber-view active">
        <div class="hub-container">
            <!-- HERO BANNER -->
            <div class="hub-hero-banner">
                <div class="hub-quran-verse">
                    ﴿وَالشَّمْسُ وَالْقَمَرُ بِحُسْبَانٍ ۝ وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ ۝ وَالسَّمَاءَ رَفَعَهَا وَوَضَعَ الْمِيزَانَ﴾
                </div>
                <h1 class="hub-main-title">مختبر المعرفة الكونية والنواميس الأزلية</h1>
                <p class="hub-sub-title">
                    الموسوعة الموحدة الكبرى التي تصهر كوزمولوجيا الوحي القرآني، شبكة النبوات، علوم الأفلاك، 
                    الأوفاق الهندسية، منازل القمر، الساعات الكلدانية، وفيزياء الرنين الترددي في صرح معرفي واحد لا نظير له.
                </p>

                <!-- LIVE METRICS -->
                <div class="hub-metrics-row">
                    <div class="hub-metric-card">
                        <div class="metric-val">73</div>
                        <div class="metric-lbl">عقدة كوزمولوجية مستخلصة</div>
                    </div>
                    <div class="hub-metric-card">
                        <div class="metric-val">20</div>
                        <div class="metric-lbl">باباً علمياً مفهرساً</div>
                    </div>
                    <div class="hub-metric-card">
                        <div class="metric-val">7</div>
                        <div class="metric-lbl">أفلاك وترددات مدارية</div>
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

            <!-- CONTROLS & SEARCH BAR -->
            <div class="hub-filter-bar">
                <div class="hub-filter-pills">
                    <button class="hub-filter-pill active" onclick="filterHubCategory('ALL')">الكل (20)</button>
                    <button class="hub-filter-pill" onclick="filterHubCategory('quran')">الركن الأول: كوزمولوجيا الوحي والنبوات (8)</button>
                    <button class="hub-filter-pill" onclick="filterHubCategory('occult_lab')">الركن الثاني: سفر النواميس والمختبر الرياضي (12)</button>
                </div>
                <div class="hub-search-box">
                    <input type="text" id="hub-search-input" class="hub-search-input" placeholder="🔍 ابحث في الأبواب الـ 20 والمفاهيم..." oninput="filterHubSearch(this.value)">
                </div>
            </div>

            <!-- 17 CHAPTER CARDS GRID -->
            <div class="hub-doors-grid" id="hub-doors-grid">
                <!-- DOOR 1 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-graph')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 01</span>
                    </div>
                    <div class="card-icon-box">🕸️</div>
                    <div class="card-door-title">أطلس المفاهيم والشبكة الكونية</div>
                    <div class="card-door-desc">خريطة تفاعلية شاملة وأطلس نظري يضم 73 عقدة معرفية ومئات الروابط الفكرية مع نظام تصفية وبحث فوري فائق السرعة للهواتف والحواسيب.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 2 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-spheres')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 02</span>
                    </div>
                    <div class="card-icon-box">🪐</div>
                    <div class="card-door-title">سلم الأفلاك السبعة وعرش الرحمن</div>
                    <div class="card-door-desc">مطابقة بصرية تفاعلية بين السماوات السبع، الأفلاك، والأنبياء (من فلك القمر لآدم إلى فلك زحل لإبراهيم) مع شواهد المعراج النبوي.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 3 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-chakras')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 03</span>
                    </div>
                    <div class="card-icon-box">🧘</div>
                    <div class="card-door-title">مجسم التشاكرات والأنبياء</div>
                    <div class="card-door-desc">تشريح مراكز الطاقة الحيوية السبعة في الهيكل الإنساني، الغدد الصماء المقابلة، ومقارنتها بمقامات الأنبياء ونقد التحريف الفيدانتي.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 4 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-zodiac')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 04</span>
                    </div>
                    <div class="card-icon-box">♈</div>
                    <div class="card-door-title">دائرة البروج الاثني عشر</div>
                    <div class="card-door-desc">قبة فلكية تفاعلية للبروج ومنازلها وأربابها، طبائعها الأربعة، وموقع البروج في الذكر الحكيم كآيات وقوانين كونية مسخرة.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 5 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-timeline')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 05</span>
                    </div>
                    <div class="card-icon-box">⏳</div>
                    <div class="card-door-title">تعاقب العصور الكبرى (2,160 سنة)</div>
                    <div class="card-door-desc">خط زمني بانورامي لحركة المبادرة المحورية (2,160 سنة لكل عصر فلكي) وتطابقها مع نزول الشرائع الكبرى من الثور إلى الحوت والدلو.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 6 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-matrix')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 06</span>
                    </div>
                    <div class="card-icon-box">🏛️</div>
                    <div class="card-door-title">المصفوفة المعمارية الشاملة</div>
                    <div class="card-door-desc">جدول توازني ضخم يربط كل فلك بصفته القرآنية، نبيه، معدنه، شاكرته، لونه، والحكمة الباطنية المنسوبة له في التراث المعتبر.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 7 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-manuscripts')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 07</span>
                    </div>
                    <div class="card-icon-box">📜</div>
                    <div class="card-door-title">أمهات المخطوطات والوثائق النادرة</div>
                    <div class="card-door-desc">مستودع المخطوطات الكبرى (ابن عربي، البوني، السهروردي، جابر بن حيان، هرمس) مع تحليل نقدي معماري لكل كتاب ومصدر.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 8 -->
                <div class="hub-door-card" data-cat="quran" onclick="navigateToChamber('tab-critique')" style="--door-accent:var(--gold);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-quran">كوزمولوجيا الوحي</span>
                        <span class="card-door-number">الباب 08</span>
                    </div>
                    <div class="card-icon-box">⚖️</div>
                    <div class="card-door-title">ميزان القرآن ودحض التناقضات</div>
                    <div class="card-door-desc">المسطرة النقدية الصارمة للمرشد: رصد التحريفات في المخطوطات، وتفكيك الإسرائيليات والخرافات بالدليل القرآني القاطع.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 9 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-kings')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 09</span>
                    </div>
                    <div class="card-icon-box">👑</div>
                    <div class="card-door-title">ملوك الأفلاك والأيام السبعة</div>
                    <div class="card-door-desc">مصفوفة ملوك الأفلاك والأيام السبعة عبر بابل، مصر، اليونان، النورد، والقبالاه، مع خوادمهم السفلية وتوافقات البخور والمعادن.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 10 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-zodiac-angels')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 10</span>
                    </div>
                    <div class="card-icon-box">🌟</div>
                    <div class="card-door-title">ملائكة الأبراج والوجوه الـ 36</div>
                    <div class="card-door-desc">التشريح الباطني لملوك الأبراج الـ 12 مع أرواح الوجوه العشرية الـ 36 (Decans - باكيو) وتقسيماتها الطاقية والعلاجية عبر الحضارات.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 11 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-hours')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 11</span>
                    </div>
                    <div class="card-icon-box">⏱️</div>
                    <div class="card-door-title">ساعات الأيام الـ 24 الكلدانية</div>
                    <div class="card-door-desc">النظام الكلداني البابلي لتعاقب الساعات الفلكية (12 نهارية و12 ليلية) وحاكم كل ساعة وأفضل الأعمال الروحانية المتناغمة معها.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 12 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-mansions')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 12</span>
                    </div>
                    <div class="card-icon-box">🌙</div>
                    <div class="card-door-title">منازل القمر الـ 28 والتوافقات</div>
                    <div class="card-door-desc">الدائرة القمرية الكاملة من الشرطين إلى الرشاء، درجاتها الفلكية (12° 51' 26")، طبائعها، وخواصها الأثيرية في كتب الأقدمين.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 13 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-letters-magic')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 13</span>
                    </div>
                    <div class="card-icon-box">🪶</div>
                    <div class="card-door-title">طبائع الحروف والأسحار الأربعة</div>
                    <div class="card-door-desc">توزيع الحروف الـ 28 على العناصر الأربعة (ناري، هوائي، مائي، ترابي) وتصنيف الأسحار وتطابقها الطاقي مع الأمزجة البشرية.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 14 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-bodies')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 14</span>
                    </div>
                    <div class="card-icon-box">🧬</div>
                    <div class="card-door-title">الأجساد السبعة وميكانيكا الاختراق</div>
                    <div class="card-door-desc">تشريح طبقات الوعي البشري السبع (المادي، الأثيري، النجمي، العقلي، السببي، الروحي، الإلهي) وكيف يخترق التردد السلبي الهالة.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 15 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-numbers')" style="--door-accent:var(--cyan-accent);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 15</span>
                    </div>
                    <div class="card-icon-box">🔢</div>
                    <div class="card-door-title">الأوفاق الكونية والمربعات السحرية (3×3 حتى 9×9)</div>
                    <div class="card-door-desc">الهندسة الرياضية للأوفاق السحرية كلغة كونية وموجات أثيرية واقفة، مقارنة الحضارات (لو شو، الفيدا، أغريبا، والغزالي)، ودستور البناء والتفعيل والإغلاق.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 16 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-physics')" style="--door-accent:var(--cyan-accent);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 16</span>
                    </div>
                    <div class="card-icon-box">🔊</div>
                    <div class="card-door-title">فيزياء الذبذبات والمولد الصوتي</div>
                    <div class="card-door-desc">مختبر تفاعلي حي بمولد صوتي حقيقي (Web Audio API) يولد ترددات الكواكب المدارية مع شاشة راسم إشارة (Canvas) لتحليل الموجات.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 17 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-criterion')" style="--door-accent:var(--cyan-accent);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 17</span>
                    </div>
                    <div class="card-icon-box">⚖️</div>
                    <div class="card-door-title">ميزان الشريعة والمرشد الباطني</div>
                    <div class="card-door-desc">المسطرة الإيمانية الصارمة: الفرق بين دراسة سنن الكون الفلكية وبين الشرك والعبودية لغير الله، وحماية النفس بوحي الخالق.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 18 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-astrology-calc')" style="--door-accent:var(--cyan-accent);">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 18</span>
                    </div>
                    <div class="card-icon-box">🌌</div>
                    <div class="card-door-title">المرصد الفلكي التنجيمي الكوني الشامل</div>
                    <div class="card-door-desc">محرك تفاعلي فائق لحساب الطوالع والطبائع عبر 6 حضارات: حساب الجمل والزيج العربي (بالاسم واسم الأم)، التنجيم الغربي، البابلي، الفيدي، الأركان الصينية، والارتباط القبالي.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 19 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-seals-zouhri')" style="--door-accent:#d8b4fe;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 19</span>
                    </div>
                    <div class="card-icon-box">👑</div>
                    <div class="card-door-title">ديوان الأختام والزوهرية والسلالات</div>
                    <div class="card-door-desc">الهندسة الرمزية لخاتم سليمان الأعظم وأختام الكواكب السبعة (SVG)، والملف الطبي والأنثروبولوجي للإنسان الزوهري وتفكيك نبش الكنوز، وموسوعة السلالات الروحية وبذور النجوم.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>

                <!-- DOOR 20 -->
                <div class="hub-door-card" data-cat="occult_lab" onclick="navigateToChamber('tab-inner-realms')" style="--door-accent:#38bdf8;">
                    <div class="card-top-meta">
                        <span class="card-pillar-tag tag-occult-lab">سفر النواميس والمختبر</span>
                        <span class="card-door-number">الباب 20</span>
                    </div>
                    <div class="card-icon-box">🪐</div>
                    <div class="card-door-title">سفر العوالم الباطنية وأسرار الوعي</div>
                    <div class="card-door-desc">أساطير الأراضي الباطنية وأغارثا وعوالم المثال، تشريح الهالة والقرين والتنقية الإدراكية، تاريخ ومراحل الإسقاط النجمي وعلومه العصبية، وسر الأوفاق وتنزيه الحقيقة المحمدية، مع مختبر محاكاة موجات الدماغ.</div>
                    <div class="card-action-bar">
                        <span>دخول الباب</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

    # --- MASTER LUXURY JAVASCRIPT CONTROLLER ---
    luxury_js = """
    // ========================================================
    // KNOWLEDGE LAB — MASTER UNIFIED ROUTER & AUDIO CONTROLLER
    // ========================================================
    const CHAMBER_NAMES = {
        'tab-hub': '🏛️ لوحة الفهرس الشامل',
        'tab-graph': 'الباب 01: أطلس المفاهيم والشبكة الكونية',
        'tab-spheres': 'الباب 02: سلم الأفلاك السبعة وعرش الرحمن',
        'tab-chakras': 'الباب 03: مجسم التشاكرات والأنبياء',
        'tab-zodiac': 'الباب 04: دائرة البروج الاثني عشر',
        'tab-timeline': 'الباب 05: تعاقب العصور (2,160 سنة)',
        'tab-matrix': 'الباب 06: مصفوفة البناء المعماري الكوني',
        'tab-manuscripts': 'الباب 07: أمهات المخطوطات والكتب النادرة',
        'tab-critique': 'الباب 08: ميزان القرآن ودحض التناقضات',
        'tab-kings': 'الباب 09: ملوك الأفلاك والأيام السبعة',
        'tab-zodiac-angels': 'الباب 10: ملائكة الأبراج والـ 36 وجهاً',
        'tab-hours': 'الباب 11: ساعات الأيام الـ 24 الكلدانية',
        'tab-mansions': 'الباب 12: منازل القمر الـ 28 والتوافقات',
        'tab-letters-magic': 'الباب 13: طبائع الحروف والأسحار الأربعة',
        'tab-bodies': 'الباب 14: الأجساد السبعة وميكانيكا الاختراق',
        'tab-numbers': 'الباب 15: شفرة الأرقام والوفق الغزالي 3×3',
        'tab-physics': 'الباب 16: فيزياء الذبذبات والمولد الصوتي',
        'tab-criterion': 'الباب 17: ميزان الشريعة وحصن المرشد',
        'tab-astrology-calc': 'الباب 18: المرصد الفلكي التنجيمي الشامل',
        'tab-seals-zouhri': 'الباب 19: ديوان الأختام والزوهرية والسلالات',
        'tab-inner-realms': 'الباب 20: سفر العوالم الباطنية وأسرار الوعي'
    };

    let activeChamberId = 'tab-hub';

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

        // 5. Special handlers per chamber
        if (targetId === 'tab-graph') {
            // Auto-trigger mobile theory mode if screen is narrow
            if (window.innerWidth <= 860 && typeof switchGraphMode === 'function') {
                switchGraphMode('theory');
            }
            if (typeof cosmicNetwork !== 'undefined' && cosmicNetwork) {
                setTimeout(() => { cosmicNetwork.redraw(); cosmicNetwork.fit(); }, 200);
            }
        }
        if (targetId === 'tab-letters-magic' && typeof renderLetters === 'function') {
            renderLetters();
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

        // 6. Update URL hash and smooth scroll
        window.location.hash = '#' + targetId;
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Legacy Routing Aliases
    window.switchTab = navigateToChamber;
    window.switchCodexTab = navigateToChamber;

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

    // HUB FILTER & SEARCH
    function filterHubCategory(cat, evt) {
        document.querySelectorAll('.hub-filter-pill').forEach(pill => {
            pill.classList.remove('active');
        });
        const clicked = evt ? evt.target : (window.event ? window.event.target : null);
        if (clicked) clicked.classList.add('active');

        const q = (document.getElementById('hub-search-input')?.value || '').trim().toLowerCase();

        document.querySelectorAll('.hub-door-card').forEach(card => {
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

    function filterHubSearch(query) {
        const q = (query || '').trim().toLowerCase();
        const activePill = document.querySelector('.hub-filter-pill.active');
        const activeText = activePill ? activePill.innerText : '';
        let currentCat = 'ALL';
        if (activeText.includes('الوحي')) currentCat = 'quran';
        if (activeText.includes('النواميس') || activeText.includes('المختبر')) currentCat = 'occult_lab';

        document.querySelectorAll('.hub-door-card').forEach(card => {
            const cardCat = card.getAttribute('data-cat');
            const cardText = card.innerText.toLowerCase();
            const matchesCat = (currentCat === 'ALL' || cardCat === currentCat);
            const matchesQuery = (!q || cardText.includes(q));

            if (matchesCat && matchesQuery) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

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

    # Inject dark mode & theme color meta tags
    dark_meta = """
    <meta name="color-scheme" content="dark">
    <meta name="theme-color" content="#030611">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    """
    if "color-scheme" not in atlas_with_css:
        atlas_with_css = atlas_with_css.replace('<head>', f'<head>\n{dark_meta}')

    # Enforce dark inline style on html tag if missing
    if 'style="background-color: #030611;' not in atlas_with_css:
        atlas_with_css = atlas_with_css.replace('<html lang="ar" dir="rtl">', '<html lang="ar" dir="rtl" style="background-color: #030611; color-scheme: dark;">')

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
        
        astro_chamber_html = get_astrology_chamber_html()
        seals_chamber_html = get_seals_zouhri_chamber_html()
        inner_realms_chamber_html = get_inner_realms_chamber_html()

        # Build unified main
        unified_main = f"""
        <main class="master-chambers-wrapper">
            {master_hub_html}
            {atlas_main_inner}
            {codex_main_clean}
            {astro_chamber_html}
            {seals_chamber_html}
            {inner_realms_chamber_html}
        </main>
        """

        assembled_html = atlas_with_header[:main_open_pos] + unified_main + atlas_with_header[main_close_pos + len('</main>'):]
    else:
        assembled_html = atlas_with_header

    # Inject unified scripts right before </body>
    body_end_pos = assembled_html.rfind('</body>')
    if body_end_pos != -1:
        astro_chamber_js = get_astrology_chamber_js()
        seals_chamber_js = get_seals_zouhri_chamber_js()
        inner_realms_chamber_js = get_inner_realms_chamber_js()

        full_js_block = f"""
        <script>
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

    print("[4/5] Writing to destination files...")
    # Write website/index.html
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(final_html)

    # Sync to root files
    shutil.copyfile(INDEX_PATH, ROOT_INDEX)
    shutil.copyfile(INDEX_PATH, ROOT_VIEWER)

    print("[5/5] Success! Verified files updated:")
    print(f"  - {INDEX_PATH} ({len(final_html):,} bytes)")
    print(f"  - {ROOT_INDEX}")
    print(f"  - {ROOT_VIEWER}")


if __name__ == "__main__":
    build_luxury_portal()
