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
from wordcloud import WordCloud

# .csv Tabelle mit Daten in das Pandas-DataFrame df ablegen
df1 = pd.read_csv('Attendance.csv')

p1 = plt.figure(1)

sb.countplot(x = "Home" , data=df1, order = df1['Home'].value_counts().index)
plt.title("Mannschaften nach Anzahl der gespielten Fußballspiele als Heimmannschaft")
plt.xlabel("Mannschaften")
plt.ylabel("Anzahl der Spiele")
plt.xticks(rotation=90)

df2 = pd.read_csv('NetFlix.csv')

wc = WordCloud(
    background_color="white", 
    max_words=len(df2['country']), 
    max_font_size=38, 
    relative_scaling=0.4
).generate(" ".join(str(country) for country in df2['country']))

plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.tight_layout()
plt.show()