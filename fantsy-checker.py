# fantasy_checker.py

# Hamna ka tool — sirf "fantasy trade calculator" ke liye!

# Chalana:  python fantasy_checker.py   (kuch type nahi karna parega)

print("=== Fantasy Trade Calculator — Niche Check ===\n")

# ---- Sheet ka data (pehle se bhara hua) ----

keyword     = "fantasy trade calculator"
volume      = 48000        # 48K, US
kd          = 0
competitor  = "idptradecalculator.com"
da          = 0.7
dr          = None         # sheet me "-" tha = maloom nahi
pages       = 17600        # 17.6K
competition = "Low"        # 2 weak sites

print("Keyword:    ", keyword)
print("Volume:     ", f"{volume:g} /mo (US)")
print("KD:         ", kd)
print("Competitor: ", competitor)
print("DA:         ", da)
print("DR:         ", "- (maloom nahi, Moz/Ahrefs se check karo)")
print("Pages:      ", f"{pages:g}")
print("Competition:", competition, "(2 weak sites)")

def show(title, checks):
    # checks: [(naam, True/False/None), ...]
    # True = PASS, False = FAIL, None = maloom nahi (SKIP)
    print(f"\n--- {title} ---")
    fails = 0
    skips = 0
    for name, ok in checks:
        if ok is None:
            mark = "SKIP"
            skips = skips + 1
        elif ok:
            mark = "PASS"
        else:
            mark = "FAIL"
            fails = fails + 1
        print(f"[{mark}] {name}")
    if fails == 0 and skips == 0:
        print("=> ALL PASS — qualify!")
    elif fails == 0:
        print(f"=> PASS, lekin {skips} cheez khud verify karo.")
    else:
        print(f"=> {fails} FAIL — reject.")

show("APK criteria (vol>=30k, DA<=25, DR<=20, pages<150)", [
    ("Volume >= 30,000", volume >= 30000),
    ("DA <= 25", da <= 25),
    ("DR <= 20", None if dr is None else dr <= 20),
    ("Pages < 150", pages < 150),
])

show("SaaS criteria (vol>=5k, pages<=100)", [
    ("Volume >= 5,000", volume >= 5000),
    ("Pages <= 100", pages <= 100),
])

show("Ecom criteria (vol>=500, pages<=150)", [
    ("Volume >= 500", volume >= 500),
    ("Pages <= 150", pages <= 150),
])

print("\nHo gaya! 🎉")