from prettytable import PrettyTable

table = PrettyTable()
list_of_pocemons = ["Pucachu", "Bulbazavr", "Squirtel"]
table.add_column("Pokemon name", list_of_pocemons, align="l")
types = ["electric", "grass", "water"]
table.add_column("Type", types, align="l")

print(table)
