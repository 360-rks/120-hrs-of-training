class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False

class PizzaService:
    counter = 100
    
    def __init__(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = -1
        
    def validate_pizza_type(self):
        if self.pizza_type.lower() == "small" or self.pizza_type.lower() == "medium":
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            pizza_cost_table = {"small": 150, "medium": 200}
            additional_topping_cost_table = {"small": 35, "medium": 50}
            
            pizza_cost = pizza_cost_table[self.pizza_type.lower()] * self.quantity
            if self.additional_topping:
                pizza_cost += additional_topping_cost_table[self.pizza_type.lower()] * self.quantity
                
            self.pizza_cost = pizza_cost
            self.service_id = self.pizza_type[0].upper() + str(PizzaService.counter + 1)
            PizzaService.counter += 1
            
        else:
            self.pizza_cost = -1
    
class DoorDelivery(PizzaService):
    def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super().__init__(pizza_type, quantity, additional_topping)
        self.distance_in_kms = distance_in_kms
        
    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False
        
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() and super().calculate_pizza_cost() != -1:
            delivery_charge_table = {1: 5, 6: 7}
            
            if self.distance_in_kms <= 5:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
            else:
                self.pizza_cost += delivery_charge_table[1] * self.quantity
                self.pizza_cost += delivery_charge_table[6] * (self.distance_in_kms - 5) * self.quantity
                
        else:
            self.pizza_cost = -1

# Testing
pizza_service = PizzaService("Small", 3, True)
pizza_service.calculate_pizza_cost()
print("Service ID:", pizza_service.service_id)
print("Pizza cost:", pizza_service.pizza_cost)

door_delivery = DoorDelivery("Medium", 2, False, 8)
door_delivery.calculate_pizza_cost()
print("Service ID:", door_delivery.service_id)
print("Pizza cost:", door_delivery.pizza_cost)
