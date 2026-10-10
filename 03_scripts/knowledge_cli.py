"""
Knowledge Lab - Central Command Line Hub
Provides one-click management for Knowledge Vault, PDF pipeline,
and graph visualization.
"""

import sys
import os
import webbrowser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = BASE_DIR / "03_scripts"
VIEWER_HTML = BASE_DIR / "knowledge_graph_viewer.html"

# Add scripts directory to path
sys.path.insert(0, str(SCRIPTS_DIR))
import graph_builder
import pdf_processor


def print_banner():
    print("=" * 65)
    print("           🌌 KNOWLEDGE LAB - بيئة ربط المعرفة الكبرى 🌌")
    print("=" * 65)
    print(" [1] 🌐 تحديث شبكة المعرفة وفتح خريطة العلاقات في المتصفح")
    print(" [2] 📚 سحب ومعالجة الكتب والمخطوطات من (01_raw_pdf)")
    print(" [3] 🔍 البحث السريع في المفاهيم والنوتس")
    print(" [4] 📊 إحصائيات شبكة المعرفة الحالية")
    print(" [5] 🚪 خروج")
    print("=" * 65)


def show_stats():
    nodes, links = graph_builder.scan_vault()
    print("\n--- [إحصائيات البيئة الحالية] ---")
    print(f"• إجمالي الكيانات والمفاهيم (Nodes): {len(nodes)}")
    print(f"• إجمالي الروابط الشبكية (Wikilinks): {len(links)}")
    
    types_count = {}
    for n in nodes.values():
        t = n.get("type", "other")
        types_count[t] = types_count.get(t, 0) + 1
        
    print("• توزيع الكيانات:")
    for t, cnt in types_count.items():
        print(f"   - {t}: {cnt}")
    print("---------------------------------\n")


def search_vault():
    query = input("\n[?] اكتب كلمة البحث (مفهوم، عالم، عصر، كوكب): ").strip().lower()
    if not query:
        return
    nodes, _ = graph_builder.scan_vault()
    found = 0
    print(f"\n--- نتائج البحث عن: '{query}' ---")
    for nid, node in nodes.items():
        match = (query in node["label"].lower() or 
                 query in nid.lower() or 
                 any(query in t.lower() for t in node.get("tags", [])) or
                 query in node.get("snippet", "").lower())
        if match:
            found += 1
            print(f"\n★ [{node['label']}] ({node['type']})")
            print(f"  الملف: {node['relpath']}")
            if node.get("snippet"):
                print(f"  نبذة: {node['snippet'][:120]}...")
            if node.get("connections"):
                print(f"  مرتبط بـ: {', '.join(node['connections'][:4])}")
                
    if found == 0:
        print("  لم يتم العثور على نتائج.")
    print(f"\n[+] إجمالي النتائج: {found}\n")


def main():
    while True:
        print_banner()
        choice = input("[+] اختر رقم العملية (1-5): ").strip()
        
        if choice == "1":
            print("\n[+] جارٍ قراءة الـ Vault وبناء الجراف...")
            nodes, links = graph_builder.scan_vault()
            graph_builder.generate_html_viewer(nodes, links)
            print("[✔] تم توليد ملف HTML. جارٍ الفتح في المتصفح...")
            webbrowser.open(VIEWER_HTML.as_uri())
            
        elif choice == "2":
            pdf_processor.process_all_raw_pdfs()
            
        elif choice == "3":
            search_vault()
            
        elif choice == "4":
            show_stats()
            
        elif choice == "5":
            print("\n[✔] وداعاً، استمتع بربط المعرفة في Obsidian!")
            break
        else:
            print("[!] اختيار غير صحيح، حاول ثانية.")


if __name__ == "__main__":
    main()
