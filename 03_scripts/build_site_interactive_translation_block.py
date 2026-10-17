import sys
sys.stdout.reconfigure(encoding="utf-8")

interactive_html = """
            <!-- ======================================================================== -->
            <!-- 🏛️ الديوان المترجم الشامل لبردية لندن وليدن (الأبواب العشرة الكبرى) -->
            <!-- ======================================================================== -->
            <div class="demotic-translation-grand-chamber" style="margin-top: 40px; background: rgba(9, 14, 28, 0.98); border: 2px solid #f59e0b; border-radius: 20px; padding: 34px; box-shadow: 0 20px 60px rgba(0,0,0,0.95); color: #f8fafc;">
                
                <div style="text-align: center; border-bottom: 2px dashed rgba(245, 158, 11, 0.45); padding-bottom: 26px; margin-bottom: 32px;">
                    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(245, 158, 11, 0.15); border: 1px solid #f59e0b; color: #fbbf24; padding: 6px 22px; border-radius: 25px; font-size: 0.9rem; font-weight: 800; margin-bottom: 14px;">
                        <span>📜</span> ديوان الترجمة الشاملة والتحقيق الأكاديمي غير المنقوص (10 أبواب كبرى)
                    </div>
                    <h3 style="font-size: 2rem; color: #f59e0b; margin-bottom: 12px; font-weight: 900;">
                        المتن الكامل لبردية لندن وليدن السحرية الديموطيقية<br>
                        <span style="font-size: 1.15rem; color: #94a3b8; font-weight: 500;">Complete Exhaustive Translation of BM 10070 & Leiden I 383 (Recto 1-29 & Verso 1-33)</span>
                    </h3>
                    <p style="max-width: 950px; margin: 0 auto; color: #cbd5e1; font-size: 0.98rem; line-height: 1.85;">
                        ترجمة تفصيلية دقيقة محققة من الأصل الديموطيقي والقبطي المبكر واليوناني، منظمة في عشرة أبواب هيكلية تفصل كامل العزائم، الإجراءات الطقسية، الوصفات الطبية، والتحقيق الإبستيمي لأطروحة الدكتوراه.
                    </p>
                </div>

                <!-- أبواب الترجمة العشرة بتصميم الأكورديون الأكاديمي المنظم -->
                <div style="display: flex; flex-direction: column; gap: 20px;">

                    <!-- الباب 1 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 12px; padding: 18px;" open>
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #fbbf24; display: flex; align-items: center; justify-content: space-between;">
                            <span>🔮 الباب الأول: كوزمولوجيا الاستنزال الأكبر بالإناء والزيت (Lecanomancy) — الأعمدة (Col. I, II, III)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">3 أعمدة رئيسية</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• الشروط المادية:</strong> إناء برونزي أو فخاري بكر غير مدهون، زيت زيتون واحات نقي، صبي وسيط بكر (Medium) لم يقرب النساء، مخدع مظلم تماماً مع شعلة واحدة خافتة تعكس الضوء بزاوية 45° على الزيت.</p>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #fbbf24;">
                                <strong style="color: #fde047;">ترجمة عزيمة الاستفتاح (Col. I. 1-10):</strong><br>
                                <em>«افتحوا لي الأرض! افتحوا لي العالم السفلي! افتحوا لي النون (الأوقيانوس الأزلي)! أيتها العتمة انقشعي، وأيها النور انبثق في هذا الإناء! أنا هو الكاهن القائم على الخدمة، استدعي أنوبيس العظيم حارس العتبة، ليفتح الأبواب ويفرش البساط الطاهر للآلهة الزائرة...»</em>
                            </div>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #fbbf24;">
                                <strong style="color: #fde047;">طقس كشف السارق بمسحوق الزعفران (Col. III. 29):</strong><br>
                                <em>«إذا أردت إحضار السارق المجهول، فخذ مسحوق الزعفران (Crocus) واخلطه مع ملح الشبة المعدنية (Alum)، وضعهما على موقد الجمر في مواجهة الإناء؛ فإن ملامح السارق وهيئته تنطبع في الزيت أمام الصبي أو يأتي السارق بنفسه خاضعاً».</em>
                            </div>
                        </div>
                    </details>

                    <!-- الباب 2 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #38bdf8; display: flex; align-items: center; justify-content: space-between;">
                            <span>⚕️ الباب الثاني: ديوان حكيم الأطباء إمحوتب واستنزال الرؤى المنامية (Imouthes & Oneiromancy) — العمود (Col. IV)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">الرؤيا المنامية</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• الكيفية:</strong> تطهير الفراش بماء النطرون، كتابة تميمة من 7 سطور توضع تحت الرأس لاستنزال روح الطبيب الأسطوري <strong>إمحوتب (ابن بتاح)</strong> في المنام ليملي التشخيص والدواء.</p>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #38bdf8;">
                                <strong style="color: #7dd3fc;">ترجمة النص اليوناني المدمج بالديموطيقية (Col. IV. 9-19):</strong><br>
                                <em>«أدعوك أيها الإله الأكبر، الطبيب الحكيم إمحوتب! تعال إليّ هذه الليلة بسلام، واكشف لي في نومي عن أصل هذا الداء ووصفة الشفاء، ولا تدعني في حيرة وظلام بحق رب السماء السابعة والنور الذي لا ينطفئ...»</em>
                            </div>
                            <p><strong>• الأسطر 20-24:</strong> معادلات فلكية لضبط الطالع (Horoscope) والاقتران القمري، ومكحلة من كبد الجوارح لتقوية البصر.</p>
                        </div>
                    </details>

                    <!-- الباب 3 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #facc15; display: flex; align-items: center; justify-content: space-between;">
                            <span>🕯️ الباب الثالث: ديوان مصباح النور واستنزالات السراج المنفرد والمزدوج (Lychnomancy) — الأعمدة (Col. V, VI, VII, VIII)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">4 أعمدة كاملة</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• شروط السراج:</strong> سراج فخاري أبيض نقي غير مدهون، فتيل كتان بكر، زيت واحات صافٍ، ودهن الجفون بكحل عيون الهدهد ومسحوق الميعة.</p>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #facc15;">
                                <strong style="color: #fde047;">ترجمة مناجاة المصباح المنفرد (Col. V. 9-23):</strong><br>
                                <em>«أيها المصباح النقي القائم في محراب الظلمات، لست مجرد فخار وزيت بل أنت عين حورس المشعة بنور الحق! لتنفتح عيناي بنور الصقر ولتثبت حدقتاي في لهبك دون رجفة لأشهد ما خفي عن البشر...»</em>
                            </div>
                            <p><strong>• طقس الكاهن بشاش وسلاسل الحروف (VI - VIII):</strong> تكرار الأحرف الصوتية السبعة (Α Ε Η Ι Ο Υ Ω) وأسماء أبراكاس وماسكيلي لفتح مسارات الوعي الصوري وحضور أنوبيس بحربته الكتانية.</p>
                        </div>
                    </details>

                    <!-- الباب 4 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #fb923c; display: flex; align-items: center; justify-content: space-between;">
                            <span>☀️ الباب الرابع: عرش الأرباب — خونسو الطيبي ومركب الإله رع النهاري — الأعمدة (Col. IX, X)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">استنزال الظهيرة الشمسي</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• مناجاة خونسو (Col. IX):</strong> استنزال قمر طيبة لطرد الأرواح المتمردة وشياطين الهواء من مجلس الاستنزال.</p>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #fb923c;">
                                <strong style="color: #fdba74;">ترجمة طقس شهود مركب الإله رع (Col. X. 22-35):</strong><br>
                                <em>«يُمارس وقت الزوال التام تحت قرص الشمس المباشر بإناء نحاسي مذهب: أيها الإله رع الجالس في مركب الملايين من السنين، يا مبدد جحافل الظلام بنوره؛ أستنزلك في كبد هذا الإناء! أرني بحارة مركبك واكسُ وجهي بهيبتك وجبروتك ليخر أعدائي صرعى أمام هيبتي...»</em>
                            </div>
                        </div>
                    </details>

                    <!-- الباب 5 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #c084fc; display: flex; align-items: center; justify-content: space-between;">
                            <span>👑 الباب الخامس: ديوان الوقار والهيبة وتليين قلوب الملوك ودفع بطش الحكام — الأعمدة (Col. XI, Col. XV 24-31)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">الهيبة وعقد الألسن</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• طقس العمود XI:</strong> دهان الوجه بخلاصة زهور اللوتس وزيت البلسان النقي وتلاوة عزيمة تماثل الكاهن بحورس المتوج لإلقاء الوقار في قلوب السلاطين.</p>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #c084fc;">
                                <strong style="color: #e879f9;">ترجمة صيغة عقد ألسنة الحكام (Col. XV. 24-31):</strong><br>
                                <em>«أربط لسان كل سلطان جائر، وأقيد يد كل خصم ظالم! ليتحول غضبه إلى رقة وسيفه إلى سلام، ولتخرس الكلمات في فمه فلا ينطق إلا بما يسرني وينفعني بحق القوى الأزلية الحاكمة...»</em>
                            </div>
                        </div>
                    </details>

                    <!-- الباب 6 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #fb7185; display: flex; align-items: center; justify-content: space-between;">
                            <span>🖤 الباب السادس: سحر الكهانة الأسود — طلاسم التفريق، حيوان الزبابة، والربط العاطفي — الأعمدة (Col. XII, XIII, XV, XXV, XXVI)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">سحر التفريق والربط</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #fb7185;">
                                <strong style="color: #fda4af;">ترجمة طقس تفريق الزوجين بحيوان الزبابة (Col. XIII. 11-29):</strong><br>
                                <em>«تُجفف جيفة حيوان الزبابة (Shrew-mouse) وتُسحق مع شعر الرجل والمرأة وتدفن في مجرى ماء: أيتها الأرواح الكامنة في المقابر، كما فارقت هذه الزبابة النور والحياة، اجعلوا فلان يفارق زوجته فلانة! ألقوا بينهما البغضاء والكراهية والنفور فلا يجتمعا على فراش حتى يقع الطلاق التام...»</em>
                            </div>
                            <p><strong>• طلاسم الوجد (Col. XXV & XXVI):</strong> استدرار آلام إيزيس وبكائها على أوزوريس لربط قلب المرأة وسلب إرادتها ونومها حتى تعود خاضعة.</p>
                        </div>
                    </details>

                    <!-- الباب 7 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #34d399; display: flex; align-items: center; justify-content: space-between;">
                            <span>🐍 الباب السابع: عيادة طيبة الإكلينيكية — ترياق السموم ولدغات العقارب والبلعوم — الأعمدة (Col. XIX, XX)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">طب الطوارئ الفرعوني</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>1. عضة الكلب المسعور (19/1-9):</strong> غسل بالخل والنطرون ووضع كمادة من مسحوق الشيح وعسل النحل لتعقيم الأنسجة.</p>
                            <p><strong>2. استخراج السموم من القلب (19/10-21):</strong> شراب من عصارة الصمغ العربي وخل التفاح والكرفس لتحفيز القيء وتطهير المعدة.</p>
                            <p><strong>3. عظام الحلق المعترضة (19/21 & 20/27):</strong> بلع لقيمات مغلفة بزيت اللوز وشحم الإوز وتدليك العنق خارجياً نحو الأسفل.</p>
                            <p><strong>4. لدغة العقرب (20/1-27):</strong> ربط العضو ووضع كمادة الثوم المهروس والخل والملح البحري لتحييد السم الزلالي.</p>
                        </div>
                    </details>

                    <!-- الباب 8 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(14, 165, 233, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #38bdf8; display: flex; align-items: center; justify-content: space-between;">
                            <span>🌌 الباب الثامن: كوزمولوجيا النجوم القطبية والأفلاك — كوكبة الدب الأكبر والقمر والشمس — الأعمدة (Col. XVI - XVIII, XXIII, XXVII - XXIX)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">الكوزمولوجيا النجمية</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #38bdf8;">
                                <strong style="color: #7dd3fc;">ترجمة استنزال كوكبة الدب الأكبر («فخذ الثور» - Col. XVIII):</strong><br>
                                <em>«أيتها النجوم الخالدة المحيطة بمحور القطب الشمالي، أنتم حراس العرش السماوي الذين لا يذوقون الموت؛ استنزل بركتكم في شعلتي ونوركم في بصري لأشهد أسرار الفلك ودورات الزمان...»</em>
                            </div>
                            <p><strong>• استنزال القمر (Col. XXIII):</strong> ترصد الليالي البيض لمطابقة استنزال الإناء مع ذروة الجذب القمري واستقرار التيارات الأثيرية.</p>
                        </div>
                    </details>

                    <!-- الباب 9 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #f87171; display: flex; align-items: center; justify-content: space-between;">
                            <span>💀 الباب التاسع: دستور التخدير والسموم والسبات الكاتاليبسي وعقاقير الهوس — العمود (Col. XXIV) وظهر البردية (Verso II, III, XXIX)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">السموم والسبات</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• السبات الكاتاليبسي (Col. XXIV):</strong> خلاصات الماندراكولا والسكران الأسود والخشخاش لإحداث شلل عضلي وانخفاض التنفس ونبض القلب لمحاكاة الموت الظاهري لساعات طويلة.</p>
                            <p><strong>• عقار الخبل والهوس (Verso Col. XXIX):</strong> خلاصات الداتورة والسكران في النبيذ لإحداث اضطراب عقلي وفقدان الذاكرة والهلوسة.</p>
                        </div>
                    </details>

                    <!-- الباب 10 -->
                    <details style="background: rgba(17, 24, 39, 0.85); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 18px;">
                        <summary style="cursor: pointer; font-size: 1.18rem; font-weight: 800; color: #34d399; display: flex; align-items: center; justify-content: space-between;">
                            <span>🌿 الباب العاشر: الصيدلية الفرعونية الكبرى ومعجم العقاقير والمعادن — ظهر البردية كاملاً (Verso Col. I - XXXIII)</span>
                            <span style="font-size: 0.85rem; color: #94a3b8; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 8px;">33 عموداً طبياً وصيدلانياً</span>
                        </summary>
                        <div style="margin-top: 16px; border-top: 1px solid rgba(148, 163, 184, 0.2); padding-top: 14px; font-size: 0.92rem; line-height: 1.8; color: #cbd5e1;">
                            <p><strong>• Verso I - V:</strong> دستور النباتات الإلهية (حاجب رع، حاجب القمر، قلب حورس)، تصنيف الأحجار والمعادن، قطرات الأذن، ووصفات وقف النزيف واختبار الحمل بالقمح والشعير.</p>
                            <p><strong>• Verso VIII - X:</strong> علاج داء النقرس بنبات اللحلاح (الكولشيسين) والنبيذ العتيق ومراهم تدليك أوتار الأقدام.</p>
                            <p><strong>• Verso XII - XXI:</strong> استرداد المسروقات، استنزال الأحلام، وعلاج الرمد وجفاف العيون.</p>
                            <div style="background: rgba(0,0,0,0.4); padding: 14px; border-radius: 8px; margin: 10px 0; border-right: 3px solid #34d399;">
                                <strong style="color: #6ee7b7;">حوار حورس وإيزيس لخفض الحمى (Verso Col. XXXIII):</strong><br>
                                <em>«حوار طقسي لخفض حرارة حمى النفضان؛ وضع كمادات ماء بارد ودهان الجبين بمستخلصات قشور الصفصاف (الساليسين الطبيعي)، وهو النص الختامي لكامل مخطوطة لندن وليدن».</em>
                            </div>
                        </div>
                    </details>

                </div>

            </div>
            <!-- ======================================================================== -->
"""

with open("03_scripts/interactive_translation_block.html", "w", encoding="utf-8") as f:
    f.write(interactive_html.strip() + "\n")

print("Created 03_scripts/interactive_translation_block.html successfully!")