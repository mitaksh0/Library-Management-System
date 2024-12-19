from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import tasks

@api_view(['GET', 'POST'])
def manage_reports(request):

    if request.method == 'GET':
        #return report
        data = tasks.read_report('latest')
        return Response(data)

    elif request.method == 'POST':
        #start process
        tasks.store_report.delay()
        return Response({
            "message": "report scan started"
        })
    
@api_view(['GET'])
def list_all_reports(request):
    data = tasks.read_report('all')
    return Response(data)
