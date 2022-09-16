'''
# saveDile.py - contains functions for saving DataFrame object.
# SaveToCSV() - saves with CSV extension.
'''
def SaveToCSV(df, nameFile):
    try:
        df.to_csv(f"doc/{nameFile}.csv", sep=';', encoding='cp1251', index=False)
        print(f"File [{nameFile}.csv] saved successfully!")
    except Exception:
        print(Exception)

