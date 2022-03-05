# https://www.geeksforgeeks.org/how-to-add-one-row-in-an-existing-pandas-dataframe/

from IPython.display import display, HTML

import pandas as pd
from numpy.random import randint

data = pd.DataFrame()

# append(), concat(), loc[]. Iloc menja postojeci jedino
# append is deprecated

# Preko loc-a
# ==================================================
dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76]
        }

df = pd.DataFrame(dict)
display(df)

df.loc[len(df.index)] = ['Amy', 89, 93]
display(df)

# Preko appenda
# ==================================================
import pandas as pd
import numpy as np

dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76]
        }

df = pd.DataFrame(dict)
display(df)

df2 = {'Name': 'Amy', 'Maths': 89, 'Science': 93}
df = df.append(df2, ignore_index=True)
display(df)

# Preko concata. Kreira sa novi datafrehm i spoji sa postojecim
# ==================================================
dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76]
        }

df1 = pd.DataFrame(dict)
display(df1)

dict = {'Name': ['Amy', 'Maddy'],
        'Maths': [89, 90],
        'Science': [93, 81]
        }

df2 = pd.DataFrame(dict)
display(df2)

df3 = pd.concat([df1, df2], ignore_index=True)
df3.reset_index()
display(df3)