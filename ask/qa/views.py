from django.http import HttpResponse


def test(request):

    print("DEBUG: {}".format(request.GET.get('name')))
    return HttpResponse('OK {}'.format(request.GET))
