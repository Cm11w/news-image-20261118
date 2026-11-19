// news-image-20261118: "The World in One Day" — Wednesday, November 18, 2026.
// The entry image is entry.png beside this file, drawn by code in
// draw_entry.py (Python/PIL, Noto fonts); this program copies it to
// /output/entry.png. No network, deterministic: every run writes the
// same bytes. The image is 1024x1024 and under the 1 MiB gate limit,
// verified by the kit check before submission.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
