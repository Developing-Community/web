from django.utils import timezone

from taxonomy.models import Term, TaxonomyType
from django.contrib import messages
from django.shortcuts import render

from .forms import ArticleForm
from .models import Content, ContentType, ContentRelation, ContentRealtionType


def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        subject_title = form.cleaned_data.get('subject_title')
        subject = Term.objects.filter(title=subject_title)
        if subject.exists():
            subject = subject.first()
        else:
            subject = Term(
                title = subject_title,
                title_fa = subject_title,
                taxonomy_type = TaxonomyType.LEARNING_FIELD
            )
            subject.save()
        instance = Content(
            title = form.cleaned_data.get('title'),
            # image = form.cleaned_data.get('image'),
            content = form.cleaned_data.get('content'),
            # publish = form.cleaned_data.get('publish'),
            publish = timezone.now(),
            type = ContentType.ARTICLE,
            author = request.user,
        )
        instance.save()
        messages.success(request, "فرم با موفقیت ثبت شد", extra_tags='html_safe')
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title" : 'مقاله جدید',
        # "form_description" : ''
    }
    return render(request, "default_restricted_form.html", context)