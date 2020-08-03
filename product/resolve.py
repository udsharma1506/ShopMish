'''
Resolve is created to acts an intermediate/resolver between MishiPay and other 3rd party vendors
Here we change the structure of the request body as per understands by 3rd party
and change the response back to the structure understand by app
'''
from mishshop.shopify import Shopify

SHOPIFY = "shopify"

#To fetch the list of products
def get_product(channel_name):
	response = {}
	if channel_name == SHOPIFY:
		# Modify request data

		response = Shopify.get_product_list()

		# TODO: Modify response data
	return response

# To Create an Order
def create_order(channel_name, data):

	response = {}
	if channel_name == SHOPIFY:
		line_items = []
		# Modify request data

		for i,j in dict(data).items():
			temp =       {
					"variant_id": i,
					"quantity": j
				  }
			line_items.append(temp)
		data = {"order":{"line_items": line_items}}
		response = Shopify.create_an_order(data)

		# TODO: Modify response data
	return response

