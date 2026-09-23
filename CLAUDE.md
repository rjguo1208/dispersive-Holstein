@AGENTS.md

## Local notes (Anvil)

- Node.js 22 comes from nvm and is already on `PATH`.
- The system `python3` (3.6) runs the build and checks; `module load anaconda/2025.12-py313`
  gives Python 3.13 with Pillow for screenshot cropping.
- Figures: `TECTONIC=$SCRATCH/claude-work/tools/tectonic TMPDIR=$SCRATCH/claude-work/tmp npm run figures`
  (Tectonic 0.17.0; its bundle cache is in `~/.cache/tectonic`).
- Browser check: serve a directory containing a `claude-Holstein-model -> site` symlink with
  `python3 -m http.server 8765 --bind 127.0.0.1`, then run
  `~/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell --no-sandbox --disable-gpu --hide-scrollbars --virtual-time-budget=15000 --window-size=1280,2400 --screenshot=out.png http://127.0.0.1:8765/claude-Holstein-model/`
  (use `--window-size=390,...` for mobile). Without `--virtual-time-budget` the formulas can
  appear blank because the fonts have not loaded yet.
- Working files go in `$SCRATCH/claude-work/`, not `/tmp`.
