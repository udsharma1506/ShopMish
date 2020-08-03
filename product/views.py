from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse, HttpResponseRedirect, HttpResponse


from .resolve import get_product, create_order

# Create your views here.

# View Function to support the API call
class GetProductList(View):

	def get(self, request):

		response = get_product('shopify')

		return JsonResponse(data={"products": response})


# View Function to support the API call
class CreateOrder(View):

	def post(self, request):

		data = request.POST.dict()
		response = create_order('shopify',data)
		return JsonResponse(data={"products": response})
