from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404
)
import os
from app.models import User, Profile
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, DeleteView, UpdateView,
)
from django.urls import reverse_lazy
from app.forms import UserEditForm, UserCreateForm, ProfileEditForm, ProfileCreateForm
from django.core.files.storage import FileSystemStorage


# list of users
class ListUserView(ListView):
    model = User
    template_name = 'app/users/list.html'
    context_object_name = 'users'

    queryset = User.objects\
        .select_related('profile')\
        .order_by('-id', 'first_name', 'last_name')

    extra_context = {'page': 'users'}


# detail of user
class DetailUserView(DetailView):
    model = User
    template_name = 'app/users/detail.html'
    context_object_name = 'user'

    queryset = User.objects.select_related('profile')

    extra_context = {'page': 'users'}


# edit user
class EditUserViewNew(TemplateView):
    model = User
    template_name = 'app/users/edit.html'
    success_url = reverse_lazy('app:users')

    context_object_name = 'user'
    queryset = User.objects.select_related('profile')

    extra_context = {'page': 'users'}


class EditUserView(TemplateView):
    template_name = 'app/users/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # data
        id = kwargs['pk']
        user = get_object_or_404(User, id=id)

        # return
        context['page'] = 'users'
        context['user'] = user
        context['form'] = UserEditForm(instance=user)
        context['form_profile'] = ProfileEditForm(instance=user.profile)

        return context

    def post(self, request, pk, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(User, id=pk)
        form = UserEditForm(request.POST, request.FILES, instance=user)
        form_profile = ProfileEditForm(request.POST, instance=user.profile)

        # старое и новое фото
        photo_old = None
        photo_new = None

        if user.photo:
            photo_old = user.photo.path

        if form.files.get('photo', None) is not None:
            photo_new = 'photo/' + str(form.files.get('photo', None))

        # сохранить
        try:
            if form.is_valid():
                # профиль есть
                if user.profile is not None:
                    # обновить юзера
                    form.save()

                    # обновить профиль
                    Profile.objects\
                        .filter(id=user.profile.id)\
                        .update(
                            department=form.data['department'],
                            secure_code=form.data['secure_code'],
                            status=form.data['status'],
                        )

                # профиля нет
                elif user.profile is None and form.data['department']:
                    # создать профиль
                    profile = Profile.objects.create(
                        department=form.data.get('department'),
                        secure_code=form.data.get('secure_code'),
                        status=form.data.get('status'),
                    )

                    # обновить юзера
                    user.profile = profile
                    user.save(update_fields=['profile'])

                # удалить старое фото если выбрано новое фото
                if photo_old is not None and photo_new is not None and photo_old != photo_new:
                    if os.path.isfile(photo_old):
                        os.remove(photo_old)

                return redirect(reverse('app:users'))

        except Exception as error:
            context['error'] = str(error)

        context['form'] = form
        context['form_profile'] = form_profile

        return render(request, self.template_name, context)


# create user
class CreateUserViewNew(CreateView):
    model = User
    template_name = 'app/users/create.html'
    success_url = reverse_lazy('app:users')

    context_object_name = 'user'
    queryset = User.objects.select_related('profile')

    extra_context = {'page': 'users'}
    fields = ['first_name', 'last_name', 'email', 'photo']


class CreateUserView(TemplateView):
    template_name = 'app/users/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # return data
        context['page'] = 'users'
        context['form'] = UserCreateForm()
        context['form_profile'] = ProfileCreateForm()

        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        form = UserCreateForm(request.POST, request.FILES)
        form_profile = ProfileCreateForm(request.POST)

        try:
            if form.is_valid():
                # создать профиль
                profile = Profile.objects.create(
                    department=form_profile.data.get('department'),
                    secure_code=form_profile.data.get('secure_code'),
                    status=form_profile.data.get('status'),
                )

                # создать юзера
                photo = None
                if request.FILES['photo'] is not None:
                    photo = 'photo/' + request.FILES['photo'].name

                User.objects.create(
                    first_name=form.data.get('first_name'),
                    last_name=form.data.get('last_name'),
                    email=form.data.get('email'),
                    profile=profile,
                    photo=photo,
                )

                # сохранить фото
                if photo is not None:
                    fs = FileSystemStorage()
                    fs.save(photo, request.FILES['photo'])

                return redirect(reverse('app:users'))

        except Exception as error:
            context['error'] = str(error)

        context['form'] = form
        context['form_profile'] = form_profile

        return render(request, self.template_name, context)


# remove user
class RemoveUserView(DeleteView):
    model = User
    template_name = 'app/users/remove.html'
    success_url = reverse_lazy('app:users')

    context_object_name = 'user'
    queryset = User.objects.select_related('profile')

    extra_context = {'page': 'users'}


# about
class AboutView(TemplateView):
    template_name = 'app/about.html'
    extra_context = {'page': 'about'}