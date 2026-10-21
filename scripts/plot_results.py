"""Plot the moire go/no-go results from site/data/*.csv to vector SVG + PDF in site/results/.

Needs matplotlib (not part of the site build). Figures are 8.6 cm wide (one Physical Review column) and drawn at 1:1;
labels are English or mathematical so the same files serve both languages.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA, OUT = ROOT / "site" / "data", ROOT / "site" / "results"
W = 3.375                                     # inches, APS single column
BLUE, VERM, GREEN, GRAY = "#0072B2", "#D55E00", "#009E73", "#7F7F7F"
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif"], "mathtext.fontset": "stix",
    "font.size": 9, "axes.labelsize": 9, "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 7.5,
    "axes.linewidth": 0.7, "lines.linewidth": 1.1, "lines.markersize": 3.5, "legend.frameon": False,
    "xtick.direction": "in", "ytick.direction": "in", "xtick.top": True, "ytick.right": True,
    "xtick.major.width": 0.7, "ytick.major.width": 0.7, "xtick.minor.width": 0.5, "ytick.minor.width": 0.5,
    "xtick.major.size": 3.0, "ytick.major.size": 3.0, "xtick.minor.size": 1.6, "ytick.minor.size": 1.6,
    "figure.constrained_layout.use": True, "savefig.bbox": "standard", "pdf.fonttype": 42,
    "svg.fonttype": "path", "svg.hashsalt": "dispersive-Holstein", "hatch.linewidth": 0.6,
})


def table(name):
    with open(DATA / name) as f:
        return [r for r in csv.DictReader(line for line in f if not line.startswith("#"))]


def save(fig, name):
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / f"{name}.svg", metadata={"Date": None})
    fig.savefig(OUT / f"{name}.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(fig)
    print("wrote", name)


def mass_scaling():
    rows = table("moire-mass-scaling.csv")
    fig, ax = plt.subplots(figsize=(W, 2.5))
    ax.axhspan(0.06, 0.2, color=GRAY, alpha=0.18, lw=0)
    ax.text(51, 0.11, "intralayer deformation-potential\n$E_p^0$ (estimate)", ha="right", va="center", fontsize=7, color="0.3")
    for (carrier, m), style in {("hole", "0.45"): ("k", "o", "-"), ("exciton", "0.8"): (BLUE, "s", "--"),
                                ("exciton", "1.1"): (VERM, "^", "-.")}.items():
        r = [x for x in rows if x["carrier"] == carrier and x["mass_me"] == m and float(x["V_meV"]) <= 50]
        lab = f"hole, $m^*={m}$" if carrier == "hole" else f"exciton COM, $M={m}$"
        ax.semilogy([float(x["V_meV"]) for x in r], [float(x["Ep0_needed_eV"]) for x in r], color=style[0],
                    marker=style[1], ls=style[2], label=lab)
    ax.set_xlim(0, 52)
    ax.set_ylim(1e-5, 20)
    ax.set_xlabel(r"moiré potential depth $V$ (meV)")
    ax.set_ylabel(r"contact $E_p^0$ for $\lambda_M=1$ (eV)")
    ax.legend(loc="lower left")
    save(fig, "moire-mass-scaling")


def tmd_twist():
    rows = table("tmd-ix-twist-scan.csv")
    fig, ax = plt.subplots(figsize=(W, 2.6))
    for st, col, mk, ls in (("R", BLUE, "o", "-"), ("H", VERM, "s", "--")):
        r = [x for x in rows if x["stack"] == st]
        t = np.array([float(x["theta_eff_deg"]) for x in r])
        f = lambda *k: np.array([sum(float(x[c]) for c in k) for x in r])
        lo = f("Ep_LB_meV", "Ep_A1p_meV", "Ep_LA_bonded_meV")
        hi = f("Ep_LB_meV", "Ep_A1p_meV", "Ep_LA_slip_meV", "Ep_flex_meV")
        ax.fill_between(t, lo, hi, color=col, alpha=0.22, lw=0, label=f"$E_p$ range, {st}")
        ax.semilogy(t, f("W_X_meV"), color=col, marker=mk, ls=ls, label=f"$W_X$, {st} stacking")
    for t, lab in ((3.0, "3R sample"), (4.5, "2H sample")):
        ax.axvline(t, color=GRAY, lw=0.6, ls=":")
        ax.text(t - 0.05, 160, lab, ha="right", va="center", fontsize=7, color="0.3")
    ax.set_xlim(0.9, 4.6)
    ax.set_ylim(1e-4, 500)
    ax.set_xlabel(r"effective twist angle $\theta_{\mathrm{eff}}$ (deg)")
    ax.set_ylabel("energy (meV)")
    ax.legend(loc="lower right", handlelength=1.8)
    save(fig, "tmd-ix-twist")


def tmd_huang_rhys():
    rows = table("tmd-ix-twist-scan.csv")
    pick = {"R": next(x for x in rows if x["stack"] == "R" and float(x["theta_eff_deg"]) == 3.0),
            "H": next(x for x in rows if x["stack"] == "H" and float(x["theta_eff_deg"]) == 4.5)}
    chan = [("S_LB", "LB\n3.6 meV"), ("S_A1p", "A$_1'$\n30 meV"), ("S_LA_bonded", "LA\nbonded"),
            ("S_LA_slip", "LA\nslipping"), ("S_flex", "flexural\n(bound)")]
    fig, ax = plt.subplots(figsize=(W, 2.5))
    x = np.arange(len(chan))
    # Soubelet et al., Nat. Commun. 16, 8735 (2025): S = 3.1 +- 0.4 (3R), 1.6 +- 0.2 (2H)
    ax.axhspan(2.7, 3.5, color=BLUE, alpha=0.16, lw=0)
    ax.axhspan(1.4, 1.8, color=VERM, alpha=0.16, lw=0)
    ax.text(-0.45, 3.1, "exp. 3R", va="center", fontsize=7, color=BLUE)
    ax.text(-0.45, 1.6, "exp. 2H", va="center", fontsize=7, color=VERM)
    for st, col, off, hatch, lab in (("R", BLUE, -0.19, None, r"3R, $\theta_{\mathrm{eff}}=3^\circ$"),
                                     ("H", VERM, 0.19, "////", r"2H, $\theta_{\mathrm{eff}}=4.5^\circ$")):
        ax.bar(x + off, [float(pick[st][c]) for c, _ in chan], width=0.36, color=col, alpha=0.85 if hatch is None else 0.55,
               hatch=hatch, edgecolor="white" if hatch else col, lw=0.3, label=lab)
    ax.set_yscale("log")
    ax.set_ylim(3e-4, 10)
    ax.set_xlim(-0.55, len(chan) - 0.45)
    ax.set_xticks(x)
    ax.set_xticklabels([l for _, l in chan], fontsize=7.5)
    ax.tick_params(axis="x", which="both", top=False, bottom=False)
    ax.set_ylabel("Huang–Rhys factor $S$")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.72))
    save(fig, "tmd-ix-huang-rhys")


def hbn_linear():
    rows = sorted(table("hbn-stackings.csv"), key=lambda r: float(r["g"]))
    fig, ax = plt.subplots(figsize=(W, 2.3))
    y = np.arange(len(rows))
    tot = np.array([float(r["Ep0_LA_eV"]) + float(r["Ep0_LB_eV"]) for r in rows])
    g = np.array([float(r["g"]) for r in rows])
    g_la = g * np.array([float(r["Ep0_LA_eV"]) for r in rows]) / tot
    ax.barh(y, g_la, color=GRAY, height=0.6, label="in-plane LA")
    ax.barh(y, g - g_la, left=g_la, color=BLUE, height=0.6, label="interlayer breathing (LB)")
    ax.axvline(1.0, color="k", lw=0.8, ls="--")
    ax.text(0.98, len(rows) - 0.55, "self-trapping\nthreshold $g=1$", ha="right", va="top", fontsize=7)
    names = [r["stacking"].replace("'", "′") + f"  ({r['on_top_contacts']})" for r in rows]
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7.5)
    ax.tick_params(axis="y", which="both", left=False, right=False)
    ax.set_xlim(0, 1.1)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlabel(r"2D self-trapping parameter $g=E_p^0A_{\mathrm{cell}}M/\pi\hbar^2$")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.08))
    save(fig, "hbn-linear")


def hbn_triplet():
    rows = {r["run"]: r for r in table("hbn-triplet-3x3.csv")}
    runs = [("st3_AAb", "AA"), ("st3_ApB", "A′B"), ("st3_AAp_s0.75", "AA′"), ("st3_ABp", "AB′\n(slid)")]
    fig, (a, b) = plt.subplots(2, 1, figsize=(W, 3.9), sharex=True)
    x = np.arange(len(runs))
    relax = [-float(rows[k]["E_selftrap_eV"]) for k, _ in runs]
    stokes = [float(rows[k]["Stokes_eV"]) for k, _ in runs]
    a.axhspan(1.75, 2.25, color=VERM, alpha=0.15, lw=0)
    a.text(-0.4, 2.0, "observed 4-eV band: 1.75 eV below the free exciton,\n2.25 eV below the gap (Roux et al.)",
           va="center", fontsize=6.8, color="0.25")
    hatch = ["", "", "", "////"]
    a.bar(x - 0.19, relax, width=0.36, color=BLUE, hatch=hatch, edgecolor="white", lw=0.3, label=r"triplet relaxation $-\Delta E_T$")
    a.bar(x + 0.19, stokes, width=0.36, color="k", alpha=0.75, hatch=hatch, edgecolor="white", lw=0.3, label="Stokes shift")
    a.set_ylim(0, 2.5)
    a.set_ylabel("energy (eV)")
    a.legend(loc="upper left", bbox_to_anchor=(0.0, 0.67))
    d_cell = [float(rows[k]["d_relaxed_A"]) - float(rows[k]["d_flat_A"]) for k, _ in runs]
    d_pair = [float(rows[k]["pair_dz_relaxed_A"]) - float(rows[k]["pair_dz_flat_A"]) for k, _ in runs]
    b.axhline(0, color=GRAY, lw=0.6)
    b.bar(x - 0.19, d_cell, width=0.36, color=GREEN, hatch=hatch, edgecolor="white", lw=0.3, label="cell average")
    b.bar(x + 0.19, d_pair, width=0.36, color="k", alpha=0.75, hatch=hatch, edgecolor="white", lw=0.3, label="seeded pair")
    b.set_ylim(-0.55, 0.2)
    b.set_ylabel(r"interlayer $\Delta d$ (Å)")
    b.legend(loc="lower right", ncol=2)
    b.set_xticks(x)
    b.set_xticklabels([l for _, l in runs])
    b.set_xlim(-0.55, len(runs) - 0.45)
    for ax in (a, b):
        ax.tick_params(axis="x", which="both", top=False, bottom=False)
    for ax, lab in ((a, "(a)"), (b, "(b)")):
        ax.text(0.985, 0.95, lab, transform=ax.transAxes, ha="right", va="top")
    save(fig, "hbn-triplet")


if __name__ == "__main__":
    mass_scaling()
    tmd_twist()
    tmd_huang_rhys()
    hbn_linear()
    hbn_triplet()
