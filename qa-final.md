# QA — Final image, news-image-20261118

Checked 19 Nov 2026, ~08:55 WIB, by reading the rendered image directly
(full size, 300px downscale, and one crop per block). Image: `entry.png`
(sha256 `c649bb55347da433c8f6cf69d6bea75c88c257d58be0776871fbdccae3a0def5`).

## Format — PASS
- PNG, 1024×1024, 143,535 bytes (limit 1,048,576). Valid PNG.
- `main.ts` run twice → byte-identical output (same sha256 all three
  copies: draw output + 2× main.ts output). `main.ts` unchanged from
  the draft (it only copies entry.png).
- Kit check NOT re-run in this phase: format facts above are unchanged
  in kind from the draft (which passed 4/5 checks; transcripts_present
  failed as expected — the transcript bundle is made by the parent at
  submit time). Re-run the kit check before submission.

## Visual — PASS, no fixes needed
- Date "Wednesday, November 18, 2026" prominent at top, correct weekday.
- All 5 blocks inside their cards; no text overflow, no overlap, no
  garbled or clipped text in the final render (verified per-block crops).
- New bar-chart icon (Anthropic block, code-drawn) renders cleanly and
  does not collide with the headline or tag. The old sun icon function
  is now unused but left in `draw_entry.py` (harmless).
- 300px downscale: date fully readable, all 5 headlines readable, tags
  readable, body text small but the structure and every story's gist
  remain clear — same standard as the draft QA.
- No illustration element was used: typographic design with five small
  geometric icons drawn in code (globe, bars, chip, spiral) — nothing
  copied, no photos, no characters, no third-party artwork.
- Fonts: Noto Serif/Sans (OFL), drawn by code in `draw_entry.py`.

## Claims vs research — PASS
Every sentence in the image traces to `research-19nov.md`:
- Lead: 5 tankers destroyed (CENTCOM claim, attributed); IRGC twice
  targeted U.S. warships; "Iran said it hit 10 ships" — now attributed
  (was "Iran hit 10 ships" in the draft; every 18 Nov source frames
  the 10-ship attack as an IRGC claim); oil above $100.
- APEC: Trump–Marcos meeting 18 Nov Manila; trilateral "confirmed for
  Thursday" + "first-ever" — upgraded from "expected" on the strength
  of the Chinese Foreign Ministry confirmation (16 Nov, via Hindu
  Business Line / SCMP) plus White House and Kremlin confirmations.
  The meeting itself is 19 Nov and is not claimed to have happened.
- Anthropic (NEW block): $83/share, above the $70–$78 range, $81bn
  sale, "the largest on record" — Reuters/Bloomberg/CNBC + Anthropic's
  own announcement 18 Nov; $81.34bn gross on 980m shares (FinanceFeeds,
  AlphaSignal), surpassing SpaceX's June deal (Financial News, citing
  CNBC). Conflicting valuation figures ($1.5tn vs ~$1.10tn) were NOT
  used. Replaces the EU permits deal (verified but cut — see below).
- Nvidia: revenue $115.8bn (+103%), shares fell 2.9% Wednesday to
  $150.96, fifth straight loss — 18 Nov close verified via Finnhub
  quote snapshot, AP, CNBC, Motley Fool.
- Akvan: turned severe Wednesday (IMD press release No. 4, 5:30 am
  18 Nov); landfall "forecast for Friday at 90–100 km/h" — per IMD
  bulletin No. 27 (2:30 am 19 Nov), which supersedes the draft's
  bulletin No. 20 (very severe, 120–130, Nellore–Visakhapatnam).
  Still labelled a forecast.
- Footer sources updated: European Council out, Bloomberg + Anthropic in;
  one line, fits.

## Weakest story in the final image
**Cyclone Akvan.** It is the only block whose core event has not
happened yet (landfall is a Friday forecast), and the forecast was
downgraded overnight (very severe → severe, 120–130 → 90–100 km/h).
Its 18 Nov news value is real — the storm reached severe status on
Wednesday and the forecast itself moved — but it is the thinnest of
the five. The next-weakest is the lead's second sentence, which rests
on an IRGC claim (now honestly attributed). The EU deal, Ebola and
Peltola are documented as verified-but-cut in `research-19nov.md`;
Ebola and Peltola were excluded by the dating rule (first reported
17 Nov), not by importance.

## Status — FINAL, ready to show the user
- No submission made, no repo created on GitHub, no bundle — all
  forbidden in this phase (parent handles those at submit time).
- Local git repo: this QA + the final draw script, image and refresh
  research are committed on top of the draft commits.
- Deadline: 20 Nov 2026 07:00 WIB. Nothing in the image depends on
  19 Nov events, so no further refresh is needed before the parent
  shows it to the user.
