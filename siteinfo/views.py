from django.shortcuts import render



def index_view(request):
    return render(request, 'siteinfo/index.html', {})
def groups_view(request):
    return render(request, 'siteinfo/groups.html', {})