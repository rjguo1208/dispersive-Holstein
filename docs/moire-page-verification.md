# 验证记录：Moiré 极化子评估页（2026-10-21）

本记录说明新页面的数据来源、作图、构建、显示与引用检查。页面内容本身是评估与估计：所有数值来自 PBE(+D3)
计算与简化模型，没有经过独立复核；扭转 hBN 部分是初步结果，6×6 超胞与 HSE 计算仍在排队。构建与发布通过
不代表这些结果已被验证。

## 改动

- 新增 `src/moire.html`（中文源）及其英文翻译：推导笔记的核对、转向激子的理由、MoSe₂/WSe₂ 层间激子的
  go/no-go、扭转 hBN 的初步结果、下一步、数据与参考文献。
- 四个页面的页面目录都加入“Moiré 极化子评估”；讨论记录新增本次提问。
- 新增 `scripts/plot_results.py`：从 `site/data/*.csv` 生成 `site/results/` 中的 5 张矢量图（SVG + PDF，
  8.6 cm 宽，标注只用英文与数学符号，两种语言共用）。
- 新增 `site/data/`：4 个 CSV 与 2 个 JSON，由本地脚本从计算输出导出，不在本站重新计算。

## 数据来源

- 连续模型的质量标度（图 1）：评估目录中的连续模型脚本输出（三位有效数字）。
- MoSe₂/WSe₂（图 2、图 3）：1×1 单层与双层 DFT 结果的汇总，以及 1°–4.5° 的扭角扫描。
- 扭转 hBN（图 4、图 5）：六种 1×1 双层堆垛，以及 3×3 双层超胞中的 8 个 ΔSCF 三重态计算。另加一项几何分析，
  从各计算的 `t_relax.out` 读出弛豫结构，得到平均层间距、种子原子对、层间滑移与自旋参与比。
- 单层对照没有完成（第 9 步 SCF 未收敛），页面只引用前 8 步的能量与畸变。

## 整理时发现并改正的错误

本地的 MoSe₂/WSe₂ 报告把 Soubelet 等两块样品的堆垛与扭角配反了，原稿用 R 4.5°、H 3° 与实验比较。
按该文的约定，2H 样品 θ ≈ 4.5°，3R 样品 θ ≈ 57°（偏离 R 堆垛 3°）。页面与本地报告都已改为 R 3°、H 4.5°，
并采用发表版的 S = 1.6 ± 0.2（arXiv 第一版为 1.5 ± 0.2）。量级结论不变。

## 构建与站点检查

- `npm run build`：`moire.html` 与 `en/moire.html` 各 128 个公式。
- `npm run check`：`OK: 8 bilingual pages; 966 LaTeX expressions with MathML; 1 TikZ figures; 5 scientific plots; ...`，
  包括两种语言的表格数字与资源一致、所有本地链接与锚点存在、SVG 有 viewBox 且不含位图。

## 显示检查

本地以 `/dispersive-Holstein/` 前缀预览（headless Chromium，`--virtual-time-budget=15000`）：中文与英文桌面版、
中文手机版（390 px）的公式、图和表格显示正常，宽表格在手机上可横向滚动。讨论记录页的新条目与页面目录正常。

## 参考文献

期刊文章已与 Crossref 记录核对，预印本已与 arXiv API 核对：

| 条目 | DOI 或 arXiv |
| --- | --- |
| Arsenault et al., Phys. Rev. Lett. 132, 126501 (2024) | 10.1103/PhysRevLett.132.126501 |
| Abramovitch and Bernardi (2026) | arXiv:2603.14800 |
| Mao et al. (2026) | arXiv:2607.11425 |
| Uzundal et al. (2026) | arXiv:2606.28185 |
| Ramos-Alonso and Ochoa, Phys. Rev. B 114, L051106 (2026) | 10.1103/z93l-2chl |
| Del Grande and Strubbe (2026) | arXiv:2604.28143 |
| Iakovlev, Semina, Glazov and Sherman, Phys. Rev. B 105, 205305 (2022) | 10.1103/PhysRevB.105.205305 |
| Soubelet, Delhomme, Blundo, Stier and Finley, Nat. Commun. 16, 8735 (2025) | 10.1038/s41467-025-64176-6 |
| Knorr, Brem, Meneghini and Malic, Nanoscale 16, 8996 (2024) | 10.1039/d4nr00136b |
| Sio and Giustino, Nat. Phys. 19, 629 (2023) | 10.1038/s41567-023-01953-4 |
| Roux et al., Phys. Rev. X 15, 021067 (2025) | 10.1103/PhysRevX.15.021067 |
| Dai, Lian, Lafuente-Bartolome and Giustino, Phys. Rev. Lett. 132, 036902 (2024) | 10.1103/PhysRevLett.132.036902 |

Soubelet 等的 S 值、峰间距与样品角度取自发表版正文；Roux 等与 Sio–Giustino 的数字取自 arXiv 全文。

## 发布与线上检查

- 推送触发的 `Check theory website` 通过（run 39665430926）；手动发布 `Deploy GitHub Pages` 通过（run 39665441379）。
- 线上 `moire.html`、`en/moire.html`、讨论记录与其余页面，以及 `results/` 与 `data/` 中的文件均返回 HTTP 200。
- 英文页的线上截图（`--timeout=60000`）中公式、图与表格显示正常。
