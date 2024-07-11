def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'user_management/login.html', {'error': 'Invalid username or password'})
    return render(request, 'user_management/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')