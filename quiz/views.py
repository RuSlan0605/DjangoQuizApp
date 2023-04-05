from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import CreateUserForm
from .models import Quiz


def page_list(request):
    if request.method == 'POST':
        questions = Quiz.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for question in questions:
            total += 1
            if question.answer == question.op1:
                score += 10
                correct += 1
            elif question.answer == question.op2:
                score += 10
                correct += 1
            elif question.answer == question.op3:
                score += 10
                correct += 1
            elif question.answer == question.op4:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10)*100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz/results.html',context)
    else:
        questions = Quiz.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz/page_list.html',context) 

def register(request):
    if request.user.is_authenticated:
        return redirect('page_list') 
    else: 
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'registrations/register.html', context)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('page_list')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password1=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        context={}
        return render(request,'registrations/login.html',context)

def logout(request):
    logout(request)
    return redirect('page_list')

