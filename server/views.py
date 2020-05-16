from predict.views import Loader
from rest_framework import generics
from django.conf import settings
from django.shortcuts import HttpResponse


class GetSalaryAPIView(generics.GenericAPIView):

    def post(self, request):

        if request.method == 'POST':
            data = request.data

            # Extract age from the post request body
            exp = float(data['exp'])

            # load the salary predictor
            salary = Loader(settings.BASE_DIR + "/predict/model.sav", [[exp]]).load()

            # return a simple HTTP Response
            return HttpResponse(salary)

        else:
            return 'Failed to get model'
