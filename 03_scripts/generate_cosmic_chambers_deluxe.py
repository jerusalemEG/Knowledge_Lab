# -*- coding: utf-8 -*-
"""
Knowledge Lab - Deluxe Cosmic Chambers & JSON Engine (جنة العلوم الباطنية الشاملة)
Engineered for supreme architectural organization, full indexing across all 20 chambers,
illuminated manuscript styling, embedded JSON data, and rich interactive visual graphics.
"""

import json
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPH_JSON_PATH = os.path.join(SCRIPT_DIR, "knowledge_graph.json")
VAULT_NODES_DATA = {}
if os.path.exists(GRAPH_JSON_PATH):
    try:
        with open(GRAPH_JSON_PATH, "r", encoding="utf-8") as f:
            raw_g = json.load(f)
            VAULT_NODES_DATA = raw_g.get("nodes", {})
    except Exception as e:
        print(f"Warning loading {GRAPH_JSON_PATH}: {e}")

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
        background: radial-gradient(circle at 50% 50%, #ffffff 0%, #f8fafc 60%, #edf2f7 100%);
        border: 2px solid var(--border-gold);
        border-radius: 24px;
        padding: 24px;
        margin: 20px auto 35px auto;
        max-width: 850px;
        box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08), 0 0 25px rgba(184, 134, 11, 0.12);
        position: relative;
    }

    .chamber-canvas-box canvas {
        width: 100%;
        max-width: 520px;
        height: auto;
        aspect-ratio: 1 / 1;
        filter: drop-shadow(0 4px 15px rgba(184, 134, 11, 0.15));
    }

    .canvas-legend-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 18px;
        flex-wrap: wrap;
        margin-top: 14px;
        font-size: 0.85rem;
        color: #475569;
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
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 20px;
        padding: 22px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
        overflow: hidden;
    }

    .cosmic-gilded-card:hover {
        transform: translateY(-5px);
        border-color: var(--card-accent, var(--gold));
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08), 0 0 20px rgba(184, 134, 11, 0.15);
        background: #fafbfc;
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
        color: var(--gold);
        background: rgba(212, 175, 55, 0.12);
        border: 1px solid rgba(184, 134, 11, 0.35);
        padding: 3px 10px;
        border-radius: 8px;
    }

    .card-sub-badge {
        font-size: 0.78rem;
        color: #64748b;
    }

    .card-main-title {
        font-family: 'Amiri', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: #0f172a;
        margin: 0 0 10px 0;
        line-height: 1.3;
    }

    .card-meta-table {
        display: flex;
        flex-direction: column;
        gap: 6px;
        font-size: 0.84rem;
        color: #334155;
        margin: 12px 0;
        border-top: 1px solid #e2e8f0;
        padding-top: 10px;
    }

    .card-meta-row {
        display: flex;
        justify-content: space-between;
    }

    .card-meta-lbl {
        color: #64748b;
    }

    .card-meta-val {
        color: #0f172a;
        font-weight: 600;
    }

    .card-verse-quote {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(254, 240, 138, 0.25));
        border-right: 3px solid var(--gold);
        border-radius: 6px;
        padding: 8px 12px;
        font-family: 'Amiri', serif;
        font-size: 0.95rem;
        color: #854d0e;
        margin-top: 10px;
        line-height: 1.5;
        font-weight: 600;
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
        background: #ffffff;
        border: 1.5px solid var(--border-gold);
        border-radius: 10px;
        text-align: center;
        vertical-align: middle;
        font-family: 'Amiri', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #0f172a;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
        transition: all 0.2s;
    }

    .wafq-cell:hover {
        background: var(--gold);
        color: #ffffff;
        box-shadow: 0 0 15px var(--gold-glow);
        transform: scale(1.08);
    }

    /* Abjad Live Interactive Box */
    .abjad-calc-box {
        background: #ffffff;
        border: 2px solid var(--border-gold);
        border-radius: 22px;
        padding: 24px;
        max-width: 820px;
        margin: 0 auto 30px auto;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.06);
    }

    .abjad-input {
        width: 100%;
        background: #f8fafc;
        border: 1.5px solid #cbd5e1;
        border-radius: 12px;
        padding: 12px 18px;
        font-family: 'Amiri', serif;
        font-size: 1.35rem;
        color: #0f172a;
        text-align: center;
        margin-bottom: 20px;
        transition: all 0.2s;
    }

    .abjad-input:focus {
        outline: none;
        border-color: var(--gold);
        box-shadow: 0 0 15px var(--gold-glow);
    }

    .abjad-results-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        text-align: center;
    }

    .abjad-result-card {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 14px;
        padding: 14px;
    }

    .abjad-val-big {
        font-family: 'Amiri', serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: var(--gold);
        line-height: 1.1;
    }

    .elem-progress-bar {
        height: 8px;
        background: #e2e8f0;
        border-radius: 4px;
        overflow: hidden;
        margin-top: 6px;
    }

    .elem-progress-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.4s ease;
    }

    /* ========================================================
       CHAMBER 01: ATLAS OF CONCEPTS (أطلس الأقسام والشروح المنظمة)
       ======================================================== */
    .atlas-controls-bar {
        display: flex;
        flex-direction: column;
        gap: 16px;
        margin-bottom: 24px;
    }

    .atlas-pills-scroll {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
        justify-content: center;
    }

    .atlas-cat-pill {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 20px;
        padding: 8px 18px;
        color: #334155;
        font-family: 'Amiri', serif;
        font-size: 0.95rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 1px 4px rgba(15, 23, 42, 0.03);
    }

    .atlas-cat-pill:hover {
        border-color: var(--gold);
        color: #0f172a;
        background: #f8fafc;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(184, 134, 11, 0.15);
    }

    .atlas-cat-pill.active {
        background: linear-gradient(135deg, var(--gold), #d4af37);
        border-color: var(--gold);
        color: #ffffff;
        box-shadow: 0 2px 12px rgba(184, 134, 11, 0.3);
    }

    .atlas-search-box {
        width: 100%;
        max-width: 650px;
        margin: 0 auto;
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 25px;
        padding: 12px 24px;
        color: #0f172a;
        font-size: 1rem;
        font-family: 'Tajawal', sans-serif;
        outline: none;
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
        transition: all 0.3s ease;
        text-align: right;
        display: block;
    }

    .atlas-search-box:focus {
        border-color: var(--gold);
        box-shadow: 0 0 15px rgba(184, 134, 11, 0.3);
    }

    .atlas-workspace-grid {
        display: grid;
        grid-template-columns: 360px 1fr;
        gap: 24px;
        align-items: start;
    }

    @media (max-width: 992px) {
        .atlas-workspace-grid {
            grid-template-columns: 1fr;
        }
    }

    .atlas-sidebar-panel {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1.5px solid #cbd5e1;
        border-radius: 20px;
        padding: 18px;
        box-shadow: 0 6px 25px rgba(15, 23, 42, 0.05);
    }

    .atlas-sidebar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1.5px solid rgba(184, 134, 11, 0.25);
        padding-bottom: 12px;
        margin-bottom: 14px;
    }

    .atlas-sidebar-title {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        color: var(--gold);
        font-weight: 700;
    }

    .atlas-cat-count {
        background: rgba(212, 175, 55, 0.15);
        border: 1px solid rgba(184, 134, 11, 0.35);
        border-radius: 12px;
        padding: 2px 10px;
        font-size: 0.8rem;
        color: var(--gold);
        font-weight: 700;
    }

    .atlas-nodes-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
        max-height: 720px;
        overflow-y: auto;
        padding-left: 4px;
    }

    .atlas-nodes-list::-webkit-scrollbar {
        width: 6px;
    }
    .atlas-nodes-list::-webkit-scrollbar-thumb {
        background: rgba(184, 134, 11, 0.35);
        border-radius: 3px;
    }

    .atlas-node-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 14px;
        padding: 14px;
        cursor: pointer;
        transition: all 0.25s ease;
        position: relative;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
    }

    .atlas-node-card:hover {
        background: #f8fafc;
        border-color: var(--gold);
        transform: translateX(-4px);
        box-shadow: 0 4px 12px rgba(184, 134, 11, 0.12);
    }

    .atlas-node-card.active {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), rgba(254, 240, 138, 0.3));
        border: 1.5px solid var(--gold);
        box-shadow: 0 2px 10px rgba(184, 134, 11, 0.2);
    }

    .atlas-node-card-title {
        font-family: 'Amiri', serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
        line-height: 1.4;
    }

    .atlas-node-card.active .atlas-node-card-title {
        color: #854d0e;
    }

    .atlas-node-card-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.78rem;
        color: #64748b;
    }

    .atlas-dossier-panel {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 24px;
        padding: 32px 28px;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.05);
        min-height: 500px;
    }

    .atlas-dossier-header {
        border-bottom: 1.5px solid rgba(184, 134, 11, 0.25);
        padding-bottom: 20px;
        margin-bottom: 24px;
    }

    .atlas-dossier-title {
        font-family: 'Amiri', serif;
        font-size: 1.85rem;
        font-weight: 700;
        color: #0f172a;
        margin: 0 0 12px 0;
        line-height: 1.35;
    }

    .atlas-dossier-meta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
    }

    .atlas-tag-pill {
        background: rgba(212, 175, 55, 0.12);
        border: 1px solid rgba(184, 134, 11, 0.35);
        border-radius: 12px;
        padding: 3px 10px;
        font-size: 0.8rem;
        color: var(--gold);
        font-weight: 600;
    }

    .atlas-dossier-body {
        font-size: 1.05rem;
        line-height: 1.9;
        color: #1e293b;
        font-family: 'Tajawal', sans-serif;
    }

    .atlas-dossier-body h1, .atlas-dossier-body h2, .atlas-dossier-body h3 {
        font-family: 'Amiri', serif;
        color: #0f172a;
        margin-top: 24px;
        margin-bottom: 12px;
        border-bottom: 1.5px solid #e2e8f0;
        padding-bottom: 6px;
    }

    .atlas-dossier-body blockquote {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(254, 240, 138, 0.25));
        border-right: 4px solid var(--gold);
        border-radius: 12px;
        padding: 14px 20px;
        margin: 18px 0;
        color: #854d0e;
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        font-weight: 700;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .atlas-dossier-body ul, .atlas-dossier-body ol {
        margin: 14px 0 14px 24px;
        padding: 0;
    }

    .atlas-dossier-body li {
        margin-bottom: 8px;
    }

    .atlas-conns-box {
        margin-top: 36px;
        padding-top: 20px;
        border-top: 1.5px solid #e2e8f0;
    }

    .atlas-conns-title {
        font-family: 'Amiri', serif;
        font-size: 1.15rem;
        color: var(--gold);
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .atlas-conns-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .atlas-conn-item {
        background: rgba(2, 132, 199, 0.08);
        border: 1px solid rgba(2, 132, 199, 0.3);
        border-radius: 16px;
        padding: 6px 14px;
        color: #0284c7;
        font-size: 0.88rem;
        font-family: 'Amiri', serif;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.25s ease;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    .atlas-conn-item:hover {
        background: rgba(2, 132, 199, 0.18);
        border-color: #0284c7;
        transform: translateY(-2px);
    }
    """


def generate_graph_chamber_html():
    meta = CHAMBER_METADATA["tab-graph"]

    categories = [
        {"name": "ALL", "label": "🌐 الكل", "color": "#ffd700"},
        {"name": "أولو العزم من الرسل", "label": "👑 أولو العزم من الرسل", "color": "#ffd166"},
        {"name": "الهيكل القرآني والمصفوفات", "label": "🔴 الهيكل القرآني والمصفوفات", "color": "#ff4d6d"},
        {"name": "دائرة البروج الاثني عشر", "label": "♈ دائرة البروج (12)", "color": "#ff9f1c"},
        {"name": "الميلوثيسيا وتصريف القوى", "label": "🟣 الميلوثيسيا وتصريف القوى", "color": "#9d4edd"},
        {"name": "المخطوطات والحكماء", "label": "🌿 أمهات المخطوطات والحكماء", "color": "#70e000"},
        {"name": "العصور والرسالات التاريخية", "label": "🟡 العصور والرسالات", "color": "#ffb703"},
        {"name": "الدورات الكونية والفلك", "label": "🔵 الدورات الفلكية", "color": "#00b4d8"},
        {"name": "الهرمسية والكيمياء القديمة", "label": "⚗️ الخيمياء والهرمسية", "color": "#06d6a0"},
        {"name": "مفاهيم عامة", "label": "🌌 مفاهيم كوزمولوجية", "color": "#3a86ff"}
    ]

    cat_pills_html = ""
    for c in categories:
        active_cls = " active" if c["name"] == "ALL" else ""
        cat_pills_html += f'<button class="atlas-cat-pill{active_cls}" data-cat="{c["name"]}" onclick="filterAtlasCategory(\'{c["name"]}\')" style="--pill-color:{c["color"]};"><span>{c["label"]}</span></button>'

    content_html = f"""
    <div class="atlas-controls-bar">
        <div class="atlas-pills-scroll">
            {cat_pills_html}
        </div>
        <input type="text" id="atlas-search-input" class="atlas-search-box" placeholder="🔍 ابحث في عناوين وشروح ومصطلحات الشبكة المعرفية..." oninput="handleAtlasSearch(this.value)">
    </div>

    <div class="atlas-workspace-grid">
        <!-- SIDEBAR: CONCEPTS DIRECTORY -->
        <div class="atlas-sidebar-panel">
            <div class="atlas-sidebar-header">
                <span id="atlas-sidebar-cat-label" class="atlas-sidebar-title">🌐 كافة مفاهيم الشبكة الكونية</span>
                <span id="atlas-nodes-count-badge" class="atlas-cat-count">جاري التحميل...</span>
            </div>
            <div id="atlas-nodes-list" class="atlas-nodes-list">
                <!-- Dynamically populated via JS -->
            </div>
        </div>

        <!-- MAIN: FULL EXPLANATION DOSSIER IN-PAGE -->
        <div class="atlas-dossier-panel" id="atlas-dossier-panel">
            <div id="atlas-dossier-header" class="atlas-dossier-header">
                <h2 id="atlas-dossier-title" class="atlas-dossier-title">جاري تحميل المعارف الكونية...</h2>
                <div id="atlas-dossier-meta" class="atlas-dossier-meta-row"></div>
            </div>

            <div id="atlas-dossier-body" class="atlas-dossier-body">
                <!-- Formatted full explanation -->
            </div>

            <div id="atlas-conns-box" class="atlas-conns-box">
                <div class="atlas-conns-title">
                    <i class="fa-solid fa-circle-nodes"></i>
                    <span>المفاهيم والعقد المتصلة بهذا الأصل في شبكة المعرفة:</span>
                </div>
                <div id="atlas-dossier-connections" class="atlas-conns-grid">
                    <!-- Connected pills -->
                </div>
            </div>
        </div>
    </div>
    """

    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-graph",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html="",
        content_html=content_html
    )


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
    legacy_dom_safety = '<div id="spheres-list" style="display:none;"></div><div id="sphere-detail" style="display:none;"></div><table style="display:none;"><tbody id="panoramic-spheres-tbody"></tbody></table>'
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-spheres",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html=visual_html,
        content_html=f'<div class="cosmic-cards-grid">{cards_html}</div>{legacy_dom_safety}'
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
    legacy_zodiac_safety = '<div id="zodiac-grid" style="display:none;"></div><div id="zodiac-detail-card" style="display:none;"></div><table style="display:none;"><tbody id="panoramic-zodiac-tbody"></tbody></table>'
    return wrap_chamber_in_royal_manuscript(
        chamber_id="tab-zodiac",
        chamber_num=meta["num"],
        chamber_title=meta["title"],
        pavilion_badge=meta["pavilion"],
        quran_verse=meta["verse"],
        intro_folio=meta["intro"],
        visual_html=visual_html,
        content_html=f'<div class="cosmic-cards-grid">{cards_html}</div>{legacy_zodiac_safety}'
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

    treatises_html = """
    <!-- 4 MASTER SCHOLARLY TREATISES -->
    <div style="margin-top:40px; margin-bottom:30px;">
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
                            <li><strong>5. المساحة (The Scalar Volume $T$):</strong> المجموع التراكمي لكافة أعداد الوفق ($T = n \\times M$)، وهو يمثل الكتلة الحجمية للطاقة المستودعة.</li>
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
                            <li><strong>الفك والتحليل العكسي لأي طلسم مجهول:</strong> فحص خانة المفتاح (أقل رقم)، ثم حساب المجموع المستودع: $N = (\\text{Key} \\times n) + S + \\text{Remainder}$، ثم مطابقة الناتج بأسماء الله الحسنى والآيات القرآنية لمعرفة السر المودع وكشف ما إذا كان الوفق سليماً أم فاسداً مشوهاً.</li>
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

    <!-- Complete 7 Planetary Squares Compendium Table -->
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
        content_html=f'<div class="cosmic-cards-grid">{wafq_cards}</div>{treatises_html}'
    )


def get_deluxe_chambers_html():
    """Generates and combines all deluxe manuscript chambers."""
    return (
        generate_graph_chamber_html() +
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
        if chamber_id in ["tab-graph", "tab-spheres", "tab-zodiac", "tab-mansions", "tab-kings", "tab-letters-magic", "tab-numbers"]:
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
    nodes_json = json.dumps(VAULT_NODES_DATA, ensure_ascii=False)
    return f"""
    // ========================================================
    // KNOWLEDGE LAB — CLIENT-SIDE MASTER COSMIC DATABASE
    // ========================================================
    window.COSMIC_DATABASE = {db_json};
    window.VAULT_NODES_DATA = {nodes_json};
    console.log("🌌 [COSMIC_DATABASE] Loaded successfully with", Object.keys(window.COSMIC_DATABASE).length, "catalogs and", Object.keys(window.VAULT_NODES_DATA).length, "vault concepts.");
    """


def get_chambers_visual_js():
    """Returns the interactive Canvas drawings and live mathematical calculation scripts."""
    return """
    // ========================================================
    // KNOWLEDGE LAB — INTERACTIVE CANVAS & CALCULATION SCRIPTS
    // ========================================================

    // 0. ATLAS OF CONCEPTS (CHAMBER 01) CONTROLLER
    window.activeAtlasCategory = 'ALL';
    window.currentAtlasNodeId = 'Islamic_Cosmological_Prophetic_Master_Index';
    window.currentGraphMode = 'theory';

    // Stubs for legacy hooks
    function switchGraphMode(mode) {
        window.currentGraphMode = 'theory';
    }

    function renderAtlasNodesList() {
        const listContainer = document.getElementById('atlas-nodes-list');
        if (!listContainer || !window.VAULT_NODES_DATA) return;
        
        const searchInput = document.getElementById('atlas-search-input');
        const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
        const cat = window.activeAtlasCategory || 'ALL';
        
        const nodes = Object.values(window.VAULT_NODES_DATA);
        const filtered = nodes.filter(n => {
            const matchCat = (cat === 'ALL' || n.category === cat);
            const matchQuery = (!query || 
                (n.label && n.label.toLowerCase().includes(query)) ||
                (n.snippet && n.snippet.toLowerCase().includes(query)) ||
                (n.body_markdown && n.body_markdown.toLowerCase().includes(query)) ||
                (n.tags && n.tags.some(t => t.toLowerCase().includes(query)))
            );
            return matchCat && matchQuery;
        });

        const countBadge = document.getElementById('atlas-nodes-count-badge');
        if (countBadge) countBadge.innerText = `${filtered.length} مفهوم`;

        listContainer.innerHTML = filtered.map(n => `
            <div class="atlas-node-card ${n.id === window.currentAtlasNodeId ? 'active' : ''}" 
                 id="atlas-card-${n.id}" 
                 onclick="selectAtlasNode('${n.id}')">
                <div class="atlas-node-card-title">${n.label || n.id}</div>
                <div class="atlas-node-card-meta">
                    <span style="color:${n.color || 'var(--gold)'}; font-weight:700;">${n.category}</span>
                    <span>🔗 ${(n.connections || []).length} روابط</span>
                </div>
            </div>
        `).join('');
    }

    function selectAtlasNode(nodeId) {
        if (!window.VAULT_NODES_DATA || !window.VAULT_NODES_DATA[nodeId]) return;
        window.currentAtlasNodeId = nodeId;
        const node = window.VAULT_NODES_DATA[nodeId];

        // Highlight card
        document.querySelectorAll('.atlas-node-card').forEach(c => c.classList.remove('active'));
        const activeCard = document.getElementById('atlas-card-' + nodeId);
        if (activeCard) activeCard.classList.add('active');

        // Update Title
        const titleEl = document.getElementById('atlas-dossier-title');
        if (titleEl) titleEl.innerText = node.label || node.id;

        // Update Meta Row
        const metaEl = document.getElementById('atlas-dossier-meta');
        if (metaEl) {
            const tagsHtml = (node.tags || []).map(t => `<span class="atlas-tag-pill">#${t}</span>`).join('');
            metaEl.innerHTML = `
                <span class="atlas-tag-pill" style="background:${node.color || '#ffd700'}22; color:${node.color || '#ffd700'}; border-color:${node.color || '#ffd700'}55; font-weight:700;">
                    ${node.category}
                </span>
                <span class="atlas-tag-pill">🔗 ${(node.connections || []).length} روابط متصلة</span>
                ${tagsHtml}
            `;
        }

        // Render Full Markdown Body
        const bodyEl = document.getElementById('atlas-dossier-body');
        if (bodyEl) {
            const mdText = node.body_markdown || node.raw_content || node.snippet || 'لا يوجد شرح مفصل.';
            if (typeof marked !== 'undefined' && marked.parse) {
                bodyEl.innerHTML = marked.parse(mdText);
            } else {
                bodyEl.innerHTML = `<p style="white-space:pre-wrap;">${mdText}</p>`;
            }
        }

        // Render Connected Nodes Pills
        const connsEl = document.getElementById('atlas-dossier-connections');
        if (connsEl) {
            const conns = node.connections || [];
            if (conns.length > 0) {
                connsEl.innerHTML = conns.map(cid => {
                    const target = window.VAULT_NODES_DATA[cid];
                    const lbl = target ? (target.label || target.id) : cid;
                    return `<span class="atlas-conn-item" onclick="selectAtlasNode('${cid}')"><i class="fa-solid fa-link"></i> ${lbl}</span>`;
                }).join('');
            } else {
                connsEl.innerHTML = '<span style="font-size:0.85rem; color:#94a3b8;">هذا المفهوم يمثل أصلاً كلياً لا يتفرع عنه روابط مباشرة.</span>';
            }
        }

        // Smooth scroll to dossier on mobile
        if (window.innerWidth <= 992) {
            const dossierPanel = document.getElementById('atlas-dossier-panel');
            if (dossierPanel) {
                dossierPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }

    function filterAtlasCategory(catName) {
        window.activeAtlasCategory = catName;
        document.querySelectorAll('.atlas-cat-pill').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-cat') === catName);
        });

        const labelEl = document.getElementById('atlas-sidebar-cat-label');
        if (labelEl) {
            labelEl.innerText = catName === 'ALL' ? '🌐 كافة مفاهيم الشبكة الكونية' : catName;
        }

        renderAtlasNodesList();
    }

    function handleAtlasSearch(query) {
        renderAtlasNodesList();
    }

    function initAtlasChamber() {
        if (window.VAULT_NODES_DATA && Object.keys(window.VAULT_NODES_DATA).length > 0) {
            renderAtlasNodesList();
            const firstId = window.currentAtlasNodeId || Object.keys(window.VAULT_NODES_DATA)[0];
            selectAtlasNode(firstId);
        }
    }

    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAtlasChamber);
    } else {
        setTimeout(initAtlasChamber, 100);
    }

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
