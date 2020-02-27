import os
import json
import pandas
import pickle
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class View:
    @csrf_exempt
    def get_predictions(self, request):
        if request.method == 'POST':
            input_data = json.loads(request.body.decode('utf-8'))
            input_data = pandas.DataFrame(input_data['objects'])
            model_file_path = os.path.join(settings.MODEL_PATH, settings.MODEL_NAME)
            model = pickle.load(open(model_file_path, 'rb'))
            predictions = model['Model'].predict(input_data)
            predictions = {"Predictions": [{"Gender": gender} for gender in predictions]}
            return JsonResponse(predictions)
    
