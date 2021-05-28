from django.views.generic import View
from django.http import HttpResponse

class ConfirmationSample(View):
    def get(self, request):
        return HttpResponse(
            "Helloword!"
        )

# Create your views here.
