## Author:
##
## Dieses Programm analysiert Daten im bezug auf die
## FIFA Fußball-Weltmeißterschaft 2022 in Qatar, genauer gesagt
## auf die Anzahl der Besucher für die jeweiligen
##
## Der Datensatz wurde von Kaggle übernommen:
## https://www.kaggle.com/datasets/parasharmanas/qatar-2022-fifa-world-cup-attendance?resource=download
##
## Außerdem werden verschiedene Zusammenhänge und Gruppierungen
## visuell dargestellt mit hilfe des Seaborn Pakets/Bibliothek.
##

import seaborn as sb
import pandas as pd

# .csv Tabelle mit Daten in das Pandas-DataFrame df ablegen
df = pd.read_csv('Attendance Sheet.csv')


print(df.groupby("Venue")["Date"].count())
