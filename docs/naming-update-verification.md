# 验证记录：改名与模型名称说明（2026-09-23）

本记录只说明这次网站更新的构建、显示、发布与引用检查。新增的 2.1 节是术语与分类说明，
不涉及新的数值计算；构建和部署成功不代表页面上的推导已被验证。

## 改动

- 仓库由 `rjguo1208/claude-Holstein-model` 改名为 `rjguo1208/dispersive-Holstein`，本地目录同步改为
  `~/code/dispersive-Holstein`；GitHub Pages 地址变为 <https://rjguo1208.github.io/dispersive-Holstein/>。
- 理论笔记新增 2.1 节“名称：色散 Holstein 模型，而不是 Peierls 模型”：两种耦合的定义、动量空间顶点、
  “耦合类型 × 声子色散”分类表。页首说明、页面描述与页脚改为“色散 Holstein 模型”；页脚不再标注维护者。
- 参考文献增至 16 条，并按首次出现的顺序重新编号。
- 讨论记录新增本次提问及答复，其余条目中的仓库链接改为新地址。
- 文字表格在窄屏中改为横向滚动（`min-width: 36rem`），第一列设最小宽度，取代原来的不换行规则；
  后者会让长的行标题把其他列挤到不可读。

## 构建与站点检查

- `npm run build`：`index.html` 与 `en/index.html` 各渲染 179 个公式。
- `npm run check`：
  `OK: 4 bilingual pages; 358 LaTeX expressions with MathML; 1 TikZ figures; 0 scientific plots; translations, paired language navigation, identical numerical tables/resources, local links, anchors and fonts.`
- 推送触发的 `Check theory website` 通过（run 35916448765）；手动发布 `Deploy GitHub Pages` 通过（run 35916516336）。

## 显示与线上检查

- 本地以 `/dispersive-Holstein/` 前缀预览：桌面 1280 px 与手机 390 px 下，新分类表和第 4 节参数表显示正常；
  手机上两张表可横向滚动，各列可读。
- 线上：`/`、`/index.html`、`/log.html`、`/en/`、`/en/index.html`、`/en/log.html`、样式表、KaTeX 字体与
  `figures/model.svg` 均返回 HTTP 200；英文版 2.1 节的公式与表格在线上截图中显示正常。
- 原地址 <https://rjguo1208.github.io/claude-Holstein-model/> 返回 404。GitHub 会把旧仓库地址重定向到新仓库，
  但不会重定向 Pages 网址。

## 新增参考文献

以下条目的标题、作者、期刊、卷和页码已与 Crossref 记录核对。Zhang (2023) 与 Sous 等 (2018) 的内容描述
依据 arXiv 摘要（arXiv:2303.15303、arXiv:1805.06109）；其余条目只按标题所反映的主题引用。

| 条目 | DOI |
| --- | --- |
| Yam, Moeller, Sawatzky and Berciu, Phys. Rev. B 102, 235145 (2020) | 10.1103/PhysRevB.102.235145 |
| Sous, Chakraborty, Krems and Berciu, Phys. Rev. Lett. 121, 247001 (2018) | 10.1103/PhysRevLett.121.247001 |
| Marchand and Berciu, Phys. Rev. B 88, 060301 (2013) | 10.1103/PhysRevB.88.060301 |
| Zhang, Phys. Rev. B 108, 075156 (2023) | 10.1103/PhysRevB.108.075156 |
| Su, Schrieffer and Heeger, Phys. Rev. Lett. 42, 1698 (1979) | 10.1103/PhysRevLett.42.1698 |
| Mozafari and Stafström, J. Chem. Phys. 138, 184104 (2013) | 10.1063/1.4803691 |
