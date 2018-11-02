from django.shortcuts import render

from .forms import AccountUserForm


def account_login(request):
    form = AccountUserForm()

    if request.method=='POST':
        print('*'*50)
        print(request.POST)
        print('*' * 50)

    return render(request, 'accounts/login.html', {'form': form})