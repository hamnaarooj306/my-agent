# niche_checker.py

# iSkills Niche Research Criteria ke mutabiq check!

# Chalana: python niche_checker.py

print("=== iSkills Niche Checker ===\n")

print("Niche type chuno:")
print("  1 = Info      (vol T1>=15000 / ROW>=30000 | DA<=25 | DR<=20 | pages<=150)")
print("  2 = APK       (vol >=30000 | DA<=25 | DR<=20 | pages<150)")
print("  3 = Affiliate (vol >=500 | DA<=25 | DR<=20 | pages<=150)")
print("  4 = Ecom      (vol >=500 | DA<=25 | DR<=20 | pages<=150)")
print("  5 = Tool      (vol T1>=15000 / ROW>=30000 | DA<=25 | DR<=20 | pages<=150)")
print("  6 = SaaS      (vol >=5000 | DA<=25 | DR<=20 | pages<=100)")
niche = input("Number likho (1-6): ").strip()

keyword = input("\nKeyword: ")
vol_raw = input("Volume (e.g. 48K): ").strip()
tier1 = input("Tier 1 countries (US/UK/CA...) ka volume ha? (haan/nahi): ").strip().lower()
da_raw = input("DA - Moz (na maloom ho to - likho): ").strip()
dr_raw = input("DR - Ahrefs (na maloom ho to - likho): ").strip()
pages_raw = input("Competitor site pages (na maloom ho to - likho): ").strip()

def parse_num(s):
    # "48K" -> 48000, "17.6K" -> 17600, "-" -> None (maloom nahi)
    s = s.strip().upper()
    if s == "-" or s == "":
        return None
    if s.endswith("K"):
        return float(s[:-1]) * 1000
    if s.endswith("M"):
        return float(s[:-1]) * 1000000
    return float(s)

def check(name, val_text, ok):
    # True = PASS, False = FAIL, None = maloom nahi (SKIP)
    if ok is None:
        return ("SKIP", name, val_text + " <- khud verify karo (Moz/Ahrefs)")
    if ok:
        return ("PASS", name, val_text)
    return ("FAIL", name, val_text)

volume = parse_num(vol_raw)
da = parse_num(da_raw)
dr = parse_num(dr_raw)
pages = parse_num(pages_raw)
is_tier1 = tier1.startswith("h")  # "haan" likha to True

def txt(v):
    return f"{v:g}" if v is not None else "-"

def le(val, limit):
    return None if val is None else val <= limit

def lt(val, limit):
    return None if val is None else val < limit

def ge(val, limit):
    return None if val is None else val >= limit

checks = []
if niche == "1":      # Info
    need = 15000 if is_tier1 else 30000
    checks = [
        check(f"Volume >= {need:g}", txt(volume), ge(volume, need)),
        check("DA <= 25", txt(da), le(da, 25)),
        check("DR <= 20", txt(dr), le(dr, 20)),
        check("Pages <= 150", txt(pages), le(pages, 150)),
    ]
elif niche == "2":    # APK
    checks = [
        check("Volume >= 30,000", txt(volume), ge(volume, 30000)),
        check("DA <= 25", txt(da), le(da, 25)),
        check("DR <= 20", txt(dr), le(dr, 20)),
        check("Pages < 150", txt(pages), lt(pages, 150)),
    ]
elif niche == "3":    # Affiliate
    checks = [
        check("Volume >= 500", txt(volume), ge(volume, 500)),
        check("DA <= 25", txt(da), le(da, 25)),
        check("DR <= 20", txt(dr), le(dr, 20)),
        check("Pages <= 150", txt(pages), le(pages, 150)),
    ]
elif niche == "4":    # Ecom / Services
    checks = [
        check("Volume >= 500", txt(volume), ge(volume, 500)),
        check("DA <= 25", txt(da), le(da, 25)),
        check("DR <= 20", txt(dr), le(dr, 20)),
        check("Pages <= 150", txt(pages), le(pages, 150)),
    ]
elif niche == "5":    # Tool
    need = 15000 if is_tier1 else 30000
    checks = [
        check(f"Volume >= {need:g}", txt(volume), ge(volume, need)),
        check("DA <= 25", txt(da), le(da, 25)),
        check("DR <= 20", txt(dr), le(dr, 20)),
        check("Pages <= 150", txt(pages), le(pages, 150)),
    ]
elif niche == "6":    # SaaS
    checks = [
        check("Volume >= 5,000", txt(volume), ge(volume, 5000)),
        check("DA <= 25", txt(da), le(da, 25)),
        check("DR <= 20", txt(dr), le(dr, 20)),
        check("Pages <= 100", txt(pages), le(pages, 100)),
    ]
else:
    print("Ghalat number! 1 se 6 tak likho.")

print(f"\n--- Result: {keyword} ---")
failed = 0
skipped = 0
for mark, name, val in checks:
    if mark == "FAIL":
        failed = failed + 1
    if mark == "SKIP":
        skipped = skipped + 1
    print(f"[{mark}] {name}  (value: {val})")

print()
if not checks:
    print("Dobara chalao aur sahi number chuno.")
elif failed == 0 and skipped == 0:
    print("VERDICT: ALL PASS — ye keyword qualify karta ha!")
elif failed == 0:
    print(f"VERDICT: PASS — lekin {skipped} cheez khud verify karo (Moz/Ahrefs).")
else:
    print(f"VERDICT: {failed} FAIL — ye keyword reject.")
    