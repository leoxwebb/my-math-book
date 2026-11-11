## Development

This project uses **pnpm** as its package manager. Always use `pnpm` (e.g. `pnpm add`, `pnpm install`, `pnpm view`, `pnpm exec`) instead of `npm` or `npx`, so that `pnpm-lock.yaml` stays the single lockfile.

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Writing math

Math is rendered at build time by KaTeX (`remark-math` + `rehype-katex`). Write `$…$` for inline and `$$…$$` for display math. Inside Markdown tables, write `\lvert x \rvert` instead of `|x|`, since `|` splits table cells.

## Diagrams

Mermaid diagrams are rendered client-side by `astro-mermaid` and follow the light/dark theme. Write them as ` ```mermaid ` fenced code blocks in `.md`/`.mdx` pages. In `astro.config.mjs`, the `mermaid()` integration must stay listed before `starlight()`. Use Mermaid for flowcharts and dependency graphs only.

## Figures

All other figures are drawn with Python (matplotlib + numpy, managed by `uv` in `figures/`) and committed as generated SVGs; the site build never runs Python. Do not hand-write SVG.

- Each figure script lives at `figures/<chapter>/<name>.py`, defines `main()`, and saves with `common.save(fig, "<chapter>/<slug>")`, which writes `src/assets/figures/<chapter>/<slug>.svg`.
- Draw only with colors from `common.C` (the `PALETTE` in `figures/common.py`); `save()` maps them to Starlight CSS variables so figures follow the light/dark theme, and fails on any other color.
- Regenerate with `pnpm figures` (all) or `pnpm figures <filter>` (e.g. `pnpm figures prologue`), and commit the script and its SVG together. The first run downloads Noto Sans SC into `figures/fonts/` (git-ignored, checksum-verified).
- Embed in MDX with `<Figure name="<chapter>/<slug>" alt="…">caption</Figure>` from `src/components/Figure.astro`, which inlines the SVG at build time.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
