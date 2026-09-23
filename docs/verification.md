# 验证记录：首版网站（2026-09-23）

> 仓库已于 2026-09-23 由 `claude-Holstein-model` 改名为 `dispersive-Holstein`。本记录描述首版，保留当时的名称与网址。

本记录只说明网站的构建、显示与引用检查。页面上的物理内容是理论设计笔记，
没有经过数值验证；构建和部署成功不代表其中的推导或结论已被验证。

## 构建与站点检查

- `npm run build`：KaTeX 0.18.7，`output: 'htmlAndMathml'`，`strict: 'error'`。
  `index.html` 与 `en/index.html` 各渲染 170 个公式；`log.html` 与 `en/log.html` 没有公式。
- `npm run check` 输出：
  `OK: 4 bilingual pages; 340 LaTeX expressions with MathML; 1 TikZ figures; 0 scientific plots; translations, paired language navigation, identical numerical tables/resources, local links, anchors and fonts.`
- 相对 Codex 版本，`scripts/check_site.py` 做了两处通用化：允许没有公式的页面（有公式时仍要求全部渲染并带 MathML）；
  把“首页恰好 4 幅图”改为“每幅 TikZ 图都必须出现在某个页面上”。其余检查保持不变。
- 系统 Python 3.6.8 与 Python 3.13.9 都能运行构建和检查。

## 示意图

- `site/figures/model.tex` 用 Tectonic 0.17.0 编译，`pdftocairo` 20.11.0 转换为 SVG；SVG 带源文件 SHA-256，
  有 `viewBox`，不含位图或脚本。
- 图中只用数学符号标注，两种语言共用；图注与替代文本经翻译目录提供英文。

## 浏览器显示

用 Chrome for Testing 153（headless shell），在本地以 `/claude-Holstein-model/` 前缀提供 `site/`：

- 桌面 1280 px：左侧页面目录固定，右上角语言切换，当前页与当前语言有标记；公式、表格、示意图显示正常。
- 手机 390 px：页面目录在页首；长公式和示意图可横向滚动，示意图最小宽度 520 px，缺陷格点在首屏内可见。
- 讨论记录在手机上改用逐条列表，不再使用四列表格。
- KaTeX 字体使用 `font-display: block`。截图若不等待字体加载，公式会显示为空白；
  加 `--virtual-time-budget=15000` 后中英文页面均正常。这不影响真实浏览器，只影响截图时机。

## 发布

- 仓库 `rjguo1208/claude-Holstein-model`（公开），GitHub Pages 发布来源为 GitHub Actions（`build_type: workflow`），与 Codex 的 Holstein-model 相同。
- 推送触发的 `Check theory website` 通过（run 35914097810），其中包括重新构建后 `git diff --exit-code -- site/`。
- 手动触发的 `Deploy GitHub Pages` 通过（run 35914151600）。
- 线上检查：`/`、`/index.html`、`/log.html`、`/en/`、`/en/index.html`、`/en/log.html`、样式表、KaTeX 字体、
  `figures/model.svg|pdf|tex` 均返回 HTTP 200；中英文标题正确。
- 线上截图（桌面英文、手机中文）中公式、示意图、页面目录与语言切换显示正常。远程页面截图需用
  `--timeout=20000` 等待真实时间；`--virtual-time-budget` 在网络请求完成前就会结束，得到空白图。

## 参考文献

以下条目的标题、作者、期刊、卷和页码已与 Crossref 记录核对：

| 条目 | DOI |
| --- | --- |
| Holstein, Ann. Phys. 8, 325 (1959) | 10.1016/0003-4916(59)90002-8 |
| Montroll and Potts, Phys. Rev. 100, 525 (1955) | 10.1103/PhysRev.100.525 |
| Anderson, Phys. Rev. 124, 41 (1961) | 10.1103/PhysRev.124.41 |
| Hewson and Meyer, J. Phys.: Condens. Matter 14, 427 (2002) | 10.1088/0953-8984/14/3/312 |
| Koster and Slater, Phys. Rev. 96, 1208 (1954) | 10.1103/PhysRev.96.1208 |
| Ebrahimnejad and Berciu, Phys. Rev. B 85, 165117 (2012) | 10.1103/PhysRevB.85.165117 |
| Shinozuka and Toyozawa, J. Phys. Soc. Jpn. 46, 505 (1979) | 10.1143/JPSJ.46.505 |
| Dunlap, Kenkre and Reineker, Phys. Rev. B 47, 14842 (1993) | 10.1103/PhysRevB.47.14842 |
| Anderson, Phys. Rev. Lett. 34, 953 (1975) | 10.1103/PhysRevLett.34.953 |

Lang and Firsov, Sov. Phys. JETP 16, 1301 (1963) 没有 DOI，按通行引用格式列出，未经 Crossref 核对。
页面只引用这些文献的标题所反映的主题，没有转述未核对的具体结论。

## 物理内容的状态

- 页面中的公式（Koster–Slater 束缚态权重、$\chi_{00}$、耦合谱与弛豫能、Hellmann–Feynman 关系、
  一维经典晶格下纯耦合缺陷的阈值 $E_{p,d}=t$ 等）是解析推导，尚未用数值计算核对。
- “中间区电子引起的软化和同位素效应最大”是基于推理的预计，页面上已如此标注。
