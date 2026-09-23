# 验证记录：项目计划页（2026-09-23）

本记录只说明计划页发布时的构建、显示与引用检查。计划本身尚未开始实施，页面上没有任何数值结果。

## 改动

- 新增 `src/plan.html`（中文源）及其英文翻译：目标与问题、单位与两种精确数值表示、七个阶段（阶段 6 可选）、
  验证清单 V1–V9、参数扫描、代码与数据组织、风险与对策、三个决策点。
- 三个页面的页面目录都加入“项目计划”；理论笔记第 8 节末尾链接到计划页。
- 理论笔记第 5 节的声子模式指标由 $\lambda$ 改为 $\nu$，避免与耦合常数 $\lambda$ 混淆。
- 讨论记录新增本次提问。按用户要求，不再使用 9 月 6 日的笔记。

## 数值基准的来源

计划中的 V2 基准 $E(0)=-2.4696847$、$Z_0=0.738435$、$m^*/m_0=1.35063$（$t=\omega_0=g=1$，不含零点能）
取自已有 VED 计算的结果文件，而不是凭记忆填写。

## 构建与站点检查

- `npm run build`：`plan.html` 与 `en/plan.html` 各 176 个公式；全站 710 个。
- `npm run check`：`OK: 6 bilingual pages; 710 LaTeX expressions with MathML; ...`，包括两种语言的表格数字一致。
- 推送触发的 `Check theory website` 通过（run 35919276831）；手动发布 `Deploy GitHub Pages` 通过（run 35919325415）。

## 显示与线上检查

- 本地以 `/dispersive-Holstein/` 前缀预览：中文桌面版与英文手机版显示正常。
- 线上 `plan.html`、`en/plan.html` 及其余页面均返回 HTTP 200；英文计划页的线上截图中公式正常。
- 截图说明：headless Chromium 的 `--timeout` 到时会停止加载；20 秒时字体有时尚未下载完，公式显示为空白，
  改为 60 秒后正常。字体文件本身的下载时间约 0.07 秒，线上页面没有问题。

## 新增参考文献

以下条目的标题、作者、期刊、卷和页码已与 Crossref 记录核对：

| 条目 | DOI |
| --- | --- |
| Jeckelmann and White, Phys. Rev. B 57, 6376 (1998) | 10.1103/PhysRevB.57.6376 |
| Hauschild and Pollmann, SciPost Phys. Lect. Notes 5 (2018) | 10.21468/SciPostPhysLectNotes.5 |
| Fishman, White and Stoudenmire, SciPost Phys. Codebases 4 (2022) | 10.21468/SciPostPhysCodeb.4 |
| Bonča, Trugman and Batistić, Phys. Rev. B 60, 1633 (1999) | 10.1103/PhysRevB.60.1633 |
| Zhang, Jeckelmann and White, Phys. Rev. Lett. 80, 2661 (1998) | 10.1103/PhysRevLett.80.2661 |
