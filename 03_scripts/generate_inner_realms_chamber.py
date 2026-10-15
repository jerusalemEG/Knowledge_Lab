# -*- coding: utf-8 -*-
"""
Knowledge Lab - Esoteric Inner Realms, Etheric Anatomy & Consciousness Odyssey (Chamber 20)
Modules:
1. Subterranean Realms & Hidden Lands (Agartha, Shambhala, Mundus Archetypus, Jabalka & Jabarsa, Geology vs Myth).
2. Etheric Anatomy, Qareen & Energetic Hygiene (Theosophical Thought-Forms, The Shadow Archetype, Cognitive & Psychic Cleansing).
3. The Odyssey of Consciousness: Astral Projection (Historical Evolution, Sylvan Muldoon & Robert Monroe, Neurobiology of OOBE).
4. The Metaphysics of Wafq & Transcendent Archetypes (Prophetic Matrices, Why the Muhammadan Reality Transcends Finite Squares).
5. Interactive Brainwave & Consciousness Harmonizer Studio (Binaural Wave Simulator, Energetic Balance Diagnostic).
"""

def get_inner_realms_chamber_html():
    return '''
    <!-- CHAMBER 20: INNER REALMS, ETHERIC ANATOMY & ASTRAL CONSCIOUSNESS (#tab-inner-realms) -->
    <div id="tab-inner-realms" class="tab-content chamber-view">
        <div class="content-container" style="max-width:1400px; margin:0 auto; padding:20px 15px;">
            
            <!-- CHAMBER HERO -->
            <div style="background:linear-gradient(135deg, rgba(8,18,36,0.96), rgba(3,6,17,0.98)); border:1px solid rgba(56,189,248,0.35); border-radius:24px; padding:35px 25px; margin-bottom:30px; position:relative; overflow:hidden; box-shadow:0 15px 45px rgba(0,0,0,0.7);">
                <div style="position:absolute; top:-30px; left:-30px; width:260px; height:260px; background:radial-gradient(circle, rgba(56,189,248,0.18) 0%, transparent 70%); pointer-events:none;"></div>
                <div style="position:absolute; bottom:-40px; right:-40px; width:260px; height:260px; background:radial-gradient(circle, rgba(168,85,247,0.15) 0%, transparent 70%); pointer-events:none;"></div>
                
                <div style="display:flex; align-items:center; gap:16px; margin-bottom:12px; flex-wrap:wrap;">
                    <span style="background:rgba(56,189,248,0.18); border:1px solid #38bdf8; color:#38bdf8; padding:5px 14px; border-radius:20px; font-size:0.85rem; font-weight:700;">
                        🪐 الركن الرابع: ديوان العوالم الخفية وسفر الوعي
                    </span>
                    <span style="background:rgba(148, 163, 184,0.14); border:1px solid var(--gold); color:var(--gold); padding:5px 14px; border-radius:20px; font-size:0.85rem; font-weight:700;">
                        الباب 20 • دراسة مقارنة ومختبر تفاعلي
                    </span>
                </div>
                
                <h1 style="font-family:'Amiri', serif; font-size:2.4rem; color:#f1f5f9; margin:10px 0 15px 0; text-shadow:0 0 25px rgba(56,189,248,0.4);">
                    سفر العوالم الباطنية، الجسد الأثيري، وأسرار الوعي
                </h1>
                
                <p style="font-size:1.05rem; color:#94a3b8; line-height:1.8; max-width:1050px; margin:0;">
                    موسوعة فكرية ومختبر استكشافي يجمع بين أساطير الأراضي الباطنية المحجوبة عبر الحضارات (أغارثا وعوالم المثال والسهروردي)، وتشريح الهالة والقرين وتنقية الحقول الذهنية من شوائب الإجهاد وفق المدارس الفلسفية والثيوصوفية، والتحليل التاريخي والعصبي لظاهرة الإسقاط النجمي (Astral Projection)، مع تفكيك فلسفة الأوفاق الرياضية وتنزيه الحقيقة المحمدية عن الحصر العددي.
                </p>
            </div>

            <!-- SUB-NAVIGATION TABS -->
            <div style="display:flex; gap:10px; overflow-x:auto; padding-bottom:12px; margin-bottom:28px; border-bottom:1px solid rgba(255,255,255,0.08); scrollbar-width:thin;">
                <button class="inner-tab-pill active" onclick="switchInnerRealmsSubTab('inner-sub-subterranean')" id="pill-inner-subterranean">
                    🗺️ ١. الأراضي الباطنية وأساطير باطن الأرض
                </button>
                <button class="inner-tab-pill" onclick="switchInnerRealmsSubTab('inner-sub-etheric')" id="pill-inner-etheric">
                    🛡️ ٢. تشريح الهالة، القرين، والتنقية الأثيرية
                </button>
                <button class="inner-tab-pill" onclick="switchInnerRealmsSubTab('inner-sub-astral')" id="pill-inner-astral">
                    ✨ ٣. سفر الوعي والإسقاط النجمي (Astral Odyssey)
                </button>
                <button class="inner-tab-pill" onclick="switchInnerRealmsSubTab('inner-sub-prophetic-wafq')" id="pill-inner-prophetic-wafq">
                    ⚖️ ٤. سر الأوفاق وتنزيه الحقيقة المحمدية
                </button>
                <button class="inner-tab-pill" onclick="switchInnerRealmsSubTab('inner-sub-lab')" id="pill-inner-lab">
                    🧪 ٥. مختبر توازن الوعي ومحاكي الترددات
                </button>
            </div>

            <!-- ========================================== -->
            <!-- SECTION 1: SUBTERRANEAN REALMS & HIDDEN LANDS -->
            <!-- ========================================== -->
            <div id="inner-sub-subterranean" class="inner-sub-view active">
                <div style="background:rgba(11,17,33,0.85); border:1px solid rgba(56,189,248,0.25); border-radius:20px; padding:30px; margin-bottom:30px;">
                    <div style="display:flex; align-items:center; gap:12px; margin-bottom:18px;">
                        <span style="font-size:2rem;">🗺️</span>
                        <div>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#38bdf8; margin:0;">
                                الأراضي الباطنية والكون المحجوب: بين الميثولوجيا وعوالم الرمز
                            </h2>
                            <span style="color:#94a3b8; font-size:0.9rem;">دراسة مقارنة بين أساطير أغارثا التبتية، وعالم المثال الإشراقي، وحقائق الجيولوجيا الحديثة</span>
                        </div>
                    </div>

                    <p style="color:#475569; line-height:1.85; font-size:1.02rem; margin-bottom:25px;">
                        شغلت فكرة "العوالم المحجوبة داخل الأرض" مخيلة الحضارات الإنسانية منذ فجر التاريخ. فلم تكن الأرض في وعي القدماء مجرد كتلة صماء من الصخور والمعادن، بل كائناً حياً يحوي أروقة باطنية، وأنهاراً سفلية، وحضارات مخبأة وراء بوابات قطبية أو كهوف عميقة، حيث يلتقي الحكماء بعيداً عن اضطرابات السطح.
                    </p>

                    <!-- COMPARATIVE 3-COLUMNS MATRIX -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-bottom:30px;">
                        
                        <!-- CARD 1: AGARTHA & SHAMBHALA -->
                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(56,189,248,0.2); border-radius:16px; padding:22px;">
                            <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
                                <span style="font-size:1.5rem;">🏔️</span>
                                <h3 style="color:#38bdf8; font-size:1.2rem; margin:0; font-family:'Amiri',serif;">أغارثا وشامبالا (التبت والشرق الأقصى)</h3>
                            </div>
                            <p style="color:#94a3b8; font-size:0.92rem; line-height:1.75; margin-bottom:12px;">
                                في المعتقدات الفيدية والبوذية التبتية، يُشار إلى <strong>شامبالا (Shambhala)</strong> كأرض مقدسة يسودها الصفاء الروحي، بينما تطورت في الأدبيات الثيوصوفية في القرنين التاسع عشر والعشرين أسطورة <strong>أغارثا (Agartha)</strong> كشبكة أنفاق تمتد في باطن الأرض يحكمها "ملك العالم" (King of the World).
                            </p>
                            <div style="background:rgba(0,0,0,0.3); border-radius:10px; padding:12px; font-size:0.85rem; color:#475569;">
                                <strong style="color:var(--gold);">الرمزية الفلسفية:</strong> ترمز أغارثا إلى "المركز الروحي الباطن" في قلب الإنسان، حيث الحكمة النقية المحجوبة عن حواس السطح الصاخبة.
                            </div>
                        </div>

                        <!-- CARD 2: MUNDUS ARCHETYPUS & SUHRAWARDI -->
                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(168,85,247,0.25); border-radius:16px; padding:22px;">
                            <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
                                <span style="font-size:1.5rem;">🌌</span>
                                <h3 style="color:#d8b4fe; font-size:1.2rem; margin:0; font-family:'Amiri',serif;">عالم المثال وجابلقا وجابرسا (السهروردي وابن عربي)</h3>
                            </div>
                            <p style="color:#94a3b8; font-size:0.92rem; line-height:1.75; margin-bottom:12px;">
                                في الفلسفة الإشراقية عند شهاب الدين السهروردي وميتافيزيقا محيي الدين بن عربي، يُطرح مفهوم <strong>عالم المثال والملكوت (Mundus Archetypus)</strong> و"أرض الحقيقة" التي تقع وراء جبل قاف، وتضم مدينتي <strong>جابلقا</strong> (في أقصى المشرق) و<strong>جابرسا</strong> (في أقصى المغرب).
                            </p>
                            <div style="background:rgba(0,0,0,0.3); border-radius:10px; padding:12px; font-size:0.85rem; color:#475569;">
                                <strong style="color:#d8b4fe;">المعنى العرفاني:</strong> هذه المدن ليست تضاريس مادية قابلة للحفر والمسح الجغرافي، بل هي أبعاد لطيفة تتجسد فيها المعاني والأرواح بصور مثالية خيالية.
                            </div>
                        </div>

                        <!-- CARD 3: GEOLOGY VS HOLLOW EARTH -->
                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(6,214,160,0.25); border-radius:16px; padding:22px;">
                            <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
                                <span style="font-size:1.5rem;">🌍</span>
                                <h3 style="color:#06d6a0; font-size:1.2rem; margin:0; font-family:'Amiri',serif;">الحقيقة الجيولوجية والفيزيائية</h3>
                            </div>
                            <p style="color:#94a3b8; font-size:0.92rem; line-height:1.75; margin-bottom:12px;">
                                أثبتت علوم الزلازل والموجات الارتدادية الجيولوجية (Seismology) في القرن العشرين والواحد والعشرين أن الأرض مكونة من طبقات مصمتة ومضغوطة: القشرة الصخرية، الوشاح الصلب واللزج، اللب الخارجي المنصهر (حديد ونيكل عند 4000° مئوية)، واللب الداخلي الصلب فائق الكثافة.
                            </p>
                            <div style="background:rgba(0,0,0,0.3); border-radius:10px; padding:12px; font-size:0.85rem; color:#475569;">
                                <strong style="color:#06d6a0;">الخلاصة العلمية:</strong> تنعدم أي فراغات جوفاء أو أراضٍ داخلية قادرة على إيواء حياة بيولوجية، مما يؤكد أن نصوص الأراضي الباطنية نصوص أدبية ومجازية صرفة.
                            </div>
                        </div>
                    </div>

                    <!-- SUBTERRANEAN EXPLORER INTERACTIVE COMPONENT -->
                    <div style="background:rgba(0,0,0,0.4); border:1px dashed rgba(56,189,248,0.3); border-radius:16px; padding:22px;">
                        <h4 style="color:#38bdf8; margin:0 0 10px 0; font-family:'Amiri',serif; font-size:1.2rem;">
                            🧭 مستكشف طبقات الأرض بين الرؤية الرمزية والجيولوجية:
                        </h4>
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:15px;">
                            <button onclick="inspectSubterraneanLayer('crust')" class="layer-pill-btn active" id="layer-btn-crust">القشرة السطحية (عالم الشهادة)</button>
                            <button onclick="inspectSubterraneanLayer('mantle')" class="layer-pill-btn" id="layer-btn-mantle">الوشاح العلوي (عوالم البرزخ الرمزي)</button>
                            <button onclick="inspectSubterraneanLayer('agartha')" class="layer-pill-btn" id="layer-btn-agartha">أغارثا والمدن الباطنية (المجاز الأسطوري)</button>
                            <button onclick="inspectSubterraneanLayer('core')" class="layer-pill-btn" id="layer-btn-core">اللب المنصهر والمركز المغناطيسي</button>
                        </div>
                        <div id="subterranean-inspector-display" style="background:rgba(15,23,42,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:12px; padding:18px; color:#475569; font-size:0.95rem; line-height:1.7;">
                            اختر إحدى الطبقات لاستعراض التوازي بين الحقيقة الجيولوجية والرمزية الميثولوجية القديمة.
                        </div>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- SECTION 2: ETHERIC ANATOMY & ENERGETIC HYGIENE -->
            <!-- ========================================== -->
            <div id="inner-sub-etheric" class="inner-sub-view">
                <div style="background:rgba(11,17,33,0.85); border:1px solid rgba(168,85,247,0.3); border-radius:20px; padding:30px; margin-bottom:30px;">
                    <div style="display:flex; align-items:center; gap:12px; margin-bottom:18px;">
                        <span style="font-size:2rem;">🛡️</span>
                        <div>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#d8b4fe; margin:0;">
                                تشريح الهالة الأثيرية، القرين، والتنقية الإدراكية
                            </h2>
                            <span style="color:#94a3b8; font-size:0.9rem;">تفكيك أوهام "الطفيلات الأثيرية" نحو منهج النقاء النفسي والحصانة العصبية المعرفية</span>
                        </div>
                    </div>

                    <p style="color:#475569; line-height:1.85; font-size:1.02rem; margin-bottom:25px;">
                        تزخر الأدبيات الباطنية والمدارس الروحية الحديثة بمفاهيم مثل "القرين"، و"الطفيلات الأثيرية" (Astral Parasites)، واليرقات الفكرية (Larvae). وعند دراسة هذه المفاهيم بعين الفحص العلمي والتحليلي، يتضح أنها تمثيلات استعارية ومجازية لحالات الإرهاق العصبي، والوساوس القهرية، والضغوط النفسية المتراكمة.
                    </p>

                    <!-- DUAL COMPARISON: OCCULT MYTH VS NEURO-PSYCHOLOGY -->
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-bottom:30px;" class="dual-grid-responsive">
                        
                        <!-- ESOTERIC TRADITION -->
                        <div style="background:rgba(26,16,40,0.6); border:1px solid rgba(168,85,247,0.25); border-radius:16px; padding:22px;">
                            <h3 style="color:#d8b4fe; font-family:'Amiri',serif; font-size:1.3rem; margin-top:0; margin-bottom:12px;">
                                📜 ما قالته الأدبيات الثيوصوفية والباطنية
                            </h3>
                            <ul style="color:#475569; font-size:0.93rem; line-height:1.85; padding-right:20px; margin:0;">
                                <li><strong>الصور الفكرية (Thought-Forms):</strong> يرى كتاب *Thought-Forms* (ليدبيتر وبيزانت 1901) أن كل فكرة مشحونة بانفعال قوي تولد شكلاً طاقياً يسبح في الهالة المحيطة بالإنسان.</li>
                                <li><strong>اليرقات والطفيلات:</strong> تفترض كتب الماجيك القديم أن الأفكار السوداوية والإدمان يجلب كائنات غير مرئية تقتات على الطاقة الحيوية للإنسان.</li>
                                <li><strong>القرين:</strong> وُصف تارة بأنه الكيان المصاحب المائل للوسوسة وتارة بأنه النظير الباطني غير المرئي للإنسان.</li>
                            </ul>
                        </div>

                        <!-- NEURO-PSYCHOLOGICAL TRUTH -->
                        <div style="background:rgba(8,24,36,0.6); border:1px solid rgba(56,189,248,0.25); border-radius:16px; padding:22px;">
                            <h3 style="color:#38bdf8; font-family:'Amiri',serif; font-size:1.3rem; margin-top:0; margin-bottom:12px;">
                                🧠 الرؤية العلمية والنفسية المعاصرة
                            </h3>
                            <ul style="color:#475569; font-size:0.93rem; line-height:1.85; padding-right:20px; margin:0;">
                                <li><strong>الظل النفسي (Carl Jung's Shadow):</strong> القرين هو انعكاس رمزي دقيق لـ "الظل النفسي" في التحليل النفسي؛ وهو مجموع الرغبات المكبوتة والمخاوف غير المعالجة في اللاشعور.</li>
                                <li><strong>حلقة الاستنزاف العصبي (Cognitive Rumination):</strong> "الطفيلات" ليست كائنات خارجية، بل هي حلقة الاجترار الذهني (Rumination) وزيادة نشاط شبكة الوضع الافتراضي (DMN) في الدماغ عند القلق.</li>
                                <li><strong>تفسير الشعور بالثقل:</strong> الإحساس بالثقل في الصدر أو الأطراف ناتج فيزيولوجياً عن ارتفاع هرمون الكورتيزول وتشنج الألياف العضلية السطحية.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- 4 PILLARS OF REAL COGNITIVE & ENERGETIC HYGIENE -->
                    <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(244,180,26,0.25); border-radius:16px; padding:24px;">
                        <h3 style="color:var(--gold); font-family:'Amiri',serif; font-size:1.35rem; margin-top:0; margin-bottom:16px;">
                            ✨ الأركان الحقيقية للتنقية الإدراكية والتناغم الداخلي (Cognitive Hygiene)
                        </h3>
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:16px;">
                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:16px;">
                                <div style="color:#00f0ff; font-weight:700; margin-bottom:6px;">١. تفريغ الاجترار الذهني</div>
                                <div style="color:#94a3b8; font-size:0.87rem; line-height:1.6;">كتابة الأفكار وتفريغها كتابياً يوقف تكرار الإشارات العصبية الضاغطة في الفص الجبهي.</div>
                            </div>
                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:16px;">
                                <div style="color:#06d6a0; font-weight:700; margin-bottom:6px;">٢. ضبط الإيقاع الحيوي للنوم</div>
                                <div style="color:#94a3b8; font-size:0.87rem; line-height:1.6;">النوم المنتظم (7-8 ساعات) يفعّل الجهاز الغليمفاوي (Glymphatic System) لغسل السموم العصبية بالدماغ.</div>
                            </div>
                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:16px;">
                                <div style="color:#94a3b8; font-weight:700; margin-bottom:6px;">٣. التنفس المتناغم (Coherence)</div>
                                <div style="color:#94a3b8; font-size:0.87rem; line-height:1.6;">تنفس الصندوق (4-4-4-4) يخفض استثارة العصب الحائر ويعيد توازن ضربات القلب والجهاز العصبي السمبثاوي.</div>
                            </div>
                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:16px;">
                                <div style="color:#a855f7; font-weight:700; margin-bottom:6px;">٤. اليقظة والذكر القلبي</div>
                                <div style="color:#94a3b8; font-size:0.87rem; line-height:1.6;">استحضار الصفاء والسكينة القلبية يمنح مناعة وجدانية ضد الاستسلام للأوهام والمخاوف المفرطة.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- SECTION 3: ASTRAL PROJECTION & ODYSSEY -->
            <!-- ========================================== -->
            <div id="inner-sub-astral" class="inner-sub-view">
                <div style="background:rgba(11,17,33,0.85); border:1px solid rgba(0,240,255,0.28); border-radius:20px; padding:30px; margin-bottom:30px;">
                    <div style="display:flex; align-items:center; gap:12px; margin-bottom:18px;">
                        <span style="font-size:2rem;">✨</span>
                        <div>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:var(--cyan-accent); margin:0;">
                                سفر الوعي والإسقاط النجمي (Astral Projection): التاريخ والمراحل والعلوم
                            </h2>
                            <span style="color:#94a3b8; font-size:0.9rem;">تتبع تجارب الخروج من الجسد من نصوص الفراعنة إلى معهد مونرو وعلم الأعصاب الحديث</span>
                        </div>
                    </div>

                    <p style="color:#475569; line-height:1.85; font-size:1.02rem; margin-bottom:25px;">
                        يُعرّف <strong>الإسقاط النجمي (Astral Projection)</strong> أو ما يُصطلح عليه علمياً بـ <em>تجارب الخروج من الجسد (Out-of-Body Experiences - OBE)</em> بأنه حالة وعي يشعر فيها الفرد بانفصال إدراكه البصري والحسي عن جسده المادي. ارتبطت هذه التجربة بأساطير السفر الروحي عبر الأكوان، بينما أثبتت الدراسات العصبية المعاصرة أنها نتاج آليات دماغية مذهلة تحدث أثناء اضطراب التزامن الإدراكي.
                    </p>

                    <!-- 4 STAGES ACCORDING TO ESOTERIC LITERATURE -->
                    <h3 style="color:#00f0ff; font-family:'Amiri',serif; font-size:1.35rem; margin-bottom:15px;">
                        📜 مراحل التجربة كما وصفتها الأدبيات الكلاسيكية (مولدون، معهد مونرو، بريز):
                    </h3>
                    
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:18px; margin-bottom:30px;">
                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(0,240,255,0.2); border-radius:14px; padding:18px;">
                            <div style="font-size:1.2rem; color:var(--gold); font-weight:700; margin-bottom:8px;">١. جسر الألفا والثيتا (Alpha-Theta Bridge)</div>
                            <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                استرخاء عضلي كامل يدخل الدماغ في حالة "الجسد نائم والعقل مستيقظ" (Mind Awake, Body Asleep)، حيث تتباطأ أمواج المخ من بيتا (14-30Hz) إلى ثيتا (4-7Hz).
                            </p>
                        </div>

                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(0,240,255,0.2); border-radius:14px; padding:18px;">
                            <div style="font-size:1.2rem; color:var(--gold); font-weight:700; margin-bottom:8px;">٢. الحالة التذبذبية (Vibrational State)</div>
                            <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                إحساس باهتزازات أو طنين كهربائي خفيف يسري في الجسد، وصفه روبرت مونرو بأنه اللحظة التي تسبق فك الارتباط الحسي بين الوعي والمستقبلات الجسدية.
                            </p>
                        </div>

                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(0,240,255,0.2); border-radius:14px; padding:18px;">
                            <div style="font-size:1.2rem; color:var(--gold); font-weight:700; margin-bottom:8px;">٣. الانفصال وحبل الفضة (Silver Cord)</div>
                            <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                شعور بالطفو أو الانزلاق خارج الجسد الفيزيائي، مع وجود رابط رمزي دائم يُعرف في الثيوصوفيا بـ "الحبل الفضي" يضمن العودة الفورية بمجرد اضطراب التنفس.
                            </p>
                        </div>

                        <div style="background:rgba(15,23,42,0.7); border:1px solid rgba(0,240,255,0.2); border-radius:14px; padding:18px;">
                            <div style="font-size:1.2rem; color:var(--gold); font-weight:700; margin-bottom:8px;">٤. العودة والالتحام (Re-integration)</div>
                            <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                عودة سريعة للوعي إلى الجسد بمجرد حدوث صوت خارجي أو حركة خفيفة، وغالباً ما تصاحبها خفقة حسية أو انتفاضة نوم فسيولوجية (Hypnic Jerk).
                            </p>
                        </div>
                    </div>

                    <!-- THE NEUROLOGICAL TRUTH EXPLAINED -->
                    <div style="background:linear-gradient(135deg, rgba(8,18,36,0.9), rgba(4,10,24,0.95)); border:1px solid rgba(56,189,248,0.3); border-radius:16px; padding:24px;">
                        <h4 style="color:#38bdf8; font-family:'Amiri',serif; font-size:1.3rem; margin-top:0; margin-bottom:12px;">
                            🔬 التفسير العلمي العصبي لتجارب الخروج من الجسد (Neurological Reality):
                        </h4>
                        <p style="color:#475569; font-size:0.95rem; line-height:1.8; margin-bottom:12px;">
                            في عام 2002، قام عالم الأعصاب السويسري <strong>أولاف بلانكي (Olaf Blanke)</strong> بنشر دراسة تاريخية في مجلة <em>Nature</em>، حيث تمكن من تحفيز تجربة "الخروج من الجسد" كهربائياً لدى مريضة واعية من خلال تنشيط منطقة محددة في الدماغ تُدعى <strong>التقاطع الصدغي الجداري (Temporoparietal Junction - TPJ)</strong>.
                        </p>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;" class="dual-grid-responsive">
                            <div style="background:rgba(0,0,0,0.3); border-radius:10px; padding:14px;">
                                <strong style="color:var(--gold);">دور منطقة الـ TPJ:</strong> هي المركز المسؤول عن دمج الإشارات الحسية (الرؤية، السمع، والمستقبلات الحسية العميقة) لبناء إحساسك بأنك "موجود داخل حدود جسدك". إذا اضطرب هذا الدمج أثناء النعاس، يرى الدماغ نفسه "من الخارج".
                            </div>
                            <div style="background:rgba(0,0,0,0.3); border-radius:10px; padding:14px;">
                                <strong style="color:var(--cyan-accent);">العلاقة بشلل النوم:</strong> تحدث الحالة عندما يدخل الدماغ في مرحلة حركة العين السريعة (REM Atonia) حيث يتم شل عضلات الجسد لمنع تمثيل الأحلام، مع بقاء الفص الجبهي في حالة يقظة واعية جزئياً.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ========================================== -->
            <!-- SECTION 4: THE METAPHYSICS OF WAFQ & MUHAMMADAN REALITY -->
            <!-- ========================================== -->
            <div id="inner-sub-prophetic-wafq" class="inner-sub-view">
                <div style="background:rgba(11,17,33,0.92); border:1px solid rgba(244,180,26,0.35); border-radius:24px; padding:35px 25px; margin-bottom:30px; box-shadow:0 15px 45px rgba(0,0,0,0.6);">
                    
                    <!-- SECTION HERO -->
                    <div style="display:flex; align-items:center; gap:14px; margin-bottom:20px; flex-wrap:wrap;">
                        <span style="font-size:2.2rem;">⚖️</span>
                        <div>
                            <h2 style="font-family:'Amiri', serif; font-size:2rem; color:var(--gold); margin:0;">
                                الموسوعة الرياضية والفلسفية الكبرى للأوفاق: فك ألغاز المربعات وتنزيه الحقيقة المحمدية
                            </h2>
                            <span style="color:#94a3b8; font-size:0.95rem;">تشريح مثلث الغزالي (3×3)، خوارزميات الأوفاق من 4×4 إلى 9×9، وتفكيك أوهام الفاعلية بالبراهين العلمية</span>
                        </div>
                    </div>

                    <p style="color:#475569; line-height:1.9; font-size:1.05rem; margin-bottom:30px;">
                        تعتبر <strong>الأوفاق والمربعات السحرية (Magic Squares)</strong> من أعظم النماذج التي التقى فيها التفكير الرياضي الجبري بالتأويل الفلسفي والرمزية الباطنية عبر تاريخ الحضارات. يقدم هذا القسم تشريحاً علمياً وتاريخياً دقيقاً لقوانين بناء الأوفاق (من 3×3 إلى 9×9)، وتفكيكاً موضوعياً لـ "الشواهد وتجارب النجاح" التي ادعاها القدماء، مع إيضاح البرهان العقلي والعرفاني في تنزيه الحقيقة المحمدية عن أي حصر عددي أو هندسي.
                    </p>

                    <!-- CHAPTER 1: THE MATHEMATICAL ANATOMY OF GHAZALI 3X3 -->
                    <div style="background:rgba(15,23,42,0.75); border:1px solid rgba(244,180,26,0.25); border-radius:18px; padding:25px; margin-bottom:28px;">
                        <h3 style="color:#94a3b8; font-family:'Amiri',serif; font-size:1.45rem; margin-top:0; margin-bottom:15px; border-bottom:1px solid rgba(244,180,26,0.2); padding-bottom:10px;">
                            📐 الفصل الأول: التشريح الرياضي الصارم لمثلث الغزالي (3×3) وكشف لغز ثوابته
                        </h3>

                        <p style="color:#475569; font-size:0.95rem; line-height:1.85;">
                            يُطلق على المربع السحري ذي الرتبة 3 اسم "مثلث الغزالي" في التراث العربي والإسلامي، نسبة إلى الفيلسوف حجة الإسلام أبي حامد الغزالي الذي ذكره في مقدمة كتاب <em>المنقذ من الضلال</em> وفي كتاب <em>النفخ والتسوية</em> كمثال رياضي بديع على خواص الأعداد وانسجامها الطبيعي.
                        </p>

                        <!-- 3 COLUMNS OF ALGEBRAIC PROOFS -->
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:18px; margin:20px 0;">
                            
                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:18px; border-right:3px solid var(--gold);">
                                <h4 style="color:var(--gold); margin:0 0 8px 0; font-size:1.1rem; font-family:'Amiri',serif;">١. برهان الخانة المركزية ($C = S / 3$)</h4>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.75; margin:0;">
                                    إذا كان مجموع كل صف وعمود وقطر يساوي $S$، فإن مجموع الضلع الأوسط والعمود الأوسط والقطرين الأربعة التي تلتقي في المركز يعطي:
                                    <br><code style="color:#38bdf8; background:rgba(0,0,0,0.5); padding:2px 6px; border-radius:4px;">4S = (مجموع الـ 9 خانات) + 3C = 3S + 3C</code>
                                    <br>بطرح $3S$ من الطرفين ينتج حتماً: <strong>$C = S / 3$</strong>.
                                    لهذا السبب الرياضي البحت، يجب أن تكون الخانة الوسطى دائماً ثلث مجموع الأضلاع، ولا يمكن للوفق أن يستقيم بدون هذه الحتمية الجبرية.
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:18px; border-right:3px solid #38bdf8;">
                                <h4 style="color:#38bdf8; margin:0 0 8px 0; font-size:1.1rem; font-family:'Amiri',serif;">٢. سر ثنائيات التناظر (بطد زهج واح)</h4>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.75; margin:0;">
                                    في الوفق الطبيعي (الأعداد من 1 إلى 9، والمجموع $S=15$ والمركز $C=5$):
                                    تكون كل خانتين متقابلتين عبر المركز مجموعهما $2C = 10$:
                                    <br>• $2 + 8 = 10$ (القطر الأول)
                                    <br>• $4 + 6 = 10$ (القطر الثاني)
                                    <br>• $9 + 1 = 10$ (العمود الأوسط)
                                    <br>• $7 + 3 = 10$ (الصف الأوسط)
                                    هذه الثنائيات الأربعة المتكاملة هندسياً تفسر لماذا يبدو المربع متزناً بشكل مطلق من كل اتجاه.
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.35); border-radius:12px; padding:18px; border-right:3px solid #06d6a0;">
                                <h4 style="color:#06d6a0; margin:0 0 8px 0; font-size:1.1rem; font-family:'Amiri',serif;">٣. خوارزمية التعمير لأي عدد مطلوب ($N$)</h4>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.75; margin:0;">
                                    لإسقاط أي عدد كلي $N$ في المثلث، وُضعت المعادلة الجبرية:
                                    <br><code style="color:#94a3b8; background:rgba(0,0,0,0.5); padding:2px 6px; border-radius:4px;">(N - 12) / 3 = المفتاح (Base)</code>
                                    <br><strong>حالات الكسر الحسابي:</strong>
                                    <br>• إذا كان الباقي $R=0$: يعمر بزيادة 1 مطردة.
                                    <br>• إذا كان الباقي $R=1$: تزاد 1 في الخانة السابعة (بيت الزاي).
                                    <br>• إذا كان الباقي $R=2$: تزاد 1 في الخانة الرابعة (بيت الدال).
                                </p>
                            </div>
                        </div>

                        <!-- VISUAL SVG OF GHAZALI 3X3 MATRIX -->
                        <div style="background:#030712; border:1px solid rgba(244,180,26,0.3); border-radius:14px; padding:20px; text-align:center; margin-top:20px;">
                            <div style="color:var(--gold); font-size:1rem; font-weight:700; margin-bottom:12px;">مصفوفة مثلث الغزالي الطبيعي 3×3 (ثابت المجموع = 15)</div>
                            <div style="display:inline-grid; grid-template-columns:repeat(3, 75px); gap:6px; margin:0 auto;">
                                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); color:#94a3b8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">4</div>
                                <div style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; color:#38bdf8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">9</div>
                                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); color:#94a3b8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">2</div>
                                
                                <div style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; color:#38bdf8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">3</div>
                                <div style="background:rgba(168,85,247,0.25); border:2px solid #a855f7; color:#fff; font-size:1.6rem; font-weight:800; padding:16px 0; border-radius:8px; box-shadow:0 0 15px rgba(168,85,247,0.4);">5</div>
                                <div style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; color:#38bdf8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">7</div>
                                
                                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); color:#94a3b8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">8</div>
                                <div style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; color:#38bdf8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">1</div>
                                <div style="background:rgba(244,180,26,0.15); border:1px solid var(--gold); color:#94a3b8; font-size:1.4rem; font-weight:800; padding:16px 0; border-radius:8px;">6</div>
                            </div>
                            <div style="color:#94a3b8; font-size:0.85rem; margin-top:12px;">لاحظ: كل صف وعمود وقطر يعطي 15 • الخانات الزوجية بالأركان (4, 2, 8, 6) والفردية بالصلبان (9, 3, 7, 1) والمركز (5)</div>
                        </div>
                    </div>

                    <!-- CHAPTER 2: DECONSTRUCTING TESTIMONIALS & SUCCESS CLAIMS -->
                    <div style="background:rgba(15,23,42,0.75); border:1px solid rgba(56,189,248,0.25); border-radius:18px; padding:25px; margin-bottom:28px;">
                        <h3 style="color:#38bdf8; font-family:'Amiri',serif; font-size:1.45rem; margin-top:0; margin-bottom:15px; border-bottom:1px solid rgba(56,189,248,0.2); padding-bottom:10px;">
                            🔬 الفصل الثاني: تفكيك "الشواهد وتجربة النجاح" وسيكولوجيا الإيمان بفاعلية الأوفاق
                        </h3>

                        <p style="color:#475569; font-size:0.95rem; line-height:1.85;">
                            كثيراً ما نقرأ في المخطوطات القديمة عبارات مثل: <em>"وهذا المثلث سر الأسرار وقد شوهد نجاحه بالتجربة القطعية"</em>، ويزعم مروجوها أن المربع كفيل بجلب الأرزاق أو كشف الكنوز أو تيسير الصعاب. فكيف نفسر هذه الشواهد وتلك المزاعم من منظور التحليل العلمي والنفسي؟
                        </p>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px; margin-top:20px;">
                            
                            <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:18px;">
                                <div style="color:var(--gold); font-weight:700; font-size:1.05rem; margin-bottom:6px;">١. الانبهار بالتناظر (Symmetry Awe)</div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                    في العصور القديمة وقبل نشوء الجبر الحديث ونظرية المصفوفات، كان التناغم الرياضي الصارم للمربعات يبدو وكأنه "معجزة خارقة". فاعتقد الإنسان القديم أن شكلاً يتساوى فيه الجمع في كل الاتجاهات لا بد وأن يكون صلة وصل سرية بالطبيعة، فجرى إسقاط القداسة والقدرة الغيبية على مصفوفة هي في الأصل حقيقة جبرية بحتة.
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:18px;">
                                <div style="color:#38bdf8; font-weight:700; font-size:1.05rem; margin-bottom:6px;">٢. الانحياز التأكيدي (Confirmation Bias)</div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                    الآلية النفسية الكلاسيكية: إذا رسم الشخص الوفق وحصل له أمر إيجابي مصادفةً، سارع إلى تخليده وكتابته في الهوامش باعتباره "مجرباً قاطعاً". أما المئات من الحالات التي لم يحدث فيها شيء، فيتم نسيانها أو تبريرها بالقول: "أخطأت في ساعة الرصد، أو نوع البخور، أو كان الحبر غير نقي".
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.3); border-radius:12px; padding:18px;">
                                <div style="color:#06d6a0; font-weight:700; font-size:1.05rem; margin-bottom:6px;">٣. الدواء الوهمي والتركيز التأملي (Placebo & Focus)</div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0;">
                                    عملية حساب الوفق، ورسم خاناته، وكتابة الأرقام بتأنٍّ في عزلة، تُدخل الممارس في حالة من التركيز الذهني الشديد والهدوء العصبي الشبيه بالتأمل (Zen Meditation). هذا الهدوء يخفف هرمونات التوتر ويمنح الإنسان شعوراً بالسيطرة والأمان النفسي، فيتوهم أن الورقة هي التي أحدثت التغيير.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- CHAPTER 3: EXPANDED ENCYCLOPEDIA OF HIGHER-ORDER SQUARES (4X4 TO 9X9) -->
                    <div style="background:rgba(15,23,42,0.75); border:1px solid rgba(168,85,247,0.3); border-radius:18px; padding:25px; margin-bottom:28px;">
                        <h3 style="color:#d8b4fe; font-family:'Amiri',serif; font-size:1.45rem; margin-top:0; margin-bottom:15px; border-bottom:1px solid rgba(168,85,247,0.2); padding-bottom:10px;">
                            🏛️ الفصل الثالث: الأطلس الشامل للأوفاق الكبرى من 4×4 إلى 9×9 وقوانين تعميرها
                        </h3>

                        <p style="color:#475569; font-size:0.95rem; line-height:1.85;">
                            تنقسم الأوفاق في علم الرياضيات التوافقية إلى ثلاثة أصناف أساسية لكل صنف منها خوارزمية هندسية مستقلة تماماً لحساب الثابت السحري الطبيعي:
                            <br><code style="color:var(--gold); background:rgba(0,0,0,0.5); padding:3px 8px; border-radius:4px; font-size:1rem;">M = [ n × (n² + 1) ] / 2</code>
                        </p>

                        <!-- GRID OF HIGHER ORDER SQUARES -->
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-top:20px;">
                            
                            <!-- 4x4 SQUARE -->
                            <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(56,189,248,0.2); border-radius:14px; padding:18px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <strong style="color:#38bdf8; font-size:1.15rem;">المربع الرباعي (4×4 - كوكب المشتري)</strong>
                                    <span style="background:rgba(56,189,248,0.2); color:#38bdf8; padding:2px 8px; border-radius:8px; font-size:0.8rem;">ثابت M = 34</span>
                                </div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:8px;">
                                    <strong>الخوارزمية (عكس الأقطار):</strong> تُكتب الأرقام من 1 إلى 16 بالتتابع، ثم تُعكس فقط الأرقام الواقعة على الأقطار الرئيسية في أماكنها التناظرية ($1 \leftrightarrow 16, 4 \leftrightarrow 13, 6 \leftrightarrow 11, 7 \leftrightarrow 10$).
                                    <br><strong>الإعجاز التناغمي:</strong> المجموع 34 يتحقق في 86 تشكيلة مختلفة (الأركان الأربعة، المربع المركزي 2×2، الأرباع الأربعة المقسمة).
                                </p>
                            </div>

                            <!-- 5x5 SQUARE -->
                            <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(244,180,26,0.2); border-radius:14px; padding:18px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <strong style="color:var(--gold); font-size:1.15rem;">المربع المخمس (5×5 - كوكب المريخ)</strong>
                                    <span style="background:rgba(244,180,26,0.2); color:var(--gold); padding:2px 8px; border-radius:8px; font-size:0.8rem;">ثابت M = 65</span>
                                </div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:8px;">
                                    <strong>الخوارزمية (القفز الفردي - De la Loubère):</strong> نبدأ بالرقم 1 في منتصف الصف العلوي، ثم نتحرك قطرياً خطوة للأعلى وخطوة لليمين (مع الدوران الدوري كسطح كروي)، وإذا كانت الخانة مشغولة ننزل خطوة رأسية واحدة لأسفل.
                                    <br><strong>الخانة المركزية:</strong> دائماً $C = 13$ (نصف الثابت الطبيعي لخانة المنتصف).
                                </p>
                            </div>

                            <!-- 6x6 SQUARE -->
                            <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(239,68,68,0.2); border-radius:14px; padding:18px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <strong style="color:#f87171; font-size:1.15rem;">المربع المسدس (6×6 - كوكب الشمس)</strong>
                                    <span style="background:rgba(239,68,68,0.2); color:#f87171; padding:2px 8px; border-radius:8px; font-size:0.8rem;">ثابت M = 111</span>
                                </div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:8px;">
                                    <strong>معضلة زوج الفرد (Singly Even):</strong> أصعب أنواع الأوفاق؛ يُبنى بطريقة "ستراشي" (Strachey Method) بتقسيم المربع إلى 4 أرباع كل منها 3×3 (A, B, C, D)، ثم تعميرها بخوارزمية الفردي وتبديل أعمدة محددة بين الربعين A وD لضبط الأقطار.
                                </p>
                            </div>

                            <!-- 7x7 SQUARE -->
                            <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(6,214,160,0.2); border-radius:14px; padding:18px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <strong style="color:#06d6a0; font-size:1.15rem;">المربع المسبع (7×7 - كوكب الزهرة)</strong>
                                    <span style="background:rgba(6,214,160,0.2); color:#06d6a0; padding:2px 8px; border-radius:8px; font-size:0.8rem;">ثابت M = 175</span>
                                </div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:8px;">
                                    <strong>الخوارزمية:</strong> 49 خانة تُعمر بقانون القفز الفردي للبوزجاني، حيث تقع الخانة 25 في المركز الحقيقي، وكل حلقتين متداخلتين تشكلان مصفوفة فرعية متناغمة الأضلاع.
                                </p>
                            </div>

                            <!-- 8x8 SQUARE -->
                            <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(168,85,247,0.2); border-radius:14px; padding:18px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <strong style="color:#d8b4fe; font-size:1.15rem;">المربع المثمن (8×8 - كوكب عطارد)</strong>
                                    <span style="background:rgba(168,85,247,0.2); color:#d8b4fe; padding:2px 8px; border-radius:8px; font-size:0.8rem;">ثابت M = 260</span>
                                </div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:8px;">
                                    <strong>الخوارزمية (زوجي الزوج):</strong> يُقسم إلى 4 مربعات 4×4 مع تطبيق قلب الأقطار المزدوج للأرقام من 1 إلى 64. يشتهر بتطابقه مع مسألة جولة الحصان في الشطرنج (Knight's Tour).
                                </p>
                            </div>

                            <!-- 9x9 SQUARE -->
                            <div style="background:rgba(0,0,0,0.35); border:1px solid rgba(148, 163, 184,0.2); border-radius:14px; padding:18px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <strong style="color:#94a3b8; font-size:1.15rem;">المربع المتسع (9×9 - كوكب القمر)</strong>
                                    <span style="background:rgba(148, 163, 184,0.2); color:#94a3b8; padding:2px 8px; border-radius:8px; font-size:0.8rem;">ثابت M = 369</span>
                                </div>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:8px;">
                                    <strong>كمال المراتب (81 خانة):</strong> أعلى الأوفاق الكلاسيكية في التراث، خانته المركزية $C = 41$، ويمثل تمام تسلسل الآحاد التسعة متكررة في تسع مجموعات متراكبة بقمة التناغم التناظري.
                                </p>
                            </div>
                        </div>

                        <!-- MASTER SYNOPSIS TABLE (3x3 to 9x9) -->
                        <div style="margin-top:25px; overflow-x:auto;">
                            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; text-align:center;">
                                <thead>
                                    <tr style="background:rgba(0,0,0,0.6); color:var(--gold); border-bottom:1px solid rgba(244,180,26,0.3);">
                                        <th style="padding:10px;">الرتبة ($n$)</th>
                                        <th style="padding:10px;">الاسم التراثي</th>
                                        <th style="padding:10px;">عدد الخانات ($n²$)</th>
                                        <th style="padding:10px;">الثابت السحري ($M$)</th>
                                        <th style="padding:10px;">الخانة المركزية ($C$)</th>
                                        <th style="padding:10px;">نوع الصنف الرياضي</th>
                                        <th style="padding:10px;">الخوارزمية المعتمدة</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">3×3</td>
                                        <td style="padding:9px;">المثلث (الغزالي)</td>
                                        <td style="padding:9px;">9</td>
                                        <td style="padding:9px; color:#38bdf8;">15</td>
                                        <td style="padding:9px; color:#06d6a0;">5</td>
                                        <td style="padding:9px;">فردي (Odd)</td>
                                        <td style="padding:9px;">بطد زهج واح / قطري</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">4×4</td>
                                        <td style="padding:9px;">المربع (المشتري)</td>
                                        <td style="padding:9px;">16</td>
                                        <td style="padding:9px; color:#38bdf8;">34</td>
                                        <td style="padding:9px; color:#94a3b8;">— (مزدوج)</td>
                                        <td style="padding:9px;">زوجي الزوج (Doubly Even)</td>
                                        <td style="padding:9px;">عكس الأقطار المتصالبة</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">5×5</td>
                                        <td style="padding:9px;">المخمس (المريخ)</td>
                                        <td style="padding:9px;">25</td>
                                        <td style="padding:9px; color:#38bdf8;">65</td>
                                        <td style="padding:9px; color:#06d6a0;">13</td>
                                        <td style="padding:9px;">فردي (Odd)</td>
                                        <td style="padding:9px;">دي لا لوبير (القفز الفردي)</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">6×6</td>
                                        <td style="padding:9px;">المسدس (الشمس)</td>
                                        <td style="padding:9px;">36</td>
                                        <td style="padding:9px; color:#38bdf8;">111</td>
                                        <td style="padding:9px; color:#94a3b8;">— (مزدوج)</td>
                                        <td style="padding:9px;">زوجي الفرد (Singly Even)</td>
                                        <td style="padding:9px;">لوكس وستراشي (LUX)</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">7×7</td>
                                        <td style="padding:9px;">المسبع (الزهرة)</td>
                                        <td style="padding:9px;">49</td>
                                        <td style="padding:9px; color:#38bdf8;">175</td>
                                        <td style="padding:9px; color:#06d6a0;">25</td>
                                        <td style="padding:9px;">فردي (Odd)</td>
                                        <td style="padding:9px;">البوزجاني التبادلي</td>
                                    </tr>
                                    <tr style="border-bottom:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02);">
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">8×8</td>
                                        <td style="padding:9px;">المثمن (عطارد)</td>
                                        <td style="padding:9px;">64</td>
                                        <td style="padding:9px; color:#38bdf8;">260</td>
                                        <td style="padding:9px; color:#94a3b8;">— (مزدوج)</td>
                                        <td style="padding:9px;">زوجي الزوج (Doubly Even)</td>
                                        <td style="padding:9px;">الانعكاس المزدوج الرباعي</td>
                                    </tr>
                                    <tr>
                                        <td style="padding:9px; color:#94a3b8; font-weight:700;">9×9</td>
                                        <td style="padding:9px;">المتسع (القمر)</td>
                                        <td style="padding:9px;">81</td>
                                        <td style="padding:9px; color:#38bdf8;">369</td>
                                        <td style="padding:9px; color:#06d6a0;">41</td>
                                        <td style="padding:9px;">فردي (Odd)</td>
                                        <td style="padding:9px;">كمال المراتب الآحادية</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- CHAPTER 4: WHY THE MUHAMMADAN REALITY TRANSCENDS FINITE MATRICES -->
                    <div style="background:linear-gradient(135deg, rgba(20,14,35,0.9), rgba(8,12,28,0.95)); border:1px solid rgba(244,180,26,0.35); border-radius:18px; padding:25px;">
                        <h3 style="color:var(--gold); font-family:'Amiri',serif; font-size:1.45rem; margin-top:0; margin-bottom:15px; border-bottom:1px solid rgba(244,180,26,0.2); padding-bottom:10px;">
                            👑 الفصل الرابع: البرهان العرفاني والتنزيهي — لماذا لا يوجد وفق للحقيقة المحمدية؟
                        </h3>

                        <p style="color:#475569; font-size:0.95rem; line-height:1.9;">
                            إذا كانت كتب المخطوطات والرموز قد وضعت أوفاقاً للمقامات الكونية والطبائع الأربعة وعزت لكل نبي من أولي العزم نسبة فلكية جزئية، فلماذا أجمعت الدوائر الفلسفية والعرفانية الرصينة على امتناع وضع وفق يمثل "الحقيقة المحمدية"؟
                        </p>

                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:18px; margin:20px 0;">
                            
                            <div style="background:rgba(0,0,0,0.4); border-radius:12px; padding:18px; border-top:3px solid var(--gold);">
                                <h4 style="color:var(--gold); margin:0 0 8px 0; font-family:'Amiri',serif; font-size:1.15rem;">١. استحالة حصر الكلي في جزئياته</h4>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.75; margin:0;">
                                    في فلسفة ابن عربي في <em>الفتوحات المكية</em> وعبد الكريم الجيلي في <em>الإنسان الكامل</em>، تُعد الحقيقة المحمدية أصل الوجود الكلي ومرآة الفيض الأول التي انبثقت منها سائر المراتب (من عقل كلي ونفس كلية وهيولى وأفلاك). والوفق بحكم تعريفه الرياضي هو مصفوفة جزئية مقيدة بقيمة عددية مغلقة ($N$). واستحالة حصر اللامتناهي في المتناهي تمنع عقلاً أن يُصاغ للأصل المطلق جدول محصور.
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.4); border-radius:12px; padding:18px; border-top:3px solid #38bdf8;">
                                <h4 style="color:#38bdf8; margin:0 0 8px 0; font-family:'Amiri',serif; font-size:1.15rem;">٢. الجمع بين الأضداد ونفي التحيز</h4>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.75; margin:0;">
                                    كل وفق ينحاز بطبيعته لطبيعة عنصرية معينة (نار، ماء، هواء، تراب) أو فلك محدد (زحل، مشتري، مريخ). أما الحقيقة المحمدية فمقامها هو "مقام الجمع والوجود الأكمل" المحيط بجميع الطبائع دون أن يستغرقه طبع، والمتجاوز لكل الأفلاك دون أن يحده فلك؛ ولذا فإن حبسها في وفق يعني قسرها على عنصر دون سواه، وهو نقص يتنافى مع كمال الجمع.
                                </p>
                            </div>

                            <div style="background:rgba(0,0,0,0.4); border-radius:12px; padding:18px; border-top:3px solid #06d6a0;">
                                <h4 style="color:#06d6a0; margin:0 0 8px 0; font-family:'Amiri',serif; font-size:1.15rem;">٣. التوحيد المنزه وبساطة الرسالة</h4>
                                <p style="color:#94a3b8; font-size:0.88rem; line-height:1.75; margin:0;">
                                    الرسالة المحمدية بُنيت على هدم الطلاسم والوثنية الحسابية والتقديس الرمزي للأشكال، وجاءت بالدعوة المباشرة للتوحيد الخالص: ﴿فَاعْلَمْ أَنَّهُ لَا إِلَٰهَ إِلَّا اللَّهُ﴾. شريعتها شريعة عمل وسلوك وقلب سليم، لا شريعة أوفاق وجداول، مما يجعل التنزيه واجباً دينياً وعقلياً وعرفانياً.
                                </p>
                            </div>
                        </div>

                        <!-- GOLDEN CONCLUSION -->
                        <div style="background:rgba(0,0,0,0.5); border-right:4px solid var(--gold); border-radius:10px; padding:16px 20px; margin-top:10px;">
                            <span style="font-family:'Amiri',serif; font-size:1.1rem; color:#f1f5f9; line-height:1.8;">
                                «إن الأوفاق خُلقت للمقادير المحدودة في عالم الحساب، أما النور المحمدي فهو سر التجلي الأعظم الذي لا يحيط به خط ولا يحصره رسم؛ وما عجزت الأرقام عن عده، امتنع على الجداول حده.»
                            </span>
                        </div>
                    </div>

                </div>
            </div>

            <!-- ========================================== -->
            <!-- SECTION 5: INTERACTIVE CONSCIOUSNESS & BRAINWAVE LAB -->
            <!-- ========================================== -->
            <div id="inner-sub-lab" class="inner-sub-view">
                <div style="background:rgba(11,17,33,0.85); border:1px solid rgba(56,189,248,0.3); border-radius:20px; padding:30px; margin-bottom:30px;">
                    <div style="display:flex; align-items:center; gap:12px; margin-bottom:18px;">
                        <span style="font-size:2rem;">🧪</span>
                        <div>
                            <h2 style="font-family:'Amiri', serif; font-size:1.8rem; color:#38bdf8; margin:0;">
                                المختبر التفاعلي لموجات الدماغ وتوازن الوعي
                            </h2>
                            <span style="color:#94a3b8; font-size:0.9rem;">محاكاة حية لترددات الصفاء الذهني وتشخيص المؤشرات الحيوية لنقاء التفكير</span>
                        </div>
                    </div>

                    <!-- BRAINWAVE SIMULATOR -->
                    <div style="background:rgba(15,23,42,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:16px; padding:24px; margin-bottom:28px;">
                        <h3 style="color:#94a3b8; font-family:'Amiri',serif; font-size:1.3rem; margin-top:0; margin-bottom:14px;">
                            🧠 محاكي الترددات الدماغية وحالات الوعي:
                        </h3>
                        
                        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:20px;">
                            <button onclick="tuneBrainwaveMode('delta')" class="brain-btn" id="brain-btn-delta">دلتا (Delta 0.5 - 4 Hz) • النوم العميق</button>
                            <button onclick="tuneBrainwaveMode('theta')" class="brain-btn active" id="brain-btn-theta">ثيتا (Theta 4 - 8 Hz) • التأمل والتنويم</button>
                            <button onclick="tuneBrainwaveMode('alpha')" class="brain-btn" id="brain-btn-alpha">ألفا (Alpha 8 - 12 Hz) • الصفاء والاسترخاء</button>
                            <button onclick="tuneBrainwaveMode('beta')" class="brain-btn" id="brain-btn-beta">بيتا (Beta 13 - 30 Hz) • التفكير واليقظة</button>
                            <button onclick="tuneBrainwaveMode('gamma')" class="brain-btn" id="brain-btn-gamma">غاما (Gamma > 30 Hz) • الذروة الإدراكية</button>
                        </div>

                        <!-- WAVE VISUALIZATION CANVAS -->
                        <div style="background:#030712; border:1px solid rgba(56,189,248,0.25); border-radius:12px; padding:15px; text-align:center; margin-bottom:18px;">
                            <canvas id="brainwave-canvas" width="800" height="120" style="width:100%; max-height:120px; display:block;"></canvas>
                        </div>

                        <div id="brainwave-info-box" style="background:rgba(0,0,0,0.4); border-radius:10px; padding:16px; color:#475569; font-size:0.92rem; line-height:1.7;">
                            <strong>موجات ثيتا (Theta Waves):</strong> هي التردد المرتبط بحالات الرؤى الإبداعية، والحدس العميق، وفترات الانتقال بين اليقظة والنوم. في هذه الحالة يقل حاجز النقد العقلي ويصبح الوعي أكثر استجابة للهدوء والسكينة الداخلية.
                        </div>
                    </div>

                    <!-- COGNITIVE BALANCE SELF-ASSESSMENT -->
                    <div style="background:rgba(15,23,42,0.8); border:1px solid rgba(6,214,160,0.25); border-radius:16px; padding:24px;">
                        <h3 style="color:#06d6a0; font-family:'Amiri',serif; font-size:1.3rem; margin-top:0; margin-bottom:14px;">
                            🌿 مقياس التوازن الداخلي والحصانة الإدراكية:
                        </h3>
                        <p style="color:#94a3b8; font-size:0.9rem; margin-bottom:16px;">
                            أجب عن المؤشرات التالية لتقييم مستوى النقاء العصبي وتوازن الطاقة الحيوية في يومك:
                        </p>

                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:18px;" class="dual-grid-responsive">
                            <div>
                                <label style="display:block; color:#475569; font-size:0.88rem; margin-bottom:6px;">مستوى التوتر والإجهاد الذهني:</label>
                                <select id="diag-stress" style="width:100%; background:rgba(0,0,0,0.6); border:1px solid rgba(255,255,255,0.2); color:#fff; padding:10px; border-radius:8px;">
                                    <option value="low">منخفض (ذهن هادئ ومستقر)</option>
                                    <option value="medium" selected>متوسط (ضغوط عمل وتفكير متقطع)</option>
                                    <option value="high">مرتفع (تسارع في الأفكار وإرهاق دائم)</option>
                                </select>
                            </div>
                            <div>
                                <label style="display:block; color:#475569; font-size:0.88rem; margin-bottom:6px;">جودة النوم والاستيقاظ:</label>
                                <select id="diag-sleep" style="width:100%; background:rgba(0,0,0,0.6); border:1px solid rgba(255,255,255,0.2); color:#fff; padding:10px; border-radius:8px;">
                                    <option value="good" selected>جيدة ومريحة (7+ ساعات متصلة)</option>
                                    <option value="broken">متقطعة مع أحلام مشوشة</option>
                                    <option value="poor">أرق وصعوبة شديدة في النوم</option>
                                </select>
                            </div>
                        </div>

                        <button onclick="calculateInnerBalanceScore()" style="background:linear-gradient(135deg, #06d6a0, #00b4d8); color:#030712; font-weight:700; border:none; padding:10px 24px; border-radius:10px; cursor:pointer; font-family:'Tajawal',sans-serif; font-size:0.95rem;">
                            📊 فحص مؤشر النقاء والحصانة الداخلية
                        </button>

                        <div id="diag-result-card" style="display:none; margin-top:18px; background:rgba(0,0,0,0.5); border:1px solid #06d6a0; border-radius:12px; padding:18px; font-size:0.92rem; line-height:1.75; color:#475569;">
                            <!-- Output generated dynamically via JS -->
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    '''

def get_inner_realms_chamber_js():
    return '''
    // ==========================================
    // CHAMBER 20: INNER REALMS & ASTRAL ODYSSEY JS
    // ==========================================

    function switchInnerRealmsSubTab(subTabId) {
        document.querySelectorAll('#tab-inner-realms .inner-sub-view').forEach(el => {
            el.classList.remove('active');
            el.style.display = 'none';
        });
        document.querySelectorAll('#tab-inner-realms .inner-tab-pill').forEach(btn => {
            btn.classList.remove('active');
        });

        const activeSub = document.getElementById(subTabId);
        if (activeSub) {
            activeSub.classList.add('active');
            activeSub.style.display = 'block';
        }

        const pillMap = {
            'inner-sub-subterranean': 'pill-inner-subterranean',
            'inner-sub-etheric': 'pill-inner-etheric',
            'inner-sub-astral': 'pill-inner-astral',
            'inner-sub-prophetic-wafq': 'pill-inner-prophetic-wafq',
            'inner-sub-lab': 'pill-inner-lab'
        };
        const activePill = document.getElementById(pillMap[subTabId]);
        if (activePill) activePill.classList.add('active');

        if (subTabId === 'inner-sub-lab') {
            setTimeout(initBrainwaveCanvas, 50);
        }
    }

    // --- Subterranean Layer Inspector ---
    const SUBTERRANEAN_LAYERS = {
        'crust': {
            title: 'القشرة السطحية للأرض (0 - 40 كم)',
            geo: 'الطبقة الصلبة التي تحوي الجبال والمحيطات والغلاف الحيوي. درجة الحرارة تتدرج من حرارة السطح إلى 400° مئوية.',
            myth: 'في الميثولوجيا القديمة هي "عالم الشهادة والظاهر" ومسرح التاريخ البشري، وبوابتها إلى الباطن هي المغاور والكهوف العميقة.'
        },
        'mantle': {
            title: 'الوشاح الصخري واللزج (40 - 2890 كم)',
            geo: 'يشكل 84% من حجم الأرض، صخور سيليكاتية تتحرك بحمل حراري بطيء تحت درجات حرارة بين 1000° و3700° مئوية وضغط هائل.',
            myth: 'رمزياً يمثل "برزخ النار الصامتة" وقوة تحريك القارات؛ في الموروثات اعتبره البعض مجازاً لمسكن القوى الجوفية النائمة.'
        },
        'agartha': {
            title: 'أغارثا وشامبالا (المجاز والرمز العرفاني)',
            geo: 'جيولوجياً: يستحيل وجود أي تجاويف فارغة أو مدن مأهولة نظراً للضغط الصخري الهائل (الذي يسحق أي فراغ فوراً).',
            myth: 'عرفانياً وفلسفياً: تمثل "مدينة الحكمة الباطنة" ورمز النواة الصافية التي لا تدنسها أطماع السطح؛ مركز توازن الحكماء في الوعي الجمعي.'
        },
        'core': {
            title: 'اللب المنصهر والصلب (2890 - 6371 كم)',
            geo: 'كرة من الحديد والنيكل تولد المجال المغناطيسي الحامي لكوكب الأرض من الرياح الشمسية القاتلة. درجات الحرارة تفوق 5000° مئوية.',
            myth: 'يرمز للمركز الناري ومحور الجاذبية الكونية للكوكب؛ قلب الأرض النابض الذي يحمي الحياة عبر الدرع المغناطيسي الأثيري.'
        }
    };

    function inspectSubterraneanLayer(layerKey) {
        document.querySelectorAll('.layer-pill-btn').forEach(btn => btn.classList.remove('active'));
        const activeBtn = document.getElementById('layer-btn-' + layerKey);
        if (activeBtn) activeBtn.classList.add('active');

        const data = SUBTERRANEAN_LAYERS[layerKey];
        const display = document.getElementById('subterranean-inspector-display');
        if (data && display) {
            display.innerHTML = `
                <h4 style="color:#38bdf8; margin:0 0 8px 0; font-family:'Amiri',serif; font-size:1.15rem;">${data.title}</h4>
                <div style="margin-bottom:8px;"><strong style="color:#06d6a0;">الفيزياء والجيولوجيا:</strong> ${data.geo}</div>
                <div><strong style="color:var(--gold);">المعنى الميثولوجي والرمزي:</strong> ${data.myth}</div>
            `;
        }
    }

    // --- Brainwave Simulation Engine ---
    let brainwaveFreq = 6;
    let brainwaveColor = '#38bdf8';
    let brainAnimId = null;

    const BRAINWAVE_MODES = {
        'delta': { freq: 2, color: '#a855f7', title: 'موجات دلتا (Delta 0.5 - 4 Hz)', text: 'تنشط في النوم العميق الخالي من الأحلام. مسؤولة عن التعافي البيولوجي، وإفراز هرمون النمو، وتجديد الخلايا المناعية.' },
        'theta': { freq: 6, color: '#38bdf8', title: 'موجات ثيتا (Theta 4 - 8 Hz)', text: 'تردد التأمل العميق، والهدوء الشديد، وتجارب الأحلام الواعية والإلهام الإبداعي، وجسر الانتقال بين الوعي واللاوعي.' },
        'alpha': { freq: 10, color: '#06d6a0', title: 'موجات ألفا (Alpha 8 - 12 Hz)', text: 'حالة الاسترخاء الواعي بدون نوم؛ تهدئة الضجيج الداخلي، ومثالية للتعلم السريع والقراءة المتأملة وتخفيف التوتر.' },
        'beta': { freq: 20, color: '#f4b41a', title: 'موجات بيتا (Beta 13 - 30 Hz)', text: 'التركيز الواعي، الحساب، وحل المشكلات اليومية؛ فرط استمرارها يؤدي للإجهاد العصبي وارتفاع الكورتيزول.' },
        'gamma': { freq: 40, color: '#ff3366', title: 'موجات غاما (Gamma > 30 Hz)', text: 'التردد الأعلى؛ يرتبط بومضات البصيرة المفاجئة، والدمج متعدد الحواس، وحالات الشهود الذهني المكثف.' }
    };

    function tuneBrainwaveMode(modeKey) {
        document.querySelectorAll('.brain-btn').forEach(b => b.classList.remove('active'));
        const btn = document.getElementById('brain-btn-' + modeKey);
        if (btn) btn.classList.add('active');

        const mode = BRAINWAVE_MODES[modeKey];
        if (mode) {
            brainwaveFreq = mode.freq;
            brainwaveColor = mode.color;
            const box = document.getElementById('brainwave-info-box');
            if (box) {
                box.innerHTML = `<strong style="color:${mode.color};">${mode.title}:</strong> ${mode.text}`;
            }
        }
    }

    function initBrainwaveCanvas() {
        const canvas = document.getElementById('brainwave-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        let step = 0;

        function drawWave() {
            ctx.fillStyle = '#030712';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw center guide line
            ctx.strokeStyle = 'rgba(255,255,255,0.06)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(0, canvas.height / 2);
            ctx.lineTo(canvas.width, canvas.height / 2);
            ctx.stroke();

            // Draw sine wave
            ctx.strokeStyle = brainwaveColor;
            ctx.lineWidth = 2.5;
            ctx.shadowBlur = 10;
            ctx.shadowColor = brainwaveColor;
            ctx.beginPath();

            const h = canvas.height / 2;
            const amp = Math.min(38, Math.max(14, 45 - brainwaveFreq * 0.7));

            for (let x = 0; x < canvas.width; x++) {
                const y = h + Math.sin((x * brainwaveFreq * 0.04) + step) * amp;
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.stroke();
            ctx.shadowBlur = 0;

            step += 0.08 + (brainwaveFreq * 0.005);
            brainAnimId = requestAnimationFrame(drawWave);
        }

        if (brainAnimId) cancelAnimationFrame(brainAnimId);
        drawWave();
    }

    // --- Cognitive Balance Calculator ---
    function calculateInnerBalanceScore() {
        const stress = document.getElementById('diag-stress').value;
        const sleep = document.getElementById('diag-sleep').value;
        const card = document.getElementById('diag-result-card');
        if (!card) return;

        let score = 85;
        let advice = [];

        if (stress === 'medium') { score -= 15; advice.push('• تخصيص 15 دقيقة للتنفس العميق وتفريغ الذهن قبل النوم.'); }
        if (stress === 'high') { score -= 30; advice.push('• إيقاف الشاشات قبل النوم بساعة، وممارسة المشي لتفريغ الكورتيزول العضلي.'); }

        if (sleep === 'broken') { score -= 20; advice.push('• ضبط حرارة الغرفة (18-20° مئوية) وثبات موعد الاستيقاظ لضبط الساعة البيولوجية.'); }
        if (sleep === 'poor') { score -= 35; advice.push('• الابتعاد عن المنبهات بعد الظهر ومراجعة روتين الاسترخاء اليومي.'); }

        let color = '#06d6a0';
        let status = 'ممتاز (توافق ذهني عالي)';
        if (score < 75) { color = '#f4b41a'; status = 'متوسط (يحتاج تخفيف الإجهاد والاجترار)'; }
        if (score < 50) { color = '#ff3366'; status = 'إجهاد مرتفع (ينصح بالراحة التامة والاسترخاء)'; }

        card.style.display = 'block';
        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; flex-wrap:wrap;">
                <span style="font-size:1.1rem; font-weight:700; color:${color};">مؤشر النقاء الإدراكي: ${score}/100 — ${status}</span>
                <span style="background:${color}22; border:1px solid ${color}; color:${color}; padding:3px 10px; border-radius:12px; font-size:0.8rem;">تشخيص فوري</span>
            </div>
            <div style="margin-top:10px;">
                <strong style="color:#475569;">التوصيات العملية لتعزيز الحصانة وتوازن الطاقة:</strong>
                <div style="margin-top:6px; color:#94a3b8; font-size:0.88rem; line-height:1.7;">
                    ${advice.length > 0 ? advice.join('<br>') : '• وضعك الذهني ممتاز؛ حافظ على روتين الصفاء والرياضة والتأمل اليومي.'}
                </div>
            </div>
        `;
    }

    // Auto trigger on chamber load
    window.addEventListener('DOMContentLoaded', () => {
        // init if open
    });
    '''
