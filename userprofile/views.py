import os
from django.urls import reverse
from django.conf import settings as django_settings
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from .forms import ProfileForm, ChangePasswordForm
from .models import Profile

from PIL import Image



# @login_required
# def profile(request, username):
#     profile = get_object_or_404(User, username=username)
    
#     return render(request, 'profile/user.html', {
#         'profile': profile,
        
#         })

@login_required
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.phone = form.cleaned_data.get('phone')

            user.save()
            return redirect('/')

    else:
        form = ProfileForm(instance=user, initial={
            'user':request.user,
            'age': user.profile.age,
            'location': user.profile.location,
            'gender':user.profile.gender,
            'phone':user.profile.phone,
            'bio':user.profile.bio
            
            })
    return render(request, 'profile/edit_profile.html', {'form': form})

@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 'Your password was successfully changed.')
            return redirect('profilesettings')

    else:
        form = ChangePasswordForm(instance=user)

    return render(request, 'password.html', {'form': form})




@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True

    except Exception:
        pass

    return render(request, 'picture.html',
                  {'uploaded_picture': uploaded_picture})


@login_required
def upload_picture(request):
    try:
        profile_pictures = django_settings.MEDIA_ROOT + '/profile_pictures/'
        if not os.path.exists(profile_pictures):
            os.makedirs(profile_pictures)
        f = request.FILES['picture']
        filename = profile_pictures + request.user.username + '_tmp.jpg'
        with open(filename, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        im = Image.open(filename)
        width, height = im.size
        if width > 350:
            new_width = 350
            new_height = (height * 350) / width
            new_size = new_width, new_height
            im.thumbnail(new_size, Image.ANTIALIAS)
            im.save(filename)

        return redirect('/profile/')

    except Exception as e:
        print(e)
        return redirect('/profile/')

# crooping the image
# @login_required
# def save_uploaded_picture(request):
#     try:
#         x = int(request.POST.get('x'))
#         y = int(request.POST.get('y'))
#         w = int(request.POST.get('w'))
#         h = int(request.POST.get('h'))
#         tmp_filename = django_settings.MEDIA_ROOT + '/profile_pictures/' +\
#             request.user.username + '_tmp.jpg'
#         filename = django_settings.MEDIA_ROOT + '/profile_pictures/' +\
#             request.user.username + '.jpg'
#         im = Image.open(tmp_filename)
#         cropped_im = im.crop((x, y, w+x, h+y))
#         cropped_im.thumbnail((200, 200), Image.ANTIALIAS)
#         cropped_im.save(filename)
#         os.remove(tmp_filename)

#     except Exception:
#         pass

#     return redirect('/profile/settings/')   

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.phone = form.cleaned_data.get('phone')

            user.save()
            return redirect('/')

    else:
        form = ProfileForm(instance=user, initial={
            'user':request.user,
            'age': user.profile.age,
            'location': user.profile.location,
            'gender':user.profile.gender,
            'phone':user.profile.phone,
            'bio':user.profile.bio
            
            })
    return render(request, 'profile/user.html', {'form': form})
