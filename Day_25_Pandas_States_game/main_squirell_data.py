import pandas

raw_data = pandas.read_csv("Day_25_Pandas_States_game/squirells_data.csv")
print(raw_data)
colors_of_interest = ["Gray", "Cinnamon", "Black", "Red"]
my_squirells = {}
for color in colors_of_interest:
    my_squirells[color] = len(raw_data[raw_data["Primary Fur Color"] == color])
print(my_squirells)
squirells_dataframe = pandas.DataFrame(my_squirells, index=["Count"])
print(squirells_dataframe)
squirells_dataframe.to_csv("Day_25_Pandas_States_game/squirells_data_dataframe.csv")




