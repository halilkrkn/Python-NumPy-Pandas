# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb_1000.csv")

print(films.columns)
#%% Filmlerin ortalamasını mean() fonk. ile aldık.
print(films.star_rating.mean())

#%% Mesela burda bir filmin türüne göre beğeni ortalamasını bulduk
## groupby() ile istenilen türü Seçtik ve sonra star_rating ile de ortlamasını aldık.
## Yani filmlerin tümünün ortalamasını almadık sadece fimlerin türleri arasında ortalamasını aldık.

print(films.groupby("genre").star_rating.mean()) 