from django.utils import timezone
from rest_framework.permissions import AllowAny

from taxonomy.models import Term, TaxonomyType
from django.contrib import messages
from django.shortcuts import render

from .forms import ArticleForm, ReportForm
from .models import Content, ContentType, ContentRelation, ContentRealtionType

from .serializers import ContentSerializer, ContentCreateSerializer
from .models import Content
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, GenericAPIView
from taxonomy.models import Term
from django.contrib.auth.models import AnonymousUser as NOT_LOGGED_IN
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


class ContentListView(ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = [AllowAny]
    queryset = Content.objects.all()


class ContentRetrieveView(RetrieveAPIView):
    serializer_class = ContentSerializer
    permission_classes = [AllowAny]
    queryset = Content.objects.all()


class ContentCreateView(CreateAPIView):
    serializer_class = ContentCreateSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        # subject_str = serializer.validated_data['subject']
        #
        # # get subject
        # try:
        #     subject = Term.objects.get(title=subject_str)
        # except Term.DoesNotExist:
        #     subject = Term(title=subject_str)
        #     subject.save()
        # serializer.save(author=current_user,subject=subject)
        serializer.save(author=current_user)


@api_view(['PUT'])
def ContentUpdateView(request, pk):
    instance = get_object_or_404(Content, pk=pk)
    data = ContentSerializer(instance=instance)
    if request.method == 'PUT':
        for item in request.data:
            if hasattr(instance, item):
                setattr(instance, item, request.data[item])
        instance.save()
        new_data = ContentSerializer(instance=instance)
        return Response(new_data.data)
    return Response(data.data)


@api_view(['GET', 'DELETE'])
def ContentDelete(request, pk):
    instance = get_object_or_404(Content, pk=pk)
    data = ContentSerializer(instance=instance)
    if request.method == 'DELETE':
        instance.delete()
        return Response({'Object Deleted'})
    return Response(data.data)


### Old template view functions

def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        subject_title = form.cleaned_data.get('subject_title')
        subject = Term.objects.filter(title=subject_title)
        if subject.exists():
            subject = subject.first()
        else:
            subject = Term(
                title=subject_title,
                title_fa=subject_title,
                taxonomy_type=TaxonomyType.SUBJECT
            )
            subject.save()
        instance = Content(
            title=form.cleaned_data.get('title'),
            # image = form.cleaned_data.get('image'),
            content=form.cleaned_data.get('content'),
            # publish = form.cleaned_data.get('publish'),
            publish=timezone.now(),
            type=ContentType.ARTICLE,
            author=request.user,
        )
        instance.save()
        messages.success(request, "فرم با موفقیت ثبت شد", extra_tags='html_safe')
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": 'مقاله جدید',
        # "form_description" : ''
    }
    return render(request, "default_restricted_form.html", context)

### Old template view functions

def add_report(request):
    form = ReportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        subject_title = form.cleaned_data.get('subject_title')
        subject = Term.objects.filter(title=subject_title)
        if subject.exists():
            subject = subject.first()
        else:
            subject = Term(
                title=subject_title,
                title_fa=subject_title,
                taxonomy_type=TaxonomyType.LEARNING_FIELD
            )
            subject.save()
        instance = Content(
            title=form.cleaned_data.get('title'),
            # image = form.cleaned_data.get('image'),
            content=form.cleaned_data.get('content'),
            # publish = form.cleaned_data.get('publish'),
            publish=timezone.now(),
            type=ContentType.REPORT,
            author=request.user,
        )
        instance.save()
        messages.success(request, "فرم با موفقیت ثبت شد", extra_tags='html_safe')
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": 'گزارش جدید',
        # "form_description" : ''
    }
    return render(request, "default_restricted_form.html", context)
