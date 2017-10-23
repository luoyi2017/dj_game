from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# from .models import Admin_user
from game_server.models import Player, Player_gold_log

import datetime

def admin_login(request):
    if request.method == 'GET':
        return render(request,'admin_login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username',None)
            password = form.cleaned_data.get('password',None)
            remember = form.cleaned_data.get('remember', None)
            # user = Admin_user.objects.filter(username=username, password=password)
            user = authenticate(username=username, password=password)
            if user:
                # 登陆，自定义的login函数不要和django自带的login重名
                login(request, user)
                # 判断如果有remember,那么说明需要记住,
                # 使用None将使用settings.py中SESSION_COOKIE_AGE指定的值,
                # 这个值默认是14天
                if remember:
                    request.session.set_expiry(None)
                else:
                    # 浏览器一旦关闭,session就会过期
                    request.session.set_expiry(0)
                nexturl = request.GET.get('next')
                if nexturl:
                    return redirect(nexturl)
                else:
                    return redirect(reverse('index'))
            else:
                return render(request,'admin_login.html',{'error':'用户名或密码错误!'})
        else:
            return render(request,'admin_login.html',{'error':form.get_error()})


# 登出
def admin_logout(request):
    logout(request)
    return redirect(reverse('admin_login'))


@login_required
def index(request):
    playerlist = Player.objects.all().order_by('-regtime')
    goldlist = Player_gold_log.objects.all().order_by('-gold_change_time')
    return render(request, 'index.html', context={'playerlist':playerlist, 'goldlist':goldlist,})

@login_required
def filter_regtime(request):
    yf = request.POST.get('year_from', None)
    mf = request.POST.get('month_from', None)
    df = request.POST.get('day_from', None)
    yt = request.POST.get('year_to', None)
    mt = request.POST.get('month_to', None)
    dt = request.POST.get('day_to', None)
    if yf and mf and df and yt and mt and dt:
        date_from = datetime.datetime(int(yf), int(mf), int(df), 0, 0)
        date_to = datetime.datetime(int(yt), int(mt), int(dt), 23, 59)
        # __range 在...范围内
        reglist = Player.objects.filter(regtime__range=(date_from, date_to)).order_by('-regtime')
    else:
        reglist = Player.objects.all().order_by('-regtime')
    return render(request, 'filter_regtime.html', context={'reglist': reglist, })

@login_required
def filter_player(request):
    playerid = request.POST.get('playerid', None)
    yf = request.POST.get('year_from', None)
    mf = request.POST.get('month_from', None)
    df = request.POST.get('day_from', None)
    yt = request.POST.get('year_to', None)
    mt = request.POST.get('month_to', None)
    dt = request.POST.get('day_to', None)

    if playerid:
        if yf and mf and df and yt and mt and dt:
            date_from = datetime.datetime(int(yf), int(mf), int(df), 0, 0)
            date_to = datetime.datetime(int(yt), int(mt), int(dt), 23, 59)
            # __range 在...范围内
            goldfilter = Player_gold_log.objects.filter(playerid=playerid, gold_change_time__range=(date_from, date_to))
        else:
            goldfilter = Player_gold_log.objects.filter(playerid=playerid)
        return render(request, 'filter_player.html', context={'goldfilter': goldfilter, })
    else:
        pass