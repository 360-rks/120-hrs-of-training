class Table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)

