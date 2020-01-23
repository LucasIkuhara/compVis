from champion_dictionary import champions
import pandas as pd

data = pd.read_csv('probuilds_data.csv')

def translateEntries(word):
    if word == "blue-team":
        return 0
    elif word == "red-team":
        return 100
    else:
        try:
            return champions[word]
        except:
            print("Champion >{}< not listed".format(word))

#Input data
print(data.head(3))
data = data.applymap(translateEntries)

#Output data
print("\n\n", data.head(3))
data.head()
data.to_csv("treated_dataset.csv", index=False)
print("output: treated_dataset.csv")
