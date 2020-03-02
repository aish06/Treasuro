from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.utils import timezone

from .forms import RegisterForm,LoginForm

from user_detail.models import Profile
from verify.models import verification
from Questions.models import question_model

from hitcounter.models import hit
import random

User=get_user_model()

def index(request):
    hit1=hit.objects.get(name='archit')
    hit1.no=hit1.no+1
    hit1.save()
    return render(request,'index.html',{})


def login_page(request):
    hit1=hit.objects.get(name='archit')
    hit1.no=hit1.no+1
    hit1.save()
    context={
    'login':False
    }
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            pro=Profile.objects.get(email=username)
            if pro.rules:
                if request.GET.get('q')!=None:
                    return redirect('/dashboard?q='+request.GET.get('q'))
                else:
                    return redirect('/dashboard')
            else:
                return redirect('/rules')
        else:
            context['login']=True
    return render(request,'login.html',context)



def register_page(request):
    hit1=hit.objects.get(name='archit')
    hit1.no=hit1.no+1
    hit1.save()
    context = {
        "bool": False,
        "exist":False
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        zealid=request.POST.get("zealid")
        password = request.POST.get("password")
        objs=verification.objects.filter(zealid=zealid)
        if objs.count()<1:
            #objs.first().delete()
            try:
                new_user=User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )
            except:
                context['exist']=True
                return render(request,"signup.html",context)    
            new=Profile.objects.create(
                    leader=new_user,
                    name=name,
                    email=email,
                    number=contact,
                    rules=True,
                    lastsub=timezone.now(),
                    zealid=zealid,
                    password=password
                )
            new_zeal=verification.objects.create(
                zealid=zealid
                )
            #objs.first().delete()
            new.save()
            login(request,new_user)

            return redirect('/rules')
        else:
            context = {
                "bool": True
            }
    return render(request, "signup.html", context)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/leaderboard')

def leaderboard(request):
    hit1=hit.objects.get(name='archit')
    hit1.no=hit1.no+1
    hit1.save()
    objs=Profile.objects.all()
    context={
        "object":objs,
    }
    if request.user.is_authenticated:
        obj=Profile.objects.filter(email=request.user.username).first()
        count=0
        for i in objs:
            count=count+1
            if i.email==obj.email:
                break
        context={
            "hg":True,
            "point":obj.points,
            "object":objs,
            "rank":count,
        }

    return render(request,'leaderboard.html',context)


def question(request):
    hit1=hit.objects.get(name='archit')
    hit1.no=hit1.no+1
    hit1.save()
    if request.user.is_authenticated:
        usr=Profile.objects.get(email=request.user.username)
        if not(usr.freeze):
            if usr.level>25:
                return render(request,'completed.html',{})
            objs=question_model.objects.get(level=usr.level)
            context={
                'level':usr.level,
                'title':objs.title,
                'desc':objs.description,
                'wrong':False,
                'obj':objs,
                'correct':False,             
                #'again':False,
                #'attempts':usr.attempts,
            }
            if request.GET.get('q')!=None:
                ans=objs.correct_ans
                ans1=request.GET.get('q')
                if (ans.lower())==(ans1.lower()):
                    usr.level=usr.level+1
                    usr.points=usr.points+10
                    usr.lastsub=timezone.now()
                    usr.poi=usr.poi+"Qus"+str(usr.level-1)+" - 10\n"
                    usr.tuh=usr.tuh+"Qus"+str(usr.level-1)+" - "+str(timezone.now().time())+",\n"
                    usr.save()
                    if usr.level<=objs.top_level:
                        objs=question_model.objects.get(level=usr.level)
                        context={
                            'level':usr.level,
                            'title':objs.title,
                            'desc':objs.description,
                            'obj':objs,
                            'correct':True,
                            #'attempts':usr.attempts,
                        }
                    else:
                        return render(request,'completed.html',{})
                else:
                    context['wrong']=True
                    #usr.attempts=usr.attempts+1
                    #if usr.attempts>=100:
                    #    usr.freeze=True
                    #    usr.save()
                    #    return render(request,'freeze.html',{})
                    #usr.save()
                    #context['attempts']=usr.attempts
            return render(request,"dashboard.html",context)
        else:
            return render(request,"freeze.html",{})
    else:
        if request.GET.get('q')!=None:
            return redirect('/login?q='+request.GET.get('q'))
        else:
            return redirect('/')

def rules(request):
    hit1=hit.objects.filter(name='archit').first()
    hit1.no=hit1.no+1
    hit1.save()
    return render(request,"rules.html",{})   

def admin_view(request):
    return render(request,"wrong.html",{}) 

#def wind(request):
#    return render(request,"completed.html",{})



def soon_view(request):
    return render(request,"soon.html",{})


def comp(request):
    return render(request,"completed.html",{})
