## Development

This project uses **pnpm** as its package manager. Always use `pnpm` (e.g. `pnpm add`, `pnpm install`, `pnpm view`, `pnpm exec`) instead of `npm` or `npx`, so that `pnpm-lock.yaml` stays the single lockfile.

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Writing math

Math is rendered at build time by KaTeX (`remark-math` + `rehype-katex`). Write `$…$` for inline and `$$…$$` for display math. Inside Markdown tables, write `\lvert x \rvert` instead of `|x|`, since `|` splits table cells.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
