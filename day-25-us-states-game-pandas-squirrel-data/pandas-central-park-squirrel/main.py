from numpy import unique
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data[data["Primary Fur Color"].notna()]["Primary Fur Color"]
# squirrel_colors = data["Primary Fur Color"]

unique_squirrel_colors = {
    "color": [],
    "count": [],
}

for color in squirrel_colors:
    if color in unique_squirrel_colors["color"]:
        indx = unique_squirrel_colors["color"].index(color)
        unique_squirrel_colors["count"][indx] += 1
    else:
        unique_squirrel_colors["color"].append(color)
        unique_squirrel_colors["count"].append(1)


print(unique_squirrel_colors)
unique_squirrel_colors_df = pandas.DataFrame(unique_squirrel_colors)
print(unique_squirrel_colors_df)
unique_squirrel_colors_df.to_csv("2018_Central_park_Squirrel_Uniq_colors.csv")