# -*- coding: utf-8 -*-
"""
Knowledge Lab - Deluxe Cosmic Chambers & JSON Engine (جنة العلوم الباطنية الشاملة)
Engineered for supreme architectural organization, full indexing across all 20 chambers,
illuminated manuscript styling, embedded JSON data, and rich interactive visual graphics.
"""

import json
import re

# Comprehensive JSON Database for all Esoteric & Cosmological Chambers
COSMIC_DATABASE = {
    "spheres": [
        {"id": "sphere_1", "num": 1, "name": "فلك القمر (السماء الدنيا)", "planet": "القمر", "prophet": "آدم عليه السلام", "gem": "اللؤلؤ والفضة", "color": "#f8fafc", "freq": "174 Hz", "angel": "إسماعيل / رقيائيل", "metal": "الفضة", "quran": "﴿وَلَقَدْ زَيَّنَّا السَّمَاءَ الدُّنْيَا بِمَصَابِيحَ﴾", "desc": "مجمع الطينات السفلية، وعالم الكون والفساد، والمدخل الأول لاختراق حجب المادة."},
        {"id": "sphere_2", "num": 2, "name": "فلك عطارد (السماء الثانية)", "planet": "عطارد", "prophet": "يحيى وعيسى عليهما السلام", "gem": "الزبرجد والفيروزج", "color": "#38bdf8", "freq": "285 Hz", "angel": "ميخائيل", "metal": "الزئبق", "quran": "﴿فَقَضَاهُنَّ سَبْعَ سَمَاوَاتٍ فِي يَوْمَيْنِ﴾", "desc": "مستقر العلوم العقلية، النطق، الفصاحة، والكتابة بالقلم."},
        {"id": "sphere_3", "num": 3, "name": "فلك الزهرة (السماء الثالثة)", "planet": "الزهرة", "prophet": "يوسف الصديق عليه السلام", "gem": "الزمرد الأخضر", "color": "#10b981", "freq": "396 Hz", "angel": "عنيائيل", "metal": "النحاس", "quran": "﴿وَزَيَّنَّاهَا لِلنَّاظِرِينَ﴾", "desc": "فلك الجمال الباهر، الفنون، التناغم الموسيقي، وتسخير القلوب بالمحبة."},
        {"id": "sphere_4", "num": 4, "name": "فلك الشمس (السماء الرابعة)", "planet": "الشمس", "prophet": "إدريس عليه السلام (هرمس)", "gem": "الياقوت الأصفر والذهب", "color": "#ffd700", "freq": "528 Hz", "angel": "صلصائيل", "metal": "الذهب الخالص", "quran": "﴿وَجَعَلَ الشَّمْسَ سِرَاجًا﴾", "desc": "قلب الوجود الكوني، ومستقر الروح الحيوي، وميزان الاعتدال بين السماوات السبع."},
        {"id": "sphere_5", "num": 5, "name": "فلك المريخ (السماء الخامسة)", "planet": "المريخ", "prophet": "هارون عليه السلام", "gem": "العقيق الأحمر والياقوت", "color": "#ef4444", "freq": "639 Hz", "angel": "سمسمائيل", "metal": "الحديد", "quran": "﴿وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ﴾", "desc": "فلك القوة الدافعة، البأس الصارم، وتصفية الأكدار بنار الصهر والتطهير."},
        {"id": "sphere_6", "num": 6, "name": "فلك المشتري (السماء السادسة)", "planet": "المشتري", "prophet": "موسى الكليم عليه السلام", "gem": "الياقوت الأزرق واللازورد", "color": "#06b6d4", "freq": "741 Hz", "angel": "صرفيائيل", "metal": "القصدير", "quran": "﴿وَكَلَّمَ اللَّهُ مُوسَىٰ تَكْلِيمًا﴾", "desc": "فلك الحكمة والعدل، التوسع في الخير، وتنزيل ألواح الشرائع الربانية."},
        {"id": "sphere_7", "num": 7, "name": "فلك زحل (السماء السابعة)", "planet": "زحل", "prophet": "إبراهيم الخليل عليه السلام", "gem": "الجزع الأسود والياقوت الأشهب", "color": "#c084fc", "freq": "852 Hz", "angel": "كسفيائيل", "metal": "الرصاص", "quran": "﴿عِندَ الْبَيْتِ الْمَعْمُورِ﴾", "desc": "فلك التوحيد الصرف، الصمت الأبدي، وبوابة الخروج من عالم الزمان إلى الأبد."},
        {"id": "sphere_8", "num": 8, "name": "فلك الكرسي والعرش المحيط", "planet": "العرش الأطلس", "prophet": "النبي الخاتم محمد ﷺ", "gem": "النور المطلق", "color": "#fef08a", "freq": "963 Hz", "angel": "إسرافيل / حملة العرش", "metal": "الأثير النوراني", "quran": "﴿وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ﴾", "desc": "مقام قاب قوسين أو أدنى، محيط الكون الكلي، ومبدأ الفيض والقدرة الإلهية."}
    ],
    "zodiac": [
        {"name": "الحمل", "symbol": "♈", "element": "نار", "quality": "حار يابس", "ruler": "المريخ", "dates": "21 مارس - 19 أبريل", "angel": "ملخيائيل", "body": "الرأس والدماغ", "opposite": "الميزان ♎", "color": "#ef4444", "secrets": "مبدأ الحركة الصاعدة، كسر الجليد الكوني، وشيفرة الفداء بالكبش العظيم."},
        {"name": "الثور", "symbol": "♉", "element": "تراب", "quality": "بارد يابس", "ruler": "الزهرة", "dates": "20 أبريل - 20 مايو", "angel": "آسودائيل", "body": "الحنجرة والرقبة", "opposite": "العقرب ♏", "color": "#d97706", "secrets": "مبدأ التجسد المادي، البناء الحجري الميغاليثي، وتجلي عمارة الأهرامات."},
        {"name": "الجوزاء", "symbol": "♊", "element": "هواء", "quality": "حار رطب", "ruler": "عطارد", "dates": "21 مايو - 20 يونيو", "angel": "أمبائيل", "body": "الكتفان والرئتان", "opposite": "القوس ♐", "color": "#38bdf8", "secrets": "التناظر الثنائي، اختراع اللغات والتدوين الصوري، وانقسام النفس والروح."},
        {"name": "السرطان", "symbol": "♋", "element": "ماء", "quality": "بارد رطب", "ruler": "القمر", "dates": "21 يونيو - 22 يوليو", "angel": "موريائيل", "body": "الصدر والمعدة", "opposite": "الجدي ♑", "color": "#3b82f6", "secrets": "الرحم الكوني الحافظ لبذور الحياة، طوفان نوح وسفينة النجاة في لجة الطوفان."},
        {"name": "الأسد", "symbol": "♌", "element": "نار", "quality": "حار يابس", "ruler": "الشمس", "dates": "23 يوليو - 22 أغسطس", "angel": "ورخيائيل", "body": "القلب والظهر", "opposite": "الدلو ♒", "color": "#f59e0b", "secrets": "السيادة الشمسية المطلقة، رمزية أبي الهول، وعصر الملوك الحكماء الأوائل."},
        {"name": "العذراء", "symbol": "♍", "element": "تراب", "quality": "بارد يابس", "ruler": "عطارد", "dates": "23 أغسطس - 22 سبتمبر", "angel": "حمائييل", "body": "الأمعاء والبطن", "opposite": "الحوت ♓", "color": "#10b981", "secrets": "سنبلة القمح، الولادة العذرية البتولية (مريم عليها السلام)، والنقاء الطيني."},
        {"name": "الميزان", "symbol": "♎", "element": "هواء", "quality": "حار رطب", "ruler": "الزهرة", "dates": "23 سبتمبر - 22 أكتوبر", "angel": "زورائيل", "body": "الكليتان وأسفل الظهر", "opposite": "الحمل ♈", "color": "#06b6d4", "secrets": "إقامة العدل الكوني، ميزان الاعتدال الخريفي، وتنزيل ألواح الشريعة والوصايا."},
        {"name": "العقرب", "symbol": "♏", "element": "ماء", "quality": "بارد رطب", "ruler": "المريخ", "dates": "23 أكتوبر - 21 نوفمبر", "angel": "بربيائيل", "body": "أعضاء التوليد", "opposite": "الثور ♉", "color": "#9333ea", "secrets": "سر التحول، الموت الرمزي والبعث، والتحنيط والعبور عبر بوابات العالم الآخر."},
        {"name": "القوس", "symbol": "♐", "element": "نار", "quality": "حار يابس", "ruler": "المشتري", "dates": "22 نوفمبر - 21 ديسمبر", "angel": "أدوخيائيل", "body": "الفخذان والورك", "opposite": "الجوزاء ♊", "color": "#f97316", "secrets": "سهم الحكمة الموجه نحو مركز المجرة، الفلسفة العليا، وتجاوز الحدود الجغرافية."},
        {"name": "الجدي", "symbol": "♑", "element": "تراب", "quality": "بارد يابس", "ruler": "زحل", "dates": "22 ديسمبر - 19 يناير", "angel": "حنائيل", "body": "الركبتان والمفاصل", "opposite": "السرطان ♋", "color": "#64748b", "secrets": "بوابة الآلهة عند القدماء، الانقلاب الشتوي، وبلوغ قمة الجبل الروحي بالانضباط."},
        {"name": "الدلو", "symbol": "♒", "element": "هواء", "quality": "حار رطب", "ruler": "زحل", "dates": "20 يناير - 18 فبراير", "angel": "كمبائيل", "body": "الساقان والكاحلان", "opposite": "الأسد ♌", "color": "#0284c7", "secrets": "سكب ماء المعرفة الكلية، شبكات الاتصال اللامركزية، والوعي الجمعي المستنير."},
        {"name": "الحوت", "symbol": "♓", "element": "ماء", "quality": "بارد رطب", "ruler": "المشتري", "dates": "19 فبراير - 20 مارس", "angel": "برخيائيل", "body": "القدمان والأصابع", "opposite": "العذراء ♍", "color": "#6366f1", "secrets": "رمزية السمكة والمسيح، الفناء في بحر التوحيد، وسر بطن الحوت مع يونس عليه السلام."}
    ],
    "mansions": [
        {"num": 1, "name": "الشرطان", "deg": "0° - 12°51' الحمل", "element": "نار", "letter": "أ", "virtue": "الحزم وبداية الأعمال الكبرى"},
        {"num": 2, "name": "البطين", "deg": "12°51' - 25°42' الحمل", "element": "نار", "letter": "ب", "virtue": "استخراج الكنوز والزراعة"},
        {"num": 3, "name": "الثريا", "deg": "25°42' الحمل - 8°34' الثور", "element": "تراب", "letter": "ج", "virtue": "المحبة والبهجة والملاحة"},
        {"num": 4, "name": "الدبران", "deg": "8°34' - 21°25' الثور", "element": "تراب", "letter": "د", "virtue": "البناء والثبات وهندسة الأرض"},
        {"num": 5, "name": "الهقعة", "deg": "21°25' الثور - 4°17' الجوزاء", "element": "هواء", "letter": "هـ", "virtue": "العلم والدراسة والأسفار السريعة"},
        {"num": 6, "name": "الهنعة", "deg": "4°17' - 17°8' الجوزاء", "element": "هواء", "letter": "و", "virtue": "الألفة بين الشركاء وتيسير التجارة"},
        {"num": 7, "name": "الذراع", "deg": "17°8' الجوزاء - 0° السرطان", "element": "ماء", "letter": "ز", "virtue": "نماء الزرع وطلب الرزق والربح"},
        {"num": 8, "name": "النثرة", "deg": "0° - 12°51' السرطان", "element": "ماء", "letter": "ح", "virtue": "النصر على الأعداء وقضاء الحوائج"},
        {"num": 9, "name": "الطرف", "deg": "12°51' - 25°42' السرطان", "element": "ماء", "letter": "ط", "virtue": "عقد العزائم وحماية السفر"},
        {"num": 10, "name": "الجبهة", "deg": "25°42' السرطان - 8°34' الأسد", "element": "نار", "letter": "ي", "virtue": "الهيبة والرفعة وعلو الشأن"},
        {"num": 11, "name": "الزبرة", "deg": "8°34' - 21°25' الأسد", "element": "نار", "letter": "ك", "virtue": "عقد الصلح وطلب الحكام والأمراء"},
        {"num": 12, "name": "الصرفة", "deg": "21°25' الأسد - 4°17' العذراء", "element": "تراب", "letter": "ل", "virtue": "عزل الفاسدين وفصل الأمور"},
        {"num": 13, "name": "العواء", "deg": "4°17' - 17°8' العذراء", "element": "تراب", "letter": "م", "virtue": "المودة وجلب المنافع الحسية"},
        {"num": 14, "name": "السماك", "deg": "17°8' العذراء - 0° الميزان", "element": "هواء", "letter": "ن", "virtue": "الشفاء من الأمراض وتركيب الأدوية"},
        {"num": 15, "name": "الغفر", "deg": "0° - 12°51' الميزان", "element": "هواء", "letter": "س", "virtue": "إخفاء الأسرار والأمن من اللصوص"},
        {"num": 16, "name": "الزبانا", "deg": "12°51' - 25°42' الميزان", "element": "هواء", "letter": "ع", "virtue": "التجارة والبيع والشراء المربح"},
        {"num": 17, "name": "الإكليل", "deg": "25°42' الميزان - 8°34' العقرب", "element": "ماء", "letter": "ف", "virtue": "حفظ الأبدان وثبات العهود"},
        {"num": 18, "name": "القلب", "deg": "8°34' - 21°25' العقرب", "element": "ماء", "letter": "ص", "virtue": "الحصانة من المكائد والشدائد"},
        {"num": 19, "name": "الشولة", "deg": "21°25' العقرب - 4°17' القوس", "element": "نار", "letter": "ق", "virtue": "رد كيد الظالمين وحسم النزاع"},
        {"num": 20, "name": "النعائم", "deg": "4°17' - 17°8' القوس", "element": "نار", "letter": "ر", "virtue": "ترويض الطبائع وتيسير الصيد"},
        {"num": 21, "name": "البلدة", "deg": "17°8' القوس - 0° الجدي", "element": "تراب", "letter": "ش", "virtue": "البناء وغرس الأشجار والأمان"},
        {"num": 22, "name": "سعد الذابح", "deg": "0° - 12°51' الجدي", "element": "تراب", "letter": "ت", "virtue": "العلاج ودفع السموم والنجاة"},
        {"num": 23, "name": "سعد بلع", "deg": "12°51' - 25°42' الجدي", "element": "هواء", "letter": "ث", "virtue": "حفر الآبار والشفاء من العلل"},
        {"num": 24, "name": "سعد السعود", "deg": "25°42' الجدي - 8°34' الدلو", "element": "هواء", "letter": "خ", "virtue": "السعادة العظمى والبركة والتزويج"},
        {"num": 25, "name": "سعد الأخبية", "deg": "8°34' - 21°25' الدلو", "element": "هواء", "letter": "ذ", "virtue": "كشف المخبآت وفك العقد"},
        {"num": 26, "name": "الفرغ المقدم", "deg": "21°25' الدلو - 4°17' الحوت", "element": "ماء", "letter": "ض", "virtue": "المحبة والائتلاف وإصلاح الشأن"},
        {"num": 27, "name": "الفرغ المؤخر", "deg": "4°17' - 17°8' الحوت", "element": "ماء", "letter": "ظ", "virtue": "الاستقرار في المنازل ودفع الأذى"},
        {"num": 28, "name": "الرشاء (بطن الحوت)", "deg": "17°8' الحوت - 0° الحمل", "element": "ماء", "letter": "غ", "virtue": "تمام الأمور والختام الميمون"}
    ],
    "kings": [
        {"day": "الأحد", "planet": "الشمس", "upper": "روقيائيل", "lower": "المذهب أبا عبد الله", "metal": "الذهب", "color": "#ffd700", "incense": "السندروس والعود", "char": "ف"},
        {"day": "الإثنين", "planet": "القمر", "upper": "جبرائيل", "lower": "مُرة أبا النور", "metal": "الفضة", "color": "#f8fafc", "incense": "اللبان والجاوي", "char": "ج"},
        {"day": "الثلاثاء", "planet": "المريخ", "upper": "سمسمائيل", "lower": "الأحمر أبا محرز", "metal": "الحديد", "color": "#ef4444", "incense": "القسط والمقل", "char": "ش"},
        {"day": "الأربعاء", "planet": "عطارد", "upper": "ميكائيل", "lower": "برقان أبا العجائب", "metal": "الزئبق", "color": "#38bdf8", "incense": "المستكة والقرنفل", "char": "ث"},
        {"day": "الخميس", "planet": "المشتري", "upper": "صرفيائيل", "lower": "شمهورش قاضي الجن", "metal": "القصدير", "color": "#06b6d4", "incense": "العنبر والعود الفاخر", "char": "خ"},
        {"day": "الجمعة", "planet": "الزهرة", "upper": "عنيائيل", "lower": "زوبعة أبا حسن", "metal": "النحاس", "color": "#10b981", "incense": "المسك والزعفران", "char": "ز"},
        {"day": "السبت", "planet": "زحل", "upper": "كسفيائيل", "lower": "ميمون أبا نوخ", "metal": "الرصاص", "color": "#c084fc", "incense": "الميعة والحرمل", "char": "ذ"}
    ],
    "wafqs": [
        {"order": 3, "planet": "زحل", "constant": 15, "total": 45, "elements": "مثلث الغزالي الأقدس (بطد زهج واح)", "color": "#c084fc", "grid": [[4, 9, 2], [3, 5, 7], [8, 1, 6]]},
        {"order": 4, "planet": "المشتري", "constant": 34, "total": 136, "elements": "مربع الحكمة والعدل والتوسع", "color": "#06b6d4", "grid": [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]},
        {"order": 5, "planet": "المريخ", "constant": 65, "total": 325, "elements": "مخمس القوة والصهر والنصر", "color": "#ef4444", "grid": [[11, 24, 7, 20, 3], [4, 12, 25, 8, 16], [17, 5, 13, 21, 9], [10, 18, 1, 14, 22], [23, 6, 19, 2, 15]]},
        {"order": 6, "planet": "الشمس", "constant": 111, "total": 666, "elements": "مسدس الذهب ونور الروح والسيادة", "color": "#ffd700", "grid": [[35, 1, 6, 26, 19, 24], [3, 32, 7, 21, 23, 25], [31, 9, 2, 22, 27, 20], [8, 28, 33, 17, 10, 15], [30, 5, 34, 12, 14, 16], [4, 36, 29, 13, 18, 11]]},
        {"order": 7, "planet": "الزهرة", "constant": 175, "total": 1225, "elements": "مسبع الجمال والمحبة والتأليف", "color": "#10b981", "grid": "مصفوفة سباعية متناظرة الأقطار"},
        {"order": 8, "planet": "عطارد", "constant": 260, "total": 2080, "elements": "مثمن النطق والعلوم العقلية", "color": "#38bdf8", "grid": "مصفوفة ثمانية تامة الاتزان"},
        {"order": 9, "planet": "القمر", "constant": 369, "total": 3321, "elements": "متسع الفيض وتصريف الطينات السفلية", "color": "#f8fafc", "grid": "مصفوفة تساعية جامعة لفيوضات القمر"}
    ]
}

# Metadata for all 20 Chambers
CHAMBER_METADATA = {
    "tab-graph": {
        "num": "01",
        "title": "أطلس المفاهيم والشبكة الكونية الكبرى",
        "pavilion": "الجناح الأول: كوزمولوجيا التنزيل والملكوت",
        "verse": "﴿سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ الْحَقُّ﴾",
        "intro": "المستكشف التفاعلي للشبكة المفاهيمية الكوزمولوجية المترابطة؛ استعراض العقد المعرفية والروابط الوجودية بين آيات الكتاب المسطور ونواميس الكون المنظور."
    },
    "tab-spheres": {
        "num": "02",
        "title": "سلّم الأفلاك السبعة وعرش الرحمن",
        "pavilion": "الجناح الأول: كوزمولوجيا التنزيل والملكوت",
        "verse": "﴿الَّذِي خَلَقَ سَبْعَ سَمَاوَاتٍ طِبَاقًا ۖ مَّا تَرَىٰ فِي خَلْقِ الرَّحْمَٰنِ مِن تَفَاوُتٍ﴾",
        "intro": "التطابق المعماري الإعجازي بين السماوات السبع ومقامات الأنبياء (من فلك القمر لآدم عليه السلام حتى فلك زحل لإبراهيم الخليل والعرش المحيط للنبي الخاتم محمد ﷺ)، مع نسب المعادن والألوان والترددات."
    },
    "tab-matrix": {
        "num": "03",
        "title": "مصفوفة البناء المعماري الكوني",
        "pavilion": "الجناح الأول: كوزمولوجيا التنزيل والملكوت",
        "verse": "﴿وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ وَإِنَّا لَمُوسِعُونَ﴾",
        "intro": "المصفوفة الكونية الشاملة لمطابقة طبقات الوجود وعوالم الملك والملكوت والجبروت واللاهوت، وتفرعات الخلق السبعة وأصولها النورانية."
    },
    "tab-manuscripts": {
        "num": "04",
        "title": "أمهات المخطوطات والوثائق النادرة",
        "pavilion": "الجناح الأول: كوزمولوجيا التنزيل والملكوت",
        "verse": "﴿إِنَّا نَحْنُ نَزَّلْنَا الذِّكْرَ وَإِنَّا لَهُ لَحَافِظُونَ﴾",
        "intro": "خزانة المخطوطات المحققة والرسائل النادرة في الكوزمولوجيا والفلك القديم، مع التحقيق الإسنادي ونقد المتون وإبراز الأصول الإسلامية الأصيلة."
    },
    "tab-timeline": {
        "num": "05",
        "title": "تعاقب العصور والمبادرة المحورية (2,160 سنة)",
        "pavilion": "الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء",
        "verse": "﴿وَتِلْكَ الْأَيَّامُ نُدَاوِلُهَا بَيْنَ النَّاسِ﴾",
        "intro": "فيزياء الزمن الكوني وحركة المبادرة المحورية (Precession of the Equinoxes) وتعاقب الدورات الحضارية الكبرى في علاقتها بالنبوءات والتاريخ الإنساني."
    },
    "tab-zodiac": {
        "num": "06",
        "title": "دائرة البروج الاثني عشر والطبائع والميلوثيسيا",
        "pavilion": "الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء",
        "verse": "﴿وَالسَّمَاءِ ذَاتِ الْبُرُوجِ ۝ وَالْيَوْمِ الْمَوْعُودِ﴾",
        "intro": "تشريح دائرة البروج الاثني عشر، المثلثات الأربعة (نار، تراب، هواء، ماء)، قانون الأقطاب المتقابلة بزاوية 180 درجة، وتوزيع أعضاء الجسد البشري وفق علم الميلوثيسيا القديم المعتمد عند بطليموس والبيروني."
    },
    "tab-mansions": {
        "num": "07",
        "title": "منازل القمر الـ 28 والتوافقات الأثيرية",
        "pavilion": "الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء",
        "verse": "﴿وَالْقَمَرَ قَدَّرْنَاهُ مَنَازِلَ حَتَّىٰ عَادَ كَالْعُرْجُونِ الْقَدِيمِ﴾",
        "intro": "الموسوعة القمرية الشاملة للمنازل الثمانية والعشرين؛ درجاتها الدقيقة على مدار فلك البروج، الحرف العربي المناظر لكل منزلة، والطبائع الروحية والزراعية والطبية المتناغمة مع حركة القمر الشهرية."
    },
    "tab-hours": {
        "num": "08",
        "title": "ساعات الأيام الـ 24 الكلدانية وحكامها",
        "pavilion": "الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء",
        "verse": "﴿وَجَعَلْنَا اللَّيْلَ وَالنَّهَارَ آيَتَيْنِ ۖ فَمَحَوْنَا آيَةَ اللَّيْلِ وَجَعَلْنَا آيَةَ النَّهَارِ مُبْصِرَةً﴾",
        "intro": "الجدول الزمني الحسابي لساعات الليل والنهار الفلكية الكلدانية وحكامها، وطرق استخراج الساعات السعيدة والمعتدلة بحساب درجات الشمس."
    },
    "tab-kings": {
        "num": "09",
        "title": "ملوك الأفلاك والأيام السبعة الكبرى",
        "pavilion": "الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء",
        "verse": "﴿يُدَبِّرُ الْأَمْرَ مِنَ السَّمَاءِ إِلَى الْأَرْضِ ثُمَّ يَعْرُجُ إِلَيْهِ فِي يَوْمٍ كَانَ مِقْدَارُهُ أَلْفَ سَنَةٍ﴾",
        "intro": "ديوان الملوك العلويين والأرضيين وحكام الأيام السبعة؛ ارتباط كل يوم بكوكب ومدبر ومعدن وبخور، مع التحقيق الإبستمولوجي الذي ينفي الشركيات ويوضح أصل التسخير الإلهي."
    },
    "tab-astrology-calc": {
        "num": "10",
        "title": "المرصد الفلكي التنجيمي الكوني الشامل",
        "pavilion": "الجناح الثاني: الفلك الكوني ودورات الزمان والأنواء",
        "verse": "﴿فَنَظَرَ نَظْرَةً فِي النُّجُومِ ۝ فَقَالَ إِنِّي سَقِيمٌ﴾",
        "intro": "المرصد الرياضي التفاعلي؛ حساب مواضع الكواكب والمنازل والبروج بدقة فلكية معاصرة مع محرك إبستمولوجي يحذر من دعاوى الغيب."
    },
    "tab-letters-magic": {
        "num": "11",
        "title": "طبائع الحروف الـ 28 وعلم الجمل والأوفاق",
        "pavilion": "الجناح الثالث: الأوفاق والرياضيات المقدسة والفيزياء",
        "verse": "﴿ن ۚ وَالْقَلَمِ وَمَا يَسْطُرُونَ﴾",
        "intro": "علم الحرف الإلهي والرمز السيميائي؛ توزيع الحروف الـ 28 على العناصر الأربعة والطبائع، حساب الجمل الكبير والصغير، وهندسة ميزان الكلمات عند جابر بن حيان والبوني."
    },
    "tab-numbers": {
        "num": "12",
        "title": "ديوان الأوفاق والمربعات الرياضية (3×3 إلى 9×9)",
        "pavilion": "الجناح الثالث: الأوفاق والرياضيات المقدسة والفيزياء",
        "verse": "﴿وَكُلُّ شَيْءٍ عِندَهُ بِمِقْدَارٍ ۝ عَالِمُ الْغَيْبِ وَالشَّهَادَةِ الْكَبِيرُ الْمُتَعَالِ﴾",
        "intro": "المصفوفات السحرية والمربعات المتوازنة رياضياً من رتبة 3 (مثلث زحل الغزالي) إلى رتبة 9 (متسع القمر)، مع تحقيق توازن الأقطار والصفوف والأعمدة وتناظرها مع النواميس الكونية."
    },
    "tab-physics": {
        "num": "13",
        "title": "فيزياء الرنين المداري والمولد الصوتي الحي",
        "pavilion": "الجناح الثالث: الأوفاق والرياضيات المقدسة والفيزياء",
        "verse": "﴿وَإِن مِّن شَيْءٍ إِلَّا يُسَبِّحُ بِحَمْدِهِ وَلَٰكِن لَّا تَفْقَهُونَ تَسْبِيحَهُمْ﴾",
        "intro": "المختبر الصوتي الفيزيائي: ترددات سولفيجيو، نغمات هانز كوستو المدارية، ومحاكي الرنين والموجات الحية عبر Web Audio API."
    },
    "tab-chakras": {
        "num": "14",
        "title": "مجسم الشاكرات السبع والغدد ومقامات الرسل",
        "pavilion": "الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي",
        "verse": "﴿وَفِي أَنفُسِكُمْ ۚ أَفَلَا تُبْصِرُونَ﴾",
        "intro": "التشريح الأثيري للإنسان: مراكز الطاقة السبعة، الغدد الصماء، ومطابقتها لمقامات الأنبياء واللطائف الروحية في التراث الصوفي والمعرفي الأصيل."
    },
    "tab-bodies": {
        "num": "15",
        "title": "الأجساد السبعة وميكانيكا اختراق الهالة",
        "pavilion": "الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي",
        "verse": "﴿اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ ۚ مَثَلُ نُورِهِ كَمِشْكَاةٍ فِيهَا مِصْبَاحٌ﴾",
        "intro": "مستويات الكيان الإنساني من الجسد الطيني الكثيف إلى الجسد الأثيري والنجمي والعقلي والروحاني، وفيزياء الحقل التوريدي الواقي."
    },
    "tab-zodiac-angels": {
        "num": "16",
        "title": "ملائكة الأبراج والوجوه العشرية الـ 36 (Decans)",
        "pavilion": "الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي",
        "verse": "﴿وَالصَّافَّاتِ صَفًّا ۝ فَالزَّاجِرَاتِ زَجْرًا ۝ فَالتَّالِيَاتِ ذِكْرًا﴾",
        "intro": "المصفوفة الجامعة للوجوه الفلكية الـ 36 والملائكة والموكلين عليها عبر حضارات مصر القديمة (دندرة)، بابل، والتقاليد السيميائية الإسلامية."
    },
    "tab-seals-zouhri": {
        "num": "17",
        "title": "ديوان الأختام الرمزية والإنسان الزوهري والسلالات",
        "pavilion": "الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي",
        "verse": "﴿قَالَ الَّذِي عِندَهُ عِلْمٌ مِّنَ الْكِتَابِ أَنَا آتِيكَ بِهِ قَبْلَ أَن يَرْتَدَّ إِلَيْكَ طَرْفُكَ﴾",
        "intro": "دراسة علمية معمقة في فينوتايب الإنسان الزوهري، العلامات التشريحية، علم الأختام، وتفكيك الخرافات الشائعة بمنهج قرآني صارم."
    },
    "tab-inner-realms": {
        "num": "18",
        "title": "سفر العوالم الباطنية والإسقاط النجمي وموجات الدماغ",
        "pavilion": "الجناح الرابع: الهيكل الإنساني، الطاقات الباطنية والوعي",
        "verse": "﴿يَا مَعْشَرَ الْجِنِّ وَالْإِنسِ إِنِ اسْتَطَعْتُمْ أَن تَنفُذُوا مِنْ أَقْطَارِ السَّمَاوَاتِ وَالْأَرْضِ فَانفُذُوا﴾",
        "intro": "ميكانيكا الوعي الباطني: موجات الدماغ (ألفا، ثيتا، غاما)، الأحلام الجلية، السفر النجمي عبر التاريخ، والموقف الشرعي والتحذيرات الطبية."
    },
    "tab-critique": {
        "num": "19",
        "title": "ميزان القرآن ودحض التناقضات والخرافات",
        "pavilion": "الجناح الخامس: ميزان النقد والبرهان وحصن المرشد",
        "verse": "﴿بَلْ نَقْذِفُ بِالْحَقِّ عَلَى الْبَاطِلِ فَيَدْمَغُهُ فَإِذَا هُوَ زَاهِقٌ﴾",
        "intro": "المسطرة النقدية الصارمة للمرشد: رصد التحريفات في المخطوطات وتفكيك الإسرائيليات والخرافات بالدليل البرهاني القاطع والمنطق السديد."
    },
    "tab-criterion": {
        "num": "20",
        "title": "معيار الشريعة وحصن المرشد الباطني",
        "pavilion": "الجناح الخامس: ميزان النقد والبرهان وحصن المرشد",
        "verse": "﴿فَمَن يَكْفُرْ بِالطَّاغُوتِ وَيُؤْمِن بِاللَّهِ فَقَدِ اسْتَمْسَكَ بِالْعُرْوَةِ الْوُثْقَىٰ لَا انفِصَامَ لَهَا﴾",
        "intro": "المسطرة الإيمانية الصارمة: الفرق بين دراسة سنن الكون الفلكية وبين الشرك والعبودية لغير الله، وحماية النفس بوحي الخالق وتوحيده."
    }
}


def wrap_chamber_in_royal_manuscript(chamber_id, chamber_num, chamber_title, pavilion_badge, quran_verse, intro_folio, visual_html="", content_html=""):
    """
    Wraps any chamber inside the royal illuminated manuscript structure with 24K gold ornaments,
    tughra badge, Quranic verse banner, and celestial obsidian background.
    """
    return f"""
    <!-- CHAMBER {chamber_num}: {chamber_title} ({chamber_id}) -->
    <section id="{chamber_id}" class="tab-section chamber-view" style="display:none;">
        <div class="hub-container" style="max-width:1400px; margin:0 auto; padding:20px 15px;">
            <div class="manuscript-border-outer">
                <span class="corner-ornament corner-tl">۞</span>
                <span class="corner-ornament corner-tr">۞</span>
                <span class="corner-ornament corner-bl">۞</span>
                <span class="corner-ornament corner-br">۞</span>

                <div class="manuscript-border-inner">
                    <!-- FRONTISPIECE & ILLUMINATED HEAD -->
                    <div class="manuscript-frontispiece">
                        <div class="manuscript-tughra-badge">
                            <span>✦</span>
                            <span>{pavilion_badge} — الباب {chamber_num}</span>
                            <span>✦</span>
                        </div>
                        <div class="hub-quran-verse">
                            {quran_verse}
                        </div>
                        <h1 class="manuscript-main-heading">{chamber_title}</h1>
                        <p class="manuscript-intro-folio">
                            {intro_folio}
                        </p>
                    </div>

                    <!-- VISUAL DIAGRAMS & CANVAS OBSERVATORY -->
                    {visual_html}

                    <!-- MAIN CHAMBER CONTENT (CARDS, GRIDS, TABLES) -->
                    {content_html}
                </div>
            </div>
        </div>
    </section>
    """


def get_deluxe_chambers_css():
    return """
    /* ========================================================
       DELUXE COSMIC CHAMBERS MASTER STYLING
       ======================================================== */
    .chamber-canvas-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at 50% 50%, rgba(14, 20, 44, 0.95) 0%, rgba(6, 8, 20, 0.98) 100%);
        border: 2px solid var(--border-gold);
        border-radius: 24px;
        padding: 24px;
        margin: 20px auto 35px auto;
        max-width: 850px;
        box-shadow: 0 16px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(212, 175, 55, 0.15);
        position: relative;
    }

    .chamber-canvas-box canvas {
        width: 100%;
        max-width: 520px;
        height: auto;
        aspect-ratio: 1 / 1;
        filter: drop-shadow(0 0 20px rgba(212, 175, 55, 0.25));
    }

    .canvas-legend-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 18px;
        flex-wrap: wrap;
        margin-top: 14px;
        font-size: 0.85rem;
        color: #cbd5e1;
    }

    .canvas-legend-item {
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Interactive Grids Driven by JSON */
    .cosmic-cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 22px;
        margin-top: 25px;
    }

    .cosmic-gilded-card {
        background: linear-gradient(135deg, rgba(16, 22, 46, 0.9), rgba(9, 13, 28, 0.96));
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-radius: 20px;
        padding: 22px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        overflow: hidden;
    }

    .cosmic-gilded-card:hover {
        transform: translateY(-5px);
        border-color: var(--card-accent, var(--gold));
        box-shadow: 0 18px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(212, 175, 55, 0.25);
        background: linear-gradient(135deg, rgba(24, 34, 68, 0.94), rgba(13, 18, 40, 0.98));
    }

    .card-top-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
    }

    .card-rank-badge {
        font-family: 'Amiri', serif;
        font-size: 0.85rem;
        font-weight: 700;
        color: var(--gold-bright);
        background: rgba(212, 175, 55, 0.12);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 3px 10px;
        border-radius: 8px;
    }

    .card-sub-badge {
        font-size: 0.78rem;
        color: #94a3b8;
    }

    .card-main-title {
        font-family: 'Amiri', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: #fff;
        margin: 0 0 10px 0;
        line-height: 1.3;
    }

    .card-meta-table {
        display: flex;
        flex-direction: column;
        gap: 6px;
        font-size: 0.84rem;
        color: #cbd5e1;
        margin: 12px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        padding-top: 10px;
    }

    .card-meta-row {
        display: flex;
        justify-content: space-between;
    }

    .card-meta-lbl {
        color: #94a3b8;
    }

    .card-meta-val {
        color: #f8fafc;
        font-weight: 600;
    }

    .card-verse-quote {
        background: rgba(212, 175, 55, 0.08);
        border-right: 3px solid var(--gold);
        border-radius: 6px;
        padding: 8px 12px;
        font-family: 'Amiri', serif;
        font-size: 0.95rem;
        color: var(--gold-light);
        margin-top: 10px;
        line-height: 1.5;
    }

    /* Live Wafq Interactive Grid Display */
    .wafq-grid-table {
        margin: 15px auto;
        border-collapse: separate;
        border-spacing: 6px;
    }

    .wafq-cell {
        width: 52px;
        height: 52px;
        background: rgba(14, 20, 44, 0.9);
        border: 1.5px solid var(--border-gold);
        border-radius: 10px;
        text-align: center;
        vertical-align: middle;
        font-family: 'Amiri', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--gold-bright);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5), inset 0 0 10px rgba(212, 175, 55, 0.1);
        transition: all 0.2s;
    }

    .wafq-cell:hover {
        background: var(--gold);
        color: #070a14;
        box-shadow: 0 0 20px var(--gold-glow);
        transform: scale(1.08);
    }

    /* Abjad Live Interactive Box */
    .abjad-calc-box {
        background: rgba(11, 16, 36, 0.92);
        border: 2px solid var(--border-gold);
        border-radius: 22px;
        padding: 24px;
        max-width: 820px;
        margin: 0 auto 30px auto;
        box-shadow: 0 12px 40px rgba(0,0,0,0.7);
    }

    .abjad-input {
        width: 100%;
        background: #060816;
        border: 1.5px solid rgba(212, 175, 55, 0.35);
        border-radius: 12px;
        padding: 12px 18px;
        font-family: 'Amiri', serif;
        font-size: 1.35rem;
        color: #fff;
        text-align: center;
        margin-bottom: 20px;
        transition: all 0.2s;
    }

    .abjad-input:focus {
        outline: none;
        border-color: var(--gold);
        box-shadow: 0 0 20px var(--gold-glow);
    }

    .abjad-results-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        text-align: center;
    }

    .abjad-result-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 14px;
    }

    .abjad-val-big {
        font-family: 'Amiri', serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: var(--gold-bright);
        line-height: 1.1;
    }

    .elem-progress-bar {
        height: 8px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 4px;
        overflow: hidden;
        margin-top: 6px;
    }

    .elem-progress-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.4s ease;
    }
    """


def generate_spheres_chamber_html():
    spheres = COSMIC_DATABASE["spheres"]
    cards_html = ""
    for s in spheres:
        cards_html += f"""
        <div class="cosmic-gilded-card" style="--card-accent:{s['color']};">
            <div class="card-top-header">
                <span class="card-rank-badge">السماء {s['num']}</span>
                <span class="card-sub-badge">{s['prophet']}</span>
            </div>
            <h3 class="card-main-title">{s['name']}</h3>
            <div class="card-meta-table">
                <div class="card-meta-row"><span class="card-meta-lbl">المعدن الأثيري:</span><span class="card-meta-val">{s['metal']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">الجوهر والرمز:</span><span class="card-meta-val">{s['gem']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">الملاك الموكل:</span><span class="card-meta-val">{s['angel']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">تردد النغمة:</span><span class="card-meta-val" style="color:{s['color']};">{s['freq']}</span></div>
            </div>
            <p style="font-size:0.86rem; color:#cbd5e1; line-height:1.6; margin:6px 0;">{s['desc']}</p>
            <div class="card-verse-quote">{s['quran']}</div>
        </div>
        """

    visual_html = """
    <div class="chamber-canvas-box">
        <h3 style="font-family:'Amiri',serif; font-size:1.4rem; color:var(--gold-bright); margin-bottom:12px;">
            🪐 المحاذاة المدارية الحية للأفلاك السبعة وعرش الرحمن
        </h3>
        <canvas id="spheresOrbitsCanvas" width="550" height="550"></canvas>
        <div class="canvas-legend-row">
            <span class="canvas-legend-item"><i class="fa-solid fa-circle" style="color:#10b981; font-size:0.6rem;"></i> مركز الأرض (الطين)</span>
            <span class="canvas-legend-item"><i class="fa-solid fa-circle" style="color:#ffd700; font-size:0.6rem;"></i> المدارات السبعة</span>
            <span class="canvas-legend-item"><i class="fa-solid fa-circle" style="color:#c084fc; font-size:0.6rem;"></i> فلك الثوابت وزحل</span>
            <span class="canvas-legend-item"><i class="fa-solid fa-circle" style="color:#fef08a; font-size:0.6rem;"></i> سدرة المنتهى والعرش المحيط</span>
        </div>
    </div>
    """

    meta = CHAMBER_METADATA["tab-spheres"]
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-spheres",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html=visual_html,
        content_html=f'<div class="cosmic-cards-grid">{cards_html}</div>'
    )


def generate_zodiac_chamber_html():
    signs = COSMIC_DATABASE["zodiac"]
    cards_html = ""
    for z in signs:
        cards_html += f"""
        <div class="cosmic-gilded-card" style="--card-accent:{z['color']};">
            <div class="card-top-header">
                <span class="card-rank-badge" style="font-size:1.1rem;">{z['symbol']} برج {z['name']}</span>
                <span class="card-sub-badge">{z['dates']}</span>
            </div>
            <h3 class="card-main-title">{z['name']} ({z['element']} — {z['quality']})</h3>
            <div class="card-meta-table">
                <div class="card-meta-row"><span class="card-meta-lbl">الكوكب الحاكم:</span><span class="card-meta-val">{z['ruler']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">الملاك الموكل:</span><span class="card-meta-val">{z['angel']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">العضو في الجسد (ميلوثيسيا):</span><span class="card-meta-val">{z['body']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">القطب المتقابل (180°):</span><span class="card-meta-val" style="color:var(--gold);">{z['opposite']}</span></div>
            </div>
            <p style="font-size:0.86rem; color:#cbd5e1; line-height:1.6; margin:6px 0;">{z['secrets']}</p>
        </div>
        """

    visual_html = """
    <div class="chamber-canvas-box">
        <h3 style="font-family:'Amiri',serif; font-size:1.4rem; color:var(--gold-bright); margin-bottom:12px;">
            ♈ دائرة البروج الاثني عشر والمحاور المتقابلة (Polarity Wheel)
        </h3>
        <canvas id="zodiacWheelCanvas" width="500" height="500"></canvas>
        <div class="canvas-legend-row">
            <span class="canvas-legend-item"><i class="fa-solid fa-fire" style="color:#ef4444;"></i> ناري</span>
            <span class="canvas-legend-item"><i class="fa-solid fa-mountain" style="color:#d97706;"></i> ترابي</span>
            <span class="canvas-legend-item"><i class="fa-solid fa-wind" style="color:#38bdf8;"></i> هوائي</span>
            <span class="canvas-legend-item"><i class="fa-solid fa-water" style="color:#3b82f6;"></i> مائي</span>
        </div>
    </div>
    """

    meta = CHAMBER_METADATA["tab-zodiac"]
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-zodiac",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html=visual_html,
        content_html=f'<div class="cosmic-cards-grid">{cards_html}</div>'
    )


def generate_mansions_chamber_html():
    mansions = COSMIC_DATABASE["mansions"]
    cards_html = ""
    for m in mansions:
        cards_html += f"""
        <div class="cosmic-gilded-card">
            <div class="card-top-header">
                <span class="card-rank-badge">المنزلة {m['num']}</span>
                <span class="card-sub-badge">حرف {m['letter']}</span>
            </div>
            <h3 class="card-main-title">منزلة {m['name']}</h3>
            <div class="card-meta-table">
                <div class="card-meta-row"><span class="card-meta-lbl">الدرجة الفلكية:</span><span class="card-meta-val">{m['deg']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">العنصر الغالب:</span><span class="card-meta-val">{m['element']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">الخاصية والتأثير:</span><span class="card-meta-val" style="color:var(--emerald-accent);">{m['virtue']}</span></div>
            </div>
        </div>
        """

    meta = CHAMBER_METADATA["tab-mansions"]
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-mansions",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html="",
        content_html=f'<div class="cosmic-cards-grid">{cards_html}</div>'
    )


def generate_kings_chamber_html():
    kings = COSMIC_DATABASE["kings"]
    cards_html = ""
    for k in kings:
        cards_html += f"""
        <div class="cosmic-gilded-card" style="--card-accent:{k['color']};">
            <div class="card-top-header">
                <span class="card-rank-badge">{k['day']}</span>
                <span class="card-sub-badge">فلك {k['planet']}</span>
            </div>
            <h3 class="card-main-title">{k['upper']} (الملك العلوي)</h3>
            <div class="card-meta-table">
                <div class="card-meta-row"><span class="card-meta-lbl">الملك الأرضي الحاكم:</span><span class="card-meta-val" style="color:var(--gold);">{k['lower']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">المعدن:</span><span class="card-meta-val">{k['metal']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">البخور المناظر:</span><span class="card-meta-val">{k['incense']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">الحرف المكتوم:</span><span class="card-meta-val">{k['char']}</span></div>
            </div>
        </div>
        """

    visual_html = """
    <div class="chamber-canvas-box">
        <h3 style="font-family:'Amiri',serif; font-size:1.4rem; color:var(--gold-bright); margin-bottom:12px;">
            ⭐ المسبع الفلكي المقدس (Heptagram of Kings & Planets)
        </h3>
        <canvas id="heptagramCanvas" width="460" height="460"></canvas>
        <div class="canvas-legend-row">
            <span>تناغم أيام الأسبوع السبعة مع الملوك الروحانيين والأملاك العلوية الموكلة بحفظ النواميس</span>
        </div>
    </div>
    """

    meta = CHAMBER_METADATA["tab-kings"]
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-kings",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html=visual_html,
        content_html=f'<div class="cosmic-cards-grid">{cards_html}</div>'
    )


def generate_letters_chamber_html():
    visual_html = """
    <div class="abjad-calc-box">
        <h3 style="font-family:'Amiri',serif; font-size:1.5rem; color:var(--gold-bright); text-align:center; margin-bottom:12px;">
            🔢 حاسبة الجمل الكبير وميزان الطبائع الأربعة التفاعلية
        </h3>
        <p style="text-align:center; font-size:0.88rem; color:#cbd5e1; margin-bottom:18px;">
            اكتب أي اسم أو عبارة أو نص لحسابه بحساب الجمل الكبير، وفك توزيعه بين عناصر (النار، التراب، الهواء، الماء):
        </p>
        <input type="text" id="abjadInputText" class="abjad-input" placeholder="اكتب هنا مثلاً: الله نور السماوات والأرض..." oninput="calculateLiveAbjad()">
        
        <div class="abjad-results-row">
            <div class="abjad-result-card">
                <div style="font-size:0.8rem; color:#94a3b8;">القيمة الإجمالية (الجمل)</div>
                <div id="abjadTotalValue" class="abjad-val-big">0</div>
            </div>
            <div class="abjad-result-card">
                <div style="font-size:0.8rem; color:#94a3b8;">الطبع الغالب</div>
                <div id="abjadDominantNature" style="font-family:'Amiri',serif; font-size:1.3rem; font-weight:700; color:var(--emerald-accent); margin-top:8px;">متوازن</div>
            </div>
        </div>

        <div style="margin-top:20px; display:flex; flex-direction:column; gap:8px;">
            <div style="display:flex; justify-content:space-between; font-size:0.82rem; color:#cbd5e1;"><span>🔥 النار (أ هـ ط م ف ش ذ)</span></div>
            <div class="elem-progress-bar"><div id="elemBarFire" class="elem-progress-fill" style="width:25%; background:#ef4444;"></div></div>

            <div style="display:flex; justify-content:space-between; font-size:0.82rem; color:#cbd5e1;"><span>⛰️ التراب (ب و ي ن ص ت ض)</span></div>
            <div class="elem-progress-bar"><div id="elemBarEarth" class="elem-progress-fill" style="width:25%; background:#d97706;"></div></div>

            <div style="display:flex; justify-content:space-between; font-size:0.82rem; color:#cbd5e1;"><span>💨 الهواء (ج ز ك س ق ث ظ)</span></div>
            <div class="elem-progress-bar"><div id="elemBarAir" class="elem-progress-fill" style="width:25%; background:#38bdf8;"></div></div>

            <div style="display:flex; justify-content:space-between; font-size:0.82rem; color:#cbd5e1;"><span>💧 الماء (د ح ل ع ر خ غ)</span></div>
            <div class="elem-progress-bar"><div id="elemBarWater" class="elem-progress-fill" style="width:25%; background:#3b82f6;"></div></div>
        </div>
    </div>
    """

    meta = CHAMBER_METADATA["tab-letters-magic"]
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-letters-magic",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html=visual_html,
        content_html=""
    )


def generate_wafqs_chamber_html():
    wafqs = COSMIC_DATABASE["wafqs"]
    wafq_cards = ""
    for w in wafqs:
        grid_html = ""
        if isinstance(w["grid"], list):
            grid_html += '<table class="wafq-grid-table">'
            for row in w["grid"]:
                grid_html += '<tr>'
                for cell in row:
                    grid_html += f'<td class="wafq-cell">{cell}</td>'
                grid_html += '</tr>'
            grid_html += '</table>'
        else:
            grid_html = f'<div style="text-align:center; padding:18px; color:#94a3b8;">{w["grid"]}</div>'

        wafq_cards += f"""
        <div class="cosmic-gilded-card" style="--card-accent:{w['color']};">
            <div class="card-top-header">
                <span class="card-rank-badge">وفق {w['order']}×{w['order']}</span>
                <span class="card-sub-badge">كوكب {w['planet']}</span>
            </div>
            <h3 class="card-main-title">{w['elements']}</h3>
            <div class="card-meta-table">
                <div class="card-meta-row"><span class="card-meta-lbl">المفتاح العددي (Constant):</span><span class="card-meta-val" style="color:var(--gold);">{w['constant']}</span></div>
                <div class="card-meta-row"><span class="card-meta-lbl">مجموع أعداد الوفق:</span><span class="card-meta-val">{w['total']}</span></div>
            </div>
            {grid_html}
        </div>
        """

    meta = CHAMBER_METADATA["tab-numbers"]
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-numbers",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html="",
        content_html=f'<div class="cosmic-cards-grid">{wafq_cards}</div>'
    )


def get_deluxe_chambers_html():
    """Generates and combines all deluxe manuscript chambers."""
    return (
        generate_spheres_chamber_html() +
        generate_zodiac_chamber_html() +
        generate_mansions_chamber_html() +
        generate_kings_chamber_html() +
        generate_letters_chamber_html() +
        generate_wafqs_chamber_html()
    )


def extract_tag_content(html_text, tag_name, elem_id):
    pattern = rf'<{tag_name}\s+[^>]*id="{elem_id}"[^>]*>'
    m = re.search(pattern, html_text)
    if not m:
        return None
    start_pos = m.start()
    content_start = m.end()

    depth = 1
    pos = content_start
    open_tag_regex = re.compile(rf'<{tag_name}\b[^>]*>', re.IGNORECASE)
    close_tag_regex = re.compile(rf'</{tag_name}>', re.IGNORECASE)

    while depth > 0 and pos < len(html_text):
        next_open = open_tag_regex.search(html_text, pos)
        next_close = close_tag_regex.search(html_text, pos)

        if not next_close:
            break

        if next_open and next_open.start() < next_close.start():
            depth += 1
            pos = next_open.end()
        else:
            depth -= 1
            if depth == 0:
                end_pos = next_close.end()
                inner_content = html_text[content_start:next_close.start()]
                return start_pos, end_pos, inner_content
            pos = next_close.end()

    return None


def wrap_all_raw_chambers(html_content):
    """
    Scans the HTML for any chamber (section or div) that is NOT yet wrapped
    in .manuscript-border-outer, and wraps its inner contents in the royal manuscript architecture.
    This guarantees 100% illuminated manuscript uniformity across ALL 20 chambers!
    """
    for chamber_id, meta in CHAMBER_METADATA.items():
        # Skip chambers that are already replaced by deluxe versions
        if chamber_id in ["tab-spheres", "tab-zodiac", "tab-mansions", "tab-kings", "tab-letters-magic", "tab-numbers"]:
            continue

        for tag in ["section", "div"]:
            res = extract_tag_content(html_content, tag, chamber_id)
            if res:
                start_pos, end_pos, inner_content = res

                # If already wrapped, skip
                if 'manuscript-border-outer' in inner_content:
                    break

                wrapped_chamber = f"""
    <!-- CHAMBER {meta['num']}: {meta['title']} ({chamber_id}) -->
    <section id="{chamber_id}" class="tab-section chamber-view" style="display:none;">
        <div class="hub-container" style="max-width:1400px; margin:0 auto; padding:20px 15px;">
            <div class="manuscript-border-outer">
                <span class="corner-ornament corner-tl">۞</span>
                <span class="corner-ornament corner-tr">۞</span>
                <span class="corner-ornament corner-bl">۞</span>
                <span class="corner-ornament corner-br">۞</span>

                <div class="manuscript-border-inner">
                    <!-- FRONTISPIECE & ILLUMINATED HEAD -->
                    <div class="manuscript-frontispiece">
                        <div class="manuscript-tughra-badge">
                            <span>✦</span>
                            <span>{meta['pavilion']} — الباب {meta['num']}</span>
                            <span>✦</span>
                        </div>
                        <div class="hub-quran-verse">
                            {meta['verse']}
                        </div>
                        <h1 class="manuscript-main-heading">{meta['title']}</h1>
                        <p class="manuscript-intro-folio">
                            {meta['intro']}
                        </p>
                    </div>

                    <!-- CHAMBER BODY -->
                    {inner_content}
                </div>
            </div>
        </div>
    </section>
    """
                html_content = html_content[:start_pos] + wrapped_chamber + html_content[end_pos:]
                break

    return html_content


def get_cosmic_database_js():
    """Returns the complete JavaScript database injection for the client-side engine."""
    db_json = json.dumps(COSMIC_DATABASE, ensure_ascii=False)
    return f"""
    // ========================================================
    // KNOWLEDGE LAB — CLIENT-SIDE MASTER COSMIC DATABASE
    // ========================================================
    window.COSMIC_DATABASE = {db_json};
    console.log("🌌 [COSMIC_DATABASE] Loaded successfully with", Object.keys(window.COSMIC_DATABASE).length, "master catalogs.");
    """


def get_chambers_visual_js():
    """Returns the interactive Canvas drawings and live mathematical calculation scripts."""
    return """
    // ========================================================
    // KNOWLEDGE LAB — INTERACTIVE CANVAS & CALCULATION SCRIPTS
    // ========================================================

    // 1. SPHERES CONCENTRIC ORBITS CANVAS
    function renderSpheresOrbits() {
        const canvas = document.getElementById('spheresOrbitsCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const w = canvas.width;
        const h = canvas.height;
        const cx = w / 2;
        const cy = h / 2;

        ctx.clearRect(0, 0, w, h);

        // Center Earth
        const centerGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, 25);
        centerGrad.addColorStop(0, '#34d399');
        centerGrad.addColorStop(1, '#065f46');
        ctx.beginPath();
        ctx.arc(cx, cy, 22, 0, Math.PI * 2);
        ctx.fillStyle = centerGrad;
        ctx.fill();
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 11px Amiri';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('الأرض', cx, cy);

        // 7 Spheres + Throne
        const spheresData = (window.COSMIC_DATABASE && window.COSMIC_DATABASE.spheres) ? window.COSMIC_DATABASE.spheres : [
            {name: 'القمر', color: '#f8fafc', r: 45},
            {name: 'عطارد', color: '#38bdf8', r: 70},
            {name: 'الزهرة', color: '#10b981', r: 95},
            {name: 'الشمس', color: '#ffd700', r: 125},
            {name: 'المريخ', color: '#ef4444', r: 155},
            {name: 'المشتري', color: '#06b6d4', r: 185},
            {name: 'زحل', color: '#c084fc', r: 215},
            {name: 'العرش المحيط', color: '#fef08a', r: 245}
        ];

        spheresData.forEach((s, idx) => {
            const radius = 45 + (idx * 28);
            
            // Orbit Ring
            ctx.beginPath();
            ctx.arc(cx, cy, radius, 0, Math.PI * 2);
            ctx.strokeStyle = (s.color || '#d4af37') + '55';
            ctx.lineWidth = 1.5;
            ctx.setLineDash([4, 4]);
            ctx.stroke();
            ctx.setLineDash([]);

            // Orbit Planet Marker
            const angle = (idx * 0.85) + (Date.now() * 0.0003 * (8 - idx));
            const px = cx + Math.cos(angle) * radius;
            const py = cy + Math.sin(angle) * radius;

            ctx.beginPath();
            ctx.arc(px, py, 6, 0, Math.PI * 2);
            ctx.fillStyle = s.color || '#ffd700';
            ctx.shadowColor = s.color || '#ffd700';
            ctx.shadowBlur = 10;
            ctx.fill();
            ctx.shadowBlur = 0;

            // Name Label
            ctx.fillStyle = s.color || '#fff';
            ctx.font = '10px Amiri';
            ctx.fillText(s.planet || s.name, px, py - 10);
        });
    }

    // 2. ZODIAC POLARITY WHEEL CANVAS
    function renderZodiacWheel() {
        const canvas = document.getElementById('zodiacWheelCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const w = canvas.width;
        const h = canvas.height;
        const cx = w / 2;
        const cy = h / 2;
        const outerR = (w / 2) - 25;
        const innerR = 40;

        ctx.clearRect(0, 0, w, h);

        const signs = (window.COSMIC_DATABASE && window.COSMIC_DATABASE.zodiac) ? window.COSMIC_DATABASE.zodiac : [];
        if (signs.length !== 12) return;

        const slice = (Math.PI * 2) / 12;

        signs.forEach((z, i) => {
            const startA = (i * slice) - (Math.PI / 2);
            const endA = startA + slice;
            const midA = startA + (slice / 2);

            // Sector
            ctx.beginPath();
            ctx.moveTo(cx, cy);
            ctx.arc(cx, cy, outerR, startA, endA);
            ctx.closePath();
            ctx.fillStyle = (z.color || '#d4af37') + '22';
            ctx.fill();
            ctx.strokeStyle = 'rgba(212, 175, 55, 0.4)';
            ctx.lineWidth = 1;
            ctx.stroke();

            // Symbol and Name
            const textR = outerR - 35;
            const tx = cx + Math.cos(midA) * textR;
            const ty = cy + Math.sin(midA) * textR;

            ctx.fillStyle = z.color || '#ffd700';
            ctx.font = 'bold 15px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(z.symbol, tx, ty - 6);

            ctx.font = 'bold 11px Amiri';
            ctx.fillStyle = '#f8fafc';
            ctx.fillText(z.name, tx, ty + 10);
        });

        // Opposite Polarity Axes (6 lines across center)
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
            const a = (i * slice) - (Math.PI / 2) + (slice / 2);
            const x1 = cx + Math.cos(a) * (outerR - 15);
            const y1 = cy + Math.sin(a) * (outerR - 15);
            const x2 = cx + Math.cos(a + Math.PI) * (outerR - 15);
            const y2 = cy + Math.sin(a + Math.PI) * (outerR - 15);
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
        }
        ctx.strokeStyle = 'rgba(212, 175, 55, 0.25)';
        ctx.lineWidth = 1;
        ctx.setLineDash([2, 4]);
        ctx.stroke();
        ctx.setLineDash([]);

        // Center Sun Hub
        const hubGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, innerR);
        hubGrad.addColorStop(0, '#ffd700');
        hubGrad.addColorStop(1, '#92400e');
        ctx.beginPath();
        ctx.arc(cx, cy, innerR, 0, Math.PI * 2);
        ctx.fillStyle = hubGrad;
        ctx.fill();
        ctx.strokeStyle = '#d4af37';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#070a14';
        ctx.font = 'bold 12px Amiri';
        ctx.fillText('ميزان الفلك', cx, cy);
    }

    // 3. HEPTAGRAM PLANETARY KINGS CANVAS
    function renderHeptagramKings() {
        const canvas = document.getElementById('heptagramCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const w = canvas.width;
        const h = canvas.height;
        const cx = w / 2;
        const cy = h / 2;
        const r = (w / 2) - 45;

        ctx.clearRect(0, 0, w, h);

        const kings = (window.COSMIC_DATABASE && window.COSMIC_DATABASE.kings) ? window.COSMIC_DATABASE.kings : [];
        if (kings.length !== 7) return;

        const points = [];
        for (let i = 0; i < 7; i++) {
            const angle = (i * (Math.PI * 2 / 7)) - (Math.PI / 2);
            points.push({
                x: cx + Math.cos(angle) * r,
                y: cy + Math.sin(angle) * r,
                king: kings[i]
            });
        }

        // Outer Ring
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(212, 175, 55, 0.4)';
        ctx.lineWidth = 2;
        ctx.stroke();

        // 7-Pointed Star Connections (step of 2)
        ctx.beginPath();
        ctx.strokeStyle = 'rgba(212, 175, 55, 0.85)';
        ctx.lineWidth = 1.8;
        ctx.shadowColor = 'rgba(212, 175, 55, 0.6)';
        ctx.shadowBlur = 8;
        for (let i = 0; i < 7; i++) {
            const nextIdx = (i * 2) % 7;
            if (i === 0) ctx.moveTo(points[nextIdx].x, points[nextIdx].y);
            else ctx.lineTo(points[nextIdx].x, points[nextIdx].y);
        }
        ctx.closePath();
        ctx.stroke();
        ctx.shadowBlur = 0;

        // Draw Vertex Badges
        points.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 22, 0, Math.PI * 2);
            ctx.fillStyle = '#080c1d';
            ctx.fill();
            ctx.strokeStyle = p.king.color || '#d4af37';
            ctx.lineWidth = 2;
            ctx.stroke();

            ctx.fillStyle = p.king.color || '#ffd700';
            ctx.font = 'bold 10px Amiri';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(p.king.day, p.x, p.y - 5);
            ctx.fillStyle = '#cbd5e1';
            ctx.font = '9px Tajawal';
            ctx.fillText(p.king.planet, p.x, p.y + 7);
        });

        // Center Seal
        ctx.beginPath();
        ctx.arc(cx, cy, 30, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(16, 185, 129, 0.2)';
        ctx.fill();
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = '#34d399';
        ctx.font = 'bold 12px Amiri';
        ctx.fillText('المسبع', cx, cy - 6);
        ctx.font = '9px Tajawal';
        ctx.fillText('الحكام السبعة', cx, cy + 8);
    }

    // 4. LIVE ABJAD & 4 ELEMENTS CALCULATOR
    const ABJAD_VALUES = {
        'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ء': 1, 'ب': 2, 'ج': 3, 'د': 4,
        'ه': 5, 'هـ': 5, 'ة': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10,
        'ى': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70,
        'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400,
        'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
    };

    const FIRE_LETTERS = new Set(['ا', 'أ', 'إ', 'آ', 'ء', 'ه', 'هـ', 'ة', 'ط', 'م', 'ف', 'ش', 'ذ']);
    const EARTH_LETTERS = new Set(['ب', 'و', 'ي', 'ى', 'ن', 'ص', 'ت', 'ض']);
    const AIR_LETTERS = new Set(['ج', 'ز', 'ك', 'س', 'ق', 'ث', 'ظ']);
    const WATER_LETTERS = new Set(['د', 'ح', 'ل', 'ع', 'ر', 'خ', 'غ']);

    function calculateLiveAbjad() {
        const input = document.getElementById('abjadInputText');
        if (!input) return;
        const text = input.value.trim();

        let total = 0;
        let fireCount = 0;
        let earthCount = 0;
        let airCount = 0;
        let waterCount = 0;

        for (let char of text) {
            if (ABJAD_VALUES[char]) {
                total += ABJAD_VALUES[char];
                if (FIRE_LETTERS.has(char)) fireCount++;
                else if (EARTH_LETTERS.has(char)) earthCount++;
                else if (AIR_LETTERS.has(char)) airCount++;
                else if (WATER_LETTERS.has(char)) waterCount++;
            }
        }

        const totalLetters = (fireCount + earthCount + airCount + waterCount) || 1;
        const pFire = Math.round((fireCount / totalLetters) * 100);
        const pEarth = Math.round((earthCount / totalLetters) * 100);
        const pAir = Math.round((airCount / totalLetters) * 100);
        const pWater = Math.round((waterCount / totalLetters) * 100);

        const valElem = document.getElementById('abjadTotalValue');
        if (valElem) valElem.innerText = total.toLocaleString('ar-EG');

        const barFire = document.getElementById('elemBarFire');
        if (barFire) barFire.style.width = pFire + '%';

        const barEarth = document.getElementById('elemBarEarth');
        if (barEarth) barEarth.style.width = pEarth + '%';

        const barAir = document.getElementById('elemBarAir');
        if (barAir) barAir.style.width = pAir + '%';

        const barWater = document.getElementById('elemBarWater');
        if (barWater) barWater.style.width = pWater + '%';

        // Dominant Nature
        const domElem = document.getElementById('abjadDominantNature');
        if (domElem) {
            if (total === 0) {
                domElem.innerText = 'متوازن';
                domElem.style.color = 'var(--emerald-accent)';
            } else {
                const maxVal = Math.max(fireCount, earthCount, airCount, waterCount);
                if (maxVal === fireCount) {
                    domElem.innerText = 'ناري (حار يابس)';
                    domElem.style.color = '#ef4444';
                } else if (maxVal === earthCount) {
                    domElem.innerText = 'ترابي (بارد يابس)';
                    domElem.style.color = '#d97706';
                } else if (maxVal === airCount) {
                    domElem.innerText = 'هوائي (حار رطب)';
                    domElem.style.color = '#38bdf8';
                } else {
                    domElem.innerText = 'مائي (بارد رطب)';
                    domElem.style.color = '#3b82f6';
                }
            }
        }
    }

    // Trigger visual renders on chamber switches
    window.addEventListener('chamberSwitched', function(e) {
        const id = e.detail && e.detail.chamberId;
        if (id === 'tab-spheres') setTimeout(renderSpheresOrbits, 50);
        if (id === 'tab-zodiac') setTimeout(renderZodiacWheel, 50);
        if (id === 'tab-kings') setTimeout(renderHeptagramKings, 50);
    });

    // Initial render attempt
    setTimeout(function() {
        renderSpheresOrbits();
        renderZodiacWheel();
        renderHeptagramKings();
    }, 600);
    """
