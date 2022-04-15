class Product:
	def __init__(self, price):
		self.price = price
	
	@property # getter decorator
	def price(self):
		return self.__price

	@price.setter # setter decorator
	def price(self, value):
		if value < 0:
			raise ValueError("Price cannot be negative")
		self.__price = value

	# price = property(get_price, set_price)


product = Product(10)

print(product.price)