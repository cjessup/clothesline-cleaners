"""Local visual + interaction check. Not shipped."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
SHOT = ROOT / "_shots"
SHOT.mkdir(exist_ok=True)
BASE = "http://127.0.0.1:8765"
PAGES = [
    "/",
    "/locations.html",
    "/services.html",
    "/pickup.html",
    "/kiosk.html",
    "/specials.html",
    "/about.html",
    "/contact.html",
    "/404.html",
]
TELS = ["tel:+12083420538", "tel:+12088880855", "tel:+12086390876"]
PICKUP = "https://clotheslinecleanersid.smrtapp.com/customer/?page=delivery"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        for path in PAGES:
            page.goto(BASE + path, wait_until="networkidle")
            name = "home" if path == "/" else path.strip("/").replace(".html", "")
            page.screenshot(path=str(SHOT / f"desk-{name}.png"), full_page=True)
            viewport = page.locator('meta[name="viewport"]').count()
            assert viewport >= 1, path
            content = page.locator('meta[name="viewport"]').first.get_attribute("content") or ""
            assert "user-scalable=no" not in content
            assert "maximum-scale" not in content
            for tel in TELS:
                n = page.locator(f'a[href="{tel}"]').count()
                assert n >= 1, f"{path} missing {tel} (got {n})"
            pickup = page.locator(f'a[href="{PICKUP}"]').count()
            assert pickup >= 1, f"{path} missing pickup portal"
            print(f"desktop {path}: title={page.title()}")

        page.goto(BASE + "/", wait_until="networkidle")
        page.locator("[data-open-call]").first.click()
        page.wait_for_selector("#call-sheet[open]")
        page.screenshot(path=str(SHOT / "desk-call-sheet.png"))
        print("desktop call sheet open")
        page.locator('#call-sheet button.sheet-x').click()

        page.close()
        page = browser.new_page(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        )
        for path in ["/", "/locations.html", "/services.html", "/pickup.html", "/kiosk.html", "/contact.html"]:
            page.goto(BASE + path, wait_until="networkidle")
            name = "home" if path == "/" else path.strip("/").replace(".html", "")
            dock = page.locator(".dock").count()
            assert dock == 1, path
            call = page.locator(".dock [data-open-call]")
            loc = page.locator('.dock a[href="locations.html"]')
            pick = page.locator(f'.dock a[href="{PICKUP}"]')
            assert call.count() == 1
            assert loc.count() == 1
            assert pick.count() == 1
            page.screenshot(path=str(SHOT / f"mob-{name}.png"), full_page=True)
            print(f"mobile {path}: dock ok")

        page.goto(BASE + "/", wait_until="networkidle")
        page.locator(".nav-toggle").click()
        page.wait_for_selector("#site-nav.is-open")
        page.screenshot(path=str(SHOT / "mob-nav.png"))
        print("mobile nav open")
        page.locator('#site-nav a[href="locations.html"]').click()
        page.wait_for_url("**/locations.html")
        print("nav to locations ok")

        page.goto(BASE + "/", wait_until="networkidle")
        page.locator(".dock [data-open-call]").click()
        page.wait_for_selector("#call-sheet[open]")
        page.screenshot(path=str(SHOT / "mob-call-sheet.png"))
        for tel in TELS:
            assert page.locator(f'#call-sheet a[href="{tel}"]').count() == 1
        print("mobile call sheet phones ok")
        browser.close()
    print("VERIFY OK")


if __name__ == "__main__":
    main()
