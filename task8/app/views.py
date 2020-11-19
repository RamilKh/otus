from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404
)
import os
from app.models import User, Profile
from django.views.generic import TemplateView, ListView, DetailView
from app.forms import UserEditForm, UserCreateForm, ProfileEditForm, ProfileCreateForm


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

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        q = super().get_queryset()
        return q.filter(id=pk).select_related('profile')

    extra_context = {'page': 'users'}


# edit user
class EditUserView(TemplateView):
    template_name = 'app/users/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # data
        id = kwargs['id']
        user = get_object_or_404(User, id=id)

        # return
        context['page'] = 'users'
        context['id'] = id
        context['user'] = user
        context['form'] = UserEditForm(instance=user)
        context['form_profile'] = ProfileEditForm(instance=user.profile)

        return context

    def post(self, request, id, **kwargs):
        context = super().get_context_data(**kwargs)

        user = get_object_or_404(User, id=id)
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
        context['id'] = id

        return render(request, self.template_name, context)


# create user
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

        form = UserCreateForm(request.POST)
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
                User.objects.create(
                    first_name=form.data.get('first_name'),
                    last_name=form.data.get('last_name'),
                    email=form.data.get('email'),
                    profile=profile,
                )

                return redirect(reverse('app:users'))

        except Exception as error:
            context['error'] = str(error)

        context['form'] = form
        context['form_profile'] = form_profile

        return render(request, self.template_name, context)


# remove user
class RemoveUserView(TemplateView):
    template_name = 'app/users/edit.html'

    def get(self, request, id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = id

        user = get_object_or_404(User, id=id)

        try:
            user.delete()
            if user.photo:
                if os.path.isfile(user.photo.path):
                    os.remove(user.photo.path)

            if user.profile is not None:
                user.profile.delete()

            return redirect(reverse('app:users'))

        except Exception as error:
            context['form'] = UserEditForm(instance=user)
            context['form_profile'] = ProfileEditForm(instance=user.profile)
            context['error'] = str(error)

        return render(request, self.template_name, context=context)


# about
class AboutView(TemplateView):
    template_name = 'app/about.html'
    extra_context = {'page': 'about'}