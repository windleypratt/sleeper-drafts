import pandas as pd
from functions.storage_functions import *
from functions.sleeper_functions import *

new_leagues = ['793658982555299840','784470918977228800','786404550704758784']

users = users_from_leagues(leagues = new_leagues, update = True)

df = leagues_from_users(users=users.picked_by.to_list(), update=True)


print(len(df))
print(df.head())