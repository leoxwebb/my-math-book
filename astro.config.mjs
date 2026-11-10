// @ts-check
import { defineConfig } from "astro/config";

import starlight from "@astrojs/starlight";
import sitemap from "@astrojs/sitemap";
import * as z from "zod";

const buildEnvSchema = z.object({
  SITE_URL: z.url({ protocol: /^https?$/ }),
});
const buildEnv = buildEnvSchema.parse(process.env);

// https://astro.build/config
export default defineConfig({
  site: buildEnv.SITE_URL,
  integrations: [
    starlight({
      title: "数学大观",
      description:
        "AI 时代的数学认知地图：不为证明，而为看见全貌；不为解题，而为读懂语言。",
      defaultLocale: "root",
      locales: {
        root: { label: "简体中文", lang: "zh-CN" },
      },
    }),
    sitemap(),
  ],
});
