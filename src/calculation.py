'''
# calculation.py - contains functions for calculation.
# CalculatiocAccruals() - calculates accruals.
# CalculationGroupByHome() - calculates accruals group by home.
'''
import pandas as pd
import numpy as np

def CalculatiocAccruals(abonents_df, st_standard=0, st_counter=0):
    try:
        accruals = []
        for index, row in abonents_df.iterrows():
            match row["Тип начисления"]:
                case 1:
                    accruals.append(st_standard)
                case 2:
                    accruals.append(round((row["Текущее"] - row["Предыдущее"]) * st_counter, 2))
                case _:
                    accruals.append(0)
        abonents_df["Начислено"] = accruals
        return abonents_df
    except Exception:
        print(Exception)

def CalculationGroupByHome(abonents_df):
    try:
        group_by_home_sum = abonents_df[["Улица", "№ дома", "Начислено"]].groupby(["Улица", "№ дома"], as_index=False).sum()
        pd.DataFrame(group_by_home_sum)
        group_by_home_sum.insert(0, "№ строки", np.arange(group_by_home_sum.shape[0]))
        group_by_home_sum["Начислено"] = group_by_home_sum["Начислено"].round(2)
        return group_by_home_sum
    except Exception:
        print(Exception)