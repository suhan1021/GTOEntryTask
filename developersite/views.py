from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Developer
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.decorators import login_required


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['contact', 'g_plus', 'profile']
        labels = {
        	'contact': _('Phone Number'),
        	'g_plus': _('G+ ID'),
        	'profile': _('Profile Image')
        }
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

def index(request):
    developers = Developer.objects.all()
    is_authenticated = request.user.is_authenticated()
    username = request.user.username if is_authenticated else None
    return render(request, 'developersite/index.html', {
        'is_authenticated': is_authenticated,
        'developers': developers,
        'username': username,
    })

# @login_required
def edit(request, developer_id):
    if request.user.is_authenticated():
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
                'is_authenticated': True,
                'user_form': user_form,
                'dev_form': dev_form,
            })
    return render(request, 'developersite/edit.html', {
        'is_authenticated': False,
        'error_message': 'You are not authorized to access this page.',
    })
    
        
