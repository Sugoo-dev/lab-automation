# lab-automation

A growing collection of Python scripts I use to reduce manual calculation overhead during day-to-day bench work. Written as a postdoctoral researcher in antimicrobial pharmacology — but the tools are general enough to apply to any microbiology lab context.

The goal is not to replace lab judgment, but to eliminate repetitive arithmetic and make experimental setup faster and less error-prone.

---

## Tools

### `growth_curve_setup.py`
Calculates inoculation volumes for OD-normalized growth curve experiments.

Given the measured OD of overnight cultures, computes how much media and bacterial suspension to combine to reach a target starting OD — across multiple cultures and multiple target ODs simultaneously. Also calculates compound volume to add from a stock solution.

**Inputs (interactive prompts):**
- Target OD values
- Final well volume (µL)
- Compound concentration and stock concentration
- Number of cultures and their measured ODs

**Output:**
```
── Volume of LB to add (µL) ──
         OD = 0.05  OD = 0.10  OD = 0.20
Culture
1           177.78     155.56     111.11
2           173.68     147.37      94.74

── Volume of day culture to add (µL) ──
         OD = 0.05  OD = 0.10  OD = 0.20
Culture
1            22.22      44.44      88.89
2            26.32      52.63     105.26

── Compound ──
  Add 3.0 µL from a 1.0 mg/mL stock (→ 15 µg/mL final in 200 µL)
```

**Usage:**
```bash
python growth_curve_setup.py
```

All parameters have sensible defaults — press Enter to accept them, or type a new value to override.

---

### `growth_curve_analysis.py`
Parses and plots OD600 growth curve data exported by the Synergy H1 microplate reader (Gen5 software).

Reads the plate layout directly from the Excel file, so no manual configuration is needed — just point it at the file and it figures out which wells are active and what they contain.

**Inputs (interactive prompts):**
- Path to the Gen5-exported `.xlsx` file
- Conditions to plot (by index)
- Wells to exclude (optional)
- Plot title
- Output filename (or display interactively)

**Output:**
```
Available conditions:
  [0] MP68 (LB)          — wells: A1, A2, A3, A4, A5, A6, A7, A8
  [1] MP68 (TSB)         — wells: B1, B2, B3, B4, B5, B6, B7, B8
  [2] MP110 (TSB)        — wells: C1, C2, C3, C4, C5, C6, C7, C8
  [3] MP115 (TSB)        — wells: D1, D2, D3, D4, D5, D6, D7, D8
  [4] Control (LB)       — wells: E1
  [5] Control (TSB)      — wells: E2

Conditions to plot (e.g. 0,1,4 — or Enter for all): 0,2
Selected wells: A1, A2, A3, A4, A5, A6, A7, A8, C1, C2, C3, C4, C5, C6, C7, C8
Wells to exclude (e.g. A1,A3 — or Enter to keep all):
```

One subplot per selected condition, each autoscaled independently. Each well is plotted as an individual line with a unique color.

**Usage:**
```bash
python growth_curve_analysis.py
```

**Requirements:** `openpyxl`, `pandas`, `numpy`, `matplotlib`

---

## Stack

- Python 3
- pandas
- numpy

---

## Structure

Each script is self-contained and runs from the terminal with interactive prompts. No configuration files or dependencies beyond standard scientific Python libraries.

New tools will be added as recurring calculations come up in the lab.

---

## Author

Lorenzo — Postdoctoral Researcher, Pharmaceutical Sciences  
Focused on antimicrobial drug discovery and bacterial cell division mechanisms.
