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
import matplotlib.pyplot as plt
import pandas as pd

# .csv Tabelle mit Daten in das Pandas-DataFrame df ablegen
df = pd.read_csv('Attendance.csv')

sb.countplot(x = "Home" , data=df, order = df['Home'].value_counts().index)
plt.title("Mannschaften nach Anzahl der gespielten Fußballspiele")
plt.xlabel("Mannschaften")
plt.ylabel("Anzahl der Spiele")
plt.xticks(rotation=90)
plt.show()

sb.jointplot(data=df, x="Home", y= "Away", kind="hex")
plt.show()
