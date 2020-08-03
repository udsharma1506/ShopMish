import requests
import base64
import json

SHOPIFY_URL = 'https://a38f4a6a8cb713fe2bebdbf3df331f54:3182dcd29ff6c3f6f2dd325ba99b4216@mishipaytestdevelopmentemptystore.myshopify.com'

GET_PRODUCT_LIST = "/admin/api/2020-01/products.json"
CREATE_ORDER = "/admin/api/2020-07/orders.json"

class Baseclass(object):

	@classmethod
	def get_authrization(cls):
		# no code is present since I found SHOPIFY_URL working without authentication
		# but we can add the authentication method here if any is present.
		return None

	@classmethod
	def make_request(cls, auth_url, method, data={}, headers=None):
		# we could call the get_authrization here to validate the requests
		# cls.get_authrization()

		if method == 'GET':
			auth_response = requests.request(method, auth_url, headers=headers)
		else:
			auth_response = requests.request(method, auth_url, headers=headers, json=data)

		if not auth_response.status_code in [200,201]:
			raise Exception("Not a success response")

		response_data = auth_response.json()
		return response_data

# Shopify acts as a channel through which all the request to the Shopify will get served
class Shopify(Baseclass):
	'''
	Router to Shopify, all the request routes through here
	'''

	@classmethod
	def get_product_list(cls):

		url = SHOPIFY_URL + GET_PRODUCT_LIST
		response = cls.make_request(url, 'GET')
		return response

	@classmethod
	def create_an_order(cls, data):

		url = SHOPIFY_URL + CREATE_ORDER
		response = cls.make_request(url, 'POST', data)
		return response

