class Balance:
    def __init__(self,client_fname, client_lname, mony):
        self.mony = mony 
        self.client_fname = client_fname
        self.client_lname = client_lname
class Product:
    def __init__(self, product,amount, price):
        self.product = product
        self.amount = amount
        self.price = price
class Bucket:
    def __init__(self,client_fname, client_lname, mony):
        self.bucket_list = []
        self.balance = Balance(client_fname, client_lname, mony)
    def throw_to_bucket(self, product_name, amount):
        for product in self.bucket_list:
            if product.product == product_name:
                if product not in self.bucket_list:
                    self.bucket_list.append(product)
                else:
                    self.amount = amount
                    amount += 1
    def return_product(self, product_name,amount_to_delete):
        for product in self.bucket_list:
            if product.product == product_name:
                if product.amount >= amount_to_delete:
                    product.amount -= amount_to_delete
                    print(f'{product_name} успішно видалили з корзини')
                else:
                    print(f'Недостатньо кількості продукту {product_name} у корзині')
        else:
            print(f'Продукту {product_name} не знайдено в корзині')
    def buy_products(self):
        if self.balance.mony >= self.overall_amount:
            print(f'Продукти які ви купили:{self.bucket_list}')
            self.bucket_list.clear()
        else:
            print('На вашому балансі не достатньо грошей')





