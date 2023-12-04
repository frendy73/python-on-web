from django.shortcuts import render
from .forms import UserForm

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return render(request, 'user_form_success.html', {'name': name, 'age': age})
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})
