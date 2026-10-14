# -*- coding: utf-8 -*-
"""
Knowledge Lab - Ancient Astrolabe & Engraved Celestial Mandalas Engine
Generates interactive antique astrolabes, rotating engraved celestial circles,
and gilded illuminated parchment folios with rich calligraphy and geometric alignments.
"""

def get_astrolabe_css():
    return """
    /* ========================================================
       ANCIENT ASTROLABE & ENGRAVED CELESTIAL MANDALA ENGINE
       محرك الأسطرلاب الفلكي الأثري والألواح البردية المذهبة
       ======================================================== */

    /* The Master Astrolabe Instrument Container */
    .astrolabe-instrument-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 32px;
        padding: 30px 20px;
        background: radial-gradient(circle at 50% 50%, #ffffff 0%, #f1f5f9 100%);
        border: 2px solid var(--border-gold-strong);
        border-radius: 28px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08), inset 0 0 40px rgba(180, 138, 40, 0.06);
        margin: 28px auto 40px auto;
        max-width: 1300px;
        position: relative;
        overflow: hidden;
    }

    .astrolabe-dial-box {
        position: relative;
        width: 380px;
        height: 380px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Rotating Astrolabe Rings */
    .astrolabe-outer-limb {
        position: absolute;
        inset: 0;
        border: 3px solid #d4af37;
        border-radius: 50%;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.4), inset 0 0 25px rgba(212, 175, 55, 0.2);
        background: radial-gradient(circle, #ffffff 0%, #f1f5f9 100%);
        animation: astrolabeRotateSlow 160s linear infinite;
        cursor: grab;
    }

    .astrolabe-outer-limb:active {
        cursor: grabbing;
    }

    .astrolabe-rete-ring {
        position: absolute;
        inset: 28px;
        border: 1.5px dashed rgba(212, 175, 55, 0.5);
        border-radius: 50%;
        animation: astrolabeRotateReverse 100s linear infinite;
        pointer-events: none;
    }

    .astrolabe-zodiac-ring {
        position: absolute;
        inset: 56px;
        border: 1px solid rgba(0, 240, 255, 0.4);
        border-radius: 50%;
        animation: astrolabeRotateSlow 80s linear infinite;
        pointer-events: none;
    }

    .astrolabe-alidade-pointer {
        position: absolute;
        width: 4px;
        height: 340px;
        background: linear-gradient(180deg, transparent 0%, #ffd700 20%, #d4af37 50%, #ffd700 80%, transparent 100%);
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.7);
        border-radius: 4px;
        pointer-events: none;
        transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        z-index: 10;
    }

    .astrolabe-center-boss {
        position: absolute;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: radial-gradient(circle, #fef08a 0%, #d4af37 60%, #937322 100%);
        border: 2px solid #ffd700;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #02040a;
        font-size: 1.2rem;
        z-index: 20;
        user-select: none;
    }

    @keyframes astrolabeRotateSlow {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    @keyframes astrolabeRotateReverse {
        from { transform: rotate(360deg); }
        to { transform: rotate(0deg); }
    }

    /* Interactive Gilded Parchment Folio (لوح البردي المذهب التفاعلي) */
    .gilded-parchment-display {
        flex-grow: 1;
        background: #ffffff;
        border: 1.5px solid var(--border-gold-strong);
        border-radius: 20px;
        padding: 26px 28px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06), inset 0 0 25px rgba(180, 138, 40, 0.05);
        position: relative;
        min-width: 320px;
    }

    .gilded-parchment-display::before {
        content: '';
        position: absolute;
        top: 6px; right: 6px; bottom: 6px; left: 6px;
        border: 1px dashed rgba(212, 175, 55, 0.3);
        border-radius: 16px;
        pointer-events: none;
    }

    .parchment-head-strip {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 16px;
        padding-bottom: 12px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.25);
    }

    .parchment-tughra-title {
        font-family: 'Amiri', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #967117;
        margin: 0;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
    }

    .parchment-celestial-badge {
        background: rgba(212, 175, 55, 0.15);
        border: 1px solid var(--border-gold);
        border-radius: 14px;
        padding: 4px 12px;
        color: var(--gold);
        font-family: 'Amiri', serif;
        font-size: 0.9rem;
    }

    .parchment-body-text {
        font-size: 0.95rem;
        color: #334155;
        line-height: 1.85;
        margin-bottom: 20px;
        font-family: 'Tajawal', sans-serif;
    }

    .parchment-attributes-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 12px;
        margin-bottom: 20px;
    }

    .parchment-attr-pill {
        background: #f8fafc;
        border: 1px solid rgba(203, 213, 225, 0.8);
        border-radius: 10px;
        padding: 10px 12px;
        text-align: center;
    }

    .parchment-attr-lbl {
        font-size: 0.75rem;
        color: #94a3b8;
        margin-bottom: 4px;
    }

    .parchment-attr-val {
        font-family: 'Amiri', serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--gold-bright);
    }

    .parchment-action-btn {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.25), rgba(212, 175, 55, 0.08));
        border: 1.5px solid var(--border-gold);
        border-radius: 12px;
        padding: 10px 20px;
        color: #967117;
        font-family: 'Tajawal', sans-serif;
        font-size: 0.9rem;
        font-weight: 700;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        transition: all 0.25s;
    }

    .parchment-action-btn:hover {
        background: var(--gold);
        color: #02040a;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
        transform: translateY(-2px);
    }

    @media (max-width: 900px) {
        .astrolabe-instrument-wrapper {
            flex-direction: column;
            padding: 20px 16px;
        }
        .astrolabe-dial-box {
            width: 280px;
            height: 280px;
        }
        .astrolabe-alidade-pointer {
            height: 250px;
        }
    }
    """

def get_astrolabe_html():
    return """
    <!-- INTERACTIVE ANCIENT ASTROLABE & GILDED PARCHMENT INSTRUMENT -->
    <div class="astrolabe-instrument-wrapper">
        <!-- SVG CELESTIAL ASTROLABE DIAL -->
        <div class="astrolabe-dial-box" id="astrolabe-dial-box" title="انقر أو اسحب لتدوير الأسطرلاب الفلكي">
            <!-- OUTER ENGRAVED LIMB -->
            <svg class="astrolabe-outer-limb" viewBox="0 0 400 400">
                <circle cx="200" cy="200" r="192" fill="none" stroke="rgba(212,175,55,0.8)" stroke-width="3"/>
                <circle cx="200" cy="200" r="182" fill="none" stroke="rgba(212,175,55,0.4)" stroke-width="1" stroke-dasharray="2,4"/>
                <circle cx="200" cy="200" r="162" fill="none" stroke="rgba(212,175,55,0.5)" stroke-width="1.5"/>
                <!-- Degree graduations (360 degrees markings) -->
                <g stroke="rgba(212,175,55,0.6)" stroke-width="1.5">
                    <line x1="200" y1="8" x2="200" y2="22"/>
                    <line x1="200" y1="378" x2="200" y2="392"/>
                    <line x1="8" y1="200" x2="22" y2="200"/>
                    <line x1="378" y1="200" x2="392" y2="200"/>
                    <!-- Diagonal markings -->
                    <line x1="64" y1="64" x2="74" y2="74"/>
                    <line x1="336" y1="64" x2="326" y2="74"/>
                    <line x1="64" y1="336" x2="74" y2="326"/>
                    <line x1="336" y1="336" x2="326" y2="326"/>
                </g>
                <!-- Arabic Numerals & Astrological Seals -->
                <text x="200" y="32" fill="#ffd700" font-family="Amiri" font-size="12" text-anchor="middle" font-weight="bold">زحل ♄</text>
                <text x="368" y="204" fill="#ffd700" font-family="Amiri" font-size="12" text-anchor="middle" font-weight="bold">الشمس ☉</text>
                <text x="200" y="380" fill="#ffd700" font-family="Amiri" font-size="12" text-anchor="middle" font-weight="bold">القمر ☽</text>
                <text x="32" y="204" fill="#ffd700" font-family="Amiri" font-size="12" text-anchor="middle" font-weight="bold">المشتري ♃</text>
            </svg>

            <!-- RETE & ALMUCANTARS (شبكة السمت والعنكبوت الفلكي) -->
            <svg class="astrolabe-rete-ring" viewBox="0 0 340 340">
                <!-- Concentric coordinate spheres -->
                <circle cx="170" cy="170" r="140" fill="none" stroke="rgba(212,175,55,0.3)" stroke-width="1"/>
                <circle cx="170" cy="170" r="100" fill="none" stroke="rgba(0,240,255,0.35)" stroke-width="1"/>
                <circle cx="170" cy="170" r="60" fill="none" stroke="rgba(168,85,247,0.35)" stroke-width="1"/>
                <!-- Eccentric Zodiac Circle (فلك البروج المائل) -->
                <circle cx="170" cy="140" r="75" fill="none" stroke="#d4af37" stroke-width="2" stroke-dasharray="6,3"/>
                <!-- Star Pointers (شظايا الكواكب الثابتة) -->
                <polygon points="170,15 174,30 166,30" fill="#ffd700"/>
                <polygon points="315,140 300,144 300,136" fill="#00f0ff"/>
                <polygon points="170,290 166,275 174,275" fill="#f472b6"/>
                <polygon points="25,140 40,136 40,144" fill="#10b981"/>
            </svg>

            <!-- ZODIAC SYMBOLS RING -->
            <div class="astrolabe-zodiac-ring"></div>

            <!-- ROTATABLE ALIDADE POINTER -->
            <div id="astrolabe-alidade-pointer" class="astrolabe-alidade-pointer"></div>

            <!-- CENTER BOSS / PIVOT PIN -->
            <div class="astrolabe-center-boss" onclick="spinAstrolabeRandomly()" title="تدوير الأسطرلاب الفلكي">
                <span>۞</span>
            </div>
        </div>

        <!-- ILLUMINATED GILDED PARCHMENT FOLIO (لوح البردي المذهب) -->
        <div class="gilded-parchment-display" id="gilded-parchment-display">
            <div class="parchment-head-strip">
                <div>
                    <h3 class="parchment-tughra-title" id="parchment-title">فلك الشمس ☉ — قلب الوجود وإدريس عليه السلام</h3>
                    <span style="font-size:0.82rem; color:#94a3b8;">السماء الرابعة • معدن الذهب الخالص • شاكرة القلب</span>
                </div>
                <span class="parchment-celestial-badge" id="parchment-badge">مرتبة المركز الحيوي</span>
            </div>

            <p class="parchment-body-text" id="parchment-desc">
                تتوسط الشمس الأفلاك السبعة كما يتوسط القلب أعضاء الجسد والروح؛ مقام نبي الله إدريس (هرمس الهرامسة) 
                المرفوع مكاناً علياً، صاحب أول قلم وخياط ثياب المعرفة، ومستودع النور المحض والتردد الشفائي الكوني.
            </p>

            <div class="parchment-attributes-grid" id="parchment-attrs">
                <div class="parchment-attr-pill">
                    <div class="parchment-attr-lbl">الكوكب واليوم</div>
                    <div class="parchment-attr-val" id="attr-planet">الشمس ☉ (الأحد)</div>
                </div>
                <div class="parchment-attr-pill">
                    <div class="parchment-attr-lbl">الملك الروحاني</div>
                    <div class="parchment-attr-val" id="attr-angel">روقيائيل</div>
                </div>
                <div class="parchment-attr-pill">
                    <div class="parchment-attr-lbl">التردد المداري</div>
                    <div class="parchment-attr-val" id="attr-freq">126.22 Hz (B)</div>
                </div>
                <div class="parchment-attr-pill">
                    <div class="parchment-attr-lbl">الوفق الهندسي</div>
                    <div class="parchment-attr-val" id="attr-wafq">المسدس 6×6 (111)</div>
                </div>
            </div>

            <div style="display:flex; gap:12px; flex-wrap:wrap;">
                <button class="parchment-action-btn" id="parchment-nav-btn" onclick="navigateToChamber('tab-spheres')">
                    <i class="fa-solid fa-compass"></i>
                    <span id="parchment-btn-label">دخول سلم الأفلاك وعرش الرحمن</span>
                </button>
                <button class="parchment-action-btn" onclick="spinAstrolabeRandomly()" style="background:rgba(255,255,255,0.06); border-color:rgba(255,255,255,0.15); color:#cbd5e1;">
                    <i class="fa-solid fa-arrows-rotate"></i>
                    <span>إدارة الأسطرلاب لفلك آخر</span>
                </button>
            </div>
        </div>
    </div>
    """

def get_astrolabe_js():
    return """
    // ========================================================
    // ASTROLABE INTERACTIVE CONTROLLER & ROTATION LOGIC
    // ========================================================
    const ASTROLABE_FOLIOS = [
        {
            title: 'فلك زحل ♄ — سماء إبراهيم عليه السلام',
            sub: 'السماء السابعة • معدن الرصاص • شاكرة التاج',
            badge: 'البيت المعمور والتوحيد الصرف',
            desc: 'فلك الزمان والحدود القصوى، مسند ظهره إلى البيت المعمور؛ مقام خليل الرحمن الذي حطم أصنام الكواكب وأعلن التنزيه الأبدي: «لَا أُحِبُّ الْآفِلِينَ». يحكم يوم السبت ومربعه الرياضي المثلث 3×3.',
            planet: 'زحل ♄ (السبت)',
            angel: 'كسفيائيل',
            freq: '147.85 Hz (D)',
            wafq: 'المثلث 3×3 (15)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء زحل وعرش الرحمن',
            angle: 0
        },
        {
            title: 'فلك المشتري ♃ — سماء موسى عليه السلام',
            sub: 'السماء السادسة • معدن القصدير • شاكرة البصيرة',
            badge: 'الحكمة والتشريع الجلالي',
            desc: 'فلك العدل والفيض الواسع والتشريع الإلهي؛ مقام كليم الله موسى صاحب العصا الفالقة للبحر وألواح التوراة، الحاكم ليوم الخميس ومربعه الرياضي المربع 4×4.',
            planet: 'المشتري ♃ (الخميس)',
            angel: 'صرفيائيل',
            freq: '183.58 Hz (F#)',
            wafq: 'المربع 4×4 (34)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء المشتري والألواح',
            angle: 51
        },
        {
            title: 'فلك المريخ ♂ — سماء هارون عليه السلام',
            sub: 'السماء الخامسة • معدن الحديد • شاكرة الحنجرة',
            badge: 'السيف والبيان التنفيذي',
            desc: 'فلك القوة التنفيذية والحرارة؛ مقام هارون الوزير المؤيد، حامل قوة البيان والمنعة التي حفظت أمة التوحيد. يحكم يوم الثلاثاء ومربعه الرياضي المخمس 5×5.',
            planet: 'المريخ ♂ (الثلاثاء)',
            angel: 'سمسمائيل',
            freq: '144.72 Hz (D)',
            wafq: 'المخمس 5×5 (65)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء المريخ والقوة',
            angle: 102
        },
        {
            title: 'فلك الشمس ☉ — سماء إدريس عليه السلام',
            sub: 'السماء الرابعة • معدن الذهب • شاكرة القلب',
            badge: 'قلب الأفلاك والنور المحض',
            desc: 'المركز الحيوي لنظام الأفلاك؛ مقام هرمس الهرامسة المرفوع مكاناً علياً، أول من خط بالقلم ونظر في حركة النجوم والحساب. يحكم يوم الأحد ومربعه المسدس 6×6.',
            planet: 'الشمس ☉ (الأحد)',
            angel: 'روقيائيل',
            freq: '126.22 Hz (B)',
            wafq: 'المسدس 6×6 (111)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء الشمس وإدريس',
            angle: 154
        },
        {
            title: 'فلك الزهرة ♀ — سماء يوسف عليه السلام',
            sub: 'السماء الثالثة • معدن النحاس • شاكرة الضفيرة',
            badge: 'الجمال المطلق وتأويل الرؤى',
            desc: 'فلك التناغم الحسابي والجمال الهندسي؛ مقام يوسف الصديق الذي أوتي شطر الحسن وحكمة تأويل الدورات السبع. يحكم يوم الجمعة ومربعه المسبع 7×7.',
            planet: 'الزهرة ♀ (الجمعة)',
            angel: 'عنيائيل',
            freq: '221.23 Hz (A)',
            wafq: 'المسبع 7×7 (175)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء الزهرة والتأويل',
            angle: 205
        },
        {
            title: 'فلك عطارد ☿ — سماء عيسى ويحيى عليهما السلام',
            sub: 'السماء الثانية • معدن الزئبق • شاكرة العجز',
            badge: 'الكلمة الروحية والتطهر',
            desc: 'فلك الذكاء والاتصال والروح الكلمية التي تحيي الموتى بإذن الله وتخترق القوانين المادية الصرفة. يحكم يوم الأربعاء ومربعه المثمن 8×8.',
            planet: 'عطارد ☿ (الأربعاء)',
            angel: 'ميكائيل',
            freq: '141.27 Hz (C#)',
            wafq: 'المثمن 8×8 (260)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء عطارد والكلمة',
            angle: 257
        },
        {
            title: 'فلك القمر ☽ — سماء آدم عليه السلام',
            sub: 'السماء الأولى • معدن الفضة • شاكرة الجذر',
            badge: 'عالم التجسد والأسماء الكلية',
            desc: 'سماء الدنيا ومجمع الطينات؛ مقام آدم أبو البشر الحامل للأسماء الكلية «وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا»، وبرزخ هبوط الروح إلى المادة. يحكم يوم الإثنين ومربعه المتسع 9×9.',
            planet: 'القمر ☽ (الإثنين)',
            angel: 'جبرائيل',
            freq: '210.42 Hz (G#)',
            wafq: 'المتسع 9×9 (369)',
            chamber: 'tab-spheres',
            btnText: 'دخول سماء القمر والأسماء',
            angle: 308
        }
    ];

    let currentAstrolabeIdx = 3;

    function applyAstrolabeFolio(idx) {
        currentAstrolabeIdx = idx % ASTROLABE_FOLIOS.length;
        const item = ASTROLABE_FOLIOS[currentAstrolabeIdx];
        
        // Rotate Alidade Pointer
        const pointer = document.getElementById('astrolabe-alidade-pointer');
        if (pointer) {
            pointer.style.transform = `rotate(${item.angle}deg)`;
        }

        // Update Parchment Elements
        const titleEl = document.getElementById('parchment-title');
        const badgeEl = document.getElementById('parchment-badge');
        const descEl = document.getElementById('parchment-desc');
        const planetEl = document.getElementById('attr-planet');
        const angelEl = document.getElementById('attr-angel');
        const freqEl = document.getElementById('attr-freq');
        const wafqEl = document.getElementById('attr-wafq');
        const btnLabel = document.getElementById('parchment-btn-label');
        const navBtn = document.getElementById('parchment-nav-btn');

        if (titleEl) titleEl.innerText = item.title;
        if (badgeEl) badgeEl.innerText = item.badge;
        if (descEl) descEl.innerText = item.desc;
        if (planetEl) planetEl.innerText = item.planet;
        if (angelEl) angelEl.innerText = item.angel;
        if (freqEl) freqEl.innerText = item.freq;
        if (wafqEl) wafqEl.innerText = item.wafq;
        if (btnLabel) btnLabel.innerText = item.btnText;
        if (navBtn) navBtn.setAttribute('onclick', `navigateToChamber('${item.chamber}')`);
    }

    function spinAstrolabeRandomly() {
        const nextIdx = (currentAstrolabeIdx + 1) % ASTROLABE_FOLIOS.length;
        applyAstrolabeFolio(nextIdx);
    }
    """
