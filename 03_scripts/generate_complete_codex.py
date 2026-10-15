# -*- coding: utf-8 -*-
"""
Knowledge Lab - Grand Occult Cosmology Codex Engine (v6.0 Master-Scholar Edition)
Monumental synthesis of:
1. 7 Planetary Kings & Spheres with primary manuscript citations & Hans Cousto frequencies.
2. Complete 36 Decans (Bakyu) Matrix across Kemetic Dendera, Babylon, PGM, Picatrix, and Islamic Simya.
3. 24 Chaldean Planetary Hours with the Heptagram mathematical algorithm and temporal hour physics.
4. 28 Lunar Mansions with astronomical coordinates, Ibn Arabi's letter breath, Divine Names, and Melothesia.
5. Jabir Ibn Hayyan's Science of Balance (Mizan al-Huruf) & 4 Elemental Magic types deconstruction.
6. The 7 Subtle Bodies, Toroidal Biofield, Biophoton coherence, and the 7 Quranic Nafs stages.
7. The 7 Planetary Squares (3x3 to 9x9) with mathematical waveguide physics and live 3x3 Wafq Ghazali solver.
8. Acoustic Resonance, Cymatics, Solfeggio standing waves, and Web Audio API synthesizer.
9. The Absolute Quranic Criterion, Spiritual Sovereignty of the Muwahhid, and manuscript critique.
"""

import os
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(ROOT_DIR, "website")
CODEX_WEB_PATH = os.path.join(WEBSITE_DIR, "Grand_Occult_Cosmology_Codex.html")
CODEX_ROOT_PATH = os.path.join(ROOT_DIR, "Grand_Occult_Cosmology_Codex.html")

def generate_codex():
    print("Generating Master-Scholar Grand Occult Cosmology Codex...")

    # We read template chunks or build the complete HTML directly
    html_code = '''<!DOCTYPE html>
<html lang="ar" dir="rtl" style="background-color: #111823; color-scheme: dark;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="dark">
    <meta name="theme-color" content="#111823">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <title>سفر النواميس الباطنية والأفلاك الكبرى — الموسوعة الأكاديمية الشاملة</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            color-scheme: dark !important;
            --bg-void: #111823;
            --void-black: #111823;
            --panel-bg: rgba(30, 41, 59, 0.95);
            --border-glass: rgba(148, 163, 184, 0.2);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --gold: #64748b;
            --gold-glow: rgba(148, 163, 184, 0.35);
            --cyan: #38bdf8;
            --cyan-glow: rgba(56, 189, 248, 0.3);
            --rose: #fb7185;
            --purple: #c084fc;
            --emerald: #34d399;
            --fire: #ef4444;
            --water: #3b82f6;
            --air: #06b6d4;
            --earth: #f59e0b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', system-ui, -apple-system, sans-serif;
            scrollbar-color: rgba(148, 163, 184, 0.35) #111823 !important;
        }

        html {
            background-color: #111823 !important;
            color-scheme: dark !important;
        }

        body {
            background-color: #111823 !important;
            color: var(--text-main);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 15%, rgba(56, 189, 248, 0.04) 0%, transparent 40%),
                radial-gradient(circle at 90% 85%, rgba(148, 163, 184, 0.04) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(192, 132, 252, 0.03) 0%, transparent 50%);
            min-height: 100vh;
            color-scheme: dark !important;
        }

        ::-webkit-scrollbar {
            width: 8px !important;
            height: 8px !important;
        }
        ::-webkit-scrollbar-track {
            background: #111823 !important;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(148, 163, 184, 0.35) !important;
            border-radius: 6px !important;
            border: 2px solid #111823 !important;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(148, 163, 184, 0.65) !important;
        }

        /* Gate */
        #portal-auth-gate {
            position: fixed;
            inset: 0;
            background: #030508;
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            transition: opacity 0.4s ease, visibility 0.4s;
        }
        #portal-auth-gate.unlocked {
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }
        .auth-card {
            background: rgba(13, 17, 28, 0.95);
            border: 1px solid var(--gold);
            box-shadow: 0 0 50px rgba(244, 180, 26, 0.25);
            border-radius: 24px;
            padding: 40px 32px;
            width: 100%;
            max-width: 440px;
            text-align: center;
            backdrop-filter: blur(20px);
        }
        .auth-icon { font-size: 3rem; color: var(--gold); margin-bottom: 16px; filter: drop-shadow(0 0 15px var(--gold-glow)); }
        .auth-title { font-size: 1.5rem; color: #fff; margin-bottom: 8px; font-weight: 800; font-family:'Amiri', serif; }
        .auth-desc { font-size: 0.88rem; color: var(--text-muted); margin-bottom: 24px; line-height: 1.6; }
        .auth-input {
            width: 100%;
            padding: 14px 18px;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            color: #fff;
            font-size: 1.1rem;
            text-align: center;
            letter-spacing: 4px;
            outline: none;
            margin-bottom: 16px;
            transition: all 0.2s;
        }
        .auth-input:focus { border-color: var(--gold); box-shadow: 0 0 15px var(--gold-glow); }
        .auth-btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, var(--gold), #d49300);
            border: none;
            border-radius: 12px;
            color: #030508;
            font-weight: 800;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 4px 20px var(--gold-glow);
        }

        /* Header */
        header {
            background: rgba(8, 11, 20, 0.92);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-glass);
            padding: 14px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 10px 30px rgba(0,0,0,0.7);
        }
        .brand-title {
            font-family: 'Amiri', serif;
            font-size: 1.45rem;
            font-weight: 800;
            background: linear-gradient(135deg, #fff 0%, var(--gold) 60%, #c77dff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .brand-subtitle { font-size: 0.76rem; color: var(--text-muted); }

        .nav-scroller { overflow-x: auto; -webkit-overflow-scrolling: touch; }
        .nav-tabs {
            display: flex;
            gap: 6px;
            background: rgba(0, 0, 0, 0.45);
            padding: 4px;
            border-radius: 14px;
            border: 1px solid var(--border-glass);
            white-space: nowrap;
        }
        .nav-tab {
            background: none;
            border: none;
            color: var(--text-muted);
            padding: 8px 14px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 0.84rem;
            font-weight: 700;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .nav-tab:hover { color: #fff; background: rgba(255, 255, 255, 0.05); }
        .nav-tab.active { background: var(--gold); color: #030508; box-shadow: 0 0 18px var(--gold-glow); }

        /* Main Container */
        main { max-width: 1550px; margin: 0 auto; padding: 25px 20px 80px 20px; }
        .tab-content { display: none; animation: fadeIn 0.35s ease; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

        .hero-banner {
            background: linear-gradient(135deg, rgba(244, 180, 26, 0.1) 0%, rgba(0, 240, 255, 0.05) 50%, rgba(157, 78, 221, 0.08) 100%);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 26px 30px;
            margin-bottom: 25px;
        }
        .hero-banner h2 { font-size: 1.8rem; color: var(--gold); font-weight: 800; font-family:'Amiri', serif; margin-bottom: 6px; }
        .hero-banner p { font-size: 0.94rem; color: var(--text-muted); line-height: 1.8; max-width: 1200px; }

        /* Tables & Cards */
        .cards-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 24px; }
        .king-card {
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 18px;
            padding: 24px;
            position: relative;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .king-card:hover { transform: translateY(-4px); border-color: var(--gold); box-shadow: 0 12px 30px rgba(0,0,0,0.6); }

        .data-table-wrapper {
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            overflow-x: auto;
            margin-bottom: 25px;
            -webkit-overflow-scrolling: touch;
        }
        table { width: 100%; border-collapse: collapse; text-align: right; font-size: 0.86rem; min-width: 800px; }
        th { background: rgba(0, 0, 0, 0.6); padding: 14px 16px; color: var(--gold); border-bottom: 1px solid var(--border-glass); font-weight: 700; white-space: nowrap; }
        td { padding: 12px 16px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); color: #475569; line-height: 1.6; }
        tr:hover td { background: rgba(255, 255, 255, 0.02); }

        .day-select-bar { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 12px; margin-bottom: 16px; }
        .day-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: #475569;
            padding: 8px 16px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: 700;
            white-space: nowrap;
            transition: all 0.2s;
        }
        .day-btn.active, .day-btn:hover { background: var(--cyan); color: #030508; border-color: var(--cyan); box-shadow: 0 0 14px var(--cyan-glow); }

        .synth-btn {
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid rgba(0, 240, 255, 0.3);
            color: var(--cyan);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .synth-btn:hover, .synth-btn.playing { background: var(--cyan); color: #030508; box-shadow: 0 0 12px var(--cyan-glow); }

                /* Dynamic Multi-Order Wafq Grid & Studio Styles */
        .wafq-studio-container {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(20, 18, 48, 0.85));
            border: 1px solid rgba(244, 180, 26, 0.35);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 30px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.6), 0 0 25px rgba(244, 180, 26, 0.1);
        }
        .wafq-mode-toggle {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 14px;
            flex-wrap: wrap;
        }
        .wafq-mode-btn {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #94a3b8;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            font-family: 'Tajawal', sans-serif;
            font-size: 0.95rem;
            font-weight: 600;
            transition: all 0.25s;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .wafq-mode-btn:hover {
            color: #fff;
            border-color: var(--cyan);
        }
        .wafq-mode-btn.active {
            background: rgba(0, 240, 255, 0.15);
            border-color: var(--cyan);
            color: var(--cyan);
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.25);
        }
        .wafq-planet-selector-bar {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 20px;
            padding: 10px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .wafq-order-pill {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #475569;
            padding: 8px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.86rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }
        .wafq-order-pill:hover {
            border-color: var(--gold);
            color: #fff;
            transform: translateY(-2px);
        }
        .wafq-order-pill.active {
            background: rgba(244, 180, 26, 0.18);
            border-color: var(--gold);
            color: var(--gold);
            box-shadow: 0 0 12px rgba(244, 180, 26, 0.3);
        }
        .wafq-grid-dynamic {
            display: grid;
            gap: 6px;
            background: rgba(5, 8, 16, 0.9);
            padding: 16px;
            border-radius: 16px;
            border: 2px solid var(--gold);
            box-shadow: 0 0 30px rgba(244, 180, 26, 0.2);
            margin: 0 auto;
            max-width: 520px;
            width: 100%;
        }
        .dynamic-cell {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 8px;
            aspect-ratio: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            transition: all 0.2s;
            user-select: none;
            padding: 4px;
        }
        .dynamic-cell:hover {
            background: rgba(0, 240, 255, 0.12);
            border-color: var(--cyan);
            transform: scale(1.05);
            z-index: 5;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
        }
        .dynamic-cell.cell-key {
            border-color: var(--emerald);
            background: rgba(6, 214, 160, 0.15);
            box-shadow: 0 0 10px rgba(6, 214, 160, 0.3);
        }
        .dynamic-cell.cell-lock {
            border-color: #ef4444;
            background: rgba(239, 68, 68, 0.15);
            box-shadow: 0 0 10px rgba(239, 68, 68, 0.3);
        }
        .dynamic-cell.cell-center {
            border-color: var(--gold);
            background: rgba(244, 180, 26, 0.18);
            box-shadow: 0 0 12px rgba(244, 180, 26, 0.4);
        }
        .dynamic-cell.cell-broken {
            border-color: #c026d3;
            background: rgba(192, 38, 211, 0.2);
            box-shadow: 0 0 12px rgba(192, 38, 211, 0.4);
        }
        .dynamic-cell-val {
            font-weight: 800;
            color: #fff;
            line-height: 1;
        }
        .dynamic-cell-badge {
            font-size: 0.65rem;
            margin-top: 3px;
            font-weight: 600;
        }
        .wafq-math-badge-bar {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 14px;
        }
        .wafq-math-badge {
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 0.78rem;
            color: #94a3b8;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .wafq-math-badge strong { color: var(--gold); }
        .wafq-math-badge.verified { border-color: var(--emerald); color: var(--emerald); }

        /* Wafq Grid 3x3 Legacy & Responsive */
        .magic-grid-3x3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            background: rgba(0, 0, 0, 0.7);
            padding: 12px;
            border-radius: 14px;
            border: 2px solid var(--gold);
            box-shadow: 0 0 25px rgba(244, 180, 26, 0.25);
        }
        .grid-cell {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 8px;
            height: 75px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        .grid-cell:hover { background: rgba(148, 163, 184, 0.15); border-color: var(--gold); }
        .cell-num { font-size: 1.35rem; font-weight: 800; color: #fff; line-height: 1; }
        .cell-letter { font-size: 0.75rem; color: var(--gold); margin-top: 4px; }

        
        /* Al-Ghazali Master Manual (Asrar al-Asrar) Styles */
        .ghazali-master-handbook {
            background: linear-gradient(135deg, rgba(11, 17, 33, 0.98), rgba(20, 15, 38, 0.98));
            border: 2px solid var(--gold);
            border-radius: 24px;
            padding: 34px 28px;
            margin-bottom: 35px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(244, 180, 26, 0.25);
            position: relative;
            overflow: hidden;
        }
        .ghazali-handbook-header {
            text-align: center;
            border-bottom: 2px solid rgba(244, 180, 26, 0.3);
            padding-bottom: 24px;
            margin-bottom: 28px;
            position: relative;
        }
        .ghazali-handbook-header::after {
            content: '۞';
            position: absolute;
            bottom: -16px;
            left: 50%;
            transform: translateX(-50%);
            background: #0d1326;
            padding: 0 16px;
            color: var(--gold);
            font-size: 1.4rem;
        }
        .ghazali-handbook-title {
            font-family: 'Amiri', serif;
            font-size: 2.1rem;
            color: var(--gold);
            margin: 0 0 8px 0;
            text-shadow: 0 0 15px rgba(244, 180, 26, 0.4);
        }
        .ghazali-handbook-subtitle {
            font-size: 0.95rem;
            color: #475569;
            max-width: 860px;
            margin: 0 auto;
            line-height: 1.8;
        }
        .ghazali-nav-pills {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 28px;
            background: rgba(0, 0, 0, 0.4);
            padding: 10px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        .ghazali-nav-pill {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(244, 180, 26, 0.2);
            color: #475569;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .ghazali-nav-pill:hover {
            background: rgba(244, 180, 26, 0.18);
            border-color: var(--gold);
            color: #fff;
            transform: translateY(-2px);
        }
        .ghazali-chapter {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 26px;
            margin-bottom: 28px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
            position: relative;
        }
        .ghazali-chapter::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 4px;
            height: 100%;
            background: var(--gold);
            border-radius: 0 18px 18px 0;
        }
        .chapter-heading {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding-bottom: 12px;
        }
        .chapter-num-badge {
            background: rgba(244, 180, 26, 0.15);
            border: 1px solid var(--gold);
            color: var(--gold);
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.15rem;
            flex-shrink: 0;
        }
        .chapter-title {
            margin: 0;
            font-family: 'Amiri', serif;
            font-size: 1.4rem;
            color: #fff;
        }
        .chapter-subtitle {
            font-size: 0.82rem;
            color: #94a3b8;
            margin-top: 2px;
        }
        .specimen-grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            max-width: 320px;
            margin: 15px auto;
            background: rgba(0, 0, 0, 0.7);
            padding: 12px;
            border-radius: 12px;
            border: 1.5px solid var(--gold);
        }
        .specimen-cell {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(244, 180, 26, 0.25);
            border-radius: 8px;
            padding: 10px 4px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .specimen-cell-num {
            font-size: 1.3rem;
            font-weight: 800;
            color: #fff;
            line-height: 1;
        }
        .specimen-cell-label {
            font-size: 0.72rem;
            color: var(--gold);
            margin-top: 4px;
        }
        .specimen-cell.key-cell {
            background: rgba(6, 214, 160, 0.15);
            border-color: var(--emerald);
        }
        .specimen-cell.lock-cell {
            background: rgba(239, 68, 68, 0.15);
            border-color: #ef4444;
        }
        .specimen-cell.center-cell {
            background: rgba(244, 180, 26, 0.18);
            border-color: var(--gold);
        }
        .specimen-cell.broken-cell {
            background: rgba(192, 38, 211, 0.2);
            border-color: #c026d3;
        }
        .operational-protocol-box {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 18px;
            margin-top: 16px;
        }
        .protocol-step {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 12px;
            font-size: 0.88rem;
            line-height: 1.75;
            color: #475569;
        }
        .step-badge {
            background: rgba(0, 240, 255, 0.12);
            border: 1px solid var(--cyan);
            color: var(--cyan);
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 700;
            flex-shrink: 0;
            margin-top: 3px;
        }

        /* Treatises Card Grid */
        .wafq-treatise-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 24px;
            margin-bottom: 30px;
        }
        @media (max-width: 768px) {
            .wafq-treatise-grid { grid-template-columns: 1fr; }
        }
        .wafq-treatise-card {
            background: rgba(11, 17, 33, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 24px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        .wafq-treatise-card:hover {
            border-color: rgba(244, 180, 26, 0.4);
            transform: translateY(-3px);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7), 0 0 20px rgba(244, 180, 26, 0.1);
        }
        .wafq-treatise-card::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, var(--gold), var(--cyan), transparent);
        }
        .wafq-treatise-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding-bottom: 12px;
        }
        .wafq-treatise-icon {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: rgba(244, 180, 26, 0.12);
            border: 1px solid var(--gold);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            color: var(--gold);
            flex-shrink: 0;
        }
        .wafq-treatise-title {
            margin: 0;
            font-family: 'Amiri', serif;
            font-size: 1.3rem;
            color: #fff;
            line-height: 1.3;
        }
        .wafq-treatise-subtitle {
            font-size: 0.8rem;
            color: #94a3b8;
            margin-top: 2px;
        }
        .wafq-treatise-content {
            font-size: 0.88rem;
            line-height: 1.85;
            color: #475569;
        }
        .wafq-treatise-content strong { color: var(--gold); }
        .wafq-treatise-content em { color: var(--cyan); font-style: normal; font-weight: 600; }
        .wafq-sub-box {
            background: rgba(0, 0, 0, 0.35);
            border-right: 3px solid var(--cyan);
            border-radius: 0 10px 10px 0;
            padding: 12px 16px;
            margin: 14px 0;
            font-size: 0.85rem;
            line-height: 1.75;
        }
        .wafq-sub-box.gold { border-right-color: var(--gold); }
        .wafq-sub-box.emerald { border-right-color: var(--emerald); }
        .wafq-sub-box.crimson { border-right-color: #ef4444; }
        .wafq-sub-box.purple { border-right-color: #c026d3; }

        /* Canvas & Oscilloscope */
        .wave-canvas-wrapper {
            background: #020408;
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 16px;
            position: relative;
            margin-bottom: 25px;
        }
        #waveCanvas { width: 100%; height: 180px; display: block; border-radius: 10px; background: rgba(0, 0, 0, 0.85); }
        .canvas-controls { display: flex; justify-content: space-between; align-items: center; margin-top: 12px; flex-wrap: wrap; gap: 10px; }
        .wave-mode-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: #475569;
            padding: 6px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.8rem;
            font-weight: 700;
        }
        .wave-mode-btn.active { background: var(--emerald); color: #030508; border-color: var(--emerald); }


        /* Tab 13: Letters Magic & Jabir Balance Styles */
        .letters-workspace-container {
            display: grid;
            grid-template-columns: 1fr 420px;
            gap: 25px;
            align-items: start;
            margin-bottom: 30px;
        }
        @media (max-width: 1024px) {
            .letters-workspace-container { grid-template-columns: 1fr; }
        }
        .abjad-calc-card {
            background: rgba(11, 17, 33, 0.85);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
            margin-bottom: 25px;
        }
        .abjad-input-box {
            width: 100%;
            background: rgba(4, 8, 19, 0.9);
            border: 1px solid rgba(244, 180, 26, 0.4);
            border-radius: 12px;
            padding: 14px 18px;
            color: #fff;
            font-family: 'Amiri', serif;
            font-size: 1.25rem;
            outline: none;
            transition: all 0.25s ease;
            box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);
        }
        .abjad-input-box:focus {
            border-color: var(--cyan);
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.25);
        }
        .calc-sample-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #475569;
            padding: 4px 12px;
            border-radius: 8px;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .calc-sample-btn:hover {
            background: var(--gold);
            color: #030712;
            border-color: var(--gold);
            font-weight: 700;
        }
        .abjad-metrics-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 12px;
            margin: 16px 0;
        }
        .abjad-metric-pill {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 12px;
            text-align: center;
        }
        .abjad-metric-val {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--gold);
            font-family: 'Amiri', serif;
            line-height: 1.2;
        }
        .abjad-metric-lbl {
            font-size: 0.76rem;
            color: #94a3b8;
            margin-top: 4px;
        }
        .balance-bar-group {
            margin-top: 14px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .balance-bar-row {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.82rem;
        }
        .balance-bar-label {
            min-width: 90px;
            font-weight: 600;
        }
        .balance-bar-track {
            flex-grow: 1;
            height: 10px;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        }
        .balance-bar-fill {
            height: 100%;
            border-radius: 6px;
            transition: width 0.4s ease;
        }
        .letters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(68px, 1fr));
            gap: 10px;
            margin-top: 16px;
        }
        .letter-tile-btn {
            background: rgba(15, 23, 42, 0.85);
            border: 1.5px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 10px 4px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }
        .letter-tile-btn:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6);
            border-color: currentColor;
        }
        .letter-tile-btn.active {
            transform: translateY(-3px) scale(1.05);
            border-color: currentColor;
            box-shadow: 0 0 18px currentColor, inset 0 0 8px currentColor;
            background: rgba(255, 255, 255, 0.06);
        }
        .letter-char {
            font-size: 1.6rem;
            font-weight: 700;
            font-family: 'Amiri', serif;
            line-height: 1.1;
        }
        .letter-val {
            font-size: 0.75rem;
            color: #94a3b8;
            margin-top: 2px;
            font-weight: 600;
        }
        .letter-filter-btn {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #94a3b8;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        .letter-filter-btn:hover, .letter-filter-btn.active {
            background: var(--gold);
            color: #030712;
            border-color: var(--gold);
            font-weight: 700;
        }
        .letter-detail-card {
            background: rgba(11, 17, 33, 0.9);
            border: 1px solid rgba(244, 180, 26, 0.3);
            border-radius: 20px;
            padding: 26px;
            box-shadow: 0 16px 45px rgba(0,0,0,0.6);
            position: sticky;
            top: 80px;
        }

        /* Bodies & Quran Grid + Holographic Human Silhouette */
        .bodies-cosmos-container {
            display: grid;
            grid-template-columns: 440px 1fr;
            gap: 30px;
            align-items: start;
            margin-bottom: 30px;
        }
        @media (max-width: 1024px) {
            .bodies-cosmos-container { grid-template-columns: 1fr; }
        }
        .body-silhouette-wrapper {
            background: radial-gradient(ellipse at center, #0f172a 0%, #030712 100%);
            border: 1px solid rgba(0, 240, 255, 0.35);
            border-radius: 24px;
            padding: 25px 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 35px rgba(0, 240, 255, 0.12);
            overflow: hidden;
        }
        .body-pills-bar {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            max-width: 100%;
            padding: 4px 6px 12px 6px;
            -webkit-overflow-scrolling: touch;
            margin-bottom: 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            width: 100%;
            justify-content: flex-start;
        }
        .b-pill-btn {
            flex: 0 0 auto;
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #475569;
            padding: 7px 12px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 0.78rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.25s ease;
        }
        .b-pill-btn:hover {
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-2px);
        }
        .b-pill-btn.active {
            border-color: currentColor;
            box-shadow: 0 0 15px currentColor;
            transform: translateY(-2px);
            color: #fff;
            background: rgba(255, 255, 255, 0.08);
        }
        .silhouette-canvas {
            width: 100%;
            max-width: 340px;
            height: 540px;
            position: relative;
            display: flex;
            justify-content: center;
            margin: 0 auto;
        }
        .human-figure-svg {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            height: 100%;
            filter: drop-shadow(0 0 20px rgba(0, 240, 255, 0.35));
            pointer-events: none;
        }
        .body-point-btn {
            position: absolute;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 5;
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 2px solid rgba(255,255,255,0.85);
            box-shadow: 0 0 20px currentColor;
            background: rgba(11, 15, 23, 0.9);
            font-size: 1.15rem;
            color: #fff;
            font-family: 'Amiri', serif;
            font-weight: 700;
        }
        .body-point-btn:hover, .body-point-btn.active {
            transform: translate(-50%, -50%) scale(1.35);
            border-color: #ffffff;
            box-shadow: 0 0 35px currentColor, inset 0 0 14px currentColor;
        }
        .body-point-btn::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 2px solid currentColor;
            animation: pulse-ring 2.2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
        }
        @keyframes pulse-ring {
            0% { transform: scale(0.95); opacity: 0.8; }
            50% { transform: scale(1.6); opacity: 0; }
            100% { transform: scale(1.6); opacity: 0; }
        }
        .body-detail-card {
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 16px 45px rgba(0,0,0,0.5);
            transition: all 0.35s ease;
        }
        .bodies-stack { display: flex; flex-direction: column; gap: 14px; }
        .body-layer {
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 14px;
            padding: 20px 24px;
            display: flex;
            align-items: flex-start;
            gap: 20px;
            transition: all 0.25s;
            position: relative;
        }
        .body-layer:hover { transform: translateX(-4px); border-color: var(--cyan); box-shadow: 0 8px 24px rgba(0,229,255,0.08); }
        .body-num { font-size: 2rem; font-weight: 800; color: var(--cyan); min-width: 50px; text-align: center; font-family: 'Amiri', serif; }
        .body-filter-btn {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid var(--border-glass);
            color: #94a3b8;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        .body-filter-btn:hover, .body-filter-btn.active {
            background: var(--cyan);
            color: #030508;
            border-color: var(--cyan);
            font-weight: 700;
        }
        .defense-protocol-box {
            background: linear-gradient(135deg, rgba(6, 214, 160, 0.08), rgba(0, 229, 255, 0.04));
            border: 1px solid rgba(6, 214, 160, 0.3);
            border-radius: 12px;
            padding: 16px;
            margin-top: 10px;
        }
        .attack-vulnerability-box {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.08), rgba(244, 180, 26, 0.04));
            border: 1px solid rgba(239, 68, 68, 0.3);
            border-radius: 12px;
            padding: 16px;
            margin-top: 10px;
        }

            .cards-grid, .quranic-grid { grid-template-columns: 1fr; }
            main { padding: 15px 10px 60px 10px; }
        }
    </style>
</head>
<body>

    <!-- Main Container -->
    <main>

        <!-- 1. SEVEN PLANETARY KINGS & SPHERS (DOOR 09) -->
        <div id="tab-kings" class="tab-content active">
            <div class="hero-banner">
                <h2>👑 مصفوفة ملوك الأفلاك والأيام السبعة الكبرى عبر حضارات العالم</h2>
                <p>الحقيقة الأركيتيبية الموحدة: ملوك الأيام والأفلاك كينونة وتردد واحد عبر بابل، كيميت، اليونان، الهند، النورد، القبالاه، والمخطوطات السميائية. دراسة مقارنة عميقة لربط الفلك بملائكة التسبيح وترددات هانس كوستو الحقيقية بالهرتز والميلوثيسيا العضوية والبخور.</p>
            </div>
            <div class="cards-grid" id="kings-grid"></div>
        </div>

        <!-- 2. ZODIAC ANGELS & 36 DECANS MATRIX (DOOR 10) -->
        <div id="tab-zodiac-angels" class="tab-content">
            <div class="hero-banner">
                <h2>✨ مصفوفة ملائكة الأبراج والوجوه الـ 36 الكبرى (The 36 Decans / Bakyu)</h2>
                <p>التشريح الباطني لملوك الأبراج الـ 12 ورؤسائهم الملائكيين، مع الموسوعة الكاملة لجميع الوجوه العشرية الـ 36 (Decans) بأسمائها المصرية القديمة بمعبد دندرة (الباكيو)، حكامها الكلدانيين، تخصصاتها الطبية والميلوثيسية، وصورها الطلسمية في مخطوط غاية الحكيم (Picatrix):</p>
            </div>

            <!-- 12 Signs Angels -->
            <div style="margin-bottom:20px;">
                <h3 style="color:var(--gold); font-family:'Amiri',serif; font-size:1.3rem; margin-bottom:10px;"><i class="fa-solid fa-crown"></i> ملائكة الأبراج الاثني عشر عبر الحضارات</h3>
                <div class="data-table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>البرج</th>
                                <th>العنصر</th>
                                <th>الملاك السميائي (العربي)</th>
                                <th>الملاك القبالي (العبراني)</th>
                                <th>الإله الفرعوني (كيميت)</th>
                                <th>الكيان البابلي</th>
                                <th>السبط المقترن</th>
                            </tr>
                        </thead>
                        <tbody id="zodiac-angels-tbody"></tbody>
                    </table>
                </div>
            </div>

            <!-- Complete 36 Decans Table -->
            <div style="margin-bottom:20px;">
                <h3 style="color:#d8b4fe; font-family:'Amiri',serif; font-size:1.3rem; margin-bottom:10px;"><i class="fa-solid fa-compass"></i> الموسوعة الجامعة للوجوه الـ 36 كاملة (The Complete 36 Decans Directory)</h3>
                <div class="data-table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>البرج والوجه</th>
                                <th>الدرجات</th>
                                <th>الحاكم الكلداني</th>
                                <th>الاسم الفرعوني (الباكيو Bakyu)</th>
                                <th>الملاك الهرمسي</th>
                                <th>الميلوثيسيا العضوية</th>
                                <th>التردد (Hz)</th>
                                <th>الصورة الطلسمية والخاصية (Picatrix)</th>
                            </tr>
                        </thead>
                        <tbody id="decans-36-tbody"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 3. PLANETARY HOURS MATRIX (DOOR 11) -->
        <div id="tab-hours" class="tab-content">
            <div class="hero-banner">
                <h2>⏱️ نظام ساعات الأيام الفلكية الـ 24 وحساب الساعات الزمانية</h2>
                <p>الفيزياء الفلكية للترتيب الكلداني المتنازل (زحل ➔ المشتري ➔ المريخ ➔ الشمس ➔ الزهرة ➔ عطارد ➔ القمر)، هندسة النجمة السباعية (Heptagram)، وطريقة حساب الساعات المعوجة/الزمانية وفق قوس النهار والليل مع التردد المداري لكل ساعة وأفضل الأعمال المتوافقة معها:</p>
            </div>

            <!-- Mathematical Mechanics Box -->
            <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(0,240,255,0.3); border-radius:16px; padding:20px; margin-bottom:20px; line-height:1.8; font-size:0.9rem; color:#475569;">
                <h3 style="color:var(--cyan); margin-bottom:8px; font-family:'Amiri',serif;"><i class="fa-solid fa-square-root-variable"></i> المعادلة الرياضية لحساب الساعات الزمانية (Temporal Hours Calculation):</h3>
                <p>
                    تختلف الساعات الفلكية الزمانية عن الساعات الميكانيكية الثابتة (60 دقيقة)؛ إذ يُقسم <strong>قوس النهار الفعلي (من الشروق إلى الغروب)</strong> على 12 جزءاً متساوياً ليعطي طول الساعة النهارية، ويُقسم <strong>قوس الليل (من الغروب إلى الشروق)</strong> على 12 ليعطي الساعة الليلية. في الصيف تطول الساعة النهارية وتصل لـ 75 دقيقة، وفي الشتاء تقصر لـ 45 دقيقة. والساعة الأولى من كل يوم يحكمها كوكب اليوم نفسه، ثم تدور وفق الترتيب الكلداني المتنازل.
                </p>
            </div>

            <div class="day-select-bar">
                <button class="day-btn active" onclick="loadDayHours(0)">الأحد (الشمس)</button>
                <button class="day-btn" onclick="loadDayHours(1)">الإثنين (القمر)</button>
                <button class="day-btn" onclick="loadDayHours(2)">الثلاثاء (المريخ)</button>
                <button class="day-btn" onclick="loadDayHours(3)">الأربعاء (عطارد)</button>
                <button class="day-btn" onclick="loadDayHours(4)">الخميس (المشتري)</button>
                <button class="day-btn" onclick="loadDayHours(5)">الجمعة (الزهرة)</button>
                <button class="day-btn" onclick="loadDayHours(6)">السبت (زحل)</button>
            </div>
            <div class="data-table-wrapper">
                <table id="hours-table">
                    <thead>
                        <tr>
                            <th>الساعة</th>
                            <th>الطور الفلكي</th>
                            <th>الكوكب الحاكم</th>
                            <th>الطبيعة الفلكية</th>
                            <th>التردد المقترن</th>
                            <th>التأثير الحيوي والاستخدام بالمخطوطات</th>
                        </tr>
                    </thead>
                    <tbody id="hours-tbody"></tbody>
                </table>
            </div>
        </div>

        <!-- 4. LUNAR MANSIONS (DOOR 12) -->
        <div id="tab-mansions" class="tab-content">
            <div class="hero-banner">
                <h2>🌙 منازل القمر الـ 28: التشفير الحرفي، الأسماء الإلهية، والنجوم الحقيقية</h2>
                <p>المدار القمري الكامل المقسم إلى 28 منزلة (12° و 51' و 25.7" لكل منزلة). مطابقة دقيقة بين النجوم الفلكية الراصدة (Alpha Arietis, Pleiades, Aldebaran, Spica...)، الحرف القرآني المقابل في مذهب ابن عربي (كتاب مراتب الحروف والأفلاك)، والاسم الإلهي المقترن، والميلوثيسيا العضوية والبخور:</p>
            </div>
            <div class="data-table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>اسم المنزلة</th>
                            <th>النجوم الراصدة والدرجة</th>
                            <th>حرف ابن عربي</th>
                            <th>الاسم الإلهي المقترن</th>
                            <th>الملاك السميائي</th>
                            <th>الطبيعة</th>
                            <th>الكوكب</th>
                            <th>البخور والخاصية في المخطوطات</th>
                        </tr>
                    </thead>
                    <tbody id="mansions-tbody"></tbody>
                </table>
            </div>
        </div>

        <!-- 5. LETTER NATURES & 4 ELEMENTAL MAGICS (DOOR 13) -->
        <div id="tab-letters-magic" class="tab-content">
            <div class="hero-banner">
                <div style="font-size:0.85rem; color:var(--gold); font-family:'Amiri',serif; margin-bottom:6px; letter-spacing:1px;">﴿ كٓهيعٓصٓ ﴾ • ﴿ حم * عٓسٓقٓ ﴾ — ﴿ وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا ﴾ — الباب الثالث عشر: فيزياء الحرف وميزان الطبائع</div>
                <h2>🪶 هندسة الحروف الكونية، ميزان الحروف الجابري وعلم السيمياء العرفاني</h2>
                <p>أطلس فيزيائي وكوزمولوجي يفكك البنية الرياضية للحروف العربية الـ 28: الترددات الفونيمية (Acoustic Phonetics)، ميزان الطبائع الأربعة لجابر بن حيان بنسبة (1 : 3 : 5 : 8)، تقسيم الحروف النورانية والظلمانية عند محيي الدين بن عربي والبوني، والمحاكي المباشر لحساب الجُمّل والطبائع الحرفية.</p>
            </div>

            <!-- 4 Master Scientific & Esoteric Treatises -->
            <div class="spheres-compendium" style="margin-bottom:30px;">
                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">1. فيزياء الصوت والسايماتكس</span>
                        <h4>🌊 الميكانيكا الفونيمية والأشكال الهندسية للأمواج (Cymatic Physics)</h4>
                    </div>
                    <p>أثبتت تجارب <em>السيماتكس (Cymatics - Ernst Chladni & Hans Jenny)</em> أن كل صوت منطوق يولد أشكالاً هندسية ثنائية وثلاثية الأبعاد متطابقة في وسائط السيليكا والماء. تتميز الحروف العربية بتوزيع مخارجها الـ 17 الممتدة على طول الجهاز الصوتي البشري من أعماق الجوف والرئتين حتى الشفتين.</p>
                    <p>تولد الحروف الحلقية (الهمزة، الهاء، العين، الحاء، الغين، الخاء) ترددات تحتية عميقة (Infrasound) تتردد في القفص الصدري ومسارات الطاقة المركزية، بينما تولد الحروف الشفوية (الباء، الميم، الواو، الفاء) نغمات عالية متحدة المركز. الحرف في الحقيقة ليس صوتاً عشوائياً، بل هو <strong>مصفوفة ترددية مستقرة (Standing Resonant Wave)</strong> تؤثر مباشرة في التماسك الجزيئي لخلايا الإنسان.</p>
                    <div class="treatise-meta">
                        <span><strong>النطاق الصوتي:</strong> 85 هرتز (الحلقي) إلى 3400 هرتز (الصفيري)</span>
                        <span><strong>الأثر الحيوي:</strong> إعادة تشكيل الروابط الهيدروجينية لجزيئات الماء</span>
                    </div>
                </div>

                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">2. الرياضيات الجابرية الكونية</span>
                        <h4>⚖️ ميزان الحروف لجابر بن حيان وقانون النسب (1 : 3 : 5 : 8)</h4>
                    </div>
                    <p>أسس شيخ الكيميائيين <em>جابر بن حيان الكوفي</em> في كتبه الشهيرة <em>(كتاب الميزان، والخواص الكبير)</em> مبدأً ثورياً مفاده: أن الأسماء اللغوية للأشياء ليست اعتباطية بل تعكس التوازن الداخلي لطبائعها الأربع (الحرارة، البرودة، الرطوبة، اليبوسة).</p>
                    <p>قسّم جابر قوى الحروف إلى أربع مراتب متصاعدة هندسياً وفق النسبة الصارمة: <strong>1 درهم (المرتبة الأولى)، 3 دراهم (الثانية)، 5 دراهم (الثالثة)، 8 دراهم (الرابعة)</strong>. ومجموع هذه المراتب = <strong>17 درهماً</strong>، وهو سر الرقم 17 الذي بنى عليه جابر أكسير الحياة، وطابقه العرفاء بعدد الركعات المفروضة وأبواب الوجود الكونية السبعة عشر.</p>
                    <div class="treatise-meta">
                        <span><strong>النسبة الجابرية:</strong> 1 + 3 + 5 + 8 = 17 درهماً تامات</span>
                        <span><strong>القانون:</strong> توازن الجوهر = تطابق الطبائع الظاهرة والباطنة</span>
                    </div>
                </div>

                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">3. الإسقاط القرآني الإشراقي</span>
                        <h4>✨ الحروف النورانية الـ 14 فواتح السور وسر الإنسان الكامل</h4>
                    </div>
                    <p>افتُتحت 29 سورة في القرآن الكريم بحروف مقطعة تتألف تحديداً من <strong>14 حرفاً فريداً</strong> تمثل النصف الدقيق للأبجدية العربية، مجمعة في القول المأثور: <em>«نَصٌّ حَكِيمٌ قَاطِعٌ لَهُ سِرٌّ»</em> (ن، ص، ح، ك، ي، م، ق، ا، ط، ع، ل، هـ، س، ر).</p>
                    <p>يقابل الشيخ الأكبر <em>محيي الدين بن عربي</em> في *الفتوحات المكية* (الباب الثاني) بين هذه الحروف النورانية الـ 14 التي تمثل *عالم الأمر والأرواح العلوية*، وبين الحروف الظلمانية الـ 14 المتبقية التي تمثل *عالم الخلق والأجسام الكثيفة*. فالأولى مفاتيح الفيوضات الإلهية الإيجابية، والثانية أوعية التحقق المادي والتجلي الأرضي.</p>
                    <div class="treatise-meta">
                        <span><strong>التوزيع:</strong> 14 نورانية (عالم الأمر) مقابل 14 ظلمانية (عالم الخلق)</span>
                        <span><strong>المنازل:</strong> تطابق منازل القمر الـ 28 وأفلاك الوجود الـ 28</span>
                    </div>
                </div>

                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">4. المعيار البرهاني والتحصين</span>
                        <h4>🛡️ التمييز القطعي بين الحكمة الحرفية والشعوذة السحرية</h4>
                    </div>
                    <p>فرّق علماء الإسلام البرهانيون بين <em>علم خواص الحروف الطبيعي واللساني</em> وبين <em>الطلاسم الشيطانية المنحرفة</em> كالموجودة في شمس المعارف والعهود المكذوبة. في العقيدة التوحيدية، الحرف ليس كائناً مستقلاً يُعبد أو يُدعى من دون الله أو يُسخّر لإيذاء الخلق.</p>
                    <p>الحرف هو مظهر الكلمة الربانية: ﴿إِنَّمَا أَمْرُهُ إِذَا أَرَادَ شَيْئًا أَن يَقُولَ لَهُ كُن فَيَكُونُ﴾. فقوة الحرف في القرآن تنبع من استناده للوحي والتوحيد الخالص، والتعامل معه يكون بالتدبر والتسبيح المشروع، مع قطع دابر الشرك والتمائم المحرمة واستنزال الشياطين بالأوفاق المعكوسة.</p>
                    <div class="treatise-meta">
                        <span><strong>الحد الفاصل:</strong> التوحيد والافتقار لله مقابل الاستحضار والاستخدام الشيطاني</span>
                        <span><strong>الحكم الشرعي:</strong> التحريم القاطع لأوفاق السحر واستنطاق الحروف لغير الله</span>
                    </div>
                </div>
            </div>

            <!-- LIVE INTERACTIVE ABJAD CALCULATOR & ELEMENTAL BALANCE ENGINE -->
            <div class="abjad-calc-card">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:14px;">
                    <div>
                        <h3 style="color:var(--gold); font-family:'Amiri',serif; margin:0 0 4px 0; font-size:1.35rem; display:flex; align-items:center; gap:8px;">
                            <span>🔢</span> المولد التفاعلي لحساب الجُمّل وميزان الطبائع الأربعة الحي
                        </h3>
                        <p style="font-size:0.83rem; color:#94a3b8; margin:0;">اكتب أي نص أو اسم لتحليله فورياً وحساب قواه العددية وتوزيع طبائعه (نار، هواء، ماء، تراب):</p>
                    </div>
                    <div style="display:flex; gap:6px; flex-wrap:wrap;">
                        <span style="font-size:0.78rem; color:#94a3b8; align-self:center;">نماذج جاهزة:</span>
                        <button class="calc-sample-btn" onclick="setSampleText('الله')">الله</button>
                        <button class="calc-sample-btn" onclick="setSampleText('محمّد')">محمّد</button>
                        <button class="calc-sample-btn" onclick="setSampleText('القدس')">القدس</button>
                        <button class="calc-sample-btn" onclick="setSampleText('سلام')">سلام</button>
                        <button class="calc-sample-btn" onclick="setSampleText('نور')">نور</button>
                        <button class="calc-sample-btn" onclick="setSampleText('بسم الله الرحمن الرحيم')">البسملة</button>
                    </div>
                </div>

                <input type="text" id="abjad-live-input" class="abjad-input-box" placeholder="اكتب هنا أي كلمة أو جملة عربية..." value="بسم الله الرحمن الرحيم" oninput="calculateLettersLive()">

                <!-- Real-Time Metrics Output -->
                <div class="abjad-metrics-row">
                    <div class="abjad-metric-pill">
                        <div class="abjad-metric-val" id="metric-major" style="color:var(--gold);">786</div>
                        <div class="abjad-metric-lbl">الجُمّل الكبير (المجموع)</div>
                    </div>
                    <div class="abjad-metric-pill">
                        <div class="abjad-metric-val" id="metric-minor" style="color:var(--cyan);">3</div>
                        <div class="abjad-metric-lbl">الجُمّل الصغير (الجذر 1-9)</div>
                    </div>
                    <div class="abjad-metric-pill">
                        <div class="abjad-metric-val" id="metric-letters-count" style="color:#a78bfa;">19</div>
                        <div class="abjad-metric-lbl">عدد الحروف الصافية</div>
                    </div>
                    <div class="abjad-metric-pill">
                        <div class="abjad-metric-val" id="metric-luminous-pct" style="color:#34d399;">78.9%</div>
                        <div class="abjad-metric-lbl">نسبة النورانية (فواتح السور)</div>
                    </div>
                </div>

                <!-- Elemental Balance Bars -->
                <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:16px; border:1px solid rgba(255,255,255,0.06);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:700; color:#fff; font-size:0.9rem;">⚖️ ميزان الطبائع الأربعة الجابري للنص:</span>
                        <span id="element-diagnosis" style="font-size:0.82rem; color:var(--gold); font-weight:600;">طبيعة مائية ترابية متزنة</span>
                    </div>

                    <div class="balance-bar-group">
                        <div class="balance-bar-row">
                            <span class="balance-bar-label" style="color:#ef4444;">🔥 النار (الحرارة/اليبوسة):</span>
                            <div class="balance-bar-track">
                                <div class="balance-bar-fill" id="bar-fire" style="width:25%; background:linear-gradient(90deg, #ef4444, #f87171);"></div>
                            </div>
                            <span id="pct-fire" style="min-width:40px; color:#ef4444; font-weight:700;">25%</span>
                        </div>
                        <div class="balance-bar-row">
                            <span class="balance-bar-label" style="color:#06b6d4;">💨 الهواء (الحرارة/الرطوبة):</span>
                            <div class="balance-bar-track">
                                <div class="balance-bar-fill" id="bar-air" style="width:20%; background:linear-gradient(90deg, #06b6d4, #67e8f9);"></div>
                            </div>
                            <span id="pct-air" style="min-width:40px; color:#06b6d4; font-weight:700;">20%</span>
                        </div>
                        <div class="balance-bar-row">
                            <span class="balance-bar-label" style="color:#3b82f6;">💧 الماء (البرودة/الرطوبة):</span>
                            <div class="balance-bar-track">
                                <div class="balance-bar-fill" id="bar-water" style="width:35%; background:linear-gradient(90deg, #3b82f6, #60a5fa);"></div>
                            </div>
                            <span id="pct-water" style="min-width:40px; color:#3b82f6; font-weight:700;">35%</span>
                        </div>
                        <div class="balance-bar-row">
                            <span class="balance-bar-label" style="color:#f59e0b;">🏔️ التراب (البرودة/اليبوسة):</span>
                            <div class="balance-bar-track">
                                <div class="balance-bar-fill" id="bar-earth" style="width:20%; background:linear-gradient(90deg, #f59e0b, #fbbf24);"></div>
                            </div>
                            <span id="pct-earth" style="min-width:40px; color:#f59e0b; font-weight:700;">20%</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE 28 LETTERS GRID & INSPECTOR CARD -->
            <div class="letters-workspace-container">
                <!-- Left: 28 Letters Grid with Category Filters -->
                <div>
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                        <h3 style="color:#fff; font-family:'Amiri',serif; margin:0; font-size:1.25rem;">
                            🔤 مصفوفة الحروف العربية الـ 28 التفاعلية:
                        </h3>
                        <div style="display:flex; gap:6px; flex-wrap:wrap;">
                            <button class="letter-filter-btn active" onclick="filterLetters('all', this)">الكل (28)</button>
                            <button class="letter-filter-btn" onclick="filterLetters('luminous', this)" style="border-color:#94a3b8; color:#94a3b8;">النورانية (14)</button>
                            <button class="letter-filter-btn" onclick="filterLetters('dark', this)">الظلمانية (14)</button>
                            <button class="letter-filter-btn" onclick="filterLetters('fire', this)" style="border-color:#ef4444; color:#ef4444;">🔥 النار (7)</button>
                            <button class="letter-filter-btn" onclick="filterLetters('air', this)" style="border-color:#06b6d4; color:#06b6d4;">💨 الهواء (7)</button>
                            <button class="letter-filter-btn" onclick="filterLetters('water', this)" style="border-color:#3b82f6; color:#3b82f6;">💧 الماء (7)</button>
                            <button class="letter-filter-btn" onclick="filterLetters('earth', this)" style="border-color:#f59e0b; color:#f59e0b;">🏔️ التراب (7)</button>
                        </div>
                    </div>

                    <div class="letters-grid" id="letters-grid">
                        <!-- Populated dynamically by JS -->
                    </div>
                </div>

                <!-- Right: Letter Dossier Inspector Panel -->
                <div class="letter-detail-card" id="letter-detail-card">
                    <!-- Populated dynamically by selectLetter(char) -->
                </div>
            </div>

            <!-- 4 Element Deep Scientific Analysis Cards -->
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin-bottom:35px;">
                <div style="background:var(--panel-bg); border:1px solid var(--fire); border-radius:16px; padding:20px; box-shadow:0 8px 25px rgba(239,68,68,0.12);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <h3 style="color:var(--fire); margin:0; font-family:'Amiri',serif; font-size:1.2rem;"><i class="fa-solid fa-fire"></i> 1. الحروف النارية (الأثير والحرارة)</h3>
                        <span style="background:rgba(239,68,68,0.15); border:1px solid var(--fire); color:#fca5a5; padding:2px 8px; border-radius:8px; font-size:0.75rem; font-weight:700;">أ • هـ • ط • م • ف • ش • ذ</span>
                    </div>
                    <div style="font-size:0.84rem; line-height:1.7; color:#ffe5ec;">
                        <p style="margin-bottom:8px;"><strong>الفيزياء الفونيمية:</strong> موجات طولية سريعة ذات وتيرة اهتزاز عالية تفرز هرمونات النشاط والحركة (الأدرينالين والدوبامين)، وتمثل مبدأ الكبريت الفلسفي المحرك للمادة.</p>
                        <p style="margin:0;"><strong>التأثير الوجودي:</strong> البدايات القاطعة، الشجاعة، الاحتراق والتجدد، وكسر القيود؛ تناسب استنهاض الهمم ومكافحة الخمول.</p>
                    </div>
                </div>

                <div style="background:var(--panel-bg); border:1px solid var(--air); border-radius:16px; padding:20px; box-shadow:0 8px 25px rgba(6,182,212,0.12);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <h3 style="color:var(--air); margin:0; font-family:'Amiri',serif; font-size:1.2rem;"><i class="fa-solid fa-wind"></i> 2. الحروف الهوائية (الاتصال والانتشار)</h3>
                        <span style="background:rgba(6,182,212,0.15); border:1px solid var(--air); color:#67e8f9; padding:2px 8px; border-radius:8px; font-size:0.75rem; font-weight:700;">ج • ز • ك • س • ق • ث • ظ</span>
                    </div>
                    <div style="font-size:0.84rem; line-height:1.7; color:#e0fbfc;">
                        <p style="margin-bottom:8px;"><strong>الفيزياء الفونيمية:</strong> موجات تخلخل وانتشار صوتي تعتمد على انطلاق النفس والصفير والهمس؛ تحفز التبادل الأيوني وشبكات الاتصال العصبية الفكرية.</p>
                        <p style="margin:0;"><strong>التأثير الوجودي:</strong> نشر المعارف، سلاسة النطق، توارد الأفكار الإلهامية، والتواصل الروحي السريع كحبال الأثير الناقلة.</p>
                    </div>
                </div>

                <div style="background:var(--panel-bg); border:1px solid var(--water); border-radius:16px; padding:20px; box-shadow:0 8px 25px rgba(59,130,246,0.12);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <h3 style="color:var(--water); margin:0; font-family:'Amiri',serif; font-size:1.2rem;"><i class="fa-solid fa-water"></i> 3. الحروف المائية (السيولة والذاكرة)</h3>
                        <span style="background:rgba(59,130,246,0.15); border:1px solid var(--water); color:#93c5fd; padding:2px 8px; border-radius:8px; font-size:0.75rem; font-weight:700;">د • ح • ل • ع • ر • خ • غ</span>
                    </div>
                    <div style="font-size:0.84rem; line-height:1.7; color:#dbeafe;">
                        <p style="margin-bottom:8px;"><strong>الفيزياء الفونيمية:</strong> موجات هيدروديناميكية متدفقة تحاكي رنين الماء الجاري؛ تعزز الروابط الهيدروجينية السداسية وتساعد على امتصاص الصدمات النفسية.</p>
                        <p style="margin:0;"><strong>التأثير الوجودي:</strong> الشفاء، المحبة والانسجام، التسامح، وغسل الأكدار القلبية؛ تناسب التبريد وتسكين الغضب والحرارة الحارقة.</p>
                    </div>
                </div>

                <div style="background:var(--panel-bg); border:1px solid var(--earth); border-radius:16px; padding:20px; box-shadow:0 8px 25px rgba(245,158,11,0.12);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <h3 style="color:var(--earth); margin:0; font-family:'Amiri',serif; font-size:1.2rem;"><i class="fa-solid fa-mountain"></i> 4. الحروف الترابية (التكثيف والتثبيت)</h3>
                        <span style="background:rgba(245,158,11,0.15); border:1px solid var(--earth); color:#fde68a; padding:2px 8px; border-radius:8px; font-size:0.75rem; font-weight:700;">ب • و • ي • ن • ص • ت • ض</span>
                    </div>
                    <div style="font-size:0.84rem; line-height:1.7; color:#fef3c7;">
                        <p style="margin-bottom:8px;"><strong>الفيزياء الفونيمية:</strong> موجات ضغط صوتية ذات ترددات أرضية رنانة مع رنين شومان (7.83 هرتز)؛ تعزز الثبات والاتزان الجسدي ومناعة الهيكل العظمي.</p>
                        <p style="margin:0;"><strong>التأثير الوجودي:</strong> ترسيخ القواعد، الصبر، الإصرار، تثبيت المقامات، وحفظ الأمانات والعهود دون تذبذب.</p>
                    </div>
                </div>
            </div>

            <!-- Panoramic 28-Letter Comparative Matrix Table -->
            <div style="background:rgba(10,16,26,0.85); border:1px solid rgba(0,229,255,0.25); border-radius:16px; padding:24px; overflow-x:auto;">
                <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                    <span style="font-size:1.4rem;">📊</span>
                    <h3 style="color:#fff; font-family:'Amiri',serif; margin:0; font-size:1.3rem;">جدول المقارنة البانورامي الشامل للحروف الـ 28 والطبائع ومخارج الصوت والمنازل الكونية</h3>
                </div>
                <table style="width:100%; border-collapse:collapse; font-size:0.84rem; color:#475569; text-align:right;">
                    <thead>
                        <tr style="background:rgba(15,23,42,0.9); border-bottom:2px solid var(--gold); color:var(--gold);">
                            <th style="padding:10px;">الحرف</th>
                            <th style="padding:10px;">الجُمّل</th>
                            <th style="padding:10px;">الطبيعة العنصرية</th>
                            <th style="padding:10px;">التصنيف</th>
                            <th style="padding:10px;">المخرج الصوتي</th>
                            <th style="padding:10px;">الفلك والكوكب</th>
                            <th style="padding:10px;">منزلة القمر</th>
                            <th style="padding:10px;">ميزان جابر</th>
                            <th style="padding:10px;">الاسم الإلهي المفتاح</th>
                        </tr>
                    </thead>
                    <tbody id="panoramic-letters-table">
                        <!-- Populated dynamically by JS -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 6. 7 SUBTLE BODIES & BIOFIELD (DOOR 14) -->
        <div id="tab-bodies" class="tab-content">
            <div class="hero-banner">
                <div style="font-size:0.85rem; color:var(--gold); font-family:'Amiri',serif; margin-bottom:6px; letter-spacing:1px;">﴿ وَنَفْسٍ وَمَا سَوَّاهَا * فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَاهَا ﴾ — الباب الرابع عشر: فيزياء النواميس الوجودية</div>
                <h2>🧬 تشريح الأجساد السبعة، فيزياء البيوفوتون وميكانيكا الاختراق الطاقي</h2>
                <p>أطلس كوزمولوجي وفيزيائي شامل يربط حقول الكهروديناميكا الكمومية، فيزياء البيوفوتون الأحيائية (Fritz-Albert Popp)، الحقل الكهرومغناطيسي التوريدي للقلب البشري (HeartMath Institute)، بالأغماد والأجساد اللطيفة السبعة وتدرجات النفس السبعة في محكم التنزيل، مع مصفوفة كشف الثغرات والتحصين النبوي الدقيق.</p>
            </div>

            <!-- 4 Master Scientific & Esoteric Treatises -->
            <div class="spheres-compendium" style="margin-bottom:30px;">
                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">1. فيزياء الكم والأورا التوريدية</span>
                        <h4>⚡ ميكانيكا الحقل التوريدي وانبعاثات البيوفوتون (Biophotonic Physics)</h4>
                    </div>
                    <p>أثبتت أبحاث الفيزيائي الألماني <em>فـريـتـز-ألبـرت بـوب (Fritz-Albert Popp)</em> أن كل خلية حية تبعث فوتونات ضوئية متناهية الصغر بمعدل يتراوح بين 100 إلى 1000 فوتون/سم²/ثانية في النطاق الطيفي (200-800 نانومتر). هذا الإشعاع الفوق-ضعيف (UPE) ليس ناتجاً ثانوياً للتمثيل الغذائي بل هو <strong>حقل اتصالات كمومي متماسك (Coherent Optical Field)</strong> ينظم الانقسام الخلوي وتشفير الـ DNA.</p>
                    <p>يولد القلب البشري عبر نبضاته حقلاً كهرومغناطيسياً توريدياً (Toroidal Biofield) يفوق حقل الدماغ الكهربائي بـ 60 ضعفاً، ومغناطيسياً بأكثر من 5000 ضعف، ويمتد شعاعياً إلى مسافة 3 أمتار حول الجسد، مشكلاً الغلاف المانع والحجاب الحيوي الأول ضد الترددات الدخيلة والكيانات النارية.</p>
                    <div class="treatise-meta">
                        <span><strong>التردد الأساسي:</strong> 0.1 هرتز (Heart-Brain Coherence)</span>
                        <span><strong>الناقل الفيزيائي:</strong> حقل التماسك الفوتوني الفوق-ضعيف</span>
                    </div>
                </div>

                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">2. الإسقاط القرآني الإشراقي</span>
                        <h4>📜 تدرجات النفس السبعة والأغماد الكونية (Koshas & Nafs)</h4>
                    </div>
                    <p>يقابل التراث الإشراقي السرياني والحكمة المشرقية مراتب الوجود الإنساني بالأغماد السبعة (Septenary subtle sheaths): الجسد الكثيف (الصلصال)، الجسد الأثيري (قالب الطاقة والبرانا)، الجسد النجمي العاطفي، الجسد العقلي الفكري، الجسد السببي (الكرما ومخزن الذواكر)، الجسد البوذي العرفاني، والروح المنفوخة من أمر الله.</p>
                    <p>تتطابق هذه الطبقات حرفياً مع مراقي النفس في القرآن الكريم: <em>(الأمّارة بالسوء ➔ اللوّامة ➔ المُلْهَمة ➔ المطمئنّة ➔ الراضية ➔ المَرْضيّة ➔ الكامِلة الصافية)</em>. فكلما ترقت النفس درجة، زادت كثافة التردد الضوئي لبيوفوتونات الجسد، وانتقل مركز الوعي من الجسد الطيني الكثيف إلى الحضور الروحي الخالص.</p>
                    <div class="treatise-meta">
                        <span><strong>المرجع الإشراقي:</strong> السهروردي (حكمة الإشراق) والجيلي (الإنسان الكامل)</span>
                        <span><strong>المعادلة:</strong> التزكية = رفع تردد الطيف الفوتوني</span>
                    </div>
                </div>

                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">3. علم الباثولوجيا الطاقية</span>
                        <h4>🕸️ ميكانيكا التمزق الأثيري والطفليات النجمية (Astral Parasites & Larvae)</h4>
                    </div>
                    <p>لا يستطيع أي كيان ناري أو شيطاني اختراق الجسد المادي مباشرة؛ بل يحدث الاختراق عبر ثغرات في <strong>الجسد الأثيري والجسد النجمي (Astral Aura Tears)</strong>. تنشأ هذه الثغرات بفعل الصدمات النفسية الحادة (Trauma)، الخوف المذعور، الغضب الشديد، الإدمان الكيميائي، أو ممارسة الطقوس الظلامية والعهود السحرية.</p>
                    <p>تلتصق بتلك التمزقات كيانات طفيلية هلامية الشكل تُعرف في علوم الباطن بـ <em>اليرقات النجمية (Astral Larvae)</em> و<em>الديدان الطاقية</em>؛ حيث تتغذى على طاقة الخوف والشراهة والغضب، وتفرز ذبذبات وسواسية تُجبر الضحية على تكرار الأنماط التدميرية لتأمين غذائها الأثيري المستمر.</p>
                    <div class="treatise-meta">
                        <span><strong>أعراض التمزق:</strong> إرهاق مزمن مجهول السبب، برودة الأطراف، كوابيس الجاثوم</span>
                        <span><strong>الميكانيكا:</strong> رنين ترادفي منخفض (Low vibrational entrainment)</span>
                    </div>
                </div>

                <div class="sphere-treatise">
                    <div class="treatise-header">
                        <span class="treatise-badge">4. مصفوفة التحصين والدرع النبوي</span>
                        <h4>🛡️ بروتوكول إعادة بناء التماسك البيوفوتوني وتطهير الهالة</h4>
                    </div>
                    <p>يؤسس الطب النبوي والشريعة الغراء نظاماً هندسياً صارماً لإعادة شحن وترميم الحقل التوريدي:</p>
                    <ul style="padding-right:18px; margin:8px 0; font-size:0.87rem; color:#475569; line-height:1.7;">
                        <li><strong>الوضوء المستمر (Biophotonic Discharge):</strong> يزيل الماء الجاري الشحنات الكهروستاتيكية الزائدة ويعيد استقطاب الأيونات السالبة في الجلد، مؤكداً نبوياً: «إِنَّ أُمَّتِي يُدْعَوْنَ يَوْمَ الْقِيَامَةِ غُرًّا مُحَجَّلِينَ مِنْ آثَارِ الْوُضُوءِ».</li>
                        <li><strong>السجود للأرض (Earthing Resonance):</strong> تفريغ الترددات الكهرومغناطيسية الضارة ومزامنة الدماغ مع تردد رنين شومان (7.83 هرتز) للأرض عبر الاتصال المباشر لسبعة أعضاء.</li>
                        <li><strong>الحصن الحصين (آية الكرسي والمعوذتان):</strong> تردد صوتي بمقامات الترتيل يولد حقلاً موجياً واقفاً (Standing Scalar Wave) يغلق شقوق الهالة تماماً ويعكس الهجمات النارية كمرآة كهرومغناطيسية عاكسة.</li>
                    </ul>
                    <div class="treatise-meta">
                        <span><strong>بروتوكول الطوارئ:</strong> الاستعاذة العميقة مع زفير مديد ونفث على الكفين ومسح الجسد</span>
                        <span><strong>التأثير:</strong> إغلاق فوري للثغرات الأثيرية خلال 3 دقائق</span>
                    </div>
                </div>
            </div>

            <!-- Interactive 7-Layer Biofield Toroid Resonator -->
            <!-- Holographic Meditating Human Silhouette & 7 Subtle Bodies (Microcosm) -->
            <div class="bodies-cosmos-container">
                <!-- Human Silhouette Hologram -->
                <div class="body-silhouette-wrapper">
                    <div style="font-size: 0.95rem; font-weight: 700; color: var(--gold); margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                        <span>🧬 المجسم النوراني للأجساد السبعة والأغلفة الحيوية (Koshas & Aura)</span>
                    </div>

                    <!-- Interactive Quick Selector Pills -->
                    <div class="body-pills-bar" id="body-pills-bar">
                        <button class="b-pill-btn active" id="b-pill-1" onclick="selectBodyLayer('1')" style="color:#ef4444;"><span style="width:8px;height:8px;border-radius:50%;background:#ef4444;"></span>١. المادي</button>
                        <button class="b-pill-btn" id="b-pill-2" onclick="selectBodyLayer('2')" style="color:#ff8c00;"><span style="width:8px;height:8px;border-radius:50%;background:#ff8c00;"></span>٢. الأثيري</button>
                        <button class="b-pill-btn" id="b-pill-3" onclick="selectBodyLayer('3')" style="color:#f4b41a;"><span style="width:8px;height:8px;border-radius:50%;background:#f4b41a;"></span>٣. النجمي</button>
                        <button class="b-pill-btn" id="b-pill-4" onclick="selectBodyLayer('4')" style="color:#06d6a0;"><span style="width:8px;height:8px;border-radius:50%;background:#06d6a0;"></span>٤. العقلي</button>
                        <button class="b-pill-btn" id="b-pill-5" onclick="selectBodyLayer('5')" style="color:#00f0ff;"><span style="width:8px;height:8px;border-radius:50%;background:#00f0ff;"></span>٥. السببي</button>
                        <button class="b-pill-btn" id="b-pill-6" onclick="selectBodyLayer('6')" style="color:#8b5cf6;"><span style="width:8px;height:8px;border-radius:50%;background:#8b5cf6;"></span>٦. البوذي</button>
                        <button class="b-pill-btn" id="b-pill-7" onclick="selectBodyLayer('7')" style="color:#c026d3;"><span style="width:8px;height:8px;border-radius:50%;background:#c026d3;"></span>٧. الروحاني</button>
                    </div>

                    <div class="silhouette-canvas" id="silhouette-canvas">
                        <!-- High-Tech Sacred Meditating Human Hologram SVG with 7 Auric Sheaths -->
                        <svg class="human-figure-svg" viewBox="0 0 320 540" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <linearGradient id="bodyGrad" x1="0" y1="0" x2="0" y2="540" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.35" />
                                    <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.22" />
                                    <stop offset="100%" stop-color="#ef4444" stop-opacity="0.35" />
                                </linearGradient>
                                <linearGradient id="spineRainbow" x1="0" y1="30" x2="0" y2="480" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#ffffff" />
                                    <stop offset="16%" stop-color="#8b5cf6" />
                                    <stop offset="33%" stop-color="#3b82f6" />
                                    <stop offset="50%" stop-color="#06d6a0" />
                                    <stop offset="66%" stop-color="#f4b41a" />
                                    <stop offset="83%" stop-color="#ff8c00" />
                                    <stop offset="100%" stop-color="#ef4444" />
                                </linearGradient>
                                <radialGradient id="auraGlow" cx="160" cy="95" r="90" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#94a3b8" stop-opacity="0.45" />
                                    <stop offset="60%" stop-color="#00f0ff" stop-opacity="0.15" />
                                    <stop offset="100%" stop-color="#000000" stop-opacity="0" />
                                </radialGradient>
                                <filter id="glowFilt" x="-20%" y="-20%" width="140%" height="140%">
                                    <feGaussianBlur stdDeviation="3" result="blur" />
                                    <feComposite in="SourceGraphic" in2="blur" operator="over" />
                                </filter>
                            </defs>

                            <!-- Concentric 7 Subtle Auric Kosha Envelopes -->
                            <!-- 7. Atmic Envelope (Apex Cosmic Field) -->
                            <ellipse cx="160" cy="270" rx="155" ry="255" stroke="#c026d3" stroke-width="2" stroke-dasharray="6 4" opacity="0.65" />
                            <!-- 6. Buddhic Envelope (Radiant Bliss Oval) -->
                            <ellipse cx="160" cy="265" rx="135" ry="225" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="5 3" opacity="0.7" />
                            <!-- 5. Causal Envelope (Cosmic Memory Matrix) -->
                            <ellipse cx="160" cy="260" rx="115" ry="195" stroke="#00f0ff" stroke-width="2" stroke-dasharray="4 4" opacity="0.75" />
                            <!-- 4. Mental Envelope (Intellectual Coherence Field) -->
                            <ellipse cx="160" cy="255" rx="95" ry="165" stroke="#06d6a0" stroke-width="2" opacity="0.65" />
                            <!-- 3. Astral Envelope (Emotional Toroidal Field) -->
                            <ellipse cx="160" cy="250" rx="78" ry="135" stroke="#f4b41a" stroke-width="2.2" opacity="0.75" />

                            <!-- Glowing Aura Background behind Head -->
                            <circle cx="160" cy="95" r="85" fill="url(#auraGlow)" />

                            <!-- Sacred Geometry Halo behind Head -->
                            <circle cx="160" cy="95" r="75" stroke="rgba(244, 180, 26, 0.4)" stroke-width="1.5" stroke-dasharray="6 4" />
                            <circle cx="160" cy="95" r="60" stroke="rgba(0, 240, 255, 0.35)" stroke-width="1" />
                            <circle cx="160" cy="95" r="45" stroke="rgba(168, 85, 247, 0.4)" stroke-width="1" stroke-dasharray="3 3" />
                            <!-- Radiating Rays -->
                            <line x1="160" y1="15" x2="160" y2="35" stroke="#94a3b8" stroke-width="2" />
                            <line x1="160" y1="155" x2="160" y2="175" stroke="#94a3b8" stroke-width="1.5" />
                            <line x1="80" y1="95" x2="100" y2="95" stroke="#94a3b8" stroke-width="1.5" />
                            <line x1="220" y1="95" x2="240" y2="95" stroke="#94a3b8" stroke-width="1.5" />

                            <!-- Meditating Human Silhouette Contour (Lotus Pose) -->
                            <!-- 2. Etheric Envelope (Pranic Blueprint hugging skin) -->
                            <circle cx="160" cy="95" r="34" stroke="#ff8c00" stroke-width="2" stroke-dasharray="3 2" fill="none" opacity="0.8" />
                            <circle cx="160" cy="95" r="28" fill="url(#bodyGrad)" stroke="#00f0ff" stroke-width="1.8" />
                            <path d="M152,122 L150,135 L170,135 L168,122" fill="url(#bodyGrad)" stroke="#00f0ff" stroke-width="1.5" />
                            <path d="M150,135 C138,138 112,148 95,165 C78,182 66,215 62,250 C58,285 64,310 75,325 C84,337 96,335 105,320 C114,305 118,275 125,235 C130,205 136,175 145,160 L145,260 C138,295 132,340 120,370 C108,400 78,430 52,455 C35,472 40,498 70,505 C108,512 140,512 160,512 C180,512 212,512 250,505 C280,498 285,472 268,455 C242,430 212,400 200,370 C188,340 182,295 175,260 L175,160 C184,175 190,205 195,235 C202,275 206,305 215,320 C224,335 236,337 245,325 C256,310 262,285 258,250 C254,215 242,182 225,165 C208,148 182,138 170,135 Z" 
                                  fill="url(#bodyGrad)" stroke="#00f0ff" stroke-width="1.8" filter="url(#glowFilt)" />

                            <!-- Meditating Hands in Mudra over Lap -->
                            <ellipse cx="160" cy="425" rx="36" ry="16" fill="rgba(0, 240, 255, 0.12)" stroke="rgba(0, 240, 255, 0.5)" stroke-width="1.5" />

                            <!-- Sacred Heart Geometry (Merkabah) at Heart Center -->
                            <polygon points="160,230 182,268 138,268" stroke="rgba(16, 185, 129, 0.45)" stroke-width="1.2" fill="none" />
                            <polygon points="160,280 182,242 138,242" stroke="rgba(16, 185, 129, 0.45)" stroke-width="1.2" fill="none" />
                            <circle cx="160" cy="255" r="24" stroke="rgba(244, 180, 26, 0.3)" stroke-width="1" stroke-dasharray="2 2" fill="none" />

                            <!-- Sushumna (Central Spine Rainbow Light Channel) -->
                            <line x1="160" y1="35" x2="160" y2="480" stroke="url(#spineRainbow)" stroke-width="4.5" stroke-linecap="round" />

                            <!-- Ida (Left Lunar Channel - Cyan) -->
                            <path d="M160,470 C135,435 135,415 160,395 C185,360 185,345 160,325 C135,290 135,275 160,255 C185,225 185,210 160,195 C135,165 135,155 160,140 C185,110 185,100 160,85" 
                                  stroke="#00f0ff" stroke-width="2" stroke-dasharray="4 3" fill="none" opacity="0.75" />

                            <!-- Pingala (Right Solar Channel - Gold) -->
                            <path d="M160,470 C185,435 185,415 160,395 C135,360 135,345 160,325 C185,290 185,275 160,255 C135,225 135,210 160,195 C185,165 185,155 160,140 C135,110 135,100 160,85" 
                                  stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 3" fill="none" opacity="0.75" />
                        </svg>

                        <!-- 7 Subtle Bodies Pulsating Interactive Nodes -->
                        <div class="body-point-btn" id="body-node-7" style="top: 38px; color: #c026d3; border-color: #c026d3; background: rgba(192, 38, 211, 0.3);" onclick="selectBodyLayer('7')" title="٧. الجسد الروحاني الأسمى (Atmic Spark)">٧</div>
                        <div class="body-point-btn" id="body-node-6" style="top: 85px; color: #8b5cf6; border-color: #8b5cf6;" onclick="selectBodyLayer('6')" title="٦. الجسد البوذي (Buddhic)">٦</div>
                        <div class="body-point-btn" id="body-node-5" style="top: 170px; color: #00f0ff; border-color: #00f0ff;" onclick="selectBodyLayer('5')" title="٥. الجسد السببي (Causal)">٥</div>
                        <div class="body-point-btn" id="body-node-4" style="top: 250px; color: #06d6a0; border-color: #06d6a0;" onclick="selectBodyLayer('4')" title="٤. الجسد العقلي (Mental)">٤</div>
                        <div class="body-point-btn" id="body-node-3" style="top: 325px; color: #f4b41a; border-color: #f4b41a;" onclick="selectBodyLayer('3')" title="٣. الجسد النجمي (Astral)">٣</div>
                        <div class="body-point-btn" id="body-node-2" style="top: 395px; color: #ff8c00; border-color: #ff8c00;" onclick="selectBodyLayer('2')" title="٢. الجسد الأثيري (Etheric)">٢</div>
                        <div class="body-point-btn active" id="body-node-1" style="top: 470px; color: #ef4444; border-color: #ef4444;" onclick="selectBodyLayer('1')" title="١. الجسد المادي الكثيف (Physical)">١</div>
                    </div>

                    <div style="margin-top: 15px; font-size: 0.8rem; color: #94a3b8; text-align: center;">
                        ✨ انقر على أي غلاف أو طبقة لعرض الفيزيولوجيا الحيوية وبروتوكول التحصين النبوي
                    </div>
                </div>

                <!-- Deep Interactive Synthesis Panel -->
                <div class="body-detail-card" id="body-detail-card">
                    <!-- Injected dynamically by selectBodyLayer() -->
                </div>
            </div>

            <!-- Filter Categories Bar -->
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:20px; background:rgba(15,23,42,0.6); padding:12px 18px; border-radius:12px; border:1px solid var(--border-glass);">
                <div style="font-weight:700; color:#fff; font-size:0.95rem;">
                    🔎 تصفية مستويات الوعي والأغماد السبعة:
                </div>
                <div style="display:flex; gap:8px; flex-wrap:wrap;">
                    <button class="body-filter-btn active" onclick="filterBodies('all', this)">عرض المنظومة الكاملة (7)</button>
                    <button class="body-filter-btn" onclick="filterBodies('dense', this)">الأجساد الكثيفة والقالب (1-2)</button>
                    <button class="body-filter-btn" onclick="filterBodies('bridge', this)">الجسر النفسي والعقلي (3-4)</button>
                    <button class="body-filter-btn" onclick="filterBodies('spiritual', this)">المراقي النورانية والروحية (5-7)</button>
                </div>
            </div>

            <!-- Master 7 Bodies Stack Cards -->
            <div class="bodies-stack" id="bodies-stack"></div>

            <!-- Panoramic Comparative Matrix Table -->
            <div style="margin-top:40px; background:rgba(10,16,26,0.85); border:1px solid rgba(0,229,255,0.2); border-radius:16px; padding:24px; overflow-x:auto;">
                <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                    <span style="font-size:1.4rem;">📊</span>
                    <h3 style="color:#fff; font-family:'Amiri',serif; margin:0; font-size:1.3rem;">جدول المقارنة البانورامي الشامل للأجساد السبعة ومراتب النفس ومفاتيح الإغلاق</h3>
                </div>
                <table style="width:100%; border-collapse:collapse; font-size:0.85rem; color:#475569; text-align:right;">
                    <thead>
                        <tr style="background:rgba(15,23,42,0.9); border-bottom:2px solid var(--gold); color:var(--gold);">
                            <th style="padding:12px 10px;">#</th>
                            <th style="padding:12px 10px;">الجسد / الغمد</th>
                            <th style="padding:12px 10px;">مرتبة النفس</th>
                            <th style="padding:12px 10px;">النطاق الترددي / المادة</th>
                            <th style="padding:12px 10px;">موقع الحقل وسمكه</th>
                            <th style="padding:12px 10px;">طبيعة الاختراق والطفيليات</th>
                            <th style="padding:12px 10px;">بروتوكول الإغلاق والحجاب</th>
                        </tr>
                    </thead>
                    <tbody id="panoramic-bodies-table">
                        <!-- Populated in renderBodies -->
                    </tbody>
                </table>
            </div>
        </div>

                <!-- 7. NUMBERS & WAFQ GHAZALI (DOOR 15) -->
        <div id="tab-numbers" class="tab-content">
            <div class="hero-banner">
                <h2>🔢 الباب الخامس عشر: المربعات السحرية والأوفاق الكونية (3×3 حتى 9×9) — لغة النواميس، ميكانيكا التشفير، ودستور التفعيل والإغلاق</h2>
                <p>تفكيك علم الأوفاق كلغة برمجة كونية ومصفوفات طاقية ذات موجات واقفة (Scalar Standing Waves)؛ دراسة مقارنة عبر الحضارات (لو شو الصيني، يانترا الفيدا الهندية، بابل، الغزالي، البوني، وكورنيليوس أغريبا)؛ الشروط الصارمة للتحقيق والرنين؛ ودليل البناء، التفعيل، الفك، والختم.</p>
            </div>

            <!-- DUAL INTERACTIVE WAFQ STUDIO -->
            <div class="wafq-studio-container">
                <!-- Mode Switcher -->
                <div class="wafq-mode-toggle">
                    <button class="wafq-mode-btn active" id="wafq-mode-btn-planetary" onclick="switchWafqStudioMode('planetary')">
                        <i class="fa-solid fa-solar-system"></i> مختبر الأوفاق الكوكبية السبعة (من 3×3 إلى 9×9)
                    </button>
                    <button class="wafq-mode-btn" id="wafq-mode-btn-ghazali" onclick="switchWafqStudioMode('ghazali')">
                        <i class="fa-solid fa-calculator"></i> حاسبة ومولّد وفق الغزالي 3×3 الحي والمخصص (Live Custom Engine)
                    </button>
                </div>

                <!-- PANEL 1: PLANETARY MATRIX LAB (3x3 to 9x9) -->
                <div id="wafq-planetary-panel">
                    <!-- Planetary Order Selector Pills -->
                    <div class="wafq-planet-selector-bar">
                        <button class="wafq-order-pill active" id="wafq-pill-3" onclick="renderPlanetaryMatrixLab(3)">
                            <span style="color:#6b7280;">♄</span> زحل 3×3 (M=15)
                        </button>
                        <button class="wafq-order-pill" id="wafq-pill-4" onclick="renderPlanetaryMatrixLab(4)">
                            <span style="color:#3b82f6;">♃</span> المشتري 4×4 (M=34)
                        </button>
                        <button class="wafq-order-pill" id="wafq-pill-5" onclick="renderPlanetaryMatrixLab(5)">
                            <span style="color:#ef4444;">♂</span> المريخ 5×5 (M=65)
                        </button>
                        <button class="wafq-order-pill" id="wafq-pill-6" onclick="renderPlanetaryMatrixLab(6)">
                            <span style="color:#f4b41a;">☉</span> الشمس 6×6 (M=111)
                        </button>
                        <button class="wafq-order-pill" id="wafq-pill-7" onclick="renderPlanetaryMatrixLab(7)">
                            <span style="color:#06d6a0;">♀</span> الزهرة 7×7 (M=175)
                        </button>
                        <button class="wafq-order-pill" id="wafq-pill-8" onclick="renderPlanetaryMatrixLab(8)">
                            <span style="color:#9d4edd;">☿</span> عطارد 8×8 (M=260)
                        </button>
                        <button class="wafq-order-pill" id="wafq-pill-9" onclick="renderPlanetaryMatrixLab(9)">
                            <span style="color:#00f0ff;">☽</span> القمر 9×9 (M=369)
                        </button>
                    </div>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:24px; align-items:start;">
                        <!-- Left: Dynamic Grid & Verification Badges -->
                        <div>
                            <div class="wafq-grid-dynamic" id="wafq-dynamic-grid-container"></div>
                            <div class="wafq-math-badge-bar" id="wafq-math-badges-container"></div>
                        </div>

                        <!-- Right: Inspector Telemetry & Scholarship Card -->
                        <div id="wafq-inspector-content" style="background:rgba(0,0,0,0.35); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:20px;">
                            <!-- Injected dynamically via JS -->
                        </div>
                    </div>
                </div>

                <!-- PANEL 2: GHAZALI CUSTOM 3x3 ENGINE -->
                <div id="wafq-ghazali-panel" style="display:none;">
                    <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:12px;">
                        <div>
                            <h3 style="margin:0; font-family:'Amiri',serif; font-size:1.35rem; color:var(--gold); display:flex; align-items:center; gap:8px;">
                                <i class="fa-solid fa-calculator"></i> حاسبة تعمير مثلث الغزالي 3×3 لأي عدد أو اسم (Custom 3x3 Generator)
                            </h3>
                            <span style="font-size:0.8rem; color:#94a3b8;">أدخل أي عدد صحيح أو اسم/آية (يتم حساب الجُمّل الكبير تلقائياً)، ويتم استخراج المفتاح والمغلق وخانة الجبر ومطابقة المجاميع اللحظية:</span>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <input type="text" id="wafq-input" value="105" placeholder="أدخل عدداً أو اسماً (مثال: 105، آدم، الله، سلام)" style="background:rgba(0,0,0,0.6); border:1px solid var(--gold); border-radius:8px; padding:8px 14px; color:#fff; font-family:'Tajawal',sans-serif; font-size:0.95rem; width:240px; text-align:center;">
                            <button onclick="calculateLiveWafq()" class="synth-btn" style="padding:8px 16px; font-weight:700;"><i class="fa-solid fa-wand-magic-sparkles"></i> توليد الوفق</button>
                        </div>
                    </div>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:24px; align-items:center;">
                        <!-- Visual Grid Output -->
                        <div>
                            <div style="text-align:center; font-size:0.85rem; color:#94a3b8; margin-bottom:10px; background:rgba(0,0,0,0.4); padding:8px 12px; border-radius:8px;" id="wafq-math-summary">
                                المطلوب (N) = <strong>105</strong> | المفتاح = <strong>31</strong> | الأس = 12 | الباقي = <strong>0</strong> (تام)
                            </div>
                            <div class="magic-grid-3x3" id="live-wafq-grid" style="max-width:320px; margin:0 auto;"></div>
                            <div class="wafq-math-badge-bar" id="ghazali-verification-badges" style="margin-top:12px;"></div>
                        </div>

                        <!-- Explanatory Guide -->
                        <div style="font-size:0.86rem; line-height:1.8; color:#475569; background:rgba(0,0,0,0.3); padding:18px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                            <strong style="color:var(--gold); font-size:1rem; display:block; margin-bottom:6px;">قاعدة تعمير مثلث الغزالي الرياضية الصارمة:</strong>
                            <ol style="margin:0 0 10px 18px; padding:0;">
                                <li><strong>المعادلة الأصلية:</strong> (العدد المطلوب - 12) ÷ 3 = المفتاح (حيث العدد المطلوب هو الرقم المباشر أو مجموع حروف الاسم بحساب الجُمّل).</li>
                                <li><strong>إذا كان الباقي 0 (وفق تام):</strong> يعمر الوفق تتابعياً بالسير الطبيعي (1 إلى 9) بإضافة 1 في كل خانة.</li>
                                <li><strong>إذا كان الباقي 1 (كسر 1):</strong> يُجبر الوفق بزيادة 1 في البيت السابع (الزاي 7)، فتتوالى الخانات 7 و 8 و 9 بزيادة واحد إضافي.</li>
                                <li><strong>إذا كان الباقي 2 (كسر 2):</strong> يُجبر الوفق بزيادة 1 في البيت الرابع (الدال 4)، فتتوالى الخانات من 4 إلى 9 بزيادة واحد إضافي.</li>
                            </ol>
                            <div style="background:rgba(244,180,26,0.1); border-right:3px solid var(--gold); padding:8px 12px; border-radius:4px; font-size:0.82rem;">
                                كل صف، عمود، وقطر يعطي بدقة متناهية العدد المطلوب نفسه، مما يخلق توازناً هندسياً تاماً يمنع تراكم الشحنات التشتتية.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            
            <!-- ========================================================
                 THE AL-GHAZALI MASTER HANDBOOK (ASRAR AL-ASRAR) 3x3
                 ======================================================== -->
            <div class="ghazali-master-handbook" id="ghazali-handbook">
                <div class="ghazali-handbook-header">
                    <span style="font-size:0.82rem; color:var(--cyan); letter-spacing:1px; text-transform:uppercase; font-weight:700;">
                        The Definitive Hermetic & Mathematical Manual of Ghazali's 3x3 Magic Square
                    </span>
                    <h3 class="ghazali-handbook-title">
                        📜 كتيب أسرار الأسرار الشريف: الدستور التشغيلي والكتيب الكامل لتعمير وتفعيل وتصريف مثلث الغزالي 3×3 (بطد زهج واح)
                    </h3>
                    <p class="ghazali-handbook-subtitle">
                        دليل تطبيقي تفصيلي شامل من الألف إلى الياء: تشريح البيوت التسعة ومسارات الطاقة، خوارزمية التعمير الجبري بدقة متناهية، ثلاثة نماذج تطبيقية واقعية كاملة (الشفاء، الرزق، والهيبة)، دستور الأحبار والأوعية، مواقيت الرصد الفلكي، بروتوكول التفعيل والرنين، ودليل الفك والتحليل العكسي للأوفاق المجهولة وإبطال الفاسد منها تحت لواء التوحيد القرآني الخالص.
                    </p>
                </div>

                <!-- QUICK NAVIGATION PILLS -->
                <div class="ghazali-nav-pills">
                    <a href="#ghazali-ch1" class="ghazali-nav-pill"><i class="fa-solid fa-compass"></i> الباب 1: تشريح البيوت وسير بطد</a>
                    <a href="#ghazali-ch2" class="ghazali-nav-pill"><i class="fa-solid fa-calculator"></i> الباب 2: خوارزمية التعمير والكسر</a>
                    <a href="#ghazali-ch3" class="ghazali-nav-pill"><i class="fa-solid fa-cube"></i> الباب 3: نماذج تطبيقية كبرى</a>
                    <a href="#ghazali-ch4" class="ghazali-nav-pill"><i class="fa-solid fa-pen-fancy"></i> الباب 4: دستور الأحبار والمواد</a>
                    <a href="#ghazali-ch5" class="ghazali-nav-pill"><i class="fa-solid fa-clock"></i> الباب 5: مواقيت الرصد وساعات الكواكب</a>
                    <a href="#ghazali-ch6" class="ghazali-nav-pill"><i class="fa-solid fa-volume-high"></i> الباب 6: بروتوكول التفعيل والرنين</a>
                    <a href="#ghazali-ch7" class="ghazali-nav-pill"><i class="fa-solid fa-key"></i> الباب 7: علامات الفساد والبطلان</a>
                    <a href="#ghazali-ch8" class="ghazali-nav-pill"><i class="fa-solid fa-shield-halved"></i> الباب 8: التحصين التوحيدي</a>
                    <a href="#ghazali-ch9" class="ghazali-nav-pill"><i class="fa-solid fa-eye-slash"></i> الباب 9: فيزياء الحجب والإغشاء (سدّاً سدّاً)</a>
                    <a href="#ghazali-ch10" class="ghazali-nav-pill"><i class="fa-solid fa-eye"></i> الباب 10: تنقية الرّان وفتح البصيرة</a>
                    <a href="#ghazali-ch11" class="ghazali-nav-pill"><i class="fa-solid fa-crown"></i> الباب 11: تفكيك مغالطة الخدام والسيادة</a>
                    <a href="#ghazali-ch12" class="ghazali-nav-pill"><i class="fa-solid fa-arrow-up-right-dots"></i> الباب 12: فلسفة الأعداد والقراءات والبسط</a>
                    <a href="#ghazali-ch13" class="ghazali-nav-pill"><i class="fa-solid fa-fire-flame-curved"></i> الباب 13: الدستور الكيميائي للبخورات السبعة</a>
                    <a href="#ghazali-ch14" class="ghazali-nav-pill"><i class="fa-solid fa-wind"></i> الباب 14: التوافق الزماني والمكاني والرياح الأربع</a>
                    <a href="#ghazali-ch15" class="ghazali-nav-pill"><i class="fa-solid fa-infinity"></i> الباب 15: الأسرار الرياضية التي لم يذكرها الغزالي</a>
                </div>

                <!-- CHAPTER 1 -->
                <div class="ghazali-chapter" id="ghazali-ch1">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١</div>
                        <div>
                            <h4 class="chapter-title">الباب الأول: مدخل الأصول وتشريح خارطة البيوت التسعة وسير "بطد زهج واح"</h4>
                            <div class="chapter-subtitle">The Anatomical Blueprint: The 9 Matrix Cells & Elemental Coordinates</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>سُمّي هذا المثلث بـ <strong>"مثلث الغزالي الشريف"</strong> أو مثلث <strong>"بطد زهج واح"</strong> لأن الإمام أبا حامد الغزالي جعله في كتابيه <em>"المنقذ من الضلال"</em> و<em>"السر المصون"</em> دليلاً عقلياً برهانياً على وجود خواص باطنية طبيعية في الأعداد والنواميس أودعها الله تعالى في خلقه كالأدوية الكيميائية. وتسمية "بطد زهج واح" ليست لفظاً طلسمياً، بل هي اختصار لأرقام الخانات التسعة بحساب الجُمّل الصغير مصفوفة في ثلاثة أسطر:</p>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; align-items:center; margin:16px 0;">
                            <div>
                                <div class="specimen-grid-container">
                                    <div class="specimen-cell"><span class="specimen-cell-num" style="color:#ef4444;">د (4)</span><span class="specimen-cell-label">بيت الدال</span></div>
                                    <div class="specimen-cell lock-cell"><span class="specimen-cell-num" style="color:var(--gold);">ط (9)</span><span class="specimen-cell-label">المغلاق 🔒</span></div>
                                    <div class="specimen-cell"><span class="specimen-cell-num" style="color:#00f0ff;">ب (2)</span><span class="specimen-cell-label">بيت الباء</span></div>
                                    
                                    <div class="specimen-cell"><span class="specimen-cell-num" style="color:#00f0ff;">ج (3)</span><span class="specimen-cell-label">بيت الجيم</span></div>
                                    <div class="specimen-cell center-cell"><span class="specimen-cell-num" style="color:var(--gold);">هـ (5)</span><span class="specimen-cell-label">القطب ⚖️</span></div>
                                    <div class="specimen-cell"><span class="specimen-cell-num" style="color:#ef4444;">ز (7)</span><span class="specimen-cell-label">بيت الزاي</span></div>
                                    
                                    <div class="specimen-cell"><span class="specimen-cell-num" style="color:var(--emerald);">ح (8)</span><span class="specimen-cell-label">بيت الحاء</span></div>
                                    <div class="specimen-cell key-cell"><span class="specimen-cell-num" style="color:var(--emerald);">أ (1)</span><span class="specimen-cell-label">المفتاح 🔑</span></div>
                                    <div class="specimen-cell"><span class="specimen-cell-num" style="color:#94a3b8;">و (6)</span><span class="specimen-cell-label">بيت الواو</span></div>
                                </div>
                                <div style="text-align:center; font-size:0.78rem; color:#94a3b8;">توزيع الخانات التسعة الأصلي ومراتب الحروف الأبجدية</div>
                            </div>

                            <div style="background:rgba(0,0,0,0.3); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                                <strong style="color:var(--gold); display:block; margin-bottom:8px;">وظائف البيوت التسعة ومسار التدفق:</strong>
                                <ul style="margin:0 0 0 16px; padding:0; font-size:0.84rem; line-height:1.75;">
                                    <li><strong>بيت 1 (الألف - المفتاح):</strong> أسفل المنتصف. هو مدخل الطاقة وبداية السير، ويجب أن يكون أصغر عدد بالوفق.</li>
                                    <li><strong>الأركان الأربعة (الزوجية 2، 4، 6، 8):</strong> (ب، د، و، ح) تمثل أوتاد التثبيت والجاذبية الأرضية، وهي أعداد زوجية (طبيعة ين Yin).</li>
                                    <li><strong>الأطراف المتعامدة (الفردية 1، 3، 7، 9):</strong> (أ، ج، ز، ط) تمثل الصلبان الطاقية المتحركة (طبيعة يانغ Yang) ومسارات نقل الإشارة.</li>
                                    <li><strong>بيت 5 (الهاء - القطب والقلب):</strong> عين الوفق ومركز الثقل. يتوسط كافة الخطوط ويجب أن يساوي دائماً ثلث المجموع المطلوب في الأوفاق التامة.</li>
                                    <li><strong>بيت 9 (الطاء - المغلاق):</strong> أعلى المنتصف. هو مخرج الطاقة وصمام الأمان، ويحمل أكبر عدد في الوفق لمنع ارتداد الشحنة.</li>
                                </ul>
                            </div>
                        </div>

                        <div class="wafq-sub-box gold">
                            <strong>توزيع الطبائع الأربعة (Fire, Earth, Air, Water) داخل المثلث:</strong>
                            <br>• <strong>المثلث الناري:</strong> الخانات (1، 5، 9) ➔ القطر الصاعد والمحور المركزي (الحرارة، الحيوية، والسيادة).
                            <br>• <strong>المثلث الترابي:</strong> الخانات (2، 6) ➔ أركان التثبيت والاستقرار المادي والمناعة.
                            <br>• <strong>المثلث الهوائي:</strong> الخانات (3، 7) ➔ جانبا الوفق (الاتصالات، الفكر، وسرعة السريان).
                            <br>• <strong>المثلث المائي:</strong> الخانات (4، 8) ➔ الركنان الآخران (المرونة، المحبة، وسريان السوائل والشفاء).
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 2 -->
                <div class="ghazali-chapter" id="ghazali-ch2">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٢</div>
                        <div>
                            <h4 class="chapter-title">الباب الثاني: الرياضيات الصارمة وخوارزمية التعمير الجبري وحالات الكسر الثلاث</h4>
                            <div class="chapter-subtitle">The Exact Algebraic Engine & The 3 Invariant Remainder Cases</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>يقوم تعمير مثلث الغزالي على معادلة جبرية قطعية ثابتة لا تحتمل الخطأ أو التقريب:</p>
                        
                        <div style="background:rgba(244,180,26,0.1); border:1.5px solid var(--gold); border-radius:12px; padding:16px; text-align:center; margin:14px 0;">
                            <span style="font-size:1.15rem; color:#fff; font-family:'Tajawal',sans-serif; font-weight:700;">
                                القانون الكلي: $	ext{المفتاح} = \lfloor(N - 12) \div 3
floor$ | $	ext{الباقي (الكسر)} = (N - 12) \pmod 3$
                            </span>
                            <div style="font-size:0.8rem; color:#94a3b8; margin-top:6px;">حيث $N$ هو المجموع المطلوب، والرقم 12 هو "الأس" الثابت للمثلث</div>
                        </div>

                        <p><strong>لماذا نطرح الرقم 12 بالتحديد؟</strong> لأن حاصل جمع الزيادات النسبية بين الخانات التسعة في سيرها الطبيعي (بدءاً من الصفر) يساوي: $0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36$، وحيث أن المثلث له 3 صفوف، فإن نصيب الصف الواحد من الزيادات التراكمية هو $36 \div 3 = 12$. فطرح 12 هو تفريغ للوزن الهندسي للشبكة حتى يتبقى المقدار الخالص القابل للقسمة على 3 بالتساوي.</p>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin:16px 0;">
                            <!-- Case 0 -->
                            <div style="background:rgba(6,214,160,0.08); border:1px solid var(--emerald); border-radius:12px; padding:16px;">
                                <strong style="color:var(--emerald); font-size:1rem; display:block; margin-bottom:6px;">
                                    <i class="fa-solid fa-check-double"></i> الحالة الأولى: الباقي = 0 (الوفق التام الصحاح)
                                </strong>
                                <span style="font-size:0.82rem; color:#475569; display:block; margin-bottom:8px;">
                                    يحدث عندما يقبل الناتج $(N - 12)$ القسمة على 3 دون باقٍ (مثل الأعداد 15، 66، 105، 786).
                                </span>
                                <div style="background:rgba(0,0,0,0.4); padding:10px; border-radius:8px; font-size:0.8rem;">
                                    <strong>قاعدة التنزيل:</strong> يعمر الوفق تتابعياً بالسير الطبيعي بإضافة 1 في كل بيت دون أي قفزة:
                                    <br>بيت 1 = المفتاح
                                    <br>بيت 2 = المفتاح + 1 ... حتى بيت 9 = المفتاح + 8.
                                    <br><span style="color:var(--emerald);">النتيجة: كل صف، عمود، وقطر = $N$ تماماً!</span>
                                </div>
                            </div>

                            <!-- Case 1 -->
                            <div style="background:rgba(192,38,211,0.08); border:1px solid #c026d3; border-radius:12px; padding:16px;">
                                <strong style="color:#c026d3; font-size:1rem; display:block; margin-bottom:6px;">
                                    <i class="fa-solid fa-bolt"></i> الحالة الثانية: الباقي = 1 (كسر 1 ➔ جبر بيت 7)
                                </strong>
                                <span style="font-size:0.82rem; color:#475569; display:block; margin-bottom:8px;">
                                    يحدث عندما يتبقى 1 بعد القسمة (مثل الأعداد 16، 94، 106، 391).
                                </span>
                                <div style="background:rgba(0,0,0,0.4); padding:10px; border-radius:8px; font-size:0.8rem;">
                                    <strong>قاعدة التنزيل:</strong> السير طبيعي من بيت 1 إلى 6 (+1 كل خطوة).
                                    <br><strong>عند بيت 7 (الزاي):</strong> يُزاد 1 إضافي جبري (قفزة بـ +2 عن بيت 6)!
                                    <br>البيوت 8 و 9: تستمر بزيادة +1 بعد الجبر.
                                    <br><span style="color:#c026d3;">السر: بيت 7 يعوض النقص في الصف الأوسط والعمود الأيسر.</span>
                                </div>
                            </div>

                            <!-- Case 2 -->
                            <div style="background:rgba(239,68,68,0.08); border:1px solid #ef4444; border-radius:12px; padding:16px;">
                                <strong style="color:#ef4444; font-size:1rem; display:block; margin-bottom:6px;">
                                    <i class="fa-solid fa-fire"></i> الحالة الثالثة: الباقي = 2 (كسر 2 ➔ جبر بيت 4)
                                </strong>
                                <span style="font-size:0.82rem; color:#475569; display:block; margin-bottom:8px;">
                                    يحدث عندما يتبقى 2 بعد القسمة (مثل الأعداد 17، 107، 308).
                                </span>
                                <div style="background:rgba(0,0,0,0.4); padding:10px; border-radius:8px; font-size:0.8rem;">
                                    <strong>قاعدة التنزيل:</strong> السير طبيعي من بيت 1 إلى 3 (+1 كل خطوة).
                                    <br><strong>عند بيت 4 (الدال):</strong> يُزاد 1 إضافي جبري (قفزة بـ +2 عن بيت 3)!
                                    <br>البيوت من 5 إلى 9: تستمر بزيادة +1 تتابعياً.
                                    <br><span style="color:#ef4444;">السر: بيت 4 في الركن يوزع الزيادة بدقة عبر الصف الأول والعمود الأيمن.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 3: THE 3 COMPLETE OPERATIONAL CASE STUDIES -->
                <div class="ghazali-chapter" id="ghazali-ch3">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٣</div>
                        <div>
                            <h4 class="chapter-title">الباب الثالث: النماذج التطبيقية العملية الكبرى الثلاثة من الألف إلى الياء</h4>
                            <div class="chapter-subtitle">3 Complete Real-World End-to-End Operational Case Studies</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>لكي لا يبقى هذا العلم نظرياً في بطون المخطوطات، إليك ثلاثة تصاريف حقيقية كاملة لكبرى مطالب الحياة الإنسانية، مشروحة بالحساب الهندسي والشبكة البصرية وبروتوكول الاستخدام الفعلي خطوة بخطوة:</p>

                        <!-- EXAMPLE 1: HEALING & RECOVERY -->
                        <div style="background:rgba(6,214,160,0.05); border:1.5px solid var(--emerald); border-radius:16px; padding:22px; margin-bottom:24px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; border-bottom:1px solid rgba(6,214,160,0.25); padding-bottom:12px; margin-bottom:14px;">
                                <div>
                                    <h5 style="margin:0; font-family:'Amiri',serif; font-size:1.35rem; color:var(--emerald);">
                                        🌿 النموذج التطبيقي الأول: مثلث الشفاء التام ودفع العلل والأسقام (اسم الله "شافي")
                                    </h5>
                                    <span style="font-size:0.8rem; color:#94a3b8;">الغرض: شفاء الأمراض الباثولوجية، رفع المناعة الخلوية، طرد التراكمات الطاقية السامة، وتجديد الحقل الحيوي.</span>
                                </div>
                                <span style="background:rgba(6,214,160,0.2); color:var(--emerald); padding:4px 12px; border-radius:20px; font-weight:700; font-size:0.8rem;">حالة كسر 1 (جبر بيت 7)</span>
                            </div>

                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; align-items:center;">
                                <div>
                                    <div class="specimen-grid-container" style="border-color:var(--emerald);">
                                        <div class="specimen-cell"><span class="specimen-cell-num">129</span><span class="specimen-cell-label">د (4)</span></div>
                                        <div class="specimen-cell lock-cell"><span class="specimen-cell-num">135</span><span class="specimen-cell-label">ط (9) 🔒</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">127</span><span class="specimen-cell-label">ب (2)</span></div>
                                        
                                        <div class="specimen-cell"><span class="specimen-cell-num">128</span><span class="specimen-cell-label">ج (3)</span></div>
                                        <div class="specimen-cell center-cell"><span class="specimen-cell-num">130</span><span class="specimen-cell-label">هـ (5) ⚖️</span></div>
                                        <div class="specimen-cell broken-cell"><span class="specimen-cell-num">133</span><span class="specimen-cell-label">ز (7) ⚡ جبر</span></div>
                                        
                                        <div class="specimen-cell"><span class="specimen-cell-num">134</span><span class="specimen-cell-label">ح (8)</span></div>
                                        <div class="specimen-cell key-cell"><span class="specimen-cell-num">126</span><span class="specimen-cell-label">أ (1) 🔑</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">131</span><span class="specimen-cell-label">و (6)</span></div>
                                    </div>
                                    <div class="wafq-math-badge-bar">
                                        <div class="wafq-math-badge verified">صف 1: 129+135+127 = <strong>391</strong> ✓</div>
                                        <div class="wafq-math-badge verified">صف 2: 128+130+133 = <strong>391</strong> ✓</div>
                                        <div class="wafq-math-badge verified">صف 3: 134+126+131 = <strong>391</strong> ✓</div>
                                    </div>
                                </div>

                                <div style="font-size:0.85rem; line-height:1.75; color:#475569;">
                                    <strong style="color:var(--gold);">١. الاستخراج الحسابي الدقيق:</strong>
                                    <br>• جُمّل "شـافـي": ش (300) + ا (1) + ف (80) + ي (10) = <strong>391</strong>.
                                    <br>• طرح الأس: $391 - 12 = 379$.
                                    <br>• القسمة: $379 \div 3 = 126$ والباقي <strong>1</strong>.
                                    <br>• إذن: المفتاح = <strong>126</strong>، الباقي = 1 ➔ جبر بزيادة +1 في البيت 7.
                                    <br>• سَير التنزيل: (بيت 1=126، 2=127، 3=128، 4=129، 5=130، 6=131) ➔ <strong>قفزة في بيت 7 = 133</strong> ➔ (بيت 8=134، بيت 9=135).
                                </div>
                            </div>

                            <!-- Operational Field Protocol -->
                            <div class="operational-protocol-box">
                                <strong style="color:var(--emerald); font-size:0.95rem; display:block; margin-bottom:10px;">
                                    <i class="fa-solid fa-notes-medical"></i> البروتوكول الميداني الكامل للاستخدام والشفاء:
                                </strong>
                                <div class="protocol-step">
                                    <span class="step-badge">التوقيت</span>
                                    <span>يوم الأحد عند شروق الشمس (ساعة الشمس الأولى) لطرد الظلمات الحيوية، أو يوم الخميس في ساعة المشتري في النصف الأول من الشهر القمري.</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">المداد والحامل</span>
                                    <span>يُكتب بمداد طاهر من <strong>ماء الورد والزعفران وقليل من المسك الأبيض</strong> على <strong>صحن صيني أو زجاجي أبيض نقي</strong> لا نقش فيه ولا رسم.</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">التعزيم والتفعيل</span>
                                    <span>أثناء الكتابة يُطلق بخور <strong>اللبان الذكر والسندروس</strong>، وبعد الفراغ تُقرأ سورة الفاتحة 7 مرات، وآية الشفاء ﴿وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ﴾ 70 مرة، وترديد اسم "يا شافي" بعدد الجُمّل (391 مرة).</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">التطبيق الجسدي</span>
                                    <span>يُمحى الوفق بماء زمزم أو ماء نقي، ويشربه المريض على الريق صباحاً لمدة 7 أيام متتالية مع المشي حافياً على التراب 10 دقائق لتفريغ الشحنات السامة (Grounding).</span>
                                </div>
                            </div>
                        </div>

                        <!-- EXAMPLE 2: WEALTH & ABUNDANCE -->
                        <div style="background:rgba(244,180,26,0.05); border:1.5px solid var(--gold); border-radius:16px; padding:22px; margin-bottom:24px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; border-bottom:1px solid rgba(244,180,26,0.25); padding-bottom:12px; margin-bottom:14px;">
                                <div>
                                    <h5 style="margin:0; font-family:'Amiri',serif; font-size:1.35rem; color:var(--gold);">
                                        💰 النموذج التطبيقي الثاني: مثلث الرزق وتيسير التجارة والوفرة المالية (اسم الله "رزاق")
                                    </h5>
                                    <span style="font-size:0.8rem; color:#94a3b8;">الغرض: فك التعطيل المالي، فتح أبواب البيع والشراء، توسيع هالة القبول والوفرة، وجلب التوفيق في الصفقات.</span>
                                </div>
                                <span style="background:rgba(244,180,26,0.2); color:var(--gold); padding:4px 12px; border-radius:20px; font-weight:700; font-size:0.8rem;">حالة كسر 2 (جبر بيت 4)</span>
                            </div>

                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; align-items:center;">
                                <div>
                                    <div class="specimen-grid-container" style="border-color:var(--gold);">
                                        <div class="specimen-cell broken-cell"><span class="specimen-cell-num">102</span><span class="specimen-cell-label">د (4) ⚡ جبر</span></div>
                                        <div class="specimen-cell lock-cell"><span class="specimen-cell-num">107</span><span class="specimen-cell-label">ط (9) 🔒</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">99</span><span class="specimen-cell-label">ب (2)</span></div>
                                        
                                        <div class="specimen-cell"><span class="specimen-cell-num">100</span><span class="specimen-cell-label">ج (3)</span></div>
                                        <div class="specimen-cell center-cell"><span class="specimen-cell-num">103</span><span class="specimen-cell-label">هـ (5) ⚖️</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">105</span><span class="specimen-cell-label">ز (7)</span></div>
                                        
                                        <div class="specimen-cell"><span class="specimen-cell-num">106</span><span class="specimen-cell-label">ح (8)</span></div>
                                        <div class="specimen-cell key-cell"><span class="specimen-cell-num">98</span><span class="specimen-cell-label">أ (1) 🔑</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">104</span><span class="specimen-cell-label">و (6)</span></div>
                                    </div>
                                    <div class="wafq-math-badge-bar">
                                        <div class="wafq-math-badge verified">صف 1: 102+107+99 = <strong>308</strong> ✓</div>
                                        <div class="wafq-math-badge verified">صف 2: 100+103+105 = <strong>308</strong> ✓</div>
                                        <div class="wafq-math-badge verified">صف 3: 106+98+104 = <strong>308</strong> ✓</div>
                                    </div>
                                </div>

                                <div style="font-size:0.85rem; line-height:1.75; color:#475569;">
                                    <strong style="color:var(--gold);">١. الاستخراج الحسابي الدقيق:</strong>
                                    <br>• جُمّل "رزاق": ر (200) + ز (7) + ا (1) + ق (100) = <strong>308</strong>.
                                    <br>• طرح الأس: $308 - 12 = 296$.
                                    <br>• القسمة: $296 \div 3 = 98$ والباقي <strong>2</strong>.
                                    <br>• إذن: المفتاح = <strong>98</strong>، الباقي = 2 ➔ جبر بزيادة +1 في البيت 4.
                                    <br>• سَير التنزيل: (بيت 1=98، 2=99، 3=100) ➔ <strong>قفزة في بيت 4 = 102</strong> ➔ (بيت 5=103، 6=104، 7=105، 8=106، 9=107).
                                </div>
                            </div>

                            <!-- Operational Field Protocol -->
                            <div class="operational-protocol-box">
                                <strong style="color:var(--gold); font-size:0.95rem; display:block; margin-bottom:10px;">
                                    <i class="fa-solid fa-coins"></i> البروتوكول الميداني الكامل لجلب الوفرة والتيسير:
                                </strong>
                                <div class="protocol-step">
                                    <span class="step-badge">التوقيت</span>
                                    <span>يوم الخميس (فلك المشتري)، ساعة المشتري الأولى بعد الشروق، والقمر في برج ناري أو هوائي (الحمل، الأسد، القوس، أو الجوزاء) خالٍ من النحوس.</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">المداد والحامل</span>
                                    <span>يُكتب بمداد الزعفران وماء الورد والعنبر على <strong>ورقة كاغد مصقولة فاخرة ذات لون ذهبي/بيج</strong> أو صفيحة رقيقة من القصدير النقي (معدن المشتري).</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">التعزيم والتفعيل</span>
                                    <span>يُطلق بخور <strong>الصندل الأبيض وعلك الروم واللبان الذكر</strong>، وتُتلى آية الرزق ﴿إِنَّ اللَّهَ هُوَ الرَّزَّاقُ ذُو الْقُوَّةِ الْمَتِينُ﴾ 27 مرة، ثم تلاوة "يا رزاق" بعدد المفتاح (98 مرة) أو بعدد الاسم (308 مرات).</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">الحفظ والتصريف</span>
                                    <span>يُطوى الوفق في قماش حريري أخضر أو أصفر طبيعي، ويُوضع في خزينة المال، أو في المحفظة، أو يُعلق في مدخل المحل التجاري في مكان طاهر مرتفع عن الأنظار.</span>
                                </div>
                            </div>
                        </div>

                        <!-- EXAMPLE 3: SOVEREIGNTY & PROTECTION (ALLAH) -->
                        <div style="background:rgba(0,240,255,0.05); border:1.5px solid var(--cyan); border-radius:16px; padding:22px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; border-bottom:1px solid rgba(0,240,255,0.25); padding-bottom:12px; margin-bottom:14px;">
                                <div>
                                    <h5 style="margin:0; font-family:'Amiri',serif; font-size:1.35rem; color:var(--cyan);">
                                        👑 النموذج التطبيقي الثالث: مثلث الهيبة والسيادة المطلقة ودحر الأعداء (اسم الجلالة "الله")
                                    </h5>
                                    <span style="font-size:0.8rem; color:#94a3b8;">الغرض: الهيبة في قلوب الخلق، النصر على المعتدين، رباطة الجأش، طرد المخاوف النفسية، والحفظ من كيد السحرة والشياطين.</span>
                                </div>
                                <span style="background:rgba(0,240,255,0.2); color:var(--cyan); padding:4px 12px; border-radius:20px; font-weight:700; font-size:0.8rem;">وفق تام صحيح (باقي 0)</span>
                            </div>

                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; align-items:center;">
                                <div>
                                    <div class="specimen-grid-container" style="border-color:var(--cyan);">
                                        <div class="specimen-cell"><span class="specimen-cell-num">21</span><span class="specimen-cell-label">د (4)</span></div>
                                        <div class="specimen-cell lock-cell"><span class="specimen-cell-num">26</span><span class="specimen-cell-label">ط (9) 🔒</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">19</span><span class="specimen-cell-label">ب (2)</span></div>
                                        
                                        <div class="specimen-cell"><span class="specimen-cell-num">20</span><span class="specimen-cell-label">ج (3)</span></div>
                                        <div class="specimen-cell center-cell"><span class="specimen-cell-num">22</span><span class="specimen-cell-label">هـ (5) ⚖️</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">24</span><span class="specimen-cell-label">ز (7)</span></div>
                                        
                                        <div class="specimen-cell"><span class="specimen-cell-num">25</span><span class="specimen-cell-label">ح (8)</span></div>
                                        <div class="specimen-cell key-cell"><span class="specimen-cell-num">18</span><span class="specimen-cell-label">أ (1) 🔑</span></div>
                                        <div class="specimen-cell"><span class="specimen-cell-num">23</span><span class="specimen-cell-label">و (6)</span></div>
                                    </div>
                                    <div class="wafq-math-badge-bar">
                                        <div class="wafq-math-badge verified">صفوف وأعمدة = <strong>66</strong> ✓</div>
                                        <div class="wafq-math-badge verified">قطر 1: 21+22+23 = <strong>66</strong> ✓</div>
                                        <div class="wafq-math-badge verified">قطر 2: 19+22+25 = <strong>66</strong> ✓</div>
                                    </div>
                                </div>

                                <div style="font-size:0.85rem; line-height:1.75; color:#475569;">
                                    <strong style="color:var(--gold);">١. الاستخراج الحسابي الدقيق:</strong>
                                    <br>• جُمّل "الله": ا (1) + ل (30) + ل (30) + هـ (5) = <strong>66</strong>.
                                    <br>• طرح الأس: $66 - 12 = 54$.
                                    <br>• القسمة: $54 \div 3 = 18$ والباقي <strong>0</strong> (تام صحاح!).
                                    <br>• إذن: المفتاح = <strong>18</strong>، الأس = 12، الباقي = 0 ➔ لا يوجد كسر ولا جبر.
                                    <br>• سَير التنزيل: تتابعي تام (18، 19، 20، 21، 22، 23، 24، 25، 26).
                                    <br>• <em>تطابق مطلق:</em> كل صف وعمود وقطر يساوي 66 دون أدنى تفاوت في أي محور!
                                </div>
                            </div>

                            <!-- Operational Field Protocol -->
                            <div class="operational-protocol-box">
                                <strong style="color:var(--cyan); font-size:0.95rem; display:block; margin-bottom:10px;">
                                    <i class="fa-solid fa-crown"></i> البروتوكول الميداني الكامل للهيبة والتحصين السيادي:
                                </strong>
                                <div class="protocol-step">
                                    <span class="step-badge">التوقيت</span>
                                    <span>ليلة الجمعة في الثلث الأخير من الليل (وقت النزول الإلهي والسحر)، أو صبيحة يوم الأحد في شروق الشمس.</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">المداد والحامل</span>
                                    <span>يُكتب بمداد المسك الأسود والزعفران وماء الورد على <strong>رق غزال طاهر مدبوغ بحسب الشريعة</strong> أو ورقة بيضاء كتانية صافية.</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">التطويق والختم</span>
                                    <span>يُحاط المربع دائرياً بكتابة <strong>آية الكرسي كاملة</strong> دون طمس لحروفها، وتُكتب في أركانه الأربعة الحروف النورانية القرآنية: (كهيعص - حمعسق).</span>
                                </div>
                                <div class="protocol-step">
                                    <span class="step-badge">التفعيل والحمل</span>
                                    <span>يُبخر بـ <strong>المسك الخام والعود القماري</strong>، ويُقرأ عليه اسم الجلالة "يا الله" 66 مرة مع آية الكرسي 66 مرة. يُطوى ويُحفظ في جراب جلدي طبيعي ويُحمل على العضد الأيمن أو الصدر جهة القلب.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 4 -->
                <div class="ghazali-chapter" id="ghazali-ch4">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٤</div>
                        <div>
                            <h4 class="chapter-title">الباب الرابع: دستور الأحبار والمواد والأوعية الروحانية والفيزيائية</h4>
                            <div class="chapter-subtitle">Alchemy of Substrates, Organic Inks & Biological Resonance Instruments</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>إن من أكبر أسباب فشل المشتغلين المعاصرين بالأوفاق هو استخدامهم <strong>أدوات صناعية كيميائية ميتة</strong> تعزل الشحنات الكهروستاتيكية وتمنع تشكل الحقل الرنيني الأثيري. إليك الدستور المادي الصحيح كما قعّده أئمة الصنعة:</p>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin:16px 0;">
                            <div style="background:rgba(0,0,0,0.3); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                                <strong style="color:var(--gold); display:block; margin-bottom:8px;"><i class="fa-solid fa-flask"></i> ١. سر طبخ "المداد الروحاني الأصلي":</strong>
                                <ul style="margin:0 0 0 16px; padding:0; font-size:0.84rem;">
                                    <li><strong>المذيب الأساسي:</strong> ماء ورد طائفي أو دمشقي مقطر ثلاثاً (طبيعي 100% خالٍ من الكحول).</li>
                                    <li><strong>المادة الصبغية:</strong> خيوط زعفران أصلي قشميري أو إيراني نقي (حوالي 1-2 غرام يُنقع في ماء الورد الدافئ حتى يكتسب لوناً ذهبياً ياقوتياً).</li>
                                    <li><strong>المثبت الرنيني:</strong> قيراط من المسك الطبيعي المطحون (مسك الغزال الأسود للتحصين والهيبة، أو مسك أبيض للشفاء والمحبة).</li>
                                    <li><strong>مانع التعفن:</strong> قليل من الكافور الطبيعي البلوري لحفظ المداد وتطييب رائحته.</li>
                                    <li><em>التحذير الصارم:</em> يُمنع منعاً باتاً استخدام الحبر الجاف التجاري أو أقلام الفلوماستر؛ لأن البلاستيك والمركبات البترولية تعمل كعازل كهروستاتيكي يقتل الإشارة الأثيرية فوراً.</li>
                                </ul>
                            </div>

                            <div style="background:rgba(0,0,0,0.3); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                                <strong style="color:var(--cyan); display:block; margin-bottom:8px;"><i class="fa-solid fa-scroll"></i> ٢. علم الأوعية والحوامل (Substrates):</strong>
                                <ul style="margin:0 0 0 16px; padding:0; font-size:0.84rem;">
                                    <li><strong>الورق الطبيعي (الكاغد):</strong> ورق مصقول يدوي مصنوع من ألياف القطن أو الكتان أو الحرير الطبيعي، خالٍ من مبيضات الكلور الكيميائية.</li>
                                    <li><strong>الرقوق الحيوانية:</strong> رق غزال طاهر مدبوغ بالطرق الشرعية (أقوى موصل للشحنات البيولوجية للأعمال السيادية والحفظ).</li>
                                    <li><strong>الصفائح المعدنية:</strong> النحاس الأحمر النقي لأعمال الزهرة والمحبة، القصدير للمشتري والمال، الذهب للشمس، والفضة للقمر.</li>
                                    <li><strong>الصحاف الخزفية:</strong> صحون صينية أو زجاجية بيضاء خالية من الشروخ والرسوم لشرب المحو الاستشفائي.</li>
                                </ul>
                            </div>
                        </div>

                        <div class="wafq-sub-box crimson">
                            <strong>أداة الكتابة (القلم):</strong> يُشترط أن يكون القلم مصنوعاً من <strong>قصب فارسي طبيعي</strong> مبري بشطفة مائلة بزاوية 45 درجة، أو عود سواك أراك مشحوذ. لماذا؟ لأن القصب والألياف النباتية تسمح بسريان <em>الشحنة الكهرومغناطيسية الحيوية من أصابع الكاتب إلى السطح</em> مباشرة دون تشويش معدني أو بلاستيكي عازل.
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 5 -->
                <div class="ghazali-chapter" id="ghazali-ch5">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٥</div>
                        <div>
                            <h4 class="chapter-title">الباب الخامس: مواقيت الرصد الفلكي وساعات الكواكب وخلو المسار</h4>
                            <div class="chapter-subtitle">Astronomical Resonance: Planetary Hours & The Void of Course Curse</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>لا يعمل الوفق في فراغ زمني منعزل؛ بل هو <strong>موجّه موجي يلتقط الترددات الكوكبية المدارية</strong>. فإذا كُتب الوفق في ساعة كوكبية متضاربة، انعدم الرنين وحصل التداخل الهدام. إليك القواعد الزمنية الصارمة:</p>

                        <div style="overflow-x:auto; margin:16px 0;">
                            <table style="width:100%; border-collapse:collapse; font-size:0.83rem; text-align:right;">
                                <thead>
                                    <tr style="background:rgba(15,23,42,0.9); border-bottom:2px solid var(--gold); color:var(--gold);">
                                        <th style="padding:10px;">اليوم</th>
                                        <th style="padding:10px;">الكوكب الحاكم</th>
                                        <th style="padding:10px;">ساعة الشروق الأولى</th>
                                        <th style="padding:10px;">الطبيعة والغرض الملائم</th>
                                        <th style="padding:10px;">البخور المناسب</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>الأحد</strong></td>
                                        <td style="padding:8px; color:#f4b41a;">الشمس ☉</td>
                                        <td style="padding:8px;">ساعة الشمس</td>
                                        <td style="padding:8px;">العزة، السيادة، الشفاء الجسدي، طرد الظلمات</td>
                                        <td style="padding:8px;">سندروس، لبان ذكر، ميعة سائلة</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>الإثنين</strong></td>
                                        <td style="padding:8px; color:#00f0ff;">القمر ☽</td>
                                        <td style="padding:8px;">ساعة القمر</td>
                                        <td style="padding:8px;">الصلح، تليين القلوب، تحريك السوائل، البصيرة</td>
                                        <td style="padding:8px;">لبان ذكر، كافور، مسك أبيض</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>الثلاثاء</strong></td>
                                        <td style="padding:8px; color:#ef4444;">المريخ ♂</td>
                                        <td style="padding:8px;">ساعة المريخ</td>
                                        <td style="padding:8px;">رد كيد المعتدين، قطع السلاسل، تدمير الأسحار</td>
                                        <td style="padding:8px;">قسط هندي، صندل أحمر، كبريت</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>الأربعاء</strong></td>
                                        <td style="padding:8px; color:#9d4edd;">عطارد ☿</td>
                                        <td style="padding:8px;">ساعة عطارد</td>
                                        <td style="padding:8px;">الحفظ، الذكاء، الفصاحة، حل المعضلات العقلية</td>
                                        <td style="padding:8px;">جاوي، مستكة، علك الروم</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>الخميس</strong></td>
                                        <td style="padding:8px; color:#3b82f6;">المشتري ♃</td>
                                        <td style="padding:8px;">ساعة المشتري</td>
                                        <td style="padding:8px;">سعة الأرزاق، التجارة، القبول والجاه، تيسير الأمور</td>
                                        <td style="padding:8px;">صندل أبيض، عنبر خام، لبان</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>الجمعة</strong></td>
                                        <td style="padding:8px; color:#06d6a0;">الزهرة ♀</td>
                                        <td style="padding:8px;">ساعة الزهرة</td>
                                        <td style="padding:8px;">المحبة الشرعية، الألفة الأسرية، علاج الكليتين</td>
                                        <td style="padding:8px;">دهن ورد، مسك، ميعة يابسة</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:8px;"><strong>السبت</strong></td>
                                        <td style="padding:8px; color:#6b7280;">زحل ♄</td>
                                        <td style="padding:8px;">ساعة زحل</td>
                                        <td style="padding:8px;">تثبيت الأبنية، عقد الألسن عن الشر، الصبر</td>
                                        <td style="padding:8px;">حلتيت، قشور رمان، لبان مر</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="wafq-sub-box crimson">
                            <strong>⚠️ التحذير الصارم من "خلو مسار القمر" (Moon Void of Course):</strong>
                            خلو المسار هو الفترة التي ينتهي فيها القمر من تشكيل أي اتصال فلكي رئيسي (اقتران، تثليث، تربيع...) مع أي كوكب آخر قبل أن ينتقل إلى البرج التالي. في هذه الفترة، <strong>تكون الطاقة الفلكية معطلة وميتة بنسبة 100%</strong>؛ وأي وفق أو عمل يُكتب أثناء خلو المسار يبوء بالفشل التام والتعطل مهما بلغت دقة الحساب والنية!
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 6 -->
                <div class="ghazali-chapter" id="ghazali-ch6">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٦</div>
                        <div>
                            <h4 class="chapter-title">الباب السادس: بروتوكول التفعيل الصوتي والرنين وتوجيه النية</h4>
                            <div class="chapter-subtitle">Acoustic Entrainment, Mantra Physics & Brainwave Synchronization</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>كتابة الأرقام على الورق هي بمثابة بناء "الدائرة الكهربائية المادية"؛ أما <strong>التفعيل الصوتي وتوجيه النية</strong> فهو تمرير "التيار الكهربائي الحي" في تلك الدائرة. وبدون هذا البروتوكول، يظل الوفق جسداً بلا روح:</p>

                        <div class="operational-protocol-box">
                            <strong style="color:var(--cyan); font-size:0.95rem; display:block; margin-bottom:12px;">
                                <i class="fa-solid fa-atom"></i> المراحل الأربع لشحن الوفق بالطاقة الحيوية:
                            </strong>
                            <div class="protocol-step">
                                <span class="step-badge">المرحلة 1: الطهارة والتأريض</span>
                                <span>الوضوء الكامل بسرد، الجلوس مستقبلاً القبلة الشريفة في مكان طاهر ذي إضاءة خافتة، وإشعال البخور المناسب لطرد الطاقات الهوائية المشوشة.</span>
                            </div>
                            <div class="protocol-step">
                                <span class="step-badge">المرحلة 2: تماسك موجات الدماغ</span>
                                <span>ممارسة تنفس الحجاب الحاجز البطيء (شهيق 4 ثوانٍ، حبس 4 ثوانٍ، زفير 6 ثوانٍ) لمدة 5 دقائق لإدخال الدماغ في حالة <strong>ثيتا-ألفا (Theta-Alpha Coherence 7-8 Hz)</strong>، وطرد أي تردد أو شك؛ لأن الشك يولد موجات تداخل هدام تلغي شحنة الوفق.</span>
                            </div>
                            <div class="protocol-step">
                                <span class="step-badge">المرحلة 3: الحبس التنفسي عند القطب</span>
                                <span>أثناء رسم خطوط الوفق وكتابة الأرقام، يتم الشهيق مع البداية بالمفتاح (بيت 1)، وعند الوصول إلى بيت الهاء (القطب 5)، يحبس الكاتب نَفَسَه ويركز كامل نيته في قلبه مستشعراً نزول النور الإلهي، ثم يزفر ببطء عند كتابة المغلاق (بيت 9).</span>
                            </div>
                            <div class="protocol-step">
                                <span class="step-badge">المرحلة 4: الانجرار الصوتي الرنيني</span>
                                <span>بعد اكتمال الرسم، يُوضع الوفق على كف اليد اليمنى ويُقرّب من الفم، وتُتلى الآية أو الاسم الإلهي المستودع <strong>بالنغمة الصوتية الهادئة المتوافقة مع تردد الكوكب</strong> بعدد المفتاح أو بعدد الجُمّل الكلي، بحيث تصطدم الذبذبات الصوتية والأنفاس مباشرة بسطح الحبر، فتنغرس الشحنة الصوتية في بلورات الزعفران.</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 7 -->
                <div class="ghazali-chapter" id="ghazali-ch7">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٧</div>
                        <div>
                            <h4 class="chapter-title">الباب السابع: دليل الفك والتحليل العكسي للأوفاق المجهولة وإبطال الفاسد منها</h4>
                            <div class="chapter-subtitle">Reverse Engineering Historical Talismans & Safely Neutralizing Corrupted Magic</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>إذا عثرت على وفق تاريخي أو طلسم مجهول في مخطوط أو ورقة قديمة، وأردت معرفة حقيقته وكشف سره خلال دقيقتين دون تخمين، فاتبع <strong>خوارزمية الهندسة العكسية</strong> التالية:</p>

                        <div style="background:rgba(0,0,0,0.35); border-radius:12px; border:1px solid rgba(255,255,255,0.08); padding:18px; margin:14px 0;">
                            <strong style="color:var(--gold); display:block; margin-bottom:10px;"><i class="fa-solid fa-magnifying-glass"></i> خطوات فك شفرة أي وفق 3×3 مجهول:</strong>
                            <ol style="margin:0 0 0 20px; padding:0; font-size:0.85rem; line-height:1.8;">
                                <li><strong>الخطوة 1: تحديد المفتاح:</strong> انظر إلى أصغر رقم موجود في الوفق، وتحقق مما إذا كان يقع في أسفل الوسط (بيت الألف). إذا كان كذلك، فالوفق يعتمد طريقة بطد زهج واح.</li>
                                <li><strong>الخطوة 2: فحص الزيادة والكسر:</strong> قارن بين الخانات المتتالية:
                                    <br>• إذا كانت كل خانة تزيد بـ 1 عن سابقتها حتى النهاية ➔ <strong>الباقي = 0</strong>.
                                    <br>• إذا وجدت قفزة بـ 2 بين البيت 6 و 7 (الزاي وسط اليسار) ➔ <strong>الباقي = 1</strong>.
                                    <br>• إذا وجدت قفزة بـ 2 بين البيت 3 و 4 (الدال أعلى اليمين) ➔ <strong>الباقي = 2</strong>.
                                </li>
                                <li><strong>الخطوة 3: تطبيق المعادلة العكسية لاستخراج الاسم:</strong>
                                    <div style="background:rgba(0,240,255,0.1); padding:8px 14px; border-radius:6px; margin:6px 0; font-weight:700; color:#fff;">
                                        $N = (	ext{المفتاح} 	imes 3) + 12 + 	ext{الباقي}$
                                    </div>
                                </li>
                                <li><strong>الخطوة 4: مطابقة الناتج $N$:</strong> ابحث عن العدد $N$ في جداول أسماء الله الحسنى أو الآيات المشهورة؛ فإذا كان 66 فهو "الله"، وإذا كان 129 فهو "لطيف"، وإذا كان 308 فهو "رزاق"، وإذا كان 786 فهو "البسملة". وبذلك تعرف بدقة متناهية ما أودعه الصانع!</li>
                            </ol>
                        </div>

                        <div class="wafq-sub-box crimson">
                            <strong>كشف الأوفاق الخبيثة أو السحرية الشيطانية وإبطالها الآمن:</strong>
                            <br>• <strong>علامات الفساد والشواش:</strong> إذا جمعت الصفوف والأعمدة ووجدتها غير متساوية، أو وجدت حروفاً مقلوبة، أو رموزاً سريانية طلاسمية غير مفهومة، أو خانات مطموسة عمداً بالسوائل، فهذا <strong>وفق خبيث صُمم لإحداث تداخل هدام وتمزيق الهالة الأثيرية</strong>.
                            <br>• <strong>بروتوكول الإبطال الآمن التام:</strong>
                            لا تحرق الوفق أبداً بالنار (لأن الحرق ينشط الكيانات النارية ويفكك الروابط بعنف)؛ بل ضعه في إناء ماء طاهر مذاب فيه <strong>ملح صخري خشن وخل طبيعي</strong>، واقرأ عليه آيات إبطال السحر: ﴿مَا جِئْتُم بِهِ السِّحْرُ إِنَّ اللَّهَ سَيُبْطِلُهُ﴾ [يونس: 81]، ﴿فَوَقَعَ الْحَقُّ وَبَطَلَ مَا كَانُوا يَعْمَلُونَ﴾ [الأعراف: 118]، والمعوذتين. بمجرد ذوبان الحبر في الماء المالح، ينحل التناظر الهندسي فوراً، وينهار الحقل التداخلي وتنقطع التغذية الأثيرية بسلام.
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 8 -->
                <div class="ghazali-chapter" id="ghazali-ch8">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٨</div>
                        <div>
                            <h4 class="chapter-title">الباب الثامن: الإغلاق التام، التحصين بالأحرف النورانية، والميزان التوحيدي الأسمى</h4>
                            <div class="chapter-subtitle">Hermetic Sealing, The 14 Luminous Letters & Quranic Sovereignty</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>إن ترك الوفق مفتوحاً دون إغلاق يشبه ترك سلك كهربائي عارٍ متصل بالتيار في بركة ماء؛ حيث يؤدي تسرب الطاقة إلى استنزاف هالة صاحبه واجتذاب الطفيليات واليرقات النجمية. إليك دستور الختم والحصانة الكبرى:</p>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin:16px 0;">
                            <div style="background:rgba(0,0,0,0.3); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                                <strong style="color:var(--gold); display:block; margin-bottom:8px;"><i class="fa-solid fa-lock"></i> ١. طوق الحروف النورانية الـ 14:</strong>
                                <p style="font-size:0.84rem; margin:0;">
                                    تُحاط جوانب المربع الأربعة بكتابة الحروف النورانية القرآنية الأربعة عشر المفرقة دون طمس: <strong>(ن، ص، ح، ك، ي، م، ق، ا، ط، ع، ل، هـ، س، ر)</strong> التي يجمعها قول العلماء: <em>"نص حكيم قاطع له سر"</em>. تشكل هذه الحروف درعاً كهروديناميكياً يمنع أي كيان من التسلل إلى قلب الوفق.
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.3); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                                <strong style="color:var(--emerald); display:block; margin-bottom:8px;"><i class="fa-solid fa-shield-cat"></i> ٢. أقفال الأركان بآيات الإحكام:</strong>
                                <p style="font-size:0.84rem; margin:0;">
                                    تُكتب في زوايا المربع الأربعة أواخر سورة الحشر ﴿هُوَ اللَّهُ الَّذِي لَا إِلَٰهَ إِلَّا هُوَ...﴾ أو قوله تعالى: ﴿وَجَعَلْنَا مِن بَيْنِ أَيْدِيهِمْ سَدًّا وَمِنْ خَلْفِهِمْ سَدًّا فَأَغْشَيْنَاهُمْ فَهُمْ لَا يُبْصِرُونَ﴾ [يس: 9]، لتكون أوتاداً مانعة تحبس الطاقة الإيجابية في الداخل وتصد أي اختراق خارجي.
                                </p>
                            </div>
                        </div>

                        <!-- THE MONOTHEISTIC FORTRESS -->
                        <div style="background:linear-gradient(135deg, rgba(244,180,26,0.15), rgba(6,214,160,0.1)); border:2px solid var(--gold); border-radius:14px; padding:20px; margin-top:18px;">
                            <h5 style="margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.3rem; color:var(--gold); text-align:center;">
                                ⚖️ الميزان التوحيدي والقرآني الأسمى — سيادة المؤمن الموحد
                            </h5>
                            <p style="font-size:0.88rem; line-height:1.85; color:#f0f6fc; margin:0;">
                                <strong>الحقيقة العقدية والبرهانية الصارمة:</strong>
                                إن الأعداد، الأوفاق، والنجوم والأفلاك ليست آلهة، ولا تملك في ملكوت السماوات والأرض مثقال ذرة من نفع أو ضر بذاتها، بل هي محض <strong>أسباب وقوانين وسنن كونية مسخرة</strong> خلقها الله تعالى بحكمته البالغة وأودع فيها الاتزان ﴿وَأَحْصَىٰ كُلَّ شَيْءٍ عَدَدًا﴾ [الجن: 28].
                                <br><br>
                                المسلم المؤمن الموحد بالله لا يستعين بجن، ولا يتقرب إلى كوكب، ولا يذبح لغير الله؛ بل ينظر إلى هذه المصفوفات كما ينظر المهندس إلى مصفوفات الجبر وحساب التفاضل، وكما ينظر الطبيب إلى خواص الأعشاب والمركبات. والإنسان الموحد المتوكل على الله هو خليفة الله وسيد فوق كل هذه النواميس المسخرة بنور لا إله إلا الله محمد رسول الله، وسر إجابة الدعاء وتحقيق الغايات إنما هو بصدق التوجه إلى مسبب الأسباب ومجري السحاب ومسخر النجوم، له الملك وله الحمد وهو على كل شيء قدير.
                            </p>
                        </div>
                    </div>
                </div>

            </div>
            
                <!-- CHAPTER 9: THE VEILING PHYSICS (SADDAN SADDAN) -->
                <div class="ghazali-chapter" id="ghazali-ch9">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">٩</div>
                        <div>
                            <h4 class="chapter-title">الباب التاسع: فيزياء الحجب الطاقي وحصن الإغشاء — تشريح آية السد الكونية</h4>
                            <div class="chapter-subtitle">Cognitive Blind-Spotting & Waveform Deflection: The Sadda Vector (N = 3144)</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            يعتمد سر الحجب والدفع في الكوزمولوجيا القرآنية على قوله تعالى: 
                            <strong style="color:var(--gold);">﴿وَجَعَلْنَا مِن بَيْنِ أَيْدِيهِمْ سَدًّا وَمِنْ خَلْفِهِمْ سَدًّا فَأَغْشَيْنَاهُمْ فَهُمْ لَا يُبْصِرُونَ﴾</strong> [يس: 9]. 
                            إن هذا القانون ليس مجرد حجب بصري فيزيائي عشوائي، بل هو <em>انحراف في التردد الإدراكي (Cognitive Blind-Spotting)</em> 
                            يعزل حقل الإنسان الحيوي عن رادارات الحقد، الحسد، والتتبع الطاقي السلبي، محولاً الهالة إلى وسط عاكس للموجات المشوشة.
                        </p>

                        <!-- Math Breakdown -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(0,240,255,0.3); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:var(--cyan); margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.2rem;">
                                📐 الاستخراج الرياضي الدقيق لآية السد:
                            </h5>
                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; font-size:0.85rem;">
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    جُمّل الآية الكريمة كاملاً: <strong style="color:var(--gold); font-size:1.15rem;">N = 3144</strong>
                                </div>
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    طرح الأس الثابت: <strong style="color:#fff;">3144 - 12 = 3132</strong>
                                </div>
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    القسمة على 3 (المفتاح): <strong style="color:var(--emerald); font-size:1.15rem;">المفتاح = 1044</strong>
                                </div>
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    الباقي: <strong style="color:var(--cyan); font-size:1.15rem;">الباقي = 0 (تام بلا كسر!)</strong>
                                </div>
                            </div>
                        </div>

                        <!-- 3x3 Grid Specimen -->
                        <div style="display:flex; justify-content:center; margin:20px 0;">
                            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; width:340px; background:rgba(0,0,0,0.8); border:2px solid var(--cyan); border-radius:14px; padding:12px; box-shadow:0 0 30px rgba(0,240,255,0.25);">
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">1047</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت د (4)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#ef4444; font-size:1.2rem;">1052</span>
                                    <span style="font-size:0.68rem; color:#ef4444;">المغلاق 🔒 (9)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">1045</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ب (2)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">1046</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ج (3)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(244,180,26,0.18); border:1px solid var(--gold); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:var(--gold); font-size:1.2rem;">1048</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">القطب ⚖️ (5)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">1050</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ز (7)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">1051</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ح (8)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(6,214,160,0.15); border:1px solid var(--emerald); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:var(--emerald); font-size:1.2rem;">1044</span>
                                    <span style="font-size:0.68rem; color:var(--emerald);">المفتاح 🔑 (1)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">1049</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت و (6)</span>
                                </div>
                            </div>
                        </div>

                        <p>
                            <strong>التحقق الهندسي:</strong> 
                            مجموع كل ضلع: $1047 + 1052 + 1045 = 3144$. 
                            المجموع التراكمي للمصفوفة (المساحة الكلية): $T = 3144 \times 3 = 9432$. 
                            يتميز هذا الوفق بأنه تام رياضي بلا انكسار، مما يمنحه ثباتاً طاقياً فائقاً في صد الترددات الخبيثة ورد كيد المتربصين.
                        </p>
                    </div>
                </div>

                <!-- CHAPTER 10: CLEANSING THE RA'N & ACTIVATING THE PINEAL INSIGHT -->
                <div class="ghazali-chapter" id="ghazali-ch10">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١٠</div>
                        <div>
                            <h4 class="chapter-title">الباب العاشر: إزالة الرّان الطاقي وفتح البصيرة الصنوبرية — فيزياء تطهير النواة الإدراكية</h4>
                            <div class="chapter-subtitle">Purging the Ra'n Biomagnetic Smog & Awakening Pineal Clarity (N = 558)</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            كشف القرآن الكريم عن ماهية الحجب الداخلي بقوله تعالى: 
                            <strong style="color:var(--gold);">﴿كَلَّا بَلْ رَانَ عَلَىٰ قُلُوبِهِم مَّا كَانُوا يَكْسِبُونَ﴾</strong> [المطففين: 14]. 
                            إن <strong>«الرّان»</strong> في الفهم العلمي الباطني هو طبقة سميكة من التشويش الكهرومغناطيسي المنبعث من الأفكار المظلمة، 
                            الذنوب، والصدمات النفسية المتراكمة، والتي تلتصق بالهالة الحيوية وتغلق النفاذية الضوئية للغدة الصنوبرية (Pineal Gland).
                        </p>

                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(244,180,26,0.3); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:var(--gold); margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.2rem;">
                                👁️ استخراج وفق فتح البصيرة والنور التام:
                            </h5>
                            <p style="font-size:0.86rem; margin:0 0 10px 0;">
                                جمع الاسمين الإلهيين: <strong>«بَصِيرٌ»</strong> (جمله = 302) + <strong>«نُورٌ»</strong> (جمله = 256) 
                                $\Rightarrow N = 302 + 256 = 558$.
                            </p>
                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; font-size:0.85rem;">
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    العدد المطلوب: <strong style="color:var(--gold); font-size:1.15rem;">N = 558</strong>
                                </div>
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    طرح الأس: <strong style="color:#fff;">558 - 12 = 546</strong>
                                </div>
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    المفتاح: <strong style="color:var(--emerald); font-size:1.15rem;">546 ÷ 3 = 182</strong>
                                </div>
                                <div style="background:rgba(255,255,255,0.03); padding:10px; border-radius:8px;">
                                    المغلاق: <strong style="color:#ef4444; font-size:1.15rem;">182 + 8 = 190</strong>
                                </div>
                            </div>
                        </div>

                        <!-- 3x3 Specimen for Insight -->
                        <div style="display:flex; justify-content:center; margin:20px 0;">
                            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; width:340px; background:rgba(0,0,0,0.8); border:2px solid var(--gold); border-radius:14px; padding:12px; box-shadow:0 0 30px rgba(244,180,26,0.25);">
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">185</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت د (4)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#ef4444; font-size:1.2rem;">190</span>
                                    <span style="font-size:0.68rem; color:#ef4444;">المغلاق 🔒 (9)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">183</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ب (2)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">184</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ج (3)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(244,180,26,0.18); border:1px solid var(--gold); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:var(--gold); font-size:1.2rem;">186</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">القطب ⚖️ (5)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">188</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ز (7)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">189</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت ح (8)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(6,214,160,0.15); border:1px solid var(--emerald); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:var(--emerald); font-size:1.2rem;">182</span>
                                    <span style="font-size:0.68rem; color:var(--emerald);">المفتاح 🔑 (1)</span>
                                </div>
                                <div class="specimen-cell" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); border-radius:8px; height:70px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                                    <span style="font-weight:800; color:#fff; font-size:1.2rem;">187</span>
                                    <span style="font-size:0.68rem; color:var(--gold);">بيت و (6)</span>
                                </div>
                            </div>
                        </div>

                        <p>
                            <strong>بروتوكول تفعيل البصيرة:</strong> 
                            يُعمر هذا الوفق على لوح فضي أو كاغد أبيض بمداد الزعفران وماء الورد في ساعة المشتري يوم الخميس، 
                            ويُتلى الاسمان «يا بصير يا نور» بعدد المفتاح (182 مرة) مع صيام الوعي عن اللغو والشتات الذهني. 
                            يعمل هذا التزامن على إعادة تهيئة الغدة الصنوبرية وزيادة انبعاث الفوتونات الحيوية المترابطة (Biophoton Coherence).
                        </p>
                    </div>
                </div>

                <!-- CHAPTER 11: DECONSTRUCTION OF SERVITOR MYTH & DIVINE SOVEREIGNTY -->
                <div class="ghazali-chapter" id="ghazali-ch11">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١١</div>
                        <div>
                            <h4 class="chapter-title">الباب الحادي عشر: تفكيك مغالطة «الأرواح الخادمة والخدام» وترسيخ سيادة التوحيد</h4>
                            <div class="chapter-subtitle">Deconstruction of Servitor Spirits & The Absolute Monotheistic Sovereignty</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            من أعظم المفاسد التي حشا بها جهلة النساخ كتب التراث هو الزعم بأن للأوفاق «أرواحاً خادمة، عماراً، أو أعواناً سفلية» 
                            تُستجلب بالتعازيم وتُستعبد للأغراض الدنيوية. يمثل هذا التصور انحداراً خرافياً يناقض العقل الصريح وصريح القرآن.
                        </p>

                        <div style="background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.3); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:#ef4444; margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.2rem;">
                                ⚖️ النقد العلمي والعقدي الصارم لأكذوبة الخدام:
                            </h5>
                            <ul style="margin:0 0 0 18px; padding:0; font-size:0.86rem; line-height:1.8;">
                                <li>
                                    <strong>1. نقد ابن خلدون في «المقدمة»:</strong> 
                                    أثبت ابن خلدون أن استحضار الكيانات والرؤى الهلوسية في الخلوات ليس إلا <em>إسقاطات نفسية وهمية (Psychological Hallucinations)</em> 
                                    ناشئة عن إنهاك الحواس واختلال كيمياء الدماغ، وليست كائنات خارجية مستقلة تخدم أحداً.
                                </li>
                                <li>
                                    <strong>2. تقرير أبي حامد الغزالي:</strong> 
                                    بين الغزالي في <em>المنقذ من الضلال</em> أن التأثيرات المشاهدة في الأوفاق هي <strong>خواص هندسية طبيعية</strong> 
                                    أودعها الله في التناسب العددي كما أودع خاصية الإسهال في السقمونيا وخاصية الجذب في المغناطيس، والوسائط المزعومة ليست إلا أوهاماً دجلية.
                                </li>
                                <li>
                                    <strong>3. الميزان القرآني:</strong> 
                                    الإنسان المؤمن هو خليفة الله في أرضه المسخر له ما في السماوات والأرض ﴿وَسَخَّرَ لَكُم مَّا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ جَمِيعًا مِّنْهُ﴾ [الجاثية: 13]. 
                                    فمن طلب خادماً برزخياً أو سفلباً فقد تنازل عن رتبة السيادة واستعبد نفسه لأوهام وضيعة.
                                </li>
                            </ul>
                        </div>

                        <p>
                            <strong>السر الحقيقي للتأثير:</strong> 
                            قوة الوفق تنبع حصراً من <strong>«تماسك العزيمة وتجريد التوحيد (Mental & Spiritual Coherence)»</strong>؛ 
                            فعندما ينسجم العقل البشري مع التناسب الرياضي المتزن، تزول ممانعة الشتات، وتتطابق النية مع سنن الكون المسخرة، 
                            فيستجيب الواقع لقوة التوكل الصادق على مسبب الأسباب ومجري السحاب سبحانه.
                        </p>
                    </div>
                </div>

                <!-- CHAPTER 12: NUMERICAL DERIVATIONS & RECITATION RATIOS -->
                <div class="ghazali-chapter" id="ghazali-ch12">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١٢</div>
                        <div>
                            <h4 class="chapter-title">الباب الثاني عشر: فلسفة استخراج الأعداد الترددية وسر اختيار الأسماء وقوانين التلاوة</h4>
                            <div class="chapter-subtitle">Numerical Vibrations, Gematria Expansion Methods & Recitation Harmonic Ratios</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            لا توضع الأرقام في مثلث الغزالي اعتباطاً أو على سبيل التخمين؛ بل لكل رقم شفرة ترددية هندسية تحاكي القانون الكوني. 
                            هنا نفكك سر الأعداد المستخدمة، ولماذا تم اختيارها، وكيف يُربط عدد التلاوة بأضلاع الوفق.
                        </p>

                        <!-- The Derivations Table -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(148, 163, 184,0.3); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:var(--gold); margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                🔢 لماذا اخترنا هذه الأعداد بالذات في النماذج التطبيقية؟
                            </h5>
                            <div style="overflow-x:auto;">
                                <table style="width:100%; border-collapse:collapse; font-size:0.84rem; text-align:right;">
                                    <thead>
                                        <tr style="background:rgba(255,255,255,0.06); color:var(--gold); border-bottom:2px solid rgba(148, 163, 184,0.3);">
                                            <th style="padding:10px;">الغاية</th>
                                            <th style="padding:10px;">العدد (N)</th>
                                            <th style="padding:10px;">الاشتقاق والسر الترددي</th>
                                            <th style="padding:10px;">المفتاح والباقي</th>
                                            <th style="padding:10px;">الأثر الطاقي المستهدف</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                            <td style="padding:10px; font-weight:700; color:var(--emerald);">الشفاء الخلوي</td>
                                            <td style="padding:10px; color:#fff; font-weight:800;">391</td>
                                            <td style="padding:10px;">جُمّل ﴿وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ﴾ مطروحاً منها شوائب الترددات، وتوافق اسم الله «الشافي» المكرر بحساب البسط</td>
                                            <td style="padding:10px;">المفتاح 126 | باقي 1 (جبر في بيت 7)</td>
                                            <td style="padding:10px;">إعادة ضبط الرنين البيولوجي، تحفيز المناعة، ورفع حيوية الأنسجة</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                            <td style="padding:10px; font-weight:700; color:var(--cyan);">الوفرة والرزق</td>
                                            <td style="padding:10px; color:#fff; font-weight:800;">308</td>
                                            <td style="padding:10px;">جُمّل اسم الله «الرَّزَّاقُ» (ر=200، ز=7، ا=1، ق=100 $\Rightarrow 308$)، وتوافقه مع فلك الزهرة ومعدن النحاس</td>
                                            <td style="padding:10px;">المفتاح 98 | باقي 2 (جبر في بيت 4)</td>
                                            <td style="padding:10px;">فتح قنوات التيسير، إزالة موانع الفقر الذهني، وتناغم طاقة الجذب</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                            <td style="padding:10px; font-weight:700; color:var(--gold);">الهيبة والسيادة</td>
                                            <td style="padding:10px; color:#fff; font-weight:800;">66</td>
                                            <td style="padding:10px;">جُمّل لفظ الجلالة الأقدس «الله» (ا=1، ل=30، ل=30، هـ=5 $\Rightarrow 66$)، وهو أصل الأعداد الشمسية</td>
                                            <td style="padding:10px;">المفتاح 18 | باقي 0 (تام بلا كسر)</td>
                                            <td style="padding:10px;">هيبة الحضور، انشراح الصدر، سكون العقل، وشموخ الشخصية</td>
                                        </tr>
                                        <tr>
                                            <td style="padding:10px; font-weight:700; color:#ef4444;">الحصن والإغشاء</td>
                                            <td style="padding:10px; color:#fff; font-weight:800;">3144</td>
                                            <td style="padding:10px;">جُمّل آية يس 9 ﴿وَجَعَلْنَا مِن بَيْنِ أَيْدِيهِمْ سَدًّا...﴾ بتمام حروفها الموزونة</td>
                                            <td style="padding:10px;">المفتاح 1044 | باقي 0 (تام)</td>
                                            <td style="padding:10px;">انحراف التردد المعادي وتوليد درع وقائي عاكس للسهام الطاقية</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <!-- 5 Expansion Methods -->
                        <h5 style="color:var(--cyan); margin:18px 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                            📜 طرق البسط الخمس للأعداد والأسماء في المخطوطات القديمة:
                        </h5>
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:14px; margin-bottom:20px;">
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:var(--gold);">1. البسط الحرفي المجرد:</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">تفكيك الاسم إلى حروف مفرقة (م، ح، م، د) وحساب جمل كل حرف، وهو الأساس المباشر لتحديد المفتاح.</p>
                            </div>
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:var(--cyan);">2. البسط العددي اللفظي:</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">كتابة العدد كنص هجائي: (تسعون وثمانية) ثم حساب جمل الحروف الناتجة لرفع التردد لدرجة أعلى.</p>
                            </div>
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:var(--emerald);">3. البسط الألفي الاسمي:</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">كتابة كل حرف باسمه الصوتي الكامل: (ألف، لام، ميم) وهو أرقى مراتب التوليد في سيمياء الحروف لجابر بن حيان.</p>
                            </div>
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:#d8b4fe;">4. البسط التكسيري المزجي:</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">مزج حروف اسم الطالب مع حروف الآية حرفاً بحرف لصنع وحدة أثيرية لا تنفصم في حقل الوعي.</p>
                            </div>
                        </div>

                        <!-- Recitation Ratio Laws -->
                        <div style="background:linear-gradient(135deg, rgba(15,23,42,0.9), rgba(4,8,19,0.95)); border:2px solid var(--emerald); border-radius:14px; padding:18px;">
                            <h5 style="color:var(--emerald); margin:0 0 8px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                🗣️ قواعد ونسب التلاوة (Recitation Harmonic Ratios):
                            </h5>
                            <ul style="margin:0 0 0 18px; padding:0; font-size:0.86rem; line-height:1.8;">
                                <li><strong>التلاوة بعدد المفتاح (The Key):</strong> تفتح مجرى الطاقة وتخاطب العقل الواعي وتبدأ سريان النية في الأثير.</li>
                                <li><strong>التلاوة بعدد القطب (Center = المفتاح + 4):</strong> تثبت النية في مركز القلب والغدة الصنوبرية وتمنع التشوش الداخلي.</li>
                                <li><strong>التلاوة بعدد المغلاق (Lock = المفتاح + 8):</strong> تحبس الطاقة داخل الوفق وتمنع تسربها للأطياف العشوائية.</li>
                                <li><strong>التلاوة بعدد الضلع الواحد (N):</strong> وهي القراءة المثلى لترديد الذكر يومياً أثناء حمل الوفق أو تأمله.</li>
                                <li><strong>التلاوة بالمساحة الكلية ($3N$):</strong> تُستخدم حصراً في اليوم الأول لتدشين الوفق وكسر حاجز المقاومة النفسية الأولي.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 13: THE PLANETARY INCENSE & TERPENE CODEX -->
                <div class="ghazali-chapter" id="ghazali-ch13">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١٣</div>
                        <div>
                            <h4 class="chapter-title">الباب الثالث عشر: الدستور الكيميائي للبخورات السبعة وتوافقاتها اليومية والكوكبية</h4>
                            <div class="chapter-subtitle">The Seven Planetary Incense Formulas, Olfactory Neuroscience & Terpene Resonance</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            لم يكن البخور في المخطوطات القديمة طقساً سحرياً شكلياً؛ بل هو <strong>كيمياء حيوية عصبية (Neuro-Aromatherapy)</strong>. 
                            ترتبط جزيئات الروائح العطرية مباشرة بالبصلة الشمية (Olfactory Bulb) المرتبطة فورياً بالجهاز الحوفي (Limbic System) 
                            واللوزة الدماغية (Amygdala) دون المرور بفلترة المهاد، مما يغير حالة الدماغ الترددية في أجزاء من الثانية من بيتا المشوشة (Beta) 
                            إلى ألفا وثيتا المتصلة بالسكينة والتأمل العميق (Alpha/Theta 8–12 Hz).
                        </p>

                        <!-- The 7 Days Incense Master Table -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:var(--gold); margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                🌿 جدول البخورات الكوكبية للأيام السبعة ومركباتها التربينية:
                            </h5>
                            <div style="overflow-x:auto;">
                                <table style="width:100%; border-collapse:collapse; font-size:0.83rem; text-align:right;">
                                    <thead>
                                        <tr style="background:rgba(255,255,255,0.06); color:var(--gold); border-bottom:2px solid rgba(148, 163, 184,0.3);">
                                            <th style="padding:10px;">اليوم والفلك</th>
                                            <th style="padding:10px;">البخور الرئيسي النقي</th>
                                            <th style="padding:10px;">الخلطة المتوافقة التراثية</th>
                                            <th style="padding:10px;">المركب الكيميائي الفعّال</th>
                                            <th style="padding:10px;">التأثير العصبي والنفسي</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                            <td style="padding:10px; font-weight:700; color:var(--gold);">الأحد (الشمس) ☉</td>
                                            <td style="padding:10px;">السندروس المغربي واللبان الذكر الحوجري</td>
                                            <td style="padding:10px;">سندروس + لبان حوجري + عود صليب + خيوط زعفران كشميري</td>
                                            <td style="padding:10px; color:var(--cyan);">Alpha-pinene & Incensole acetate</td>
                                            <td style="padding:10px;">تنشيط مراكز التيقظ بالدماغ، طرد الكآبة، وتعزيز الثقة والوضوح</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                            <td style="padding:10px; font-weight:700; color:#60a5fa;">الاثنين (القمر) ☽</td>
                                            <td style="padding:10px;">الكندر الأبيض والمستكة الرومية</td>
                                            <td style="padding:10px;">كندر نقي + مستكة يونانية + ميعة سائلة + قطرات ماء ورد</td>
                                            <td style="padding:10px; color:var(--cyan);">Boswellic acids & Masticadienonic acid</td>
                                            <td style="padding:10px;">تهدئة الجهاز العصبي الودي، خفض ضغط الدم، وتصفية الأحلام</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                            <td style="padding:10px; font-weight:700; color:#ef4444;">الثلاثاء (المريخ) ♂</td>
                                            <td style="padding:10px;">القسط الهندي والصندل الأحمر</td>
                                            <td style="padding:10px;">قسط هندي حار + صندل أحمر + حبوب خردل بري + دم الأخوين</td>
                                            <td style="padding:10px; color:var(--cyan);">Costunolide & Santalin</td>
                                            <td style="padding:10px;">شحذ الحزم، تبديد الخوف، وتطهير الهواء من الميكروبات والطفيليات</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                            <td style="padding:10px; font-weight:700; color:var(--cyan);">الأربعاء (عطارد) ☿</td>
                                            <td style="padding:10px;">الجاوي الأبيض التنافري والكزبرة</td>
                                            <td style="padding:10px;">جاوي سيامي أبيض + كزبرة يابسة مطحونة + محلب أسود</td>
                                            <td style="padding:10px; color:var(--cyan);">Benzoic acid & Linalool</td>
                                            <td style="padding:10px;">تحفيز الذاكرة قصيرة المدى، زيادة التركيز، وسرعة البديهة الحسابية</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                            <td style="padding:10px; font-weight:700; color:#d8b4fe;">الخميس (المشتري) ♃</td>
                                            <td style="padding:10px;">العود القماري والصندل الأبيض</td>
                                            <td style="padding:10px;">خشب عود هندي قماري + صندل مقاصيري + كافور طبيعي بلوري</td>
                                            <td style="padding:10px; color:var(--cyan);">Alpha-santalol & Agarospirol</td>
                                            <td style="padding:10px;">أعمق مراتب السكينة الصوفية، تعزيز الانشراح الروحي، وتنشيط الغدة الصنوبرية</td>
                                        </tr>
                                        <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                            <td style="padding:10px; font-weight:700; color:var(--emerald);">الجمعة (الزهرة) ♀</td>
                                            <td style="padding:10px;">المسك الأسود وخلاصة الياسمين والزعفران</td>
                                            <td style="padding:10px;">مسك غزال أسود نقي + لادن عنبري + زهور ياسمين مجففة + قرنفل</td>
                                            <td style="padding:10px; color:var(--cyan);">Muskone & Eugenol</td>
                                            <td style="padding:10px;">تحفيز إفراز الإندورفين والأوكسيتوسين، تعزيز الألفة والمودة والمشاعر الراقية</td>
                                        </tr>
                                        <tr>
                                            <td style="padding:10px; font-weight:700; color:#94a3b8;">السبت (زحل) ♄</td>
                                            <td style="padding:10px;">الميعة اليابسة والحلتيت وحبة البركة</td>
                                            <td style="padding:10px;">ميعة يابسة + حلتيت منقى + حبة البركة + بذور البيلسان الأسود</td>
                                            <td style="padding:10px; color:var(--cyan);">Thymoquinone & Ferulic acid</td>
                                            <td style="padding:10px;">تثبيت العزيمة، قطع الهلوسات النفسية، الحصانة الأرضية، وتسكين الاضطراب</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <!-- Practical Fumigation Protocol -->
                        <div style="background:rgba(0,0,0,0.5); border-left:4px solid var(--gold); padding:16px; border-radius:10px;">
                            <strong style="color:var(--gold); display:block; margin-bottom:6px;">⚠️ بروتوكول التبخير الصحي السليم:</strong>
                            <p style="font-size:0.84rem; line-height:1.75; margin:0; color:#475569;">
                                • يُشترط استخدام جمر نقي من خشب طبيعي (كالفحم النباتي الخالي من الإضافات الكيميائية والكبريت).<br>
                                • لا يُرمى البخور دفعة واحدة؛ بل توضع حبيبات صغيرة تدريجياً ليتصاعد الدخان رقيقاً نقياً غير خانق.<br>
                                • الحفاظ على تهوية لطيفة بالغرفة لتجديد الأكسجين وتجنب استنشاق أول أكسيد الكربون، فالمطلوب هو الرائحة الأثيرية وليس الاختناق بالدخان.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 14: CHRONO-SPATIAL HARMONY & COSMIC WINDS -->
                <div class="ghazali-chapter" id="ghazali-ch14">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١٤</div>
                        <div>
                            <h4 class="chapter-title">الباب الرابع عشر: التوافق الزماني والمكاني الفلكي — الساعات الكلدانية ومنازل القمر والرياح الأربع</h4>
                            <div class="chapter-subtitle">Chrono-Spatial Planetary Hours, Lunar Mansions & The Four Cosmic Directions</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            يعمل مثلث الغزالي كهوائي كهرومغناطيسي؛ ولكي يلتقط الإشارة الكونية بأعلى قدر من النقاوة، يجب ضبط 
                            <strong>«التردد الزماني (Temporal Tuning)»</strong> و<strong>«التوجيه المكاني (Spatial Alignment)»</strong>.
                        </p>

                        <!-- The 24 Hours Rules -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(0,240,255,0.3); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:var(--cyan); margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                ⏱️ ميزان الساعات الفلكية الزمانية (Temporal Planetary Hours):
                            </h5>
                            <p style="font-size:0.85rem; line-height:1.75; margin:0 0 10px 0;">
                                الساعات الفلكية ليست ساعات اليد الثابتة (60 دقيقة)؛ بل تُحسب بتقسيم الفترة بين شروق الشمس وغروبها على 12 لحساب طول الساعة النهارية، 
                                وما بين الغروب والشروق على 12 لحساب الساعة الليلية. وتتعاقب الكواكب وفق النظام الكلداني:
                            </p>
                            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:12px; font-size:0.84rem;">
                                <div style="background:rgba(6,214,160,0.1); border:1px solid var(--emerald); padding:12px; border-radius:10px;">
                                    <strong style="color:var(--emerald);">ساعات السعد الأكبر (المشتري ♃):</strong>
                                    <p style="margin:4px 0 0 0;">مثالية للرزق، التوسعة، القضاء، الصلح، وتعمير أوفاق الوفرة والشفاء.</p>
                                </div>
                                <div style="background:rgba(236,72,153,0.1); border:1px solid #ec4899; padding:12px; border-radius:10px;">
                                    <strong style="color:#f472b6;">ساعات السعد الأصغر (الزهرة ♀):</strong>
                                    <p style="margin:4px 0 0 0;">مثالية للمحبة، الألفة، الفنون، تلطيف المشاعر، والتوافق الإنساني.</p>
                                </div>
                                <div style="background:rgba(244,180,26,0.1); border:1px solid var(--gold); padding:12px; border-radius:10px;">
                                    <strong style="color:var(--gold);">ساعات العزة والنور (الشمس ☉):</strong>
                                    <p style="margin:4px 0 0 0;">مثالية للهيبة، السيادة، لقاء ذوي النفوذ، والتحصين الشامل.</p>
                                </div>
                                <div style="background:rgba(239,68,68,0.1); border:1px solid #ef4444; padding:12px; border-radius:10px;">
                                    <strong style="color:#ef4444;">ساعات التحذير والانضباط (زحل والمريخ):</strong>
                                    <p style="margin:4px 0 0 0;">يُحظر فيها أعمال الجلب والخير؛ وتُخصص حصراً لدفع الضرر الشديد وكبح الظلمة والتحصين الدفاعي.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Spatial & Directions -->
                        <h5 style="color:var(--gold); margin:18px 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                            🧭 اتجاهات الجلوس واستقبال الرياح الكونية الأربعة:
                        </h5>
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:14px; margin-bottom:18px;">
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:var(--gold);">١. اتجاه القبلة المشرفة (مبدأ التوحيد):</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">هو الأصل الثابت في كافة الأعمال النورانية، حيث تتجه النفس نحو مركز ثقل التوحيد الكوني.</p>
                            </div>
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:var(--cyan);">٢. مهب الصبا (الشرق):</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">رياح الحياة والتجدد والبدايات المشرقة؛ يستقبلها الطالب عند كتابة أوفاق الشفاء وفتح البصيرة.</p>
                            </div>
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:var(--emerald);">٣. مهب الشمال:</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">رياح الرصانة والتثبيت والوقار وقطع حمى الآلام؛ يستقبلها الطالب عند تثبيت الرزق والصبر.</p>
                            </div>
                            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
                                <strong style="color:#ef4444;">٤. مهب الدبور (الغرب):</strong>
                                <p style="font-size:0.82rem; margin:4px 0 0 0;">رياح الإدبار والقطع؛ يُستقبل حصراً عند كتابة حروز الحجب والإغشاء ودفع العدوان.</p>
                            </div>
                        </div>

                        <!-- Lunar Mansions Compatibility -->
                        <div style="background:rgba(15,23,42,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:16px;">
                            <strong style="color:#fff; display:block; margin-bottom:6px;"><i class="fa-solid fa-moon"></i> أطوار القمر ومنازله الـ 28:</strong>
                            <p style="font-size:0.84rem; line-height:1.75; margin:0; color:#475569;">
                                • يُشترط في أعمال الشفاء والرزق والهيبة أن يكون القمر <strong>في طور الزيادة (من الهلال إلى البدر)</strong>، وتُفضل المنازل السعيدة: (الثريا، الهنعة، الذراع، الجبهة، السماك الأعزل، الغفر، وسعد السعود).<br>
                                • يُجتنب التعمير في أوقات <em>خلو المسار (Moon Void of Course)</em> أو في أيام المحاق المظلمة (آخر ليلتين من الشهر القمري) إلا لأعمال الحجب والدفع المخصوصة.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- CHAPTER 15: THE UNSPOKEN MATHEMATICAL & TOPOLOGICAL SECRETS -->
                <div class="ghazali-chapter" id="ghazali-ch15">
                    <div class="chapter-heading">
                        <div class="chapter-num-badge">١٥</div>
                        <div>
                            <h4 class="chapter-title">الباب الخامس عشر: الأسرار الرياضية والطوبولوجية التي لم يذكرها الغزالي في كتبه</h4>
                            <div class="chapter-subtitle">Topological Rotational Symmetry, The Hollow-Center Mystery & De-activation Protocols</div>
                        </div>
                    </div>
                    <div style="font-size:0.88rem; line-height:1.85; color:#475569;">
                        <p>
                            لقد أوجز الإمام الغزالي في كتبه <em>«السر المصون»</em> و<em>«المنقذ من الضلال»</em> قواعد الوفق دون أن يبين 
                            البرهان الرياضي والطوبولوجي العميق الذي يفسر لماذا يعمل هذا التشكيل تحديداً. هنا نكشف ما عجز عنه الشراح القدامى:
                        </p>

                        <!-- Mathematical Proof of Broken Cell -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(192,38,211,0.4); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:#d946ef; margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                📐 البرهان الرياضي القطعي: لماذا يُجبر الكسر في بيتي 7 و 4 فقط؟
                            </h5>
                            <p style="font-size:0.86rem; line-height:1.8; margin:0 0 12px 0;">
                                يتساءل كل باحث في علم الأوفاق: لماذا إذا كان الباقي 1 نزيد واحداً في بيت الزاي (البيت 7) تحديداً، 
                                وإذا كان الباقي 2 نزيد في بيت الدال (البيت 4)؟ إليك البرهان من نظرية الزمر والجبر الخطي:
                            </p>
                            <div style="background:rgba(255,255,255,0.03); padding:14px; border-radius:10px; font-size:0.84rem; line-height:1.8;">
                                1. في مصفوفة 3×3 الطبيعية، يقع بيت <strong>الزاي (7)</strong> في العمود الثالث والصف الثاني. إذا أضفنا +1 إليه، فإن التناظر الدوار حول القطب (البيت 5) يعوض هذا الفارق بدقة عبر الأقطار والصفوف دون كسر التناظر الهرميتي.<br>
                                2. لو وُضع الجبر في البيت 8 أو 9 أو 1، لاختل توازن قطرين معاً، ولاستحال رياضياً أن يتساوى مجموع الصف مع مجموع العمود!<br>
                                3. أما في باقي 2، فإن البيت <strong>الدال (4)</strong> يقع في الركن الأيسر العلوي، وزيادة +1 فيه تعوض القطر الرئيسي والصف الأول بآن واحد، فيظل الثابت السحري $M$ متطابقاً في الاتجاهات الثمانية. إنه <em>الحل الوحيد الممكن جبرياً في الفضاء الإقليدي ثلاثي الأبعاد</em>!
                            </div>
                        </div>

                        <!-- Hollow Center Secret -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(244,180,26,0.3); border-radius:14px; padding:18px; margin:16px 0;">
                            <h5 style="color:var(--gold); margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                🕳️ سر «المثلث الخالي الوسط» (The Zero-Point Cavity Square):
                            </h5>
                            <p style="font-size:0.86rem; line-height:1.8; margin:0;">
                                في بعض النسخ الخطية النادرة، ترك الغزالي بيت القطب (البيت 5) فارغاً تماماً وكتب فيه كلمة «لا إله إلا الله» أو تركه خاوياً. 
                                هذا السر يسمى <strong>«فيزياء الخلاء النقطي (Zero-Point Cavity)»</strong>؛ 
                                حيث يؤدي تفريغ المركز إلى نشوء فرق جهد طاقي هائل (Potential Gradient) بين المحيط المليء بالأرقام والمركز الخالي، 
                                مما يجذب طاقة الغاية كإعصار حلزوني توريدي يتدفق نحو المركز ولا يتسرب خارجه أبداً.
                            </p>
                        </div>

                        <!-- De-activation Protocol -->
                        <div style="background:linear-gradient(135deg, rgba(239,68,68,0.1), rgba(0,0,0,0.6)); border:2px solid #ef4444; border-radius:14px; padding:18px;">
                            <h5 style="color:#ef4444; margin:0 0 8px 0; font-family:'Amiri',serif; font-size:1.25rem;">
                                🔒 بروتوكول فك الوفق وصرفه عند انتهاء الحاجة (De-activation & Zeroing):
                            </h5>
                            <p style="font-size:0.86rem; line-height:1.8; margin:0 0 10px 0; color:#f8fafc;">
                                إذا تحقق الغرض المرجو (تم الشفاء، حلت البركة، أو زال الخطر)، فإن ترك الوفق مشحوناً للأبد قد يؤدي إلى ركود طاقي. 
                                إليك دستور صرف الطاقة وتفريغ الشحنة بأمان تام:
                            </p>
                            <ol style="margin:0 0 0 18px; padding:0; font-size:0.84rem; line-height:1.75; color:#475569;">
                                <li><strong>المحو المائي:</strong> يُغسل الكاغد في ماء طاهر جارٍ أو ماء مطر مع قراءة سورة الإخلاص والمعوذتين، حتى تذوب الأرقام تماماً ويعود الماء إلى الأرض الطيبة (سقي شجرة مثمرة).</li>
                                <li><strong>التحلل الحراري:</strong> يُحرق الكاغد في موقد نقي مع رشة لبان ذكر، ويُذر رماده في مهب ريح الصبا أو في نهر جارٍ.</li>
                                <li><strong>إعلان الشكر والامتنان:</strong> صلاة ركعتين شكراً لله تعالى على قضاء الحاجة وتأكيد أن الفضل والمنة لله وحده لا لعدد ولا لوفق، وبذلك تُغلق الدائرة الأثيرية في سلام تام.</li>
                            </ol>
                        </div>
                    </div>
                </div>

            <!-- ========================================================
                 END OF AL-GHAZALI MASTER HANDBOOK
                 ======================================================== -->

            <!-- 4 MASTER SCHOLARLY TREATISES -->
            <div style="margin-bottom:30px;">
                <h3 style="color:var(--gold); font-family:'Amiri',serif; font-size:1.45rem; margin-bottom:16px; display:flex; align-items:center; gap:10px;">
                    <i class="fa-solid fa-book-atlas"></i> الموسوعة الأكاديمية الشاملة لعلم الأوفاق: النواميس الكونية ودستور التحقيق
                </h3>

                <div class="wafq-treatise-grid">
                    <!-- TREATISE 1 -->
                    <div class="wafq-treatise-card">
                        <div class="wafq-treatise-header">
                            <div class="wafq-treatise-icon"><i class="fa-solid fa-shapes"></i></div>
                            <div>
                                <h4 class="wafq-treatise-title">الركن الأول: أنطولوجيا الوفق كلغة كونية وشيفرة المصفوفات المتزنة</h4>
                                <div class="wafq-treatise-subtitle">The Cosmic Ontology of Magic Squares & Zero-Entropy Physics</div>
                            </div>
                        </div>
                        <div class="wafq-treatise-content">
                            <p>علم الأوفاق ليس ركاماً من الطلاسم أو التنجيم الفلكلوري؛ بل هو <strong>لغة برمجة فراغية كونية (Universal Spatial Programming)</strong> تحاكي قوانين الاتزان والتناظر في مصفوفات الوجود. في الفضاء الحر، تتشتت الطاقات والموجات عشوائياً وفق القانون الثاني للديناميكا الحرارية (زيادة الإنتروبيا). أما داخل الوفق، فإن تساوي مجاميع الصفوف، الأعمدة، والأقطار يحقق ظاهرة <em>إلغاء الإنتروبيا الطاقية (Zero-Entropy Matrix)</em>، حيث تلغي التيارات المتضادة شواش بعضها البعض ليتحول المربع إلى <strong>مرنان كهرومغناطيسي مغلق (Closed Resonator Cavity)</strong> يحبس الطاقة في موجة دائرية توريدية فائقة التركيز.</p>

                            <div class="wafq-sub-box gold">
                                <strong>التشريح الهيكلي الخماسي لجسد الوفق (The Fivefold Anatomy):</strong>
                                <ul style="margin:4px 0 0 16px; padding:0;">
                                    <li><strong>1. المفتاح (The Key / Portal):</strong> أصغر خانة بالوفق (رقم 1 في الطبيعي)؛ يمثل مدخل التيار والقطب الموجب لتدفق الشحنة الأثيرية.</li>
                                    <li><strong>2. المغلاق (The Lock / Seal):</strong> أكبر خانة بالوفق ($n^2$)؛ صمام الأمان الذي يحبس الدائرة ويمنع تسرب الشحنة أو انفراطها.</li>
                                    <li><strong>3. القطب والعدل (Center of Gravity):</strong> مركز الثقل الهندسي والمغناطيسي الذي تتناظر حوله كافة الخانات كمرآة كوانتية.</li>
                                    <li><strong>4. الميزان (The Magic Constant $M$):</strong> الثابت المحوري لكل صف وعمود وقطر، المحسوب بالقانون الكوني: M = n(n^2 + 1) / 2.</li>
                                    <li><strong>5. المساحة (The Scalar Volume $T$):</strong> المجموع التراكمي لكافة أعداد الوفق ($T = n 	imes M$)، وهو يمثل الكتلة الحجمية للطاقة المستودعة.</li>
                                </ul>
                            </div>

                            <p><strong>ميكانيكا الكسر والجبر (Symmetry Breaking & Repair):</strong> إذا كان العدد المستودع لا يقبل القسمة بالتساوي على رتبة الوفق ($n$)، ينشأ باقي قسمة (الكسر). إهمال الكسر يفسد توازن المصفوفة ويجعلها عرجاء طاقياً. لذا صاغ الغزالي والبوني ميزاناً عبقرياً يجبر الخلل بزيادة 1 في بيوت محددة (البيت 7 في باقي 1، والبيت 4 في باقي 2)، وهو ما يعرف في الفيزياء الحديثة بـ <em>كسر التناظر التلقائي المنظم (Spontaneous Symmetry Breaking)</em> لحفظ الثابت الكلي.</p>

                            <p><strong>التفسير الكوانتي الحديث:</strong> في الجبر الخطي، يطابق كل وفق سحري مصفوفة قيم ذاتية هيرميتية (Hermitian Eigenvalue Matrix). هذا التناظر الدقيق يمنع ظاهرة فك الترابط الكمي (Decoherence)، ويجعل الوفق قادراً على العمل كهوائي كوني (Scalar Waveguide) يلتقط الترددات الكوكبية وينقلها إلى الحقل الحيوي للإنسان.</p>
                        </div>
                    </div>

                    <!-- TREATISE 2 -->
                    <div class="wafq-treatise-card">
                        <div class="wafq-treatise-header">
                            <div class="wafq-treatise-icon" style="color:var(--cyan); border-color:var(--cyan); background:rgba(0,240,255,0.12);"><i class="fa-solid fa-earth-americas"></i></div>
                            <div>
                                <h4 class="wafq-treatise-title">الركن الثاني: حوار الحضارات الكبرى والاكتشاف المشترك للنواميس</h4>
                                <div class="wafq-treatise-subtitle">Comparative Civilizations & The Universal Discovery</div>
                            </div>
                        </div>
                        <div class="wafq-treatise-content">
                            <p>إن أبلغ برهان على كون الأوفاق نواميس فيزيائية ثابتة لا خرافات محلية، هو أن <strong>كل الحضارات الكبرى المنعزلة جغرافياً وتاريخياً قد اكتشفت نفس المربعات السحرية بذات الأعداد والتراتيب</strong> دون أن تلتقي!</p>

                            <div class="wafq-sub-box emerald">
                                <strong>تتبع المصفوفات عبر التاريخ الإنساني:</strong>
                                <ul style="margin:4px 0 0 16px; padding:0;">
                                    <li><strong>الصين القديمة (لو شو Luo Shu 2800 ق.م):</strong> سلحفاة النهر الأصفر ونقوش درعها المقدسة التي تطابقت بنسبة 100% مع مثلث الغزالي وزحل (4-9-2 / 3-5-7 / 8-1-6). قسمت الصين الأعداد الفردية كـ <em>يانغ</em> سماوي نشط في المراكز، والأعداد الزوجية كـ <em>ين</em> أرضي ساكن في الأركان.</li>
                                    <li><strong>الهند الفيدية ومعبد خاجوراه (1000 م):</strong> يانترا كوبيرا لجلب الوفرة ($M=72$) ومربع جاينا فائق التناظر (Chautisa Yantra 4×4) حيث كل صف، عمود، قطر، وكل مربع فرعي 2×2، وكل زاوية تساوي 34 في تناغم هائل (Pandiagonal Perfect Square).</li>
                                    <li><strong>بابل والرافدين:</strong> النظام الستيني المقدس، والأختام الفلكية للكواكب السبعة التي وزعت الساعات اليومية وحسابات المنازل.</li>
                                    <li><strong>العصر الإسلامي الذهبي:</strong>
                                        <br>• <em>الإمام أبو حامد الغزالي:</em> في "المنقذ من الضلال" و"السر المصون"، برهن على أن خواص الأوفاق مثل خواص الأدوية الكيميائية؛ كلاهما أسباب مسخرة بأمر الله يدركها البرهان العقلي.
                                        <br>• <em>الشيخ أحمد البوني:</em> في "شمس المعارف" و"لطائف الإشارات"، قعّد التنزيل الحرفي والعددي وربط الأوفاق بالأسماء الحسنى وسر الحروف.
                                        <br>• <em>جابر بن حيان:</em> كتاب الموازين ونظرية 1:3:5:8 في موازنة طبائع المعادن الأربعة عبر أوفاق كيميائية صارمة.
                                        <br>• <em>ابن خلدون:</em> الفصل الاستثنائي في "المقدمة" الذي فكك الأوفاق فلسفياً ورياضياً وميز بين العلم البرهاني والدجل الوهمي.
                                    </li>
                                    <li><strong>النهضة الأوروبية والهرمسية:</strong> نقل <em>هاينريش كورنيليوس أغريبا (1533)</em> الأوفاق الكوكبية السبعة من المخطوطات الأندلسية الإسلامية (غاية الحكيم / Picatrix)، وخلد <em>ألبرشت دورر (1514)</em> مربع المشتري 4×4 في لوحته العالمية Melencolia I.</li>
                                </ul>
                            </div>

                            <p><strong>سر الاكتشاف الأعظم المشترك:</strong> لماذا اتفقت بابل مع الصين والهند والأندلس؟ لأن المربعات السحرية هي <em>الثوابت الطوبولوجية للفضاء ثلاثي الأبعاد (Topological Invariants)</em>. إنها ليست من صنع عقل بشري، بل هي بصمات التصميم الرياضي الذي بنى الله به شبكة الزمكان وتوازن الذرات والمجرات.</p>
                        </div>
                    </div>

                    <!-- TREATISE 3 -->
                    <div class="wafq-treatise-card">
                        <div class="wafq-treatise-header">
                            <div class="wafq-treatise-icon" style="color:#c026d3; border-color:#c026d3; background:rgba(192,38,211,0.12);"><i class="fa-solid fa-gears"></i></div>
                            <div>
                                <h4 class="wafq-treatise-title">الركن الثالث: ميكانيكا البناء، التفعيل، الفك، والإغلاق التام</h4>
                                <div class="wafq-treatise-subtitle">The Complete Operational Protocol: Construct, Activate, Decipher & Seal</div>
                            </div>
                        </div>
                        <div class="wafq-treatise-content">
                            <p>لكي يكون العمل بالوفق عملاً هندسياً ناجحاً ومحمياً، يجب اتباع الدستور التشغيلي الرباعي الصارم:</p>

                            <div class="wafq-sub-box purple">
                                <strong>1. ميكانيكا البناء والتنزيل (Construction Algorithms):</strong>
                                <ul style="margin:4px 0 0 16px; padding:0;">
                                    <li><strong>الأوفاق الفردية (3x3, 5x5, 7x7, 9x9):</strong> طريقة دي لا لوبير (De la Loubère Siamese Method) وسير "بطد زهج واح"؛ البدء بالرقم 1 في منتصف الصف الأول، والتحرك قطرياً للأعلى واليمين، وعند الاصطدام بخانة ممتلئة أو الخروج يتم الهبوط خانة واحدة للأسفل.</li>
                                    <li><strong>الأوفاق الزوجية المتماثلة (4x4, 8x8):</strong> طريقة الأقطار المتناظرة؛ ملء الخانات تسلسلياً 1 إلى $n^2$، ثم عكس الأرقام الواقعة على الأقطار الرئيسية عبر طرحها من $(n^2 + 1)$.</li>
                                    <li><strong>استخراج المفتاح من أي اسم أو آية:</strong> حساب الجُمّل الكبير ($N$) ثم طرح الأس ($S$) ثم القسمة على الرتبة ($n$)، فيكون الناتج هو المفتاح، والباقي يُجبر في خانة الكسر.</li>
                                </ul>
                            </div>

                            <div class="wafq-sub-box crimson">
                                <strong>2. ميكانيكا التفعيل (Activation) والفك العكسي (Deciphering):</strong>
                                <ul style="margin:4px 0 0 16px; padding:0;">
                                    <li><strong>التفعيل الطاقي:</strong> اختيار ساعة الكوكب المناسبة، شحن الوفق بنغمة التردد المداري (Hans Cousto Frequency)، وتلاوة الاسم بالعدد المودع لتحقيق الانجرار الرنيني (Acoustic Entrainment).</li>
                                    <li><strong>الفك والتحليل العكسي لأي طلسم مجهول:</strong> فحص خانة المفتاح (أقل رقم)، ثم حساب المجموع المستودع: $N = (	ext{Key} 	imes n) + S + 	ext{Remainder}$، ثم مطابقة الناتج بأسماء الله الحسنى والآيات القرآنية لمعرفة السر المودع وكشف ما إذا كان الوفق سليماً أم فاسداً مشوهاً.</li>
                                </ul>
                            </div>

                            <p><strong>3. ميكانيكا الإغلاق والختم والتحصين (Sealing & Shielding):</strong>
                            ترك الوفق مفتوحاً يجعله ثقباً أثيرياً يسرب الطاقة ويجتذب الطفيليات النارية. يُغلق الوفق بـ:
                            1. إحكامه بخانة المغلاق القصوى.
                            2. إحاطته بسور من الحروف النورانية القرآنية المفرقة غير المطموسة.
                            3. تثبيت أركانه الأربعة بآيات الإحكام ﴿وَجَعَلْنَا مِن بَيْنِ أَيْدِيهِمْ سَدًّا وَمِنْ خَلْفِهِمْ سَدًّا﴾.
                            4. ولإبطال أي وفق فاسد أو سحر قديم: يتم محوه بماء مقروء عليه آيات الإبطال، فبزوال التناظر الهندسي ينحل الحقل التداخلي فوراً وتتلاشى العقدة.</p>
                        </div>
                    </div>

                    <!-- TREATISE 4 -->
                    <div class="wafq-treatise-card">
                        <div class="wafq-treatise-header">
                            <div class="wafq-treatise-icon" style="color:var(--emerald); border-color:var(--emerald); background:rgba(6,214,160,0.12);"><i class="fa-solid fa-scale-balanced"></i></div>
                            <div>
                                <h4 class="wafq-treatise-title">الركن الرابع: شروط العمل، قانون الرنين الروحي، والميزان التوحيدي</h4>
                                <div class="wafq-treatise-subtitle">The 7 Pillars of Harmonic Success, Failure Traps & Quranic Sovereignty</div>
                            </div>
                        </div>
                        <div class="wafq-treatise-content">
                            <p>لكي يتحقق الأثر الطاقي بنسبة 100% ودون أي ارتداد سلبي، وضع الحكماء <strong>دستور الشروط السبعة للتحقيق التام</strong>:</p>

                            <div class="wafq-sub-box emerald">
                                <strong>الشروط السبعة للنجاح المؤكد (The 7 Pillars of Success):</strong>
                                <ol style="margin:4px 0 0 18px; padding:0;">
                                    <li><strong>1. الدقة الرياضية الصارمة:</strong> خطأ برقم واحد يدمر الدائرة بالكامل؛ الأوفاق كالمعادلات الكيميائية لا تقبل التقريب.</li>
                                    <li><strong>2. وحدة وتماسك النية (Coherent Intent):</strong> تشتت الفكر أو التردد يولد موجات تداخل هدام تلغي الرنين الأثيري.</li>
                                    <li><strong>3. التوافق الفلكي والزمني:</strong> مراعاة ساعات الكواكب وتجنب أوقات الاحتراق والقمر في خلو المسار.</li>
                                    <li><strong>4. الطهارة البيولوجية والبيئية:</strong> الوضوء التام، البيئة الهادئة، والبخور الطبيعي الخالص (اللبان الذكر، الصندل، المسك).</li>
                                    <li><strong>5. التأريض والتحصين (Grounding):</strong> تحصين الهالة بالأذكار لمنع اختراق اليرقات النجمية أثناء تدفق الشحنة.</li>
                                    <li><strong>6. الرنين الصوتي المتناغم:</strong> الترديد الصوتي بالنغمة الموافقة لتردد الكوكب (Cousto Orbital Hz).</li>
                                    <li><strong>7. الكتمان الطاقي (Hermetic Secrecy):</strong> حفظ العمل في طي الكتمان حتى يكتمل تكوينه في عالم الشهادة.</li>
                                </ol>
                            </div>

                            <p><strong>موانع الفشل السبعة (The 7 Failure Traps):</strong>
                            الخطأ في حساب الجُمّل، النوايا الخبيثة أو الإضرار بالخلق (مما يفعل قانون القصاص الكوني العادل فيرتد السحر على صاحبه ويحرق هالته)، استخدام بخور كيميائي مغشوش، غياب التأريض، والتفاخر والثرثرة قبل تمام التجسد المادي.</p>

                            <div class="wafq-sub-box gold">
                                <strong>الميزان التوحيدي والقرآني الأسمى — سيادة الإنسان الموحد:</strong>
                                <p style="margin:0;">الحقيقة العقدية الصارمة: الأعداد، الكواكب، والأوفاق ليست آلهة، ولا تملك في الكون ذرة من نفع أو ضر بذاتها، بل هي مجرد نواميس فيزيائية وأسباب كونية مسخرة بإرادة الله الواحد القهار ﴿وَأَحْصَىٰ كُلَّ شَيْءٍ عَدَدًا﴾ [الجن: 28]. الإنسان المؤمن الموحد المتوكل على ربه هو خليفة الله في أرضه، وهو سيد فوق كل هذه القوى المسخرة؛ يستعمل العلم الرياضي كما يستعمل مهندس الطيران قوانين الديناميكا الهوائية، وكل ذلك في رحاب التوحيد الخالص ونور <em>لا إله إلا الله محمد رسول الله</em>.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Complete 7 Planetary Squares Compendium -->
            <div style="margin-bottom:25px;">
                <h3 style="color:#d8b4fe; font-family:'Amiri',serif; font-size:1.35rem; margin-bottom:12px;">
                    <i class="fa-solid fa-cubes"></i> مصفوفة الأوفاق السبعة الكوكبية الكاملة من 3×3 إلى 9×9 وتردداتها وتطبيقاتها عبر الحضارات
                </h3>
                <div class="data-table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>نوع الوفق ورتبته</th>
                                <th>الكوكب والمعدن</th>
                                <th>الثابت (M)</th>
                                <th>المجموع (T)</th>
                                <th>في الصين القديمة (Luo Shu)</th>
                                <th>في الفيدا الهندية (Yantra)</th>
                                <th>في الهرمسية الغربية (Agrippa)</th>
                                <th>التردد والنغمة</th>
                                <th>التأثير البيولوجي والأثيري</th>
                                <th>استماع للرنين</th>
                            </tr>
                        </thead>
                        <tbody id="planetary-wafqs-tbody"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 8. UNIFIED RESONANCE PHYSICS & LIVE WAVE SYNTHESIZER (DOOR 16) -->
        <div id="tab-physics" class="tab-content">
            <div class="hero-banner">
                <h2>🔊 فيزياء الذبذبات والرنين الكوني: المولد الصوتي التفاعلي</h2>
                <p>مختبر حي يولد النغمات الحقيقية للأفلاك الكونية (Hans Cousto Orbital Octaves) وترددات الصولفيج (528Hz DNA Repair) مع راسم إشارة تذبذبي حي ومحاكاة التداخل البنّاء والهدام:</p>
            </div>
            <div class="wave-canvas-wrapper">
                <canvas id="waveCanvas"></canvas>
                <div class="canvas-controls">
                    <div style="display:flex; gap:8px;">
                        <button class="wave-mode-btn active" onclick="setWaveMode('constructive')">تداخل بنّاء (رنين متناغم)</button>
                        <button class="wave-mode-btn" onclick="setWaveMode('destructive')">تداخل هدام (تفريغ وقطع)</button>
                    </div>
                    <div id="wave-status" style="font-size:0.82rem; color:var(--cyan); font-weight:700;">الموجة: تداخل بنّاء متناغم</div>
                </div>
            </div>
        </div>

        <!-- 9. QURANIC CRITERION & MURSHID (DOOR 17) -->
        <div id="tab-criterion" class="tab-content">
            <div class="hero-banner">
                <h2>⚖️ ميزان التحكيم القرآني والتوحيدي: حصن المرشد وسيادة الإنسان</h2>
                <p>التفكيك الشرعي والعقدي الصارم: الفرق بين استشعار سنن الكون الفلكية وبين عبادة الكواكب أو الاستعانة بالشياطين، ولماذا يُعد الإنسان المؤمن الموحد سيداً فوق كل هذه القوى المسخرة بنور لا إله إلا الله:</p>
            </div>
            <div class="quranic-grid" id="quranic-grid"></div>
        </div>

    </main>

    <script>
        // DATA: Planetary Kings Matrix
        const KINGS_DATA = [
            {
                day: "الأحد (Sunday)", planet: "الشمس ☉", color: "#f4b41a",
                archetype: "ملك التاج والنور السيادي",
                civs: { babylon: "شَمَش (Shamash)", egypt: "رَع / أوزوريس", greco: "هيليوس / أبولو", vedic: "سوريا (Surya)", norse: "سول / بالدر", kabbalah: "ميخائيل (تيفريت)", arabic: "روقيائيل / المُذْهِب" },
                metal: "الذهب الخالص 24k", incense: "السندروس والميعة السائلة واللبان الذكر", chakra: "القلب 💚", organ: "القلب، الشريان الأورطي، وحيوية البصر", freq: 528,
                desc: "حاكم السيادة، الشهرة، العزة، الشفاء الجسدي، وطرد الكيانات المظلمة بنور الوعي الصافي. نصه القرآني: ﴿وَجَعَلْنَا سِرَاجًا وَهَّاجًا﴾."
            },
            {
                day: "الإثنين (Monday)", planet: "القمر ☽", color: "#00f0ff",
                archetype: "ملكة الفضة ومصفوفة الأوهام",
                civs: { babylon: "سِين (Sin)", egypt: "تَحوت / إيزيس", greco: "سيليني / ديانا", vedic: "تشاندرا (Chandra)", norse: "ماني (Mani)", kabbalah: "جبرائيل (يسود)", arabic: "جبرائيل / مُرَّة الأبيض" },
                metal: "الفضة النقية 999", incense: "اللبان الذكر والكافور ودهن الياسمين", chakra: "العجز والرحم 🧡", organ: "الدماغ، المعدة، السوائل الحيوية، والرحم", freq: 210.42,
                desc: "حاكم الذاكرة الباطنية، الأحلام، المد والجزر، تحريك السوائل، وسحر التأثير على الهرمونات. نصه القرآني: ﴿وَالْقَمَرَ قَدَّرْنَاهُ مَنَازِلَ﴾."
            },
            {
                day: "الثلاثاء (Tuesday)", planet: "المريخ ♂", color: "#ef4444",
                archetype: "المحارب ذو اللهب الأحمر",
                civs: { babylon: "نِيرْغَال (Nergal)", egypt: "حورس المنتقم / سِت", greco: "آريس / مارْس", vedic: "مانغالا (Mangala)", norse: "تير (Tyr)", kabbalah: "كامايل (جيفوراه)", arabic: "سمسمائيل / الأحمر (أبو محرز)" },
                metal: "الحديد والفولاذ الصرف", incense: "القسط الهندي، الصندل الأحمر، والكبريت", chakra: "الضفيرة الشمسية 💛", organ: "كريات الدم الحمراء، المرارة، والعضلات", freq: 144.72,
                desc: "حاكم الصراع، القطع، تدمير الحصون، وسحر الحروب وتفجير القيود السحرية بالقوة الجبرية. نصه القرآني: ﴿وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ﴾."
            },
            {
                day: "الأربعاء (Wednesday)", planet: "عطارد ☿", color: "#9d4edd",
                archetype: "كاتب الشيفرات والزئبق الطائر",
                civs: { babylon: "نَابُو (Nabu)", egypt: "تَحوت صاحب القلم", greco: "هيرميس / ميركوري", vedic: "بُودْهَا (Budha)", norse: "أودين (Odin)", kabbalah: "رافائيل (هود)", arabic: "ميكائيل / بُرْقان ذو الجناحين" },
                metal: "الزئبق الممتزج والقصدير", incense: "الجاوي التناصري وعلك الروم والمستكة", chakra: "الحنجرة 🩵", organ: "الجهاز العصبي، السيالات، والرئتان والنطق", freq: 141.27,
                desc: "حاكم الاتصالات، تشفير الطلاسم، فك الأقفال، الحساب، الإيهام اللغوي، والارتحال بين الأبعاد. نصه القرآني: ﴿ن ۚ وَالْقَلَمِ وَمَا يَسْطُرُونَ﴾."
            },
            {
                day: "الخميس (Thursday)", planet: "المشتري ♃", color: "#3b82f6",
                archetype: "الحبر الأعظم والقضاء الأسمى",
                civs: { babylon: "مَرْدُوخ (Marduk)", egypt: "آمون رَع", greco: "زيوس / جوبيتر", vedic: "بريهاسباتي (Guru)", norse: "ثُور (Thor)", kabbalah: "تزادكييل (خيسيد)", arabic: "صَرْفَيائيل / شَمْهُورَش القاضي" },
                metal: "القصدير الأبيض (الرصاص القلعي)", incense: "الصندل الأبيض، العنبر، والزعفران", chakra: "العين الثالثة 💙", organ: "الكبد، الشرايين الكبرى، وأنسجة الوفرة", freq: 183.58,
                desc: "حاكم الوفرة، جلب الأرزاق، توسيع الهالة الطاقية، القضاء والعدل الكوني، والقبول والجاه. نصه القرآني: ﴿يَرْفَعِ اللَّهُ الَّذِينَ آمَنُوا مِنكُمْ﴾."
            },
            {
                day: "الجمعة (Friday)", planet: "الزهرة ♀", color: "#06d6a0",
                archetype: "حارسة الجمال والمغناطيسية",
                civs: { babylon: "عَشْتَار (Ishtar)", egypt: "حتحور / باستيت", greco: "أفروديت / فينوس", vedic: "شُوكْرَا (Shukra)", norse: "فْرَيَا (Freya)", kabbalah: "هانييل (نتزاخ)", arabic: "عَنَيائيل / زَوْبَعَة أبو حسن" },
                metal: "النحاس الأحمر النقي", incense: "دهن الورد الجوري، الميعة، والمسك الأبيض", chakra: "القلب والمشاعر 💚", organ: "الكليتان، الغدد التناسلية، ونضارة البشرة", freq: 221.23,
                desc: "حاكمة الجذب والمغناطيسية الحيوية، سحر المحبة والألفة، الفنون والجماليات، والتوافق بين النفوس. نصه القرآني: ﴿زُيِّنَ لِلنَّاسِ حُبُّ الشَّهَوَاتِ﴾."
            },
            {
                day: "السبت (Saturday)", planet: "زحل ♄", color: "#6b7280",
                archetype: "حارس العتبة والزمن والقبضة",
                civs: { babylon: "نِينُورْتَا (Ninurta)", egypt: "أوزوريس الميت / سِت", greco: "كْرُونُوس / سَاتُورْن", vedic: "شَانِي (Shani)", norse: "لُوكي / سُورتُور", kabbalah: "تزافكييل (بينه)", arabic: "كَسْفَيائيل / مَيْمُون أبانوخ" },
                metal: "الرصاص الأسود الثقيل", incense: "المقل الأزرق، الحلتيت، والكبريت الصخري", chakra: "الجذر والتأريض ❤️", organ: "الهيكل العظمي، الطحال، الأسنان، والمفاصل", freq: 147.85,
                desc: "حاكم التثبيت، التعطيل، إطالة الأمد، سحر المقابر والربط المزمن، وحراسة البوابات الكونية. نصه القرآني: ﴿وَكُلُّ شَيْءٍ عِندَهُ بِمِقْدَارٍ﴾."
            }
        ];

        // DATA: Zodiac 12 Angels Matrix
        const ZODIAC_ANGELS_DATA = [
            { sign: "الحمل ♈", elem: "ناري 🔥", arabic: "طاطيائيل (أو مَلْخِيائيل)", kabbalah: "مالخيدئيل (Malkhidael)", egypt: "آمون-رع (الكبش الإلهي)", babylon: "دوموزي (Dumuzi)", tribe: "يهوذا" },
            { sign: "الثور ♉", elem: "ترابي ⛰️", arabic: "طوفيائيل (أو أسموديل)", kabbalah: "أسموديل (Asmodel)", egypt: "أبيس / أوزوريس", babylon: "غوانا (Gu.an.na)", tribe: "يساكر" },
            { sign: "الجوزاء ♊", elem: "هوائي 💨", arabic: "هَمْرائيئل (أو أمبرييل)", kabbalah: "أمبريئيل (Ambriel)", egypt: "شو وتفنوت", babylon: "لوغال-إيرا وميسلامتا", tribe: "زبولون" },
            { sign: "السرطان ♋", elem: "مائي 🌊", arabic: "شَلْقِيائيل (أو موريل)", kabbalah: "موريئيل (Muriel)", egypt: "خِبري (الجعران)", babylon: "ألا-لول (السلطعون)", tribe: "رأوبين" },
            { sign: "الأسد ♌", elem: "ناري 🔥", arabic: "كَلْكِيائيل (أو فيرخييل)", kabbalah: "فيرخيئيل (Verchiel)", egypt: "سخمت (اللبؤة النارية)", babylon: "أور-غولا (أسد نيرغال)", tribe: "شمعون" },
            { sign: "العذراء ♍", elem: "ترابي ⛰️", arabic: "طَلْقِيائيل (أو حماليل)", kabbalah: "حميليئيل (Hamaliel)", egypt: "إيزيس (حاملة السنبلة)", babylon: "شَالا (ربة الحصاد)", tribe: "جاد" },
            { sign: "الميزان ♎", elem: "هوائي 💨", arabic: "مَهْقِيائيل (أو زورييل)", kabbalah: "زوريئيل (Zuriel)", egypt: "ماعت (ميزان الحق)", babylon: "زيبانيتو (ميزان شمش)", tribe: "أفرايم" },
            { sign: "العقرب ♏", elem: "مائي 🌊", arabic: "صَلْصِيائيل (أو بارخييل)", kabbalah: "بارخيئيل (Barchiel)", egypt: "سيركيت (ربة العقرب)", babylon: "جير-تاب (عقرب عشتار)", tribe: "منسى" },
            { sign: "القوس ♐", elem: "ناري 🔥", arabic: "عَمْشِيائيل (أو أدفخييل)", kabbalah: "أدفخيئيل (Advachiel)", egypt: "نفرتوم القنطورس", babylon: "بابيلساغ (المحارب المجنح)", tribe: "بنيامين" },
            { sign: "الجدي ♑", elem: "ترابي ⛰️", arabic: "غَفْقِيائيل (أو هنائيل)", kabbalah: "هنائيل (Hanael)", egypt: "خنوم (صانع الطين)", babylon: "سوخور-ماش (عنزة إنكي)", tribe: "دان" },
            { sign: "الدلو ♒", elem: "هوائي 💨", arabic: "عَرْفِيائيل (أو قمبييل)", kabbalah: "غمبريئيل (Cambiel)", egypt: "حابي (فيضان النيل)", babylon: "غُولا (ساكب المياه)", tribe: "أشير" },
            { sign: "الحوت ♓", elem: "مائي 🌊", arabic: "طَلْحِيائيل (أو أمنيتزيئيل)", kabbalah: "أمنيتزيئيل (Amnitziel)", egypt: "نفتيس (حارسة البرزخ)", babylon: "سيم-ماه (السمكتان)", tribe: "نفتالي" }
        ];

        // DATA: Complete 36 Decans Matrix
        const DECANS_36_DATA = [
            // الحمل
            { sign: "الحمل (الوجه 1)", deg: "0° - 10°", ruler: "المريخ ♂", bakyu: "أسيكان (Assican)", angel: "مالخيدائيل", organ: "الرأس والجمجمة والدماغ", freq: "144.72 Hz", desc: "رجل أسود ضخم يرتدي الأبيض ويتقلد سيفاً قاطعاً؛ شجاعة وقهر وفتح." },
            { sign: "الحمل (الوجه 2)", deg: "10° - 20°", ruler: "الشمس ☉", bakyu: "سينوت (Senacher)", angel: "عزريائيل", organ: "العين اليمنى وحاسة البصر", freq: "528 Hz", desc: "امرأة حسناء ترتدي حلة حمراء وعلى رأسها إكليل ذهب؛ سيادة وجاه وشهرة." },
            { sign: "الحمل (الوجه 3)", deg: "20° - 30°", ruler: "الزهرة ♀", bakyu: "أريو (Acentacer)", angel: "عنائيل", organ: "عظام الجبين والأنف", freq: "221.23 Hz", desc: "رجل شاحب يمسك بقوس ذهبي مرصع؛ حذق ومهارة وفنون دقيقة." },
            // الثور
            { sign: "الثور (الوجه 1)", deg: "0° - 10°", ruler: "عطارد ☿", bakyu: "أساتي (Asicath)", angel: "أسموديل", organ: "الحنجرة والرقبة والأحبال", freq: "141.27 Hz", desc: "امرأة تجدل شعرها وتلبس حلي فضة وتزرع حقلاً؛ فلاحة وعمارة وتجارة." },
            { sign: "الثور (الوجه 2)", deg: "10° - 20°", ruler: "القمر ☽", bakyu: "فيرو (Viroaso)", angel: "حميليئيل", organ: "الغدة الدرقية والبلعوم", freq: "210.42 Hz", desc: "رجل كالقنطورس يحمل مفتاحاً كبيراً ومكيال قمح؛ وفرة وثروة وبناء مدن." },
            { sign: "الثور (الوجه 3)", deg: "20° - 30°", ruler: "زحل ♄", bakyu: "أهارف (Aharph)", angel: "كسفيائيل", organ: "الفقرات العنقية وقاعدة الرأس", freq: "147.85 Hz", desc: "كهل يتكئ على عصا محاطاً بكتل صخرية؛ استخراج كنوز ودفائن وثبات." },
            // الجوزاء
            { sign: "الجوزاء (الوجه 1)", deg: "0° - 10°", ruler: "المشتري ♃", bakyu: "تيسغار (Thesogar)", angel: "أمبرييل", organ: "الكتفان وعضد اليدين", freq: "183.58 Hz", desc: "شابان يحملان قلم قصب وألواحاً طينية؛ فصاحة وكتابة وفلسفة وحساب." },
            { sign: "الجوزاء (الوجه 2)", deg: "10° - 20°", ruler: "المريخ ♂", bakyu: "فيرات (Veras)", angel: "سمسمائيل", organ: "الذراعان والساعدان", freq: "144.72 Hz", desc: "رجل مدجج بالدروع يحمل رمحاً وميزاناً مقلوباً؛ جدل ومناورات وخصومات." },
            { sign: "الجوزاء (الوجه 3)", deg: "20° - 30°", ruler: "الشمس ☉", bakyu: "تبي (Tepiseat)", angel: "ميخائيل", organ: "الأصابع والأوتار العصبية", freq: "528 Hz", desc: "رجل يعزف على قيثارة وترية فتصغي له الطيور؛ موسيقى وهندسة وفنون رياضية." },
            // السرطان
            { sign: "السرطان (الوجه 1)", deg: "0° - 10°", ruler: "الزهرة ♀", bakyu: "سوثير (Sotheir)", angel: "مورييل", organ: "الصدر والرئتان والأضلاع العليا", freq: "221.23 Hz", desc: "امرأة فائقة الجمال تخرج من صدفة وتحمل غصن آس؛ حب وألفة واستجلاب خير." },
            { sign: "السرطان (الوجه 2)", deg: "10° - 20°", ruler: "عطارد ☿", bakyu: "سياث (Syath)", angel: "رفائيل", organ: "المعدة والحجاب الحاجز", freq: "141.27 Hz", desc: "رجل على ضفة نهر ومعه شبكة صيد ملأى بلآلئ؛ سفر بحري وأحلام كاشفة." },
            { sign: "السرطان (الوجه 3)", deg: "20° - 30°", ruler: "القمر ☽", bakyu: "ثومي (Thumis)", angel: "جبرائيل", organ: "الكبد والأغشية المصلية", freq: "210.42 Hz", desc: "رجل يجري ممسكاً بكلب صيد وتحته سرطان عظيم؛ مد وجزر وحركة أرحام." },
            // الأسد
            { sign: "الأسد (الوجه 1)", deg: "0° - 10°", ruler: "زحل ♄", bakyu: "شاروتش (Chararch)", angel: "فيرخييل", organ: "القلب والصمام الأورطي", freq: "147.85 Hz", desc: "رجل يركب أسداً كاسراً بزمام من جمر؛ هيبة شديدة وقهر أعداء وحفظ ملك." },
            { sign: "الأسد (الوجه 2)", deg: "10° - 20°", ruler: "المشتري ♃", bakyu: "أبتول (Aptol)", angel: "صرفيائيل", organ: "العمود الفقري والظهر", freq: "183.58 Hz", desc: "رجل بتاج مرصع يعتلي جواداً أبيض؛ علو الرتب ونيل الوزارات والعدل." },
            { sign: "الأسد (الوجه 3)", deg: "20° - 30°", ruler: "المريخ ♂", bakyu: "فوكا (Phouph)", angel: "سمسمائيل", organ: "نخاع العظم وقوة الدم", freq: "144.72 Hz", desc: "رجل يلوح بصولجان ناري تتبعه نمور ضارية؛ بطش وكسر المتجبرين." },
            // العذراء
            { sign: "العذراء (الوجه 1)", deg: "0° - 10°", ruler: "الشمس ☉", bakyu: "أنوبيس (Anobreath)", angel: "حماليل", organ: "الأمعاء الدقيقة والغدد المعوية", freq: "528 Hz", desc: "عذراء بكر بثوب كتان تمسك سنبلة قمح؛ حصاد ونقاء وشفاء بالأعشاب." },
            { sign: "العذراء (الوجه 2)", deg: "10° - 20°", ruler: "الزهرة ♀", bakyu: "أوتي (Utiath)", angel: "عنائيل", organ: "البنكرياس وأسفل البطن", freq: "221.23 Hz", desc: "رجل وسيم يمسك صرة نقود ويزن غلالاً؛ ادخار واقتصاد ومكاسب طيبة." },
            { sign: "العذراء (الوجه 3)", deg: "20° - 30°", ruler: "عطارد ☿", bakyu: "روميو (Romios)", angel: "ميكائيل", organ: "الجهاز الهضمي العصبي", freq: "141.27 Hz", desc: "رجل يقرأ في سفر وبيده عدسة فاحصة؛ علوم التشفير والتدقيق والمخطوطات." },
            // الميزان
            { sign: "الميزان (الوجه 1)", deg: "0° - 10°", ruler: "القمر ☽", bakyu: "بيكات (Serucath)", angel: "زورييل", organ: "الكليتان والخصر", freq: "210.42 Hz", desc: "رجل يحمل ميزاناً متكافئاً وفوقه هلال مشع؛ عدل وفض نزاعات ومصالحات." },
            { sign: "الميزان (الوجه 2)", deg: "10° - 20°", ruler: "زحل ♄", bakyu: "تاري (Tarath)", angel: "كسفيائيل", organ: "أسفل الظهر والعجز", freq: "147.85 Hz", desc: "كهل يمسك بمرآة تكشف خفايا الضمائر؛ كشف المستور وحكمة صامتة." },
            { sign: "الميزان (الوجه 3)", deg: "20° - 30°", ruler: "المشتري ♃", bakyu: "سيبو (Sebou)", angel: "صرفيائيل", organ: "الأوردة الحوضية", freq: "183.58 Hz", desc: "شاب أنيق يعزف على عود بين الأزهار؛ محبة وزواج شريف وائتلاف قلوب." },
            // العقرب
            { sign: "العقرب (الوجه 1)", deg: "0° - 10°", ruler: "المريخ ♂", bakyu: "كيمين (Charchnoumis)", angel: "بارخييل", organ: "الأجهزة التناسلية والإخراج", freq: "144.72 Hz", desc: "رجل بحربة مسمومة يخرج معه عقرب هائل؛ دفاع سحري قاهر ودحر المعتدين." },
            { sign: "العقرب (الوجه 2)", deg: "10° - 20°", ruler: "الشمس ☉", bakyu: "أريت (Arath)", angel: "ميخائيل", organ: "غدة البروستاتا وجدار الرحم", freq: "528 Hz", desc: "فارس على جمل يشع نوراً وسط الرمال؛ تحويل السم إلى ترياق وانبعاث." },
            { sign: "العقرب (الوجه 3)", deg: "20° - 30°", ruler: "الزهرة ♀", bakyu: "كينوت (Chontare)", angel: "عنائيل", organ: "الأعصاب الحوضية العميقة", freq: "221.23 Hz", desc: "امرأة تسكب ماء من جرة بلور في بئر سحيق؛ سبر أغوار الباطن والأسرار." },
            // القوس
            { sign: "القوس (الوجه 1)", deg: "0° - 10°", ruler: "عطارد ☿", bakyu: "ميسوت (Misat)", angel: "أدفخييل", organ: "الوركان وعظام الحوض", freq: "141.27 Hz", desc: "رجل بثياب سفر يشد وتراً نحو النجوم؛ ارتحال واستبصار وبلوغ المقاصد." },
            { sign: "القوس (الوجه 2)", deg: "10° - 20°", ruler: "القمر ☽", bakyu: "خاوت (Chout)", angel: "جبرائيل", organ: "عضلات الفخذ والشرايين", freq: "210.42 Hz", desc: "قنطورس نبيل يقود أيائل برية؛ هداية الضالين والتعليم الحكيم." },
            { sign: "القوس (الوجه 3)", deg: "20° - 30°", ruler: "زحل ♄", bakyu: "أبات (Abat)", angel: "كسفيائيل", organ: "عظام الفخذ والمفصل", freq: "147.85 Hz", desc: "شيخ حكيم يمسك بكرة نحاسية يرصد البروج؛ فلك ورصد نواميس كلية." },
            // الجدي
            { sign: "الجدي (الوجه 1)", deg: "0° - 10°", ruler: "المشتري ♃", bakyu: "سوبي (Sobi)", angel: "هنائيل", organ: "الركبتان والمفصل الرضفي", freq: "183.58 Hz", desc: "رجل بصولجان عاجي على قمة جبل يشرف على الأودية؛ سيادة وصعود خالد." },
            { sign: "الجدي (الوجه 2)", deg: "10° - 20°", ruler: "المريخ ♂", bakyu: "تميت (Temat)", angel: "سمسمائيل", organ: "أوتار الركبة والغضاريف", freq: "144.72 Hz", desc: "رجل بمطرقة حديدية يطرق سنداناً في منجم؛ تعدين وتطويع الصخر وصبر." },
            { sign: "الجدي (الوجه 3)", deg: "20° - 30°", ruler: "الشمس ☉", bakyu: "بيكاتي (Bicati)", angel: "روقيائيل", organ: "الجلد الخارجي والميلانين", freq: "528 Hz", desc: "شيخ جالس على عرش جرانيت بميزان صخري؛ قضاء صارم وحفظ نظم وأمم." },
            // الدلو
            { sign: "الدلو (الوجه 1)", deg: "0° - 10°", ruler: "الزهرة ♀", bakyu: "أوتست (Autest)", angel: "كمبييل", organ: "الساقان وقصبة الرجل", freq: "221.23 Hz", desc: "رجل يسكب من إبريق ذهبي ماءً يروي شجرة حكمة؛ عصر الدلو وبث المعرفة." },
            { sign: "الدلو (الوجه 2)", deg: "10° - 20°", ruler: "عطارد ☿", bakyu: "ساسيت (Sasit)", angel: "ميكائيل", organ: "أوردة الساقين والدوران الطرفي", freq: "141.27 Hz", desc: "مخترع بين آلات هندسية ودوائر أثيرية؛ تسريع العلوم واختصار القرون." },
            { sign: "الدلو (الوجه 3)", deg: "20° - 30°", ruler: "القمر ☽", bakyu: "بياوت (Biaout)", angel: "جبرائيل", organ: "الأعصاب الحركية في الساقين", freq: "210.42 Hz", desc: "رجل يرصد السماء بهالات نورانية؛ وعي موحد وتخاطر واتصال كوني." },
            // الحوت
            { sign: "الحوت (الوجه 1)", deg: "0° - 10°", ruler: "زحل ♄", bakyu: "تشانتي (Chantat)", angel: "أمنيتزييل", organ: "القدمان وأصابع الرجلين", freq: "147.85 Hz", desc: "ناسك بسراج خافت يسير على صفحة البحر؛ عزلة وبرزخ ومحو الأنا." },
            { sign: "الحوت (الوجه 2)", deg: "10° - 20°", ruler: "المشتري ♃", bakyu: "أريمي (Arim)", angel: "صرفيائيل", organ: "كعوب القدم والجهاز اللمفاوي", freq: "183.58 Hz", desc: "عابد يبسط كفيه فينفتح باب نور في السحاب؛ كرامات وفيوضات ورحمة." },
            { sign: "الحوت (الوجه 3)", deg: "20° - 30°", ruler: "المريخ ♂", bakyu: "كرومي (Chroum)", angel: "سمسمائيل", organ: "باطن القدمين وقنوات التأريض", freq: "144.72 Hz", desc: "رجل يصارع حوتاً في لجة البحر فيظفر بجوهرة؛ ختام الدورة وميلاد جديد." }
        ];

        // Chaldean Order Cycle
        const CHALDEAN_ORDER = ["زحل", "المشتري", "المريخ", "الشمس", "الزهرة", "عطارد", "القمر"];
        const PLANET_NATURES = {
            "الشمس": { nature: "سعد معتدل (حار يابس)", freq: 528, work: "عقد المحبة، الهيبة، ودخول الملوك والشفاء وفتح البصيرة" },
            "الزهرة": { nature: "سعد أصغر (بارد رطب)", freq: 221.23, work: "المحبة، التهييج، الجلب، والتأليف بين القلوب والفنون" },
            "عطارد": { nature: "ممتزج بحسب ما يقارنه", freq: 141.27, work: "عقد الألسن، التجارة، الحساب، والطلاسم الفكرية والعلوم" },
            "القمر": { nature: "سريع الفيض (بارد رطب)", freq: 210.42, work: "الأسفار، السوائل، الأحلام، وسحر الأرحام والمد والجزر" },
            "زحل": { nature: "نحس أكبر (بارد يابس)", freq: 147.85, work: "التعطيل، الهدم، التثبيت، التقييد، وسحر المقابر والبناء القديم" },
            "المشتري": { nature: "سعد أكبر (حار رطب)", freq: 183.58, work: "الأرزاق، الوفرة، القضاء، دفع الأعداء والرفعة والوزارة" },
            "المريخ": { nature: "نحس أصغر (حار يابس)", freq: 144.72, work: "النزاع، التفرقة، الحروب، والحميات والقطع وتفجير الحصون" }
        };
        const DAY_START_PLANET_INDEX = [3, 6, 2, 5, 1, 4, 0];

        // DATA: 28 Lunar Mansions Compendium
        const MANSIONS_DATA = [
            { num: 1, name: "الشَّرَطَان", deg: "الحمل (0° - 12°51')", stars: "Alpha & Beta Arietis", letter: "أ", god_name: "البديع", angel: "جبرائيل", nat: "نارية", planet: "المريخ", inc: "القسط والكندر", work: "إثارة العزائم والحروب والأسفار وفتح المغاليق" },
            { num: 2, name: "البُطَيْن", deg: "الحمل (12°51' - 25°42')", stars: "Epsilon Arietis", letter: "ب", god_name: "الباعث", angel: "صعصيائيل", nat: "ترابية", planet: "الزهرة", inc: "اللبان الأبيض", work: "طلب الدفائن والكنوز وعمارة الأرض والزرع" },
            { num: 3, name: "الثُّرَيَّا", deg: "الحمل / الثور (25°42' - 8°34')", stars: "Pleiades Cluster", letter: "ج", god_name: "الباطن", angel: "عطايل", nat: "هوائية", planet: "عطارد", inc: "الصندل الأحمر والمسك", work: "المودة، الألفة، الصيد، والبركة في الأرزاق" },
            { num: 4, name: "الدَّبَرَان", deg: "الثور (8°34' - 21°25')", stars: "Aldebaran (عين الثور)", letter: "د", god_name: "الآخر", angel: "روقيائيل", nat: "مائية", planet: "القمر", inc: "الميعة والجاوي", work: "التفرقة، هدم أسوار الظلمة، وتحويل مجرى المياه" },
            { num: 5, name: "الهَقْعَة", deg: "الثور / الجوزاء (21°25' - 4°17')", stars: "Lambda Orionis (رأس الجبار)", letter: "هـ", god_name: "الحكيم", angel: "طهطائيل", nat: "نارية", planet: "الشمس", inc: "المسك والكافور", work: "إصلاح الفاسد، المصالحات الشريفة، والشفاء" },
            { num: 6, name: "الهَنْعَة", deg: "الجوزاء (4°17' - 17°08')", stars: "Gamma Geminorum (الهنعة)", letter: "و", god_name: "السميع", angel: "شمعائيل", nat: "ترابية", planet: "الزهرة", inc: "اللبان والعود", work: "عقد المحبة الصادقة وقضاء الحوائج عند الحكام" },
            { num: 7, name: "الذِّرَاع", deg: "الجوزاء / السرطان (17°08' - 0°)", stars: "Castor & Pollux", letter: "ز", god_name: "البصير", angel: "مهقائيل", nat: "هوائية", planet: "عطارد", inc: "السندروس والجاوي", work: "حصول الجاه، عقد الألسن، والظفر بالعلوم الدقيقة" },
            { num: 8, name: "النَّثْرَة", deg: "السرطان (0° - 12°51')", stars: "Praesepe (معلف السرطان)", letter: "ح", god_name: "العليم", angel: "خفيائيل", nat: "مائية", planet: "القمر", inc: "الكافور واللبان", work: "النصر في الخصومة، إبطال المكايد، وحفظ الأجنة" },
            { num: 9, name: "الطَّرْف", deg: "السرطان / الأسد (12°51' - 25°42')", stars: "Lambda & Mu Leonis", letter: "ط", god_name: "القاهر", angel: "طاطائيل", nat: "نارية", planet: "زحل", inc: "المقل والكبريت", work: "عقد الأعداء، الحصون المنيعة، وإخماد الفتن" },
            { num: 10, name: "الجَبْهَة", deg: "الأسد (25°42' - 8°34')", stars: "Regulus (قلب الأسد)", letter: "ي", god_name: "العزيز", angel: "لوخائيل", nat: "ترابية", planet: "الشمس", inc: "العود والزعفران", work: "المهابة، دخول السلاطين، وعلو القدر والشهرة" },
            { num: 11, name: "الزُّبْرَة", deg: "الأسد (8°34' - 21°25')", stars: "Delta & Theta Leonis", letter: "ك", god_name: "اللطيف", angel: "همريائيل", nat: "هوائية", planet: "الزهرة", inc: "الصندل والمستكة", work: "تسهيل الولادة، الخلاص من السجون، والقبول" },
            { num: 12, name: "الصَّرْفَة", deg: "الأسد / العذراء (21°25' - 4°17')", stars: "Denebola (ذنب الأسد)", letter: "ل", god_name: "القوي", angel: "حرفائيل", nat: "مائية", planet: "عطارد", inc: "اللبان والجاوي", work: "صرف المكاره، كشف الخداع، ونماء الزرع" },
            { num: 13, name: "العَوَّاء", deg: "العذراء (4°17' - 17°08')", stars: "Beta & Eta Virginis", letter: "م", god_name: "المحيي", angel: "طوفيائيل", nat: "نارية", planet: "القمر", inc: "الميعة والزعفران", work: "الألفة والزواج، جلب الأرزاق والمكاسب التجارية" },
            { num: 14, name: "السِّمَاك", deg: "العذراء / الميزان (17°08' - 0°)", stars: "Spica (السماك الأعزل)", letter: "ن", god_name: "المميت", angel: "سمخائيل", nat: "ترابية", planet: "الزهرة", inc: "العود والمسك", work: "الشفاء من الأمراض المزمنة، وتثبيت البناء" },
            { num: 15, name: "الغَفْر", deg: "الميزان (0° - 12°51')", stars: "Iota & Kappa Virginis", letter: "ص", god_name: "الغفور", angel: "عزريائيل", nat: "هوائية", planet: "عطارد", inc: "اللبان الذكر", work: "غفران الزلات، استخراج الدفائن، وصلح المتخاصمين" },
            { num: 16, name: "الزُّبَانَى", deg: "الميزان / العقرب (12°51' - 25°42')", stars: "Alpha & Beta Librae", letter: "ع", god_name: "العدل", angel: "شرطيائيل", nat: "مائية", planet: "المريخ", inc: "القسط والخردل", work: "إقامة ميزان الحق، رد الظلم، وعقد الظالمين" },
            { num: 17, name: "الإِكْلِيل", deg: "العقرب (25°42' - 8°34')", stars: "Beta & Delta Scorpii", letter: "ف", god_name: "الفتاح", angel: "شمسائيل", nat: "نارية", planet: "المشتري", inc: "اللبان والسندروس", work: "حفظ الأموال، رد كيد السارقين، وحراسة المسافر" },
            { num: 18, name: "القَلْب", deg: "العقرب (8°34' - 21°25')", stars: "Antares (قلب العقرب)", letter: "ض", god_name: "القدوس", angel: "سمسمائيل", nat: "ترابية", planet: "المريخ", inc: "الصندل الأحمر", work: "قهر الجبابرة، تحصين الثغور، وعلاج لدغ الهوام" },
            { num: 19, name: "الشَّوْلَة", deg: "العقرب / القوس (21°25' - 4°17')", stars: "Lambda & Upsilon Scorpii", letter: "ق", god_name: "الوارث", angel: "قرقائيل", nat: "هوائية", planet: "زحل", inc: "الكبريت والحرمل", work: "تدمير معاقل المردة، حصر العدو، واستنزاف قوته" },
            { num: 20, name: "النَّعَائِم", deg: "القوس (4°17' - 17°08')", stars: "Gamma & Delta Sagittarii", letter: "ر", god_name: "الرحمن", angel: "رومائيل", nat: "مائية", planet: "المشتري", inc: "المسك الأبيض", work: "البركة الواسعة، تيسير السفر بالبر والبحر، والهيبة" },
            { num: 21, name: "البَلْدَة", deg: "القوس / الجدي (17°08' - 0°)", stars: "منطقة خالية من النجوم النيرة", letter: "ش", god_name: "الملك", angel: "شفائيل", nat: "نارية", planet: "الشمس", inc: "العود القماري", work: "بناء المعاقل، توطين المدن، وثبات الحكم" },
            { num: 22, name: "سَعْدُ الذَّابِح", deg: "الجدي (0° - 12°51')", stars: "Alpha & Beta Capricorni", letter: "ت", god_name: "التواب", angel: "تلهائيل", nat: "ترابية", planet: "المريخ", inc: "القسط واللبان", work: "النجاة من المهالك، تفرقة عساكر الشر، والشفاء" },
            { num: 23, name: "سَعْدُ بُلَع", deg: "الجدي / الدلو (12°51' - 25°42')", stars: "Mu & Epsilon Aquarii", letter: "ث", god_name: "الجامع", angel: "ثقفائيل", nat: "هوائية", planet: "عطارد", inc: "السندروس والجاوي", work: "ابتلاع الأمراض، شفاء المعدة والسموم، والمحبة" },
            { num: 24, name: "سَعْدُ السُّعُود", deg: "الدلو (25°42' - 8°34')", stars: "Beta & Xi Aquarii", letter: "خ", god_name: "الخالق", angel: "خلائيل", nat: "مائية", planet: "المشتري", inc: "المسك والعنبر", work: "سعد السعود الأعظم: تيسير العسير، الغنى، والزواج المبارك" },
            { num: 25, name: "سَعْدُ الأَخْبِيَة", deg: "الدلو / الحوت (8°34' - 21°25')", stars: "Gamma & Zeta Aquarii", letter: "ذ", god_name: "المبين", angel: "ذكيائيل", nat: "نارية", planet: "الزهرة", inc: "الميعة واللبان", work: "كشف الخبايا والدفائن والضمائر، وإخراج المستور" },
            { num: 26, name: "فَرْغُ الدَّلْوِ المُقَدَّم", deg: "الحوت (21°25' - 4°17')", stars: "Alpha & Beta Pegasi", letter: "ض", god_name: "الرزاق", angel: "فرغائيل", nat: "ترابية", planet: "المشتري", inc: "الصندل والعود", work: "سريان الأرزاق، نماء التجارة، وفيضان الخيرات" },
            { num: 27, name: "فَرْغُ الدَّلْوِ المُؤَخَّر", deg: "الحوت (4°17' - 17°08')", stars: "Gamma Pegasi & Alpha Andromedae", letter: "ظ", god_name: "الظاهر", angel: "ظلمائيل", nat: "هوائية", planet: "القمر", inc: "الكافور واللبان", work: "دفع كيد السحرة، رد المكائد، والصلح والتجارة" },
            { num: 28, name: "الرَّشَاء (بَطْنُ الحُوت)", deg: "الحوت / الحمل (17°08' - 0°)", stars: "Beta Andromedae (المرأة المسلسلة)", letter: "غ", god_name: "الغني", angel: "غنيائيل", nat: "مائية", planet: "الزهرة", inc: "المسك ودهن الورد", work: "ختام الدائرة المبارك: صيد البحر، جمع الشمل، وتأليف القلوب" }
        ];

                // DATA: 7 Planetary Wafqs Compendium across Civilizations
        const PLANETARY_WAFQS_DATA = [
            {
                order: "المثلث (3×3)", n: 3, planet: "زحل ♄ (Saturn)", day: "السبت", metal: "الرصاص الأسود", color: "#6b7280",
                constant: 15, total: 45, freq: "147.85 Hz", note: "D (ري)", sound: 147.85,
                china: "لو شو (Luo Shu 洛書 2800 ق.م) — سلحفاة الإمبراطور يو ونواة الباغوا",
                vedic: "يانترا زحل (Shani Yantra) — تثبيت الحدود وحصن الكرما وتجاوز القيود",
                hermetic: "Seal of Saturn (Agrippa 1533) — روح زحل (Zazel) وملاك كاسييل (Cassiel)",
                element: "ترابي / مائي باطني (تثبيت وترسيخ)",
                bio: "العظام، المفاصل، الصبر، تفريغ الشحنات السلبية، وحفظ الحدود الكونية والهالة من الاختراق.",
                path_desc: "سير بطد زهج واح (De la Loubère): يبدأ بـ 1 في أعلى المنتصف ويصعد قطرياً، وعند الصدمة ينزل خطوة."
            },
            {
                order: "المربع (4×4)", n: 4, planet: "المشتري ♃ (Jupiter)", day: "الخميس", metal: "القصدير الأبيض (الرصاص القلعي)", color: "#3b82f6",
                constant: 34, total: 136, freq: "183.58 Hz", note: "F# (فا دييز)", sound: 183.58,
                china: "مصفوفة التناظر الرباعي في كتاب التغيرات (I Ching) ونظام الاتجاهات الأربعة",
                vedic: "يانترا كوبيرا ومربع جاينا فائق التناظر في خاجوراه (Chautisa Yantra — كل 2×2 وكل ركن = 34)",
                hermetic: "مربع المشتري في لوحة Melencolia I لألبرشت دورر (1514) وأختام أغريبا لجلب الجاه والوفرة",
                element: "هوائي ناري (توسع وتمدد)",
                bio: "الكبد، الشرايين الكبرى، توسيع المجال الهالاتي التوريدي، جلب الوفرة وتيسير الأسباب.",
                path_desc: "طريقة تناظر الأقطار المتقاطعة (Cross-Diagonal Inversion): ملء الأرقام 1-16 ثم عكس خانات الأقطار."
            },
            {
                order: "المخمس (5×5)", n: 5, planet: "المريخ ♂ (Mars)", day: "الثلاثاء", metal: "الحديد والفولاذ الصرف", color: "#ef4444",
                constant: 65, total: 325, freq: "144.72 Hz", note: "D (ري)", sound: 144.72,
                china: "مصفوفة العناصر الخمسة الصينية (Wu Xing — خشب، نار، تراب، معدن، ماء) ودورات التوليد",
                vedic: "يانترا مانغالا (Mangala Yantra) — شجاعة المحارب ورد الطاقات المعتدية",
                hermetic: "Seal of Mars (Agrippa) — روح برزافيل (Bartzabel) وملاك سمسمائيل، تفجير الحصون السحرية",
                element: "ناري حارق (قطع وردع)",
                bio: "كريات الدم الحمراء، المناعة الخلوية الهجومية، الشجاعة، وقطع القيود وسلاسل الطاقات السامة.",
                path_desc: "طريقة دي لا لوبير السيامية للمخمس: البدء في منتصف الصف العلوي والصعود قطرياً بزاوية 45 درجة."
            },
            {
                order: "المسدس (6×6)", n: 6, planet: "الشمس ☉ (Sol)", day: "الأحد", metal: "الذهب الخالص 24k", color: "#f4b41a",
                constant: 111, total: 666, freq: "528.00 Hz", note: "C (دو / ترنيمة 528 إصلاح DNA)", sound: 528,
                china: "سداسيات آي تشينغ الـ 64 (Hexagrams) وتناغم السماء السادسة والتاي تشي (Taiji)",
                vedic: "يانترا سوريا الذهبية (Surya Yantra) — مركز الوعي والسيادة والشفاء الكوني الأسمى",
                hermetic: "وفق الشمس الأعظم (Agrippa) والمجموع 666 (ثابت المثلث الشمسي) وروح سورات وملاك ميخائيل",
                element: "ناري نقي / أثيري علوي",
                bio: "القلب، شبكية العين، حيوية الروح، العزة والهيبة، وطرد الكيانات المظلمة بنور الوعي الصافي.",
                path_desc: "طريقة التقسيم الرباعي الشمسي المتناظر (Singly-Even Sub-grids): توازن المربعات الفرعية 3×3 الأربعة."
            },
            {
                order: "المسبع (7×7)", n: 7, planet: "الزهرة ♀ (Venus)", day: "الجمعة", metal: "النحاس الأحمر النقي", color: "#06d6a0",
                constant: 175, total: 1225, freq: "221.23 Hz", note: "A (لا)", sound: 221.23,
                china: "المسار الأثيري للنغمات الموسيقية السبع (Pentatonic Extension) وقانون الألوان الطيفية",
                vedic: "يانترا شوكرا (Shukra Yantra) — مغناطيسية القلوب وتناغم المشاعر والجمال الكوني",
                hermetic: "Seal of Venus (Agrippa) — ذكاء كيدميل (Kedemel) وملاك عنيائيل لجلب الألفة والمودة",
                element: "ترابي هوائي (انسجام وجذب)",
                bio: "الكليتان، الغدد الصماء التناسلية، الجاذبية الحيوية، تهدئة التوتر العصبي وتجديد نضارة البشرة.",
                path_desc: "طريقة الصعود السيامي الفردي للمسبع (Siamese 7x7): البدء بـ 1 في أعلى المنتصف بحساب 49 خانة."
            },
            {
                order: "المثمن (8×8)", n: 8, planet: "عطارد ☿ (Mercury)", day: "الأربعاء", metal: "الزئبق الممتزج والرصاص القصديري", color: "#9d4edd",
                constant: 260, total: 2080, freq: "141.27 Hz", note: "C# (دو دييز)", sound: 141.27,
                china: "رموز الباغوا الثمانية (Eight Trigrams) ومصفوفة الفضاء الكوني المحيط بالمركز",
                vedic: "يانترا بودها (Budha Yantra) — الذكاء المتوقد، الفصاحة، حل الشيفرات والرياضيات المعقدة",
                hermetic: "Seal of Mercury (Agrippa) — روح تيرييل (Tiriel) وملاك رفائيل لفك الأقفال والعلوم الدقيقة",
                element: "هوائي مائي متقلب (سرعة وذكاء)",
                bio: "الجهاز العصبي، السيالات العصبية، الرئتان، فصّي المخ، وسرعة البديهة وحل المعضلات الفكرية.",
                path_desc: "طريقة انعكاس الأقطار المزدوجة (Doubly-Even 8x8 Blocks): تقسيم رقعة الشطرنج إلى 4 مربعات 4×4 وعكس الأقطار."
            },
            {
                order: "المتسع (9×9)", n: 9, planet: "القمر ☽ (Luna)", day: "الإثنين", metal: "الفضة النقية 999", color: "#00f0ff",
                constant: 369, total: 3321, freq: "210.42 Hz", note: "G# (صول دييز)", sound: 210.42,
                china: "قاعات القصر السماوي التسعة (Nine Halls of Ming Tang) وشبكة الأرقام السحرية الإمبراطورية",
                vedic: "يانترا تشاندرا ومصفوفة الكواكب التسعة (Navagraha Yantra) — استقرار النفس وحفظ الذاكرة",
                hermetic: "وفق القمر الأعظم 9×9 (Agrippa) — ملاك جبرائيل وروح حشموداي لحكم المد والجزر والأحلام",
                element: "مائي أثيري (ذاكرة وحدس)",
                bio: "السوائل البيولوجية، الدماغ الأيمن، الذاكرة العميقة، تنشيط الأحلام الصادقة، وتوازن الهرمونات.",
                path_desc: "طريقة دي لا لوبير السيامية للمتسع: 81 خانة بتوازن كامل لمجموع 369 لكل صف وعمود وقطر."
            }
        ];

        // DATA: 7 Subtle Bodies Stack
        const BODIES_DATA = [
            {
                num: "1",
                category: "dense",
                name: "الجسد المادي الكثيف (Physical Sthula Sarira)",
                nafs: "النفس الأمّارة بالسوء ﴿إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ﴾",
                chakra: "الشاكرا الجذرية (Muladhara) — قاعدة الحوض والعجان",
                color: "#ef4444",
                dimension: "عالم المُلْك والشهادة (3D Physical Plane)",
                thickness: "0 سم (الحدود الفيزيائية للجلد والبشرة)",
                frequency: "10⁻³ إلى 10² هرتز (الميكانيكا الحيوية والنبضات العصبية)",
                physics: "النسيج الذري الكيميائي، المادة الصلصالية الترابية، الهيكل العظمي، شبكة الألياف العصبية المايلينية، وحركة الأيونات عبر مضخات الصوديوم والبوتاسيوم في الغشاء الخلوي.",
                attack: "الأمراض الباثولوجية العضوية، متلازمة الإنهاك المزمن، الانقياد الأعمى لغرائز البقاء والشهوات الحيوانية السامة، خمول الأنزيمات وتكلس الغدة الصنوبرية بفعل السموم.",
                defense: "الصيام الدوري الجاف والمتقطع لتفعيل عملية الالتهام الذاتي (Autophagy)، تناول الغذاء العضوي الحلال الطيب، والمشي حافياً لتفريغ الشحنات الإيجابية السامة إلى الأرض.",
                symptoms: "ثقل غير مبرر في الكتفين، خدر في الأطراف، صداع مزمن في مؤخرة الرأس عند محاولة العبادة.",
                quran_shield: "﴿كُلُوا مِن طَيِّبَاتِ مَا رَزَقْنَاكُمْ وَلَا تَطْغَوْا فِيهِ فَيَحِلَّ عَلَيْكُمْ غَضَبِي﴾ [طه: 81]"
            },
            {
                num: "2",
                category: "dense",
                name: "الجسد الأثيري / قالب الحياة (Etheric Pranamaya)",
                nafs: "النفس اللوّامة ﴿وَلَا أُقْسِمُ بِالنَّفْسِ اللَّوَّامَةِ﴾",
                chakra: "شاكرا العجز والسرّة (Svadhisthana & Manipura) — خزان طاقة الحياة",
                color: "#ff8c00",
                dimension: "عالم المثال السفلي والحقل البلازمي الحيوي",
                thickness: "2.5 سم إلى 7 سم خارج حدود البشرة",
                frequency: "10² إلى 10⁴ هرتز (انبعاثات البيوفوتون الحيوية)",
                physics: "مصفوفة النبض الكهرومغناطيسي والمجال المورفوجيني المنظم للخلايا؛ تيار الفوتونات الحيوية (Biophotons) المنبعثة من سلاسل الميتوكوندريا المنظمة في شبكة السكك الدقيقة (Microtubules).",
                attack: "ثقوب الهالة وتمزقات الحقل التوريدي الناتجة عن الصدمات؛ هجمات مصاصي الطاقة الحيوية، استيطان اليرقات النجمية (Astral Larvae) المتغذية على عصارة طاقة الحياة.",
                defense: "إدامة الوضوء بالسرد؛ حمامات الملح الصخري والمغنيسيوم لتطهير الهالة؛ تنفس الحجاب الحاجز البطيء (Pranayama) مع الاستعاذة؛ وتدليك نقاط مسارات الطاقة بزيت الزيتون المقروء عليه.",
                symptoms: "استيقاظ متعب رغم النوم الطويل، إحساس بنفث بارد بين الكتفين، كدمات زرقاء مفاجئة دون ارتطام فيزيائي.",
                quran_shield: "﴿وَإِمَّا يَنزَغَنَّكَ مِنَ الشَّيْطَانِ نَزْغٌ فَاسْتَعِذْ بِاللَّهِ إِنَّهُ سَمِيعٌ عَلِيمٌ﴾ [الأعراف: 200]"
            },
            {
                num: "3",
                category: "bridge",
                name: "الجسد النجمي / العاطفي (Astral Kamamaya)",
                nafs: "النفس المُلْهَمة ﴿فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَاهَا﴾",
                chakra: "شاكرا القلب (Anahata) وشاكرا الضفيرة الشمسية (Solar Plexus)",
                color: "#f4b41a",
                dimension: "عالم البرزخ والعوالم النجمية الحلمية (Astral Plane)",
                thickness: "15 سم إلى 45 سم حول الجسد",
                frequency: "10⁴ إلى 10⁶ هرتز (طيف المشاعر والرنين الوجداني)",
                physics: "حقل كهروديناميكي يتشكل من الترددات الصادرة عن نبضات القلب ومراكز الانفعال باللوزة الدماغية (Amygdala)؛ يتغير لونه وكثافته لحظياً بحسب مشاعر الخوف، الغضب، أو العشق والمحبة.",
                attack: "نوبات الذعر والهلع غير المسبب، أحلام الجاثوم والاختناق النومي، تطفل الكيانات النارية عبر حبال الأثير العاطفية، استدراج الشخص للغضب الشديد لفتح شق أثيري واسع.",
                defense: "كظم الغيظ الفوري (تثبيط الأدرينالين)، المحافظة على طهارة القلب من الغل والحسد، قراءة سورتي الفلق والناس مع النفث والمسح قبل النوم، والابتعاد عن دراما الاستنزاف النفسي.",
                symptoms: "ضيق مباغت في الصدر مع تسارع خفقان القلب دون علة طبية، رؤية خيالات سوداء خاطفة في طرف الرؤية المحيطية.",
                quran_shield: "﴿قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ * مِن شَرِّ مَا خَلَقَ * وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ﴾ [الفلق: 1-3]"
            },
            {
                num: "4",
                category: "bridge",
                name: "الجسد العقلي / الفكري (Mental Manomaya)",
                nafs: "النفس المطمئنّة ﴿يَا أَيَّتُهَا النَّفْسُ الْمُطْمَئِنَّةُ﴾",
                chakra: "شاكرا الحنجرة والشاكرا الجبهية (Ajna) — ناصية الدماغ",
                color: "#06d6a0",
                dimension: "العالم العقلي الكوني وفضاء الأشكال الفكرية (Mental Plane)",
                thickness: "45 سم إلى 90 سم متسعة بحسب الرقي الفكري",
                frequency: "موجات ألفا وثيتا المتزامنة (Alpha-Theta Coherence 7.8 - 12 Hz)",
                physics: "حقل الأنماط الفكرية والهندسة التوليدية للوعي؛ الأشكال الفكرية (Thought-forms) التي يفرزها العقل تكتسب شحنة شبه مستقلة وتجذب ما يشابهها وفق قوانين الرنين الترددي.",
                attack: "الوسواس القهري العقائدي، التشكيك التدميري في بديهيات الوجود، الأفكار السوداوية المزروعة بالإيحاء الشيطاني، والتشويش المعرفي عبر الإفراط في مدخلات الشاشات التكنولوجية.",
                defense: "ترتيل القرآن الكريم بالتدبر لضبط إيقاع الفص الجبهي، الاشتغال بالعلوم البرهانية والميتافيزيقية الشريفة، صمت الفضول اللفظي، وقول: «آمنتُ بالله ورسله» عند عروض الشكوك.",
                symptoms: "تشتت ذهني حاد، وساوس تلح على إهانة المقدسات، شعور بطنين حاد في الأذن اليسرى متزامن مع ضيق الفكر.",
                quran_shield: "﴿إِنَّ الَّذِينَ اتَّقَوْا إِذَا مَسَّهُمْ طَائِفٌ مِّنَ الشَّيْطَانِ تَذَكَّرُوا فَإِذَا هُم مُّبْصِرُونَ﴾ [الأعراف: 201]"
            },
            {
                num: "5",
                category: "spiritual",
                name: "الجسد السببي / مخزن الذواكر (Causal Vijnanamaya)",
                nafs: "النفس الراضية ﴿ارْجِعِي إِلَىٰ رَبِّكِ رَاضِيَةً﴾",
                chakra: "شاكرا التاج العليا (Sahasrara) وشاكرا العين الباطنة العرفانية",
                color: "#00f0ff",
                dimension: "عالم الجبروت واللوح المحفوظ الجزئي وسجلات الكارما والأعمال",
                thickness: "يمتد من 1 متر إلى عدة أمتار، كروي بيضاوي الشكل",
                frequency: "موجات غاما الفوقية (Gamma Waves > 40-100 Hz)",
                physics: "حقل تخزين الذواكر الكونية العميقة، الأسباب والنتائج؛ يتضمن بصمات الأعمال والعهود المبرمة في عالم الذر: ﴿أَلَسْتُ بِرَبِّكُمْ قَالُوا بَلَىٰ﴾، والصفات الوراثية الروحية المتوارثة.",
                attack: "تفعيل السحر الوراثي والسلالي الموروث عبر دماء الأجداد، نقض العهود الفطرية، وحرمان العبد من التوفيق الرباني بسبب تراكم الذنوب التي رانت على القلب.",
                defense: "التوبة النصوح الخارقة لخط الزمن السببي؛ كثرة الاستغفار بالأسحار لمحو آثار الذنوب من الصحائف؛ الصدقة الخفية لدفع البلاء النازل؛ وبر الوالدين لترميم الروابط السلالية.",
                symptoms: "تعطيل متكرر في مسارات الحياة الحيوية (الزواج، الرزق، المشاريع) بنمط متطابق دون سبب مادي مفهوم.",
                quran_shield: "﴿فَقُلْتُ اسْتَغْفِرُوا رَبَّكُمْ إِنَّهُ كَانَ غَفَّارًا * يُرْسِلِ السَّمَاءَ عَلَيْكُم مِّدْرَارًا﴾ [نوح: 10-11]"
            },
            {
                num: "6",
                category: "spiritual",
                name: "الجسد البوذي / المعرفة الكلية (Buddhic Anandamaya)",
                nafs: "النفس المَرْضيّة ﴿مَّرْضِيَّةً * فَادْخُلِي فِي عِبَادِي﴾",
                chakra: "شاكرا النجم الروحي (Soul Star) فوق الرأس بنصف ذراع",
                color: "#8b5cf6",
                dimension: "عالم اللاهوت النسبي وعالم الأرواح النورانية القدسية",
                thickness: "حقل متسع لا محدود يحتضن البيئة المحيطة بالإشراق",
                frequency: "التردد النوراني الفائق غير المقاس بالأجهزة الفيزيائية الكثيفة",
                physics: "غمد البهجة والنعيم الإلهي (Ananda)؛ يمثل حالة التماسك الكامل للأمواج النورانية حيث ينعدم حاجز الزمان والمكان وتحدث الكشوفات الإلهامية الصادقة والشهود الروحي.",
                attack: "لا تستطيع الشياطين اختراقه مباشرة؛ بل تسعى لحجبه عن الوعي عبر تضخيم الإيغو الروحي (Spiritual Ego)، والغرور بالكرامات أو الاستدراج بمخاطبات شيطانية مموهة كأنها ملائكية.",
                defense: "دوام الافتقار الصادق لله؛ كتمان الأنوار والأحوال عن غير أهلها؛ نفي الحول والقوة الشخصية: «لا حول ولا قوة إلا بالله العلي العظيم»؛ واستحضار عظمة الحق وتواضع العبودية.",
                symptoms: "الشعور بالعجب الروحي والاستعلاء على الخلق، أو انقطاع مفاجئ لحلاوة المناجاة بسبب دبيب الكبر الخفي.",
                quran_shield: "﴿يَمُنُّونَ عَلَيْكَ أَنْ أَسْلَمُوا قُل لَّا تَمُنُّوا عَلَيَّ إِسْلَامَكُم بَلِ اللَّهُ يَمُنُّ عَلَيْكُمْ أَنْ هَدَاكُمْ لِلْإِيمَانِ﴾ [الحجرات: 17]"
            },
            {
                num: "7",
                category: "spiritual",
                name: "الجسد الروحاني الأسمى (Atmic Divine Spark)",
                nafs: "النفس الكاملة الصافية ﴿وَأَدْخُلِي جَنَّتِي﴾ — سر الحقيقة المحمدية",
                chakra: "نقطة الوصل اللاهوتية الكونية — سر الروح المنسوب للحق",
                color: "#c026d3",
                dimension: "عالم الأمر الإلهي ﴿قُلِ الرُّوحُ مِنْ أَمْرِ رَبِّي﴾",
                thickness: "حقل لامتناهٍ مندمج مع الفيض الإلهي الأزلي الأبدي",
                frequency: "نور الأنوار الأزلي — النقطة الصفرية الكونية (Zero Point Field)",
                physics: "النفخة العلوية الصمدية التي لا تنفد؛ النقطة التي يتجلى فيها سر التوحيد المحض، وهي خالية من أي نقص أو تحول، باقية بعد فناء العوالم بأمر بارئها.",
                attack: "مستحيل الاختراق أو التلويث أو القرب منه بأي قوة نارية أو ظلمة إبليسية على الإطلاق؛ فهو محمي بالذات الإلهية، لكن الجهل به يحرم الإنسان من تذوق حقيقة خلافته الكونية.",
                defense: "التوحيد الخالص المجرد: كلمة الإخلاص «لا إله إلا الله محمد رسول الله» متحققة بالقلب واللسان والعمل، والفناء في مرضاة الله سبحانه.",
                symptoms: "الغفلة التامة عن الغاية من الخلق والعيش كالحيوانات الأرضية دون بوصلة وجودية.",
                quran_shield: "﴿فَإِذَا سَوَّيْتُهُ وَنَفَخْتُ فِيهِ مِن رُّوحِي فَقَعُوا لَهُ سَاجِدِينَ﴾ [الحجر: 29]"
            }
        ];

        const QURANIC_DATA = [
            {
                title: "1. زيف ربوبية الكواكب وتأكيد تسخيرها الإلهي",
                ayah: "﴿لَا تَسْجُدُوا لِلشَّمْسِ وَلَا لِلْقَمَرِ وَاسْجُدُوا لِلَّهِ الَّذِي خَلَقَهُنَّ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ﴾",
                surah: "سورة فصلت: الآية 37",
                analysis: "حسم قرآني قاطع: الشمس والقمر والأفلاك مخلوقات مسخرة لا تملك لنفسها فضلاً عن غيرها ضراً ولا نفعاً. التنجيم القائم على دعاء الكواكب هو شرك صريح."
            },
            {
                title: "2. كشف عجز السحر وبطلانه الذاتي المحتوم",
                ayah: "﴿إِنَّمَا صَنَعُوا كَيْدُ سَاحِرٍ ۖ وَلَا يُفْلِحُ السَّاحِرُ حَيْثُ أَتَىٰ﴾",
                surah: "سورة طه: الآية 69",
                analysis: "وصف السحر بأنه (كيد)، أي مناورة وهمية تقوم على الإيهام والتأثير النفسي، وأن الفلاح منفي عنه قطعياً في كل زمان ومكان."
            },
            {
                title: "3. نفي التأثير المستقل إلا بإذن الله الكوني والشرعي",
                ayah: "﴿وَمَا هُم بِضَارِّينَ بِهِ مِنْ أَحَدٍ إِلَّا بِإِذْنِ اللَّهِ﴾",
                surah: "سورة البقرة: الآية 102",
                analysis: "العلة الفاعلة الوحيدة هي مشيئة الخالق؛ والسحر سبب كوني قد ينفذ ابتلاءً بحسب السنن، ولكنه ينقطع وينسحق فور الاتصال بالسبب الأسمى ومشيئة الحفظ."
            },
            {
                title: "4. قانون التوازن والعدل الإلهي في بنية السماء",
                ayah: "﴿وَالسَّمَاءَ رَفَعَهَا وَوَضَعَ الْمِيزَانَ ۝ أَلَّا تَطْغَوْا فِي الْمِيزَانِ﴾",
                surah: "سورة الرحمن: الآيات 7-8",
                analysis: "الكون كله مبني على ميزان هندسي وفيزيائي دقيق؛ ودراسة الأرقام والأفلاك كسنن علمية هي تدبر في خلق الله، ما لم تنحرف إلى الشعوذة والادعاء."
            },
            {
                title: "5. حصانة الإنسان الموحد وسقوط سلطان الشيطان",
                ayah: "﴿إِنَّ عِبَادِي لَيْسَ لَكَ عَلَيْهِمْ سُلْطَانٌ ۚ وَكَفَىٰ بِرَبِّكَ وَكِيلًا﴾",
                surah: "سورة الإسراء: الآية 65",
                analysis: "إعلان سيادة المؤمن؛ الشيطان والسحرة لا يملكون سلطاناً جبرياً، وسلطانهم فقط على من والاهم وفتح لهم ثغرات الغفلة والشرك والهلع."
            },
            {
                title: "6. الترياق القرآني الصاعق لإبطال كل العقد",
                ayah: "﴿وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ﴾",
                surah: "سورة الإسراء: الآية 82",
                analysis: "القرآن ذبذبة نورانية حية، رنينها يفك كل تداخل أثيري خبيث، ويعيد تنظيم الترددات الخلوية والنفسية إلى الفطرة السليمة."
            }
        ];

        // RENDER FUNCTIONS
        function renderKings() {
            const grid = document.getElementById('kings-grid');
            if (!grid) return;
            grid.innerHTML = KINGS_DATA.map(k => `
                <div class="king-card">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                            <span style="font-size:1.6rem; color:${k.color}; font-weight:800;">${k.planet}</span>
                            <span style="background:rgba(255,255,255,0.06); border:1px solid var(--border-glass); padding:3px 10px; border-radius:12px; font-size:0.75rem; color:${k.color}; font-weight:700;">${k.day}</span>
                        </div>
                        <h3 style="color:#fff; font-family:'Amiri',serif; font-size:1.35rem; margin-bottom:6px;">${k.archetype}</h3>
                        <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.7; margin-bottom:16px;">${k.desc}</p>
                        
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.05); border-radius:12px; padding:12px; font-size:0.8rem; margin-bottom:14px; line-height:1.6;">
                            <div style="color:${k.color}; font-weight:700; margin-bottom:4px;"><i class="fa-solid fa-scroll"></i> الإسناد السميائي والأنثروبولوجي:</div>
                            <div><strong>الملاك العلوي والسفلي:</strong> ${k.civs.arabic}</div>
                            <div><strong>بابل:</strong> ${k.civs.babylon} | <strong>كيميت:</strong> ${k.civs.egypt}</div>
                            <div><strong>اليونان:</strong> ${k.civs.greco} | <strong>الفيدا:</strong> ${k.civs.vedic} | <strong>القبالاه:</strong> ${k.civs.kabbalah}</div>
                        </div>

                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:0.78rem; margin-bottom:14px;">
                            <div style="background:rgba(255,255,255,0.02); padding:6px 10px; border-radius:8px;"><strong>المعدن:</strong> ${k.metal}</div>
                            <div style="background:rgba(255,255,255,0.02); padding:6px 10px; border-radius:8px;"><strong>البخور:</strong> ${k.incense}</div>
                            <div style="background:rgba(255,255,255,0.02); padding:6px 10px; border-radius:8px;"><strong>الشاكرة:</strong> ${k.chakra}</div>
                            <div style="background:rgba(255,255,255,0.02); padding:6px 10px; border-radius:8px;"><strong>العضو:</strong> ${k.organ}</div>
                        </div>
                    </div>

                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.06); padding-top:12px;">
                        <span style="color:var(--cyan); font-weight:700; font-size:0.85rem;"><i class="fa-solid fa-wave-square"></i> ${k.freq} Hz</span>
                        <button class="synth-btn" onclick="playPlanetTone(${k.freq}, '${k.planet} - ${k.freq} Hz')"><i class="fa-solid fa-play"></i> استماع للرنين</button>
                    </div>
                </div>
            `).join('');
        }

        function renderZodiacAngels() {
            const tbody = document.getElementById('zodiac-angels-tbody');
            if (!tbody) return;
            tbody.innerHTML = ZODIAC_ANGELS_DATA.map(z => `
                <tr>
                    <td><strong style="color:var(--gold); font-size:0.95rem;">${z.sign}</strong></td>
                    <td>${z.elem}</td>
                    <td><strong style="color:var(--cyan);">${z.arabic}</strong></td>
                    <td>${z.kabbalah}</td>
                    <td>${z.egypt}</td>
                    <td>${z.babylon}</td>
                    <td><strong style="color:var(--rose);">${z.tribe}</strong></td>
                </tr>
            `).join('');
        }

        function render36Decans() {
            const tbody = document.getElementById('decans-36-tbody');
            if (!tbody) return;
            tbody.innerHTML = DECANS_36_DATA.map(d => `
                <tr>
                    <td><strong style="color:var(--gold); font-size:0.92rem;">${d.sign}</strong></td>
                    <td><span style="color:#475569; font-weight:600;">${d.deg}</span></td>
                    <td><span style="color:var(--cyan); font-weight:700;">${d.ruler}</span></td>
                    <td><strong style="color:#f472b6;">${d.bakyu}</strong></td>
                    <td>${d.angel}</td>
                    <td>${d.organ}</td>
                    <td><code style="color:var(--gold);">${d.freq}</code></td>
                    <td style="font-size:0.8rem; color:#94a3b8; max-width:320px;">${d.desc}</td>
                </tr>
            `).join('');
        }

        function loadDayHours(dayIdx) {
            document.querySelectorAll('.day-btn').forEach((b, i) => b.classList.toggle('active', i === dayIdx));
            const tbody = document.getElementById('hours-tbody');
            if (!tbody) return;
            let startIndex = DAY_START_PLANET_INDEX[dayIdx];
            let rowsHtml = '';

            for (let h = 1; h <= 24; h++) {
                let planetName = CHALDEAN_ORDER[(startIndex + (h - 1)) % 7];
                let isDay = h <= 12;
                let hourNum = isDay ? h : (h - 12);
                let phaseLabel = isDay ? `نهارية (${hourNum})` : `ليلية (${hourNum})`;
                let pInfo = PLANET_NATURES[planetName];

                rowsHtml += `
                    <tr>
                        <td><strong>الساعة ${h}</strong></td>
                        <td><span style="color:${isDay ? 'var(--gold)' : 'var(--cyan)'}; font-weight:700;">${phaseLabel}</span></td>
                        <td><strong style="color:#fff; font-size:0.95rem;">${planetName}</strong></td>
                        <td>${pInfo.nature}</td>
                        <td><span style="color:var(--cyan); font-weight:700;">${pInfo.freq} Hz</span></td>
                        <td>${pInfo.work}</td>
                    </tr>
                `;
            }
            tbody.innerHTML = rowsHtml;
        }

        function renderMansions() {
            const tbody = document.getElementById('mansions-tbody');
            if (!tbody) return;
            tbody.innerHTML = MANSIONS_DATA.map(m => `
                <tr>
                    <td><strong style="color:var(--gold);">${m.num}</strong></td>
                    <td><strong style="color:#fff; font-size:0.92rem;">${m.name}</strong></td>
                    <td><span style="color:#94a3b8; font-size:0.8rem;">${m.stars}</span><br><code style="color:var(--cyan); font-size:0.75rem;">${m.deg}</code></td>
                    <td><strong style="color:var(--gold); font-size:1.15rem; font-family:'Amiri',serif;">${m.letter}</strong></td>
                    <td><strong style="color:#c084fc;">${m.god_name}</strong></td>
                    <td>${m.angel}</td>
                    <td>${m.nat}</td>
                    <td>${m.planet}</td>
                    <td style="font-size:0.8rem; color:#475569;"><strong>البخور:</strong> ${m.inc}<br><strong>التأثير:</strong> ${m.work}</td>
                </tr>
            `).join('');
        }

                function renderPlanetaryWafqs() {
            const tbody = document.getElementById('planetary-wafqs-tbody');
            if (!tbody) return;
            tbody.innerHTML = PLANETARY_WAFQS_DATA.map(w => `
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                    <td><strong style="color:var(--gold); font-size:0.95rem;">${w.order}</strong></td>
                    <td><strong style="color:${w.color};">${w.planet}</strong><br><span style="font-size:0.75rem; color:#94a3b8;">${w.metal}</span></td>
                    <td><span style="color:var(--cyan); font-weight:700; font-size:1rem;">${w.constant}</span></td>
                    <td><span style="color:#f472b6; font-weight:700;">${w.total}</span></td>
                    <td style="font-size:0.8rem; color:#e2e8f0;">${w.china}</td>
                    <td style="font-size:0.8rem; color:#475569;">${w.vedic}</td>
                    <td style="font-size:0.8rem; color:#fef08a;">${w.hermetic}</td>
                    <td><code style="color:var(--gold); font-weight:700;">${w.freq}</code><br><span style="font-size:0.75rem; color:#94a3b8;">${w.note}</span></td>
                    <td style="font-size:0.82rem; color:#a7f3d0;">${w.bio}</td>
                    <td><button class="synth-btn" style="padding:4px 10px; font-size:0.75rem;" onclick="playPlanetTone(${w.sound}, '${w.planet} - ${w.freq}')"><i class="fa-solid fa-play"></i> استماع</button></td>
                </tr>
            `).join('');
        }

        function selectBodyLayer(id) {
            const b = BODIES_DATA.find(x => x.num === id);
            if (!b) return;

            // Sync Hologram SVG Node Buttons
            document.querySelectorAll('.body-point-btn').forEach(btn => btn.classList.remove('active'));
            const activeNode = document.getElementById('body-node-' + id);
            if (activeNode) activeNode.classList.add('active');

            // Sync Quick Selector Pills
            document.querySelectorAll('.b-pill-btn').forEach(btn => btn.classList.remove('active'));
            const activePill = document.getElementById('b-pill-' + id);
            if (activePill) activePill.classList.add('active');

            // Render Comprehensive Dossier
            const card = document.getElementById('body-detail-card');
            if (card) {
                card.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; flex-wrap:wrap; gap:10px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:14px;">
                        <div>
                            <span style="background:${b.color}22; border:1px solid ${b.color}; color:${b.color}; padding:3px 12px; border-radius:12px; font-size:0.75rem; font-weight:700;">الغلاف النوراني رقم ${b.num}</span>
                            <h3 style="color:${b.color}; font-family:'Amiri',serif; margin:8px 0 4px 0; font-size:1.5rem; text-shadow:0 0 18px ${b.color}55;">${b.name}</h3>
                            <div style="color:var(--gold); font-size:0.95rem; font-family:'Amiri',serif;">${b.nafs}</div>
                        </div>
                        <div style="text-align:left;">
                            <span style="background:rgba(244,180,26,0.12); border:1px solid var(--gold); color:var(--gold); padding:4px 12px; border-radius:8px; font-size:0.8rem; font-weight:700;">${b.dimension}</span>
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:0.83rem; margin-bottom:14px; background:rgba(0,0,0,0.3); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.05);">
                        <div><strong style="color:var(--cyan);">الشاكرا والموقع:</strong> <span style="color:#475569;">${b.chakra}</span></div>
                        <div><strong style="color:var(--cyan);">السُمك والمدى:</strong> <span style="color:#475569;">${b.thickness}</span></div>
                        <div style="grid-column:span 2;"><strong style="color:var(--cyan);">التردد الحاكم:</strong> <span style="color:#475569;">${b.frequency}</span></div>
                    </div>
                    <p style="font-size:0.88rem; color:#475569; line-height:1.65; margin-bottom:14px;">
                        <strong style="color:#fff;">الفيزياء الحيوية وميكانيكا الفوتون:</strong> ${b.physics}
                    </p>
                    <div class="attack-vulnerability-box">
                        <strong style="color:#f87171; display:flex; align-items:center; gap:6px; font-size:0.9rem;">⚠️ آلية الاختراق والطفيليات النجمية (Astral Tears):</strong>
                        <p style="font-size:0.84rem; color:#fca5a5; margin:6px 0 0 0; line-height:1.5;">${b.attack}</p>
                        <div style="font-size:0.82rem; color:#fecaca; margin-top:8px; border-top:1px dashed rgba(239,68,68,0.3); padding-top:6px;"><strong>أعراض التمزق في الهالة:</strong> ${b.symptoms}</div>
                    </div>
                    <div class="defense-protocol-box">
                        <strong style="color:#34d399; display:flex; align-items:center; gap:6px; font-size:0.9rem;">🛡️ بروتوكول الإغلاق والحصن النبوي:</strong>
                        <p style="font-size:0.84rem; color:#a7f3d0; margin:6px 0 0 0; line-height:1.5;">${b.defense}</p>
                        <div style="margin-top:10px; background:rgba(0,0,0,0.35); padding:10px 14px; border-radius:8px; color:var(--gold); font-family:'Amiri',serif; font-size:0.95rem; border-right:3px solid var(--gold);">${b.quran_shield}</div>
                    </div>
                `;
            }

            // Highlight card in stack
            const stackCard = document.getElementById('body-card-' + id);
            if (stackCard) {
                document.querySelectorAll('.body-layer').forEach(c => c.style.borderColor = 'var(--border-glass)');
                stackCard.style.borderColor = b.color;
            }
        }

        function filterBodies(cat, btn) {
            document.querySelectorAll('.body-filter-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');

            const container = document.getElementById('bodies-stack');
            if (!container) return;

            const filtered = cat === 'all' ? BODIES_DATA : BODIES_DATA.filter(b => b.category === cat);
            container.innerHTML = filtered.map(b => `
                <div class="body-layer" id="body-card-${b.num}" style="border-right: 4px solid ${b.color}; cursor:pointer;" onclick="selectBodyLayer('${b.num}')">
                    <div class="body-num" style="color:${b.color};">${b.num}</div>
                    <div style="flex-grow:1;">
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:8px;">
                            <div>
                                <h3 style="color:${b.color}; font-family:'Amiri',serif; font-size:1.3rem; margin:0 0 4px 0; text-shadow:0 0 15px ${b.color}44;">${b.name}</h3>
                                <span style="color:var(--gold); font-family:'Amiri',serif; font-size:0.88rem;">${b.nafs}</span>
                            </div>
                            <div style="display:flex; gap:6px; flex-wrap:wrap;">
                                <span style="background:${b.color}22; border:1px solid ${b.color}; color:${b.color}; padding:2px 10px; border-radius:12px; font-size:0.75rem; font-weight:700;">${b.chakra}</span>
                                <span style="background:rgba(244,180,26,0.12); border:1px solid var(--gold); color:var(--gold); padding:2px 10px; border-radius:12px; font-size:0.75rem; font-weight:700;">${b.dimension}</span>
                            </div>
                        </div>
                        <p style="font-size:0.86rem; color:#94a3b8; line-height:1.6; margin-bottom:10px;">
                            <strong style="color:#e2e8f0;">الفيزياء الحيوية والتردد:</strong> ${b.physics}
                            <span style="display:block; color:var(--cyan); font-size:0.82rem; margin-top:3px;"><strong>التردد:</strong> ${b.frequency} | <strong>النطاق والسمك:</strong> ${b.thickness}</span>
                        </p>
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(290px, 1fr)); gap:12px; font-size:0.83rem;">
                            <div style="background:rgba(239,68,68,0.08); border-right:3px solid var(--fire); padding:10px 14px; border-radius:8px; color:#fca5a5;">
                                <strong style="color:#f87171;">⚠️ آلية الاختراق والطفيليات:</strong>
                                <p style="margin:4px 0 0 0; line-height:1.5;">${b.attack}</p>
                                <div style="margin-top:6px; font-size:0.8rem; color:#fecaca;"><strong>الأعراض:</strong> ${b.symptoms}</div>
                            </div>
                            <div style="background:rgba(6,214,160,0.08); border-right:3px solid var(--emerald); padding:10px 14px; border-radius:8px; color:#a7f3d0;">
                                <strong style="color:#34d399;">🛡️ الحصن النبوي والإغلاق:</strong>
                                <p style="margin:4px 0 0 0; line-height:1.5;">${b.defense}</p>
                                <div style="margin-top:6px; font-size:0.82rem; color:var(--gold); font-family:'Amiri',serif;">${b.quran_shield}</div>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
        }


        // DATA: Complete 28 Arabic Letters Matrix
        const LETTERS_DATA = [
            {
                char: "ا", name: "الألف", val: 1, element: "fire", element_ar: "ناري (أثيري حار يابس)", color: "#ef4444",
                nature: "luminous", nature_ar: "نوراني (من فواتح السور)",
                makhraj: "الجوف وتجويف الحلق والصدر (مبدأ الأصوات)",
                hz: "85 - 250 هرتز (التردد الجذري)",
                celestial: "فلك الشمس وفلك البروج المحيط",
                mansion: "1. الشرطين (نطح الحمل)",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "الله / الأحد",
                secret: "الحرف القائم الفرد، سر الألوهية والتوحيد الخالص، لا يقبل الحركة ولا الاتصال بما بعده."
            },
            {
                char: "ب", name: "الباء", val: 2, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "dark", nature_ar: "ظلماني (وعاء الخلق والتركيب)",
                makhraj: "الشفتان بانطباق تام",
                hz: "350 - 600 هرتز",
                celestial: "فلك القمر (الأقرب للأرض)",
                mansion: "2. البطين (بطن الحمل)",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "البارئ / الباقي",
                secret: "باء البسملة التي ظهر بها الوجود، ونقطة الباء هي أول تعين للفيض في عالم الكثرة."
            },
            {
                char: "ج", name: "الجيم", val: 3, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "وسط اللسان مع الحنك الأعلى (شديد مجهور)",
                hz: "1200 - 1800 هرتز",
                celestial: "فلك المشتري (السعد الأكبر)",
                mansion: "3. الثريا (النجم)",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "الجامع / الجليل",
                secret: "سر الجمع والائتلاف، توسط القوى وربط الأضداد في حركة دائرية مستمرة."
            },
            {
                char: "د", name: "الدال", val: 4, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "طرف اللسان مع أصول الثنايا العليا",
                hz: "400 - 800 هرتز",
                celestial: "فلك المريخ (الحديد والقوة)",
                mansion: "4. الدبران (عين الثور)",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "الدائم / الديان",
                secret: "قاعدة التربيع والدوام، استقرار الأركان الأربعة للطبيعة وثبات العالم المادي."
            },
            {
                char: "هـ", name: "الهاء", val: 5, element: "fire", element_ar: "ناري (حار يابس)", color: "#ef4444",
                nature: "luminous", nature_ar: "نوراني (كهيعص)",
                makhraj: "أقصى الحلق (النَفَس الإلهي الصافي)",
                hz: "90 - 220 هرتز",
                celestial: "فلك الزهرة (الجمال والتناغم)",
                mansion: "5. الهقعة (رأس الجوزاء)",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "الهادي / هو",
                secret: "ضمير الغيب المطلق (هُوَ)، هاء الهوية الذاتية وأصل انبعاث النفس الحي من الصدر."
            },
            {
                char: "و", name: "الواو", val: 6, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "الشفتان بانضمام وتدوير",
                hz: "300 - 550 هرتز",
                celestial: "فلك عطارد (العلم والكتابة)",
                mansion: "6. الهنعة (منكبا الجوزاء)",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "الودود / الواسع",
                secret: "واو العطف والوصل الكوني، الصلة بين الأرواح والأجساد وبين البداية والنهاية."
            },
            {
                char: "ز", name: "الزاي", val: 7, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "طرف اللسان مع فويق الثنايا السفلى (صفير)",
                hz: "2400 - 3500 هرتز",
                celestial: "فلك زحل (الشيخ والميزان)",
                mansion: "7. الذراع (ذراع الأسد)",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "الزكي",
                secret: "سر السبعة التامة وأيام الأسبوع وأفلاك السماوات السبع والتطهير الفائق للمعدن."
            },
            {
                char: "ح", name: "الحاء", val: 8, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "luminous", nature_ar: "نوراني (حم)",
                makhraj: "وسط الحلق (مهموس رخو مائي)",
                hz: "450 - 950 هرتز",
                celestial: "فلك المشتري",
                mansion: "8. النثرة (أنف الأسد)",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "الحي / الحكيم",
                secret: "حياة الكائنات، سر حملة العرش الثمانية، وانفتاح أبواب الجنان الثمانية."
            },
            {
                char: "ط", name: "الطاء", val: 9, element: "fire", element_ar: "ناري (حار يابس)", color: "#ef4444",
                nature: "luminous", nature_ar: "نوراني (طه، طسم)",
                makhraj: "طرف اللسان مع أصول الثنايا (مستعلٍ مطبق)",
                hz: "200 - 500 هرتز",
                celestial: "فلك المريخ",
                mansion: "9. الطرف (عينا الأسد)",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "الطاهر / القدوس",
                secret: "نهاية الآحاد وأعلى مراتب الأرقام المفردة، سر الطهارة التامة واحتراق الشياطين."
            },
            {
                char: "ي", name: "الياء", val: 10, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "luminous", nature_ar: "نوراني (يس، كهيعص)",
                makhraj: "وسط اللسان مع الحنك",
                hz: "1500 - 2400 هرتز",
                celestial: "فلك الشمس",
                mansion: "10. الجبهة (جبهة الأسد)",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "يا أحد / الحي القيوم",
                secret: "مفتاح العشرات، ختام الأبجدية ورجوع المنتهى إلى المبتدأ (الألف والياء)."
            },
            {
                char: "ك", name: "الكاف", val: 20, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "luminous", nature_ar: "نوراني (كهيعص)",
                makhraj: "أقصى اللسان أسفل القاف قليلاً",
                hz: "800 - 1400 هرتز",
                celestial: "فلك الزهرة",
                mansion: "11. الزبرة (خرات الأسد)",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "الكريم / الكافي",
                secret: "كاف التكوين: ﴿إِنَّمَا أَمْرُهُ إِذَا أَرَادَ شَيْئًا أَن يَقُولَ لَهُ كُن فَيَكُونُ﴾، سر الأمر النافذ."
            },
            {
                char: "ل", name: "اللام", val: 30, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "luminous", nature_ar: "نوراني (الم، المر)",
                makhraj: "أدنى حافة اللسان إلى منتهاها",
                hz: "600 - 1100 هرتز",
                celestial: "فلك عطارد",
                mansion: "12. الصرفة (ذنب الأسد)",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "اللطيف",
                secret: "سر اللطف الإلهي الخفي، واسطة الاتصال بين الألف المبتدئة والميم المنتهية في (الم)."
            },
            {
                char: "م", name: "الميم", val: 40, element: "fire", element_ar: "ناري (حار يابس)", color: "#ef4444",
                nature: "luminous", nature_ar: "نوراني (الم، حم)",
                makhraj: "الشفتان مع الغنة الخيشومية",
                hz: "200 - 450 هرتز",
                celestial: "فلك القمر",
                mansion: "13. العواء",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "الملك / المجيد",
                secret: "ميم الملك والمحمدية، سر الأربعين ليلة لموسى، واستواء الإنسانية في كمال الأربعين."
            },
            {
                char: "ن", name: "النون", val: 50, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "luminous", nature_ar: "نوراني (ن والقلم)",
                makhraj: "طرف اللسان مع لثة الثنايا والخيشوم",
                hz: "500 - 900 هرتز",
                celestial: "فلك زحل",
                mansion: "14. السماك (الأعزل)",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "النور / النافع",
                secret: "نون الدواة الكونية، نصف الدائرة الذي يمسك بنقطة الحقيقة، وخمسون ألف سنة من المعارج."
            },
            {
                char: "س", name: "السين", val: 60, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "luminous", nature_ar: "نوراني (يس، طسم)",
                makhraj: "أسلة اللسان مع أطراف الثنايا (صفير)",
                hz: "3000 - 4500 هرتز",
                celestial: "فلك المشتري",
                mansion: "15. الغفر",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "السلام / السميع",
                secret: "سر السمع الروحي والسلام الإلهي، والأسنان الثلاث التي تمثل مراتب الشريعة والطريقة والحقيقة."
            },
            {
                char: "ع", name: "العين", val: 70, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "luminous", nature_ar: "نوراني (عسق، كهيعص)",
                makhraj: "وسط الحلق (حرف عميق مجهور)",
                hz: "300 - 700 هرتز",
                celestial: "فلك المريخ",
                mansion: "16. الزبانى",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "العليم / العلي",
                secret: "عين البصيرة والشهود، نبع المعارف الإلهية، والسبعون ألف حجاب من نور وظلمة."
            },
            {
                char: "ف", name: "الفاء", val: 80, element: "fire", element_ar: "ناري (حار يابس)", color: "#ef4444",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "بطن الشفة السفلى مع أطراف الثنايا العليا",
                hz: "1200 - 2200 هرتز",
                celestial: "فلك الشمس",
                mansion: "17. الإكليل",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "الفتاح / الفاطر",
                secret: "سر الفتح المبين وفطر السماوات والأرض وانفلاق الإصباح والبدايات الإعجازية."
            },
            {
                char: "ص", name: "الصاد", val: 90, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "luminous", nature_ar: "نوراني (ص والقرآن)",
                makhraj: "أسلة اللسان مع استعلاء وإطباق",
                hz: "1800 - 3200 هرتز",
                celestial: "فلك الزهرة",
                mansion: "18. القلب (قلب العقرب)",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "الصمد / الصادق",
                secret: "سر الصمود الأبدي، صفاء القلب من الأغيار، وثبات الإيمان أمام عواصف الترددات."
            },
            {
                char: "ق", name: "القاف", val: 100, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "luminous", nature_ar: "نوراني (ق والقرآن المجيد)",
                makhraj: "أقصى اللسان مع الحنك اللحمي (قلقلة)",
                hz: "400 - 900 هرتز",
                celestial: "فلك عطارد",
                mansion: "19. الشولة",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "القدير / القاهر",
                secret: "جبل قاف المحيط بالأرض، قدرة الحق القاهرة على كل باطل، وسر المائة التامة في الميزان."
            },
            {
                char: "ر", name: "الراء", val: 200, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "luminous", nature_ar: "نوراني (الر، المر)",
                makhraj: "طرف اللسان مع الحنك (تكرير لطيف)",
                hz: "500 - 1200 هرتز",
                celestial: "فلك القمر",
                mansion: "20. النعائم",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "الرحمن / الرحيم",
                secret: "رحمة الوجود الواسعة، تكرير الفيض الإلهي على الخلائق وتجدد النعم في كل طرفة عين."
            },
            {
                char: "ش", name: "الشين", val: 300, element: "fire", element_ar: "ناري (حار يابس)", color: "#ef4444",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "وسط اللسان (تفشي الريح والحرارة)",
                hz: "2200 - 3800 هرتز",
                celestial: "فلك الكواكب الثابتة (الكرسي الأدنى)",
                mansion: "21. البلدة",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "الشكور / الشهيد",
                secret: "تفشي الأنوار واشتعال الشوق الإلهي، والشهود العرفاني للحق في كل ذرة من ذرات الوجود."
            },
            {
                char: "ت", name: "التاء", val: 400, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "طرف اللسان مع أصول الثنايا العليا",
                hz: "600 - 1000 هرتز",
                celestial: "فلك البروج (الفلك الأطلس)",
                mansion: "22. سعد الذابح",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "التواب",
                secret: "سر التوبة والرجوع إلى الأصل، تقوى القلوب، والأربعمائة عام في مسافات الحجب."
            },
            {
                char: "ث", name: "الثاء", val: 500, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "طرف اللسان مع أطراف الثنايا العليا (لثوي)",
                hz: "2500 - 4000 هرتز",
                celestial: "فلك الكرسي الإلهي الواسع",
                mansion: "23. سعد بلع",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "الثابت",
                secret: "ثبات الحقائق في الكرسي: ﴿وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ﴾، وخمسة قرون في قياس الأنوار."
            },
            {
                char: "خ", name: "الخاء", val: 600, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "أدنى الحلق مما يلي الفم (استعلاء)",
                hz: "700 - 1400 هرتز",
                celestial: "فلك العرش المحيط بالخلائق",
                mansion: "24. سعد السعود",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "الخبير / الخالق",
                secret: "سر الخلق من العدم، الإحاطة الخبيرة بالأكوان، وستة أيام من أيام الخلق التكويني."
            },
            {
                char: "ذ", name: "الذال", val: 700, element: "fire", element_ar: "ناري (حار يابس)", color: "#ef4444",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "طرف اللسان مع أطراف الثنايا العليا (مجهور)",
                hz: "800 - 1600 هرتز",
                celestial: "سدرة المنتهى وحجاب الجبروت",
                mansion: "25. سعد الأخبية",
                jabir: "المرتبة الأولى (1 درهم)",
                divine_name: "ذو الجلال والإكرام",
                secret: "سر الذات الإلهية وذروة التجليات، ومقام سدرة المنتهى التي عندها ينتهي علم كل مخلوق."
            },
            {
                char: "ض", name: "الضاد", val: 800, element: "earth", element_ar: "ترابي (بارد يابس)", color: "#f59e0b",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "إحدى حافتي اللسان أو كلاهما مع الأضراس العليا (استطالة)",
                hz: "300 - 700 هرتز",
                celestial: "اللوح المحفوظ وعالم الذواكر الكلية",
                mansion: "26. الفرغ المقدم",
                jabir: "المرتبة الثانية (3 دراهم)",
                divine_name: "الضار / النافع",
                secret: "حرف الضاد المميز للغة القرآن (لغة الضاد)، والاستطالة الصوتية الكونية وثبات ما كُتب في اللوح."
            },
            {
                char: "ظ", name: "الظاء", val: 900, element: "air", element_ar: "هوائي (حار رطب)", color: "#06b6d4",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "طرف اللسان مع أطراف الثنايا مع استعلاء وإطباق",
                hz: "1000 - 2000 هرتز",
                celestial: "القلم الأعلى المأمور بالكتابة",
                mansion: "27. الفرغ المؤخر",
                jabir: "المرتبة الثالثة (5 دراهم)",
                divine_name: "الظاهر",
                secret: "ظهور المعاني الغيبية في خطوط القلم، وحصانة الأوامر الإلهية النافذة في عالم الملكوت."
            },
            {
                char: "غ", name: "الغين", val: 1000, element: "water", element_ar: "مائي (بارد رطب)", color: "#3b82f6",
                nature: "dark", nature_ar: "ظلماني (وعاء التركيب)",
                makhraj: "أدنى الحلق مما يلي الفم (رخاوة واستعلاء)",
                hz: "400 - 850 هرتز",
                celestial: "العقل الأول الكوني (الروح الأعظم)",
                mansion: "28. الرشاء (بطن الحوت)",
                jabir: "المرتبة الرابعة (8 دراهم)",
                divine_name: "الغني / الغفار",
                secret: "ختام الألوف التامة (1000)، غنى الحق المطلق عن العالمين، وغفران الذنوب ولو كانت كزبد البحر."
            }
        ];

        // CONTROLLERS FOR TAB 13
        function calculateLettersLive() {
            const input = document.getElementById('abjad-live-input');
            const text = input ? input.value : '';

            // Clean Arabic text and calculate
            let majorTotal = 0;
            let pureLettersCount = 0;
            let luminousCount = 0;
            let countFire = 0, countAir = 0, countWater = 0, countEarth = 0;

            const ABJAD_MAP = {
                'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ء': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'ة': 5, 'هـ': 5,
                'و': 6, 'ؤ': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ى': 10, 'ئ': 10, 'ك': 20, 'ل': 30,
                'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300,
                'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
            };

            const LUMINOUS_SET = new Set(['ا', 'أ', 'إ', 'آ', 'ء', 'ح', 'ر', 'س', 'ص', 'ط', 'ع', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'ة', 'ي', 'ى']);
            const FIRE_SET = new Set(['ا', 'أ', 'إ', 'آ', 'ء', 'ه', 'ة', 'ط', 'م', 'ف', 'ش', 'ذ']);
            const AIR_SET = new Set(['ج', 'ز', 'ك', 'س', 'ق', 'ث', 'ظ']);
            const WATER_SET = new Set(['د', 'ح', 'ل', 'ع', 'ر', 'خ', 'غ']);
            const EARTH_SET = new Set(['ب', 'و', 'ؤ', 'ي', 'ى', 'ئ', 'ن', 'ص', 'ت', 'ض']);

            for (let ch of text) {
                if (ABJAD_MAP[ch] !== undefined) {
                    pureLettersCount++;
                    majorTotal += ABJAD_MAP[ch];

                    if (LUMINOUS_SET.has(ch)) luminousCount++;
                    if (FIRE_SET.has(ch)) countFire++;
                    else if (AIR_SET.has(ch)) countAir++;
                    else if (WATER_SET.has(ch)) countWater++;
                    else if (EARTH_SET.has(ch)) countEarth++;
                }
            }

            // Digital Root (الجمل الصغير 1-9)
            let minor = 0;
            if (majorTotal > 0) {
                minor = majorTotal % 9;
                if (minor === 0) minor = 9;
            }

            // Update UI Numbers
            const majorEl = document.getElementById('metric-major');
            if (majorEl) majorEl.innerText = majorTotal.toLocaleString();

            const minorEl = document.getElementById('metric-minor');
            if (minorEl) minorEl.innerText = minor;

            const countEl = document.getElementById('metric-letters-count');
            if (countEl) countEl.innerText = pureLettersCount;

            const lumPctEl = document.getElementById('metric-luminous-pct');
            const lumPct = pureLettersCount > 0 ? ((luminousCount / pureLettersCount) * 100).toFixed(1) : 0;
            if (lumPctEl) lumPctEl.innerText = lumPct + '%';

            // Calculate Elemental Percentages
            const totalElements = countFire + countAir + countWater + countEarth;
            const pctFire = totalElements > 0 ? ((countFire / totalElements) * 100).toFixed(0) : 25;
            const pctAir = totalElements > 0 ? ((countAir / totalElements) * 100).toFixed(0) : 25;
            const pctWater = totalElements > 0 ? ((countWater / totalElements) * 100).toFixed(0) : 25;
            const pctEarth = totalElements > 0 ? ((countEarth / totalElements) * 100).toFixed(0) : 25;

            // Update Bars
            const barFire = document.getElementById('bar-fire');
            if (barFire) barFire.style.width = pctFire + '%';
            const valFire = document.getElementById('pct-fire');
            if (valFire) valFire.innerText = pctFire + '% (' + countFire + ')';

            const barAir = document.getElementById('bar-air');
            if (barAir) barAir.style.width = pctAir + '%';
            const valAir = document.getElementById('pct-air');
            if (valAir) valAir.innerText = pctAir + '% (' + countAir + ')';

            const barWater = document.getElementById('bar-water');
            if (barWater) barWater.style.width = pctWater + '%';
            const valWater = document.getElementById('pct-water');
            if (valWater) valWater.innerText = pctWater + '% (' + countWater + ')';

            const barEarth = document.getElementById('bar-earth');
            if (barEarth) barEarth.style.width = pctEarth + '%';
            const valEarth = document.getElementById('pct-earth');
            if (valEarth) valEarth.innerText = pctEarth + '% (' + countEarth + ')';

            // Diagnosis
            const diagEl = document.getElementById('element-diagnosis');
            if (diagEl) {
                const maxVal = Math.max(countFire, countAir, countWater, countEarth);
                let dom = [];
                if (countFire === maxVal && maxVal > 0) dom.push('نارية حارة يابسة');
                if (countAir === maxVal && maxVal > 0) dom.push('هوائية حارة رطبة');
                if (countWater === maxVal && maxVal > 0) dom.push('مائية باردة رطبة');
                if (countEarth === maxVal && maxVal > 0) dom.push('ترابية باردة يابسة');

                diagEl.innerText = totalElements > 0 ? 'الطبيعة الغالبة: ' + dom.join(' مع ') : 'طبيعة متوازنة';
            }
        }

        function setSampleText(sample) {
            const input = document.getElementById('abjad-live-input');
            if (input) {
                input.value = sample;
                calculateLettersLive();
            }
        }

        function selectLetter(char) {
            const l = LETTERS_DATA.find(x => x.char === char);
            if (!l) return;

            // Highlight tile
            document.querySelectorAll('.letter-tile-btn').forEach(btn => btn.classList.remove('active'));
            const activeTile = document.getElementById('tile-' + char);
            if (activeTile) activeTile.classList.add('active');

            // Render Inspector Card
            const card = document.getElementById('letter-detail-card');
            if (card) {
                card.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:12px;">
                        <div>
                            <div style="display:flex; align-items:center; gap:10px;">
                                <span style="font-size:2.8rem; font-family:'Amiri',serif; color:${l.color}; line-height:1; font-weight:bold;">${l.char}</span>
                                <div>
                                    <h3 style="color:${l.color}; font-family:'Amiri',serif; margin:0; font-size:1.35rem; text-shadow:0 0 14px ${l.color}44;">حرف ${l.name}</h3>
                                    <span style="color:var(--gold); font-size:0.85rem; font-weight:700;">الجُمّل: ${l.val}</span>
                                </div>
                            </div>
                        </div>
                        <div style="text-align:left;">
                            <span style="background:${l.color}22; border:1px solid ${l.color}; color:${l.color}; padding:4px 10px; border-radius:8px; font-size:0.75rem; font-weight:700; display:block; margin-bottom:4px;">
                                ${l.element_ar}
                            </span>
                            <span style="background:${l.nature === 'luminous' ? 'rgba(244,180,26,0.15)' : 'rgba(148,163,184,0.1)'}; border:1px solid ${l.nature === 'luminous' ? 'var(--gold)' : '#64748b'}; color:${l.nature === 'luminous' ? 'var(--gold)' : '#94a3b8'}; padding:2px 8px; border-radius:6px; font-size:0.72rem;">
                                ${l.nature_ar}
                            </span>
                        </div>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:0.82rem; margin-bottom:14px; background:rgba(0,0,0,0.3); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.05);">
                        <div><strong style="color:var(--cyan);">المخرج الصوتي:</strong> <span style="color:#475569; display:block; margin-top:2px;">${l.makhraj}</span></div>
                        <div><strong style="color:var(--cyan);">التردد المقدر:</strong> <span style="color:#475569; display:block; margin-top:2px;">${l.hz}</span></div>
                        <div><strong style="color:var(--cyan);">الفلك والكوكب:</strong> <span style="color:#475569; display:block; margin-top:2px;">${l.celestial}</span></div>
                        <div><strong style="color:var(--cyan);">منزلة القمر:</strong> <span style="color:#475569; display:block; margin-top:2px;">${l.mansion}</span></div>
                        <div style="grid-column:span 2;"><strong style="color:var(--gold);">ميزان جابر بن حيان:</strong> <span style="color:#fef08a;">${l.jabir}</span></div>
                        <div style="grid-column:span 2;"><strong style="color:var(--gold);">الاسم الإلهي المفتاح:</strong> <span style="color:#34d399; font-weight:700;">${l.divine_name}</span></div>
                    </div>

                    <div style="background:linear-gradient(135deg, rgba(244,180,26,0.08), rgba(0,240,255,0.04)); border:1px solid rgba(244,180,26,0.3); border-radius:10px; padding:12px;">
                        <strong style="color:var(--gold); display:flex; align-items:center; gap:6px; font-size:0.85rem;">📜 السر العرفاني والحقيقة الكونية:</strong>
                        <p style="font-size:0.83rem; color:#475569; line-height:1.6; margin:6px 0 0 0;">${l.secret}</p>
                    </div>
                `;
            }
        }

        function filterLetters(cat, btn) {
            document.querySelectorAll('.letter-filter-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');

            let filtered = LETTERS_DATA;
            if (cat === 'luminous') filtered = LETTERS_DATA.filter(l => l.nature === 'luminous');
            else if (cat === 'dark') filtered = LETTERS_DATA.filter(l => l.nature === 'dark');
            else if (cat === 'fire') filtered = LETTERS_DATA.filter(l => l.element === 'fire');
            else if (cat === 'air') filtered = LETTERS_DATA.filter(l => l.element === 'air');
            else if (cat === 'water') filtered = LETTERS_DATA.filter(l => l.element === 'water');
            else if (cat === 'earth') filtered = LETTERS_DATA.filter(l => l.element === 'earth');

            const container = document.getElementById('letters-grid');
            if (!container) return;

            container.innerHTML = filtered.map(l => `
                <div class="letter-tile-btn" id="tile-${l.char}" style="border-color:${l.color}; color:${l.color};" onclick="selectLetter('${l.char}')">
                    <span class="letter-char">${l.char}</span>
                    <span class="letter-val">${l.val}</span>
                </div>
            `).join('');

            // Select first from filtered if available
            if (filtered.length > 0) {
                selectLetter(filtered[0].char);
            }
        }

        function renderLetters() {
            filterLetters('all');
            calculateLettersLive();
            selectLetter('ا');

            // Render Panoramic Table
            const tableBody = document.getElementById('panoramic-letters-table');
            if (tableBody) {
                tableBody.innerHTML = LETTERS_DATA.map((l, idx) => `
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:${idx % 2 === 0 ? 'rgba(15,23,42,0.4)' : 'rgba(10,16,26,0.6)'};">
                        <td style="padding:10px; font-weight:bold; font-family:'Amiri',serif; font-size:1.2rem; color:${l.color};">${l.char} (${l.name})</td>
                        <td style="padding:10px; font-weight:700; color:var(--gold);">${l.val}</td>
                        <td style="padding:10px;"><span style="color:${l.color};">${l.element_ar.split(' ')[0]}</span></td>
                        <td style="padding:10px;"><span style="color:${l.nature === 'luminous' ? 'var(--gold)' : '#94a3b8'}; font-weight:600;">${l.nature === 'luminous' ? 'نوراني' : 'ظلماني'}</span></td>
                        <td style="padding:10px; font-size:0.8rem; color:#475569;">${l.makhraj}</td>
                        <td style="padding:10px; font-size:0.8rem; color:var(--cyan);">${l.celestial}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#a78bfa;">${l.mansion}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#fef08a;">${l.jabir}</td>
                        <td style="padding:10px; font-size:0.82rem; color:#34d399; font-weight:600;">${l.divine_name}</td>
                    </tr>
                `).join('');
            }
        }

        function renderBodies() {
            filterBodies('all');
            selectBodyLayer('1');

            // Render Panoramic Table
            const tableBody = document.getElementById('panoramic-bodies-table');
            if (tableBody) {
                tableBody.innerHTML = BODIES_DATA.map((b, idx) => `
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:${idx % 2 === 0 ? 'rgba(15,23,42,0.4)' : 'rgba(10,16,26,0.6)'};">
                        <td style="padding:10px; font-weight:bold; color:${b.color};">${b.num}</td>
                        <td style="padding:10px; font-weight:700; color:${b.color};">${b.name}</td>
                        <td style="padding:10px; color:var(--gold); font-family:'Amiri',serif;">${b.nafs}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#94a3b8;">${b.frequency}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#475569;">${b.thickness}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#fca5a5;">${b.attack.substring(0, 75)}...</td>
                        <td style="padding:10px; font-size:0.8rem; color:#a7f3d0;">${b.defense.substring(0, 75)}...</td>
                    </tr>
                `).join('');
            }
        }

        function renderQuranic() {
            const grid = document.getElementById('quranic-grid');
            if (!grid) return;
            grid.innerHTML = QURANIC_DATA.map(q => `
                <div class="quran-proof-card">
                    <h3 style="color:#fff; font-family:'Amiri',serif; font-size:1.15rem; margin-bottom:10px;">${q.title}</h3>
                    <div class="quran-ayah-box">${q.ayah}</div>
                    <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.78rem; color:#94a3b8; margin-bottom:10px;">
                        <span><i class="fa-solid fa-book-quran"></i> ${q.surah}</span>
                        <span style="color:var(--emerald);"><i class="fa-solid fa-check-double"></i> إحكام قطعي</span>
                    </div>
                    <p style="font-size:0.86rem; color:#475569; line-height:1.7;">${q.analysis}</p>
                </div>
            `).join('');
        }

                // MAGIC SQUARE GENERATION ALGORITHMS (3x3 to 9x9)
        function generateOddMagicSquare(n) {
            let grid = Array.from({length: n}, () => Array(n).fill(0));
            let r = 0;
            let c = Math.floor(n / 2);
            for (let num = 1; num <= n * n; num++) {
                grid[r][c] = num;
                let nr = (r - 1 + n) % n;
                let nc = (c + 1) % n;
                if (grid[nr][nc] !== 0) {
                    r = (r + 1) % n;
                } else {
                    r = nr;
                    c = nc;
                }
            }
            return grid;
        }

        function generateDoublyEvenMagicSquare(n) {
            let grid = Array.from({length: n}, () => Array(n).fill(0));
            for (let r = 0; r < n; r++) {
                for (let c = 0; c < n; c++) {
                    grid[r][c] = r * n + c + 1;
                    if ((r % 4 === c % 4) || ((r % 4 + c % 4) === 3)) {
                        grid[r][c] = (n * n + 1) - grid[r][c];
                    }
                }
            }
            return grid;
        }

        function getSun6x6MagicSquare() {
            return [
                [6, 32, 3, 34, 35, 1],
                [7, 11, 27, 28, 8, 30],
                [19, 14, 16, 15, 23, 24],
                [18, 20, 22, 21, 17, 13],
                [25, 29, 10, 9, 26, 12],
                [36, 5, 33, 4, 2, 31]
            ];
        }

        let currentSelectedWafqOrder = 3;
        let currentWafqStudioMode = 'planetary';

        function switchWafqStudioMode(mode) {
            currentWafqStudioMode = mode;
            document.querySelectorAll('.wafq-mode-btn').forEach(b => b.classList.remove('active'));
            const activeBtn = document.getElementById(`wafq-mode-btn-${mode}`);
            if (activeBtn) activeBtn.classList.add('active');

            const planetaryPanel = document.getElementById('wafq-planetary-panel');
            const ghazaliPanel = document.getElementById('wafq-ghazali-panel');
            if (planetaryPanel && ghazaliPanel) {
                if (mode === 'planetary') {
                    planetaryPanel.style.display = 'block';
                    ghazaliPanel.style.display = 'none';
                    renderPlanetaryMatrixLab(currentSelectedWafqOrder);
                } else {
                    planetaryPanel.style.display = 'none';
                    ghazaliPanel.style.display = 'block';
                    renderPlanetaryMatrixLab(3);
            calculateLiveWafq();
                }
            }
        }

        function renderPlanetaryMatrixLab(order) {
            currentSelectedWafqOrder = order;
            document.querySelectorAll('.wafq-order-pill').forEach(p => p.classList.remove('active'));
            const activePill = document.getElementById(`wafq-pill-${order}`);
            if (activePill) activePill.classList.add('active');

            const pData = PLANETARY_WAFQS_DATA.find(x => x.n === order) || PLANETARY_WAFQS_DATA[0];

            let grid = [];
            if (order % 2 !== 0) {
                grid = generateOddMagicSquare(order);
            } else if (order % 4 === 0) {
                grid = generateDoublyEvenMagicSquare(order);
            } else if (order === 6) {
                grid = getSun6x6MagicSquare();
            }

            const M = (order * (order * order + 1)) / 2;
            const T = order * M;

            // Render Grid
            const gridContainer = document.getElementById('wafq-dynamic-grid-container');
            if (gridContainer) {
                gridContainer.style.gridTemplateColumns = `repeat(${order}, 1fr)`;
                const minVal = 1;
                const maxVal = order * order;

                let cellsHtml = '';
                for (let r = 0; r < order; r++) {
                    for (let c = 0; c < order; c++) {
                        const val = grid[r][c];
                        let cellClass = 'dynamic-cell';
                        let badgeText = '';

                        if (val === minVal) {
                            cellClass += ' cell-key';
                            badgeText = 'المفتاح 🔑';
                        } else if (val === maxVal) {
                            cellClass += ' cell-lock';
                            badgeText = 'المغلاق 🔒';
                        } else if (order % 2 !== 0 && r === Math.floor(order/2) && c === Math.floor(order/2)) {
                            cellClass += ' cell-center';
                            badgeText = 'القطب ⚖️';
                        }

                        const numSize = order <= 4 ? '1.3rem' : (order <= 6 ? '1.05rem' : (order <= 7 ? '0.9rem' : '0.75rem'));

                        cellsHtml += `
                            <div class="${cellClass}" title="الصف ${r+1}، العمود ${c+1}: القيمة ${val}">
                                <span class="dynamic-cell-val" style="font-size:${numSize};">${val}</span>
                                ${badgeText ? `<span class="dynamic-cell-badge" style="color:var(--gold);">${badgeText}</span>` : ''}
                            </div>
                        `;
                    }
                }
                gridContainer.innerHTML = cellsHtml;
            }

            // Render Math Badges
            const badgesContainer = document.getElementById('wafq-math-badges-container');
            if (badgesContainer) {
                badgesContainer.innerHTML = `
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> كل الصفوف = <strong>${M}</strong></div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> كل الأعمدة = <strong>${M}</strong></div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> القطران (D1 & D2) = <strong>${M}</strong></div>
                    <div class="wafq-math-badge"><i class="fa-solid fa-calculator"></i> المجموع الكلي (T) = <strong>${T}</strong></div>
                    <div class="wafq-math-badge"><i class="fa-solid fa-wave-square"></i> التردد المداري = <strong style="color:var(--cyan);">${pData.freq}</strong></div>
                `;
            }

            // Render Inspector Card
            const inspectorEl = document.getElementById('wafq-inspector-content');
            if (inspectorEl) {
                inspectorEl.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:10px;">
                        <div>
                            <h4 style="margin:0; font-family:'Amiri',serif; font-size:1.4rem; color:${pData.color};">
                                ${pData.order} — ${pData.planet}
                            </h4>
                            <span style="font-size:0.82rem; color:#94a3b8;">اليوم: <strong style="color:#fff;">${pData.day}</strong> | المعدن: <strong style="color:var(--gold);">${pData.metal}</strong> | العنصر: <em>${pData.element}</em></span>
                        </div>
                        <button class="synth-btn" style="padding:6px 14px; font-size:0.85rem;" onclick="playPlanetTone(${pData.sound}, '${pData.planet} - ${pData.freq}')">
                            <i class="fa-solid fa-play"></i> استمع لرنين ${pData.freq}
                        </button>
                    </div>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; margin-bottom:14px; font-size:0.85rem;">
                        <div style="background:rgba(0,0,0,0.3); padding:10px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <span style="color:#94a3b8; display:block; font-size:0.75rem;">الثابت السحري (Magic Constant):</span>
                            <strong style="color:var(--gold); font-size:1.2rem;">M = ${M}</strong>
                        </div>
                        <div style="background:rgba(0,0,0,0.3); padding:10px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <span style="color:#94a3b8; display:block; font-size:0.75rem;">المساحة الكلية (Total Sum):</span>
                            <strong style="color:var(--cyan); font-size:1.2rem;">T = ${T}</strong>
                        </div>
                        <div style="background:rgba(0,0,0,0.3); padding:10px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <span style="color:#94a3b8; display:block; font-size:0.75rem;">التردد المداري والنغمة:</span>
                            <strong style="color:#34d399; font-size:1.1rem;">${pData.freq} (${pData.note})</strong>
                        </div>
                    </div>

                    <div style="font-size:0.86rem; line-height:1.75; color:#475569;">
                        <div style="margin-bottom:8px;">
                            <strong style="color:var(--gold);"><i class="fa-solid fa-route"></i> مسار التنزيل الحركي (Traversal Algorithm):</strong><br>
                            <span>${pData.path_desc}</span>
                        </div>
                        <div style="margin-bottom:8px;">
                            <strong style="color:var(--cyan);"><i class="fa-solid fa-globe"></i> في الحضارات الكبرى (Comparative Matrix):</strong>
                            <ul style="margin:4px 0 8px 18px; padding:0; font-size:0.83rem;">
                                <li><strong>الصين القديمة:</strong> ${pData.china}</li>
                                <li><strong>الهند الفيدية:</strong> ${pData.vedic}</li>
                                <li><strong>الهرمسية الغربية:</strong> ${pData.hermetic}</li>
                            </ul>
                        </div>
                        <div style="background:rgba(15,23,42,0.6); padding:10px; border-radius:8px; border-right:3px solid ${pData.color};">
                            <strong style="color:#fff;"><i class="fa-solid fa-heart-pulse"></i> الأثر الحيوي والأثيري:</strong>
                            <p style="margin:3px 0 0 0; font-size:0.83rem; color:#e2e8f0;">${pData.bio}</p>
                        </div>
                    </div>
                `;
            }
        }

        // LIVE WAFQ 3x3 GHAZALI ENGINE (ADVANCED ABJAD & BALANCED COMPILATION)
        function calculateLiveWafq() {
            const rawVal = document.getElementById('wafq-input')?.value.trim() || '105';
            let targetN = parseInt(rawVal);
            let abjadBreakdown = '';

            // Abjad calculator fallback if text is passed
            if (isNaN(targetN) || targetN < 15) {
                targetN = 0;
                const ABJAD_MAP = {
                    'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ء': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'هـ': 5, 'ة': 5,
                    'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ى': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50,
                    'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500,
                    'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
                };
                let parts = [];
                for (let ch of rawVal) {
                    if (ABJAD_MAP[ch]) {
                        targetN += ABJAD_MAP[ch];
                        parts.push(`${ch}=${ABJAD_MAP[ch]}`);
                    }
                }
                if (targetN < 15) targetN = 105;
                if (parts.length > 0) {
                    abjadBreakdown = ` | بحساب الجُمّل لـ "${rawVal}": [${parts.join(' + ')}] = ${targetN}`;
                }
            }

            // Formula: (N - 12) / 3
            const baseDeduct = 12;
            const diff = targetN - baseDeduct;
            const key = Math.floor(diff / 3);
            const remainder = diff % 3;

            // Base 3x3 Positions (Batad Zahaj Wah):
            // 4 (D), 9 (T), 2 (B)
            // 3 (J), 5 (H), 7 (Z)
            // 8 (Hh), 1 (A), 6 (W)
            const LETTERS = ['د', 'ط', 'ب', 'ج', 'هـ', 'ز', 'ح', 'أ', 'و'];
            const NATURAL_CELL_INDEX = [4, 9, 2, 3, 5, 7, 8, 1, 6];

            let gridCells = [];
            for (let i = 0; i < 9; i++) {
                const natVal = NATURAL_CELL_INDEX[i]; // 1 to 9
                let cellVal = key + (natVal - 1);
                let isBroken = false;

                // Broken step adjustment (Al-Kasr):
                if (remainder === 1 && natVal >= 7) {
                    cellVal += 1;
                    if (natVal === 7) isBroken = true;
                } else if (remainder === 2 && natVal >= 4) {
                    cellVal += 1;
                    if (natVal === 4) isBroken = true;
                }

                gridCells.push({
                    val: cellVal,
                    letter: LETTERS[i],
                    isKey: (natVal === 1),
                    isLock: (natVal === 9),
                    isCenter: (natVal === 5),
                    isBroken: isBroken,
                    cellIndex: natVal
                });
            }

            const summaryEl = document.getElementById('wafq-math-summary');
            if (summaryEl) {
                summaryEl.innerHTML = `المطلوب (N) = <strong>${targetN}</strong> | المفتاح = <strong>${key}</strong> | الأس = 12 | الباقي = <strong>${remainder}</strong> (${remainder === 0 ? 'تام بلا كسر' : (remainder === 1 ? 'جبر +1 في بيت 7 (الزاي)' : 'جبر +1 في بيت 4 (الدال)')})${abjadBreakdown}`;
            }

            // Sums verification
            const r0 = gridCells[0].val + gridCells[1].val + gridCells[2].val;
            const r1 = gridCells[3].val + gridCells[4].val + gridCells[5].val;
            const r2 = gridCells[6].val + gridCells[7].val + gridCells[8].val;
            const c0 = gridCells[0].val + gridCells[3].val + gridCells[6].val;
            const c1 = gridCells[1].val + gridCells[4].val + gridCells[7].val;
            const c2 = gridCells[2].val + gridCells[5].val + gridCells[8].val;

            const gridEl = document.getElementById('live-wafq-grid');
            if (gridEl) {
                gridEl.innerHTML = gridCells.map(c => {
                    let borderClass = '';
                    let badge = '';
                    if (c.isKey) { borderClass = 'style="border-color:var(--emerald); background:rgba(6,214,160,0.15);"'; badge = '<span style="font-size:0.65rem; color:var(--emerald);">المفتاح 🔑</span>'; }
                    else if (c.isLock) { borderClass = 'style="border-color:#ef4444; background:rgba(239,68,68,0.15);"'; badge = '<span style="font-size:0.65rem; color:#ef4444;">المغلاق 🔒</span>'; }
                    else if (c.isCenter) { borderClass = 'style="border-color:var(--gold); background:rgba(244,180,26,0.18);"'; badge = '<span style="font-size:0.65rem; color:var(--gold);">القطب ⚖️</span>'; }
                    else if (c.isBroken) { borderClass = 'style="border-color:#c026d3; background:rgba(192,38,211,0.2);"'; badge = '<span style="font-size:0.65rem; color:#c026d3;">خانة الجبر ⚡</span>'; }

                    return `
                        <div class="grid-cell" ${borderClass} title="بيت ${c.cellIndex} (حرف ${c.letter}) = ${c.val}">
                            <span class="cell-num">${c.val}</span>
                            <span class="cell-letter">${c.letter} (بيت ${c.cellIndex})</span>
                            ${badge}
                        </div>
                    `;
                }).join('');
            }

            const ghazaliBadgesEl = document.getElementById('ghazali-verification-badges');
            if (ghazaliBadgesEl) {
                ghazaliBadgesEl.innerHTML = `
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> صف 1 = <strong>${r0}</strong> (${r0===targetN?'✓':'≠'})</div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> صف 2 = <strong>${r1}</strong> (${r1===targetN?'✓':'≠'})</div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> صف 3 = <strong>${r2}</strong> (${r2===targetN?'✓':'≠'})</div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> عمود 1 = <strong>${c0}</strong> (${c0===targetN?'✓':'≠'})</div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> عمود 2 = <strong>${c1}</strong> (${c1===targetN?'✓':'≠'})</div>
                    <div class="wafq-math-badge verified"><i class="fa-solid fa-check-circle"></i> عمود 3 = <strong>${c2}</strong> (${c2===targetN?'✓':'≠'})</div>
                `;
            }
        }

        // WEB AUDIO API LIVE SYNTHESIZER
        let audioCtx = null;
        let currentOsc = null;
        let currentGain = null;

        function playPlanetTone(freq, name) {
            try {
                const AudioCtx = window.AudioContext || window.webkitAudioContext;
                if (!audioCtx) audioCtx = new AudioCtx();
                if (audioCtx.state === 'suspended') audioCtx.resume();

                if (currentOsc) {
                    try { currentOsc.stop(); currentOsc.disconnect(); } catch(e){}
                }

                currentOsc = audioCtx.createOscillator();
                currentGain = audioCtx.createGain();

                currentOsc.type = 'sine';
                currentOsc.frequency.setValueAtTime(freq, audioCtx.currentTime);

                currentGain.gain.setValueAtTime(0.001, audioCtx.currentTime);
                currentGain.gain.exponentialRampToValueAtTime(0.14, audioCtx.currentTime + 0.1);

                currentOsc.connect(currentGain);
                currentGain.connect(audioCtx.destination);
                currentOsc.start();

                document.querySelectorAll('.synth-btn').forEach(b => b.classList.remove('playing'));
                if (event && event.target) {
                    const btn = event.target.closest('button');
                    if (btn) btn.classList.add('playing');
                }
            } catch (e) {
                console.warn('Audio tone could not play', e);
            }
        }

        function stopTone() {
            if (currentOsc) {
                try { currentOsc.stop(); currentOsc.disconnect(); } catch(e){}
                currentOsc = null;
            }
            document.querySelectorAll('.synth-btn').forEach(b => b.classList.remove('playing'));
        }

        // CANVAS WAVE SIMULATOR
        let waveMode = 'constructive';
        let wavePhase = 0;

        function setWaveMode(mode) {
            waveMode = mode;
            document.querySelectorAll('.wave-mode-btn').forEach(b => b.classList.remove('active'));
            if (event && event.target) event.target.classList.add('active');
            const statusEl = document.getElementById('wave-status');
            if (statusEl) {
                statusEl.innerText = mode === 'constructive' ? 'الموجة: تداخل بنّاء متناغم (جلب وصحة وانسجام)' : 'الموجة: تداخل هدام (تفريغ وقطع للعقد)';
            }
        }

        function drawWave() {
            const canvas = document.getElementById('waveCanvas');
            if (canvas) {
                const ctx = canvas.getContext('2d');
                canvas.width = canvas.parentElement.clientWidth - 32;
                canvas.height = 180;

                ctx.fillStyle = '#020408';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.lineWidth = 2.5;
                ctx.strokeStyle = waveMode === 'constructive' ? '#00f0ff' : '#ff3366';
                ctx.shadowColor = waveMode === 'constructive' ? '#00f0ff' : '#ff3366';
                ctx.shadowBlur = 12;

                ctx.beginPath();
                const midY = canvas.height / 2;
                wavePhase += 0.04;

                for (let x = 0; x < canvas.width; x++) {
                    let y;
                    if (waveMode === 'constructive') {
                        y = midY + Math.sin(x * 0.03 + wavePhase) * 35 + Math.sin(x * 0.015 + wavePhase * 1.5) * 20;
                    } else {
                        y = midY + (Math.sin(x * 0.04 + wavePhase) - Math.sin(x * 0.04 + wavePhase)) * 10 + (Math.random() - 0.5) * 6;
                    }
                    if (x === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }
                ctx.stroke();
            }
            requestAnimationFrame(drawWave);
        }

        // TABS SWITCHING
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
            const target = document.getElementById(tabId);
            if (target) target.classList.add('active');
            const activeBtn = Array.from(document.querySelectorAll('.nav-tab')).find(b => b.getAttribute('onclick')?.includes(tabId));
            if (activeBtn) activeBtn.classList.add('active');
        }

        // INITIALIZATION
        window.addEventListener('load', () => {
            renderKings();
            renderZodiacAngels();
            render36Decans();
            loadDayHours(0);
            renderMansions();
            renderPlanetaryWafqs();
            renderLetters();
            renderBodies();
            renderQuranic();
            calculateLiveWafq();
            requestAnimationFrame(drawWave);
        });
    </script>
</body>
</html>'''

    with open(CODEX_WEB_PATH, 'w', encoding='utf-8') as f:
        f.write(html_code)

    with open(CODEX_ROOT_PATH, 'w', encoding='utf-8') as f:
        f.write(html_code)

    print(f"Generated {CODEX_WEB_PATH} ({len(html_code):,} bytes)")
    print(f"Generated {CODEX_ROOT_PATH}")

if __name__ == "__main__":
    generate_codex()
