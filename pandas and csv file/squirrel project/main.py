import pandas as pd
data=pd.read_csv("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\pandas and csv file/squirrel project/squirrel.csv")

gray_squirrel=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrel=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel=len(data[data["Primary Fur Color"]=="Black"])

squirrel_dict={
    "Fur colors": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

file=pd.DataFrame(squirrel_dict)
file.to_csv("squirrel_count.csv")



