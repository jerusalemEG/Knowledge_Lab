"""
Generate all 12 individual Zodiac notes and Universal Throne Sphere in Vault
"""

import sys
from pathlib import Path

# Force UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

VAULT_DIR = Path(__file__).resolve().parent.parent / "02_vault"
ZODIAC_DIR = VAULT_DIR / "09_Zodiac_Archetypes"
ZODIAC_DIR.mkdir(parents=True, exist_ok=True)

# 12 Signs Data
SIGNS = [
    {
        "id": "Zodiac_01_Aries",
        "name": "برج الحمل (Aries)",
        "glyph": "♈",
        "element": "نار منقلبة",
        "ruler": "المريخ ♂ (وشرفه في الشمس)",
        "organ": "الرأس والدماغ والعينان",
        "tribe": "سبط يهوذا / جاد",
        "letter": "الهاء (هـ)",
        "opposite": "Zodiac_07_Libra",
        "opposite_name": "برج الميزان",
        "era": "Age_of_Aries_Libra_Polarity",
        "desc": "الريادة النارية، صهر أسلحة الحديد، الحرب، ورمزية الكبش المقدس والشوفار في رسالة موسى والخروج من مصر."
    },
    {
        "id": "Zodiac_02_Taurus",
        "name": "برج الثور (Taurus)",
        "glyph": "♉",
        "element": "تراب ثابت",
        "ruler": "الزهرة ♀ (وشرفه في القمر)",
        "organ": "العنق والحنجرة والغدة الدرقية",
        "tribe": "سبط يوسف / إفرايم",
        "letter": "الواو (و)",
        "opposite": "Zodiac_08_Scorpio",
        "opposite_name": "برج العقرب",
        "era": "Age_of_Taurus_Scorpio_Polarity",
        "desc": "الاستقرار في وادي النيل والرافدين، عجل أبيس، البناء الحجري الضخم؛ يقابله في العقرب هوس المقابر والتحنيط والأهرامات."
    },
    {
        "id": "Zodiac_03_Gemini",
        "name": "برج الجوزاء (Gemini)",
        "glyph": "♊",
        "element": "هواء متقلب",
        "ruler": "عطارد ☿ (وشرفه في الرأس)",
        "organ": "الكتفان والذراعان والرئتان والجهاز العصبي",
        "tribe": "سبط زبولون / بنيامين",
        "letter": "الزاي (ز)",
        "opposite": "Zodiac_09_Sagittarius",
        "opposite_name": "برج القوس",
        "era": "Age_of_Gemini_Early_Writing",
        "desc": "التوأمان المؤسسان (قابيل وهابيل، جلجامش وإنكيدو)، بدايات التدوين الصوري واللغات والتجارة المفتوحة."
    },
    {
        "id": "Zodiac_04_Cancer",
        "name": "برج السرطان (Cancer)",
        "glyph": "♋",
        "element": "ماء منقلب",
        "ruler": "القمر ☽ (وشرفه في المشتري)",
        "organ": "الصدر والثديان والمعدة",
        "tribe": "سبط يساكر / رأوبين",
        "letter": "الحاء (ح)",
        "opposite": "Zodiac_10_Capricorn",
        "opposite_name": "برج الجدي",
        "era": "Age_of_Cancer_Deluge",
        "desc": "طوفان ذوبان الجليد، سفينة نوح والرحم الحافظ للبذور، ونشأة أولى القرى المائية المستقرة كأريحا."
    },
    {
        "id": "Zodiac_05_Leo",
        "name": "برج الأسد (Leo)",
        "glyph": "♌",
        "element": "نار ثابتة",
        "ruler": "الشمس ☉ (موطن السيادة والنور)",
        "organ": "القلب والعمود الفقري والشرايين",
        "tribe": "سبط يهوذا (الأسد الملكي)",
        "letter": "الطاء (ط)",
        "opposite": "Zodiac_11_Aquarius",
        "opposite_name": "برج الدلو",
        "era": "Age_of_Leo_and_Sphinx",
        "desc": "السيادة الفردية، شعلة الروح الأبدية، الذهب؛ نحت تمثال أبو الهول بالجيزة متجهاً نحو شروق شمس برجه في 10,500 ق.م."
    },
    {
        "id": "Zodiac_06_Virgo",
        "name": "برج العذراء (Virgo) — سر السيدة مريم والمسيح",
        "glyph": "♍",
        "element": "تراب متقلب",
        "ruler": "عطارد ☿ (موطنه وشرفه)",
        "organ": "البطن والأمعاء والجهاز الهضمي والتصفية",
        "tribe": "سبط أشير / نفتالي",
        "letter": "الياء (ي)",
        "opposite": "Zodiac_12_Pisces",
        "opposite_name": "برج الحوت",
        "era": "Age_of_Pisces_Virgo_Polarity",
        "desc": "برج السيدة العذراء مريم وسر ميلاد السيد المسيح: الولادة البتولية الإعجازية؛ ولادته في «بيت لحم» (بيت الخبز؛ والنجم الأسطع في العذراء هو السِّماك الأعزل Spica أي سنبلة القمح مادة الخبز)، وتكامله مع قطب الحوت المقابل (تكثير السمك والخبز والرهبنة)."
    },
    {
        "id": "Zodiac_07_Libra",
        "name": "برج الميزان (Libra)",
        "glyph": "♎",
        "element": "هواء منقلب",
        "ruler": "الزهرة ♀ (وشرفه في زحل)",
        "organ": "الكليتان وأسفل الظهر والتوازن الأسموزي",
        "tribe": "سبط دان / لاوي",
        "letter": "الكاف (ك)",
        "opposite": "Zodiac_01_Aries",
        "opposite_name": "برج الحمل",
        "era": "Age_of_Aries_Libra_Polarity",
        "desc": "كفتا العدل والميزان الأخلاقي؛ ألواح الوصايا العشر لموسى، والقوانين الصارمة للجمهوريات والدول لموازنة نار الحرب."
    },
    {
        "id": "Zodiac_08_Scorpio",
        "name": "برج العقرب (Scorpio)",
        "glyph": "♏",
        "element": "ماء ثابت",
        "ruler": "المريخ وبلوتو (وشرفه في أورانوس)",
        "organ": "الأعضاء التناسلية وجهاز الإخراج والتجدد الخلوي",
        "tribe": "سبط دان / شمعون",
        "letter": "اللام (ل)",
        "opposite": "Zodiac_02_Taurus",
        "opposite_name": "برج الثور",
        "era": "Age_of_Taurus_Scorpio_Polarity",
        "desc": "عالم الموت والبعث والتحول الخيميائي وطائر الفينيق؛ كتاب الموتى في مصر والتحنيط وسحر العوالم السفلية."
    },
    {
        "id": "Zodiac_09_Sagittarius",
        "name": "برج القوس (Sagittarius)",
        "glyph": "♐",
        "element": "نار متقلبة",
        "ruler": "المشتري ♃ (وشرفه في الذنب)",
        "organ": "الفخذان والوركان والعصب الوركي",
        "tribe": "سبط نفتالي / منسى",
        "letter": "الميم (م)",
        "opposite": "Zodiac_03_Gemini",
        "opposite_name": "برج الجوزاء",
        "era": "Age_of_Gemini_Early_Writing",
        "desc": "القنطور والسهم المنطلق نحو النجوم؛ الفلسفة الكونية الكبرى، استكشاف الآفاق، التعليم العالي، والحكمة النبوية."
    },
    {
        "id": "Zodiac_10_Capricorn",
        "name": "برج الجدي (Capricorn)",
        "glyph": "♑",
        "element": "تراب منقلب",
        "ruler": "زحل ♄ (وشرفه في المريخ)",
        "organ": "الركبتان والهيكل العظمي والجلد والمفاصل",
        "tribe": "سبط بنيامين / زبولون",
        "letter": "النون (ن)",
        "opposite": "Zodiac_04_Cancer",
        "opposite_name": "برج السرطان",
        "era": "Age_of_Cancer_Deluge",
        "desc": "الماعز الجبلي الصاعد نحو قمة الهرم؛ الهياكل الصلبة، صرامة الزمان والحدود والمؤسسات والتحمل الصخري الشديد."
    },
    {
        "id": "Zodiac_11_Aquarius",
        "name": "برج الدلو (Aquarius)",
        "glyph": "♒",
        "element": "هواء ثابت",
        "ruler": "زحل وأورانوس (وشرفه في نبتون)",
        "organ": "الساقان والكاحلان والدورة الدموية والجهاز الكهربائي",
        "tribe": "سبط رأوبين / دان",
        "letter": "السين (س)",
        "opposite": "Zodiac_05_Leo",
        "opposite_name": "برج الأسد",
        "era": "Age_of_Aquarius_Leo_Polarity",
        "desc": "سكب ماء المعرفة للبشرية جمعاء دون وسيط كهنوتي؛ عصر الذكاء الاصطناعي، الاتصال الشبكي، اللامركزية، والوعي الكوني."
    },
    {
        "id": "Zodiac_12_Pisces",
        "name": "برج الحوت (Pisces) — رسالة السيد المسيح",
        "glyph": "♓",
        "element": "ماء متقلب",
        "ruler": "المشتري ونبتون (وشرفه في الزهرة)",
        "organ": "القدمان وجهاز المناعة اللمفاوي",
        "tribe": "سبط شمعون / يوسف",
        "letter": "العين (ع)",
        "opposite": "Zodiac_06_Virgo",
        "opposite_name": "برج العذراء",
        "era": "Age_of_Pisces_Virgo_Polarity",
        "desc": "محور رسالة السيد المسيح والمحبة المطلقة: السمكتان السابحتان في محيط الروحانية، اتخاذ السمكة شعاراً، دعوة صيادي الناس، والتكامل مع قطب العذراء المقابل (تكثير السمك والخبز والرهبنة)."
    }
]

for s in SIGNS:
    filepath = ZODIAC_DIR / f"{s['id']}.md"
    content = f"""---
title: "{s['name']}"
type: zodiac_sign
glyph: "{s['glyph']}"
element: "{s['element']}"
ruler: "{s['ruler']}"
organ: "{s['organ']}"
tribe: "{s['tribe']}"
letter: "{s['letter']}"
tags:
  - zodiac
  - astrology
  - melothesia
  - {s['id'].lower()}
connections:
  - "[[{s['opposite']}]]"
  - "[[{s['era']}]]"
  - "[[Melothesia_Body_Cosmos_Mapping]]"
  - "[[Prophetic_Spheres_Comparative_Master_Matrix]]"
---

# {s['name']} {s['glyph']}

> **البيانات الكوزمولوجية:**
> - **العنصر والطبيعة:** {s['element']}
> - **الكوكب الحاكم والشرف:** {s['ruler']}
> - **القطب المقابل (180°):** [[{s['opposite']}|{s['opposite_name']}]]
> - **العضو الجسدي (الميلوثيسيا):** [[Melothesia_Body_Cosmos_Mapping|{s['organ']}]]
> - **السبط الكابالي:** {s['tribe']}
> - **حرف التكوين الأبجدي:** {s['letter']}

---

## 1. الدلالة الرمزية والرسالية الكبرى
{s['desc']}

---

## 2. الارتباط بالعصور والنبوات
- يرتبط هذا البرج مباشرة بـ [[{s['era']}]]، وبالمصفوفة الكبرى: [[Prophetic_Spheres_Comparative_Master_Matrix]].
- يتكامل مع القطب المقابل بزاوية 180 درجة: [[{s['opposite']}|{s['opposite_name']}]].
"""
    filepath.write_text(content, encoding="utf-8")
    print(f"[✔] تم إنشاء نوتة: {s['id']}")

# Also create Muhammad Universal Throne Sphere note in 03_Esoteric_Systems
throne_file = VAULT_DIR / "03_Esoteric_Systems" / "Universal_Throne_Sphere_Muhammad.md"
throne_content = """---
title: فلك العرش الأطلس المحيط — النبي الخاتم محمد ﷺ
type: master_sphere
tags:
  - muhammad_universal
  - throne_sphere
  - macrocosmic_pole
  - ascension
  - sufism
  - perennial_philosophy
created: 2026-10-10
connections:
  - "[[Universal_Esoteric_Map_of_Consciousness]]"
  - "[[Prophetic_Spheres_Comparative_Master_Matrix]]"
  - "[[Ibn_Arabi_Fusus_al_Hikam_Cosmology]]"
---

# فلك العرش الأطلس المحيط (الحقيقة الجامعة وخاتم النبوة)

> **"مقام قاب قوسين أو أدنى" — سدرة المنتهى وما وراء السماوات السبع.**

## 1. الموقع الكوزمولوجي المحيط
في كوزمولوجيا الشيخ الأكبر محيي الدين ابن عربي (فصوص الحكم - فص حكمة فردية في كلمة محمدية) وإخوان الصفا:
- لا يقتصر مقام النبي الخاتم محمد صلى الله عليه وسلم على فلك كوكبي جزئي من السبعة.
- مقامه هو **"فلك العرش الأطلس المحيط الأعظم"**؛ وهو الفلك التاسع غير المكوكب الذي يحيط بجميع الأفلاك السبعة والبروج الاثني عشر ويدير حركاتها بالفيض الكلي.
- في رحلة المعراج، جاوز النبي الأنبياء في سماواتهم (من آدم في فلك القمر، حتى إبراهيم في فلك زحل عند البيت المعمور) ثم ارتقى فوق زحل مخترقاً الحجب إلى سدرة المنتهى.

## 2. جمع دائرة البروج
- يمثل النبي الخاتم نقطة الختام والمركز لجميع البروج الاثني عشر؛ حيث توحدت في رسالته كمالات جميع الشرائع السابقة ممتدة إلى قيام الساعة (رحمة للعالمين).

## الروابط المتصلة:
- [[Universal_Esoteric_Map_of_Consciousness]]
- [[Prophetic_Spheres_Comparative_Master_Matrix]]
- [[Ibn_Arabi_Fusus_al_Hikam_Cosmology]]
"""
throne_file.write_text(throne_content, encoding="utf-8")
print("[✔] تم إنشاء نوتة فلك العرش المحيط للنبي محمد ﷺ.")
