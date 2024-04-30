!pip install python-Levenshtein
import pandas as pd
from fuzzywuzzy import fuzz

data = pd.read_excel("QURAN_DF1 - Copy.xlsx")

def f(a, data, threshold = 100):
    s = None
    for index, row in data.iterrows():
        similarity = fuzz.token_sort_ratio(a, row["Clean Text"])
        if similarity >= threshold:
            s = row["Sura Nam"]
            break
    return s

while True:
    a = input("Please enter the Ayah you want to search for, hit x to exit : ")
    s = f(a, data)
    if s is not None:
        print("The Ayah is in Surah:", s)
    elif a.lower() == 'x':
        print("Exiting the program.")
        break
    else:
        print("No Sura for given Ayah.")