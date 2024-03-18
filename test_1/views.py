from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test_api(request):
    context = {
        'integer': 100,
        'string': 'hello world',
        'boolean': True,
        'list': [1, 2, 3]
    }
    return Response(data=context)