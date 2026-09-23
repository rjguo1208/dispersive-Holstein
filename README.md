# 孤立缺陷与 Holstein 模型（Claude 研究笔记）

网站：<https://rjguo1208.github.io/claude-Holstein-model/> · [English](https://rjguo1208.github.io/claude-Holstein-model/en/)

这是 Claude 为本项目维护的中英文网站，用来存放项目内容，也是与 Claude 交互的地方。结构和规则沿用 Codex 维护的 [Holstein-model](https://github.com/rjguo1208/Holstein-model)：LaTeX 公式在构建时预先排版，TikZ 图编译成 PDF 和 SVG，中英文两个版本同步维护，经 GitHub Actions 发布到 GitHub Pages。

This is the bilingual website Claude maintains for this project: it stores the project
content and is the place to interact with Claude. It follows the structure and rules of
the Codex-maintained [Holstein-model](https://github.com/rjguo1208/Holstein-model) site.

## 当前内容

- [理论笔记](https://rjguo1208.github.io/claude-Holstein-model/)：孤立缺陷的简易模型，研究缺陷如何改变局域电子态、局域声子态和电声耦合。只讨论基态与静态响应，不涉及缺陷激发态（不使用 Huang–Rhys 模型）。这是理论设计笔记，尚未实现或数值验证。
- [讨论记录](https://rjguo1208.github.io/claude-Holstein-model/log.html)：每次提问、回答所在页面和当前状态，以及交互方式。

## 与 Claude 交互 / Interaction

1. 在 Claude Code 中提问。需要公式或图的讲解会写到本站，终端里给出链接和简短摘要。
2. 对某页或某节有疑问，可以用 [问题或反馈模板](https://github.com/rjguo1208/claude-Holstein-model/issues/new/choose)提交 issue。请 Claude 查看网站反馈时，它会读取 issue、在 issue 中回复，并把修改写进页面。
3. 每次更新都同时维护中文和英文，并在讨论记录中追加一条。

Ask in Claude Code, or open an issue with the question template; Claude replies in the
issue and records page changes in the discussion log.

## 本地预览

已生成的页面与全部资源保存在 `site/`：

```bash
cd site
python3 -m http.server 8000 --bind 127.0.0.1
```

打开 <http://localhost:8000>。

## 修改正文或公式

需要 Node.js 22 和 Python 3。修改 `src/*.html` 中的正文和 LaTeX，或修改 `src/style.css`，然后运行：

```bash
npm ci --ignore-scripts
npm run build
npm run check
```

使用 `\(...\)` 写行内公式，`\[...\]` 写独立公式。构建采用固定版本的 [KaTeX](https://katex.org/docs/api.html)（0.18.7，严格模式），遇到不支持的公式语法即报错。数学表达式中的小于号使用 `\lt`，不使用 HTML 实体。`site/*.html`、`site/en/*.html` 和 `site/assets/` 均为已提交的发布产物，阅读时无需 JavaScript、外部字体或 CDN。

## 中英文同步维护 / Bilingual updates

每次更新网站都必须同时更新中文和英文；这项要求记录在 [AGENTS.md](AGENTS.md)。共同结构与中文内容保存在 `src/*.html`，英文保存在 `src/locales/en.json`，键是合并空白后的中文原文。查看当前所有待翻译文本：

```bash
python3 scripts/localize.py --extract
```

构建会拒绝缺失、空白、仍含中文或已过时的翻译，并检查两种语言的数学表达式完全一致。`npm run check` 检查所有页面的双语配对、当前语言、页面目录、本地链接、公式、锚点、表格数值和共用资源。

For every update, edit the Chinese sources and their English translations together.
The build fails on missing or obsolete translations and on changed mathematics.

## 修改示意图

`site/figures/` 中的 `.tex` 均可独立编译，使用标准 LaTeX、AMS Math 和 TikZ。每幅图在网页中同时提供 SVG、PDF 和 LaTeX 源文件。安装 [Tectonic](https://tectonic-typesetting.github.io/en-US/install.html) 和 Poppler（提供 `pdftocairo`）后：

```bash
npm run figures
npm run check
```

如果 Tectonic 不在 PATH，可设置 `TECTONIC=/path/to/tectonic`。构建脚本把 LaTeX 源文件的 SHA-256 写入 SVG；站点检查会拒绝源文件已改变但图未重新编译的情况，也会拒绝没有被任何页面使用的图。

## 发布

GitHub Pages 的发布来源为 GitHub Actions。推送到 `main` 会运行检查；发布由 `Deploy GitHub Pages` 工作流手动触发：

```bash
gh workflow run pages.yml --ref main -R rjguo1208/claude-Holstein-model
```

检查和发布流程都会重新渲染公式、验证本地链接与图文件，并确认发布产物与源文件一致。工作流只上传 `site/`，所有资源路径兼容 `/claude-Holstein-model/` 子路径。

## 文件结构

```text
src/index.html                理论笔记（中文源与 LaTeX 公式）
src/log.html                  讨论记录与交互方式
src/locales/en.json           全站英文翻译；键为中文原文
src/style.css                 简洁排版与打印样式
site/index.html, site/log.html 预先渲染的中文页面
site/en/                      英文页面
site/assets/katex/            数学样式、字体与许可证
site/figures/                 示意图的 LaTeX、PDF 与 SVG
scripts/build.mjs             公式渲染、双语页面与静态资源
scripts/localize.py           英文翻译、共用链接与公式一致性检查
scripts/build_figures.py      TikZ → PDF → SVG
scripts/check_site.py         数学、链接、字体、双语与图来源检查
docs/                         每次发布的验证记录
.github/workflows/            自动检查及 Pages 发布
.github/ISSUE_TEMPLATE/       问题或反馈模板
AGENTS.md                     维护规则（CLAUDE.md 引用它）
```

KaTeX 的许可证随发布资源保留在 `site/assets/katex/LICENSE`。本版的构建、浏览器与参考文献检查见 [验证记录](docs/verification.md)。
