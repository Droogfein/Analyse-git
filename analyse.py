## Author:
##
## Dieses Programm analysiert Daten im bezug auf die
## FIFA Fußball-Weltmeißterschaft 2022 in Qatar, genauer gesagt
## auf die Anzahl der Besucher für die jeweiligen
##
## Der Datensatz wurde von Kaggle übernommen:
## https://www.kaggle.com/
##
## Außerdem werden verschiedene Zusammenhänge und Gruppierungen
## visuell dargestellt mit hilfe des Seaborn Pakets/Bibliothek.
##

import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# .csv Tabelle mit Daten in das Pandas-DataFrame df ablegen
df1 = pd.read_csv('Attendance.csv')

sb.countplot(x = "Home" , data=df1, order = df1['Home'].value_counts().index)
plt.title("Mannschaften nach Anzahl der gespielten Fußballspiele als Heimmannschaft")
plt.xlabel("Mannschaften")
plt.ylabel("Anzahl der Spiele")
plt.xticks(rotation=90)
plt.tight_layout()

df2 = pd.read_csv('NetFlix.csv')

wc = WordCloud(
    background_color="white", 
    max_words=len(df2['country']), 
    max_font_size=100, 
    relative_scaling=.4
).generate(" ".join(str(country) for country in df2['country']))

plt.figure()
plt.imshow(wc)
plt.title("World cloud der Länder wo Netflix FIlme und Serien aufgenommen wurden.")
plt.axis("off")
plt.tight_layout()
plt.show()