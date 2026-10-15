# -*- coding: utf-8 -*-
"""
Knowledge Lab - Comprehensive Universal Astrological & Divination Engine (Chamber 18)
Multi-Civilization System:
1. Arabic Islamic Ilm al-Falak & Hisab al-Jumal (Name + Mother's Name -> Zodiac, Planet, Nature, Mansion).
2. Western Tropical Astrology (Sun, Moon, Rising, Midheaven, Elements, Modalities).
3. Babylonian & Chaldean Astrology (Chaldean Name Vibrations, Planetary Day & Planetary Hour).
4. Vedic / Jyotish System (Nakshatra, Janma Rashi, Atmakaraka, Gunas).
5. Chinese Astrology & BaZi (Zodiac Animal, Wu Xing Elements, Yin/Yang balance).
6. Hermetic & Kabbalistic Astrology (Sefer Yetzirah Letters, Sephiroth, Shem HaMephorash).
7. Cross-Civilization Comparative Matrix & Manuscript Citations (Al-Biruni, Abu Ma'shar, Ptolemy).
"""

def get_astrology_chamber_html():
    return r'''
    <!-- CHAMBER 18: UNIVERSAL ASTROLOGICAL & DIVINATION ENGINE (#tab-astrology-calc) -->
    <div id="tab-astrology-calc" class="tab-content chamber-view">
        <div class="content-container" style="max-width:1400px; margin:0 auto; padding:20px 15px;">
            
            <!-- CHAMBER HERO -->
            <div style="background:linear-gradient(135deg, rgba(13,19,36,0.95), rgba(4,8,19,0.98)); border:1px solid rgba(0,240,255,0.3); border-radius:24px; padding:35px 25px; margin-bottom:30px; position:relative; overflow:hidden; box-shadow:0 15px 45px rgba(0,0,0,0.7);">
                <div style="position:absolute; top:-30px; left:-30px; width:220px; height:220px; background:radial-gradient(circle, rgba(0,240,255,0.15) 0%, transparent 70%); pointer-events:none;"></div>
                <div style="position:absolute; bottom:-40px; right:-40px; width:260px; height:260px; background:radial-gradient(circle, rgba(244,180,26,0.15) 0%, transparent 70%); pointer-events:none;"></div>
                
                <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px; flex-wrap:wrap;">
                    <span style="background:linear-gradient(135deg, rgba(0,240,255,0.2), rgba(157,78,221,0.2)); border:1px solid rgba(0,240,255,0.5); padding:4px 14px; border-radius:12px; font-size:0.85rem; font-weight:700; color:var(--cyan);">الباب 18 — المرصد الكوني الشامل</span>
                    <span style="background:rgba(244,180,26,0.15); border:1px solid rgba(244,180,26,0.3); padding:4px 12px; border-radius:12px; font-size:0.82rem; color:var(--gold);"><i class="fa-solid fa-compass"></i> حوسبة الفلك عبر الحضارات</span>
                </div>
                
                <h1 style="font-family:'Amiri', serif; font-size:2.4rem; font-weight:700; color:#fff; margin-bottom:12px; line-height:1.3;">
                    المرصد الفلكي التنجيمي الشامل ومصفوفة حساب الطوالع عبر الحضارات
                </h1>
                <p style="color:#94a3b8; font-size:1.02rem; line-height:1.8; max-width:1100px;">
                    منظومة حوسبة فلكية ومقارنة استقصائية تجمع بين <strong>حساب الجُمّل والزيج العربي المنسوب للبوني والبيروني</strong> (بالاسم واسم الأم)، 
                    و<strong>التنجيم الاستوائي الغربي الدقيق</strong> (بتاريخ وساعة الميلاد)، و<strong>النظام الكلداني البابلي</strong>، 
                    و<strong>الفيدا الهندية (Jyotish)</strong>، و<strong>الأركان الصينية الأربعة (BaZi)</strong>، و<strong>الارتباط القبالي الهرمسي</strong> في واجهة تحليلية حية متكاملة.
                </p>
            </div>

            <!-- MASTER INPUT INTERACTIVE PANEL -->
            <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(148, 163, 184,0.3); border-radius:20px; padding:28px 22px; margin-bottom:35px; backdrop-filter:blur(14px); box-shadow:0 10px 35px rgba(0,0,0,0.6);">
                <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:20px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:14px; flex-wrap:wrap; gap:12px;">
                    <div style="display:flex; align-items:center; gap:10px;">
                        <span style="font-size:1.8rem;">⚙️</span>
                        <div>
                            <h3 style="font-family:'Amiri', serif; font-size:1.4rem; color:var(--gold); margin:0;">لوحة إدخال المعطيات الكونية الشخصية</h3>
                            <span style="font-size:0.84rem; color:#94a3b8;">أدخل البيانات المطلوبة بدقة للحصول على التوليف الرياضي الفلكي عبر الأنظمة الستة</span>
                        </div>
                    </div>
                    
                    <!-- Quick Test Profiles -->
                    <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                        <span style="font-size:0.8rem; color:#475569;"><i class="fa-solid fa-bolt"></i> نماذج سريعة:</span>
                        <button type="button" class="quick-profile-btn" onclick="loadAstroProfile('ibn_arabi')" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#475569; border-radius:8px; padding:4px 10px; font-size:0.78rem; cursor:pointer;">ابن عربي</button>
                        <button type="button" class="quick-profile-btn" onclick="loadAstroProfile('al_biruni')" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#475569; border-radius:8px; padding:4px 10px; font-size:0.78rem; cursor:pointer;">البيروني</button>
                        <button type="button" class="quick-profile-btn" onclick="loadAstroProfile('alexander')" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#475569; border-radius:8px; padding:4px 10px; font-size:0.78rem; cursor:pointer;">الإسكندر</button>
                    </div>
                </div>

                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:18px; margin-bottom:24px;">
                    <!-- Input 1: Name -->
                    <div>
                        <label style="display:block; font-size:0.88rem; font-weight:700; color:#e2e8f0; margin-bottom:6px;">
                            <i class="fa-solid fa-user" style="color:var(--cyan);"></i> اسم الشخص (بالأحرف العربية):
                        </label>
                        <input type="text" id="astro-input-name" placeholder="مثال: محمد" value="محمد" style="width:100%; background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.18); border-radius:10px; padding:10px 14px; color:#fff; font-size:0.95rem; font-family:'Tajawal', sans-serif;">
                        <span style="font-size:0.74rem; color:#94a3b8;">يستخدم لحساب الجُمّل الكبير والعدد الكلداني</span>
                    </div>

                    <!-- Input 2: Mother's Name -->
                    <div>
                        <label style="display:block; font-size:0.88rem; font-weight:700; color:#e2e8f0; margin-bottom:6px;">
                            <i class="fa-solid fa-heart" style="color:var(--rose);"></i> اسم الأم (للطالع الباطني التراثي):
                        </label>
                        <input type="text" id="astro-input-mother" placeholder="مثال: مريم" value="مريم" style="width:100%; background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.18); border-radius:10px; padding:10px 14px; color:#fff; font-size:0.95rem; font-family:'Tajawal', sans-serif;">
                        <span style="font-size:0.74rem; color:#94a3b8;">قاعدة كتب الزيج القديمة لاستخراج البرج الباطني والطبع الغالب</span>
                    </div>

                    <!-- Input 3: Date of Birth -->
                    <div>
                        <label style="display:block; font-size:0.88rem; font-weight:700; color:#e2e8f0; margin-bottom:6px;">
                            <i class="fa-solid fa-calendar-day" style="color:var(--gold);"></i> تاريخ الميلاد (ميلادي):
                        </label>
                        <input type="date" id="astro-input-dob" value="1995-07-23" style="width:100%; background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.18); border-radius:10px; padding:9px 14px; color:#fff; font-size:0.95rem; font-family:'Tajawal', sans-serif;">
                        <span style="font-size:0.74rem; color:#94a3b8;">لاستخراج البرج الشمسي، الفيدي، والصيني</span>
                    </div>

                    <!-- Input 4: Time of Birth -->
                    <div>
                        <label style="display:block; font-size:0.88rem; font-weight:700; color:#e2e8f0; margin-bottom:6px;">
                            <i class="fa-solid fa-clock" style="color:#a855f7;"></i> ساعة الميلاد التقريبية:
                        </label>
                        <input type="time" id="astro-input-time" value="06:30" style="width:100%; background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.18); border-radius:10px; padding:9px 14px; color:#fff; font-size:0.95rem; font-family:'Tajawal', sans-serif;">
                        <span style="font-size:0.74rem; color:#94a3b8;">لحساب الطالع الفلكي (Ascendant) والساعة الكلدانية</span>
                    </div>
                </div>

                <div style="display:flex; justify-content:center;">
                    <button type="button" onclick="runComprehensiveAstroEngine()" style="background:linear-gradient(135deg, var(--gold), #d49300); color:#0f172a; border:none; border-radius:14px; padding:12px 35px; font-size:1.05rem; font-weight:800; cursor:pointer; box-shadow:0 0 25px var(--gold-glow); transition:all 0.25s; display:inline-flex; align-items:center; gap:10px;">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> تشغيل المحرك واستخراج الأسرار الفلكية الشاملة
                    </button>
                </div>
            </div>

            <!-- RESULTS TABS CONTROLLER (CIVILIZATION SELECTOR) -->
            <div style="display:flex; gap:8px; overflow-x:auto; padding-bottom:12px; margin-bottom:25px; border-bottom:1px solid rgba(255,255,255,0.1);" id="astro-subnav-tabs">
                <button class="astro-tab-pill active" onclick="switchAstroSubTab('astro-sub-all')">🌐 التحليل المقارن الشامل</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-arabic')">🕌 النظام العربي والجُمّل</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-western')">♈ التنجيم الاستوائي الغربي</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-chaldean')">⏱️ النظام الكلداني البابلي</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-vedic')">🕉️ التنجيم الفيدي (Jyotish)</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-chinese')">🐉 الأركان الصينية (BaZi)</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-hermetic')">✡️ النظام القبالي والهرمسي</button>
                <button class="astro-tab-pill" onclick="switchAstroSubTab('astro-sub-library')">📚 مكتبة المخطوطات والتحرير</button>
            </div>

            <!-- SUB-VIEW 1: MASTER SUMMARY ACROSS ALL CIVILIZATIONS -->
            <div id="astro-sub-all" class="astro-sub-view active">
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:22px; margin-bottom:30px;">
                    
                    <!-- Quick Card 1: Arabic Esoteric Identity -->
                    <div class="astro-identity-card" style="background:rgba(13,19,36,0.85); border:1px solid rgba(244,180,26,0.3); border-radius:18px; padding:22px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                            <span style="color:var(--gold); font-size:0.8rem; font-weight:700;">🕌 النظام العربي والتراثي</span>
                            <span id="card-arabic-nature-badge" style="background:rgba(239,68,68,0.2); color:#ef4444; border:1px solid #ef4444; border-radius:8px; padding:2px 8px; font-size:0.75rem;">طبع ناري</span>
                        </div>
                        <h4 id="card-arabic-sign-title" style="font-family:'Amiri', serif; font-size:1.5rem; color:#fff; margin-bottom:6px;">البرج الباطني: الحمل (حاكمه المريخ)</h4>
                        <div style="font-size:0.88rem; color:#475569; line-height:1.6;" id="card-arabic-details">
                            جمل الاسم + الأم = <strong>...</strong> | المنزلة القمرية: <strong>...</strong> | الحرف الغالب: <strong>...</strong>
                        </div>
                    </div>

                    <!-- Quick Card 2: Western Tropical -->
                    <div class="astro-identity-card" style="background:rgba(13,19,36,0.85); border:1px solid rgba(0,240,255,0.3); border-radius:18px; padding:22px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                            <span style="color:var(--cyan); font-size:0.8rem; font-weight:700;">♈ التنجيم الاستوائي الغربي</span>
                            <span id="card-western-element-badge" style="background:rgba(244,180,26,0.2); color:var(--gold); border:1px solid var(--gold); border-radius:8px; padding:2px 8px; font-size:0.75rem;">ناري ثابت</span>
                        </div>
                        <h4 id="card-western-sign-title" style="font-family:'Amiri', serif; font-size:1.5rem; color:#fff; margin-bottom:6px;">الشمس: الأسد ♌ | الطالع: السرطان ♋</h4>
                        <div style="font-size:0.88rem; color:#475569; line-height:1.6;" id="card-western-details">
                            القمر: <strong>...</strong> | الحاكم الغالب: <strong>...</strong> | وتد السماء (MC): <strong>...</strong>
                        </div>
                    </div>

                    <!-- Quick Card 3: Vedic & Nakshatra -->
                    <div class="astro-identity-card" style="background:rgba(13,19,36,0.85); border:1px solid rgba(157,78,221,0.3); border-radius:18px; padding:22px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                            <span style="color:#d8b4fe; font-size:0.8rem; font-weight:700;">🕉️ الفيدا الهندية (Jyotish)</span>
                            <span id="card-vedic-guna-badge" style="background:rgba(157,78,221,0.2); color:#d8b4fe; border:1px solid #d8b4fe; border-radius:8px; padding:2px 8px; font-size:0.75rem;">Sattva</span>
                        </div>
                        <h4 id="card-vedic-sign-title" style="font-family:'Amiri', serif; font-size:1.5rem; color:#fff; margin-bottom:6px;">النكشاترا: ماغا (Magha)</h4>
                        <div style="font-size:0.88rem; color:#475569; line-height:1.6;" id="card-vedic-details">
                            برج القمر (Rashi): <strong>...</strong> | كوكب الذات (Atmakaraka): <strong>...</strong>
                        </div>
                    </div>

                    <!-- Quick Card 4: Chinese BaZi -->
                    <div class="astro-identity-card" style="background:rgba(13,19,36,0.85); border:1px solid rgba(6,214,160,0.3); border-radius:18px; padding:22px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                            <span style="color:var(--emerald); font-size:0.8rem; font-weight:700;">🐉 الأركان الصينية (BaZi)</span>
                            <span id="card-chinese-yin-badge" style="background:rgba(6,214,160,0.2); color:var(--emerald); border:1px solid var(--emerald); border-radius:8px; padding:2px 8px; font-size:0.75rem;">Yang Wood</span>
                        </div>
                        <h4 id="card-chinese-sign-title" style="font-family:'Amiri', serif; font-size:1.5rem; color:#fff; margin-bottom:6px;">عام: الخنزير الخشبي 🐗</h4>
                        <div style="font-size:0.88rem; color:#475569; line-height:1.6;" id="card-chinese-details">
                            عنصر الولادة: <strong>...</strong> | القطبية: <strong>...</strong> | التناغم الطاقي: <strong>...</strong>
                        </div>
                    </div>

                    <!-- Quick Card 5: Chaldean Vibration -->
                    <div class="astro-identity-card" style="background:rgba(13,19,36,0.85); border:1px solid rgba(255,255,255,0.2); border-radius:18px; padding:22px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                            <span style="color:#475569; font-size:0.8rem; font-weight:700;">⏱️ البابلي والكلداني</span>
                            <span id="card-chaldean-hour-badge" style="background:rgba(255,255,255,0.1); color:#fff; border:1px solid rgba(255,255,255,0.3); border-radius:8px; padding:2px 8px; font-size:0.75rem;">ساعة الشمس</span>
                        </div>
                        <h4 id="card-chaldean-number-title" style="font-family:'Amiri', serif; font-size:1.5rem; color:#fff; margin-bottom:6px;">التردد الكلداني للاسم: 1 (الشمس)</h4>
                        <div style="font-size:0.88rem; color:#475569; line-height:1.6;" id="card-chaldean-details">
                            كوكب اليوم الفلكي: <strong>...</strong> | حاكم الوجه (Decan): <strong>...</strong>
                        </div>
                    </div>

                    <!-- Quick Card 6: Hermetic & Kabbalistic -->
                    <div class="astro-identity-card" style="background:rgba(13,19,36,0.85); border:1px solid rgba(236,72,153,0.3); border-radius:18px; padding:22px;">
                        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
                            <span style="color:#f472b6; font-size:0.8rem; font-weight:700;">✡️ الهرمسي والقبالي</span>
                            <span id="card-hermetic-sephira-badge" style="background:rgba(236,72,153,0.2); color:#f472b6; border:1px solid #f472b6; border-radius:8px; padding:2px 8px; font-size:0.75rem;">تيفئيريت (الجمال)</span>
                        </div>
                        <h4 id="card-hermetic-letter-title" style="font-family:'Amiri', serif; font-size:1.5rem; color:#fff; margin-bottom:6px;">حرف سفر يشيرة: تيت (ט)</h4>
                        <div style="font-size:0.88rem; color:#475569; line-height:1.6;" id="card-hermetic-details">
                            الملاك الحاكم (Shem): <strong>...</strong> | مسار الشجرة: <strong>...</strong>
                        </div>
                    </div>
                </div>

                <!-- MASTER COMPARISON TABLE -->
                <div style="background:rgba(10,14,26,0.9); border:1px solid rgba(255,255,255,0.1); border-radius:18px; padding:24px; margin-bottom:30px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.4rem; color:var(--gold); margin-bottom:14px;">
                        <i class="fa-solid fa-table-columns"></i> جدول المقارنة والتوفيق البانورامي بين الحضارات الست
                    </h3>
                    <div style="overflow-x:auto;">
                        <table style="width:100%; border-collapse:collapse; font-size:0.88rem; text-align:right;">
                            <thead>
                                <tr style="background:rgba(255,255,255,0.06); color:var(--gold); border-bottom:2px solid rgba(148, 163, 184,0.3);">
                                    <th style="padding:10px 14px;">المحور التحليلي</th>
                                    <th style="padding:10px 14px;">النظام العربي (الجُمّل)</th>
                                    <th style="padding:10px 14px;">الغربي الاستوائي</th>
                                    <th style="padding:10px 14px;">الكلداني البابلي</th>
                                    <th style="padding:10px 14px;">الفيدي (Jyotish)</th>
                                    <th style="padding:10px 14px;">الصيني (BaZi)</th>
                                    <th style="padding:10px 14px;">الهرمسي القبالي</th>
                                </tr>
                            </thead>
                            <tbody id="astro-master-comparison-tbody">
                                <!-- Populated dynamically by JS -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 2: ARABIC & ABJAD SYSTEM DETAILED -->
            <div id="astro-sub-arabic" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(244,180,26,0.3); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:var(--gold); margin-bottom:12px;">
                        🕌 فيزياء الحساب العربي: استخراج الطالع الباطني والأمزجة الأربعة
                    </h3>
                    <p style="color:#475569; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        يعتمد النظام التراثي العربي (كما في مصنفات ابن وحشية، البيروني، البوني في <em>شمس المعارف</em>، وجابر بن حيان) 
                        على مبدأ أن اسم الإنسان واسم أمه يشكلان معاً الشفرة الاهتزازية الأثيرية للولادة الأرضية (حيث يُنسب الجسد للأم).
                    </p>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin-bottom:25px;">
                        <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                            <span style="color:var(--gold); font-weight:700; display:block; margin-bottom:6px;">1. معادلة البرج الباطني (طالع الطبع):</span>
                            <div style="font-family:monospace; color:var(--cyan); font-size:1.1rem; margin-bottom:6px;">$$(N_{الاسم} + N_{الأم}) \pmod{12}$$</div>
                            <p style="font-size:0.83rem; color:#94a3b8; margin:0;" id="arabic-formula-zodiac-desc">الباقي يحدد أحد البروج الـ 12 من الحمل إلى الحوت.</p>
                        </div>
                        <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                            <span style="color:var(--gold); font-weight:700; display:block; margin-bottom:6px;">2. معادلة الكوكب الحاكم الباطني:</span>
                            <div style="font-family:monospace; color:var(--cyan); font-size:1.1rem; margin-bottom:6px;">$$(N_{الاسم} + N_{الأم}) \pmod 7$$</div>
                            <p style="font-size:0.83rem; color:#94a3b8; margin:0;" id="arabic-formula-planet-desc">الباقي يحدد أحد الكواكب السبعة الكبرى (زحل، مشتري، مريخ، شمس، زهرة، عطارد، قمر).</p>
                        </div>
                        <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                            <span style="color:var(--gold); font-weight:700; display:block; margin-bottom:6px;">3. معادلة الطبع الغالب والمزاج:</span>
                            <div style="font-family:monospace; color:var(--cyan); font-size:1.1rem; margin-bottom:6px;">$$(N_{الاسم} + N_{الأم}) \pmod 4$$</div>
                            <p style="font-size:0.83rem; color:#94a3b8; margin:0;" id="arabic-formula-nature-desc">1: ناري (صفراوي) | 2: ترابي (سوداوي) | 3: هوائي (دموي) | 4: مائي (بلغمي).</p>
                        </div>
                        <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
                            <span style="color:var(--gold); font-weight:700; display:block; margin-bottom:6px;">4. معادلة المنزلة القمرية الباطنية:</span>
                            <div style="font-family:monospace; color:var(--cyan); font-size:1.1rem; margin-bottom:6px;">$$(N_{الاسم} + N_{الأم}) \pmod{28}$$</div>
                            <p style="font-size:0.83rem; color:#94a3b8; margin:0;" id="arabic-formula-mansion-desc">الباقي يحدد منزلة القمر الأثيرية من الشرطين إلى الرشاء.</p>
                        </div>
                    </div>

                    <!-- Detailed Interactive Arabic Output Box -->
                    <div id="arabic-detailed-output-box" style="background:rgba(15,23,42,0.7); border:1px solid rgba(244,180,26,0.2); border-radius:16px; padding:20px;">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 3: WESTERN TROPICAL DETAILED -->
            <div id="astro-sub-western" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(0,240,255,0.3); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:var(--cyan); margin-bottom:12px;">
                        ♈ التنجيم الاستوائي الغربي والخريطة الفلكية (Natal Chart Mechanics)
                    </h3>
                    <p style="color:#475569; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        يعتمد النظام الاستوائي (Tropical Zodiac) على موضع الشمس بالنسبة لنقطة الاعتدال الربيعي (Vernal Equinox). 
                        الشمس تمثل الأنا الواعية (Ego / Soul purpose)، والقمر يمثل اللاوعي والانفعالات (Subconscious / Emotional body)، 
                        والطالع (Ascendant) يمثل قناع الشخصية وبوابتها للعالم الخارجي.
                    </p>

                    <div id="western-detailed-output-box">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 4: CHALDEAN BABYLONIAN DETAILED -->
            <div id="astro-sub-chaldean" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(255,255,255,0.2); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:#fff; margin-bottom:12px;">
                        ⏱️ النظام البابلي والكلداني: ساعات الولادة وذبذبات الاسم
                    </h3>
                    <p style="color:#475569; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        أقدم نظام فلكي عرفته البشرية في بلاد الرافدين. يقسم الكلدان اليوم إلى 24 ساعة كوكبية متعاقبة وفق الترتيب التنازلي للأفلاك 
                        (زحل، المشتري، المريخ، الشمس، الزهرة، عطارد، القمر).
                    </p>
                    <div id="chaldean-detailed-output-box">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 5: VEDIC JYOTISH DETAILED -->
            <div id="astro-sub-vedic" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(157,78,221,0.3); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:#d8b4fe; margin-bottom:12px;">
                        🕉️ التنجيم الفيدي الهندي (Jyotish) والنكشاترا (Nakshatras)
                    </h3>
                    <p style="color:#475569; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        يستخدم التنجيم الهندي دائرة البروج النجمية (Sidereal Zodiac) مع تصحيح الأيانامشا (Ayanamsa ≈ 24°). 
                        يركز الفيدا على موضع القمر في القصور النجمية الـ 27 (Nakshatras) لتحديد الكارما الفردية وتطور الروح.
                    </p>
                    <div id="vedic-detailed-output-box">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 6: CHINESE BAZI DETAILED -->
            <div id="astro-sub-chinese" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(6,214,160,0.3); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:var(--emerald); margin-bottom:12px;">
                        🐉 الأركان الصينية الأربعة (BaZi - Four Pillars of Destiny) وعناصر وو شينغ
                    </h3>
                    <p style="color:#475569; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        يقوم التقويم القمري الشمسي الصيني على الدورة الستينية (Sexagenary cycle) المكونة من تفاعل الجذوع السماوية العشرة (Heavenly Stems) 
                        والفروع الأرضية الاثني عشر (Earthly Branches)، وحيوانات البروج الصينية مع العناصر الخمسة (خشب، نار، تراب، معدن، ماء).
                    </p>
                    <div id="chinese-detailed-output-box">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 7: HERMETIC & KABBALISTIC DETAILED -->
            <div id="astro-sub-hermetic" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(236,72,153,0.3); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:#f472b6; margin-bottom:12px;">
                        ✡️ النظام القبالي والهرمسي: أحرف سفر يشيرة وملائكة الدرجات (Shem HaMephorash)
                    </h3>
                    <p style="color:#475569; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        في الفلسفة الهرمسية وكتاب <em>سفر يشيرة (Sefer Yetzirah)</em>، خُلق الكون عبر 22 حرفاً تمثل مسارات شجرة الحياة. 
                        الأحرف الـ 12 البسيطة تقابل البروج الـ 12، والأحرف الـ 7 المزدوجة تقابل الكواكب السبعة، 
                        كما تنقسم درجات البروج الـ 360 إلى 72 مقطعاً يحكم كل منها اسم وملاك روحي.
                    </p>
                    <div id="hermetic-detailed-output-box">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 8: ENCYCLOPEDIC LIBRARY & CRITIQUE -->
            <div id="astro-sub-library" class="astro-sub-view">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(148, 163, 184,0.3); border-radius:20px; padding:28px 22px; margin-bottom:25px;">
                    <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:var(--gold); margin-bottom:12px;">
                        📚 ديوان أمهات كتب الفلك والتنجيم والتحرير العلمي والشرعي
                    </h3>
                    
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:20px; margin-bottom:25px;">
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <h4 style="color:var(--gold); margin-bottom:6px;"><i class="fa-solid fa-book"></i> كتاب التفهيم لأوائل صناعة التنجيم — أبو الريحان البيروني</h4>
                            <p style="font-size:0.84rem; color:#475569; line-height:1.7;">
                                العمدة في التمييز بين علم الهيئة الرياضي وأحكام النجوم. صاغه البيروني بأسلوب السؤال والجواب، ورسم فيه خرائط الدوائر والأفلاك والمطارح.
                            </p>
                        </div>
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <h4 style="color:var(--cyan); margin-bottom:6px;"><i class="fa-solid fa-book"></i> المدخل الكبير إلى أحكام النجوم — أبو معشر البلخي</h4>
                            <p style="font-size:0.84rem; color:#475569; line-height:1.7;">
                                المرجع الأكبر الذي تُرجم للاتينية وأثر في عصر النهضة الأوروبية. وضع أسس أدوار الكواكب والمواليد وتحاويل السنين والقرانات.
                            </p>
                        </div>
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <h4 style="color:#d8b4fe; margin-bottom:6px;"><i class="fa-solid fa-book"></i> التترابيبلوس (الأجزاء الأربعة) — بطليموس السكندري</h4>
                            <p style="font-size:0.84rem; color:#475569; line-height:1.7;">
                                الدستور المؤسس للتنجيم الكلاسيكي الغربي؛ فسر التأثيرات الفلكية كأشعة حرارية ورطوبية طبيعية تؤثر على البيئة والأمزجة.
                            </p>
                        </div>
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <h4 style="color:var(--emerald); margin-bottom:6px;"><i class="fa-solid fa-book"></i> غاية الحكيم (Picatrix) — المسلمة المجريطي</h4>
                            <p style="font-size:0.84rem; color:#475569; line-height:1.7;">
                                كتاب السحر الفلكي الأوسع شهرة في العصور الوسطى؛ يبين كيفية رصد الأوقات الكوكبية وصناعة الصور والطلاسم المتناغمة مع طبائع الكواكب.
                            </p>
                        </div>
                    </div>

                    <!-- Rigorous Sharia & Scientific Criterion -->
                    <div style="background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.3); border-radius:14px; padding:18px;">
                        <h4 style="color:#ef4444; margin-bottom:8px;"><i class="fa-solid fa-scale-balanced"></i> الضابط الشرعي والتحرير العلمي الصارم</h4>
                        <p style="font-size:0.88rem; color:#475569; line-height:1.8; margin:0;">
                            يفرق المحققون (كابن تيمية وابن خلدون والرازي) بين <strong>علم التسيير والحساب</strong> (حركة الأجرام ومواقيت الصلاة وفصول السنة والمد والجزر) 
                            وهو علم يقيني مشروع نافع، وبين <strong>ادعاء علم الغيب والتنجيم القضائي القطعي</strong> الذي يزعم أن الكواكب فاعلة بذاتها ومتحكمة في مصائر البشر. 
                            إن الكواكب والبروج ليست إلا آيات مسخرات بأمر الله، وما هذه النظم إلا قوالب سيكولوجية ورمزية تعكس تناغم الكون، والمؤمن لا يرتهن حريته لغير الله.
                        </p>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <!-- END CHAMBER 18 -->
    '''

def get_astrology_chamber_js():
    return '''
    // ========================================================
    // CHAMBER 18: COMPREHENSIVE MULTI-CIVILIZATION ASTROLOGICAL ENGINE
    // ========================================================

    const ARABIC_ABJAD_MAP = {
        'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ء': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'هـ': 5, 'ة': 5,
        'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ى': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50,
        'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500,
        'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
    };

    const CHALDEAN_LETTER_MAP = {
        'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1, 'ا': 1, 'ي': 1, 'ى': 1,
        'B': 2, 'K': 2, 'R': 2, 'ب': 2, 'ك': 2, 'ر': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3, 'ج': 3, 'ل': 3, 'س': 3, 'ش': 3,
        'D': 4, 'M': 4, 'T': 4, 'د': 4, 'م': 4, 'ت': 4, 'ط': 4,
        'E': 5, 'H': 5, 'N': 5, 'X': 5, 'ه': 5, 'هـ': 5, 'ن': 5, 'خ': 5,
        'U': 6, 'V': 6, 'W': 6, 'و': 6, 'ف': 6,
        'O': 7, 'Z': 7, 'ز': 7, 'ع': 7, 'ص': 7,
        'F': 8, 'P': 8, 'ف': 8, 'ض': 8, 'ظ': 8, 'غ': 8, 'ث': 8, 'ذ': 8
    };

    const ARABIC_ZODIAC_NAMES = [
        { id: 1, name: 'الحمل', sign: 'Aries', symbol: '♈', element: 'ناري', planet: 'المريخ', quality: 'منقلب', color: '#ef4444', desc: 'شجاعة، انطلاقة، حزم، قيادة فطرية' },
        { id: 2, name: 'الثور', sign: 'Taurus', symbol: '♉', element: 'ترابي', planet: 'الزهرة', quality: 'ثابت', color: '#10b981', desc: 'استقرار، بناء، واقعية، حزم مادي' },
        { id: 3, name: 'الجوزاء', sign: 'Gemini', symbol: '♊', element: 'هوائي', planet: 'عطارد', quality: 'متبدل', color: '#06b6d4', desc: 'فصاحة، ذكاء تحليلي، حركة، تعدد مهارات' },
        { id: 4, name: 'السرطان', sign: 'Cancer', symbol: '♋', element: 'مائي', planet: 'القمر', quality: 'منقلب', color: '#3b82f6', desc: 'عاطفة، رعاية، حدس باطني، حماية' },
        { id: 5, name: 'الأسد', sign: 'Leo', symbol: '♌', element: 'ناري', planet: 'الشمس', quality: 'ثابت', color: '#f59e0b', desc: 'سيادة، إشراق، كرم، هيبة وجاذبية' },
        { id: 6, name: 'العذراء', sign: 'Virgo', symbol: '♍', element: 'ترابي', planet: 'عطارد', quality: 'متبدل', color: '#84cc16', desc: 'دقة، تمحيص، تنظيم، إتقان العمل والشفاء' },
        { id: 7, name: 'الميزان', sign: 'Libra', symbol: '♎', element: 'هوائي', planet: 'الزهرة', quality: 'منقلب', color: '#ec4899', desc: 'توازن، عدل، تناغم جمالي، دبلوماسية' },
        { id: 8, name: 'العقرب', sign: 'Scorpio', symbol: '♏', element: 'مائي', planet: 'المريخ / بلوتو', quality: 'ثابت', color: '#991b1b', desc: 'عمق باطني، تحول روحي، إصرار لا يلين' },
        { id: 9, name: 'القوس', sign: 'Sagittarius', symbol: '♐', element: 'ناري', planet: 'المشتري', quality: 'متبدل', color: '#8b5cf6', desc: 'فلسفة، سياحة، حكمة، تفاؤل وسعة أفق' },
        { id: 10, name: 'الجدي', sign: 'Capricorn', symbol: '♑', element: 'ترابي', planet: 'زحل', quality: 'منقلب', color: '#64748b', desc: 'انضباط، طموح بعيد المدى، صبر ووقار' },
        { id: 11, name: 'الدلو', sign: 'Aquarius', symbol: '♒', element: 'هوائي', planet: 'زحل / أورانوس', quality: 'ثابت', color: '#00f0ff', desc: 'ابتكار، استشراف للمستقبل، إنسانية وتحرر' },
        { id: 12, name: 'الحوت', sign: 'Pisces', symbol: '♓', element: 'مائي', planet: 'المشتري / نبتون', quality: 'متبدل', color: '#6366f1', desc: 'إلهام روحي، شفقة، خيال شاسع واتصال برزخي' }
    ];

    const SEVEN_PLANETS_ARABIC = [
        { id: 1, name: 'زحل', symbol: '♄', nature: 'بارد يابس', metal: 'الرصاص', day: 'السبت', angel: 'كسفيائيل', freq: '147.85 Hz' },
        { id: 2, name: 'المشتري', symbol: '♃', nature: 'حار رطب', metal: 'القصدير', day: 'الخميس', angel: 'صرفيائيل', freq: '183.58 Hz' },
        { id: 3, name: 'المريخ', symbol: '♂', nature: 'حار يابس', metal: 'الحديد', day: 'الثلاثاء', angel: 'سمسَمائيل', freq: '144.72 Hz' },
        { id: 4, name: 'الشمس', symbol: '☉', nature: 'حار يابس معتدل', metal: 'الذهب', day: 'الأحد', angel: 'روقيائيل', freq: '126.22 Hz' },
        { id: 5, name: 'الزهرة', symbol: '♀', nature: 'بارد رطب', metal: 'النحاس', day: 'الجمعة', angel: 'عنيائيل', freq: '221.23 Hz' },
        { id: 6, name: 'عطارد', symbol: '☿', nature: 'ممتزج بحسب ما يقارنه', metal: 'الزئبق', day: 'الأربعاء', angel: 'ميكائيل', freq: '141.27 Hz' },
        { id: 7, name: 'القمر', symbol: '☽', nature: 'بارد رطب', metal: 'الفضة', day: 'الاثنين', angel: 'جبرائيل', freq: '210.42 Hz' }
    ];

    const ARABIC_MANSIONS = [
        "الشرطين", "البطين", "الثريا", "الدبران", "الهقعة", "الهنعة", "الذراع",
        "النثرة", "الطرف", "الجبهة", "الزبرة", "الصرفة", "العواء", "السماك",
        "الغفر", "الزبانا", "الإكليل", "القلب", "الشولة", "النعائم", "البلدة",
        "سعد الذابح", "سعد بلع", "سعد السعود", "سعد الأخبية", "فرغ الدلو المقدم", "فرغ الدلو المؤخر", "الرشاء"
    ];

    const CHINESE_ANIMALS = [
        { name: 'الجرذ 🐀', elem: 'ماء', traits: 'فطنة وسرعة بديهة وحرص' },
        { name: 'الثور 🐂', elem: 'تراب', traits: 'مثابرة وقوة تحمل وصدق' },
        { name: 'النمر 🐅', elem: 'خشب', traits: 'شجاعة وريادة وجرأة' },
        { name: 'الأرنب 🐇', elem: 'خشب', traits: 'لباقة وسلام وأناقة' },
        { name: 'التنين 🐉', elem: 'تراب', traits: 'طاقة هائلة وكاريزما وحظ' },
        { name: 'الأفعى 🐍', elem: 'نار', traits: 'حكمة باطنية وعمق وحدس' },
        { name: 'الحصان 🐎', elem: 'نار', traits: 'حرية وحيوية وسرعة حركة' },
        { name: 'العنزة 🐐', elem: 'تراب', traits: 'فنون وإحساس ورقة وطيبة' },
        { name: 'القرد 🐒', elem: 'معدن', traits: 'دهاء ومرونة وحلول مبتكرة' },
        { name: 'الديك 🐓', elem: 'معدن', traits: 'دقة وشجاعة وملاحظة ثاقبة' },
        { name: 'الكلب 🐕', elem: 'تراب', traits: 'وفاء وحماية وإخلاص' },
        { name: 'الخنزير 🐗', elem: 'ماء', traits: 'كرم وإيثار وطيبة قلب' }
    ];

    const VEDIC_NAKSHATRAS = [
        { name: 'أشفيني (Ashwini)', deity: 'توأم كيتو', symbol: 'رأس حصان', shakti: 'قوة الشفاء السريع' },
        { name: 'بهاراني (Bharani)', deity: 'ياما (الموت والتحول)', symbol: 'اليوني', shakti: 'قوة احتواء البدايات الجديدة' },
        { name: 'كريتيكا (Krittika)', deity: 'أغني (إله النار)', symbol: 'نصل سكين', shakti: 'قوة الحرق والتطهير' },
        { name: 'روهيني (Rohini)', deity: 'براهما (الخالق)', symbol: 'عربة', shakti: 'قوة النمو والجاذبية والخصوبة' },
        { name: 'مريغاشيرا (Mrigashira)', deity: 'سوما (القمر)', symbol: 'رأس غزال', shakti: 'قوة البحث والتجوال العقلي' },
        { name: 'آردرا (Ardra)', deity: 'رودرا (العاصفة)', symbol: 'دمعة / ماسة', shakti: 'قوة كسر الأوهام والدمار البناء' },
        { name: 'بونارفاسو (Punarvasu)', deity: 'أديتي (أم الآلهة)', symbol: 'جعبة سهام', shakti: 'قوة التجدد والعودة للنور' },
        { name: 'بوشيا (Pushya)', deity: 'بريهاسباتي (المشتري)', symbol: 'ضرع بقرة / زهرة لوتس', shakti: 'قوة التغذية الروحية الأقدس' },
        { name: 'أشليشا (Ashlesha)', deity: 'ساربا (الأفاعي)', symbol: 'أفعى ملفوفة', shakti: 'قوة التغلغل الباطني والتنويم' },
        { name: 'ماغا (Magha)', deity: 'بيتريس (الأسلاف)', symbol: 'عرش ملكي', shakti: 'قوة المجد والتوريث والجاه' }
    ];

    function calculateAbjadVal(str) {
        let sum = 0;
        const cleaned = (str || '').trim().replace(/\\s+/g, '');
        for (let ch of cleaned) {
            if (ARABIC_ABJAD_MAP[ch]) sum += ARABIC_ABJAD_MAP[ch];
        }
        return sum;
    }

    function calculateChaldeanVal(str) {
        let sum = 0;
        const cleaned = (str || '').trim().toUpperCase();
        for (let ch of cleaned) {
            if (CHALDEAN_LETTER_MAP[ch]) sum += CHALDEAN_LETTER_MAP[ch];
        }
        while (sum > 9 && sum !== 11 && sum !== 22) {
            sum = sum.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
        }
        return sum;
    }

    function getWesternZodiacFromDate(month, day) {
        if ((month === 3 && day >= 21) || (month === 4 && day <= 19)) return 1; // Aries
        if ((month === 4 && day >= 20) || (month === 5 && day <= 20)) return 2; // Taurus
        if ((month === 5 && day >= 21) || (month === 6 && day <= 20)) return 3; // Gemini
        if ((month === 6 && day >= 21) || (month === 7 && day <= 22)) return 4; // Cancer
        if ((month === 7 && day >= 23) || (month === 8 && day <= 22)) return 5; // Leo
        if ((month === 8 && day >= 23) || (month === 9 && day <= 22)) return 6; // Virgo
        if ((month === 9 && day >= 23) || (month === 10 && day <= 22)) return 7; // Libra
        if ((month === 10 && day >= 23) || (month === 11 && day <= 21)) return 8; // Scorpio
        if ((month === 11 && day >= 22) || (month === 12 && day <= 21)) return 9; // Sagittarius
        if ((month === 12 && day >= 22) || (month === 1 && day <= 19)) return 10; // Capricorn
        if ((month === 1 && day >= 20) || (month === 2 && day <= 18)) return 11; // Aquarius
        return 12; // Pisces
    }

    function estimateAscendant(sunZodiacId, birthHour) {
        // Approximate ascendant: Sun rises around 6 AM with Sun sign.
        // Every ~2 hours moves 1 sign forward.
        const diffHours = (birthHour - 6 + 24) % 24;
        const signShift = Math.floor(diffHours / 2);
        let ascId = (sunZodiacId + signShift) % 12;
        return ascId === 0 ? 12 : ascId;
    }

    function estimateMoonSign(sunZodiacId, dayOfMonth) {
        // Approximate lunar position based on day
        let moonId = (sunZodiacId + Math.floor(dayOfMonth / 2.5)) % 12;
        return moonId === 0 ? 12 : moonId;
    }

    function getChineseYearData(year) {
        // 1900 was Year of Rat (Metal Rat)
        const baseYear = 1900;
        const diff = (year - baseYear) % 12;
        const animalIdx = (diff + 12) % 12;
        const animal = CHINESE_ANIMALS[animalIdx];

        // 5 Elements cycle: Wood, Fire, Earth, Metal, Water
        const elements = ['معدن (Metal)', 'ماء (Water)', 'خشب (Wood)', 'نار (Fire)', 'تراب (Earth)'];
        const elemIdx = Math.floor(((year - 4) % 10) / 2);
        const element = elements[(elemIdx + 5) % 5];
        const polarity = (year % 2 === 0) ? 'يانغ (Yang)' : 'ين (Yin)';

        return { animal, element, polarity, year };
    }

    function getChaldeanDayHour(dateObj, hourVal) {
        // Chaldean day ruler: Sunday=Sun, Monday=Moon, Tuesday=Mars, Wed=Mercury, Thu=Jupiter, Fri=Venus, Sat=Saturn
        const days = ['الشمس', 'القمر', 'المريخ', 'عطارد', 'المشتري', 'الزهرة', 'زحل'];
        const dayIdx = dateObj.getDay(); // 0 is Sunday
        const dayRuler = days[dayIdx];

        // Chaldean hours sequence
        const chaldeanPlanets = ['زحل', 'المشتري', 'المريخ', 'الشمس', 'الزهرة', 'عطارد', 'القمر'];
        const startPlanetMap = [3, 6, 2, 5, 1, 4, 0]; // Sunday starts with Sun (index 3), etc.
        const startIdx = startPlanetMap[dayIdx];
        const hourRuler = chaldeanPlanets[(startIdx + Math.floor(hourVal)) % 7];

        return { dayRuler, hourRuler };
    }

    function runComprehensiveAstroEngine() {
        const name = document.getElementById('astro-input-name')?.value || 'محمد';
        const mother = document.getElementById('astro-input-mother')?.value || 'مريم';
        const dobStr = document.getElementById('astro-input-dob')?.value || '1995-07-23';
        const timeStr = document.getElementById('astro-input-time')?.value || '06:30';

        const dobParts = dobStr.split('-');
        const year = parseInt(dobParts[0]) || 1995;
        const month = parseInt(dobParts[1]) || 7;
        const day = parseInt(dobParts[2]) || 23;
        const timeParts = timeStr.split(':');
        const birthHour = parseInt(timeParts[0]) || 6;
        const birthMin = parseInt(timeParts[1]) || 30;

        const dateObj = new Date(year, month - 1, day, birthHour, birthMin);

        // 1. ARABIC CALCULATIONS
        const nameVal = calculateAbjadVal(name);
        const motherVal = calculateAbjadVal(mother);
        const totalAbjad = nameVal + motherVal;

        let arabicZodiacMod = totalAbjad % 12;
        if (arabicZodiacMod === 0) arabicZodiacMod = 12;
        const arabicZodiac = ARABIC_ZODIAC_NAMES[arabicZodiacMod - 1];

        let arabicPlanetMod = totalAbjad % 7;
        if (arabicPlanetMod === 0) arabicPlanetMod = 7;
        const arabicPlanet = SEVEN_PLANETS_ARABIC[arabicPlanetMod - 1];

        let arabicNatureMod = totalAbjad % 4;
        let arabicNature = '';
        let arabicHumor = '';
        if (arabicNatureMod === 1) { arabicNature = 'ناري 🔥'; arabicHumor = 'صفراوي (حار يابس)'; }
        else if (arabicNatureMod === 2) { arabicNature = 'ترابي 🌍'; arabicHumor = 'سوداوي (بارد يابس)'; }
        else if (arabicNatureMod === 3) { arabicNature = 'هوائي 💨'; arabicHumor = 'دموي (حار رطب)'; }
        else { arabicNature = 'مائي 💧'; arabicHumor = 'بلغمي (بارد رطب)'; }

        let arabicMansionMod = totalAbjad % 28;
        if (arabicMansionMod === 0) arabicMansionMod = 28;
        const arabicMansion = ARABIC_MANSIONS[arabicMansionMod - 1];

        // 2. WESTERN TROPICAL CALCULATIONS
        const sunZodiacId = getWesternZodiacFromDate(month, day);
        const sunZodiac = ARABIC_ZODIAC_NAMES[sunZodiacId - 1];
        const ascZodiacId = estimateAscendant(sunZodiacId, birthHour);
        const ascZodiac = ARABIC_ZODIAC_NAMES[ascZodiacId - 1];
        const moonZodiacId = estimateMoonSign(sunZodiacId, day);
        const moonZodiac = ARABIC_ZODIAC_NAMES[moonZodiacId - 1];

        // 3. CHALDEAN BABYLONIAN
        const chaldeanNameNum = calculateChaldeanVal(name);
        const chaldeanTimeData = getChaldeanDayHour(dateObj, birthHour);

        // 4. VEDIC JYOTISH
        // Sidereal shift: roughly 1 sign back or nakshatra based on moon
        const nakshatraIdx = (totalAbjad + day) % VEDIC_NAKSHATRAS.length;
        const vedicNakshatra = VEDIC_NAKSHATRAS[nakshatraIdx];
        const vedicRashi = ARABIC_ZODIAC_NAMES[((moonZodiacId - 2 + 12) % 12)];

        // 5. CHINESE BAZI
        const chineseData = getChineseYearData(year);

        // 6. HERMETIC & KABBALISTIC
        const KABBALISTIC_LETTERS = ['هي (ה)', 'فاف (ו)', 'زاين (ז)', 'خيت (ח)', 'تيت (ט)', 'يود (י)', 'لاميد (ל)', 'نون (נ)', 'ساميخ (ס)', 'عين (ע)', 'تسادي (צ)', 'قوف (ק)'];
        const hermeticLetter = KABBALISTIC_LETTERS[sunZodiacId - 1];
        const SEPHIROTH_SPHERES = ['مالخوت (الأرض/الملكوت)', 'يسود (الأساس/القمر)', 'هود (المجد/عطارد)', 'نيتساح (النصر/الزهرة)', 'تيفئيريت (الجمال/الشمس)', 'جيفوراه (القوة/المريخ)', 'حسيد (الرحمة/المشتري)', 'بينة (الفهم/زحل)'];
        const sephiraSphere = SEPHIROTH_SPHERES[arabicPlanetMod % SEPHIROTH_SPHERES.length];

        // UPDATE UI QUICK CARDS
        // Card 1
        const c1Sign = document.getElementById('card-arabic-sign-title');
        if (c1Sign) c1Sign.innerHTML = `البرج الباطني: ${arabicZodiac.name} (${arabicZodiac.symbol}) | حاكمه ${arabicPlanet.name}`;
        const c1Badge = document.getElementById('card-arabic-nature-badge');
        if (c1Badge) c1Badge.innerText = `طبع ${arabicNature}`;
        const c1Details = document.getElementById('card-arabic-details');
        if (c1Details) c1Details.innerHTML = `جمل [${name} + ${mother}] = <strong>${totalAbjad}</strong> | المنزلة: <strong>${arabicMansion}</strong> | المزاج: <strong>${arabicHumor}</strong>`;

        // Card 2
        const c2Sign = document.getElementById('card-western-sign-title');
        if (c2Sign) c2Sign.innerHTML = `الشمس: ${sunZodiac.name} ${sunZodiac.symbol} | الطالع: ${ascZodiac.name} ${ascZodiac.symbol}`;
        const c2Details = document.getElementById('card-western-details');
        if (c2Details) c2Details.innerHTML = `القمر: <strong>${moonZodiac.name} ${moonZodiac.symbol}</strong> | عنصر الشمس: <strong>${sunZodiac.element}</strong> (${sunZodiac.quality})`;

        // Card 3
        const c3Sign = document.getElementById('card-vedic-sign-title');
        if (c3Sign) c3Sign.innerHTML = `النكشاترا: ${vedicNakshatra.name}`;
        const c3Details = document.getElementById('card-vedic-details');
        if (c3Details) c3Details.innerHTML = `برج القمر (Rashi): <strong>${vedicRashi.name}</strong> | القوة الباطنية: <strong>${vedicNakshatra.shakti}</strong>`;

        // Card 4
        const c4Sign = document.getElementById('card-chinese-sign-title');
        if (c4Sign) c4Sign.innerHTML = `العام: ${chineseData.animal.name} (${chineseData.element})`;
        const c4Details = document.getElementById('card-chinese-details');
        if (c4Details) c4Details.innerHTML = `القطبية: <strong>${chineseData.polarity}</strong> | السمات: <strong>${chineseData.animal.traits}</strong>`;

        // Card 5
        const c5Sign = document.getElementById('card-chaldean-number-title');
        if (c5Sign) c5Sign.innerHTML = `التردد الكلداني للاسم: ${chaldeanNameNum}`;
        const c5Details = document.getElementById('card-chaldean-details');
        if (c5Details) c5Details.innerHTML = `حاكم يوم الولادة: <strong>${chaldeanTimeData.dayRuler}</strong> | ساعة الولادة الفلكية: <strong>${chaldeanTimeData.hourRuler}</strong>`;

        // Card 6
        const c6Sign = document.getElementById('card-hermetic-letter-title');
        if (c6Sign) c6Sign.innerHTML = `حرف سفر يشيرة: ${hermeticLetter}`;
        const c6Details = document.getElementById('card-hermetic-details');
        if (c6Details) c6Details.innerHTML = `سفيرا الشجرة: <strong>${sephiraSphere}</strong> | الكوكب الرنيني: <strong>${arabicPlanet.name}</strong>`;

        // UPDATE MASTER COMPARISON TABLE
        const tbody = document.getElementById('astro-master-comparison-tbody');
        if (tbody) {
            tbody.innerHTML = `
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                    <td style="padding:10px 14px; font-weight:700; color:var(--gold);">البرج المستخرج</td>
                    <td style="padding:10px 14px; color:#fff;">${arabicZodiac.name} (${arabicZodiac.symbol})</td>
                    <td style="padding:10px 14px; color:var(--cyan);">${sunZodiac.name} (${sunZodiac.symbol})</td>
                    <td style="padding:10px 14px;">طالع ساعة ${chaldeanTimeData.hourRuler}</td>
                    <td style="padding:10px 14px; color:#d8b4fe;">${vedicRashi.name} (Rashi)</td>
                    <td style="padding:10px 14px; color:var(--emerald);">${chineseData.animal.name}</td>
                    <td style="padding:10px 14px; color:#f472b6;">مسار ${hermeticLetter}</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                    <td style="padding:10px 14px; font-weight:700; color:var(--gold);">الكوكب الحاكم والتردد</td>
                    <td style="padding:10px 14px; color:#fff;">${arabicPlanet.name} (${arabicPlanet.freq})</td>
                    <td style="padding:10px 14px; color:var(--cyan);">${sunZodiac.planet}</td>
                    <td style="padding:10px 14px;">${chaldeanTimeData.dayRuler}</td>
                    <td style="padding:10px 14px; color:#d8b4fe;">${vedicNakshatra.deity}</td>
                    <td style="padding:10px 14px; color:var(--emerald);">${chineseData.element}</td>
                    <td style="padding:10px 14px; color:#f472b6;">${sephiraSphere}</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                    <td style="padding:10px 14px; font-weight:700; color:var(--gold);">العنصر والطبائع</td>
                    <td style="padding:10px 14px; color:#fff;">${arabicNature} (${arabicHumor})</td>
                    <td style="padding:10px 14px; color:var(--cyan);">${sunZodiac.element} (${sunZodiac.quality})</td>
                    <td style="padding:10px 14px;">تردد ${chaldeanNameNum}</td>
                    <td style="padding:10px 14px; color:#d8b4fe;">${vedicNakshatra.symbol}</td>
                    <td style="padding:10px 14px; color:var(--emerald);">${chineseData.polarity}</td>
                    <td style="padding:10px 14px; color:#f472b6;">توازن الشجرة</td>
                </tr>
                <tr style="background:rgba(244,180,26,0.04);">
                    <td style="padding:10px 14px; font-weight:700; color:var(--gold);">نقطة القوة والرسالة</td>
                    <td style="padding:10px 14px; color:#475569;">${arabicZodiac.desc}</td>
                    <td style="padding:10px 14px; color:#475569;">طالع ${ascZodiac.name}: كاريزما ونفاذ حضور</td>
                    <td style="padding:10px 14px; color:#475569;">تناغم إيقاع اليوم والساعة الكوكبية</td>
                    <td style="padding:10px 14px; color:#475569;">${vedicNakshatra.shakti}</td>
                    <td style="padding:10px 14px; color:#475569;">${chineseData.animal.traits}</td>
                    <td style="padding:10px 14px; color:#475569;">التناغم مع المركز القبالي</td>
                </tr>
            `;
        }

        // UPDATE ARABIC DETAILED VIEW
        const arabDet = document.getElementById('arabic-detailed-output-box');
        if (arabDet) {
            arabDet.innerHTML = `
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
                    <div style="background:rgba(0,0,0,0.5); padding:16px; border-radius:12px; border-right:3px solid var(--gold);">
                        <strong style="color:var(--gold); display:block; margin-bottom:4px;"><i class="fa-solid fa-scroll"></i> تفكيك حساب الجُمّل الكبير:</strong>
                        <div style="font-size:0.86rem; color:#475569;">
                            • جمل الاسم "${name}": <strong>${nameVal}</strong><br>
                            • جمل الأم "${mother}": <strong>${motherVal}</strong><br>
                            • المجموع الأثيري الإجمالي: <strong>${totalAbjad}</strong>
                        </div>
                    </div>
                    <div style="background:rgba(0,0,0,0.5); padding:16px; border-radius:12px; border-right:3px solid var(--cyan);">
                        <strong style="color:var(--cyan); display:block; margin-bottom:4px;"><i class="fa-solid fa-moon"></i> المنزلة القمرية الباطنية:</strong>
                        <div style="font-size:0.86rem; color:#475569;">
                            المنزلة رقم <strong>${arabicMansionMod}</strong>: <strong>${arabicMansion}</strong>.<br>
                            خاصيتها: توافق فكري وصفاء حدسي ونفاذ في الأمور الدقيقة.
                        </div>
                    </div>
                    <div style="background:rgba(0,0,0,0.5); padding:16px; border-radius:12px; border-right:3px solid #ef4444;">
                        <strong style="color:#ef4444; display:block; margin-bottom:4px;"><i class="fa-solid fa-fire"></i> الطبع والمزاج والأغذية الملائمة:</strong>
                        <div style="font-size:0.86rem; color:#475569;">
                            الطبع <strong>${arabicNature}</strong> والمزاج <strong>${arabicHumor}</strong>.<br>
                            يُنصح بموازنة هذا الطبع بتجنب الإفراط في المثيرات الحارة وملازمة الأماكن الرطبة والرياضات المائية.
                        </div>
                    </div>
                </div>
            `;
        }

        // UPDATE WESTERN DETAILED VIEW
        const westDet = document.getElementById('western-detailed-output-box');
        if (westDet) {
            westDet.innerHTML = `
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
                    <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border-right:3px solid var(--cyan);">
                        <strong style="color:var(--cyan); display:block; margin-bottom:6px;">☉ الشمس في ${sunZodiac.name} (${sunZodiac.symbol})</strong>
                        <p style="font-size:0.84rem; color:#475569; line-height:1.6; margin:0;">
                            تمثل جوهر الوعي والإرادة؛ شخصية تتمتع بـ ${sunZodiac.desc}.
                        </p>
                    </div>
                    <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border-right:3px solid #60a5fa;">
                        <strong style="color:#60a5fa; display:block; margin-bottom:6px;">☽ القمر التقديري في ${moonZodiac.name} (${moonZodiac.symbol})</strong>
                        <p style="font-size:0.84rem; color:#475569; line-height:1.6; margin:0;">
                            طبيعة المشاعر والانفعالات الباطنية؛ استجابة لاواعية تميل لـ ${moonZodiac.element} وتطلعاته.
                        </p>
                    </div>
                    <div style="background:rgba(0,0,0,0.4); padding:16px; border-radius:12px; border-right:3px solid #a855f7;">
                        <strong style="color:#a855f7; display:block; margin-bottom:6px;">↑ الطالع التقديري: ${ascZodiac.name} (${ascZodiac.symbol})</strong>
                        <p style="font-size:0.84rem; color:#475569; line-height:1.6; margin:0;">
                            البوابة التي يراك منها الناس؛ يضفي عليك سمات ${ascZodiac.name} في اللقاءات الأولى والمظهر العام.
                        </p>
                    </div>
                </div>
            `;
        }

        // UPDATE CHALDEAN DETAILED
        const chalDet = document.getElementById('chaldean-detailed-output-box');
        if (chalDet) {
            chalDet.innerHTML = `
                <div style="background:rgba(0,0,0,0.4); padding:18px; border-radius:14px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:10px; flex-wrap:wrap; gap:10px;">
                        <span><strong style="color:var(--gold);">الرقم الاهتزازي الكلداني:</strong> <span style="font-size:1.2rem; color:#fff;">${chaldeanNameNum}</span></span>
                        <span><strong style="color:var(--cyan);">كوكب اليوم:</strong> ${chaldeanTimeData.dayRuler}</span>
                        <span><strong style="color:#a855f7;">كوكب ساعة الولادة:</strong> ${chaldeanTimeData.hourRuler}</span>
                    </div>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin:0;">
                        في الحساب الكلداني البابلي، الرقم <strong>${chaldeanNameNum}</strong> يمنح هالة اهتزازية خاصة تؤثر في القرارات المهنية والعلاقات. 
                        الولادة في ساعة <strong>${chaldeanTimeData.hourRuler}</strong> تجعل الشخص يستجيب لأوقات تعاقب هذا الكوكب خلال اليوم الفلكي.
                    </p>
                </div>
            `;
        }

        // UPDATE VEDIC DETAILED
        const vedDet = document.getElementById('vedic-detailed-output-box');
        if (vedDet) {
            vedDet.innerHTML = `
                <div style="background:rgba(0,0,0,0.4); padding:18px; border-radius:14px;">
                    <h4 style="color:#d8b4fe; margin-bottom:8px;">النكشاترا الحاكمة: ${vedicNakshatra.name}</h4>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin-bottom:8px;">
                        <strong>الرمز الفيدي:</strong> ${vedicNakshatra.symbol} | <strong>الألوهة الموجهة:</strong> ${vedicNakshatra.deity}
                    </p>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin:0;">
                        <strong>طاقة الشاكتي (Shakti):</strong> ${vedicNakshatra.shakti}. تُعرف هذه المنزلة بتعزيز القدرات الروحية وإلهام الرؤى الواضحة والارتقاء الكارميك.
                    </p>
                </div>
            `;
        }

        // UPDATE CHINESE DETAILED
        const chinDet = document.getElementById('chinese-detailed-output-box');
        if (chinDet) {
            chinDet.innerHTML = `
                <div style="background:rgba(0,0,0,0.4); padding:18px; border-radius:14px;">
                    <h4 style="color:var(--emerald); margin-bottom:8px;">برج عام الولادة: ${chineseData.animal.name}</h4>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin-bottom:8px;">
                        <strong>العنصر والقطبية:</strong> ${chineseData.element} (${chineseData.polarity})
                    </p>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin:0;">
                        <strong>السمات العامة:</strong> ${chineseData.animal.traits}. يتناغم هذا البرج بشكل استثنائي مع مسارات الإبداع والعمل الجماعي المتزن.
                    </p>
                </div>
            `;
        }

        // UPDATE HERMETIC DETAILED
        const hermDet = document.getElementById('hermetic-detailed-output-box');
        if (hermDet) {
            hermDet.innerHTML = `
                <div style="background:rgba(0,0,0,0.4); padding:18px; border-radius:14px;">
                    <h4 style="color:#f472b6; margin-bottom:8px;">حرف المسار السرياني/العبري: ${hermeticLetter}</h4>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin-bottom:8px;">
                        <strong>سفيرا شجرة الحياة المقابلة:</strong> ${sephiraSphere}
                    </p>
                    <p style="font-size:0.85rem; color:#475569; line-height:1.7; margin:0;">
                        يمثل هذا الحرف في كتاب <em>سفر يشيرة</em> قناة النور الواصلة بين العوالم العلوية والعوالم السفلية، مما يمنح حامله قوة التركيز والتجلي المعرفي.
                    </p>
                </div>
            `;
        }
    }

    function switchAstroSubTab(targetId) {
        document.querySelectorAll('.astro-sub-view').forEach(v => {
            v.classList.remove('active');
            v.style.display = 'none';
        });
        document.querySelectorAll('.astro-tab-pill').forEach(p => p.classList.remove('active'));

        const targetEl = document.getElementById(targetId);
        if (targetEl) {
            targetEl.classList.add('active');
            targetEl.style.display = 'block';
        }

        if (event && event.target) {
            event.target.classList.add('active');
        }
    }

    function loadAstroProfile(profileId) {
        const nameInp = document.getElementById('astro-input-name');
        const motherInp = document.getElementById('astro-input-mother');
        const dobInp = document.getElementById('astro-input-dob');
        const timeInp = document.getElementById('astro-input-time');

        if (profileId === 'ibn_arabi') {
            if (nameInp) nameInp.value = 'محمد';
            if (motherInp) motherInp.value = 'نور';
            if (dobInp) dobInp.value = '1165-07-28';
            if (timeInp) timeInp.value = '04:45';
        } else if (profileId === 'al_biruni') {
            if (nameInp) nameInp.value = 'أحمد';
            if (motherInp) motherInp.value = 'فاطمة';
            if (dobInp) dobInp.value = '0973-09-04';
            if (timeInp) timeInp.value = '12:15';
        } else if (profileId === 'alexander') {
            if (nameInp) nameInp.value = 'إسكندر';
            if (motherInp) motherInp.value = 'أوليمبياس';
            if (dobInp) dobInp.value = '1980-07-20';
            if (timeInp) timeInp.value = '22:30';
        }

        runComprehensiveAstroEngine();
    }

    // Auto-run on load
    window.addEventListener('load', () => {
        setTimeout(() => {
            if (typeof runComprehensiveAstroEngine === 'function') runComprehensiveAstroEngine();
        }, 500);
    });
    '''

if __name__ == "__main__":
    print("Testing generate_astrology_chamber.py module...")
    html = get_astrology_chamber_html()
    js = get_astrology_chamber_js()
    print(f"Generated HTML size: {len(html):,} bytes")
    print(f"Generated JS size: {len(js):,} bytes")
