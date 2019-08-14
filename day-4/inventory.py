class Store():
    def __init__(self, name, location):
        self.name = name
        self.warehouse_list = []
        self.location = location

    def add_warehouse(self, warehouse):
        self.warehouse_list.append(warehouse)

    def remove_warehouse(self, warehouse):
        self.warehouse_list.remove(warehouse)

    def warehouses(self):
        print(
            f'{self.name} has the following warehouses providing stock:')
        for warehouse in self.warehouse_list:
            print(f'Warehouse #{warehouse.idnum} in {warehouse.location}')
    
    def products(self):
        print(f'{self.name} has the following products available:')
        for warehouse in self.warehouse_list:
            for product in warehouse.product_list:
                print(f'{product.name}')
    
    def available(self, product_name):
        for warehouse in self.warehouse_list:
            for product in warehouse.product_list:
                if product.name == product_name:
                    print(f"{product_name} is available!")
                    return
        print(f"{product_name} is not available!")


class WareHouse():
    def __init__(self, idnum, location):
        self.idnum = idnum
        self.product_list = []
        self.location = location

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def products(self):
        print(f'Warehouse {self.idnum} has the following products available:')
        for product in self.product_list:
            print(product.name)


class Product():
    def __init__(self, name, category, manufacturer, price):
        self.name = name
        self.category = category
        self.manufacturer = manufacturer
        self.price = price


macbook = Product('MacBook', 'electronics', 'Apple', 1750)
zenbook = Product('ZenBook', 'electronics', 'Asus', 1450)
XPS13 = Product('XPS13', 'electronics', 'Dell', 1200)

warehouse1 = WareHouse(1, 'Mississauga')

warehouse1.add_product(macbook)
warehouse1.add_product(zenbook)

lambdamart = Store('LambdaMart', 'Calgary')

lambdamart.add_warehouse(warehouse1)

breakpoint()
