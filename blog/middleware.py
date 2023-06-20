class AdditionalDataMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.additional_data = {
            'user': request.user,
        }

        response = self.get_response(request)

        return response


# Пример обработки user-а в request-е

# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         additional_data = request.additional_data
#         user = additional_data['user']
#         settings = additional_data['settings']
#
#         context = {
#             'user': user,
#             'settings': settings,
#         }
#
#         return render(request, 'my_template.html', context)
