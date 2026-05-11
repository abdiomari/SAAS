import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "queryset": page_qs.count(),
        "total_visit_count": qs.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


VALID_CODE = "123"


def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get("protected_page_allowed") or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            request.session["protected_page_allowed"] = 1
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})
