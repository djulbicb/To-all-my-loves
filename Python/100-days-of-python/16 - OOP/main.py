
import prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.title = "Pokemon index"
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

# moze i ovako
# table.add_column("Third column", ["3rd Column A1", "3rd Column A2"])

print(table)

t = """
sss
"""
print(t)