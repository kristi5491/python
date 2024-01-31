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

    def __overall_sum(self):
        overall_sum = 0
        for product_in_bucket in self.bucket_list:
            overall_sum += product_in_bucket.amount
        return overall_sum

    def throw_to_bucket(self, product_name, amount_product, price_product):
        for product in self.bucket_list:
            if product.product == product_name:
                current_amount = product.amount + amount_product
                current_price = current_amount * product.price
                self.bucket_list.append(product)
                print(f'{product_name} добавлено в корзину та почточна ціна {current_price}')
                break
        else:
            new_product = Product(product_name, amount_product, price_product)
            self.bucket_list.append(new_product)
            print(f'Тепер в корзині  {product_name}')
    def return_product(self, product_name,amount_to_delete):
        for product in self.bucket_list:
            if product.product == product_name:
                if product.amount >= amount_to_delete:
                    current_amount = product.amount - amount_to_delete
                    current_price = current_amount * product.price
                    print(f'{product_name}:{current_price} успішно видалили з корзини')
                    break
                else:
                    print(f'Недостатньо кількості продукту {product_name} у корзині')
        else:
            print(f'Продукту {product_name} не знайдено в корзині')
    def buy_products(self):
        overall_price = self.__overall_sum()  
        if self.balance.mony >= overall_price:
            self.balance.mony -= overall_price
            product_names = [product.product for product in self.bucket_list]
            print(f'Продукти, які ви купили: {product_names} та скілтки ви заплатили за це {overall_price}')
            self.bucket_list.clear()
        else:
            print('На вашому балансі не достатньо грошей')

cart = bucket = Bucket("John", "Doe", 100)

bucket.throw_to_bucket("Apple", 5, 2.5)
bucket.throw_to_bucket("Banana", 3, 1.0)

bucket.throw_to_bucket("Apple", 5, 2.5)

bucket.return_product("Banana", 2)

bucket.buy_products()


