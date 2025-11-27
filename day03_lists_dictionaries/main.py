totalPrice = 0
products = [{"name": "apple",
			 "price": 0.99,
			 "stock": 10},
			 
			 {"name": "banana",
			 "price": 1.78,
			 "stock": 32},

			{"name": "carrot",
			 "price": 2.35,
			 "stock": 3}]

for product in products:
	print(f"{product['name']} sells for ${product['price']} and we have {product['stock']} in stock")

	totalPrice += product['price']

averagePrice = round(totalPrice / len(products), 2)
print(f"The average price of our products is: ${averagePrice}")