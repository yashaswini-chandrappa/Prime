'''PRODUCT STORE
Design and create a online store for products(name, price)
 1. Track the total products being created
 2. Create a static method to calculate the discounted price of a product given the discount percentage

Topics covered:
1. Class Attribute
2. Instance Attribute
3. Class Method
4. Instance Method
5. static Method
'''
class Product_store:
    product_count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product_store.product_count += 1  #accessing class attribute

    def get_info(self): #instance method
        print(f"The price of the product {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls): 
        print(f"The total products in store is {cls.product_count}")

    @staticmethod
    def calc_discount(price, percentage):
        discounted_price = (price -(price * percentage / 100))
        print(discounted_price)


p1 = Product_store("Phone", 30_000)
p2 = Product_store("Watch" , 25_000)
p3 = Product_store("Perfume", 1000)


p1.get_info()
Product_store.get_count()
p1.calc_discount(p1.price, 10)
