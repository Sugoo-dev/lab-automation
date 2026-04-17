import numpy as np
import pandas as pd


class GrowthCurveSetup:
    """
    Prepares inoculation volumes for OD-normalized growth curve experiments.

    Parameters
    ----------
    od_targets : list of float
        Target ODs for normalization. Default: [0.05, 0.10, 0.20]
    volume_ul : float
        Final well/tube volume in µL. Default: 200
    cpd_conc : float
        Desired compound concentration in µg/mL. Default: 15
    cpd_stock : float
        Compound stock concentration in µg/mL. Default: 1000
    n_cultures : int
        Number of cultures. Default: 2
    od_values : list of float, optional
        Provide ODs directly instead of prompting. Default: None (will prompt)
    """

    DEFAULT_OD_TARGETS = [0.05, 0.10, 0.20]
    DEFAULT_VOLUME_UL  = 200
    DEFAULT_CPD_CONC   = 15
    DEFAULT_CPD_STOCK  = 1000

    def __init__(
        self,
        od_targets=None,
        volume_ul=None,
        cpd_conc=None,
        cpd_stock=None,
        n_cultures=2,
        od_values=None,
    ):
        self.od_targets = od_targets if od_targets is not None else self.DEFAULT_OD_TARGETS
        self.volume_ul  = volume_ul  if volume_ul  is not None else self.DEFAULT_VOLUME_UL
        self.cpd_conc   = cpd_conc
        self.cpd_stock  = cpd_stock
        self.n_cultures = n_cultures

        self.od_values = od_values if od_values is not None else self._prompt_od_values()

        if self.cpd_conc is not None and self.cpd_stock is not None:
            self.cpd_vol_ul = round(self.cpd_conc * self.volume_ul / self.cpd_stock, 2)
        else:
            self.cpd_vol_ul = None

    def _prompt_od_values(self):
        od_values = []
        for i in range(1, self.n_cultures + 1):
            od = float(input(f'  OD of culture {i}? '))
            od_values.append(od)
        return od_values

    def _build_volume_tables(self):
        """Returns (df_lb, df_bac) DataFrames indexed by culture number."""
        records_lb, records_bac = [], []

        for i, od in enumerate(self.od_values, start=1):
            row_lb  = {f'OD = {t:.2f}': round(self.volume_ul - self.volume_ul * t / od, 2)
                       for t in self.od_targets}
            row_bac = {f'OD = {t:.2f}': round(self.volume_ul * t / od, 2)
                       for t in self.od_targets}
            row_lb['Culture']  = i
            row_bac['Culture'] = i
            records_lb.append(row_lb)
            records_bac.append(row_bac)

        df_lb  = pd.DataFrame(records_lb).set_index('Culture')
        df_bac = pd.DataFrame(records_bac).set_index('Culture')
        return df_lb, df_bac

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def report(self):
        """Print the full inoculation scheme to stdout."""
        df_lb, df_bac = self._build_volume_tables()

        print('\n── Volume of LB to add (µL) ──')
        print(df_lb.to_string())

        print('\n── Volume of day culture to add (µL) ──')
        print(df_bac.to_string())
        
        if self.cpd_vol_ul is not None:
            stock_mg_ml = self.cpd_stock / 1000
            print(f'\n── Compound ──')
            print(f'  Add {self.cpd_vol_ul} µL from a {stock_mg_ml} mg/mL stock'
                  f' (→ {self.cpd_conc} µg/mL final in {self.volume_ul} µL)')
            
    def get_tables(self):
        """Return (df_lb, df_bac) for downstream use (plotting, export, etc.)."""
        return self._build_volume_tables()


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------

if __name__ == '__main__':
    print('=== Growth Curve Setup ===')
    print('(Press Enter to keep the default value shown in brackets)\n')

    use_cpd = input('Are you using a compound? [y/n]: ').strip().lower()
    if use_cpd == 'y':
        conc  = input('Compound concentration µg/mL [15]: ').strip()
        stock = input('Stock concentration µg/mL [1000]: ').strip()
    else:
        conc  = None
        stock = None

    init_targets = input('Desired initial OD values - space separated [0.05 0.10 0.20]: ').strip()
    vol   = input('Final volume in µL [200]: ').strip()
    n     = input('Number of cultures [2]: ').strip()


    print()  # blank line before OD prompts

    exp = GrowthCurveSetup(

        volume_ul  = float(vol)   if vol   else None,
        cpd_conc  = float(conc)  if conc  else None,
        cpd_stock = float(stock) if stock else None,
        n_cultures = int(n)       if n     else 2,
        od_targets = [float(x) for x in init_targets.split()] if init_targets else None,
        )

    exp.report()