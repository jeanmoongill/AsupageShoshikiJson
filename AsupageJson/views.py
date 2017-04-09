from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Soshiki, UserInfo, TitleInfo



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
            return redirect(to_top)

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
        title_code = request.POST.get('titleid', None)

        context = {}

        #while click button is clicked
        if "clear" in request.POST:
            userInfoList = UserInfo.objects.filter(is_active=1)

            userInfo = []

            for user in userInfoList:
                userInfo.append({"id": user.id,
                                 "name":user.name,
                                 "title":user.title.name,
                                 "soshiki":user.soshiki.name,
                                 "create_time":user.create_time},)


            context['UserInfo'] = userInfo

        else:

            query_string = '''
                select

                  user_info.id,
                  user_info.name,
                  title_info.name,
                  soshiki.name,
                  user_info.create_time

                from user_info

                Left JOIN soshiki
                ON user_info.soshiki = soshiki.id
                Left Join title_info
                On user_info.title = title_info.id

                WHERE user_info.is_active = 1
                AND soshiki.is_active = 1
                AND title_info.is_active = 1
            '''

            param = []

            if soshiki_code and soshiki_code is not 0:

                query_string += " AND soshiki = %s "
                param.append(soshiki_code)


            if title_code and title_code is not 0:
                query_string += " AND title = %s"
                param.append(title_code)

            cursor = connection.cursor()
            cursor.execute(query_string, param)
            userInfo = cursor.fetchall()

            userInfoList = []

            #userInfo to list
            for user in userInfo:
                userInfoList.append({"id":user[0],
                                     "name":user[1],
                                     "title":user[2],
                                     "soshiki":user[3],
                                     "create_time":user[4]},)

            context['UserInfo'] = userInfoList

            soshiki_name = Soshiki.objects.get(is_active=1, code=soshiki_code)
            title_name = TitleInfo.objects.get(is_active=1, id=title_code)
            context['soshikiName'] = soshiki_name
            context['titleName'] = title_name

        #get soshiki Info from database
        soshiki_list = Soshiki.objects.filter(is_active = 1)
        titleInfo = TitleInfo.objects.filter(is_active=1)

        #add soshiki to dic
        context['Soshikis'] = soshiki_list
        context['TitleInfo'] = titleInfo



        return render(request, template_name='shoshiki.html', context=context)

    else:

        context = {}

        soshiki_list = Soshiki.objects.filter(is_active=1)
        userInfoList = UserInfo.objects.filter(is_active=1)
        titleInfo = TitleInfo.objects.filter(is_active=1)

        userInfo = []

        for user in userInfoList:
            userInfo.append({"id": user.id,
                             "name": user.name,
                             "title": user.title.name,
                             "soshiki": user.soshiki.name,
                             "create_time": user.create_time}, )


        context['Soshikis'] = soshiki_list
        context['UserInfo'] = userInfo
        context['TitleInfo'] = titleInfo

        return render(request, template_name='shoshiki.html', context=context)
