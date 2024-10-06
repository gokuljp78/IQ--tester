from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User,auth
from .models import question,profile
import random

# Create your views here.

# home or start unction
def home(request):
    return render(request, 'index.html')


# Login function new user
def signin(request):
    print('hello',request)
    if request.method == 'POST':
        user = request.POST['user']
        name = request.POST['name']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            if User.objects.filter(username = user).exists():
                return render(request,'signin.html',{'users':"user exist"})
            else:
                u = User.objects.create_user(username =user,first_name = name,password = password)
                u.save()
                print(User.objects.all().values_list())
                return redirect(login)
        else:
            return render(request,'signin.html',{'password':'Password not same'})
    return render(request,'signin.html')


# Signin
def login(request):
    if request.method == "POST":
        user = request.POST['user']
        password = request.POST['password']
        check = auth.authenticate(username = user, password = password)
        print(user,password,check)
        print(User.objects.all().values_list())
        if check is not None:
            auth.login(request,check)
            print('login')
            return redirect(home)
        else:
            return render(request,'login.html',{'msg':'User or Password incorrect'})
    return render(request,'login.html')


# Logout 
def logout(request):
    auth.logout(request)
    return redirect(home)

# aptitude questions
def quest(request):
    Quest = question.objects.all().values()
    lists = []
    id = []
    i=0
    while (i<10):
        redoms = random.choice(Quest)
        if redoms['id'] not in id:
            id.append(redoms['id'])
            lists.append(redoms)
            i+=1
        
    if request.method == 'POST':
        ans = request.POST['answer']
    print(id)
    return render(request,'question.html',{'qt':lists,'id':id})

# Score calculation
# scores = []
# def score(sc):
#     score = 251.2*(sc/10)
#     score1 = 251.2 - score
#     scores.append(score1)
#     return scores

def calculate(request):
    scores = []
    ans = request.POST['answer']
    ans=ans.split(',')
    counts = ans.count('t')                   #7
    score = 251.2*(counts/10)                #251.2*0.7  = 175.84
    score1 = 251.2 - score                  # 75.
    # scores.append(score1)       
    
    if profile.objects.filter(user = request.user).exists():
        print('true')
        profiles = profile.objects.filter(user = request.user)
        # Attempts
        attem = profiles.values('attempts')[0]['attempts']
        attem +=1
        print('attempts',attem) 
        # Score
        pre_score = profiles.values('scores')[0]['scores']            #[{'scores':'7'}]  or [{'scores':'7,2,2'}]
        
        # score for previous circle
        # score = 251.2*(int(pre_score[len(pre_score)-1])/10)                # 7,2,2  last
        # score1 = 251.2 - score                                           # 75.
        # scores.append(score1) 

        pre_score += ','+str(counts)                                # '7'+','+'2' =  '7,2'    new is 2
        print('score',pre_score)
        profiles.update(attempts=attem,scores=pre_score)     #update db for score & attem
    else:
        print('false')
        profiles = profile.objects.create(user = request.user)
        profiles.attempts = 1
        profiles.scores =counts
        profiles.save()
    print(scores)
    
    return render(request,'percentage.html',{'score':score*10,'score1':score1*10,'per':counts*10 })