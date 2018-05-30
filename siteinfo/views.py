from django.shortcuts import render



def index_view(request):
    return render(request, 'siteinfo/index.html', {})
def art_view(request):
    return render(request, 'siteinfo/art.html', {})