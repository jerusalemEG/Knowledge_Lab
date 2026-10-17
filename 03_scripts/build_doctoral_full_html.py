import sys
sys.stdout.reconfigure(encoding="utf-8")

doctoral_html = """
            <!-- ======================================================================== -->
            <!-- 📜 الأطروحة الأكاديمية الشاملة: بردية لندن وليدن السحرية الديموطيقية (15139) -->
            <!-- ======================================================================== -->
            <div class="demotic-papyrus-chamber" style="margin-top: 45px; background: rgba(10, 15, 29, 0.98); border: 2px solid #eab308; border-radius: 20px; padding: 36px; box-shadow: 0 20px 60px rgba(0,0,0,0.95); color: #f8fafc; font-family: system-ui, -apple-system, sans-serif;">
                
                <!-- الترويسة الأكاديمية الفاخرة -->
                <div style="text-align: center; border-bottom: 2px dashed rgba(234, 179, 8, 0.45); padding-bottom: 30px; margin-bottom: 35px;">
                    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(234, 179, 8, 0.15); border: 1px solid #eab308; color: #fde047; padding: 8px 24px; border-radius: 30px; font-size: 0.92rem; font-weight: 800; margin-bottom: 16px;">
                        <span>📜</span> المرجع الأكاديمي الشامل 29 • دراسة أطروحة الدكتوراه المقارنة لبردية طيبة (15139.pdf)
                    </div>
                    <h2 style="font-size: 2.1rem; color: #facc15; margin-bottom: 12px; font-weight: 900; line-height: 1.4;">
                        موسوعة بردية لندن وليدن السحرية الديموطيقية<br>
                        <span style="font-size: 1.2rem; color: #94a3b8; font-weight: 500;">The Demotic Magical Papyrus of London & Leiden (BM 10070 & Leiden I 383)</span>
                    </h2>
                    <p style="max-width: 1050px; margin: 0 auto; color: #cbd5e1; font-size: 1.02rem; line-height: 1.85;">
                        تحقيق أركيولوجي وفيلولوجي وطبي شامل لجميع أعمدة البردية (الوجه 1 إلى 29 والظهر 1 إلى 33 بلا استثناء)، مع فك شفراتها السرية، شرح آليات الاستنزال بالزيت والمصباح، فهرسة المعجم الصيدلاني الفرعوني، والتحقيق الإبستيمي بميزان الوحي الإلهي المعصوم.
                    </p>
                </div>

                <!-- شبكة البيانات الأركيولوجية الأساسية للمخطوطة -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-bottom: 40px;">
                    <div style="background: rgba(30, 41, 59, 0.75); border: 1px solid rgba(148, 163, 184, 0.25); border-radius: 14px; padding: 18px;">
                        <div style="color: #38bdf8; font-size: 0.82rem; font-weight: 800;">🏛️ التوثيق والشتات المتحفي</div>
                        <div style="font-size: 1.02rem; font-weight: 800; color: #f8fafc; margin-top: 5px;">المتحف البريطاني ومتحف ليدن</div>
                        <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">BM 10070 (لندن) + AMS 65 / I 383 (ليدن)</div>
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.75); border: 1px solid rgba(148, 163, 184, 0.25); border-radius: 14px; padding: 18px;">
                        <div style="color: #38bdf8; font-size: 0.82rem; font-weight: 800;">⏳ التأريخ الزمني الدقيق</div>
                        <div style="font-size: 1.02rem; font-weight: 800; color: #f8fafc; margin-top: 5px;">مطلع القرن 3 الميلادي (حوالي 200 - 250م)</div>
                        <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">أحدث وأخر برديات الخط الديموطيقي بمصر</div>
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.75); border: 1px solid rgba(148, 163, 184, 0.25); border-radius: 14px; padding: 18px;">
                        <div style="color: #38bdf8; font-size: 0.82rem; font-weight: 800;">🔤 اللغات والشفرات السرية</div>
                        <div style="font-size: 1.02rem; font-weight: 800; color: #f8fafc; margin-top: 5px;">ديموطيقية + قبطية قديمة + يونانية</div>
                        <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">نظام تشفير أبجدي للأدوية والأسماء (Cipher)</div>
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.75); border: 1px solid rgba(148, 163, 184, 0.25); border-radius: 14px; padding: 18px;">
                        <div style="color: #38bdf8; font-size: 0.82rem; font-weight: 800;">📖 طبعة التحقيق الأكاديمي</div>
                        <div style="font-size: 1.02rem; font-weight: 800; color: #f8fafc; margin-top: 5px;">إف. إل. جريفيث والسير هيربرت طومسون</div>
                        <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 4px;">مطبعة جامعة أكسفورد كلارندون (1904م)</div>
                    </div>
                </div>

                <!-- أبواب الدراسة الشاملة للأطروحة -->
                <div style="display: flex; flex-direction: column; gap: 32px;">

                    <!-- الباب 1: التفريغ الحصري لأعمدة الوجه (Recto 1 to 29) -->
                    <div style="background: rgba(17, 24, 39, 0.9); border-right: 5px solid #eab308; border-radius: 14px; padding: 26px;">
                        <h3 style="color: #facc15; font-size: 1.35rem; margin-bottom: 12px; font-weight: 800; display: flex; align-items: center; gap: 10px;">
                            <span>📜</span> الباب الأول: التفريغ والتحليل الموضعي لأعمدة الوجه التسعة والعشرين (Recto Col. I - XXIX)
                        </h3>
                        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.8; margin-bottom: 16px;">
                            تفريغ أكاديمي يغطي كامل متن الوجه الذي كتبه كاهن طيبة بعناية فائقة مقسماً على 29 عموداً مؤطراً:
                        </p>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">الأعمدة I إلى III — استنزال الإناء والزيت الأكبر:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    استنزال صور الكيانات عبر سطح زيت الزيتون في إناء برونزي أو فخاري جديد باستخدام صبي وسيط بكر (Medium). مناجاة الإله أنوبيس لفرش البساط ودعوة الآلهة. يشمل السطر 29 من العمود III طقس كشف السارق بوضع مسحوق الزعفران والشبة على الموقد.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">العمود IV — استدعاء إمحوتب وضبط الطالع:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    استنزال روح الطبيب الحكيم المؤله إمحوتب في المنام لطلب التشخيص الدوائي عبر تميمة تحت الرأس، مع نص يوناني كامل (Lines 9-19)، وتعليمات ضبط الطالع الفلكي ومكاحل العين المقوية للبصر.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">العمود V — استنزال السراج المنفرد:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    طقس كشف الرؤية بالمصباح الفخاري الأبيض غير المطلي وزيت الواحات الصافي، يمارسه الكاهن بمفرده بعد طلاء جفونه بكحل طائر الهدهد وحبوب الميعة المجففة.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">الأعمدة VI إلى VIII — طقس الكاهن بشاش وسلاسل الحروف:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    استنزال المصباح المزدوج (منفرداً أو مع وسيط) منسوباً للكاهن بشاش؛ يتضمن تراتيل الحروف الصوتية السبعة المتكررة (Vowel Chains) لفتح أبواب الأثير السبعة.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">العمود IX و X — استنزال خونسو ومركب الإله رع:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    مناجاة خونسو قاهر العوارض، وطقس الظهيرة الشمسي الفريد (الأسطر 22-35) تحت قرص الشمس لشهود مركب رع الإلهي وحماته لنيل الهيبة وقهر الأعداء.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">العمود XI — طلاسم الهيبة والقبول عند الملوك:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    صيغ المماثلة بين الكاهن وتاج حورس لنيل التقدير والرفعة ودفع غضب الرؤساء والسلاطين، ودهان الوجه بخلاصة زهور اللوتس والبلسان.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">الأعمدة XII و XIII — سحر التفريق وحيوان الزبابة:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    العمود XIII مخصص لتفريق الرجل عن المرأة؛ استخدام مسحوق جيفة حيوان الزبابة (Shrew-mouse) ودفنه في مجرى مائي لإلقاء البغضاء والفرقة.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">العمود XIV و XV — كشف الأخبار البعيدة وحل النزاع:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    استنزال الإناء الاستخباري لمعرفة أخبار المدن البعيدة؛ والعمود XV يتضمن صيغة يونانية ومترجمة ديموطيقياً لدرء غضب الحكام والخصوم.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">الأعمدة XVI إلى XVIII — رصد كوكبة الدب الأكبر:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    توجيه شعلة السراج لمطالع كوكبة الدب الأكبر ("فخذ الثور" الشمالية) لاستنزال الأرواح النجمية الخالدة في كوزمولوجيا مصر القديمة.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">العمود XIX و XX — عيادة السموم واللدغات والبلعوم:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    بروتوكول طبي لعضة الكلب، واستخراج السموم والجرعات الضارة من القلب، وعلاج انسداد الحلق بالعظام المعترضة، وإسعاف لدغة العقرب.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">الأعمدة XXI إلى XXIV — مكاحل العين والسبات الكاتاليبسي:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    صناعة الكحل السري؛ والعمود XXIV مخصص للمركبات المهدئة وإحداث النوم العميق وحالات التخشب الشبيهة بالموت (Catalepsy) بنباتات البنج والماندراكولا.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.65); padding: 14px; border-radius: 10px; border: 1px solid rgba(148, 163, 184, 0.15);">
                                <strong style="color: #38bdf8;">الأعمدة XXV إلى XXIX — طلاسم الوجد وختام شمس رع:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    طلاسم الجلب العاطفي بالتشفع بآلام إيزيس، واستنزالات الإناء الانفرادية في جوف الليل، وختام استنزال الشمس لنيل الظفر في القضاء.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- الباب 2: المعجم الصيدلاني والطبي لأعمدة الظهر (Verso 1 to 33) -->
                    <div style="background: rgba(17, 24, 39, 0.9); border-right: 5px solid #10b981; border-radius: 14px; padding: 26px;">
                        <h3 style="color: #34d399; font-size: 1.35rem; margin-bottom: 12px; font-weight: 800; display: flex; align-items: center; gap: 10px;">
                            <span>🌿</span> الباب الثاني: المعجم الصيدلاني والطب التجريبي لأعمدة الظهر الثلاثة والثلاثين (Verso Col. I - XXXIII)
                        </h3>
                        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.8; margin-bottom: 16px;">
                            المتن الطبي غير المنقح المكتوب على ظهر ألياف البردية، ويمثل إرث الكهانة الطبية والصيدلانية:
                        </p>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
                            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 14px; border-radius: 10px;">
                                <strong style="color: #6ee7b7;">Verso I إلى V — دستور الأدوية والمعادن وطب النساء:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    فهرس النباتات المنسوبة للآلهة (حاجب رع، حاجب القمر، قلب حورس)، تصنيف المعادن وراتنجات البخور، وصفات الشراب المنوم (Sleeping Draughts)، قطرات علاج الأذن وطنينها، ووصفات وقف النزيف الرحمي واختبار الحمل بالبذور.
                                </p>
                            </div>
                            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 14px; border-radius: 10px;">
                                <strong style="color: #6ee7b7;">Verso VI إلى XI — علاج النقرس وآلام القدمين والمفاصل:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    بروتوكول فرعوني كامل لعلاج داء النقرس الموضعي بواسطة نبات اللحلاح (المحتوي على الكولشيسين) مع النبيذ القديم ومراهم تدليك أوتار وباطن القدمين لتسكين الآلام الحادة.
                                </p>
                            </div>
                            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 14px; border-radius: 10px;">
                                <strong style="color: #6ee7b7;">Verso XII إلى XXI — استنزال الأحلام ومكاحل الرمد:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    صيغ استرداد المسروقات وحفظ المراكب النيلية من الغرق (XV)، استنزال الرؤى المنامية الصادقة (XVII)، استنزال الدب الأكبر (XVIII)، وقطرات علاج الرمد وجفاف العيون (XX).
                                </p>
                            </div>
                            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 14px; border-radius: 10px;">
                                <strong style="color: #6ee7b7;">Verso XXII إلى XXXIII — سموم الهوس وخافضات الحمى:</strong>
                                <p style="font-size: 0.86rem; color: #cbd5e1; margin-top: 6px; line-height: 1.6;">
                                    استنزال الإناء المنفرد، صيغ إحداث الخبل والهوس المؤقت بنبات الداتورة (XXIX)، ابتهال الإله سيسيهوت حارس السراج (XXXI)، وختام البردية بحوار حورس وإيزيس لعلاج الحمى بكمادات قشور الصفصاف (الساليسيلات).
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- الباب 3: التفسير الفسيولوجي والتهجين الديني للأطروحة -->
                    <div style="background: rgba(17, 24, 39, 0.9); border-right: 5px solid #a855f7; border-radius: 14px; padding: 26px;">
                        <h3 style="color: #c084fc; font-size: 1.35rem; margin-bottom: 12px; font-weight: 800; display: flex; align-items: center; gap: 10px;">
                            <span>🔬</span> الباب الثالث: التحليل العصبي والتهجين التوفيقي السكندري (Syncretism & Neurobiology)
                        </h3>
                        <div style="display: flex; flex-direction: column; gap: 14px; font-size: 0.92rem; line-height: 1.8;">
                            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 10px;">
                                <strong style="color: #e879f9;">1. الآلية العصبية للحرمان الحسي (Ganzfeld Effect):</strong>
                                <p style="color: #cbd5e1; margin-top: 5px;">
                                    تثبت أبحاث الأعصاب أن تثبيت البصر في غرفة مظلمة على نقطة زيت أو لهب سراج يقطع المخ عن التغذية البصرية المتنوعة؛ فيعوض الدماغ هذا النقص بإفراز الدوبامين وتنشيط القشرة الصدغية البصرية، مما يولد هلاوس عينية صريحة وتجسيدات متحركة ظنها الكهنة أرواحاً متكلمة.
                                </p>
                            </div>
                            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 10px;">
                                <strong style="color: #e879f9;">2. التوفيقية الدينية والغنوصية (Alexandrian Syncretism):</strong>
                                <p style="color: #cbd5e1; margin-top: 5px;">
                                    تُمثل البردية النموذج الأوضح للتهجين السكندري؛ حيث دُمجت الآلهة الفرعونية (تحوت، أنوبيس، خونسو) مع أسماء غنوصية هلينستية (Abrasax وسلاسل الأحرف الصوتية السبعة)، وأسماء عبرية وسريانية محرفة (Adonai, Sabaoth, Iao, Michael) لتعزيز الرهبة والتمكين الصوتي.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- الباب 4: الميزان القرآني الصارم وتفكيك التناقضات للمرشد والمحقق -->
                    <div style="background: rgba(225, 29, 72, 0.12); border: 2px solid #f43f5e; border-radius: 16px; padding: 26px;">
                        <h3 style="color: #fb7185; font-size: 1.35rem; margin-bottom: 14px; font-weight: 800; display: flex; align-items: center; gap: 10px;">
                            <span>⚖️</span> الباب الرابع: الميزان القرآني الصارم والفرقان الإبستيمي المعصوم
                        </h3>
                        <div style="display: flex; flex-direction: column; gap: 14px; font-size: 0.92rem; line-height: 1.8;">
                            <div style="background: rgba(0,0,0,0.5); padding: 16px; border-radius: 10px; border-right: 4px solid #fb7185;">
                                <strong style="color: #fda4af;">1. احتكار الغيب الإلهي وتزييف استنزال الكهان:</strong>
                                <p style="color: #cbd5e1; margin-top: 5px;">
                                    القرآن الكريم يضع القاعدة المعرفية الصارمة: ﴿قُل لَّا يَعْلَمُ مَن فِي السَّمَاوَاتِ وَالْأَرْضِ الْغَيْبَ إِلَّا اللَّهُ﴾ [النمل: 65]. وما يدعيه كهنة الزيت والمصابيح ليس إلا أوهاماً نفسية واستدراجاً شيطانياً يخلط الحق بالباطل.
                                </p>
                            </div>
                            <div style="background: rgba(0,0,0,0.5); padding: 16px; border-radius: 10px; border-right: 4px solid #fb7185;">
                                <strong style="color: #fda4af;">2. حقيقة سحر التفريق والعداوة في ميزان القرآن:</strong>
                                <p style="color: #cbd5e1; margin-top: 5px;">
                                    تخصيص البردية لأعمدة كاملة في سحر التفريق بين الزوجين (العمود XIII) يُطابق تماماً التحذير القرآني العظيم: ﴿فَيَتَعَلَّمُونَ مِنْهُمَا مَا يُفَرِّقُونَ بِهِ بَيْنَ الْمَرْءِ وَزَوْجِهِ ۚ وَمَا هُم بِضَارِّينَ بِهِ مِنْ أَحَدٍ إِلَّا بِإِذْنِ اللَّهِ﴾ [البقرة: 102]، مما يُعد وثيقة تاريخية تثبت واقعية البيان القرآني وهبوط مآل السحر.
                                </p>
                            </div>
                            <div style="background: rgba(0,0,0,0.5); padding: 16px; border-radius: 10px; border-right: 4px solid #fb7185;">
                                <strong style="color: #fda4af;">3. تحرير الطب المادي المشروع من دنس الكهانة:</strong>
                                <p style="color: #cbd5e1; margin-top: 5px;">
                                    ميز الإسلام بدقة بين «العلم الطبي التجريبي والأسباب المادية النافعة» (وهو ما حفظته البردية من نباتات اللحلاح والصفصاف) وأوجب التداوي بها، وبين «الأوهام والطلاسم الشركية» فنسفها وطهر البشرية من رقّها.
                                </p>
                            </div>
                        </div>
                    </div>

                </div>

            </div>
            <!-- ======================================================================== -->
"""

with open("03_scripts/doctoral_block.html", "w", encoding="utf-8") as f:
    f.write(doctoral_html.strip() + "\n")

print("Created 03_scripts/doctoral_block.html successfully!")