'''Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.40 min
They want to keep track of customers who buy fruits from them and also the billing process.


Write a python program to implement the class diagram given below.

RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
The above two lists have one-to-one correspondence, initialize it with the data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1

Fruit Name	Apple	Guava	Orange	Grape	Sweet Lime
Price per Kg	200	80	70	110	60Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer
If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, 
if any one of the above two points are applicable. Else apply it on calculated price
Auto-generate purchase id starting from 101 prefixed by “P”. Example – P101,P102 P103 etc.
Return final fruit price
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details'''
class FruitInfo:
    fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    fruit_price_list = [200, 80, 70, 110, 60]

    def get_fruit_price(fruit_name):
        try:
            index = FruitInfo.fruit_name_list.index(fruit_name)
            return FruitInfo.fruit_price_list[index]
        except ValueError:
            return -1


class Purchase:
    counter = 101

    def __init__(self, customer, fruit_name, quantity, customer_type):
        self.purchase_id = "P" + str(Purchase.counter)
        Purchase.counter += 1
        self.customer = customer
        self.fruit_name = fruit_name
        self.quantity = quantity
        self.customer_type = customer_type

    def calculate_price(self):
        fruit_price = FruitInfo.get_fruit_price(self.fruit_name)
        if fruit_price == -1:
            return -1

        total_price = fruit_price * self.quantity

        max_price = max(FruitInfo.fruit_price_list)
        min_price = min(FruitInfo.fruit_price_list)

        if fruit_price == max_price and self.quantity > 1:
            total_price *= 0.98
        elif fruit_price == min_price and self.quantity >= 5:
            total_price *= 0.95

        if self.customer_type == "wholesale":
            total_price *= 0.9

        return round(total_price, 2)


class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


# Sample usage:

customer1 = Customer("John Doe", "1234567890")
purchase1 = Purchase(customer1, "Apple", 2, "retail")
print(purchase1.purchase_id)  
print(purchase1.calculate_price())  

customer2 = Customer("Jane Doe", "0987654321")
purchase2 = Purchase(customer2, "Banana", 5, "wholesale")
print(purchase2.purchase_id)  
print(purchase2.calculate_price())  
