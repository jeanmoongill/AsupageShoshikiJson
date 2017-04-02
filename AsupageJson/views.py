from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Soshiki, UserInfo


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

            #save session in request

        else:

            context = {'login_error': 'please input a correct ID and PW'}
            return render(request, 'index.html', context=context)



#log out
def logout_view(request):
    '''
    :param request:
    :return: HttpResponse to login page
    '''

    #remove session
    logout(request)
    #redirect to login
    return render(request, template_name='index.html')




#top page
def to_top(request):
    '''

    :param request:
    :return: HttpResponse to top page
    '''


    if request.method == "POST":

        #get soshiki code from post
        soshiki_code = request.POST.get('soshikiCode', None)

        context = {}

        if soshiki_code:
            #get user info from db

            soshikiInfo = Soshiki.objects.get(is_active=1, code=soshiki_code)

            soshiki_id = soshikiInfo.id
            soshiki_name = soshikiInfo.name

            userInfo = UserInfo.objects.filter(soshiki = soshiki_id,
                                               is_active = 1)

            context['soshikiName'] = soshiki_name

        else:
            # get data from user_info
            userInfo = UserInfo.objects.filter(is_active=1)




        #get soshiki Info from database
        soshiki_list = Soshiki.objects.filter(is_active = 1)

        #add soshiki to dic
        context['Soshikis'] = soshiki_list
        context['UserInfo'] = userInfo

        return render(request, template_name='shoshiki.html', context=context)

    else:
        raise PermissionDenied
