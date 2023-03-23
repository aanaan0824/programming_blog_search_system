import pandas as pd
from matplotlib import pyplot as plt
 
pd.set_option('display.max_columns', None)
 
df = pd.read_csv('books.csv')
# print(df.info())
data = df[pd.notnull(df['original_publication_year'])]
grouped = data.groupby(by='original_publication_year').count()['title']
# print(grouped)
 
grouped1 = data.average_rating.groupby(by=data['original_publication_year']).mean()
# print(grouped1)
 
_x = grouped1.index
_y = grouped1.values
 
plt.figure(figsize=(15,6),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(range(len(_x))[::10],_x[::10].astype(int),rotation=45)
plt.savefig("books.png")
plt.show()