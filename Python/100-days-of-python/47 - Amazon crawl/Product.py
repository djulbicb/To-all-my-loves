class Product :
    def __init__(self, title:str, price:float):
        self.price = price
        self.title = title

    def __str__(self):
        return f"Product: {self.title}\nPrice: {self.price}"

    def to_email(self):
        return f"<h1>Hi :3</h1>" \
               f"<div>Product {self.title} is available</div>" \
               f"<div>Price {self.price}</div>"
