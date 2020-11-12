from django.shortcuts import render
from app.models import User


# list of users
def index_view(request):
    users = User.objects.all()
    return render(request, 'app/index.html', {
        'users': users
    })


# user by id
def item_view(request, id):
    user = User.objects.get(id=id)
    return render(request, 'app/item.html', {
        'user': user
    })
