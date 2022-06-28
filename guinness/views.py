from django.shortcuts import render

# Create your views here.
def get_guinness_world_records(request):
    return render(request, 'guinness/guinnesworldrecords.html')