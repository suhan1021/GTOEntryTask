from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Developer
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.decorators import login_required


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['contact', 'g_plus', 'profile']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


def index(request):
    developer_list = Developer.objects.all()
    paginator = Paginator(developer_list, 5)
    page = request.GET.get('page')
    try:
        developers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        developers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        developers = paginator.page(paginator.num_pages)
    is_authenticated = request.user.is_authenticated()
    username = request.user.username if is_authenticated else None
    return render(request, 'developersite/index.html', {
        'is_authenticated': is_authenticated,
        'developers': developers,
        'username': username,
    })


# @login_required
def edit(request, developer_id):
    is_authenticated = request.user.is_authenticated()
    if is_authenticated:
        developer = get_object_or_404(Developer, pk=developer_id)
        user = developer.user
        if user == request.user:
            if request.method == 'GET':
                user_form = UserForm(instance=user)
                dev_form = DeveloperForm(instance=developer)
            elif request.method == 'POST':
                user_form = UserForm(request.POST, instance=user)
                dev_form = DeveloperForm(request.POST, request.FILES, instance=developer)
                if user_form.is_valid() and dev_form.is_valid():
                    user_form.save()
                    dev_form.save()
                    return redirect(reverse('developersite:index'))
                else:
                    print user_form.errors
                    print dev_form.errors
            return render(request, 'developersite/edit.html', {
                'is_authenticated': is_authenticated,
                'is_authorized': True,
                'user_form': user_form,
                'dev_form': dev_form,
            })
    return render(request, 'developersite/edit.html', {
        'is_authenticated': is_authenticated,
        'is_authorized': False,
        'error_message': 'You are not authorized to access this page.',
    })


