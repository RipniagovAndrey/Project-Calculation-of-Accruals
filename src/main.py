import pandas as pd
from src.сonstants import st_counter, st_standard
from src.saveFile import SaveToCSV
from src.calculation import CalculatiocAccruals, CalculationGroupByHome

if __name__ == '__main__':
    abonents_csv = pd.read_csv("dataset/абоненты.csv", delimiter=";")
    abonents_df = pd.DataFrame(abonents_csv)

    abonents_df = CalculatiocAccruals(abonents_df, st_standard, st_counter)
    SaveToCSV(abonents_df, "Начисления_абоненты")

    group_by_home = CalculationGroupByHome(abonents_df)
    SaveToCSV(group_by_home, "Начисления_дома")


