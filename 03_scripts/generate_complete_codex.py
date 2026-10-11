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
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سفر النواميس الباطنية والأفلاك الكبرى — الموسوعة الأكاديمية الشاملة</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-void: #030508;
            --panel-bg: rgba(10, 14, 26, 0.94);
            --border-glass: rgba(255, 255, 255, 0.12);
            --text-main: #f0f6fc;
            --text-muted: #94a3b8;
            --gold: #f4b41a;
            --gold-glow: rgba(244, 180, 26, 0.35);
            --cyan: #00f0ff;
            --cyan-glow: rgba(0, 240, 255, 0.3);
            --rose: #ff3366;
            --purple: #9d4edd;
            --emerald: #06d6a0;
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
        }

        body {
            background-color: var(--bg-void);
            color: var(--text-main);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 15%, rgba(0, 240, 255, 0.04) 0%, transparent 40%),
                radial-gradient(circle at 90% 85%, rgba(244, 180, 26, 0.04) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(157, 78, 221, 0.03) 0%, transparent 50%);
            min-height: 100vh;
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
        td { padding: 12px 16px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); color: #cbd5e1; line-height: 1.6; }
        tr:hover td { background: rgba(255, 255, 255, 0.02); }

        .day-select-bar { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 12px; margin-bottom: 16px; }
        .day-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: #cbd5e1;
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

        /* Wafq Grid 3x3 */
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
            border: 1px solid rgba(255, 209, 102, 0.3);
            border-radius: 8px;
            height: 75px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        .grid-cell:hover { background: rgba(255, 209, 102, 0.15); border-color: var(--gold); }
        .cell-num { font-size: 1.35rem; font-weight: 800; color: #fff; line-height: 1; }
        .cell-letter { font-size: 0.75rem; color: var(--gold); margin-top: 4px; }

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
            color: #cbd5e1;
            padding: 6px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.8rem;
            font-weight: 700;
        }
        .wave-mode-btn.active { background: var(--emerald); color: #030508; border-color: var(--emerald); }

        /* Bodies & Quran Grid */
        .bodies-stack { display: flex; flex-direction: column; gap: 14px; }
        .body-layer {
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 14px;
            padding: 18px 24px;
            display: flex;
            align-items: center;
            gap: 20px;
            transition: all 0.25s;
        }
        .body-layer:hover { transform: translateX(-4px); border-color: var(--cyan); }
        .body-num { font-size: 1.8rem; font-weight: 800; color: var(--cyan); min-width: 45px; }

        .quranic-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 20px; }
        .quran-proof-card {
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-right: 4px solid var(--gold);
            border-radius: 14px;
            padding: 20px;
        }
        .quran-ayah-box { background: rgba(244, 180, 26, 0.08); border-radius: 10px; padding: 12px 16px; color: var(--gold); font-family: 'Amiri', serif; font-size: 1.15rem; margin-bottom: 12px; }

        @media (max-width: 768px) {
            header { flex-direction: column; gap: 12px; padding: 12px 16px; }
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
            <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(0,240,255,0.3); border-radius:16px; padding:20px; margin-bottom:20px; line-height:1.8; font-size:0.9rem; color:#cbd5e1;">
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
                <h2>🪶 ميزان الحروف الأربعة عند جابر بن حيان وتفكيك الأسحار فيزيائياً</h2>
                <p>علم الميزان الحرفي؛ تقسيم الحروف على الطبائع الأربعة (حرارة، برودة، رطوبة، يبوسة) بنسبة (1:3:5:8)، مستويات حساب الجمل الثلاثة (الكبير والصغير والأوسط)، والتشريح الفيزيائي الموجي لكيفية عمل أنواع السحر الأربعة وطريقة فك رنينها بالأمواج القرآنية المضادة:</p>
            </div>

            <!-- Jabir Science of Balance Box -->
            <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(255,209,102,0.3); border-radius:16px; padding:22px; margin-bottom:25px; line-height:1.8; font-size:0.9rem;">
                <h3 style="color:var(--gold); margin-bottom:10px; font-family:'Amiri',serif; font-size:1.3rem;"><i class="fa-solid fa-scale-unbalanced"></i> نظرية ميزان الحروف والطبائع لجابر بن حيان (Kitab al-Mizan):</h3>
                <p style="color:#cbd5e1; margin-bottom:10px;">
                    بيّن حكيم الكيمياء جابر بن حيان أن كل مادة وجرم في الكون مبني على توازن كمي لدرجات الطبائع الأربع. وحروف الاسم ليست مجرد أصوات، بل هي <strong>مؤشرات قياسية للمعاوقة الأثيرية</strong>؛ فإذا زادت الحروف النارية غلبت الحرارة واليبوسة (طبيعة النار)، وإذا كثرت الحروف الترابية حدث التكثف والثبات. حساب الجمل الكبير يعطي الطاقة الكلية (Total Energy Scalar)، والصغير يعطي زاوية الطور (Phase Modulus 1-9).
                </p>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-top:14px;">
                    <div style="background:rgba(0,0,0,0.4); padding:10px 14px; border-radius:10px; border-right:3px solid var(--gold);">
                        <strong style="color:var(--gold);">الجمل الكبير:</strong> الأبجدية كاملة من 1 إلى 1000 (ا=1، ك=20، ق=100، غ=1000).
                    </div>
                    <div style="background:rgba(0,0,0,0.4); padding:10px 14px; border-radius:10px; border-right:3px solid var(--cyan);">
                        <strong style="color:var(--cyan);">الجمل الصغير:</strong> إسقاط الأصفار لاختزال الحرف لمرتبة الآحاد (ا=1، ي=1، ق=1، غ=1).
                    </div>
                    <div style="background:rgba(0,0,0,0.4); padding:10px 14px; border-radius:10px; border-right:3px solid var(--purple);">
                        <strong style="color:var(--purple);">الجمل الأوسط:</strong> حساب بسط الحروف (حساب حروف اسم الحرف: أ ل ف = 1+30+80 = 111).
                    </div>
                </div>
            </div>

            <!-- 4 Elements Grid -->
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin-bottom:30px;">
                <div style="background:var(--panel-bg); border:1px solid var(--fire); border-radius:16px; padding:20px;">
                    <h3 style="color:var(--fire); margin-bottom:8px;"><i class="fa-solid fa-fire"></i> 1. الحروف النارية (أَهْطَمْفَشَذْ)</h3>
                    <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:12px;">الأحرف: <strong>أ (1) • هـ (5) • ط (9) • م (40) • ف (80) • ش (300) • ذ (700)</strong> — حار يابس</p>
                    <div style="font-size:0.84rem; line-height:1.7; color:#ffe5ec;">
                        <strong>السحر الناري (الكهرومغناطيسي الحراري):</strong> يعتمد على تسخين الأثر وحرقه؛ فيحدث اضطراباً في الهرمونات، خفقان القلب، الحميات غير المفسرة، ونوبات الغضب الحارق.<br>
                        <strong>العلاج المضاد:</strong> تبريد الأثر، الغسل بالماء البارد المقروء عليه آيات الإطفاء: ﴿قُلْنَا يَا نَارُ كُونِي بَرْدًا وَسَلَامًا عَلَىٰ إِبْرَاهِيمَ﴾، وتوليد نغمات الهدوء والسكينة.
                    </div>
                </div>

                <div style="background:var(--panel-bg); border:1px solid var(--air); border-radius:16px; padding:20px;">
                    <h3 style="color:var(--air); margin-bottom:8px;"><i class="fa-solid fa-wind"></i> 2. الحروف الهوائية (جَزْكَسَقَثَظْ)</h3>
                    <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:12px;">الأحرف: <strong>ج (3) • ز (7) • ك (20) • س (60) • ق (100) • ث (500) • ظ (900)</strong> — حار رطب</p>
                    <div style="font-size:0.84rem; line-height:1.7; color:#e0fbfc;">
                        <strong>السحر الهوائي (الموجات الصوتية والأثيرية):</strong> يُعلق في مهاب الرياح؛ كلما اهتز في مهب الرياح أحدث رنيناً تذبذبياً يسبب الصداع النصفي، الوسواس القهري، والشتات الفكري.<br>
                        <strong>العلاج المضاد:</strong> قطع الوتر الأثيري المعلق، الاستقرار وتثبيت الجسد بالأرض، وسماع الرقية بترددات هابطة تؤصل السكينة واليقين.
                    </div>
                </div>

                <div style="background:var(--panel-bg); border:1px solid var(--water); border-radius:16px; padding:20px;">
                    <h3 style="color:var(--water); margin-bottom:8px;"><i class="fa-solid fa-water"></i> 3. الحروف المائية (دَحْلَعَرَخَغْ)</h3>
                    <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:12px;">الأحرف: <strong>د (4) • ح (8) • ل (30) • ع (70) • ر (200) • خ (600) • غ (1000)</strong> — بارد رطب</p>
                    <div style="font-size:0.84rem; line-height:1.7; color:#dbeafe;">
                        <strong>السحر المائي (الرنين الهيدروجيني والذاكرة السائلة):</strong> يلقى في الآبار أو البحار أو يُشرب؛ يؤثر على سوائل الجسد والغدد، مسبباً الخمول، تبلد المشاعر، وبرودة الأطراف.<br>
                        <strong>العلاج المضاد:</strong> إعادة هيكلة جزيئات الماء الداخلي بالبسملة والقرآن (Hexagonal Water Structured)، والتسخين والتعرق لإخراج السموم الأثيرية.
                    </div>
                </div>

                <div style="background:var(--panel-bg); border:1px solid var(--earth); border-radius:16px; padding:20px;">
                    <h3 style="color:var(--earth); margin-bottom:8px;"><i class="fa-solid fa-mountain"></i> 4. الحروف الترابية (بَوْيَنَصْتَضْ)</h3>
                    <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:12px;">الأحرف: <strong>ب (2) • و (6) • ي (10) • ن (50) • ص (90) • ت (400) • ض (800)</strong> — بارد يابس</p>
                    <div style="font-size:0.84rem; line-height:1.7; color:#fef3c7;">
                        <strong>السحر الترابي (التثبيت المغناطيسي والدفائن):</strong> يدفن في القبور وتحت العتبات؛ يسبب ثقل العظام، آلام المفاصل والظهر، والتعطيل التام للحركة والرزق.<br>
                        <strong>العلاج المضاد:</strong> استخراج الدفين وفسخه بالملح والخل الصخري والماء المرقى، وقطع التأريض السلبي بنور التسبيح والأذكار الحية.
                    </div>
                </div>
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
                    <ul style="padding-right:18px; margin:8px 0; font-size:0.87rem; color:#cbd5e1; line-height:1.7;">
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
            <div class="toroid-interactive-container">
                <div class="toroid-svg-box">
                    <svg viewBox="0 0 500 500" id="toroid-svg">
                        <defs>
                            <radialGradient id="toroidCore" cx="50%" cy="50%" r="50%">
                                <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
                                <stop offset="25%" stop-color="#f4b41a" stop-opacity="0.8"/>
                                <stop offset="60%" stop-color="#00e5ff" stop-opacity="0.4"/>
                                <stop offset="100%" stop-color="#0a101a" stop-opacity="0"/>
                            </radialGradient>
                            <filter id="glowEffect" x="-50%" y="-50%" width="200%" height="200%">
                                <feGaussianBlur stdDeviation="6" result="blur" />
                                <feMerge>
                                    <feMergeNode in="blur" />
                                    <feMergeNode in="SourceGraphic" />
                                </feMerge>
                            </filter>
                        </defs>
                        <!-- Concentric Aura Layer Rings -->
                        <circle cx="250" cy="250" r="230" fill="none" stroke="#e0e7ff" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.3" class="toroid-ring"/>
                        <circle cx="250" cy="250" r="200" fill="none" stroke="#8b5cf6" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.4" class="toroid-ring"/>
                        <circle cx="250" cy="250" r="170" fill="none" stroke="#3b82f6" stroke-width="1.8" opacity="0.5" class="toroid-ring"/>
                        <circle cx="250" cy="250" r="140" fill="none" stroke="#06d6a0" stroke-width="2" opacity="0.6" class="toroid-ring"/>
                        <circle cx="250" cy="250" r="110" fill="none" stroke="#f4b41a" stroke-width="2" opacity="0.7" class="toroid-ring"/>
                        <circle cx="250" cy="250" r="80"  fill="none" stroke="#ff8c00" stroke-width="2.5" opacity="0.8" class="toroid-ring"/>
                        <circle cx="250" cy="250" r="50"  fill="none" stroke="#ef4444" stroke-width="3" opacity="0.9" class="toroid-ring"/>

                        <!-- Center Light Source & Human Avatar Silhouette -->
                        <circle cx="250" cy="250" r="30" fill="url(#toroidCore)" filter="url(#glowEffect)"/>
                        <path d="M250,225 C256,225 260,229 260,235 C260,241 256,245 250,245 C244,245 240,241 240,235 C240,229 244,225 250,225 Z M250,248 C258,248 266,252 268,262 L232,262 C234,252 242,248 250,248 Z M244,262 L244,278 L248,278 L248,262 Z M252,262 L252,278 L256,278 L256,262 Z" fill="#ffffff" opacity="0.9"/>

                        <!-- Interactive Layer Clickable Nodes -->
                        <!-- 1. Physical -->
                        <g class="toroid-node active" id="node-1" onclick="selectBodyLayer('1')">
                            <circle cx="250" cy="200" r="9" fill="#ef4444" stroke="#fff" stroke-width="2"/>
                            <text x="250" y="196" fill="#fff" font-size="9" text-anchor="middle" font-family="'Amiri',serif" dy="-4">1. الطيني</text>
                        </g>
                        <!-- 2. Etheric -->
                        <g class="toroid-node" id="node-2" onclick="selectBodyLayer('2')">
                            <circle cx="295" cy="210" r="9" fill="#ff8c00" stroke="#fff" stroke-width="2"/>
                            <text x="305" y="206" fill="#fff" font-size="9" text-anchor="start" font-family="'Amiri',serif" dy="-2">2. الأثيري</text>
                        </g>
                        <!-- 3. Astral -->
                        <g class="toroid-node" id="node-3" onclick="selectBodyLayer('3')">
                            <circle cx="330" cy="250" r="9" fill="#f4b41a" stroke="#fff" stroke-width="2"/>
                            <text x="342" y="254" fill="#fff" font-size="9" text-anchor="start" font-family="'Amiri',serif">3. النجمي</text>
                        </g>
                        <!-- 4. Mental -->
                        <g class="toroid-node" id="node-4" onclick="selectBodyLayer('4')">
                            <circle cx="295" cy="305" r="9" fill="#06d6a0" stroke="#fff" stroke-width="2"/>
                            <text x="305" y="316" fill="#fff" font-size="9" text-anchor="start" font-family="'Amiri',serif" dy="4">4. العقلي</text>
                        </g>
                        <!-- 5. Causal -->
                        <g class="toroid-node" id="node-5" onclick="selectBodyLayer('5')">
                            <circle cx="205" cy="305" r="9" fill="#3b82f6" stroke="#fff" stroke-width="2"/>
                            <text x="195" y="316" fill="#fff" font-size="9" text-anchor="end" font-family="'Amiri',serif" dy="4">5. السببي</text>
                        </g>
                        <!-- 6. Buddhic -->
                        <g class="toroid-node" id="node-6" onclick="selectBodyLayer('6')">
                            <circle cx="170" cy="250" r="9" fill="#8b5cf6" stroke="#fff" stroke-width="2"/>
                            <text x="158" y="254" fill="#fff" font-size="9" text-anchor="end" font-family="'Amiri',serif">6. البوذي</text>
                        </g>
                        <!-- 7. Atmic -->
                        <g class="toroid-node" id="node-7" onclick="selectBodyLayer('7')">
                            <circle cx="250" cy="20" r="10" fill="#e0e7ff" stroke="#fff" stroke-width="2"/>
                            <text x="250" y="14" fill="#fff" font-size="9" text-anchor="middle" font-family="'Amiri',serif">7. الإلهي الأسمى</text>
                        </g>
                    </svg>
                </div>

                <!-- Inspector Card for Clicked Layer -->
                <div class="body-detail-card" id="body-detail-card">
                    <!-- Populated dynamically by selectBodyLayer() -->
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
                <table style="width:100%; border-collapse:collapse; font-size:0.85rem; color:#cbd5e1; text-align:right;">
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
                <h2>🔢 شفرة الأوفاق السبعة الكوكبية (3×3 إلى 9×9) وحاسبة الغزالي الحية</h2>
                <p>الهندسة الرياضية للأوفاق السحرية كموجّهات موجية في الأثير، مصفوفة الأوفاق السبعة من مثلث زحل إلى متسع القمر بترددات هانس كوستو، وحاسبة وفق الغزالي 3×3 التفاعلية الحية لأي عدد أو اسم:</p>
            </div>

            <!-- INTERACTIVE WAFQ GENERATOR CALCULATOR -->
            <div style="background:linear-gradient(135deg, rgba(15,23,42,0.9), rgba(30,27,75,0.7)); border:1px solid rgba(255,209,102,0.3); border-radius:16px; padding:24px; margin-bottom:28px; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
                <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:12px;">
                    <div>
                        <h3 style="margin:0; font-family:'Amiri',serif; font-size:1.35rem; color:var(--gold); display:flex; align-items:center; gap:8px;">
                            <i class="fa-solid fa-calculator"></i> حاسبة ومولّد وفق الغزالي التفاعلي الحي (Live Wafq 3x3 Engine)
                        </h3>
                        <span style="font-size:0.8rem; color:#94a3b8;">أدخل أي عدد أو اسم لتوليد المثلث العددي المتوازن رياضياً فوراً مع رصد المفتاح والمغلق وخانة الجبر:</span>
                    </div>
                    <div style="display:flex; gap:8px;">
                        <input type="text" id="wafq-input" value="105" placeholder="أدخل عدداً أو اسماً (مثال: 105 أو آدم)" style="background:rgba(0,0,0,0.5); border:1px solid var(--gold); border-radius:8px; padding:8px 14px; color:#fff; font-family:'Tajawal',sans-serif; font-size:0.95rem; width:220px; text-align:center;">
                        <button onclick="calculateLiveWafq()" class="synth-btn" style="padding:8px 16px; font-weight:700;"><i class="fa-solid fa-wand-magic-sparkles"></i> توليد الوفق</button>
                    </div>
                </div>

                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; align-items:center;">
                    <!-- Visual Grid Output -->
                    <div>
                        <div style="text-align:center; font-size:0.85rem; color:#ffd166; margin-bottom:8px;" id="wafq-math-summary">
                            المطلوب (N) = <strong>105</strong> | المفتاح = <strong>31</strong> | الأس = 12 | الباقي = <strong>0</strong> (تام)
                        </div>
                        <div class="magic-grid-3x3" id="live-wafq-grid" style="max-width:320px; margin:0 auto;"></div>
                    </div>

                    <!-- Explanatory Panel -->
                    <div style="font-size:0.86rem; line-height:1.8; color:#cbd5e1; background:rgba(0,0,0,0.3); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                        <strong style="color:var(--gold);">قاعدة تعمير مثلث الغزالي الرياضية الصارمة:</strong><br>
                        1. <strong>المعادلة:</strong> (العدد المطلوب - 12) ÷ 3 = المفتاح.<br>
                        2. <strong>إذا كان الباقي 0:</strong> يعمر الوفق تتابعياً بالسير الطبيعي (1 إلى 9).<br>
                        3. <strong>إذا كان الباقي 1:</strong> يُجبر الوفق بزيادة 1 في البيت السابع (الزاي 7).<br>
                        4. <strong>إذا كان الباقي 2:</strong> يُجبر الوفق بزيادة 1 في البيت الرابع (الدال 4).<br>
                        كل صف، عمود، وقطر يعطي بدقة متناهية العدد المطلوب نفسه، مما يخلق توازناً هندسياً تاماً.
                    </div>
                </div>
            </div>

            <!-- Complete 7 Planetary Squares Compendium -->
            <div style="margin-bottom:25px;">
                <h3 style="color:#d8b4fe; font-family:'Amiri',serif; font-size:1.35rem; margin-bottom:12px;"><i class="fa-solid fa-cubes"></i> مصفوفة الأوفاق السبعة الكوكبية الكاملة من 3×3 إلى 9×9 وتردداتها المدارية</h3>
                <div class="data-table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>نوع الوفق ورتبته</th>
                                <th>الكوكب الفلكي</th>
                                <th>الثابت العددي (Row Sum)</th>
                                <th>المجموع الكلي (Total)</th>
                                <th>التردد المداري (Hans Cousto)</th>
                                <th>النغمة الموسيقية</th>
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

        // DATA: 7 Planetary Wafqs Compendium
        const PLANETARY_WAFQS_DATA = [
            { order: "المثلث (3×3)", planet: "زحل ♄", constant: 15, total: 45, freq: "147.85 Hz", note: "D (ري)", bio: "العظام، المفاصل، الصبر، وحفظ الحدود الكونية", sound: 147.85 },
            { order: "المربع (4×4)", planet: "المشتري ♃", constant: 34, total: 136, freq: "183.58 Hz", note: "F# (فا دييز)", bio: "الكبد، الشرايين، الوفرة المالية، وتوسيع الهالة", sound: 183.58 },
            { order: "المخمس (5×5)", planet: "المريخ ♂", constant: 65, total: 325, freq: "144.72 Hz", note: "D (ري)", bio: "الدم، المناعة الهجومية، الشجاعة، وقطع القيود", sound: 144.72 },
            { order: "المسدس (6×6)", planet: "الشمس ☉", constant: 111, total: 666, freq: "528 Hz", note: "C (دو / 528)", bio: "القلب، البصر، العزة، الشفاء الجسدي، وطرد الظلام", sound: 528 },
            { order: "المسبع (7×7)", planet: "الزهرة ♀", constant: 175, total: 1225, freq: "221.23 Hz", note: "A (لا)", bio: "الكلى، التناسل، الجاذبية، المحبة والتوافق العاطفي", sound: 221.23 },
            { order: "المثمن (8×8)", planet: "عطارد ☿", constant: 260, total: 2080, freq: "141.27 Hz", note: "C# (دو دييز)", bio: "الجهاز العصبي، الذكاء، البلاغة، وحل الشيفرات", sound: 141.27 },
            { order: "المتسع (9×9)", planet: "القمر ☽", constant: 369, total: 3321, freq: "210.42 Hz", note: "G# (صول دييز)", bio: "السوائل، الذاكرة، الدماغ، والأحلام والحدس الباطني", sound: 210.42 }
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
                color: "#3b82f6",
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
                color: "#e0e7ff",
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
                    <td><span style="color:#cbd5e1; font-weight:600;">${d.deg}</span></td>
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
                    <td style="font-size:0.8rem; color:#cbd5e1;"><strong>البخور:</strong> ${m.inc}<br><strong>التأثير:</strong> ${m.work}</td>
                </tr>
            `).join('');
        }

        function renderPlanetaryWafqs() {
            const tbody = document.getElementById('planetary-wafqs-tbody');
            if (!tbody) return;
            tbody.innerHTML = PLANETARY_WAFQS_DATA.map(w => `
                <tr>
                    <td><strong style="color:var(--gold); font-size:0.95rem;">${w.order}</strong></td>
                    <td><strong style="color:#fff;">${w.planet}</strong></td>
                    <td><span style="color:var(--cyan); font-weight:700; font-size:1rem;">${w.constant}</span></td>
                    <td><span style="color:#f472b6; font-weight:700;">${w.total}</span></td>
                    <td><code style="color:var(--gold); font-weight:700;">${w.freq}</code></td>
                    <td>${w.note}</td>
                    <td style="font-size:0.82rem; color:#cbd5e1;">${w.bio}</td>
                    <td><button class="synth-btn" style="padding:4px 10px; font-size:0.75rem;" onclick="playPlanetTone(${w.sound}, '${w.planet} - ${w.freq}')"><i class="fa-solid fa-play"></i> استماع</button></td>
                </tr>
            `).join('');
        }

        function selectBodyLayer(id) {
            const b = BODIES_DATA.find(x => x.num === id);
            if (!b) return;

            // Highlight node in SVG
            document.querySelectorAll('.toroid-node').forEach(node => {
                node.classList.remove('active');
            });
            const targetNode = document.getElementById('node-' + id);
            if (targetNode) targetNode.classList.add('active');

            // Render inspector card
            const card = document.getElementById('body-detail-card');
            if (card) {
                card.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
                        <div>
                            <span style="background:rgba(0,229,255,0.15); border:1px solid var(--cyan); color:var(--cyan); padding:3px 12px; border-radius:12px; font-size:0.75rem; font-weight:700;">الغلاف رقم ${b.num}</span>
                            <h3 style="color:#fff; font-family:'Amiri',serif; margin:8px 0 4px 0; font-size:1.35rem;">${b.name}</h3>
                            <div style="color:var(--gold); font-size:0.88rem; font-family:'Amiri',serif;">${b.nafs}</div>
                        </div>
                        <div style="text-align:left;">
                            <span style="background:${b.color}22; border:1px solid ${b.color}; color:${b.color}; padding:4px 10px; border-radius:8px; font-size:0.8rem; font-weight:700;">${b.dimension}</span>
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:0.82rem; margin-bottom:12px; background:rgba(0,0,0,0.25); padding:10px; border-radius:8px;">
                        <div><strong style="color:var(--cyan);">الشاكرا والمرجع:</strong> <span style="color:#cbd5e1;">${b.chakra}</span></div>
                        <div><strong style="color:var(--cyan);">السُمك والمدى:</strong> <span style="color:#cbd5e1;">${b.thickness}</span></div>
                        <div style="grid-column:span 2;"><strong style="color:var(--cyan);">التردد الحاكم:</strong> <span style="color:#cbd5e1;">${b.frequency}</span></div>
                    </div>
                    <p style="font-size:0.85rem; color:#cbd5e1; line-height:1.6; margin-bottom:12px;"><strong>الفيزياء الحيوية:</strong> ${b.physics}</p>
                    <div class="attack-vulnerability-box">
                        <strong style="color:#f87171; display:flex; align-items:center; gap:6px;">⚠️ آلية الاختراق والطفيليات:</strong>
                        <p style="font-size:0.82rem; color:#fca5a5; margin:6px 0 0 0; line-height:1.5;">${b.attack}</p>
                        <div style="font-size:0.8rem; color:#fecaca; margin-top:6px;"><strong>أعراض التمزق:</strong> ${b.symptoms}</div>
                    </div>
                    <div class="defense-protocol-box">
                        <strong style="color:#34d399; display:flex; align-items:center; gap:6px;">🛡️ الحصن النبوي والإغلاق:</strong>
                        <p style="font-size:0.82rem; color:#a7f3d0; margin:6px 0 0 0; line-height:1.5;">${b.defense}</p>
                        <div style="margin-top:8px; background:rgba(0,0,0,0.3); padding:8px; border-radius:6px; color:var(--gold); font-family:'Amiri',serif; font-size:0.9rem;">${b.quran_shield}</div>
                    </div>
                `;
            }

            // Highlight in stack
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
                                <h3 style="color:#fff; font-family:'Amiri',serif; font-size:1.25rem; margin:0 0 4px 0;">${b.name}</h3>
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

        function renderBodies() {
            filterBodies('all');
            selectBodyLayer('1');

            // Render Panoramic Table
            const tableBody = document.getElementById('panoramic-bodies-table');
            if (tableBody) {
                tableBody.innerHTML = BODIES_DATA.map((b, idx) => `
                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:${idx % 2 === 0 ? 'rgba(15,23,42,0.4)' : 'rgba(10,16,26,0.6)'};">
                        <td style="padding:10px; font-weight:bold; color:${b.color};">${b.num}</td>
                        <td style="padding:10px; font-weight:600; color:#fff;">${b.name}</td>
                        <td style="padding:10px; color:var(--gold); font-family:'Amiri',serif;">${b.nafs}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#94a3b8;">${b.frequency}</td>
                        <td style="padding:10px; font-size:0.8rem; color:#cbd5e1;">${b.thickness}</td>
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
                    <p style="font-size:0.86rem; color:#cbd5e1; line-height:1.7;">${q.analysis}</p>
                </div>
            `).join('');
        }

        // LIVE WAFQ 3x3 ENGINE
        function calculateLiveWafq() {
            const rawVal = document.getElementById('wafq-input')?.value.trim() || '105';
            let targetN = parseInt(rawVal);

            // Abjad calculator fallback if text is passed
            if (isNaN(targetN) || targetN < 15) {
                targetN = 0;
                const ABJAD_MAP = {
                    'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ء': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'هـ': 5, 'ة': 5,
                    'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ى': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50,
                    'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500,
                    'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
                };
                for (let ch of rawVal) {
                    if (ABJAD_MAP[ch]) targetN += ABJAD_MAP[ch];
                }
                if (targetN < 15) targetN = 105;
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
            const OFFSETS = [3, 8, 1, 2, 4, 6, 7, 0, 5]; // relative step increments

            let gridCells = [];
            for (let i = 0; i < 9; i++) {
                let cellVal = key + OFFSETS[i];
                // Broken step adjustment (Al-Kasr):
                if (remainder === 1 && OFFSETS[i] >= 6) {
                    cellVal += 1;
                } else if (remainder === 2 && OFFSETS[i] >= 3) {
                    cellVal += 1;
                }
                gridCells.push({ val: cellVal, letter: LETTERS[i] });
            }

            const summaryEl = document.getElementById('wafq-math-summary');
            if (summaryEl) {
                summaryEl.innerHTML = `المطلوب (N) = <strong>${targetN}</strong> | المفتاح = <strong>${key}</strong> | الأس = 12 | الباقي = <strong>${remainder}</strong> (${remainder === 0 ? 'تام' : (remainder === 1 ? 'جبر في بيت 7' : 'جبر في بيت 4')})`;
            }

            const gridEl = document.getElementById('live-wafq-grid');
            if (gridEl) {
                gridEl.innerHTML = gridCells.map(c => `
                    <div class="grid-cell">
                        <span class="cell-num">${c.val}</span>
                        <span class="cell-letter">${c.letter}</span>
                    </div>
                `).join('');
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
