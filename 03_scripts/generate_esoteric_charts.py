# -*- coding: utf-8 -*-
"""
Knowledge Lab - Grand Esoteric Visual Observatory & Charts Suite (جنة العلوم الباطنية)
Features 5 luxury interactive cosmic charts & visualizations:
1. رادار الأركان الخمسة للعلوم الباطنية (5-Axis Celestial Radar)
2. طيف الترددات الأثيرية والرنين الملكوتي مع مولد نغمات صوتي (Solfeggio & Planetary Spectrum)
3. مصفوفة الطبائع الأربعة وتوازن العناصر الكونية (Elemental Quad-Matrix Wheel)
4. شجرة اللطائف ومراكز النور السبعة (7 Lata'if & Energy Centers Interactive Conduit)
5. ميزان البرهان والتحقيق الإبستمولوجي (Epistemic Demarcation & Truth Gauge)
"""

def get_esoteric_charts_css():
    return """
    /* ========================================================
       GRAND ESOTERIC CHARTS SUITE (مرصد الرسوم البيانية الباطنية الفخمة)
       ======================================================== */
    .esoteric-observatory-wrapper {
        margin: 35px auto 45px auto;
        max-width: 1350px;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 60%, #edf2f7 100%);
        border: 2px solid var(--border-gold-strong);
        border-radius: 28px;
        padding: 30px 24px;
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08), 0 0 30px rgba(100, 116, 139, 0.12);
        position: relative;
        overflow: hidden;
    }

    .esoteric-observatory-wrapper::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 10% 20%, rgba(16, 185, 129, 0.04) 0%, transparent 40%),
                    radial-gradient(circle at 90% 15%, rgba(148, 163, 184, 0.06) 0%, transparent 45%),
                    radial-gradient(circle at 50% 85%, rgba(124, 58, 237, 0.04) 0%, transparent 50%);
        pointer-events: none;
    }

    .observatory-header {
        text-align: center;
        margin-bottom: 26px;
        position: relative;
        z-index: 2;
    }

    .observatory-tughra {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(135deg, rgba(148, 163, 184, 0.12), rgba(254, 240, 138, 0.25));
        border: 1px solid var(--border-gold);
        border-radius: 24px;
        padding: 5px 20px;
        color: var(--gold);
        font-family: 'Amiri', serif;
        font-size: 0.95rem;
        margin-bottom: 12px;
        box-shadow: 0 2px 10px rgba(100, 116, 139, 0.15);
    }

    .observatory-title {
        font-family: 'Amiri', serif;
        font-size: clamp(1.8rem, 3.8vw, 2.6rem);
        font-weight: 800;
        margin: 0 0 10px 0;
        color: #0f172a;
        line-height: 1.3;
    }

    .observatory-desc {
        font-size: 0.96rem;
        color: #334155;
        max-width: 820px;
        margin: 0 auto 22px auto;
        line-height: 1.7;
    }

    /* CHART NAVIGATION TABS */
    .observatory-nav-tabs {
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 28px;
        position: relative;
        z-index: 2;
    }

    .obs-tab-btn {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        color: #334155;
        border-radius: 14px;
        padding: 10px 18px;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.92rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
    }

    .obs-tab-btn:hover {
        background: #f8fafc;
        border-color: var(--gold);
        color: #0f172a;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(100, 116, 139, 0.15);
    }

    .obs-tab-btn.active {
        background: linear-gradient(135deg, var(--gold), #64748b);
        border-color: var(--gold);
        color: #ffffff;
        font-weight: 800;
        box-shadow: 0 2px 12px rgba(100, 116, 139, 0.3);
    }

    /* CHARTS CONTAINER */
    .observatory-panels-container {
        position: relative;
        z-index: 2;
        min-height: 480px;
    }

    .obs-chart-panel {
        display: none;
        animation: obsFadeIn 0.4s ease;
    }

    .obs-chart-panel.active {
        display: block;
    }

    @keyframes obsFadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* GRID LAYOUT FOR CHARTS: VISUAL + INSIGHTS */
    .obs-chart-grid {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 26px;
        align-items: center;
    }

    @media (max-width: 980px) {
        .obs-chart-grid {
            grid-template-columns: 1fr;
        }
    }

    .obs-visual-card {
        background: radial-gradient(circle at 50% 50%, #0d1527 0%, #090d16 65%, #030712 100%);
        border: 2px solid #475569;
        border-radius: 22px;
        padding: 24px;
        box-shadow: 0 16px 45px rgba(15, 23, 42, 0.25), 0 0 30px rgba(56, 189, 248, 0.15);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }

    .obs-info-card {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 22px;
        padding: 26px;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
        display: flex;
        flex-direction: column;
        gap: 16px;
    }

    .obs-info-title {
        font-family: 'Amiri', serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: #0f172a;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 1.5px solid #e2e8f0;
        padding-bottom: 12px;
    }

    .obs-metrics-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .obs-metric-item {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 10px 14px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.2s;
    }

    .obs-metric-item:hover {
        background: #edf2f7;
        border-color: var(--gold);
        transform: translateX(-4px);
    }

    .obs-metric-label {
        font-size: 0.9rem;
        color: #475569;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .obs-metric-value {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--emerald-accent);
    }

    /* RADAR CANVAS STYLES */
    #obsRadarCanvas {
        width: 100%;
        max-width: 440px;
        height: auto;
        aspect-ratio: 1 / 1;
        filter: drop-shadow(0 0 18px rgba(16, 185, 129, 0.35));
    }

    /* FREQUENCY HARMONIC BARS */
    .frequency-spectrum-container {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .freq-bar-item {
        background: rgba(13, 19, 38, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 10px 14px;
        display: flex;
        align-items: center;
        gap: 14px;
        cursor: pointer;
        transition: all 0.25s;
    }

    .freq-bar-item:hover, .freq-bar-item.playing {
        border-color: var(--gold-bright);
        background: rgba(148, 163, 184, 0.12);
        transform: scale(1.02);
        box-shadow: 0 4px 20px rgba(148, 163, 184, 0.25);
    }

    .freq-hz-badge {
        font-family: 'Amiri', serif;
        font-size: 1.1rem;
        font-weight: 800;
        min-width: 80px;
        color: var(--gold-bright);
        text-align: center;
        background: rgba(148, 163, 184, 0.15);
        border: 1px solid rgba(148, 163, 184, 0.3);
        padding: 4px 10px;
        border-radius: 8px;
    }

    .freq-progress-wrap {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    .freq-meta-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.85rem;
    }

    .freq-name {
        color: #f8fafc;
        font-weight: 700;
    }

    .freq-planet {
        color: #94a3b8;
    }

    .freq-progress-track {
        height: 8px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 6px;
        overflow: hidden;
        position: relative;
    }

    .freq-progress-fill {
        height: 100%;
        border-radius: 6px;
        transition: width 0.6s ease;
    }

    .freq-play-btn {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.4);
        color: var(--emerald-accent);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s;
        flex-shrink: 0;
    }

    .freq-bar-item:hover .freq-play-btn {
        background: var(--emerald-accent);
        color: #051410;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.6);
    }

    /* ELEMENTAL WHEEL STYLES */
    .elements-quad-wrapper {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
        width: 100%;
    }

    .element-card {
        border-radius: 18px;
        padding: 18px;
        display: flex;
        flex-direction: column;
        gap: 8px;
        cursor: pointer;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }

    .element-card:hover {
        transform: translateY(-4px);
    }

    .elem-fire {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.18), rgba(245, 158, 11, 0.1));
        border: 1px solid rgba(239, 68, 68, 0.4);
    }
    .elem-fire:hover {
        border-color: #ef4444;
        box-shadow: 0 8px 25px rgba(239, 68, 68, 0.35);
    }

    .elem-earth {
        background: linear-gradient(135deg, rgba(217, 119, 6, 0.18), rgba(180, 83, 9, 0.1));
        border: 1px solid rgba(217, 119, 6, 0.4);
    }
    .elem-earth:hover {
        border-color: #d97706;
        box-shadow: 0 8px 25px rgba(217, 119, 6, 0.35);
    }

    .elem-air {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.18), rgba(14, 165, 233, 0.1));
        border: 1px solid rgba(56, 189, 248, 0.4);
    }
    .elem-air:hover {
        border-color: #38bdf8;
        box-shadow: 0 8px 25px rgba(56, 189, 248, 0.35);
    }

    .elem-water {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.18), rgba(37, 99, 235, 0.1));
        border: 1px solid rgba(59, 130, 246, 0.4);
    }
    .elem-water:hover {
        border-color: #3b82f6;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.35);
    }

    .elem-icon-title {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Amiri', serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: #fff;
    }

    .elem-nature-badge {
        font-size: 0.76rem;
        padding: 2px 8px;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.1);
        color: #e2e8f0;
    }

    .elem-zodiacs {
        font-size: 0.85rem;
        color: #475569;
        line-height: 1.5;
    }

    /* 7 LATA'IF ENERGY CONDUIT */
    .lataif-conduit-wrapper {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 100%;
    }

    .lataif-node {
        display: flex;
        align-items: center;
        gap: 14px;
        background: rgba(13, 18, 36, 0.82);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 10px 16px;
        cursor: pointer;
        transition: all 0.25s;
    }

    .lataif-node:hover {
        transform: translateX(-6px);
        border-color: var(--gold);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
    }

    .lataif-rank-badge {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 0.88rem;
        flex-shrink: 0;
    }

    .lataif-meta {
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 8px;
    }

    .lataif-title {
        font-family: 'Amiri', serif;
        font-size: 1.12rem;
        font-weight: 700;
        color: #fff;
    }

    .lataif-station {
        font-size: 0.82rem;
        color: #94a3b8;
    }

    /* EPISTEMIC GAUGE STYLES */
    .epistemic-gauge-list {
        display: flex;
        flex-direction: column;
        gap: 16px;
        width: 100%;
    }

    .epistemic-gauge-card {
        background: rgba(11, 16, 32, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 14px 18px;
        display: flex;
        flex-direction: column;
        gap: 8px;
        transition: all 0.2s;
    }

    .epistemic-gauge-card:hover {
        border-color: var(--gold);
        transform: translateY(-2px);
    }

    .epistemic-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .epistemic-name {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: #f8fafc;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .epistemic-pct {
        font-family: 'Amiri', serif;
        font-size: 1.25rem;
        font-weight: 800;
    }

    .epistemic-bar-track {
        height: 10px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 6px;
        overflow: hidden;
    }

    .epistemic-bar-fill {
        height: 100%;
        border-radius: 6px;
        transition: width 1s ease-out;
    }

    .epistemic-desc {
        font-size: 0.84rem;
        color: #94a3b8;
        line-height: 1.5;
    }
    """

def get_esoteric_charts_html():
    return """
    <!-- 🌌 مرصد الرسوم البيانية الباطنية الفخمة (THE ESOTERIC VISUAL OBSERVATORY) -->
    <div class="esoteric-observatory-wrapper" id="esoteric-observatory">
        <div class="observatory-header">
            <div class="observatory-tughra">
                <span>✦</span>
                <span>مرصد النواميس الكونية والرسوم البيانية التفاعلية — جنة العلوم الباطنية</span>
                <span>✦</span>
            </div>
            <h2 class="observatory-title">مرصد المحاكاة والخرائط التفاعلية الكبرى</h2>
            <p class="observatory-desc">
                رسومات بيانية تفاعلية متطورة؛ تربط أوتار الترددات الأثيرية برادار العلوم الباطنية، ومصفوفة العناصر الأربعة بمراتب اللطائف وميزان التحقيق البرهاني الصارم.
            </p>

            <!-- 5 VISUAL OBSERVATORY NAVIGATION TABS -->
            <div class="observatory-nav-tabs">
                <button class="obs-tab-btn active" onclick="switchObservatoryChart('radar', this)">
                    <i class="fa-solid fa-compass-drafting"></i>
                    <span>رادار الأركان الخمسة</span>
                </button>
                <button class="obs-tab-btn" onclick="switchObservatoryChart('solfeggio', this)">
                    <i class="fa-solid fa-wave-square"></i>
                    <span>طيف الترددات والرنين (Solfeggio)</span>
                </button>
                <button class="obs-tab-btn" onclick="switchObservatoryChart('elements', this)">
                    <i class="fa-solid fa-shapes"></i>
                    <span>مصفوفة الطبائع الأربعة</span>
                </button>
                <button class="obs-tab-btn" onclick="switchObservatoryChart('lataif', this)">
                    <i class="fa-solid fa-dna"></i>
                    <span>شجرة اللطائف والمقامات الـ 7</span>
                </button>
                <button class="obs-tab-btn" onclick="switchObservatoryChart('epistemic', this)">
                    <i class="fa-solid fa-scale-balanced"></i>
                    <span>ميزان البرهان والتحقيق</span>
                </button>
            </div>
        </div>

        <div class="observatory-panels-container">
            <!-- PANEL 1: 5-AXIS RADAR -->
            <div class="obs-chart-panel active" id="obs-panel-radar">
                <div class="obs-chart-grid">
                    <div class="obs-visual-card">
                        <canvas id="obsRadarCanvas" width="440" height="440"></canvas>
                        <div style="font-size:0.8rem; color:#94a3b8; margin-top:12px; display:flex; gap:16px;">
                            <span><i class="fa-solid fa-circle" style="color:#10b981; font-size:0.6rem;"></i> الثقل المعرفي الموثق</span>
                            <span><i class="fa-solid fa-circle" style="color:#38bdf8; font-size:0.6rem;"></i> شبكة التوافق والتناظر</span>
                        </div>
                    </div>
                    <div class="obs-info-card">
                        <h3 class="obs-info-title">
                            <i class="fa-solid fa-shield-cat" style="color:var(--emerald-accent);"></i>
                            <span>توزيع الثقل الباطني عبر الأركان الخمسة</span>
                        </h3>
                        <p style="font-size:0.88rem; color:#475569; line-height:1.6; margin:0;">
                            رادار إحصائي تحليلي يقيس تكامل الأركان المعرفية بالموسوعة؛ يبرهن أن كل رمز فلكي أو حرفي له جذر كوزمولوجي ونواة نقدية تحميه من الشعوذة.
                        </p>
                        <div class="obs-metrics-list">
                            <div class="obs-metric-item" onclick="highlightRadarAxis(0)" style="cursor:pointer;">
                                <span class="obs-metric-label">📜 1. كوزمولوجيا التنزيل وعوالم الملكوت</span>
                                <span class="obs-metric-value" style="color:#38bdf8;">98% يقين</span>
                            </div>
                            <div class="obs-metric-item" onclick="highlightRadarAxis(1)" style="cursor:pointer;">
                                <span class="obs-metric-label">🪐 2. الفلك المداري والمنازل الـ 28</span>
                                <span class="obs-metric-value" style="color:#38bdf8;">94% دقة</span>
                            </div>
                            <div class="obs-metric-item" onclick="highlightRadarAxis(2)" style="cursor:pointer;">
                                <span class="obs-metric-label">🔢 3. أسرار الحروف والجمل والأوفاق</span>
                                <span class="obs-metric-value" style="color:#f59e0b;">91% تناظر</span>
                            </div>
                            <div class="obs-metric-item" onclick="highlightRadarAxis(3)" style="cursor:pointer;">
                                <span class="obs-metric-label">⚡ 4. فيزياء الأثير والترددات والاهتزاز</span>
                                <span class="obs-metric-value" style="color:#c084fc;">88% توافق</span>
                            </div>
                            <div class="obs-metric-item" onclick="highlightRadarAxis(4)" style="cursor:pointer;">
                                <span class="obs-metric-label">🧘 5. مراتب الوعي ومقامات الروح</span>
                                <span class="obs-metric-value" style="color:#10b981;">95% إشراق</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PANEL 2: SOLFEGGIO & PLANETARY FREQUENCIES -->
            <div class="obs-chart-panel" id="obs-panel-solfeggio">
                <div class="obs-chart-grid">
                    <div class="obs-visual-card">
                        <div class="frequency-spectrum-container">
                            <!-- 174 Hz -->
                            <div class="freq-bar-item" onclick="playHarmonicTone(174, this)">
                                <div class="freq-hz-badge">174 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name">نغمة التأسيس والأمان الحيوي</span>
                                        <span class="freq-planet">زحل / الجذر الكوني</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 25%; background: linear-gradient(90deg, #64748b, #94a3b8);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة"><i class="fa-solid fa-play"></i></button>
                            </div>

                            <!-- 285 Hz -->
                            <div class="freq-bar-item" onclick="playHarmonicTone(285, this)">
                                <div class="freq-hz-badge">285 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name">حقل الترميم والتجدد الأثيري</span>
                                        <span class="freq-planet">المشتري / التمدد</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 38%; background: linear-gradient(90deg, #d97706, #f59e0b);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة"><i class="fa-solid fa-play"></i></button>
                            </div>

                            <!-- 396 Hz -->
                            <div class="freq-bar-item" onclick="playHarmonicTone(396, this)">
                                <div class="freq-hz-badge">396 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name">فك القيود وتحرير الخوف والعقد</span>
                                        <span class="freq-planet">المريخ / القوة الدافعة</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 50%; background: linear-gradient(90deg, #ef4444, #f87171);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة"><i class="fa-solid fa-play"></i></button>
                            </div>

                            <!-- 528 Hz (MASTER) -->
                            <div class="freq-bar-item playing" onclick="playHarmonicTone(528, this)" style="border-color:var(--gold-bright);">
                                <div class="freq-hz-badge" style="background:var(--gold); color:#070a14;">528 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name" style="color:var(--gold-bright); font-weight:800;">تردد التحول المعجز والشفاء وهندسة الـ DNA</span>
                                        <span class="freq-planet" style="color:var(--gold-light);">الشمس / الذهب الأثيري</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 72%; background: linear-gradient(90deg, #38bdf8, #10b981);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة" style="background:var(--gold); color:#070a14;"><i class="fa-solid fa-play"></i></button>
                            </div>

                            <!-- 639 Hz -->
                            <div class="freq-bar-item" onclick="playHarmonicTone(639, this)">
                                <div class="freq-hz-badge">639 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name">تناغم القلوب والانسجام الروحي</span>
                                        <span class="freq-planet">الزهرة / الجمال والمحبة</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 82%; background: linear-gradient(90deg, #ec4899, #f472b6);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة"><i class="fa-solid fa-play"></i></button>
                            </div>

                            <!-- 741 Hz -->
                            <div class="freq-bar-item" onclick="playHarmonicTone(741, this)">
                                <div class="freq-hz-badge">741 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name">إيقاظ الحدس والتعبير الصافي الحكيم</span>
                                        <span class="freq-planet">عطارد / الكلمة والبيان</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 90%; background: linear-gradient(90deg, #06b6d4, #22d3ee);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة"><i class="fa-solid fa-play"></i></button>
                            </div>

                            <!-- 963 Hz -->
                            <div class="freq-bar-item" onclick="playHarmonicTone(963, this)">
                                <div class="freq-hz-badge">963 Hz</div>
                                <div class="freq-progress-wrap">
                                    <div class="freq-meta-row">
                                        <span class="freq-name">نور الاتصال بالعرش والوعي الأسمى</span>
                                        <span class="freq-planet">القمر المكتمل / المرآة الصافية</span>
                                    </div>
                                    <div class="freq-progress-track">
                                        <div class="freq-progress-fill" style="width: 100%; background: linear-gradient(90deg, #a855f7, #c084fc);"></div>
                                    </div>
                                </div>
                                <button class="freq-play-btn" title="استمع للنغمة"><i class="fa-solid fa-play"></i></button>
                            </div>
                        </div>
                    </div>

                    <div class="obs-info-card">
                        <h3 class="obs-info-title">
                            <i class="fa-solid fa-music" style="color:var(--gold-bright);"></i>
                            <span id="solfeggio-detail-title">تردد الذهب والتحول (528 Hz)</span>
                        </h3>
                        <div id="solfeggio-detail-box" style="display:flex; flex-direction:column; gap:12px; font-size:0.88rem; color:#475569; line-height:1.7;">
                            <p>
                                <strong>الرنين الفيزيائي:</strong> 528 هرتز يُعرف في علم الصوتيات الكونية بتردد الميراكل (تردد المعجزة)، وهو الطنين الرياضي المتطابق مع هندسة الكلوروفيل في النباتات وشبكة بلورات الماء المزدوج.
                            </p>
                            <p>
                                <strong>التناظر الباطني:</strong> يرتبط بكوكب الشمس، ومعدن الذهب الخالص، ومقام القلب النوراني، ويقابله في منظومة المقامات الروحية حالة "السكينة والطمأنينة".
                            </p>
                            <div style="background:rgba(148, 163, 184,0.1); border:1px solid rgba(148, 163, 184,0.3); border-radius:12px; padding:12px;">
                                💡 <strong>تجربة تفاعلية:</strong> اضغط على أي نغمة لسماع ذبذبتها النقية المولدة مباشرة عبر Web Audio API في متصفحك!
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PANEL 3: 4 ELEMENTS QUAD MATRIX -->
            <div class="obs-chart-panel" id="obs-panel-elements">
                <div class="obs-chart-grid">
                    <div class="obs-visual-card">
                        <div class="elements-quad-wrapper">
                            <!-- FIRE -->
                            <div class="element-card elem-fire" onclick="showElementDetail('fire')">
                                <div class="elem-icon-title">
                                    <span style="font-size:1.8rem;">🔥</span>
                                    <span>عنصر النار</span>
                                    <span class="elem-nature-badge">حار يابس</span>
                                </div>
                                <div class="elem-zodiacs">
                                    <strong>الأبراج:</strong> الحمل ♈، الأسد ♌، القوس ♐<br>
                                    <strong>الخلط:</strong> الصفراء | <strong>الاتجاه:</strong> الجنوب
                                </div>
                            </div>

                            <!-- EARTH -->
                            <div class="element-card elem-earth" onclick="showElementDetail('earth')">
                                <div class="elem-icon-title">
                                    <span style="font-size:1.8rem;">⛰️</span>
                                    <span>عنصر التراب</span>
                                    <span class="elem-nature-badge">بارد يابس</span>
                                </div>
                                <div class="elem-zodiacs">
                                    <strong>الأبراج:</strong> الثور ♉، العذراء ♍، الجدي ♑<br>
                                    <strong>الخلط:</strong> السوداء | <strong>الاتجاه:</strong> الشمال
                                </div>
                            </div>

                            <!-- AIR -->
                            <div class="element-card elem-air" onclick="showElementDetail('air')">
                                <div class="elem-icon-title">
                                    <span style="font-size:1.8rem;">💨</span>
                                    <span>عنصر الهواء</span>
                                    <span class="elem-nature-badge">حار رطب</span>
                                </div>
                                <div class="elem-zodiacs">
                                    <strong>الأبراج:</strong> الجوزاء ♊، الميزان ♎، الدلو ♒<br>
                                    <strong>الخلط:</strong> الدم | <strong>الاتجاه:</strong> الشرق
                                </div>
                            </div>

                            <!-- WATER -->
                            <div class="element-card elem-water" onclick="showElementDetail('water')">
                                <div class="elem-icon-title">
                                    <span style="font-size:1.8rem;">💧</span>
                                    <span>عنصر الماء</span>
                                    <span class="elem-nature-badge">بارد رطب</span>
                                </div>
                                <div class="elem-zodiacs">
                                    <strong>الأبراج:</strong> السرطان ♋، العقرب ♏، الحوت ♓<br>
                                    <strong>الخلط:</strong> البلغم | <strong>الاتجاه:</strong> الغرب
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="obs-info-card">
                        <h3 class="obs-info-title">
                            <i class="fa-solid fa-circle-nodes" style="color:#38bdf8;"></i>
                            <span id="elem-detail-title">هندسة الطبائع الأربعة والامتزاج الكوني</span>
                        </h3>
                        <div id="elem-detail-body" style="font-size:0.88rem; color:#475569; line-height:1.7; display:flex; flex-direction:column; gap:10px;">
                            <p>
                                يمثل التناظر الرباعي (نار، تراب، هواء، ماء) الأساس الرياضي للكيمياء القديمة والطب الأبقراطي والميلوثيسيا الهرمسية؛ حيث تتولد المواليد الثلاثة (جماد، نبات، حيوان) من تصارع وتكامل هذه الطبائع تحت إشراف الأفلاك السبعة.
                            </p>
                            <p>
                                <strong>المبدأ الباطني:</strong> التوازن التام بين الحرارة والبرودة والرطوبة واليبوسة هو سر اعتدال المزاج البشري والنقاء الروحي.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PANEL 4: 7 LATA'IF & CHAKRAS -->
            <div class="obs-chart-panel" id="obs-panel-lataif">
                <div class="obs-chart-grid">
                    <div class="obs-visual-card">
                        <div class="lataif-conduit-wrapper">
                            <div class="lataif-node" onclick="showLataifDetail(7)" style="border-right: 4px solid #c084fc;">
                                <div class="lataif-rank-badge" style="background:#c084fc; color:#070a14;">7</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة الأخفى (التاج النوراني)</span>
                                    <span class="lataif-station">فوق اليافوخ | سر الألوهية والفناء في الحق</span>
                                </div>
                            </div>
                            <div class="lataif-node" onclick="showLataifDetail(6)" style="border-right: 4px solid #38bdf8;">
                                <div class="lataif-rank-badge" style="background:#38bdf8; color:#070a14;">6</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة الخفي (العين الثالثة / البصيرة)</span>
                                    <span class="lataif-station">بين الحاجبين | كشف المكنونات والرؤيا الصادقة</span>
                                </div>
                            </div>
                            <div class="lataif-node" onclick="showLataifDetail(5)" style="border-right: 4px solid #22d3ee;">
                                <div class="lataif-rank-badge" style="background:#22d3ee; color:#070a14;">5</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة الروح (الحنجرة والبيان)</span>
                                    <span class="lataif-station">الحلق والصدر الأيمن | فيض الحكمة ونطق الحق</span>
                                </div>
                            </div>
                            <div class="lataif-node" onclick="showLataifDetail(4)" style="border-right: 4px solid #10b981;">
                                <div class="lataif-rank-badge" style="background:#10b981; color:#070a14;">4</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة السر والقلب (عرش الوعي)</span>
                                    <span class="lataif-station">الصدر الأيسر | مهبط التجليات ومستقر الإيمان</span>
                                </div>
                            </div>
                            <div class="lataif-node" onclick="showLataifDetail(3)" style="border-right: 4px solid #fbbf24;">
                                <div class="lataif-rank-badge" style="background:#fbbf24; color:#070a14;">3</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة النفس النامية (الضفيرة الشمسية)</span>
                                    <span class="lataif-station">أعلى السرة | إرادة التصريف والإقدام</span>
                                </div>
                            </div>
                            <div class="lataif-node" onclick="showLataifDetail(2)" style="border-right: 4px solid #f97316;">
                                <div class="lataif-rank-badge" style="background:#f97316; color:#070a14;">2</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة النفس الحيوانية (العجز والميلاد)</span>
                                    <span class="lataif-station">أسفل السرة | قوة التكاثر والنشأة الحيوية</span>
                                </div>
                            </div>
                            <div class="lataif-node" onclick="showLataifDetail(1)" style="border-right: 4px solid #ef4444;">
                                <div class="lataif-rank-badge" style="background:#ef4444; color:#070a14;">1</div>
                                <div class="lataif-meta">
                                    <span class="lataif-title">لطيفة القالب والطين (الجذر والأرض)</span>
                                    <span class="lataif-station">العصعص والقاعدة | الصلة بالطبيعة والرسوخ البدني</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="obs-info-card">
                        <h3 class="obs-info-title">
                            <i class="fa-solid fa-person-rays" style="color:var(--emerald-accent);"></i>
                            <span id="lataif-detail-title">التشريح الروحي والمراكز النورانية السبعة</span>
                        </h3>
                        <div id="lataif-detail-body" style="font-size:0.88rem; color:#475569; line-height:1.7; display:flex; flex-direction:column; gap:10px;">
                            <p>
                                يجمع التصوف الإشراقي والتحقيق الهرمسي على أن الإنسان "عالم صغير" (Microcosm) تنطوي فيه العوالم الكبرى السبعة؛ فكل مركز طاقي يقابل فلكاً سماوياً، وتردداً صوتياً، ومعدناً أرضياً.
                            </p>
                            <p>
                                <strong>سر الارتقاء:</strong> يبدأ السالك بتطهير مراكز الطين والنفس حتى يفتح مراكز القلب والسر ليفيض عليه نور الأخفى دون حجاب.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PANEL 5: EPISTEMIC BALANCE -->
            <div class="obs-chart-panel" id="obs-panel-epistemic">
                <div class="obs-chart-grid">
                    <div class="obs-visual-card">
                        <div class="epistemic-gauge-list">
                            <!-- 1. QURAN & SUNNAH -->
                            <div class="epistemic-gauge-card">
                                <div class="epistemic-header">
                                    <span class="epistemic-name">📖 محكم الوحي والتنزيل (القرآن والسنة الثابتة)</span>
                                    <span class="epistemic-pct" style="color:#38bdf8;">100% قطعي اليقين</span>
                                </div>
                                <div class="epistemic-bar-track">
                                    <div class="epistemic-bar-fill" style="width: 100%; background: linear-gradient(90deg, #38bdf8, #10b981);"></div>
                                </div>
                                <span class="epistemic-desc">الأصل الحاكم والمهيمن؛ كل ما عارضه من تنجيم أو أساطير فهو باطل مدحوض.</span>
                            </div>

                            <!-- 2. ASTRONOMY & MATH -->
                            <div class="epistemic-gauge-card">
                                <div class="epistemic-header">
                                    <span class="epistemic-name">🔭 الرصد الفلكي والرياضيات (البيروني وابن الشاطر)</span>
                                    <span class="epistemic-pct" style="color:#38bdf8;">94% دقة حسية</span>
                                </div>
                                <div class="epistemic-bar-track">
                                    <div class="epistemic-bar-fill" style="width: 94%; background: linear-gradient(90deg, #0284c7, #38bdf8);"></div>
                                </div>
                                <span class="epistemic-desc">حسابات مدارات الكواكب، منازل القمر، وخسوف وكسوف مبنية على سنن الله الكونية.</span>
                            </div>

                            <!-- 3. ISHRAQI PHILOSOPHY -->
                            <div class="epistemic-gauge-card">
                                <div class="epistemic-header">
                                    <span class="epistemic-name">🕯️ التأويل الإشراقي والرمزي (السهروردي وابن عربي)</span>
                                    <span class="epistemic-pct" style="color:#a855f7;">75% اعتبار واستئناس</span>
                                </div>
                                <div class="epistemic-bar-track">
                                    <div class="epistemic-bar-fill" style="width: 75%; background: linear-gradient(90deg, #7c3aed, #c084fc);"></div>
                                </div>
                                <span class="epistemic-desc">إشارات ومقامات ذوقية تخضع لشرط مطابقة الشريعة وعدم مخالفة نصوص الوحي.</span>
                            </div>

                            <!-- 4. ANCIENT HERMETIC -->
                            <div class="epistemic-gauge-card">
                                <div class="epistemic-header">
                                    <span class="epistemic-name">📜 الموروث الكلداني والهرمسي القديم</span>
                                    <span class="epistemic-pct" style="color:#f59e0b;">45% يحتاج تمحيصاً</span>
                                </div>
                                <div class="epistemic-bar-track">
                                    <div class="epistemic-bar-fill" style="width: 45%; background: linear-gradient(90deg, #b45309, #fbbf24);"></div>
                                </div>
                                <span class="epistemic-desc">شظايا حكمة قديمة اختلطت بالأساطير، يلزم عزل الذهب فيها عن ركام الشركيات.</span>
                            </div>

                            <!-- 5. CHARLATANRY -->
                            <div class="epistemic-gauge-card">
                                <div class="epistemic-header">
                                    <span class="epistemic-name">☠️ الشعوذة والسحر ودعوى علم الغيب</span>
                                    <span class="epistemic-pct" style="color:#ef4444;">0% باطل ومحرم</span>
                                </div>
                                <div class="epistemic-bar-track">
                                    <div class="epistemic-bar-fill" style="width: 0%; background: #ef4444;"></div>
                                </div>
                                <span class="epistemic-desc">استخدام الجان، الطلاسم الشركية، وادعاء الغيب المطلق باطل منهي عنه شرعاً وعقلاً.</span>
                            </div>
                        </div>
                    </div>

                    <div class="obs-info-card">
                        <h3 class="obs-info-title">
                            <i class="fa-solid fa-scale-unbalanced-flip" style="color:#38bdf8;"></i>
                            <span>معيار الحصانة المعرفية ونفي الدجل</span>
                        </h3>
                        <p style="font-size:0.88rem; color:#475569; line-height:1.7; margin:0;">
                            تعتمد الموسوعة ميزاناً معرفياً لا يساوم: الوحي هو القطب الثابت، والعلوم الطبيعية هي سنن التسخير، والرموز الباطنية ليست إلا مرايا لفهم النفس، مما يضمن للقارئ إبحاراً آمناً لا تشوبه خرافة.
                        </p>
                        <div style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); border-radius:12px; padding:12px; font-size:0.84rem; color:#a7f3d0;">
                            ✨ <strong>قاعدة المحققين:</strong> "كل باطن لا يشهد له ظاهر محكم فهو زندقة، وكل ظاهر لا عمق له فهو قشر جاف."
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

def get_esoteric_charts_js():
    return """
    /* ========================================================
       GRAND ESOTERIC CHARTS SUITE JAVASCRIPT LOGIC
       ======================================================== */
    let audioCtxInstance = null;
    let activeOscillator = null;
    let activeGainNode = null;

    function getAudioCtx() {
        if (!audioCtxInstance) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (AudioContextClass) {
                audioCtxInstance = new AudioContextClass();
            }
        }
        if (audioCtxInstance && audioCtxInstance.state === 'suspended') {
            audioCtxInstance.resume();
        }
        return audioCtxInstance;
    }

    function switchObservatoryChart(chartType, btnElem) {
        document.querySelectorAll('.obs-tab-btn').forEach(b => b.classList.remove('active'));
        if (btnElem) btnElem.classList.add('active');

        document.querySelectorAll('.obs-chart-panel').forEach(p => p.classList.remove('active'));
        const targetPanel = document.getElementById('obs-panel-' + chartType);
        if (targetPanel) {
            targetPanel.classList.add('active');
            if (chartType === 'radar') {
                drawRadarChart();
            }
        }
    }

    /* RADAR CANVAS RENDERER */
    function drawRadarChart(highlightIdx = -1) {
        const canvas = document.getElementById('obsRadarCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const dpr = window.devicePixelRatio || 1;
        const width = 440;
        const height = 440;

        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.scale(dpr, dpr);

        const centerX = width / 2;
        const centerY = height / 2;
        const radius = 160;
        const sides = 5;
        const angleStep = (Math.PI * 2) / sides;

        const labels = [
            "كوزمولوجيا التنزيل",
            "الفلك والمنازل",
            "الأوفاق والحروف",
            "فيزياء الأثير",
            "مراتب الوعي"
        ];
        const values = [0.98, 0.94, 0.91, 0.88, 0.95];

        ctx.clearRect(0, 0, width, height);

        // Concentric webs
        for (let level = 1; level <= 5; level++) {
            const r = (radius / 5) * level;
            ctx.beginPath();
            for (let i = 0; i < sides; i++) {
                const angle = i * angleStep - Math.PI / 2;
                const x = centerX + Math.cos(angle) * r;
                const y = centerY + Math.sin(angle) * r;
                if (i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.closePath();
            ctx.strokeStyle = level === 5 ? 'rgba(148, 163, 184, 0.4)' : 'rgba(255, 255, 255, 0.08)';
            ctx.lineWidth = 1;
            ctx.stroke();
        }

        // Radial axis lines
        for (let i = 0; i < sides; i++) {
            const angle = i * angleStep - Math.PI / 2;
            const x = centerX + Math.cos(angle) * radius;
            const y = centerY + Math.sin(angle) * radius;
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(x, y);
            ctx.strokeStyle = (i === highlightIdx) ? '#38bdf8' : 'rgba(148, 163, 184, 0.25)';
            ctx.lineWidth = (i === highlightIdx) ? 2 : 1;
            ctx.stroke();

            // Labels
            const lx = centerX + Math.cos(angle) * (radius + 24);
            const ly = centerY + Math.sin(angle) * (radius + 24);
            ctx.font = (i === highlightIdx) ? 'bold 13px Tajawal, sans-serif' : '11px Tajawal, sans-serif';
            ctx.fillStyle = (i === highlightIdx) ? '#38bdf8' : '#ffffff';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(labels[i], lx, ly);
        }

        // Polygon area
        ctx.beginPath();
        for (let i = 0; i < sides; i++) {
            const angle = i * angleStep - Math.PI / 2;
            const r = radius * values[i];
            const x = centerX + Math.cos(angle) * r;
            const y = centerY + Math.sin(angle) * r;
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.closePath();
        const grad = ctx.createRadialGradient(centerX, centerY, 10, centerX, centerY, radius);
        grad.addColorStop(0, 'rgba(16, 185, 129, 0.45)');
        grad.addColorStop(0.7, 'rgba(148, 163, 184, 0.35)');
        grad.addColorStop(1, 'rgba(168, 85, 247, 0.25)');
        ctx.fillStyle = grad;
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Data points
        for (let i = 0; i < sides; i++) {
            const angle = i * angleStep - Math.PI / 2;
            const r = radius * values[i];
            const x = centerX + Math.cos(angle) * r;
            const y = centerY + Math.sin(angle) * r;

            ctx.beginPath();
            ctx.arc(x, y, (i === highlightIdx) ? 7 : 4.5, 0, Math.PI * 2);
            ctx.fillStyle = (i === highlightIdx) ? '#38bdf8' : '#10b981';
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 1.5;
            ctx.stroke();
        }
    }

    function highlightRadarAxis(idx) {
        drawRadarChart(idx);
    }

    /* HARMONIC AUDIO PLAYER WITH WEB AUDIO API */
    function playHarmonicTone(hz, barElem) {
        try {
            const ctx = getAudioCtx();
            if (!ctx) return;

            // Stop previous tone
            if (activeOscillator) {
                try {
                    activeOscillator.stop();
                    activeOscillator.disconnect();
                } catch(e) {}
                activeOscillator = null;
            }

            document.querySelectorAll('.freq-bar-item').forEach(b => b.classList.remove('playing'));

            if (barElem) {
                barElem.classList.add('playing');
            }

            // Create sweet harmonic chime tone
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(hz, ctx.currentTime);

            // Gentle attack and decay envelope
            gain.gain.setValueAtTime(0.001, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.25, ctx.currentTime + 0.15);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 3.2);

            osc.connect(gain);
            gain.connect(ctx.destination);

            osc.start();
            osc.stop(ctx.currentTime + 3.3);
            activeOscillator = osc;

            // Update detail card
            const titleElem = document.getElementById('solfeggio-detail-title');
            const boxElem = document.getElementById('solfeggio-detail-box');
            if (titleElem && boxElem) {
                const descriptions = {
                    174: { title: "نغمة التأسيس الحيوي (174 Hz)", text: "تردد التسكين الطبيعي وإزالة التوتر الجسدي، مرتبط بالاستقرار في الأرض ومعدن الرصاص وفلك زحل." },
                    285: { title: "حقل التجدد الخلوي (285 Hz)", text: "يرتبط بتحفيز حقول الطاقة وتجديد الهالة الأثيرية وتوازن فلك المشتري ومعدن القصدير." },
                    396: { title: "فك القيود والعقد (396 Hz)", text: "تردد الاهتزاز المسؤول عن تبديد الخوف والذنب الباطني، متناظر مع نار المريخ ومعدن الحديد." },
                    528: { title: "تردد التحول والشفاء والذهب (528 Hz)", text: "تردد المعجزات الكوني، متطابق مع رنين أشعة الشمس وهندسة نمو النباتات وشفاء الشيفرة الوراثية." },
                    639: { title: "تناغم القلوب والمحبة (639 Hz)", text: "تردد الاتصال الوجداني وإصلاح العلاقات وفتح مسارات المحبة، متصل بالزهرة ومعدن النحاس." },
                    741: { title: "إيقاظ الحدس والبيان (741 Hz)", text: "تردد التعبير الصافي وحل المعضلات الفكرية، متناظر مع فلك عطارد والزئبق الأثيري." },
                    963: { title: "نور الاتصال بالعرش والأخفى (963 Hz)", text: "تردد الصفاء المطلق وإيقاظ الوعي التاجي والسكينة الروحية، متناظر مع فضة القمر الصافية." }
                };
                if (descriptions[hz]) {
                    titleElem.textContent = descriptions[hz].title;
                    boxElem.innerHTML = `<p>${descriptions[hz].text}</p><p style="color:var(--gold);">🔊 جاري تشغيل التردد الصافي (${hz} Hz)...</p>`;
                }
            }
        } catch(err) {
            console.warn("Audio Context note:", err);
        }
    }

    function showElementDetail(type) {
        const titleElem = document.getElementById('elem-detail-title');
        const bodyElem = document.getElementById('elem-detail-body');
        if (!titleElem || !bodyElem) return;

        const data = {
            fire: {
                title: "🔥 عنصر النار (الحرارة واليبوسة)",
                text: "النار هي المبدأ الصاعد والمحرك الأساسي للحياة؛ تمنح الجرأة، الإقدام، والقدرة على التحويل والتطهير. في الأبدان تمثل الصفراء وحرارة الهضم، وفي الفلك تقودها مثلثات (الحمل، الأسد، القوس)."
            },
            earth: {
                title: "⛰️ عنصر التراب (البرودة واليبوسة)",
                text: "التراب هو مبدأ الرسوخ، التماسك، وبناء الهياكل الفيزيائية. يمنح الصبر، الثبات، والقدرة على التحمل. في الأبدان يمثل السوداء والعظام، وفي الفلك تقوده مثلثات (الثور، العذراء، الجدي)."
            },
            air: {
                title: "💨 عنصر الهواء (الحرارة والرطوبة)",
                text: "الهواء هو مبدأ الانتشار، الاتصال، والتفاعل العقلي؛ ينقل الأنفاس والصوت، ويصل بين الثوابت والمتغيرات. في الأبدان يمثل الدم، وفي الفلك تقوده مثلثات (الجوزاء، الميزان، الدلو)."
            },
            water: {
                title: "💧 عنصر الماء (البرودة والرطوبة)",
                text: "الماء هو أصل الحياة ﴿وَجَعَلْنَا مِنَ الْمَاءِ كُلَّ شَيْءٍ حَيٍّ﴾؛ يمثل اللدونة، الامتزاج، والفيض العاطفي والحدسي. في الأبدان يمثل البلغم والسوائل الحيوية، وفي الفلك تقوده مثلثات (السرطان، العقرب، الحوت)."
            }
        };

        if (data[type]) {
            titleElem.textContent = data[type].title;
            bodyElem.innerHTML = `<p>${data[type].text}</p>`;
        }
    }

    function showLataifDetail(level) {
        const titleElem = document.getElementById('lataif-detail-title');
        const bodyElem = document.getElementById('lataif-detail-body');
        if (!titleElem || !bodyElem) return;

        const data = {
            7: { title: "👑 لطيفة الأخفى (مركز التاج النوراني)", text: "مقام الفناء في شهود التوحيد، ونور الاتصال المباشر بالفيض الإلهي والعرش؛ لونه بنفسجي/أبيض ناصع، وتردده 963 هرتز." },
            6: { title: "👁️ لطيفة الخفي (البصيرة والعين الثالثة)", text: "مقر الكشف الروحي واستشراف الحقائق وراء حجب المادة؛ لونه نيلي كحلي، وتردده 852 هرتز." },
            5: { title: "🗣️ لطيفة الروح (مركز البيان والحنجرة)", text: "مقر نطق الصدق والحكمة وفيض الكلمة الطيبة؛ لونه أزرق سماوي، وتردده 741 هرتز." },
            4: { title: "💚 لطيفة السر والقلب (عرش الصدر)", text: "مستقر الإيمان والسكينة ونور الحب الإلهي، أصل الاعتدال في الإنسان؛ لونه زمردي أخضر/ذهبي، وتردده 528 هرتز." },
            3: { title: "☀️ لطيفة النفس النامية (الضفيرة الشمسية)", text: "مستقر العزيمة والنشاط وقوة الإرادة الذاتية؛ لونه أصفر ذهبي، وتردده 417 هرتز." },
            2: { title: "🌊 لطيفة النفس الحيوية (مركز العجز والنشأة)", text: "مقر الحوافز والدافعية الفطرية للحياة؛ لونه برتقالي وهاج، وتردده 285 هرتز." },
            1: { title: "🌍 لطيفة القالب والطين (مركز الجذر)", text: "صلة الروح بالأرض وثبات الجسد المادي في عالم الحس؛ لونه قرمزي ياقوتي، وتردده 174 هرتز." }
        };

        if (data[level]) {
            titleElem.textContent = data[level].title;
            bodyElem.innerHTML = `<p>${data[level].text}</p>`;
        }
    }

    // Auto-draw radar on initial load
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(drawRadarChart, 600);
    });
    """
