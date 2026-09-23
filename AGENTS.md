# Website maintenance

This repository is the project website that Claude maintains for the
isolated-defect / Holstein-model project. It follows the structure and rules of
the Codex-maintained `rjguo1208/Holstein-model` site.

## Bilingual pages (user requirement)

The user requires Chinese and English versions to be updated together.

- Keep the Chinese routes at the site root and their English equivalents under
  `en/`. Every website page needs both versions and the top-right language switch.
- Edit shared content and markup in `src/*.html`, and update all affected English
  translations in `src/locales/en.json` in the same change. Translate headings,
  body text, captions, lists, link text, metadata, alternative text and
  explanatory labels inside equations. Preserve the full scientific meaning,
  qualifications and status in both languages.
- Translation keys are the Chinese source strings with whitespace normalized.
  `python3 scripts/localize.py --extract` lists the current keys. Missing, empty,
  obsolete or untranslated entries fail the build. Do not bypass these checks or
  add Chinese fallback text to make an English page build.
- Both languages share equations, anchors, figures and downloadable data. Keep
  figure labels in English or mathematical notation so the same assets serve both
  versions; translate captions and alternative text through the catalog.

## Content and interaction

- Explanations for this project that need equations or figures are published on
  this site. Add or update a page, then add an entry at the top of the discussion
  log (`src/log.html`): the date, the question as the user asked it, where the
  answer lives, and its status. A new page must be added to the `site-nav` list
  of every page.
- Keep the status honest. Theory stays "design notes" until it has been checked;
  do not mark calculations or derivations as validated merely because page
  generation, translation or deployment succeeded.
- Cite only references whose metadata has been checked (for example against
  Crossref). Never publish references written from memory.
- Feedback arrives as GitHub issues
  (`gh issue list -R rjguo1208/claude-Holstein-model`). When asked to check it,
  reply in the issue, make and log the page changes, and close the issue only
  once it has been addressed.

## Build, check and publish

- Figures are standalone LaTeX/TikZ files in `site/figures/*.tex`.
  `npm run figures` (Tectonic + Poppler `pdftocairo`) writes the PDF and an SVG
  stamped with the source hash; `npm run check` rejects stale figures.
- Run `npm run build` and `npm run check`, and commit the regenerated `site/`
  pages and assets together with the source changes.
- Check language switching and navigation on desktop and mobile, including the
  GitHub Pages `/claude-Holstein-model/` prefix. KaTeX fonts use
  `font-display: block`, so screenshots must wait for fonts to load.
- Publish both language versions together: push to `main`, then run
  `gh workflow run pages.yml --ref main -R rjguo1208/claude-Holstein-model`.
- Commit messages carry no `Co-Authored-By` trailer.
