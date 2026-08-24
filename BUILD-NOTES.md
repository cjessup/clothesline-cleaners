# Build notes - Clothesline Cleaners (Boise / Meridian) demo

- **Pages:** https://cjessup.github.io/clothesline-cleaners/
- **Repo:** https://github.com/cjessup/clothesline-cleaners
- **Folder:** D:\GrokBot-SiteBuilder\clothesline-cleaners
- **Grok CLI (exact):** `C:\Users\curti\.grok\bin\grok.exe --cwd "D:\GrokBot-SiteBuilder\clothesline-cleaners" -m grok-4.6 --reasoning-effort high --always-approve --output-format plain --no-alt-screen --no-plan --max-turns 80 --prompt-file "D:\GrokBot-SiteBuilder\_wsr-48-prompt.md"`
- **Pages check:** HTTP 200 at 12:45 PM PT on 2026-08-24 (`status: built`, source `main` `/`)
- **Grok run:** first attempt exit -1 at 39s (12:27 PM PT); retry exit 0, 846506 ms (~14.1 min), 12:28-12:43 PM PT on 2026-08-24

Static HTML/CSS/JS rebuild. WordPress Elementor/Divi was not migrated.

Live original: https://clotheslinecleaners.com/

The business was not contacted. Sheets and YouTrack were not edited.

## Facts used (confirmed on the live site)

- Name: Clothesline Cleaners. Family owned, 46 years, not a franchise. Boise plus Meridian.
- Stores: 244 S. Orchard St., Boise, ID 83705; 1800 S. Meridian Rd. #105, Meridian, ID 83642; 6700 N Linder Rd Ste 144, Meridian, ID 83646 (live site says public listings may show Green Leaf Cleaners)
- Phones mapped on the live contact page: Boise/Orchard/Route (208) 342-0538; Meridian Road (208) 888-0855; Linder/Green Leaf (208) 639-0876. Every display uses tel: links.
- Additional live-site numbers: shared text 208-428-6408; text club (833) 760-7053 (used only because they appear on fetched live pages)
- Hours from the live contact page: Boise and Meridian Road Mon-Thu 8am-5pm, Fri 8am-7pm, Sat 9am-2pm, Sun closed. Linder Mon-Thu 8am-5:30pm (same Fri/Sat/Sun). Locations page does not list Sunday; contact adds Sun closed -- noted, not invented.
- USPs as printed: 5% price-beat offer and terms (excluded competitors named); Clothing Care Council Seal since 2006 (only Idaho cleaner to earn it); CGCP, CED, CPD, CPW; Association of Wedding Gown Specialists; DLI; K4 solvent since 2016; secret shopper audits; free route pickup and delivery; one 24/7 kiosk at Meridian Road (text "Kiosk"); Boise 24-hour drop box; Meridian Road opened 2008; on-site seamstress Mon-Fri at Meridian Road
- SMRT portal kept EXTERNAL: https://clotheslinecleanersid.smrtapp.com/customer/ and ?page=delivery (no fake login)
- Printed homepage quotes used as text (Kristi, Ann DeAngeli, Heather Luther, Ron Meyers, John Kipper, Alicia/Boise Rescue Mission, Marilyn Devaney)
- April 29, 2026 price list and August 2026 specials as printed; Flex $0.98/lb / $17.99 min
- Email info@clotheslinecleaners.com from the live contact page

## Facts omitted / not invented

- Google review widgets / star ratings
- Clean Pass rates, ECO Bag, Refer-a-Friend, employment, blog body copy
- Restoration/patio/drapery deep copy beyond the services hub
- Staff bios (names only inside printed quotes)
- Route ZIP maps, unprinted hours, extra cities, extra phones
- Invented locations, prices, or reviews

## Issues fixed

| Live WordPress Elementor/Divi | This demo |
| --- | --- |
| Bloated WP homepage | Mobile-first independent cleaner, compact chips (no fat white bubbles) |
| Phones need real tel: links | Every store number is tel:+12083420538 / +12088880855 / +12086390876 |
| Weak conversion for multi-location + pickup | Sticky Call / Locations / Pickup; Pickup stays on live SMRT |
| SMRT mixed into WP chrome | Portal remains an external link; no fake account UI |

## Delivered pages

index.html, locations.html, services.html, pickup.html, kiosk.html, specials.html, about.html, contact.html, 404.html, .nojekyll, robots.txt, sitemap.xml, css/styles.css, js/main.js, original SVG + generated assets.

## Blockers

- First Grok CLI run died after 39s (exit -1) with no files written; identical retry succeeded.
- YouTrack WSR-48 was not opened; ranking used as given (High, WP Elementor/Divi bloat, multi-location pickup/delivery).
- Live sitemap.xml returned HTTP 500; remaining pages were taken from the live nav.
- SSH remotes fail on this machine; push used HTTPS (`https://github.com/cjessup/clothesline-cleaners.git`).
- Next WSR was not started.
