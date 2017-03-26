from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic.edit import FormView



class AccountLogin(FormView):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')


    def post(self, request, *args, **kwargs):
        #login
        username = request.POST['form-username']
        password = request.POST['form-password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, 'shoshiki.html')
        else:

            context = {'login_error': 'please input a correct ID and PW'}
            return render(request, 'index.html', context=context)



#top page
def to_top(request):


    return render(request, template_name='shoshiki.html')
