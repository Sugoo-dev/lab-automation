lab-automation
A growing collection of Python scripts I use to reduce manual calculation overhead during day-to-day bench work. Written as a postdoctoral researcher in antimicrobial pharmacology — but the tools are general enough to apply to any microbiology lab context.
The goal is not to replace lab judgment, but to eliminate repetitive arithmetic and make experimental setup faster and less error-prone.

Tools
growth_curve_setup.py
Calculates inoculation volumes for OD-normalized growth curve experiments.
Given the measured OD of overnight cultures, computes how much media and bacterial suspension to combine to reach a target starting OD — across multiple cultures and multiple target ODs simultaneously. Also calculates compound volume to add from a stock solution.
Inputs (interactive prompts):

Target OD values
Final well volume (µL)
Compound concentration and stock concentration
Number of cultures and their measured ODs

Output:
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
Usage:
bashpython growth_curve_setup.py
All parameters have sensible defaults — press Enter to accept them, or type a new value to override.

Stack

Python 3
pandas
numpy


Structure
Each script is self-contained and runs from the terminal with interactive prompts. No configuration files or dependencies beyond standard scientific Python libraries.
New tools will be added as recurring calculations come up in the lab.

Author
Lorenzo — Postdoctoral Researcher, Pharmaceutical Sciences
Focused on antimicrobial drug discovery and bacterial cell division mechanisms.
