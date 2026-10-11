# -*- coding: utf-8 -*-
"""
Knowledge Lab - Esoteric Seals, Zouhri Phenomenon & Spiritual Bloodlines (Chamber 19)
Comprehensive deep modules:
1. The Seven Seals of Solomon (SVG rendered symbols, Ali Ibn Abi Talib poem, planetary & abjad keys).
2. The Ghazali Triangle & 3x3 Magic Square (Mathematical laws, live calculator, deconstruction of treasure myths).
3. The 30 Master Palm Seals & Chiromancy Codex (Master SVG Palm Atlas with 111 marking, 30 documented seals).
4. The Seven Planetary Seals & Sigils from Picatrix & Agrippa (Kamea tracing method, planetary characters).
5. The Zouhri Phenomenon (The Zouhri human, historical/kabbalistic roots, medical anatomy vs myths).
6. Spiritual Bloodlines & Starseeds across Sacred & Ancient texts.
7. Interactive SVG Symbol & Sigil Explorer with zoom and detailed glyph breakdown.
"""

def get_seals_zouhri_chamber_html():
    return '''
    <!-- CHAMBER 19: ESOTERIC SEALS, ZOUHRI PHENOMENON & SPIRITUAL LINEAGES (#tab-seals-zouhri) -->
    <div id="tab-seals-zouhri" class="tab-content chamber-view">
        <div class="content-container" style="max-width:1400px; margin:0 auto; padding:20px 15px;">
            
            <!-- CHAMBER HERO -->
            <div style="background:linear-gradient(135deg, rgba(17,10,32,0.95), rgba(4,6,15,0.98)); border:1px solid rgba(157,78,221,0.35); border-radius:24px; padding:35px 25px; margin-bottom:30px; position:relative; overflow:hidden; box-shadow:0 15px 45px rgba(0,0,0,0.7);">
                <div style="position:absolute; top:-30px; left:-30px; width:240px; height:240px; background:radial-gradient(circle, rgba(157,78,221,0.18) 0%, transparent 70%); pointer-events:none;"></div>
                <div style="position:absolute; bottom:-40px; right:-40px; width:260px; height:260px; background:radial-gradient(circle, rgba(244,180,26,0.15) 0%, transparent 70%); pointer-events:none;"></div>
                
                <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px; flex-wrap:wrap;">
                    <span style="background:linear-gradient(135deg, rgba(157,78,221,0.25), rgba(0,240,255,0.15)); border:1px solid rgba(157,78,221,0.6); padding:4px 14px; border-radius:12px; font-size:0.85rem; font-weight:700; color:#d8b4fe;">الباب 19 — ديوان الأختام والزوهرية</span>
                    <span style="background:rgba(244,180,26,0.15); border:1px solid rgba(244,180,26,0.3); padding:4px 12px; border-radius:12px; font-size:0.82rem; color:var(--gold);"><i class="fa-solid fa-fingerprint"></i> الأختام السليمانية، علم الأسارير، والتشريح الطاقي</span>
                </div>
                
                <h1 style="font-family:'Amiri', serif; font-size:2.4rem; font-weight:700; color:#fff; margin-bottom:12px; line-height:1.3;">
                    ديوان الأختام الباطنية، علم الأسارير الكفية، والظاهرة الزوهرية
                </h1>
                <p style="color:#cbd5e1; font-size:1.02rem; line-height:1.8; max-width:1100px;">
                    دراسة أكاديمية استقصائية تجمع بين <strong>الهندسة الرمزية للأختام السليمانية والكوكبية</strong>، 
                    و<strong>موسوعة الأختام الكفية الثلاثين وعلم الأسارير</strong> مع خريطة تشريحية واضحة لعلامة 111 والخطوط، 
                    و<strong>أسرار مثلث الغزالي 3×3 ومحركه الحسابي التفاعلي</strong>، وتفكيك خرافات نبش الكنوز والأرصاد بميزان العقل والطب والشريعة.
                </p>
            </div>

            <!-- SUB-NAVIGATION BAR -->
            <div style="display:flex; gap:10px; overflow-x:auto; padding-bottom:12px; margin-bottom:28px; border-bottom:1px solid rgba(255,255,255,0.1);" id="seals-subnav-pills">
                <button class="seals-subnav-btn active" onclick="switchSealsSubView('seals-view-seven')">👑 خاتم سليمان الأعظم (الرموز السبعة)</button>
                <button class="seals-subnav-btn" onclick="switchSealsSubView('seals-view-ghazali')">📐 مثلث الغزالي وسر الأوفاق (3×3 بطد)</button>
                <button class="seals-subnav-btn" onclick="switchSealsSubView('seals-view-palm')">✋ أختام الكف الثلاثين وعلم الأسارير (خريطة 111)</button>
                <button class="seals-subnav-btn" onclick="switchSealsSubView('seals-view-planets')">🪐 أختام الكواكب السبعة (أغريبا وبيكاتريكس)</button>
                <button class="seals-subnav-btn" onclick="switchSealsSubView('seals-view-zouhri')">🧬 الملف الأنثروبولوجي للإنسان الزوهري</button>
                <button class="seals-subnav-btn" onclick="switchSealsSubView('seals-view-bloodlines')">🌌 السلالات الروحية وبذور النجوم</button>
                <button class="seals-subnav-btn" onclick="switchSealsSubView('seals-view-gallery')">🎨 معرض الرموز والطلاسم التفاعلي (SVG)</button>
            </div>

            <!-- SUB-VIEW 1: THE SEVEN SEALS OF SOLOMON -->
            <div id="seals-view-seven" class="seals-sub-container active">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(244,180,26,0.3); border-radius:20px; padding:28px 22px; margin-bottom:30px;">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                        <div>
                            <span style="color:var(--gold); font-size:0.85rem; font-weight:700;">📜 الأثر التاريخي والشفرة الكونية</span>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#fff; margin:4px 0 0 0;">خاتم السليماني الأعظم (الأسماء السبعة العظمى)</h2>
                        </div>
                        <span style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); color:var(--gold); padding:4px 12px; border-radius:10px; font-size:0.8rem;">فردٌ جبارٌ شكورٌ ثابتٌ ظهيرٌ خبيرٌ زكي</span>
                    </div>

                    <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin-bottom:24px;">
                        يعد <strong>الخاتم السليماني ذو الرموز السبعة</strong> أشهر الشفرات الرمزية في المخطوطات الهرمسية والإسلامية واليهودية الوسيطة. 
                        نُسب فك شفرته في التراث العربي إلى أمير المؤمنين علي بن أبي طالب في قصيدته المنظومة، كما شرحه البوني في <em>شمس المعارف الكبرى</em> 
                        وأبو حامد الغزالي في <em>المنقذ</em> و<em>الأوفاق</em>، وابن عربي في <em>الفتوحات المكية</em>.
                    </p>

                    <!-- THE POEM BOX -->
                    <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(244,180,26,0.3); border-radius:16px; padding:20px; margin-bottom:28px; text-align:center;">
                        <span style="color:var(--gold); font-size:0.82rem; font-weight:700; display:block; margin-bottom:10px;">أبيات الإمام علي بن أبي طالب في تفكيك رموز الخاتم السليماني:</span>
                        <div style="font-family:'Amiri', serif; font-size:1.15rem; color:#f8fafc; line-height:2.2; max-width:850px; margin:0 auto;">
                            ثَلاثُ عِصِيٍّ صُفِّفَتْ بَعْدَ خَاتَمٍ ❊ عَلَى رَأْسِهَا مِثْلُ السِّهَامِ تَقَوَّمُ<br>
                            وَمِيمٌ طَمِيسٌ أَبْتَرٌ ثُمَّ سُلَّمٌ ❊ إِلَى كُلِّ مَا تَرْجُوهُ بِالْخَيْرِ سُلَّمُ<br>
                            وَأَرْبَعَةٌ مِثْلُ الأَنَامِلِ صُفِّفَتْ ❊ تَلُوحُ بِهَا أَعْمَالُ سِرٍّ وَتُكْتَمُ<br>
                            وَهَاءٌ شَقِيقٌ ثُمَّ وَاوٌ مُقَوَّسٌ ❊ كَأُنْبُوبِ حَجَّامٍ مِنَ السِّرِّ أَلْوَى<br>
                            فَذَاكَ هُوَ الاسْمُ الْمُعَظَّمُ قَدْرُهُ ❊ وَإِنْ كُنْتَ يَوْماً جَاهِلاً فَتَعَلَّمُ
                        </div>
                    </div>

                    <!-- THE 7 SVG SYMBOLS GRID -->
                    <h3 style="font-family:'Amiri', serif; font-size:1.4rem; color:var(--cyan); margin-bottom:16px;">
                        <i class="fa-solid fa-shapes"></i> التفكيك الهندسي والرمزي للأشكال السبعة بالترتيب الأصيل:
                    </h3>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin-bottom:28px;">
                        
                        <!-- Symbol 1: The Star / Ring -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">1. الخاتم والنجمة (★)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك الشمس / فردٌ</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <polygon points="50,5 64,36 98,36 70,57 81,91 50,70 19,91 30,57 2,36 36,36" fill="none" stroke="#f4b41a" stroke-width="5"/>
                                    <circle cx="50" cy="50" r="14" fill="none" stroke="#00f0ff" stroke-width="3"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> نجمة خماسية أو مسدسة محاطة بهالة. ترمز لمركز الوعي وقطبية التوحيد والنفاذ الروحي الأكبر، وهي المفتاح الأول لدائرة الأختام.
                            </p>
                        </div>

                        <!-- Symbol 2: The Three Staffs -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">2. الثلاث عصي المقومة (lll)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك المريخ / جبارٌ (111)</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <line x1="28" y1="20" x2="28" y2="80" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <polygon points="28,10 20,25 36,25" fill="#f4b41a"/>
                                    <line x1="50" y1="20" x2="50" y2="80" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <polygon points="50,10 42,25 58,25" fill="#f4b41a"/>
                                    <line x1="72" y1="20" x2="72" y2="80" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <polygon points="72,10 64,25 80,25" fill="#f4b41a"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> ثلاثة أعمدة متوازية برؤوس حادة كالسهام. ترمز للسيادة على العوالم الثلاثة (الملك والملكوت والجبروت) والشهب الثاقبة.
                            </p>
                        </div>

                        <!-- Symbol 3: The Blind Meem -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">3. الميم الطميس الأبتر (م)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك المشتري / شكورٌ</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <circle cx="50" cy="50" r="28" fill="#f4b41a"/>
                                    <line x1="72" y1="50" x2="88" y2="70" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> ميم مغلقة الرأس (طمس) مقطوعة الذيل. ترمز للكتمان، وانطواء السر الإلهي في القلب، وجمع الوعي داخل الذات.
                            </p>
                        </div>

                        <!-- Symbol 4: The Ladder -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">4. السلم ذو الدرجتين (Ħ)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك الزهرة / ثابتٌ</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <line x1="30" y1="15" x2="30" y2="85" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <line x1="70" y1="15" x2="70" y2="85" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <line x1="30" y1="35" x2="70" y2="35" stroke="#06d6a0" stroke-width="6"/>
                                    <line x1="30" y1="65" x2="70" y2="65" stroke="#06d6a0" stroke-width="6"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> سُلَّم مكون من قائمين وعارضتين. يرمز لمرقاة المعراج الروحي، والتدرج في المراتب الصوفية من الأرض إلى السماوات العلا.
                            </p>
                        </div>

                        <!-- Symbol 5: The Four Fingers -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">5. الأربعة أصابع (Ш)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك عطارد / ظهيرٌ</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <line x1="20" y1="75" x2="80" y2="75" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <line x1="25" y1="30" x2="25" y2="75" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <line x1="42" y1="20" x2="42" y2="75" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <line x1="58" y1="20" x2="58" y2="75" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                    <line x1="75" y1="30" x2="75" y2="75" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> مشط أو أربعة خطوط عمودية على قاعدة واحدة بلا إبهام. ترمز للطبائع الأربعة (نار، هواء، ماء، تراب) وكتابة القدر في الألواح.
                            </p>
                        </div>

                        <!-- Symbol 6: The Split Haa -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">6. الهاء المشقوقة (ﮪ)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك القمر / خبيرٌ</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <path d="M 25 75 C 15 35, 45 20, 50 45 C 55 20, 85 35, 75 75 Z" fill="none" stroke="#f4b41a" stroke-width="6"/>
                                    <line x1="50" y1="45" x2="50" y2="75" stroke="#d8b4fe" stroke-width="4"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> حرف هاء يشبه حافر الفرس المشقوق من وسطه. يرمز لسر الهوية الأزلية (هو) وازدواجية النفس والروح، والنور المنبثق في الصدر.
                            </p>
                        </div>

                        <!-- Symbol 7: The Curved Waw -->
                        <div class="seal-glyph-card" style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
                                <span style="color:var(--gold); font-weight:700; font-size:0.85rem;">7. الواو المقوس (و)</span>
                                <span style="font-size:0.75rem; color:#94a3b8;">فلك زحل / زكيٌ</span>
                            </div>
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="70" height="70" viewBox="0 0 100 100">
                                    <circle cx="40" cy="35" r="16" fill="none" stroke="#f4b41a" stroke-width="6"/>
                                    <path d="M 56 35 C 75 45, 75 80, 25 80" fill="none" stroke="#f4b41a" stroke-width="6" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <p style="font-size:0.82rem; color:#cbd5e1; line-height:1.6; margin:0;">
                                <strong>الوصف:</strong> واو منحنية ومقوسة الرأس كأنبوب الحجامة. ترمز لحلقة الانتهاء التي ترتد إلى البداية (الأوربوروس / الإغلاق الختامي للحصن السليماني).
                            </p>
                        </div>

                    </div>
                </div>
            </div>

            <!-- SUB-VIEW: THE GHAZALI TRIANGLE (WAFQ 3x3) -->
            <div id="seals-view-ghazali" class="seals-sub-container" style="display:none;">
                <div style="background:rgba(13,19,36,0.95); border:1px solid rgba(244,180,26,0.4); border-radius:20px; padding:28px 22px; margin-bottom:30px; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                        <div>
                            <span style="color:var(--gold); font-size:0.85rem; font-weight:700;">📐 المخطوطات الهرمسية والرياضيات القديمة</span>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#fff; margin:4px 0 0 0;">مثلث الغزالي الشريف (المربع السحري 3×3 — شفرة بَطَدٍ زَهَجٍ وَاحٍ)</h2>
                        </div>
                        <span style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); color:var(--gold); padding:4px 12px; border-radius:10px; font-size:0.8rem;">سر العدد 15 — قطب التوازن 5</span>
                    </div>

                    <p style="color:#cbd5e1; font-size:0.94rem; line-height:1.8; margin-bottom:24px;">
                        يعد <strong>«مثلث الغزالي»</strong> (المربع السحري 3×3) أقدم الأوفاق الرياضية المكتشفة في تاريخ البشرية وأكثرها قداسة في التراث الهرمسي والإسلامي. 
                        عُرف في الصين القديمة باسم <em>لو شو (Luo Shu - 2800 ق.م)</em>، وترجمه علماء الرياضيات المسلمون (مثل ثابت بن قرة، إخوان الصفا، وأبو الوفاء البوزجاني)، 
                        ثم استشهد به حجة الإسلام <strong>أبو حامد الغزالي</strong> في مصنفاته كمثال عقلي على عجائب خواص التراكيب والأعداد.
                    </p>

                    <!-- SECTION 1: HISTORICAL DOCUMENTATION -->
                    <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(244,180,26,0.25); border-radius:14px; padding:20px; margin-bottom:22px; border-right:4px solid var(--gold);">
                        <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:var(--gold); margin-bottom:8px;">
                            📜 1. التوثيق التاريخي الصارم في مصنفات الإمام الغزالي
                        </h3>
                        <div style="color:#cbd5e1; font-size:0.88rem; line-height:1.8;">
                            • <strong>نص الغزالي في كتاب «المنقذ من الضلال»:</strong> استشهد الغزالي بالوفق المثلث صراحةً عندما كان يناقش أطباء عصره والفلاسفة حول حقيقة "خواص الأشياء"، قائلاً: 
                            <blockquote style="margin:10px 0; padding:10px 15px; background:rgba(244,180,26,0.08); border-right:3px solid var(--gold); font-family:'Amiri', serif; font-size:1.05rem; color:#f8fafc; font-style:italic;">
                                «وكذلك لو قيل لشخص: إذا نُقش في لوح جدول فيه تسعة أعداد، مجموع كل ضلع وقطر خمسة عشر، ووضع تحت امرأة تعسر ولادها خرج الولد سريعاً... لم يصدق به العقل لو لم يشاهده، ولأنكره لو لم يره بالتجربة».
                            </blockquote>
                            استخدم الغزالي هذا الوفق كبرهان إبستيمولوجي يثبت أن في الوجود أسراراً وتراكيب تدرك بالتجربة والرياضيات ولا يستقل العقل بإنكارها مجرداً.<br>
                            • <strong>كتاب «الأوفاق» المنسوب للغزالي:</strong> اختلف المؤرخون في نسبته؛ فمنهم من يثبت أنه من بواكير اشتغاله بعلوم الرياضيات وخواص الحروف قبل عزلته، ومنهم كابن تيمية والمحققين المعاصرين من يرى أن الكتاب جُمع ونُحل على الغزالي لاحقاً لترويج كتب الصنعة الحرفية باسمه لشهرته العلمية الفائقة.
                        </div>
                    </div>

                    <!-- SECTION 2: MATHEMATICAL ANATOMY -->
                    <h3 style="font-family:'Amiri', serif; font-size:1.4rem; color:var(--cyan); margin-bottom:14px;">
                        <i class="fa-solid fa-square-root-variable"></i> 2. التشريح الرياضي والجبري لشفرة (بَطَدٍ زَهَجٍ وَاحٍ)
                    </h3>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-bottom:28px;">
                        
                        <!-- Visual Matrix Card -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(0,240,255,0.25); border-radius:14px; padding:20px; text-align:center;">
                            <span style="color:var(--cyan); font-size:0.85rem; font-weight:700; display:block; margin-bottom:12px;">المصفوفة الطبيعية المتزنة (قاعدة 15)</span>
                            
                            <div style="display:inline-grid; grid-template-columns:repeat(3, 70px); grid-gap:8px; margin-bottom:14px; direction:ltr;">
                                <div style="background:rgba(244,180,26,0.2); border:2px solid var(--gold); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--gold);">4</div>
                                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--cyan);">9</div>
                                <div style="background:rgba(244,180,26,0.2); border:2px solid var(--gold); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--gold);">2</div>
                                
                                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--cyan);">3</div>
                                <div style="background:rgba(239,68,68,0.25); border:2px solid #ef4444; border-radius:8px; padding:15px; font-weight:900; font-size:1.5rem; color:#fff;">5</div>
                                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--cyan);">7</div>
                                
                                <div style="background:rgba(244,180,26,0.2); border:2px solid var(--gold); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--gold);">8</div>
                                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--cyan);">1</div>
                                <div style="background:rgba(244,180,26,0.2); border:2px solid var(--gold); border-radius:8px; padding:15px; font-weight:800; font-size:1.3rem; color:var(--gold);">6</div>
                            </div>

                            <div style="font-size:0.8rem; color:#94a3b8; line-height:1.6;">
                                <span style="color:var(--gold);">■ الأركان الزوجية (2, 4, 6, 8)</span>: الأوتاد الثابتة والطبائع.<br>
                                <span style="color:var(--cyan);">■ الأضلاع الفردية (1, 3, 7, 9)</span>: مسارات الحركة الكونية.<br>
                                <span style="color:#ef4444; font-weight:700;">■ المركز (5)</span>: قطب الاعتدال والمحور.
                            </div>
                        </div>

                        <!-- Mathematical Properties List -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.1); border-radius:14px; padding:20px;">
                            <strong style="color:var(--gold); font-size:1.05rem; display:block; margin-bottom:10px;">القوانين الرياضية الثمانية للوفق 3×3:</strong>
                            <ul style="color:#cbd5e1; font-size:0.85rem; line-height:1.8; margin:0; padding-right:18px;">
                                <li><strong>مجموع الأضلاع الثابت:</strong> أي صف أو عمود أو قطر = 15 (4+9+2 = 15، 3+5+7 = 15، 8+1+6 = 15).</li>
                                <li><strong>المساحة الإجمالية:</strong> مجموع الأرقام التسعة = 45، وهو بحساب الجمل مساوٍ لاسم <strong>«آدم»</strong> (أ=1 + د=4 + م=40).</li>
                                <li><strong>تناظر المركز:</strong> كل رقمين متقابلين عبر المركز مجموعهما 10، ونصفهما المركز 5 (4+6=10، 9+1=10، 2+8=10، 3+7=10).</li>
                                <li><strong>شفرة بطد زهج واح:</strong> لفظ تركيبي لحفظ مواقع الأعداد بحساب أبجد هوز: (ب=2، ط=9، د=4) / (ز=7، هـ=5، ج=3) / (و=6، ا=1، ح=8).</li>
                                <li><strong>قاعدة التعمير لأي عدد مطلوب (N):</strong> يُطرح أس المثلث (12)، ويُقسم الباقي على 3: K = (N - 12) / 3. ويدخل بالناتج K في بيت المفتاح (البيت 1)، ويزاد واحداً في كل بيت، فإن فضل كسر (1 أو 2) جُبر في بيت الكسر (البيت السابع أو الرابع).</li>
                            </ul>
                        </div>

                    </div>

                    <!-- SECTION 3: ESOTERIC CLAIMS VS RATIONAL REALITY -->
                    <div style="background:linear-gradient(135deg, rgba(30,27,75,0.95), rgba(15,23,42,0.98)); border:1px solid rgba(168,85,247,0.4); border-radius:18px; padding:24px; margin-bottom:26px;">
                        <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
                            <span style="font-size:1.6rem; color:#c084fc;">👁️</span>
                            <h3 style="font-family:'Amiri', serif; font-size:1.45rem; color:#d8b4fe; margin:0;">
                                3. ميزان الحقائق: تفكيك أسرار تفعيل البصيرة، كشف الدفائن ومكانها، وإزالة الأرصاد
                            </h3>
                        </div>

                        <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin-bottom:18px;">
                            حفلت مخطوطات السيمياء والتراث الحرفي المتأخر (مثل <em>شمس المعارف الكبرى</em>، <em>منبع أصول الحكمة</em>، ومصنفات <em>الأوفاق</em>) 
                            بنظريات مطولة تزعم أن لـ <strong>«مثلث الغزالي (وفق بطد زهج واح)»</strong> تصاريف باطنية ترتبط بكشف المغيبات وفك موانع الأرض. 
                            هنا نستعرض بدقة بالغة ما سطرته تلك المخطوطات بحرفها، مع وضع الميزان العلمي والأثري والعقلي الصارم أمامها:
                        </p>

                        <!-- DUAL COMPARISON GRID -->
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:18px; margin-bottom:18px;">
                            
                            <!-- Left: The Ancient Manuscript Claims -->
                            <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(244,180,26,0.3); border-radius:14px; padding:18px; border-right:4px solid var(--gold);">
                                <h4 style="color:var(--gold); font-size:1.1rem; margin-top:0; margin-bottom:10px;">
                                    📜 ما زعمته المخطوطات القديمة وكتب الصنعة:
                                </h4>
                                <ul style="color:#cbd5e1; font-size:0.85rem; line-height:1.8; margin:0; padding-right:18px;">
                                    <li><strong>زعم «تفعيل البصيرة وكشف الحجب»:</strong> ادعت المخطوطات أن نقش المثلث في شرف الشمس أو وقت تربيع المشتري مع الزهرة، وحمله مع رياضة حرفية وصيام، يفتح "العين الثالثة" (البصيرة الأثيرية) ويجعل حامله يستشعر الطاقات المخبوءة في الجماد.</li>
                                    <li><strong>زعم «الكشف عن مكان الكنز ودفائن الأرض»:</strong> زعمت كتب الأوفاق أن تقسيم بيوت المثلث وفق العناصر الأربعة (النار للشرق والأعلى، الهواء للجنوب، الماء للغرب والأسفل، التراب للشمال والعمق) يُستخدم عبر حساب أعداد اسم المكان لتحديد جهة ومقدار عمق الذهب المدفون.</li>
                                    <li><strong>زعم «إزالة الأرصاد وصرف عُمّار المكان»:</strong> ادعوا أن تلاوة أسماء أوتاد المثلث (بَطَدٍ زَهَجٍ وَاحٍ) تبطل "رصد الجن" الموكل بحراسة المغارات وتمنع تحول الذهب إلى فحم أو حجارة كما كان يُشاع في الفولكلور.</li>
                                </ul>
                            </div>

                            <!-- Right: The Scientific & Rational Reality -->
                            <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(0,240,255,0.3); border-radius:14px; padding:18px; border-right:4px solid var(--cyan);">
                                <h4 style="color:var(--cyan); font-size:1.1rem; margin-top:0; margin-bottom:10px;">
                                    🔬 الميزان العلمي، الأثري، والشرعي الحقيقي:
                                </h4>
                                <ul style="color:#cbd5e1; font-size:0.85rem; line-height:1.8; margin:0; padding-right:18px;">
                                    <li><strong>حقيقة «البصيرة» عند الإمام الغزالي:</strong> في مصنفاته الأصيلة المعتمدة (<em>مشكاة الأنوار</em> و<em>إحياء علوم الدين</em>)، يؤكد الغزالي أن البصيرة هي <strong>قوة إدراك عقلي وروحي شريف</strong>، تُنال بتطهير النفس من الرذائل، ورياضة الفكر بالبراهين الرياضية والمنطقية؛ وليست حاسة سحرية تُستجلب بالطلاسم والأشكال.</li>
                                    <li><strong>حقيقة الدفائن وعلم الآثار الحديث:</strong> الكنوز الأثرية (الفرعونية، الرومانية، الحميرية) دفنتها حضارات بشرية خضعت لدفن جنائزي أو تحصين عسكري. مفتاح الكشف عنها علمي بحت: تقنيات <strong>رادار اختراق الأرض (GPR)</strong>، و<strong>المسح الكهرومغناطيسي والمقاومية الكهربائية (ERT)</strong>، والمسح الجوي بالليزر <strong>(LiDAR)</strong>، وليس المربعات العددية.</li>
                                    <li><strong>أكذوبة «الرصد وحارس الكنز»:</strong> لا يوجد في صريح الدين ولا في التاريخ ما يثبت أن الجن يحرس ذهباً تحت الأرض، بل هي أسطورة ولدت لتبرير الوفيات الناتجة عن <strong>غازات المقابر السامة (الميثان وغاز الرادون)</strong> و<strong>الفخاخ المعمارية الميكانيكية</strong> (تساقط الصخور والرمال المتحركة).</li>
                                </ul>
                            </div>

                        </div>

                        <div style="background:rgba(244,180,26,0.08); border-radius:10px; padding:12px; font-size:0.84rem; color:#f8fafc; line-height:1.7;">
                            <strong>خلاصة التحقيق الأكاديمي:</strong> القيمة الحقيقية لـ «مثلث الغزالي» تكمن في كونه <strong>قمة العبقرية الرياضية والتجريد الهندسي القديم</strong>؛ حيث أظهر قدرة العقل البشري على صياغة مصفوفة توازن ثنائية الأبعاد تتطابق في كافة اتجاهاتها الرياضية، وهي اللبنة التأسيسية التي مهدت لاحقاً لنظريات الجبر الخطي والمصفوفات الحديثة في البرمجة والذكاء الاصطناعي.
                        </div>
                    </div>

                    <!-- SECTION 4: INTERACTIVE 3X3 GENERATOR -->
                    <div style="background:rgba(0,0,0,0.6); border:1px solid var(--emerald); border-radius:16px; padding:22px;">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
                            <h4 style="font-family:'Amiri', serif; font-size:1.25rem; color:var(--emerald); margin:0;">
                                🧮 المحرك التفاعلي لتعمير وفق الغزالي 3×3 (Live Wafq Calculator)
                            </h4>
                            <span style="font-size:0.78rem; color:#94a3b8;">معادلة الجبر والكسر الأكاديمية: (N - 12) / 3</span>
                        </div>
                        
                        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px; flex-wrap:wrap;">
                            <label style="color:#cbd5e1; font-size:0.85rem;">أدخل مجموع الضلع المطلوب (N يجب أن يكون 15 أو أكبر):</label>
                            <input type="number" id="ghazali-target-sum" value="15" min="15" max="99999" style="background:rgba(15,23,42,0.9); border:1px solid var(--gold); color:#fff; padding:6px 14px; border-radius:8px; font-weight:700; width:120px; font-size:1rem;">
                            <button type="button" onclick="computeLiveGhazaliWafq()" style="background:linear-gradient(135deg, var(--gold), #b45309); border:none; color:#000; font-weight:700; padding:8px 18px; border-radius:8px; cursor:pointer; font-size:0.88rem;">حساب وتعمير الوفق</button>
                        </div>

                        <div id="ghazali-calc-result" style="text-align:center; padding:15px; background:rgba(0,0,0,0.4); border-radius:12px;">
                            <!-- Populated by JS -->
                        </div>
                    </div>

                </div>
            </div>

            <!-- SUB-VIEW: ESOTERIC PALM SEALS & CHIROMANCY -->
            <div id="seals-view-palm" class="seals-sub-container" style="display:none;">
                <div style="background:rgba(13,19,36,0.95); border:1px solid rgba(0,240,255,0.35); border-radius:20px; padding:28px 22px; margin-bottom:30px; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                        <div>
                            <span style="color:var(--cyan); font-size:0.85rem; font-weight:700;">✋ التشريح الرمزي والفراسة المخطوطية</span>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#fff; margin:4px 0 0 0;">الموسوعة الشاملة للأختام الكفية الثلاثين وعلم الأسارير (Chiromancy Codex)</h2>
                        </div>
                        <span style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); color:var(--cyan); padding:4px 12px; border-radius:10px; font-size:0.8rem;">30 ختماً موثقاً — خريطة 111 والتلال</span>
                    </div>

                    <p style="color:#cbd5e1; font-size:0.94rem; line-height:1.8; margin-bottom:24px;">
                        يُعد <strong>«علم الأسارير» (قراءة خطوط الكف - Chiromancy / Cheiromancy)</strong> من أقدم الفنون الفراسية التراثية. 
                        اعتبرت المدارس الفلسفية القديمة (من أبقراط وأرسطو إلى فخر الدين الرازي وابن عربي) أن راحة كف الإنسان هي 
                        <em>«لوح محفوظ مصغر» (Microcosmic Tablet)</em> طُبعت عليه انعكاسات قوى الأفلاك وأمزجة الأعضاء الداخلية.
                    </p>

                    <!-- SECTION 1: THE 7 PLANETARY MOUNTS OF THE PALM -->
                    <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(0,240,255,0.25); border-radius:14px; padding:20px; margin-bottom:22px; border-right:4px solid var(--cyan);">
                        <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:var(--cyan); margin-bottom:10px;">
                            🌌 1. التناظر الميلوثيسي: تلال الكواكب السبعة على راحة اليد
                        </h3>
                        <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.8; margin-bottom:12px;">
                            في الفراسة الميلوثيسية (Melothesia)، لا تُقرأ خطوط الكف بمعزل عن تضاريس اليد، بل تقسم راحة اليد إلى سبع مناطق تسمى "تلال الكواكب" تحكم الطاقات الحيوية:
                        </p>
                        
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:14px;">
                            <div style="background:rgba(0,0,0,0.5); padding:12px; border-radius:10px; border-left:3px solid var(--gold);">
                                <strong style="color:var(--gold); font-size:0.9rem;">♃ تل المشتري (Mount of Jupiter):</strong>
                                <span style="font-size:0.82rem; color:#cbd5e1; display:block;">يقع عند قاعدة السبابة؛ يرمز للهيبة، القيادة، الطموح الروحي، وعزة النفس.</span>
                            </div>
                            <div style="background:rgba(0,0,0,0.5); padding:12px; border-radius:10px; border-left:3px solid #94a3b8;">
                                <strong style="color:#94a3b8; font-size:0.9rem;">♄ تل زحل (Mount of Saturn):</strong>
                                <span style="font-size:0.82rem; color:#cbd5e1; display:block;">يقع عند قاعدة الإصبع الأوسط؛ يرمز للحكمة العميقة، الصبر، الميل للعزلة، والتأمل الباطني.</span>
                            </div>
                            <div style="background:rgba(0,0,0,0.5); padding:12px; border-radius:10px; border-left:3px solid var(--gold);">
                                <strong style="color:var(--gold); font-size:0.9rem;">☉ تل الشمس (Mount of Apollo / Sun):</strong>
                                <span style="font-size:0.82rem; color:#cbd5e1; display:block;">يقع عند قاعدة البنصر؛ يرمز للإشراق، الشهرة، الإبداع الفني، والبريق الوجداني.</span>
                            </div>
                            <div style="background:rgba(0,0,0,0.5); padding:12px; border-radius:10px; border-left:3px solid var(--cyan);">
                                <strong style="color:var(--cyan); font-size:0.9rem;">☿ تل عطارد (Mount of Mercury):</strong>
                                <span style="font-size:0.82rem; color:#cbd5e1; display:block;">يقع عند قاعدة الخنصر؛ يرمز للذكاء اللماح، الفصاحة والبلاغة، والحساب والمعاملات.</span>
                            </div>
                            <div style="background:rgba(0,0,0,0.5); padding:12px; border-radius:10px; border-left:3px solid var(--emerald);">
                                <strong style="color:var(--emerald); font-size:0.9rem;">♀ تل الزهرة (Mount of Venus):</strong>
                                <span style="font-size:0.82rem; color:#cbd5e1; display:block;">يشمل قاعدة الإبهام المنتفخة؛ يرمز للحيوية الجسدية، قوة العاطفة، والحرارة الفطرية.</span>
                            </div>
                            <div style="background:rgba(0,0,0,0.5); padding:12px; border-radius:10px; border-left:3px solid #60a5fa;">
                                <strong style="color:#60a5fa; font-size:0.9rem;">☽ تل القمر (Mount of Moon):</strong>
                                <span style="font-size:0.82rem; color:#cbd5e1; display:block;">يقع في أسفل الحافة الخارجية للكف؛ يرمز للحدس الباطني، الخيال، والأحلام الكاشفة.</span>
                            </div>
                        </div>
                    </div>


                    <!-- MASTER ANATOMICAL & ESOTERIC PALM ATLAS (CLEAR HIGH-RES SVG) -->
                    <div style="background:linear-gradient(135deg, rgba(8,14,30,0.95), rgba(4,8,20,0.98)); border:1px solid rgba(0,240,255,0.3); border-radius:18px; padding:25px; margin-bottom:30px; box-shadow:0 10px 35px rgba(0,0,0,0.6);">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                            <div>
                                <span style="color:var(--cyan); font-size:0.85rem; font-weight:700;"><i class="fa-solid fa-map-location-dot"></i> الخريطة البصرية الموحدة</span>
                                <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:#fff; margin:4px 0 0 0;">أطلس تشريح كف اليد التفاعلي: التلال، الخطوط الكبرى، وعلامة 111</h3>
                            </div>
                            <span style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); color:var(--cyan); padding:4px 12px; border-radius:10px; font-size:0.8rem;">دليل التمييز والفراسة البصرية</span>
                        </div>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:25px; align-items:center;">
                            
                            <!-- Left: Large Detailed SVG Diagram -->
                            <div style="text-align:center; padding:15px; background:rgba(0,0,0,0.5); border-radius:16px; border:1px solid rgba(255,255,255,0.06);">
                                <svg viewBox="0 0 520 620" width="100%" style="max-width:480px; height:auto; filter:drop-shadow(0 0 15px rgba(0,240,255,0.15));">
                                    <defs>
                                        <radialGradient id="mountGlowJupiter" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stop-color="#f4b41a" stop-opacity="0.35"/>
                                            <stop offset="100%" stop-color="#f4b41a" stop-opacity="0"/>
                                        </radialGradient>
                                        <radialGradient id="mountGlowSaturn" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stop-color="#94a3b8" stop-opacity="0.35"/>
                                            <stop offset="100%" stop-color="#94a3b8" stop-opacity="0"/>
                                        </radialGradient>
                                        <radialGradient id="mountGlowSun" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.35"/>
                                            <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
                                        </radialGradient>
                                        <radialGradient id="mountGlowMercury" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.35"/>
                                            <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
                                        </radialGradient>
                                        <radialGradient id="mountGlowVenus" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stop-color="#06d6a0" stop-opacity="0.3"/>
                                            <stop offset="100%" stop-color="#06d6a0" stop-opacity="0"/>
                                        </radialGradient>
                                        <radialGradient id="mountGlowMoon" cx="50%" cy="50%" r="50%">
                                            <stop offset="0%" stop-color="#60a5fa" stop-opacity="0.35"/>
                                            <stop offset="100%" stop-color="#60a5fa" stop-opacity="0"/>
                                        </radialGradient>
                                    </defs>

                                    <!-- Hand Contour Outline -->
                                    <path d="M 170 580 
                                             C 120 570, 70 510, 60 410 
                                             C 50 350, 40 310, 30 290 
                                             C 15 260, 45 220, 80 240 
                                             C 110 260, 140 290, 155 310 
                                             C 150 260, 155 160, 160 120 
                                             C 165 90, 195 90, 205 120 
                                             C 215 160, 225 210, 225 240 
                                             C 230 190, 240 100, 250 60 
                                             C 255 35, 285 35, 295 60 
                                             C 305 110, 310 190, 310 240 
                                             C 320 200, 335 120, 345 95 
                                             C 355 70, 385 75, 390 100 
                                             C 395 140, 395 210, 390 260 
                                             C 400 230, 420 180, 435 165 
                                             C 450 150, 475 165, 470 190 
                                             C 460 250, 440 330, 430 380 
                                             C 415 470, 390 560, 350 580 Z" 
                                          fill="rgba(15,23,42,0.7)" stroke="rgba(0,240,255,0.4)" stroke-width="2.5"/>

                                    <!-- MOUNT GLOW AREAS -->
                                    <!-- Jupiter (Index base) -->
                                    <circle cx="185" cy="285" r="38" fill="url(#mountGlowJupiter)"/>
                                    <!-- Saturn (Middle base) -->
                                    <circle cx="270" cy="265" r="38" fill="url(#mountGlowSaturn)"/>
                                    <!-- Sun / Apollo (Ring base) -->
                                    <circle cx="355" cy="275" r="38" fill="url(#mountGlowSun)"/>
                                    <!-- Mercury (Little base) -->
                                    <circle cx="430" cy="315" r="34" fill="url(#mountGlowMercury)"/>
                                    <!-- Venus (Thumb root) -->
                                    <circle cx="150" cy="420" r="58" fill="url(#mountGlowVenus)"/>
                                    <!-- Moon (Lower outer edge) -->
                                    <circle cx="365" cy="470" r="55" fill="url(#mountGlowMoon)"/>
                                    <!-- Plain of Mars (Center) -->
                                    <circle cx="265" cy="385" r="42" fill="rgba(239,68,68,0.12)"/>

                                    <!-- MOUNT LABELS WITH PLANET ICONS -->
                                    <text x="185" y="275" fill="#f4b41a" font-size="12" font-weight="700" text-anchor="middle">♃ تل المشتري</text>
                                    <text x="185" y="290" fill="#cbd5e1" font-size="9" text-anchor="middle">الهيبة والرياسة</text>

                                    <text x="270" y="255" fill="#94a3b8" font-size="12" font-weight="700" text-anchor="middle">♄ تل زحل</text>
                                    <text x="270" y="270" fill="#cbd5e1" font-size="9" text-anchor="middle">الحكمة والزهد</text>

                                    <text x="355" y="265" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">☉ تل الشمس</text>
                                    <text x="355" y="280" fill="#cbd5e1" font-size="9" text-anchor="middle">المجد والإشراق</text>

                                    <text x="430" y="305" fill="#00f0ff" font-size="11" font-weight="700" text-anchor="middle">☿ تل عطارد</text>
                                    <text x="430" y="320" fill="#cbd5e1" font-size="9" text-anchor="middle">الذكاء والفصاحة</text>

                                    <text x="150" y="415" fill="#06d6a0" font-size="13" font-weight="700" text-anchor="middle">♀ تل الزهرة</text>
                                    <text x="150" y="432" fill="#cbd5e1" font-size="9.5" text-anchor="middle">الحيوية والعاطفة</text>

                                    <text x="365" y="465" fill="#60a5fa" font-size="13" font-weight="700" text-anchor="middle">☽ تل القمر</text>
                                    <text x="365" y="482" fill="#cbd5e1" font-size="9.5" text-anchor="middle">الحدس والخيال</text>

                                    <text x="265" y="385" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">♂ سهل المريخ</text>
                                    <text x="265" y="400" fill="#cbd5e1" font-size="9" text-anchor="middle">الشجاعة والثبات</text>

                                    <!-- MAJOR LINES -->
                                    <!-- 1. Heart Line (Pink/Purple) -->
                                    <path d="M 435 345 C 380 330, 270 330, 205 305" fill="none" stroke="#ec4899" stroke-width="4.5" stroke-linecap="round"/>
                                    <!-- 2. Head Line (Cyan) -->
                                    <path d="M 160 325 C 220 340, 310 370, 360 415" fill="none" stroke="#00f0ff" stroke-width="4" stroke-linecap="round"/>
                                    <!-- 3. Life Line (Emerald) -->
                                    <path d="M 160 325 C 190 350, 215 410, 190 535" fill="none" stroke="#06d6a0" stroke-width="4.5" stroke-linecap="round"/>
                                    <!-- 4. Fate Line (Gold dashed) -->
                                    <path d="M 265 550 L 268 285" fill="none" stroke="#f4b41a" stroke-width="3" stroke-dasharray="6,4" stroke-linecap="round"/>

                                    <!-- SPECIAL SACRED SEALS HIGHLIGHTS -->
                                    <!-- 111 / Three Staffs Marking under Sun & Jupiter -->
                                    <g transform="translate(340, 215)">
                                        <line x1="0" y1="0" x2="0" y2="28" stroke="#f4b41a" stroke-width="3.5" stroke-linecap="round"/>
                                        <polygon points="0,-4 -4,4 4,4" fill="#f4b41a"/>
                                        <line x1="12" y1="0" x2="12" y2="28" stroke="#f4b41a" stroke-width="3.5" stroke-linecap="round"/>
                                        <polygon points="12,-4 8,4 16,4" fill="#f4b41a"/>
                                        <line x1="24" y1="0" x2="24" y2="28" stroke="#f4b41a" stroke-width="3.5" stroke-linecap="round"/>
                                        <polygon points="24,-4 20,4 28,4" fill="#f4b41a"/>
                                        <rect x="-10" y="-12" width="44" height="48" fill="none" stroke="#f4b41a" stroke-width="1.2" stroke-dasharray="2,2"/>
                                    </g>
                                    <text x="352" y="198" fill="#f4b41a" font-size="11" font-weight="900" text-anchor="middle">ختم 111 (الثلاث عصي)</text>

                                    <!-- Simian Line indicator (Alternative Straight Gold Bar) -->
                                    <line x1="165" y1="330" x2="435" y2="330" stroke="#f4b41a" stroke-width="2.5" stroke-dasharray="5,3"/>
                                    <text x="300" y="323" fill="#f4b41a" font-size="9.5" font-weight="700" text-anchor="middle">مسار الخط القاطع (Simian Line)</text>

                                    <!-- The Mystic Cross between lines -->
                                    <line x1="260" y1="340" x2="274" y2="354" stroke="#d8b4fe" stroke-width="3.5" stroke-linecap="round"/>
                                    <line x1="274" y1="340" x2="260" y2="354" stroke="#d8b4fe" stroke-width="3.5" stroke-linecap="round"/>
                                    <text x="267" y="367" fill="#d8b4fe" font-size="9" font-weight="700" text-anchor="middle">الصليب الخفي</text>

                                    <!-- Eye of Buddha on Thumb -->
                                    <g transform="translate(62, 230)">
                                        <path d="M 0 0 Q 15 -10 30 0 Q 15 10 0 0 Z" fill="rgba(0,240,255,0.2)" stroke="#00f0ff" stroke-width="2.5"/>
                                        <circle cx="15" cy="0" r="3" fill="#f4b41a"/>
                                    </g>
                                    <text x="77" y="215" fill="#00f0ff" font-size="9.5" font-weight="700" text-anchor="middle">عين الصقر (يافا ريخا)</text>

                                    <!-- Ring of Solomon on Index -->
                                    <path d="M 165 295 C 175 310, 195 310, 205 295" fill="none" stroke="#06d6a0" stroke-width="3"/>
                                    <text x="185" y="320" fill="#06d6a0" font-size="9" font-weight="700" text-anchor="middle">خاتم سليمان</text>

                                    <!-- Wrist Rascettes -->
                                    <path d="M 185 570 Q 260 560 335 570" fill="none" stroke="#f4b41a" stroke-width="2.5"/>
                                    <path d="M 190 580 Q 260 570 330 580" fill="none" stroke="#f4b41a" stroke-width="2"/>
                                    <path d="M 195 590 Q 260 580 325 590" fill="none" stroke="#f4b41a" stroke-width="1.5"/>
                                    <text x="260" y="605" fill="#f4b41a" font-size="10" font-weight="700" text-anchor="middle">أساور الرسغ الملكية (Rascettes)</text>
                                </svg>
                            </div>

                            <!-- Right: Legend and Clear Key Guide -->
                            <div>
                                <h4 style="color:var(--gold); font-size:1.15rem; margin-top:0; margin-bottom:12px;">
                                    🔑 مفتاح قراءة الخريطة وتمييز العلامات والأختام:
                                </h4>
                                
                                <div style="display:flex; flex-direction:column; gap:10px; font-size:0.86rem; color:#cbd5e1;">
                                    <div style="background:rgba(244,180,26,0.1); border-right:3px solid var(--gold); padding:8px 12px; border-radius:6px;">
                                        <strong style="color:var(--gold);">⚡ ختم 111 (الثلاثة عصي والسهام):</strong>
                                        <span style="display:block; font-size:0.8rem; margin-top:2px;">يقع تحت تل الشمس أو المشتري؛ وهو شفرة عددية تعادل اسم الشمس الروحاني (ناخيئيل = 111) وترمز في المخطوطات لنفاذ الإرادة كالسهم الحارق.</span>
                                    </div>
                                    <div style="background:rgba(236,72,153,0.1); border-right:3px solid #ec4899; padding:8px 12px; border-radius:6px;">
                                        <strong style="color:#ec4899;">💖 خط القلب (Heart Line):</strong>
                                        <span style="display:block; font-size:0.8rem; margin-top:2px;">ينطلق من تحت الخنصر عابراً نحو السبابة؛ يحكم المشاعر، العواطف، والتفاعل الوجداني.</span>
                                    </div>
                                    <div style="background:rgba(0,240,255,0.1); border-right:3px solid var(--cyan); padding:8px 12px; border-radius:6px;">
                                        <strong style="color:var(--cyan);">🧠 خط الرأس (Head Line):</strong>
                                        <span style="display:block; font-size:0.8rem; margin-top:2px;">يمتد وسط الكف؛ يحكم الفكر، المنطق، سرعة الاستيعاب، والتركيز العقلي.</span>
                                    </div>
                                    <div style="background:rgba(244,180,26,0.1); border-right:3px solid var(--gold); padding:8px 12px; border-radius:6px;">
                                        <strong style="color:var(--gold);">👑 الخط القاطع (Simian Line):</strong>
                                        <span style="display:block; font-size:0.8rem; margin-top:2px;">اندماج خطي القلب والرأس في خط واحد أفقي تـام يقسم الكف؛ وهو العلامة الأبرز المنسوبة للإنسان الزوهري في الفولكلور.</span>
                                    </div>
                                    <div style="background:rgba(6,214,160,0.1); border-right:3px solid var(--emerald); padding:8px 12px; border-radius:6px;">
                                        <strong style="color:var(--emerald);">🌿 خط الحياة (Life Line):</strong>
                                        <span style="display:block; font-size:0.8rem; margin-top:2px;">يطوق تل الزهرة؛ يعكس الحيوية البيولوجية، طاقة الجسد، ومناعة البدن.</span>
                                    </div>
                                    <div style="background:rgba(216,180,254,0.1); border-right:3px solid #d8b4fe; padding:8px 12px; border-radius:6px;">
                                        <strong style="color:#d8b4fe;">✨ الصليب الخفي وعين الصقر:</strong>
                                        <span style="display:block; font-size:0.8rem; margin-top:2px;">الصليب بين خطي القلب والرأس يرمز للحدس الباطني؛ وعين الصقر على مفصل الإبهام تدل على الرؤى الصادقة.</span>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>


                    <!-- SECTION 2: THE 30 MAJOR PALM SEALS -->
                    <div style="margin-bottom:20px;">
                        <span style="color:var(--gold); font-size:0.85rem; font-weight:700;"><i class="fa-solid fa-gem"></i> الموسوعة المخطوطية الشاملة</span>
                        <h3 style="font-family:'Amiri', serif; font-size:1.6rem; color:#fff; margin:4px 0 14px 0;">
                            الأختام الكفية الثلاثون (30) وعلامات الفراسة واليد الزوهرية في المخطوطات القديمة
                        </h3>
                        <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.8;">
                            هنا نستعرض تفصيلاً دقيقاً لكل ختم وعلامة كما وردت في أمهات كتب الفراسة والأسارير القديمة (الرازي، سامودريكا شاسترا، مخطوطات الأندلس، وكتابات السيمياء)، مقرونة بالتشريح الطبي الحقيقي:
                        </p>
                    </div>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-bottom:30px;">

                        <!-- Seal 1: ختم الخط القاطع الملكي (Simian Line) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">1. ختم الخط القاطع الملكي (Simian Line)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">الخط المستعرض التام</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="26" y1="48" x2="114" y2="48" stroke="#f4b41a" stroke-width="4" stroke-linecap="round"/><circle cx="70" cy="48" r="4" fill="#00f0ff"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط عرضي وحيد متصل ومستقيم يقطع راحة الكف أفقياً من حافة إلى حافة دون انقطاع نتيجة اندماج خط القلب مع خط الرأس. سمي في كتب الصنعة 'السيف القاطع' واعتبر دليلاً على إرادة حديدية لا تتشتت ومفتاحاً لفتح المغلقات.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> طفرة جنينية تشريحية حميدة (Single Palmar Crease) تصيب 1.5% إلى 2% من عموم البشر الأصحاء ناتجة عن انثناء كف الجنين في الرحم، ولا علاقة لها بأي بعد غيبي.</p>
                            </div>
                        </div>

                        <!-- Seal 2: ختم الثلاث عصي والسهام (علامة 111) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">2. ختم الثلاث عصي والسهام (علامة 111)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">سر الرقم 111 / ناخيئيل</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="50" y1="20" x2="50" y2="70" stroke="#f4b41a" stroke-width="3"/><polygon points="50,15 46,24 54,24" fill="#f4b41a"/><line x1="70" y1="20" x2="70" y2="70" stroke="#f4b41a" stroke-width="3"/><polygon points="70,15 66,24 74,24" fill="#f4b41a"/><line x1="90" y1="20" x2="90" y2="70" stroke="#f4b41a" stroke-width="3"/><polygon points="90,15 86,24 94,24" fill="#f4b41a"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">ثلاثة خطوط عمودية متوازية يعلو كلاً منها رأس سهم، وهي المنظومة في البيت: 'ثَلاثُ عِصِيٍّ صُفِّفَتْ بَعْدَ خَاتَمٍ ❊ عَلَى رَأْسِهَا مِثْلُ السِّهَامِ تَقَوَّمُ'. تمثل القوة الثلاثية للروح والنفوذ، وقيمتها العددية بحساب الجمل (111) تطابق قطب الشمس 'ناخيئيل' وسر إشراق البصيرة.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> حزمة خطوط عمودية شائعة تحت تل الشمس أو المشتري تنشأ عن مرونة الأنسجة الضامة للأوتار الباسطة.</p>
                            </div>
                        </div>

                        <!-- Seal 3: النجمة السداسية الكفية (The Hexagram) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">3. النجمة السداسية الكفية (The Hexagram)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">خاتم داود الكفي</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <polygon points="70,25 82,46 58,46" fill="none" stroke="#f4b41a" stroke-width="2.5"/><polygon points="70,53 82,32 58,32" fill="none" stroke="#00f0ff" stroke-width="2.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">تقاطع مثلثين متطابقين متداخلين يشكلان نجمة سداسية متقنة في سهل المريخ أو تل المشتري. ترمز لأعلى درجات الحصانة الروحية والاتصال المزدوج بين العوالم العلوية والسفلية (As Above, So Below).</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تقاطع تشريحي نادر لخطوط ثانوية سطحية على أدمة الكف ناتج عن تشابك الأوتار العضلية السطحية.</p>
                            </div>
                        </div>

                        <!-- Seal 4: النجمة الخماسية النورانية (The Pentagram) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">4. النجمة الخماسية النورانية (The Pentagram)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">نجمة الروح والعناصر</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <polygon points="70,20 76,38 95,38 80,50 86,68 70,56 54,68 60,50 45,38 64,38" fill="none" stroke="#f4b41a" stroke-width="2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">نجمة خماسية تتشكل من خمسة خطوط دقيقة متقاطعة على تل المشتري أو زحل. ترمز في الفراسة لسيادة العقل والروح على العناصر الأربعة (النار، الهواء، الماء، التراب) وحضور الحكمة القيادية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تقاطع خطوط الشد في طبقة الأدمة عند التقاء الحركات الدورانية لإصبع السبابة.</p>
                            </div>
                        </div>

                        <!-- Seal 5: مثلث الحكمة الباطنية (The Mystic Triangle) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">5. مثلث الحكمة الباطنية (The Mystic Triangle)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">مثلث سهل المريخ</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <polygon points="45,45 85,38 65,70" fill="rgba(0,240,255,0.2)" stroke="#00f0ff" stroke-width="2.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">مثلث مغلق الأضلاع تماماً في وسط راحة اليد يتشكل من تقاطع خط الرأس (الفكر) وخط الحياة (الجسد) وخط الحدس/الكبد. سمي في المخطوطات 'عين الحكمة' ودل على الفطنة الحادة والبديهة الحاضرة.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> التقاء تشريحي طبيعي لثلاث طيات حركية رئيسية للكف تعكس عمق الحركات اليدوية المنسقة وتطور الأوتار.</p>
                            </div>
                        </div>

                        <!-- Seal 6: صليب الحدس الخفي (La Croix Mystique) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">6. صليب الحدس الخفي (La Croix Mystique)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">صليب ما بين السطرين</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 35 35 Q 70 42 105 32" fill="none" stroke="#64748b" stroke-width="1.5"/><path d="M 35 55 Q 70 52 105 60" fill="none" stroke="#64748b" stroke-width="1.5"/><line x1="65" y1="42" x2="75" y2="52" stroke="#d8b4fe" stroke-width="3" stroke-linecap="round"/><line x1="75" y1="42" x2="65" y2="52" stroke="#d8b4fe" stroke-width="3" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">علامة تقاطع مستقلة (+ أو ×) تتوسط الفراغ الموجود بين خط القلب وخط الرأس دون أن تمس أياً منهما. تعتبر أشهر علامة في قراءة الكف تدل على الموهبة الاستشعارية والإلهام الميتافيزيقي وحب الغوامض.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تقاطع ألياف نسيجية سطحية نتيجة حركات طي أصابع اليد المستمرة.</p>
                            </div>
                        </div>

                        <!-- Seal 7: شبكة الأسارير والمربعات (Palmar Grille) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">7. شبكة الأسارير والمربعات (Palmar Grille)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">تل القمر والزهرة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="85" y1="50" x2="85" y2="75" stroke="#f4b41a" stroke-width="2"/><line x1="95" y1="50" x2="95" y2="75" stroke="#f4b41a" stroke-width="2"/><line x1="78" y1="58" x2="102" y2="58" stroke="#f4b41a" stroke-width="2"/><line x1="78" y1="68" x2="102" y2="68" stroke="#f4b41a" stroke-width="2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">شبكة خطوط متقاطعة أفقياً وعمودياً تشبه المربعات في تل القمر أو تل الزهرة. نسبت لها كتب الفولكلور استشعار المياه الجوفية والمعادن في باطن الأرض وخبايا التيارات الأثيرية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> مرونة طبيعية في النسيج الضام لأدمة الجلد وانقباض راحة اليد عند الإمساك بالأشياء.</p>
                            </div>
                        </div>

                        <!-- Seal 8: خاتم سليمان الكفي (Ring of Solomon) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">8. خاتم سليمان الكفي (Ring of Solomon)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">هلال تل المشتري</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 33 30 C 40 38, 50 38, 55 28" fill="none" stroke="#06d6a0" stroke-width="3"/><circle cx="44" cy="33" r="3" fill="#f4b41a"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">قوس نصف دائري يحيط بقاعدة السبابة على تل المشتري. دل في كتب الفراسة على الحكمة الفطرية، والقدرة على التدريس والوعظ والتأثير الروحي على الناس بهدوء واقتدار.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية جلدية ناتجة عن حركة المفصل السنعي السلامي لإصبع السبابة.</p>
                            </div>
                        </div>

                        <!-- Seal 9: صليب النجاة والظفر (St. Andrew’s Cross) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">9. صليب النجاة والظفر (St. Andrew’s Cross)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">أسفل خط الحياة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="45" y1="65" x2="60" y2="80" stroke="#10b981" stroke-width="3" stroke-linecap="round"/><line x1="60" y1="65" x2="45" y2="80" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">تقاطع مائل على شكل حرف (X) يقع بمحاذاة خط الحياة قرب المعصم. اعتبر في الفراسة القديمة علامة 'الحصانة من المهالك والحوادث الخطيرة'، والنجاة المتكررة من الشدائد بألطاف خفية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تقاطع طيات الشد الجلدية عند قاعدة الإبهام والراحة الرسغية.</p>
                            </div>
                        </div>

                        <!-- Seal 10: المربع الحصين (The Protective Square) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">10. المربع الحصين (The Protective Square)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">درع خط الحياة والمصير</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <rect x="52" y="45" width="26" height="26" fill="rgba(244,180,26,0.15)" stroke="#f4b41a" stroke-width="2"/><line x1="65" y1="35" x2="65" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">مربع مغلق يتشكل حول انقطاع أو كسر في خط الحياة أو خط الرأس. يرمز في التراث للحماية الإلهية الفائقة التي تمنع وقوع أثر الصدمات أو الأمراض، ويدل على الحصانة وتجدد العافية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تراكب طيتين جلديتين فوق بعضهما أثناء التئام حركة نمو الأنسجة اليدوية.</p>
                            </div>
                        </div>

                        <!-- Seal 11: عين الصقر وبصيرة الإبهام (Yavarekha) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">11. عين الصقر وبصيرة الإبهام (Yavarekha)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">حبة القمح / يافا ريخا</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 22 55 Q 32 45 42 55 Q 32 65 22 55 Z" fill="none" stroke="#00f0ff" stroke-width="2.5"/><circle cx="32" cy="55" r="3" fill="#f4b41a"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خطان مقوسان يلتقيان عند الطرفين مشكلين حبة قمح أو عيناً بشرية مغلقة عند مفصل الإبهام الأول. تُسمى 'عين البصيرة'؛ تدل على صدق الرؤى والمنامات، والحاسة السادسة الفطرية التي تلتقط الأمور قبل وقوعها.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية جلدية حلقية بيضاوية حول المفصل السنعي لإبهام اليد ناتجة عن حركة الثني المحورية للإبهام.</p>
                            </div>
                        </div>

                        <!-- Seal 12: علامة السمكة والحوت (The Fish Sign) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">12. علامة السمكة والحوت (The Fish Sign)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">رمز الفيض والبركة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 45 68 Q 55 62 65 72 Q 55 82 45 76 Z" fill="none" stroke="#06d6a0" stroke-width="2.5"/><line x1="65" y1="72" x2="75" y2="65" stroke="#06d6a0" stroke-width="2"/><line x1="65" y1="72" x2="75" y2="79" stroke="#06d6a0" stroke-width="2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خطان منحنيان يتقاطعان مشكلين جسماً وذيلاً يشبهان السمكة عند قاعدة خط الحياة قرب الرسغ. ترمز للبركة الأزلية، النجاة من المهالك المائية، والغنى المعرفي والروحي المفاجئ بعد تعب.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تشعب انقسامي في الثنية الرسغية السفلية عند تلاقيها مع خط الحياة.</p>
                            </div>
                        </div>

                        <!-- Seal 13: رمح ثلاثي الشعب والتاج (The Trident) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">13. رمح ثلاثي الشعب والتاج (The Trident)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">تريشولا / تاج المصير</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="68" y1="45" x2="68" y2="20" stroke="#d8b4fe" stroke-width="3"/><path d="M 56 26 Q 68 36 68 36 Q 68 36 80 26" fill="none" stroke="#d8b4fe" stroke-width="2.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">تشعب خط المصير أو خط الشمس في نهايته إلى ثلاثة فروع رمحية تصعد نحو تلال المشتري وزحل والشمس. ترمز للمجد والسيادة واجتماع الحكمة (زحل) مع الهيبة (المشتري) والتألق الإبداعي (الشمس).</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تشعب طبيعي في تفرعات الألياف العصبية عند قاعدة الأصابع.</p>
                            </div>
                        </div>

                        <!-- Seal 14: علامة شجرة الحياة (The Tree Sign) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">14. علامة شجرة الحياة (The Tree Sign)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">الأغصان الصاعدة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="45" y1="75" x2="45" y2="25" stroke="#10b981" stroke-width="3"/><line x1="45" y1="60" x2="60" y2="48" stroke="#10b981" stroke-width="2"/><line x1="45" y1="50" x2="30" y2="38" stroke="#10b981" stroke-width="2"/><line x1="45" y1="40" x2="60" y2="28" stroke="#10b981" stroke-width="2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط عمودي صاعد تتفرع منه خطوط دقيقة مائلة إلى الأعلى كأغصان الشجرة. ترمز للنمو الروحي المتصاعد، البركة في العمر والذرية، والقدرة على التجدد بعد كل انتكاسة.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تفرعات شريانية وحركية دقيقة في مسار خط الحياة والأوتار الراحية.</p>
                            </div>
                        </div>

                        <!-- Seal 15: علامة الهلال القمري (The Lunar Crescent) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">15. علامة الهلال القمري (The Lunar Crescent)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">هلال تل القمر</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 90 50 A 18 18 0 0 0 90 75 A 12 12 0 0 1 90 50 Z" fill="#60a5fa"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">قوس هلالي مقوس على تل القمر عند الحافة السفلية للكف. يرمز لصفاء الإدراك الحدسي، الخيال الخصب، وجاذبية الحضور الروحي وقوة التأثير النفسي في النفوس.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية جلدية منحنية ناتجة عن استدارة حافة الكف الجانبية (Hypothenar eminence).</p>
                            </div>
                        </div>

                        <!-- Seal 16: علامة سهم الإرادة (The Arrow of Will) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">16. علامة سهم الإرادة (The Arrow of Will)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">السهم الصاعد</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="55" y1="65" x2="40" y2="30" stroke="#f4b41a" stroke-width="3"/><polygon points="40,25 35,36 47,32" fill="#f4b41a"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط مستقيم حاد ينطلق من سهل المريخ وينتهي برأس سهم نحو تل المشتري. يدل في الفراسة على شدة العزيمة، القدرة على اقتناص الفرص الكبرى، والإصرار الذي لا يقهر أمام العقبات.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> خط شدي سطحي يربط حركة عضلة الإبهام المقربة مع إصبع السبابة.</p>
                            </div>
                        </div>

                        <!-- Seal 17: علامة الصولجان الملكي (The Scepter Sign) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">17. علامة الصولجان الملكي (The Scepter Sign)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">صولجان تل الشمس</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="75" y1="65" x2="75" y2="28" stroke="#f4b41a" stroke-width="3"/><circle cx="75" cy="24" r="6" fill="#f4b41a"/><circle cx="75" cy="24" r="3" fill="#000"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط مستقيم يعلوه قرص دائري أو حلقة كاملة على تل الشمس (أبولو). دل في المخطوطات القديمة على نيل الجاه والشهرة والرياسة، وأن صاحب هذا الختم تتبعه القلوب بطاعة واحترام.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> اندماج خط الشمس (Apollo line) مع حليمة جلدية دائرية طبيعية.</p>
                            </div>
                        </div>

                        <!-- Seal 18: حدوة الفرس الحصينة (The Horseshoe) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">18. حدوة الفرس الحصينة (The Horseshoe)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">رمز التثبيت والحصانة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 58 45 C 58 32, 78 32, 78 45 L 78 52 C 78 55, 74 55, 74 52 L 74 45 C 74 38, 62 38, 62 45 L 62 52 C 62 55, 58 55, 58 52 Z" fill="#94a3b8"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">قوس مقلوب متقن عند قاعدة تل زحل أو وسط الكف. يرمز لتثبيت الأرزاق، طرد النحوسات والعوارض الطاقية، واستقرار الأحوال المادية والمعنوية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية دائرية تتشكل من انحناء خط الرأس حول سهل المريخ.</p>
                            </div>
                        </div>

                        <!-- Seal 19: بتلة اللوتس والصفاء (The Lotus Petal) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">19. بتلة اللوتس والصفاء (The Lotus Petal)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">زهرة الطهارة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 68 55 C 60 45, 60 35, 68 25 C 76 35, 76 45, 68 55 Z" fill="rgba(216,180,254,0.3)" stroke="#d8b4fe" stroke-width="2"/><path d="M 68 55 C 55 48, 50 40, 55 30 C 62 38, 65 48, 68 55 Z" fill="none" stroke="#d8b4fe" stroke-width="1.5"/><path d="M 68 55 C 81 48, 86 40, 81 30 C 74 38, 71 48, 68 55 Z" fill="none" stroke="#d8b4fe" stroke-width="1.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">ثلاث بتلات ملتقية عند قاعدة الكف تشبه زهرة اللوتس. ترمز للطهارة الروحية، سلامة القلب من الغل والحسد، والارتقاء في المقامات الصوفية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تلاقي ثلاث طيات رسغية وعضلية عند مركز الراحة.</p>
                            </div>
                        </div>

                        <!-- Seal 20: علامة المرساة والرسوخ (The Anchor Sign) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">20. علامة المرساة والرسوخ (The Anchor Sign)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">مرساة خط المصير</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="68" y1="30" x2="68" y2="65" stroke="#00f0ff" stroke-width="3"/><circle cx="68" cy="26" r="4" fill="none" stroke="#00f0ff" stroke-width="2"/><path d="M 52 55 Q 68 75 84 55" fill="none" stroke="#00f0ff" stroke-width="3"/><polygon points="52,53 50,60 56,58" fill="#00f0ff"/><polygon points="84,53 82,58 88,60" fill="#00f0ff"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط عمودي ينتهي بقوس سفلي وسهمين يشبه مرساة السفينة عند الرسغ. دل على الرسوخ والأمان في الأسفار والنجاة من العواصف المادية والتقلبات النفسية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تشعب خط المصير عند ارتكازه على الثنية الرسغية الأولى.</p>
                            </div>
                        </div>

                        <!-- Seal 21: نطاق الزهرة والهلال الأثيري (Girdle of Venus) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">21. نطاق الزهرة والهلال الأثيري (Girdle of Venus)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">قوس الحساسية الفائقة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 45 28 Q 75 48 105 30" fill="none" stroke="#f4b41a" stroke-width="3.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">قوس هلالي نصف دائري يمتد أعلى خط القلب، معلقاً بين ما بين السبابة والوسطى إلى ما بين البنصر والخنصر. علامة فرط الإحساس الوجداني، الذائقة الفنية العالية، والتقاط مشاعر ونوايا الآخرين بدقة مذهلة.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية جلدية ثانوية ناتجة عن حركة ضم الأصابع الوسطى والبنصر.</p>
                            </div>
                        </div>

                        <!-- Seal 22: خط الحدس الأثيري (Line of Intuition) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">22. خط الحدس الأثيري (Line of Intuition)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">قوس الإلهام الخالص</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 90 70 C 110 50, 110 35, 95 25" fill="none" stroke="#00f0ff" stroke-width="3" stroke-dasharray="6,3"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط نصف دائري مستقل ينطلق من تل القمر في أسفل الكف وينحني صاعداً نحو تل عطارد دون أن يمس خط المصير. يرمز للحدس التلقائي، التخاطر الروحي، واستشعار الوقائع قبل إعلانها.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية أدمية ناتجة عن مرونة عضلات الخنصر وحافة اليد الخارجية.</p>
                            </div>
                        </div>

                        <!-- Seal 23: حلقة زحل الصوفية (Ring of Saturn) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">23. حلقة زحل الصوفية (Ring of Saturn)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">طوق الزهد والعزلة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 58 24 C 64 32, 72 32, 78 24" fill="none" stroke="#94a3b8" stroke-width="3"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">قوس نصف دائري يطوق قاعدة الإصبع الأوسط (الوسطى). يرمز في التراث للتأمل الفلسفي العميق، الزهد في بهارج الدنيا، والميل الفطري للبحث في أسرار الوجود والكون.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية انقباضية حول المفصل السنعي للإصبع الأوسط.</p>
                            </div>
                        </div>

                        <!-- Seal 24: طوق الشمس وأبولو (Ring of Apollo) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">24. طوق الشمس وأبولو (Ring of Apollo)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">هلال الإشراق والجمال</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 75 24 C 81 32, 89 32, 95 24" fill="none" stroke="#f4b41a" stroke-width="3"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">قوس مقوس ناعم يطوق قاعدة إصبع البنصر على تل الشمس. يدل على الذائقة الجمالية الرفيعة، الكاريزما الجذابة، وحب الضياء والنور في الفكر والعمل.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> ثنية جلدية طبيعية عند قاعدة إصبع البنصر.</p>
                            </div>
                        </div>

                        <!-- Seal 25: خطوط الشفاء والمعلم (Medical Stigmata) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">25. خطوط الشفاء والمعلم (Medical Stigmata)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">خطوط الرحمة الأربعة</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <line x1="88" y1="26" x2="88" y2="44" stroke="#10b981" stroke-width="2.5"/><line x1="93" y1="25" x2="93" y2="45" stroke="#10b981" stroke-width="2.5"/><line x1="98" y1="26" x2="98" y2="44" stroke="#10b981" stroke-width="2.5"/><line x1="103" y1="28" x2="103" y2="42" stroke="#10b981" stroke-width="2.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">ثلاثة إلى أربعة خطوط عمودية دقيقة متوازية على تل عطارد تحت الخنصر. تسمى 'علامات الشفاء'؛ وتدل على موهبة فطرية في الطب، المواساة، والقدرة على تهدئة آلام الآخرين بحسن المنطق.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> خطوط تمدد عمودية فوق الأنسجة العصبية المغذية لإصبع الخنصر.</p>
                            </div>
                        </div>

                        <!-- Seal 26: خط التعاطف الوجداني (Line of Sympathy) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">26. خط التعاطف الوجداني (Line of Sympathy)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">جسر تل المشتري</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 38 28 C 45 38, 55 45, 65 48" fill="none" stroke="#ec4899" stroke-width="2.5"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط مائل ينحدر بلطف من تل المشتري باتجاه خط الرأس والقلب. يدل على رقة القلب، التعاطف الإنساني الفطري مع الضعفاء، والقدرة على احتواء النفوس الحزينة.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> طية وصل بين العضلة بين العظمية الأولى وجلد راحة اليد.</p>
                            </div>
                        </div>

                        <!-- Seal 27: أساور الرسغ الملكية الثلاثة (The Rascettes) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">27. أساور الرسغ الملكية الثلاثة (The Rascettes)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">قيود الملك والعافية</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 35 78 Q 70 72 105 78" fill="none" stroke="#f4b41a" stroke-width="3"/><path d="M 38 83 Q 70 78 102 83" fill="none" stroke="#f4b41a" stroke-width="2.5"/><path d="M 42 88 Q 70 84 98 88" fill="none" stroke="#f4b41a" stroke-width="2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">ثلاثة خطوط أفقية متوازية عميقة عند مفصل الكف مع الساعد. كل سوار منها كان يرمز في الفراسة القديمة لثلاثين عاماً من الصحة والحيوية، وتكاملها الثلاثي علامة التوازن التام بين الجسد والعقل والروح.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> طيات المعصم الانثنائية الرئيسية الناتجة عن حركة المفصل الرسغي الكعبري.</p>
                            </div>
                        </div>

                        <!-- Seal 28: خط الحارس الأثيري (Mars Guardian Line) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">28. خط الحارس الأثيري (Mars Guardian Line)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">خط الحياة المزدوج</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 38 42 C 40 55, 48 70, 58 78" fill="none" stroke="#ef4444" stroke-width="3"/><path d="M 45 44 C 47 55, 54 68, 62 75" fill="none" stroke="#f4b41a" stroke-width="2" stroke-dasharray="4,2"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط يمتد موازياً لخط الحياة من الداخل في سهل المريخ والزهرة. يسمى 'الملاك الحارس'؛ يرمز لبطانة حيوية ومناعة قوية تحمي البدن من التلف والأخطار الخارجية.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> خط جلدي داخلي يعكس قوة عضلات الإبهام السطحية (Thenar muscles).</p>
                            </div>
                        </div>

                        <!-- Seal 29: خط الكشف الرؤيوي (Line of Clairvoyance) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">29. خط الكشف الرؤيوي (Line of Clairvoyance)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">محور الإدراك الماورائي</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <path d="M 95 65 Q 85 45 70 42" fill="none" stroke="#a855f7" stroke-width="3"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">خط عميق مقوس ينطلق من عمق تل القمر متجهاً نحو سهل المريخ وخط الرأس. يدل على قوة الأحلام التحذيرية، استشعار الطاقة الكامنة في الأماكن، والصفاء الذهني التام.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> طية شمولية ثانوية بين الثنية الراحية البعيدة وحافة اليد.</p>
                            </div>
                        </div>

                        <!-- Seal 30: ختم النجم المزدوج (The Twin Stars) -->
                        <div class="seal-item-card" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; transition:all 0.25s;" onmouseover="this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'; this.style.transform='none'">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.02rem;">30. ختم النجم المزدوج (The Twin Stars)</strong>
                                <span style="font-size:0.75rem; background:rgba(244,180,26,0.15); color:var(--gold); padding:2px 8px; border-radius:6px;">اقتران المشتري والشمس</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="140" height="90" viewBox="0 0 140 90">
                                    <path d="M 25 80 Q 20 40 40 20 Q 60 10 70 15 Q 85 10 95 18 Q 110 12 115 35 Q 120 60 115 80 Z" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
                                    <polygon points="40,22 43,30 51,30 45,35 47,43 40,38 33,43 35,35 29,30 37,30" fill="#f4b41a"/><polygon points="85,22 88,30 96,30 90,35 92,43 85,38 78,43 80,35 74,30 82,30" fill="#f4b41a"/>
                                </svg>
                            </div>
                            <div style="font-size:0.82rem; color:#cbd5e1; line-height:1.7;">
                                <p style="margin:0 0 6px 0;">• <strong>المصدر والرمزية:</strong> <span style="color:#f8fafc;">نجمتان خماسيتان أو سداسيتان تتطابقان معاً: الأولى على تل المشتري (الهيبة والرياسة) والثانية على تل الشمس (المجد والبريق). اعتبرت أندر علامة فراسية تدل على الخلود المعرفي واجتماع الحكمة مع التأثير الواسع.</span></p>
                                <p style="margin:0; color:#94a3b8;">• <strong>التشريح العلمي:</strong> تقاطع تشريحي متناظر للألياف السطحية تحت إصبعي السبابة والبنصر.</p>
                            </div>
                        </div>
                    </div>

                    <!-- SECTION 3: DECONSTRUCTION OF TREASURE MYTHS -->
                    <div style="background:linear-gradient(135deg, rgba(239,68,68,0.15), rgba(0,0,0,0.7)); border:2px solid #ef4444; border-radius:16px; padding:22px;">
                        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
                            <span style="font-size:1.6rem; color:#ef4444;">🛡️</span>
                            <h3 style="font-family:'Amiri', serif; font-size:1.35rem; color:#ef4444; margin:0;">
                                3. التفكيك الصارم: دحض خرافة "الكف الزوهري مفتاح الكنوز والمرصودات"
                            </h3>
                        </div>
                        <p style="font-size:0.88rem; color:#cbd5e1; line-height:1.8; margin-bottom:12px;">
                            تزعم عصابات التنقيب العشوائي في الفولكلور المغاربي والمشرقي أن كف الشخص الزوهري (وخاصة صاحب الخط القاطع العرضي أو علامة 111) هو "مفتاح كهانة" يُبطل رصد الدفائن بمجرد مسح تراب الموقع، أو بطلب قطرات من دمه. هذا الزعم دجل محض وباطل من عدة أوجه قطعية:
                        </p>
                        <div style="font-size:0.85rem; color:#f8fafc; line-height:1.7;">
                            • <strong>الوهم الفيزيائي والمادي:</strong> خطوط الكف لا تصدر موجات كهرومغناطيسية خارقة تخترق طبقات الصخور أو تعطل مجسات الأرض؛ بل هي علامات تطور أنسجة طبيعية ناتجة عن التكون الجنيني وثني الكف.<br>
                            • <strong>المأساة الإنسانية والجنائية:</strong> ارتكبت عصابات الجهل جرائم خطف واستغلال مأساوية ضد أطفال وبالغين يحملون هذه العلامات، وهي جرائم وحشية نكراء يُعاقب عليها القانون الدولي والشرعي بأشد العقوبات الجنائية (القتل العمد والحرابة).<br>
                            • <strong>التحصين المعرفي والديني:</strong> كل ما خلقه الله في جسدك هو أثر من آثار الصانع الحكيم، ولا يملك مخلوق في الأرض ولا في السماء نفعاً ولا ضراً إلا بإذن الله، وخرافات الكنوز ليست سوى سراب يلاحقه المفلسون للنصب على الناس.
                        </div>
                    </div>

                </div>
            </div>

            <!-- SUB-VIEW 4: SEVEN PLANETARY SEALS & AGRIPPA SIGILS -->
            <div id="seals-view-planets" class="seals-sub-container">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(0,240,255,0.3); border-radius:20px; padding:28px 22px; margin-bottom:30px;">
                    <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:var(--cyan); margin-bottom:12px;">
                        🪐 أختام الكواكب السبعة وشفراتها الهندسية في مصنفات أغريبا وبيكاتريكس
                    </h2>
                    <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin-bottom:24px;">
                        في الفلسفة السيمياوية الأوربية والأندلسية (كما في <em>غاية الحكيم / Picatrix</em> وكتاب <em>الفلسفة الخفية (De Occulta Philosophia)</em> لكورنيليوس أغريبا)، 
                        تُستخرج أختام الكواكب وشفرات أرواحها الذكية (Intelligences) عبر تقنية هندسية رياضية صارمة تُعرف بـ 
                        <strong>«مسار الخطوط على المربع السحري (Sigil Kamea Tracing)»</strong>، حيث تُرسم الخطوط بربط أرقام حروف اسم الروح داخل وفق الكوكب المقابل.
                    </p>

                    <!-- Planetary Grid -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-bottom:25px;">
                        
                        <!-- Saturn -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(100,116,139,0.3); border-radius:14px; padding:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:#94a3b8; font-size:1.1rem;">♄ ختم فلك زحل (Saturn Seal)</strong>
                                <span style="font-size:0.75rem; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">مربع 3×3</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="120" height="80" viewBox="0 0 140 100">
                                    <line x1="20" y1="20" x2="120" y2="20" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
                                    <line x1="70" y1="20" x2="70" y2="80" stroke="#94a3b8" stroke-width="4"/>
                                    <line x1="40" y1="50" x2="100" y2="50" stroke="#94a3b8" stroke-width="3"/>
                                    <circle cx="20" cy="20" r="4" fill="#94a3b8"/>
                                    <circle cx="120" cy="20" r="4" fill="#94a3b8"/>
                                    <circle cx="70" cy="80" r="4" fill="#94a3b8"/>
                                </svg>
                            </div>
                            <div style="font-size:0.83rem; color:#cbd5e1; line-height:1.6;">
                                <strong>الروح الذكية:</strong> Agiel (أجيئيل = 45)<br>
                                <strong>الروح الأرضية:</strong> Zazel (زازيل = 45)<br>
                                <strong>الخواص:</strong> الثبات، البناء طويل الأمد، الحكمة، كبح الاندفاع والتأصيل.
                            </div>
                        </div>

                        <!-- Jupiter -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(216,180,254,0.3); border-radius:14px; padding:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:#d8b4fe; font-size:1.1rem;">♃ ختم فلك المشتري (Jupiter Seal)</strong>
                                <span style="font-size:0.75rem; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">مربع 4×4</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="120" height="80" viewBox="0 0 140 100">
                                    <path d="M 30 20 L 70 80 L 110 20" fill="none" stroke="#d8b4fe" stroke-width="4"/>
                                    <line x1="45" y1="50" x2="95" y2="50" stroke="#d8b4fe" stroke-width="4"/>
                                    <circle cx="70" cy="80" r="5" fill="#d8b4fe"/>
                                </svg>
                            </div>
                            <div style="font-size:0.83rem; color:#cbd5e1; line-height:1.6;">
                                <strong>الروح الذكية:</strong> Iophiel (يوفائيل = 136)<br>
                                <strong>الروح الأرضية:</strong> Hismael (هسمائيل = 136)<br>
                                <strong>الخواص:</strong> الهيبة، السعة المالية، القبول والعدل والتوسع المعرفي.
                            </div>
                        </div>

                        <!-- Mars -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(239,68,68,0.3); border-radius:14px; padding:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:#ef4444; font-size:1.1rem;">♂ ختم فلك المريخ (Mars Seal)</strong>
                                <span style="font-size:0.75rem; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">مربع 5×5</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="120" height="80" viewBox="0 0 140 100">
                                    <line x1="20" y1="50" x2="120" y2="50" stroke="#ef4444" stroke-width="4"/>
                                    <line x1="70" y1="20" x2="70" y2="80" stroke="#ef4444" stroke-width="4"/>
                                    <polygon points="120,50 100,35 100,65" fill="#ef4444"/>
                                </svg>
                            </div>
                            <div style="font-size:0.83rem; color:#cbd5e1; line-height:1.6;">
                                <strong>الروح الذكية:</strong> Graphiel (غرافائيل = 325)<br>
                                <strong>الروح الأرضية:</strong> Bartzabel (بارتزابيل = 325)<br>
                                <strong>الخواص:</strong> الشجاعة، كسر الموانع، الحسم القاطع والدفاع الحصين.
                            </div>
                        </div>

                        <!-- Sun -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(244,180,26,0.3); border-radius:14px; padding:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--gold); font-size:1.1rem;">☉ ختم فلك الشمس (Sun Seal)</strong>
                                <span style="font-size:0.75rem; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">مربع 6×6</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="120" height="80" viewBox="0 0 140 100">
                                    <circle cx="70" cy="50" r="30" fill="none" stroke="#f4b41a" stroke-width="4"/>
                                    <circle cx="70" cy="50" r="8" fill="#f4b41a"/>
                                    <line x1="20" y1="50" x2="120" y2="50" stroke="#f4b41a" stroke-width="2" stroke-dasharray="3,3"/>
                                </svg>
                            </div>
                            <div style="font-size:0.83rem; color:#cbd5e1; line-height:1.6;">
                                <strong>الروح الذكية:</strong> Nakhiel (ناخيئيل = 111)<br>
                                <strong>الروح الأرضية:</strong> Sorath (سورات = 666)<br>
                                <strong>الخواص:</strong> الملك، الجاه، الشهرة، الحيوية البيولوجية والشفاء.
                            </div>
                        </div>

                        <!-- Venus -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(6,214,160,0.3); border-radius:14px; padding:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--emerald); font-size:1.1rem;">♀ ختم فلك الزهرة (Venus Seal)</strong>
                                <span style="font-size:0.75rem; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">مربع 7×7</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="120" height="80" viewBox="0 0 140 100">
                                    <circle cx="70" cy="35" r="22" fill="none" stroke="#06d6a0" stroke-width="4"/>
                                    <line x1="70" y1="57" x2="70" y2="90" stroke="#06d6a0" stroke-width="4"/>
                                    <line x1="50" y1="72" x2="90" y2="72" stroke="#06d6a0" stroke-width="4"/>
                                </svg>
                            </div>
                            <div style="font-size:0.83rem; color:#cbd5e1; line-height:1.6;">
                                <strong>الروح الذكية:</strong> Hagiel (هاجيئيل = 49)<br>
                                <strong>الروح الأرضية:</strong> Kedemel (كدميل = 175)<br>
                                <strong>الخواص:</strong> المحبة، الألفة، الجمال، الفنون والتوافق الزواجي.
                            </div>
                        </div>

                        <!-- Mercury -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(0,240,255,0.3); border-radius:14px; padding:18px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                                <strong style="color:var(--cyan); font-size:1.1rem;">☿ ختم فلك عطارد (Mercury Seal)</strong>
                                <span style="font-size:0.75rem; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:6px;">مربع 8×8</span>
                            </div>
                            <div style="text-align:center; padding:14px; background:rgba(0,0,0,0.6); border-radius:10px; margin-bottom:12px;">
                                <svg width="120" height="80" viewBox="0 0 140 100">
                                    <path d="M 50 15 C 60 25, 80 25, 90 15" fill="none" stroke="#00f0ff" stroke-width="3"/>
                                    <circle cx="70" cy="40" r="18" fill="none" stroke="#00f0ff" stroke-width="4"/>
                                    <line x1="70" y1="58" x2="70" y2="88" stroke="#00f0ff" stroke-width="4"/>
                                    <line x1="55" y1="72" x2="85" y2="72" stroke="#00f0ff" stroke-width="4"/>
                                </svg>
                            </div>
                            <div style="font-size:0.83rem; color:#cbd5e1; line-height:1.6;">
                                <strong>الروح الذكية:</strong> Tiriel (تيريئيل = 260)<br>
                                <strong>الروح الأرضية:</strong> Taphthartharath (تافثارثارث = 2080)<br>
                                <strong>الخواص:</strong> الحكمة، التجارة، البلاغة، سرعة الفهم وتيسير المعاملات.
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 5: THE ZOUHRI PHENOMENON (DEEP INVESTIGATION) -->
            <div id="seals-view-zouhri" class="seals-sub-container">
                <div style="background:rgba(13,19,36,0.95); border:1px solid rgba(239,68,68,0.3); border-radius:20px; padding:28px 22px; margin-bottom:30px;">
                    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                        <div>
                            <span style="color:#ef4444; font-size:0.85rem; font-weight:700;"><i class="fa-solid fa-dna"></i> الملف الشامل المحرَّر</span>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#fff; margin:4px 0 0 0;">ظاهرة الإنسان الزوهري: التشريح العلمي، الجذور التراثية، وتفكيك الخرافة</h2>
                        </div>
                        <span style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; color:#ef4444; padding:4px 12px; border-radius:10px; font-size:0.8rem;">تحذير إنساني وتحصين شرعي</span>
                    </div>

                    <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin-bottom:24px;">
                        تعتبر <strong>«الزوهرية»</strong> من أكثر الظواهر غموضاً وجدلاً في الثقافة المغاربية والمشرقية. 
                        يُطلق اللفظ شعبياً على أشخاص يمتلكون علامات جسدية خلقية نادرة، ويُزعم في كتب الخرافة الشعبية أنهم يملكون 
                        «دماً خاصاً» أو «اتصالاً بعالم الجن وخبايا الأرض». هنا نضع هذا الملف تحت المجهر الطبي والأنثروبولوجي والشرعي لتفكيك الأسطورة وحماية الأرواح.
                    </p>

                    <!-- SECTION 1: LINGUISTIC & HISTORICAL ROOTS -->
                    <div style="background:rgba(0,0,0,0.4); border-radius:14px; padding:20px; margin-bottom:22px; border-right:4px solid var(--gold);">
                        <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:var(--gold); margin-bottom:8px;">
                            1. الجذور اللغوية والتاريخية للفظ «الزوهري»
                        </h3>
                        <p style="font-size:0.87rem; color:#cbd5e1; line-height:1.8; margin:0;">
                            • <strong>المعنى اللغوي:</strong> الزُّهْرَة هي البياض المشرق والنور الصافي، والزاهر هو الوجه المضيء المستنير.<br>
                            • <strong>الجذر القبالي (Sefer HaZohar):</strong> يرى بعض الباحثين أن الكلمة تأثرت بكتاب «الزوهار» (كتاب الإشراق / التنوير) في صوفية الأندلس والمغرب، حيث يرمز الزوهار للإنسان المستنير الذي تنكشف له حجب البصيرة.<br>
                            • <strong>العامية المغاربية:</strong> كلمة «الزّهْر» تعني الحظ والبركة، فالزوهري في الأصل هو "صاحب الحظ السعيد" أو المحظوظ قبل أن تحرّفها كتب الشعوذة إلى أهداف سحرية مظلمة.
                        </p>
                    </div>

                    <!-- SECTION 2: PHYSICAL SIGNS MEDICAL VS ESOTERIC -->
                    <h3 style="font-family:'Amiri', serif; font-size:1.4rem; color:var(--cyan); margin-bottom:14px;">
                        <i class="fa-solid fa-stethoscope"></i> 2. العلامات الجسدية المنسوبة للزوهري: الميزان الطبي مقابل الأسطورة
                    </h3>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:18px; margin-bottom:28px;">
                        
                        <!-- Sign 1: Simian Crease -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <strong style="color:var(--gold);">① خط الكف العرضي المتصل</strong>
                                <span style="font-size:0.75rem; color:#94a3b8;">Simian Crease</span>
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                • <strong>الأسطورة الباطنية:</strong> يُسمى "قطع الكف" أو "الخط الملكي"، وتزعم كتب الشعوذة أنه مفتاح فتح أبواب الكنوز المرصودة تحت الأرض.<br>
                                • <strong>الحقيقة الطبية والتشريحية:</strong> ظاهرة جينية طبيعية تصيب 1% إلى 2% من البشر الأصحاء حول العالم. تنتج عن اندماج خطي القلب والرأس في طية كف واحدة أثناء التكون الجنيني، ولا علاقة لها بأي بعد غيبي.
                            </p>
                        </div>

                        <!-- Sign 2: Fissured Tongue -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <strong style="color:var(--gold);">② اللسان المفلوق طولياً</strong>
                                <span style="font-size:0.75rem; color:#94a3b8;">Lingua Plicata</span>
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                • <strong>الأسطورة الباطنية:</strong> يُزعم أنه "ناطق بلغة الملائكة، ولا يتسلط على طعامه شيطان".<br>
                                • <strong>الحقيقة الطبية والتشريحية:</strong> حالة شائعة تسمى طبياً <em>Fissured Tongue</em> تصيب حوالي 5% من سكان الأرض. هي شق حميد في الغشاء المخاطي للسان نتيجة عوامل وراثية عائلية سليمة تماماً.
                            </p>
                        </div>

                        <!-- Sign 3: Heterochromia & Eye Gaze -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <strong style="color:var(--gold);">③ بريق العينين والحول الخفيف</strong>
                                <span style="font-size:0.75rem; color:#94a3b8;">Heterochromia</span>
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                • <strong>الأسطورة الباطنية:</strong> نظرة ثاقبة تكشف الغيبيات، وبريق في القزحية يعكس حضور الغدة الصنوبرية المفتوحة.<br>
                                • <strong>الحقيقة الطبية والتشريحية:</strong> تباين صبغة الميلانين في القزحية أو انعكاس الضوء على قرنية رقيقة، أو استرخاء طفيف في عضلات العين (Strabismus)، وهي صفات تشريحية نقية.
                            </p>
                        </div>

                        <!-- Sign 4: Double Hair Whorl -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <strong style="color:var(--gold);">④ دائرتا الشعر على الرأس</strong>
                                <span style="font-size:0.75rem; color:#94a3b8;">Double Crown Whorl</span>
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                • <strong>الأسطورة الباطنية:</strong> وجود "قرنين طاقيين" أو بوابتين أثيريتين لاستقبال الفيض النجمي.<br>
                                • <strong>الحقيقة الطبية والتشريحية:</strong> اتجاه نمو بصيلات فروة الرأس من نقطتين مركزيتين أثناء النمو الجنيني للبشرة، وتحدث لدى نحو 5% من المواليد.
                            </p>
                        </div>

                        <!-- Sign 5: Rare Blood Groups -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <strong style="color:var(--gold);">⑤ فصيلة الدم (Rh-Negative)</strong>
                                <span style="font-size:0.75rem; color:#94a3b8;">Rhesus Negative</span>
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                • <strong>الأسطورة الباطنية:</strong> "دم نقي لا يحمل جينات القردة البدائية، ومغذٍ لأرواح الأرض".<br>
                                • <strong>الحقيقة الطبية والتشريحية:</strong> طفرة جينية متنحية في مستضد العامل الريزوسي (D-antigen) تتركز تاريخياً في حوض الباسك وشمال إفريقيا، ولا علاقة لها بأي أصل فضائي أو سحري.
                            </p>
                        </div>

                        <!-- Sign 6: Foot / Back Line -->
                        <div style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                <strong style="color:var(--gold);">⑥ الخط الطولي بأسفل القدم أو الظهر</strong>
                                <span style="font-size:0.75rem; color:#94a3b8;">Plantar / Spinal Crease</span>
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                • <strong>الأسطورة الباطنية:</strong> خط الاتصال بالأرض واستشعار التيارات المغناطيسية السفلية.<br>
                                • <strong>الحقيقة الطبية والتشريحية:</strong> طية جلدية ناشئة عن تركز الأربطة الأخمصية أو العصبية، طبيعية تماماً.
                            </p>
                        </div>

                    </div>

                    <!-- SECTION 3: SENSITIVITY & PSYCHOLOGY -->
                    <div style="background:rgba(15,23,42,0.8); border:1px solid rgba(0,240,255,0.2); border-radius:14px; padding:20px; margin-bottom:22px;">
                        <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:var(--cyan); margin-bottom:8px;">
                            3. الخصائص النفسية والحسية: فرط الإحساس (HSP) والحساسية الحيوية
                        </h3>
                        <p style="font-size:0.87rem; color:#cbd5e1; line-height:1.8; margin:0;">
                            أظهرت الدراسات السيكولوجية الحديثة أن كثيراً ممن يُطلق عليهم "زهريون" هم في الواقع أفراد ينتمون لفئة 
                            <strong>«الأشخاص مفرطي الحساسية الحسية (Highly Sensitive Persons - HSP)»</strong>. يتميز هؤلاء بـ:
                            زيادة حساسية الجهاز العصبي المركزي للمحفزات، قوة الملاحظة، تعاطف وجداني عالٍ (Empathy)، 
                            وإدراك دقيق للتغيرات الكهرومغناطيسية والجوية (مثل استشعار رطوبة الأرض واقتراب العواصف). 
                            هذه ميزات عصبية إدراكية حقيقية فُسرت تاريخياً في بيئات الجهل بأنها "سحر واتصال بالجن".
                        </p>
                    </div>

                    <!-- SECTION 4: CRIMINAL & SHARIA CRITIQUE (DECONSTRUCTION OF TREASURE HUNTING) -->
                    <div style="background:linear-gradient(135deg, rgba(239,68,68,0.15), rgba(0,0,0,0.6)); border:2px solid #ef4444; border-radius:16px; padding:22px;">
                        <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
                            <span style="font-size:1.6rem; color:#ef4444;">⚖️</span>
                            <h3 style="font-family:'Amiri', serif; font-size:1.4rem; color:#ef4444; margin:0;">
                                4. التفكيك الجنائي والشرعي الصارم: جريمة استغلال الزهريين في نبش الكنوز
                            </h3>
                        </div>
                        <p style="font-size:0.9rem; color:#f8fafc; line-height:1.8; margin-bottom:12px;">
                            تعتبر ممارسات عصابات السحر والشعوذة في استهداف الأطفال أو البالغين الزهريين (بزعم تقديم قطرات من دمهم لـ "فك رصد الكنوز") 
                            <strong>جريمة إنسانية بشعة وخرافة شيطانية باطلة</strong>. 
                        </p>
                        <div style="font-size:0.86rem; color:#cbd5e1; line-height:1.7;">
                            • <strong>أكذوبة «الرصد»:</strong> لا وجود في القرآن والسنة لشيء اسمه "حارس كنز من الجن" ينتظر دماً بشرياً؛ بل هي حيلة اخترعها دجالو العصور المظلمة لابتزاز الناس وتبرير فشلهم في التنقيب.<br>
                            • <strong>الحكم الشرعي:</strong> قتل أو إيذاء أي نفس إنسانية لاستخراج كنز هو <strong>كفر وردة وجريمة قتل عمد جزاؤها القصاص في الدنيا والخلود في النار</strong>، والدم المسفوك قرباناً هو شرك أكبر بالاتفاق.<br>
                            • <strong>الحصن والأمان للزوهري:</strong> الإنسان الذي خلقه الله بهذه العلامات هو عبد لله مكرم، لا يملك جن ولا إنس سبيلاً عليه ما دام معتصماً بتوحيده ومحصناً بذكر ربه، ولا أثر لهذه الخرافات إلا في عقول الموهومين.
                        </div>
                    </div>

                </div>
            </div>

            <!-- SUB-VIEW 6: SPIRITUAL BLOODLINES & STARSEEDS -->
            <div id="seals-view-bloodlines" class="seals-sub-container">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(157,78,221,0.35); border-radius:20px; padding:28px 22px; margin-bottom:30px;">
                    <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#d8b4fe; margin-bottom:12px;">
                        🌌 موسوعة السلالات الروحية، الاصطفاء الجيني، وبذور النجوم في الكتب المقدسة
                    </h2>
                    <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin-bottom:24px;">
                        طرحت الحضارات القديمة والنصوص الدينية فكرة «الاصطفاء السلالي» و«الذرية النورانية». 
                        هنا نستعرض المفاهيم الكبرى كما وردت في القرآن الكريم، أسفار التراث القديم، والغنوصية الكونية.
                    </p>

                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:20px; margin-bottom:28px;">
                        
                        <!-- 1. Quranic Divine Election -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(244,180,26,0.3); border-radius:14px; padding:18px;">
                            <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:var(--gold); margin-bottom:8px;">
                                1. الاصطفاء الوراثي في القرآن الكريم
                            </h3>
                            <div style="font-family:'Amiri', serif; font-size:1.05rem; color:#f8fafc; line-height:1.9; margin-bottom:10px; background:rgba(244,180,26,0.06); padding:10px; border-radius:8px;">
                                ﴿إِنَّ اللَّهَ اصْطَفَىٰ آدَمَ وَنُوحًا وَآلَ إِبْرَاهِيمَ وَآلَ عِمْرَانَ عَلَى الْعَالَمِينَ ۝ ذُرِّيَّةً بَعْضُهَا مِن بَعْضٍ وَاللَّهُ سَمِيعٌ عَلِيمٌ﴾
                            </div>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                يثبت القرآن وجود وراثة نورانية في خطوط الأنبياء (ذرية بعضها من بعض)، حيث تنتقل مؤهلات النبوة والروحانية عبر سلاسل وراثية مطهرة وصولاً إلى النبي محمد ﷺ وعترته الطاهرة (آل البيت).
                            </p>
                        </div>

                        <!-- 2. The Watchers & Nephilim -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(239,68,68,0.3); border-radius:14px; padding:18px;">
                            <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:#ef4444; margin-bottom:8px;">
                                2. المراقبون والنفيليم (سفر أخنوخ)
                            </h3>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                في سفر أخنوخ (Book of Enoch)، هبط 200 من الملائكة المراقبين (The Watchers) على جبل حرمون وعلموا البشر أسرار الفلك والسلاح والزينة، ونتج عن تزاوجهم بالبشر «النفيليم» (العماليق / الجبابرة). يقابل هذا في القرآن قصة هاروت وماروت في بابل، وقوم عاد ﴿الَّتِي لَمْ يُخْلَقْ مِثْلُهَا فِي الْبِلَادِ﴾.
                            </p>
                        </div>

                        <!-- 3. Order of Melchizedek & Al-Khidr -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(0,240,255,0.3); border-radius:14px; padding:18px;">
                            <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:var(--cyan); margin-bottom:8px;">
                                3. رتبة ملكي صادق والخضر (عليه السلام)
                            </h3>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                سلالة الكهنة الكبرى التي لا بداية لأيامها ولا نهاية لنسبها؛ ملك ساليم وكاهن الله العلي الذي بارك إبراهيم. 
                                يتطابق في التراث الإسلامي مع مقام «الخضر» صاحب العلم اللدني ﴿وَعَلَّمْنَاهُ مِن لَّدُنَّا عِلْمًا﴾، 
                                الذي يمثل تيار الوعي الباطني المستمر خارج قيود الزمان.
                            </p>
                        </div>

                        <!-- 4. Starseeds & Dogon (Sirius) -->
                        <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(168,85,247,0.3); border-radius:14px; padding:18px;">
                            <h3 style="font-family:'Amiri', serif; font-size:1.3rem; color:#c084fc; margin-bottom:8px;">
                                4. بذور النجوم والشعرى اليمانية (Sirius)
                            </h3>
                            <p style="font-size:0.83rem; color:#cbd5e1; line-height:1.7; margin:0;">
                                في كوزمولوجيا قبائل الدوغون (مالي)، احتفظوا بمعرفة فلكية مستحيلة عن النجم القزم الأبيض "سيريوس ب" قبل اكتشافه بالتلسكوبات بقرون. 
                                والقرآن يخص هذا النجم بالذكر حصراً: ﴿وَأَنَّهُ هُوَ رَبُّ الشِّعْرَىٰ﴾ لبيان أن رب الأكوان وخالقها واحد، 
                                وأن كل وعي في المجرات خاضع للبارئ سبحانه.
                            </p>
                        </div>

                    </div>
                </div>
            </div>

            <!-- SUB-VIEW 7: INTERACTIVE SVG SYMBOL GALLERY -->
            <div id="seals-view-gallery" class="seals-sub-container">
                <div style="background:rgba(13,19,36,0.9); border:1px solid rgba(6,214,160,0.3); border-radius:20px; padding:28px 22px; margin-bottom:30px;">
                    <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:var(--emerald); margin-bottom:12px;">
                        🎨 معرض الرموز والطلاسم التفاعلي (Interactive High-Res Sigil Explorer)
                    </h2>
                    <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; margin-bottom:20px;">
                        انقر على أي رمز لاستعراضه بدقة عالية، وفك شفرته الهندسية، ومعرفة مصدره في أمهات المخطوطات.
                    </p>

                    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(140px, 1fr)); gap:14px;" id="seals-interactive-grid">
                        <!-- Populated by JS -->
                    </div>

                    <!-- Modal preview container -->
                    <div id="seal-preview-modal" style="display:none; margin-top:25px; background:rgba(0,0,0,0.6); border:1px solid var(--emerald); border-radius:16px; padding:20px; text-align:center;">
                        <div id="modal-svg-display" style="margin-bottom:14px;"></div>
                        <h4 id="modal-title" style="color:var(--gold); font-size:1.2rem; margin-bottom:6px;"></h4>
                        <p id="modal-desc" style="color:#cbd5e1; font-size:0.88rem; max-width:650px; margin:0 auto; line-height:1.7;"></p>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <!-- END CHAMBER 19 -->
    '''

def get_seals_zouhri_chamber_js():
    return '''
    // ========================================================
    // CHAMBER 19: SEALS, ZOUHRI PHENOMENON & LINEAGES CONTROLLER
    // ========================================================

    const INTERACTIVE_SIGILS_DATA = [
        { id: 'solomon_seal', title: 'خاتم سليمان الأعظم', source: 'شمس المعارف الكبرى', desc: 'الرمز الجامع للأسماء السبعة العظمى، يحقق التوازن بين الروح والجسد والمادة.', svg: '<polygon points="50,5 64,36 98,36 70,57 81,91 50,70 19,91 30,57 2,36 36,36" fill="none" stroke="#f4b41a" stroke-width="4"/><circle cx="50" cy="50" r="16" fill="none" stroke="#00f0ff" stroke-width="3"/>' },
        { id: 'ghazali_3x3', title: 'مثلث الغزالي (بطد زهج واح)', source: 'المنقذ من الضلال والأوفاق', desc: 'المربع السحري 3×3 ذو المجموع 15 ومحور التوازن 5. أقدم مصفوفة توازن رياضي في المخطوطات.', svg: '<rect x="15" y="15" width="70" height="70" fill="none" stroke="#f4b41a" stroke-width="3"/><line x1="38" y1="15" x2="38" y2="85" stroke="#00f0ff" stroke-width="2"/><line x1="62" y1="15" x2="62" y2="85" stroke="#00f0ff" stroke-width="2"/><line x1="15" y1="38" x2="85" y2="38" stroke="#00f0ff" stroke-width="2"/><line x1="15" y1="62" x2="85" y2="62" stroke="#00f0ff" stroke-width="2"/><circle cx="50" cy="50" r="5" fill="#ef4444"/>' },
        { id: 'simian_line', title: 'ختم الخط القاطع الملكي (Simian Line)', source: 'علم الأسارير والفراسة التراثية', desc: 'خط عرضي وحيد متصل ومستقيم يقطع راحة الكف أفقياً من حافة إلى حافة دون انقطاع نتيجة اندماج خط القلب مع خط الرأس. سمي في كتب الصنعة 'السيف القاطع' واعتبر دليلاً على إرادة حديدية لا تتشتت ومفتاحاً لفتح المغلقات.', svg: '<line x1=\"26\" y1=\"48\" x2=\"114\" y2=\"48\" stroke=\"#f4b41a\" stroke-width=\"4\" stroke-linecap=\"round\"/><circle cx=\"70\" cy=\"48\" r=\"4\" fill=\"#00f0ff\"/>' },
        { id: 'three_staffs_111', title: 'ختم الثلاث عصي والسهام (علامة 111)', source: 'قصيدة الإمام علي في الخاتم وشمس المعارف', desc: 'ثلاثة خطوط عمودية متوازية يعلو كلاً منها رأس سهم، وهي المنظومة في البيت: 'ثَلاثُ عِصِيٍّ صُفِّفَتْ بَعْدَ خَاتَمٍ ❊ عَلَى رَأْسِهَا مِثْلُ السِّهَامِ تَقَوَّمُ'. تمثل القوة الثلاثية للروح والنفوذ، وقيمتها العددية بحساب الجمل (111) تطابق قطب الشمس 'ناخيئيل' وسر إشراق البصيرة.', svg: '<line x1=\"50\" y1=\"20\" x2=\"50\" y2=\"70\" stroke=\"#f4b41a\" stroke-width=\"3\"/><polygon points=\"50,15 46,24 54,24\" fill=\"#f4b41a\"/><line x1=\"70\" y1=\"20\" x2=\"70\" y2=\"70\" stroke=\"#f4b41a\" stroke-width=\"3\"/><polygon points=\"70,15 66,24 74,24\" fill=\"#f4b41a\"/><line x1=\"90\" y1=\"20\" x2=\"90\" y2=\"70\" stroke=\"#f4b41a\" stroke-width=\"3\"/><polygon points=\"90,15 86,24 94,24\" fill=\"#f4b41a\"/>' },
        { id: 'palmar_hexagram', title: 'النجمة السداسية الكفية (The Hexagram)', source: 'المخطوطات الهرمسية واليهودية الوسيطة', desc: 'تقاطع مثلثين متطابقين متداخلين يشكلان نجمة سداسية متقنة في سهل المريخ أو تل المشتري. ترمز لأعلى درجات الحصانة الروحية والاتصال المزدوج بين العوالم العلوية والسفلية (As Above, So Below).', svg: '<polygon points=\"70,25 82,46 58,46\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"2.5\"/><polygon points=\"70,53 82,32 58,32\" fill=\"none\" stroke=\"#00f0ff\" stroke-width=\"2.5\"/>' },
        { id: 'palmar_pentagram', title: 'النجمة الخماسية النورانية (The Pentagram)', source: 'الفلسفة الخفية لأغريبا وبيكاتريكس', desc: 'نجمة خماسية تتشكل من خمسة خطوط دقيقة متقاطعة على تل المشتري أو زحل. ترمز في الفراسة لسيادة العقل والروح على العناصر الأربعة (النار، الهواء، الماء، التراب) وحضور الحكمة القيادية.', svg: '<polygon points=\"70,20 76,38 95,38 80,50 86,68 70,56 54,68 60,50 45,38 64,38\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"2\"/>' },
        { id: 'mystic_triangle', title: 'مثلث الحكمة الباطنية (The Mystic Triangle)', source: 'فراسة الرازي ومخطوطات الأندلس', desc: 'مثلث مغلق الأضلاع تماماً في وسط راحة اليد يتشكل من تقاطع خط الرأس (الفكر) وخط الحياة (الجسد) وخط الحدس/الكبد. سمي في المخطوطات 'عين الحكمة' ودل على الفطنة الحادة والبديهة الحاضرة.', svg: '<polygon points=\"45,45 85,38 65,70\" fill=\"rgba(0,240,255,0.2)\" stroke=\"#00f0ff\" stroke-width=\"2.5\"/>' },
        { id: 'croix_mystique', title: 'صليب الحدس الخفي (La Croix Mystique)', source: 'قراءة الكف الفلسفية الأوربية والإسلامية', desc: 'علامة تقاطع مستقلة (+ أو ×) تتوسط الفراغ الموجود بين خط القلب وخط الرأس دون أن تمس أياً منهما. تعتبر أشهر علامة في قراءة الكف تدل على الموهبة الاستشعارية والإلهام الميتافيزيقي وحب الغوامض.', svg: '<path d=\"M 35 35 Q 70 42 105 32\" fill=\"none\" stroke=\"#64748b\" stroke-width=\"1.5\"/><path d=\"M 35 55 Q 70 52 105 60\" fill=\"none\" stroke=\"#64748b\" stroke-width=\"1.5\"/><line x1=\"65\" y1=\"42\" x2=\"75\" y2=\"52\" stroke=\"#d8b4fe\" stroke-width=\"3\" stroke-linecap=\"round\"/><line x1=\"75\" y1=\"42\" x2=\"65\" y2=\"52\" stroke=\"#d8b4fe\" stroke-width=\"3\" stroke-linecap=\"round\"/>' },
        { id: 'palmar_grille', title: 'شبكة الأسارير والمربعات (Palmar Grille)', source: 'الفولكلور المغاربي وكتب الخواص', desc: 'شبكة خطوط متقاطعة أفقياً وعمودياً تشبه المربعات في تل القمر أو تل الزهرة. نسبت لها كتب الفولكلور استشعار المياه الجوفية والمعادن في باطن الأرض وخبايا التيارات الأثيرية.', svg: '<line x1=\"85\" y1=\"50\" x2=\"85\" y2=\"75\" stroke=\"#f4b41a\" stroke-width=\"2\"/><line x1=\"95\" y1=\"50\" x2=\"95\" y2=\"75\" stroke=\"#f4b41a\" stroke-width=\"2\"/><line x1=\"78\" y1=\"58\" x2=\"102\" y2=\"58\" stroke=\"#f4b41a\" stroke-width=\"2\"/><line x1=\"78\" y1=\"68\" x2=\"102\" y2=\"68\" stroke=\"#f4b41a\" stroke-width=\"2\"/>' },
        { id: 'ring_solomon', title: 'خاتم سليمان الكفي (Ring of Solomon)', source: 'الفراسة الملكية وتراث ابن عربي', desc: 'قوس نصف دائري يحيط بقاعدة السبابة على تل المشتري. دل في كتب الفراسة على الحكمة الفطرية، والقدرة على التدريس والوعظ والتأثير الروحي على الناس بهدوء واقتدار.', svg: '<path d=\"M 33 30 C 40 38, 50 38, 55 28\" fill=\"none\" stroke=\"#06d6a0\" stroke-width=\"3\"/><circle cx=\"44\" cy=\"33\" r=\"3\" fill=\"#f4b41a\"/>' },
        { id: 'st_andrews_cross', title: 'صليب النجاة والظفر (St. Andrew’s Cross)', source: 'تراث المخطوطات اللاتينية واليونانية', desc: 'تقاطع مائل على شكل حرف (X) يقع بمحاذاة خط الحياة قرب المعصم. اعتبر في الفراسة القديمة علامة 'الحصانة من المهالك والحوادث الخطيرة'، والنجاة المتكررة من الشدائد بألطاف خفية.', svg: '<line x1=\"45\" y1=\"65\" x2=\"60\" y2=\"80\" stroke=\"#10b981\" stroke-width=\"3\" stroke-linecap=\"round\"/><line x1=\"60\" y1=\"65\" x2=\"45\" y2=\"80\" stroke=\"#10b981\" stroke-width=\"3\" stroke-linecap=\"round\"/>' },
        { id: 'protective_square', title: 'المربع الحصين (The Protective Square)', source: 'علم قراءة الكف الكلاسيكي', desc: 'مربع مغلق يتشكل حول انقطاع أو كسر في خط الحياة أو خط الرأس. يرمز في التراث للحماية الإلهية الفائقة التي تمنع وقوع أثر الصدمات أو الأمراض، ويدل على الحصانة وتجدد العافية.', svg: '<rect x=\"52\" y=\"45\" width=\"26\" height=\"26\" fill=\"rgba(244,180,26,0.15)\" stroke=\"#f4b41a\" stroke-width=\"2\"/><line x1=\"65\" y1=\"35\" x2=\"65\" y2=\"80\" stroke=\"#ef4444\" stroke-width=\"2\" stroke-dasharray=\"3,2\"/>' },
        { id: 'mystic_eye', title: 'عين الصقر وبصيرة الإبهام (Yavarekha)', source: 'الفراسة الهندية (Samudrika) والتراث الصوفي', desc: 'خطان مقوسان يلتقيان عند الطرفين مشكلين حبة قمح أو عيناً بشرية مغلقة عند مفصل الإبهام الأول. تُسمى 'عين البصيرة'؛ تدل على صدق الرؤى والمنامات، والحاسة السادسة الفطرية التي تلتقط الأمور قبل وقوعها.', svg: '<path d=\"M 22 55 Q 32 45 42 55 Q 32 65 22 55 Z\" fill=\"none\" stroke=\"#00f0ff\" stroke-width=\"2.5\"/><circle cx=\"32\" cy=\"55\" r=\"3\" fill=\"#f4b41a\"/>' },
        { id: 'fish_sign', title: 'علامة السمكة والحوت (The Fish Sign)', source: 'سامودريكا شاسترا وتراث الحكماء', desc: 'خطان منحنيان يتقاطعان مشكلين جسماً وذيلاً يشبهان السمكة عند قاعدة خط الحياة قرب الرسغ. ترمز للبركة الأزلية، النجاة من المهالك المائية، والغنى المعرفي والروحي المفاجئ بعد تعب.', svg: '<path d=\"M 45 68 Q 55 62 65 72 Q 55 82 45 76 Z\" fill=\"none\" stroke=\"#06d6a0\" stroke-width=\"2.5\"/><line x1=\"65\" y1=\"72\" x2=\"75\" y2=\"65\" stroke=\"#06d6a0\" stroke-width=\"2\"/><line x1=\"65\" y1=\"72\" x2=\"75\" y2=\"79\" stroke=\"#06d6a0\" stroke-width=\"2\"/>' },
        { id: 'trident_seal', title: 'رمح ثلاثي الشعب والتاج (The Trident)', source: 'المخطوطات الشرقية والغربية المجمعة', desc: 'تشعب خط المصير أو خط الشمس في نهايته إلى ثلاثة فروع رمحية تصعد نحو تلال المشتري وزحل والشمس. ترمز للمجد والسيادة واجتماع الحكمة (زحل) مع الهيبة (المشتري) والتألق الإبداعي (الشمس).', svg: '<line x1=\"68\" y1=\"45\" x2=\"68\" y2=\"20\" stroke=\"#d8b4fe\" stroke-width=\"3\"/><path d=\"M 56 26 Q 68 36 68 36 Q 68 36 80 26\" fill=\"none\" stroke=\"#d8b4fe\" stroke-width=\"2.5\"/>' },
        { id: 'tree_of_life_palm', title: 'علامة شجرة الحياة (The Tree Sign)', source: 'علم الأسارير القديم وفراسة المعتمدين', desc: 'خط عمودي صاعد تتفرع منه خطوط دقيقة مائلة إلى الأعلى كأغصان الشجرة. ترمز للنمو الروحي المتصاعد، البركة في العمر والذرية، والقدرة على التجدد بعد كل انتكاسة.', svg: '<line x1=\"45\" y1=\"75\" x2=\"45\" y2=\"25\" stroke=\"#10b981\" stroke-width=\"3\"/><line x1=\"45\" y1=\"60\" x2=\"60\" y2=\"48\" stroke=\"#10b981\" stroke-width=\"2\"/><line x1=\"45\" y1=\"50\" x2=\"30\" y2=\"38\" stroke=\"#10b981\" stroke-width=\"2\"/><line x1=\"45\" y1=\"40\" x2=\"60\" y2=\"28\" stroke=\"#10b981\" stroke-width=\"2\"/>' },
        { id: 'lunar_crescent_palm', title: 'علامة الهلال القمري (The Lunar Crescent)', source: 'المخطوطات الفلكية والكوزمولوجية', desc: 'قوس هلالي مقوس على تل القمر عند الحافة السفلية للكف. يرمز لصفاء الإدراك الحدسي، الخيال الخصب، وجاذبية الحضور الروحي وقوة التأثير النفسي في النفوس.', svg: '<path d=\"M 90 50 A 18 18 0 0 0 90 75 A 12 12 0 0 1 90 50 Z\" fill=\"#60a5fa\"/>' },
        { id: 'arrow_of_will', title: 'علامة سهم الإرادة (The Arrow of Will)', source: 'مخطوطات الفراسة وسر الكف', desc: 'خط مستقيم حاد ينطلق من سهل المريخ وينتهي برأس سهم نحو تل المشتري. يدل في الفراسة على شدة العزيمة، القدرة على اقتناص الفرص الكبرى، والإصرار الذي لا يقهر أمام العقبات.', svg: '<line x1=\"55\" y1=\"65\" x2=\"40\" y2=\"30\" stroke=\"#f4b41a\" stroke-width=\"3\"/><polygon points=\"40,25 35,36 47,32\" fill=\"#f4b41a\"/>' },
        { id: 'scepter_sign', title: 'علامة الصولجان الملكي (The Scepter Sign)', source: 'تراث الملوك وقراءة الكف الأندلسية', desc: 'خط مستقيم يعلوه قرص دائري أو حلقة كاملة على تل الشمس (أبولو). دل في المخطوطات القديمة على نيل الجاه والشهرة والرياسة، وأن صاحب هذا الختم تتبعه القلوب بطاعة واحترام.', svg: '<line x1=\"75\" y1=\"65\" x2=\"75\" y2=\"28\" stroke=\"#f4b41a\" stroke-width=\"3\"/><circle cx=\"75\" cy=\"24\" r=\"6\" fill=\"#f4b41a\"/><circle cx=\"75\" cy=\"24\" r=\"3\" fill=\"#000\"/>' },
        { id: 'horseshoe_sign', title: 'حدوة الفرس الحصينة (The Horseshoe)', source: 'تراث الخواص والفولكلور القديم', desc: 'قوس مقلوب متقن عند قاعدة تل زحل أو وسط الكف. يرمز لتثبيت الأرزاق، طرد النحوسات والعوارض الطاقية، واستقرار الأحوال المادية والمعنوية.', svg: '<path d=\"M 58 45 C 58 32, 78 32, 78 45 L 78 52 C 78 55, 74 55, 74 52 L 74 45 C 74 38, 62 38, 62 45 L 62 52 C 62 55, 58 55, 58 52 Z\" fill=\"#94a3b8\"/>' },
        { id: 'lotus_petal', title: 'بتلة اللوتس والصفاء (The Lotus Petal)', source: 'الفراسة البوذية والمخطوطات العرفانية', desc: 'ثلاث بتلات ملتقية عند قاعدة الكف تشبه زهرة اللوتس. ترمز للطهارة الروحية، سلامة القلب من الغل والحسد، والارتقاء في المقامات الصوفية.', svg: '<path d=\"M 68 55 C 60 45, 60 35, 68 25 C 76 35, 76 45, 68 55 Z\" fill=\"rgba(216,180,254,0.3)\" stroke=\"#d8b4fe\" stroke-width=\"2\"/><path d=\"M 68 55 C 55 48, 50 40, 55 30 C 62 38, 65 48, 68 55 Z\" fill=\"none\" stroke=\"#d8b4fe\" stroke-width=\"1.5\"/><path d=\"M 68 55 C 81 48, 86 40, 81 30 C 74 38, 71 48, 68 55 Z\" fill=\"none\" stroke=\"#d8b4fe\" stroke-width=\"1.5\"/>' },
        { id: 'anchor_sign', title: 'علامة المرساة والرسوخ (The Anchor Sign)', source: 'أسرار الفراسة عند بحارة المتوسط', desc: 'خط عمودي ينتهي بقوس سفلي وسهمين يشبه مرساة السفينة عند الرسغ. دل على الرسوخ والأمان في الأسفار والنجاة من العواصف المادية والتقلبات النفسية.', svg: '<line x1=\"68\" y1=\"30\" x2=\"68\" y2=\"65\" stroke=\"#00f0ff\" stroke-width=\"3\"/><circle cx=\"68\" cy=\"26\" r=\"4\" fill=\"none\" stroke=\"#00f0ff\" stroke-width=\"2\"/><path d=\"M 52 55 Q 68 75 84 55\" fill=\"none\" stroke=\"#00f0ff\" stroke-width=\"3\"/><polygon points=\"52,53 50,60 56,58\" fill=\"#00f0ff\"/><polygon points=\"84,53 82,58 88,60\" fill=\"#00f0ff\"/>' },
        { id: 'girdle_venus', title: 'نطاق الزهرة والهلال الأثيري (Girdle of Venus)', source: 'تراث الفراسة والأسارير القديم', desc: 'قوس هلالي نصف دائري يمتد أعلى خط القلب، معلقاً بين ما بين السبابة والوسطى إلى ما بين البنصر والخنصر. علامة فرط الإحساس الوجداني، الذائقة الفنية العالية، والتقاط مشاعر ونوايا الآخرين بدقة مذهلة.', svg: '<path d=\"M 45 28 Q 75 48 105 30\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"3.5\"/>' },
        { id: 'line_of_intuition', title: 'خط الحدس الأثيري (Line of Intuition)', source: 'الكتب الهرمسية والباراسيكولوجيا التراثية', desc: 'خط نصف دائري مستقل ينطلق من تل القمر في أسفل الكف وينحني صاعداً نحو تل عطارد دون أن يمس خط المصير. يرمز للحدس التلقائي، التخاطر الروحي، واستشعار الوقائع قبل إعلانها.', svg: '<path d=\"M 90 70 C 110 50, 110 35, 95 25\" fill=\"none\" stroke=\"#00f0ff\" stroke-width=\"3\" stroke-dasharray=\"6,3\"/>' },
        { id: 'ring_of_saturn', title: 'حلقة زحل الصوفية (Ring of Saturn)', source: 'الفلسفة الفراسية وكتابات ابن سينا', desc: 'قوس نصف دائري يطوق قاعدة الإصبع الأوسط (الوسطى). يرمز في التراث للتأمل الفلسفي العميق، الزهد في بهارج الدنيا، والميل الفطري للبحث في أسرار الوجود والكون.', svg: '<path d=\"M 58 24 C 64 32, 72 32, 78 24\" fill=\"none\" stroke=\"#94a3b8\" stroke-width=\"3\"/>' },
        { id: 'ring_of_apollo', title: 'طوق الشمس وأبولو (Ring of Apollo)', source: 'فراسة الحكماء والجماليات', desc: 'قوس مقوس ناعم يطوق قاعدة إصبع البنصر على تل الشمس. يدل على الذائقة الجمالية الرفيعة، الكاريزما الجذابة، وحب الضياء والنور في الفكر والعمل.', svg: '<path d=\"M 75 24 C 81 32, 89 32, 95 24\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"3\"/>' },
        { id: 'healer_stigmata', title: 'خطوط الشفاء والمعلم (Medical Stigmata)', source: 'تراث الطب القديم وفراسة الأطباء', desc: 'ثلاثة إلى أربعة خطوط عمودية دقيقة متوازية على تل عطارد تحت الخنصر. تسمى 'علامات الشفاء'؛ وتدل على موهبة فطرية في الطب، المواساة، والقدرة على تهدئة آلام الآخرين بحسن المنطق.', svg: '<line x1=\"88\" y1=\"26\" x2=\"88\" y2=\"44\" stroke=\"#10b981\" stroke-width=\"2.5\"/><line x1=\"93\" y1=\"25\" x2=\"93\" y2=\"45\" stroke=\"#10b981\" stroke-width=\"2.5\"/><line x1=\"98\" y1=\"26\" x2=\"98\" y2=\"44\" stroke=\"#10b981\" stroke-width=\"2.5\"/><line x1=\"103\" y1=\"28\" x2=\"103\" y2=\"42\" stroke=\"#10b981\" stroke-width=\"2.5\"/>' },
        { id: 'line_of_sympathy', title: 'خط التعاطف الوجداني (Line of Sympathy)', source: 'علم الأسارير والوجدانيات', desc: 'خط مائل ينحدر بلطف من تل المشتري باتجاه خط الرأس والقلب. يدل على رقة القلب، التعاطف الإنساني الفطري مع الضعفاء، والقدرة على احتواء النفوس الحزينة.', svg: '<path d=\"M 38 28 C 45 38, 55 45, 65 48\" fill=\"none\" stroke=\"#ec4899\" stroke-width=\"2.5\"/>' },
        { id: 'royal_rascettes', title: 'أساور الرسغ الملكية الثلاثة (The Rascettes)', source: 'أصول الفراسة عند أرسطو واليونان', desc: 'ثلاثة خطوط أفقية متوازية عميقة عند مفصل الكف مع الساعد. كل سوار منها كان يرمز في الفراسة القديمة لثلاثين عاماً من الصحة والحيوية، وتكاملها الثلاثي علامة التوازن التام بين الجسد والعقل والروح.', svg: '<path d=\"M 35 78 Q 70 72 105 78\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"3\"/><path d=\"M 38 83 Q 70 78 102 83\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"2.5\"/><path d=\"M 42 88 Q 70 84 98 88\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"2\"/>' },
        { id: 'mars_guardian_line', title: 'خط الحارس الأثيري (Mars Guardian Line)', source: 'مخطوطات شمس المعارف والخواص', desc: 'خط يمتد موازياً لخط الحياة من الداخل في سهل المريخ والزهرة. يسمى 'الملاك الحارس'؛ يرمز لبطانة حيوية ومناعة قوية تحمي البدن من التلف والأخطار الخارجية.', svg: '<path d=\"M 38 42 C 40 55, 48 70, 58 78\" fill=\"none\" stroke=\"#ef4444\" stroke-width=\"3\"/><path d=\"M 45 44 C 47 55, 54 68, 62 75\" fill=\"none\" stroke=\"#f4b41a\" stroke-width=\"2\" stroke-dasharray=\"4,2\"/>' },
        { id: 'clairvoyance_line', title: 'خط الكشف الرؤيوي (Line of Clairvoyance)', source: 'المصنفات الهرمسية والغنوصية القديمة', desc: 'خط عميق مقوس ينطلق من عمق تل القمر متجهاً نحو سهل المريخ وخط الرأس. يدل على قوة الأحلام التحذيرية، استشعار الطاقة الكامنة في الأماكن، والصفاء الذهني التام.', svg: '<path d=\"M 95 65 Q 85 45 70 42\" fill=\"none\" stroke=\"#a855f7\" stroke-width=\"3\"/>' },
        { id: 'twin_stars', title: 'ختم النجم المزدوج (The Twin Stars)', source: 'أعظم طوالع الفراسة في المخطوطات الأندلسية', desc: 'نجمتان خماسيتان أو سداسيتان تتطابقان معاً: الأولى على تل المشتري (الهيبة والرياسة) والثانية على تل الشمس (المجد والبريق). اعتبرت أندر علامة فراسية تدل على الخلود المعرفي واجتماع الحكمة مع التأثير الواسع.', svg: '<polygon points=\"40,22 43,30 51,30 45,35 47,43 40,38 33,43 35,35 29,30 37,30\" fill=\"#f4b41a\"/><polygon points=\"85,22 88,30 96,30 90,35 92,43 85,38 78,43 80,35 74,30 82,30\" fill=\"#f4b41a\"/>' },
        { id: 'saturn_sigil', title: 'طلسم زحل (أجيئيل)', source: 'Agrippa - De Occulta Philosophia', desc: 'مبني على الوفق المثلث 3×3، يستجلب طاقة التثبيت والانضباط الصارم.', svg: '<line x1="20" y1="20" x2="80" y2="20" stroke="#94a3b8" stroke-width="4"/><line x1="50" y1="20" x2="50" y2="80" stroke="#94a3b8" stroke-width="4"/><circle cx="50" cy="80" r="5" fill="#94a3b8"/>' },
        { id: 'jupiter_sigil', title: 'طلسم المشتري (يوفائيل)', source: 'Picatrix / غاية الحكيم', desc: 'مبني على الوفق المربع 4×4، يجذب طاقة التوسع والهيبة وسعة الرزق.', svg: '<path d="M 25 25 L 50 75 L 75 25" fill="none" stroke="#d8b4fe" stroke-width="4"/><line x1="35" y1="50" x2="65" y2="50" stroke="#d8b4fe" stroke-width="4"/>' },
        { id: 'mars_sigil', title: 'طلسم المريخ (غرافائيل)', source: 'Agrippa Lib. II', desc: 'مبني على الوفق المخمس 5×5، يركز طاقة الحسم والشجاعة ودحر العدوان.', svg: '<line x1="20" y1="50" x2="80" y2="50" stroke="#ef4444" stroke-width="4"/><line x1="50" y1="20" x2="50" y2="80" stroke="#ef4444" stroke-width="4"/><polygon points="80,50 65,40 65,60" fill="#ef4444"/>' },
        { id: 'sun_sigil', title: 'طلسم الشمس (ناخيئيل)', source: 'شمس المعارف وبسط الحروف', desc: 'مبني على الوفق المسدس 6×6، يعزز الحيوية الجسدية والإشراق القيادي.', svg: '<circle cx="50" cy="50" r="28" fill="none" stroke="#f4b41a" stroke-width="4"/><circle cx="50" cy="50" r="7" fill="#f4b41a"/>' },
        { id: 'venus_sigil', title: 'طلسم الزهرة (هاجيئيل)', source: 'غاية الحكيم والمجريطي', desc: 'مبني على الوفق المسبع 7×7، يولد تردد الألفة والمحبة وتناغم المشاعر.', svg: '<circle cx="50" cy="35" r="18" fill="none" stroke="#06d6a0" stroke-width="4"/><line x1="50" y1="53" x2="50" y2="85" stroke="#06d6a0" stroke-width="4"/><line x1="35" y1="70" x2="65" y2="70" stroke="#06d6a0" stroke-width="4"/>' },
        { id: 'mercury_sigil', title: 'طلسم عطارد (تيريئيل)', source: 'Agrippa Kamea', desc: 'مبني على الوفق المثمن 8×8، يمنح سرعة الاستيعاب والفصاحة والتجارة.', svg: '<path d="M 35 15 C 45 25, 55 25, 65 15" fill="none" stroke="#00f0ff" stroke-width="3"/><circle cx="50" cy="40" r="15" fill="none" stroke="#00f0ff" stroke-width="3"/><line x1="50" y1="55" x2="50" y2="85" stroke="#00f0ff" stroke-width="3"/><line x1="35" y1="70" x2="65" y2="70" stroke="#00f0ff" stroke-width="3"/>' },
        { id: 'moon_sigil', title: 'طلسم القمر (ملكيئيل)', source: 'أسرار الحكماء', desc: 'مبني على الوفق المتسع 9×9، ينشط الإدراك الحدسي والأحلام الصادقة.', svg: '<path d="M 40 20 A 30 30 0 0 0 40 80 A 22 22 0 0 1 40 20 Z" fill="#60a5fa"/>' }
    ];

    function switchSealsSubView(targetId) {
        document.querySelectorAll('.seals-sub-container').forEach(c => {
            c.classList.remove('active');
            c.style.display = 'none';
        });
        document.querySelectorAll('.seals-subnav-btn').forEach(b => b.classList.remove('active'));

        const targetEl = document.getElementById(targetId);
        if (targetEl) {
            targetEl.classList.add('active');
            targetEl.style.display = 'block';
        }

        if (event && event.target) {
            event.target.classList.add('active');
        }

        if (targetId === 'seals-view-ghazali') {
            computeLiveGhazaliWafq();
        }
    }

    function computeLiveGhazaliWafq() {
        const input = document.getElementById('ghazali-target-sum');
        const resultDiv = document.getElementById('ghazali-calc-result');
        if (!input || !resultDiv) return;

        let N = parseInt(input.value);
        if (isNaN(N) || N < 15) {
            resultDiv.innerHTML = '<span style="color:#ef4444; font-weight:700;">يرجى إدخال عدد صحيح يساوي 15 أو أكبر.</span>';
            return;
        }

        // Classical rule of Al-Ghazali and ancient mathematicians:
        // As (Base) of 3x3 is 12: K = (N - 12) / 3
        const remainder = (N - 12) % 3;
        const K = Math.floor((N - 12) / 3);

        let c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 1-indexed
        for (let i = 1; i <= 9; i++) {
            let val = K + (i - 1);
            if (remainder === 1 && i >= 7) val += 1;
            if (remainder === 2 && i >= 4) val += 1;
            c[i] = val;
        }

        // Matrix placement in standard Batad Zahaj Wah:
        // row 0: c[4], c[9], c[2]
        // row 1: c[3], c[5], c[7]
        // row 2: c[8], c[1], c[6]
        const r0 = [c[4], c[9], c[2]];
        const r1 = [c[3], c[5], c[7]];
        const r2 = [c[8], c[1], c[6]];

        const sumR0 = r0[0] + r0[1] + r0[2];

        let jabrText = remainder === 0 ? 'الوفق تام بدون كسر (قسمة صحيحة).' :
                       remainder === 1 ? 'الكسر = 1 (جُبر في البيت السابع بزيادة 1 على البيوت 7، 8، 9).' :
                                         'الكسر = 2 (جُبر في البيت الرابع بزيادة 1 على البيوت 4 إلى 9).';

        resultDiv.innerHTML = `
            <div style="margin-bottom:12px; font-size:0.88rem; color:#cbd5e1; line-height:1.7;">
                <strong>المفتاح (البيت 1):</strong> <span style="color:var(--gold); font-weight:700;">${c[1]}</span> | 
                <strong>المغلاق (البيت 9):</strong> <span style="color:var(--gold); font-weight:700;">${c[9]}</span> | 
                <strong>العدل (المفتاح+المغلاق):</strong> <span style="color:var(--cyan); font-weight:700;">${c[1] + c[9]}</span> | 
                <strong>حالة الجبر:</strong> <span style="color:#a78bfa;">${jabrText}</span>
            </div>
            <div style="display:inline-grid; grid-template-columns:repeat(3, 75px); grid-gap:8px; margin-bottom:12px; direction:ltr;">
                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); padding:12px; border-radius:8px; font-weight:800; color:var(--gold); font-size:1.15rem;">${r0[0]}</div>
                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); padding:12px; border-radius:8px; font-weight:800; color:var(--cyan); font-size:1.15rem;">${r0[1]}</div>
                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); padding:12px; border-radius:8px; font-weight:800; color:var(--gold); font-size:1.15rem;">${r0[2]}</div>
                
                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); padding:12px; border-radius:8px; font-weight:800; color:var(--cyan); font-size:1.15rem;">${r1[0]}</div>
                <div style="background:rgba(239,68,68,0.2); border:2px solid #ef4444; padding:12px; border-radius:8px; font-weight:900; color:#fff; font-size:1.25rem;">${r1[1]}</div>
                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); padding:12px; border-radius:8px; font-weight:800; color:var(--cyan); font-size:1.15rem;">${r1[2]}</div>
                
                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); padding:12px; border-radius:8px; font-weight:800; color:var(--gold); font-size:1.15rem;">${r2[0]}</div>
                <div style="background:rgba(0,240,255,0.15); border:1px solid var(--cyan); padding:12px; border-radius:8px; font-weight:800; color:var(--cyan); font-size:1.15rem;">${r2[1]}</div>
                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); padding:12px; border-radius:8px; font-weight:800; color:var(--gold); font-size:1.15rem;">${r2[2]}</div>
            </div>
            <div style="font-size:0.82rem; color:#10b981; font-weight:700;">
                ✓ مجموع كل صف وكل عمود = ${sumR0} (مطابق للعدد المطلوب ${N} بنسبة 100%).
            </div>
        `;
    }

    function renderInteractiveSigils() {
        const grid = document.getElementById('seals-interactive-grid');
        if (!grid) return;

        grid.innerHTML = INTERACTIVE_SIGILS_DATA.map(sig => `
            <div onclick="previewSigil('${sig.id}')" style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:12px; text-align:center; cursor:pointer; transition:all 0.2s;" onmouseover="this.style.borderColor='var(--emerald)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.1)'">
                <svg width="60" height="60" viewBox="0 0 100 100" style="margin-bottom:8px;">
                    ${sig.svg}
                </svg>
                <span style="display:block; font-size:0.75rem; color:#cbd5e1; font-weight:700;">${sig.title}</span>
            </div>
        `).join('');
    }

    function previewSigil(sigId) {
        const sig = INTERACTIVE_SIGILS_DATA.find(s => s.id === sigId);
        if (!sig) return;

        const modal = document.getElementById('seal-preview-modal');
        const display = document.getElementById('modal-svg-display');
        const title = document.getElementById('modal-title');
        const desc = document.getElementById('modal-desc');

        if (modal && display && title && desc) {
            display.innerHTML = `<svg width="100" height="100" viewBox="0 0 100 100">${sig.svg}</svg>`;
            title.innerText = `${sig.title} (${sig.source})`;
            desc.innerText = sig.desc;
            modal.style.display = 'block';
            modal.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }

    // Auto-run on load
    window.addEventListener('load', () => {
        renderInteractiveSigils();
        computeLiveGhazaliWafq();
    });
    '''

if __name__ == "__main__":
    print("Testing generate_seals_zouhri_chamber.py module...")
    html = get_seals_zouhri_chamber_html()
    js = get_seals_zouhri_chamber_js()
    print(f"Generated HTML size: {len(html):,} bytes")
    print(f"Generated JS size: {len(js):,} bytes")
