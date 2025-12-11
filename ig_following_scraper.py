# ig_following_scraper.py
import os
import time
import re
import random
import json
import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

# ---------- CONFIG ----------
TARGET = "esedgarcia"              # Cuenta objetivo
MAX_FOLLOWING_TO_SCRAPE = 4000     # Límite de seguidos
SCROLL_PAUSE = (1.2, 2.4)
OUTPUT_FILE = "instagram_following.xlsx"
STORAGE = "auth.json"              # Sesión guardada

IG_USER = os.environ.get("IG_USER")
IG_PASS = os.environ.get("IG_PASS")
HEADLESS = os.environ.get("HEADLESS", "False").lower() in ("1", "true", "yes")

if not IG_USER or not IG_PASS:
    print("⚠ Debes exportar IG_USER e IG_PASS antes de ejecutar.")
    raise SystemExit(1)


# --------------------------------------------------------
# FUNCIÓN: SCROLL HUMANO DENTRO DEL MODAL DE FOLLOWING
# --------------------------------------------------------
def human_scroll_modal(page, scroll_box, max_items):
    users = set()
    stagnant_scrolls = 0
    last_count = 0

    while len(users) < max_items:
        elements = scroll_box.query_selector_all('a[role="link"][href*="/"] span')
        for el in elements:
            try:
                username = el.inner_text().strip()
                if username and username not in users and not username.startswith("#"):
                    users.add(username)
                    print(f" → {username}")
            except:
                continue

        scroll_box.hover()
        page.mouse.wheel(0, random.randint(500, 800))
        time.sleep(random.uniform(*SCROLL_PAUSE))

        if len(users) == last_count:
            stagnant_scrolls += 1
        else:
            stagnant_scrolls = 0

        last_count = len(users)

        if stagnant_scrolls >= 6:
            print("No se detectan más seguidos cargando.")
            break

    print(f"Total de SEGUIDOS encontrados: {len(users)}")
    return list(users)


# --------------------------------------------------------
# DETECTAR CONTENEDOR DE SCROLL DEL MODAL
# --------------------------------------------------------
def parse_following_from_modal(page, max_items):
    print("Extrayendo lista de SEGUIDOS (following)...")

    page.wait_for_selector('div[role="dialog"]', timeout=30000)

    scroll_box = None
    selectors = [
        'div[role="dialog"] div[style*="overflow-y: auto"]',
        'div[role="dialog"] div._aano',
        'div[role="dialog"] div.x9f619',
    ]

    for selector in selectors:
        el = page.query_selector(selector)
        if el:
            scroll_box = el
            print(f"✔ Contenedor detectado: {selector}")
            break

    if not scroll_box:
        print("⚠ No se detectó contenedor de scroll.")
        return []

    return human_scroll_modal(page, scroll_box, max_items)


# --------------------------------------------------------
# EXTRAER INFORMACIÓN COMPLETA DE CADA PERFIL
# --------------------------------------------------------
def get_profile_data(page, username):
    url = f"https://www.instagram.com/{username}/"
    print(f"🔎 Visitando: {url}")

    try:
        page.goto(url, timeout=30000)
    except:
        print("  → Timeout cargando perfil.")
        return None

    time.sleep(2)

    html = page.content()

    # Intento: JSON embebido
    match = re.search(r'"graphql":\s*({.*?})\s*[,}]\s*"toast_content"', html)
    if match:
        try:
            data = json.loads(match.group(1))
            user = data["user"]

            return {
                "username": user.get("username"),
                "full_name": user.get("full_name"),
                "biography": user.get("biography"),
                "followers": user.get("edge_followed_by", {}).get("count"),
                "following": user.get("edge_follow", {}).get("count"),
                "is_business": user.get("is_business_account"),
                "category": user.get("category_name"),
                "is_professional": user.get("is_professional_account"),
                "profile_pic": user.get("profile_pic_url_hd"),
                "profile_url": url
            }
        except:
            pass

    # fallback mínimo
    return {
        "username": username,
        "full_name": None,
        "biography": None,
        "followers": None,
        "following": None,
        "is_business": None,
        "category": None,
        "is_professional": None,
        "profile_pic": None,
        "profile_url": url
    }


# --------------------------------------------------------
# LOGIN O CARGA DE SESIÓN
# --------------------------------------------------------
def login_and_get_context(playwright):
    if os.path.exists(STORAGE):
        print("✔ Cargando sesión guardada…")
        browser = playwright.chromium.launch(headless=HEADLESS)
        context = browser.new_context(storage_state=STORAGE)
        return context, context.new_page()

    print("Iniciando sesión manual…")

    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context(locale="en-US")
    page = context.new_page()

    page.goto("https://www.instagram.com/accounts/login/")
    page.fill('input[name="username"]', IG_USER)
    page.fill('input[name="password"]', IG_PASS)
    page.click('button[type="submit"]')

    page.wait_for_url(re.compile("instagram.com"), timeout=60000)
    time.sleep(4)

    context.storage_state(path=STORAGE)
    print("✔ Sesión guardada")

    return context, page


# --------------------------------------------------------
# MAIN
# --------------------------------------------------------
def main():
    results = []

    with sync_playwright() as p:
        context, page = login_and_get_context(p)

        print(f"📌 Visitando perfil objetivo: {TARGET}")
        page.goto(f"https://www.instagram.com/{TARGET}/")
        time.sleep(4)

        # Abrir modal de SEGUIDOS (following)
        try:
            print("📂 Abriendo modal de SEGUIDOS...")
            following_link = page.query_selector('a[href$="/following/"]')
            following_link.click()

            page.wait_for_selector('div[role="dialog"]', timeout=10000)
            time.sleep(3)

        except Exception as e:
            print(f"❌ Error abriendo modal: {e}")
            return

        usernames = parse_following_from_modal(page, MAX_FOLLOWING_TO_SCRAPE)

        print(f"⏳ Extrayendo información de {len(usernames)} perfiles…\n")

        for i, u in enumerate(usernames, start=1):
            print(f"[{i}/{len(usernames)}] {u}")
            data = get_profile_data(page, u)
            if data:
                results.append(data)
            time.sleep(1)

        context.close()

    df = pd.DataFrame(results)
    df.to_excel(OUTPUT_FILE, index=False)

    print(f"\n📁 Datos guardados en: {OUTPUT_FILE}")
    print("🎉 Scraping completado con éxito.")


if __name__ == "__main__":
    main()
