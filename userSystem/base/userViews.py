from contextlib import nullcontext
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from base.models import CustomUser, Request, Recommendation_letter, Lesson
from django.core.mail import send_mail

def student_home(request):
    requests=Request.objects.filter(sender_id = request.user.id)
    return render(request,"student_templates/student_home.html",{"requests":requests})

def teacher_home(request):
    requests=Request.objects.filter(receiver_id = request.user.id)
    return render(request,"teacher_templates/teacher_home.html",{"requests":requests})

def add_request(request):
    user = request.user
    teachers = CustomUser.objects.filter(user_type="2")
    return render(request,"student_templates/add_request.html", {"teachers":teachers,"user":user})


def add_request_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        purpose=request.POST.get("purpose")
        receiver_id=request.POST.get("teacher_id")
        sender_id= request.POST.get("sender_id")
        status="pending"

        name1 = request.POST.get("name1")
        name2 = request.POST.get("name2")
        grade1 = request.POST.get("grade1")
        grade2 = request.POST.get("grade2")
        semester1 = request.POST.get("semester1")
        semester2 = request.POST.get("semester2")


        try:
            req=Request(
                purpose = purpose,
                receiver_id= receiver_id,
                sender_id= request.user.id ,
                status = status)
            req.save()

            lesson1=Lesson(
                name = name1,
                grade = grade1,
                semester = semester1,
                request_id = req.id
            )
            if name1!="" or grade1!="" or semester1!="" : lesson1.save()

            lesson2=Lesson(
                name = name2,
                grade = grade2,
                semester = semester2,
                request_id = req.id
            )
            if name2!="" or grade2!="" or semester2!="" : lesson2.save()

            messages.success(request,"Successfully Added Application")
            return HttpResponseRedirect(reverse("student_home"))
        except:
            messages.error(request,"Failed to Add Application" )
            return HttpResponseRedirect(reverse("add_request"))  


def view_request(request, request_id) :
    r = Request.objects.get(id = request_id)
    lessons = Lesson.objects.filter(request_id = r.id)
    return render(request,"teacher_templates/view_request.html",{"request":r, "lessons":lessons})

def accept_request(request,request_id ):
    r = Request.objects.get(id = request_id)
    r.status = "Accepted"
    r.save()
    return HttpResponseRedirect(reverse("teacher_home")) 

def reject_request(request,request_id ):
    r = Request.objects.get(id = request_id)
    r.status = "Rejected"
    r.save()
    return HttpResponseRedirect(reverse("teacher_home")) 


def add_recommendation_letter(request):
    user = request.user
    requests = Request.objects.all()
    return render(request,"teacher_templates/add_recommendation_letter.html", {"requests":requests,"user":user})

def add_recommendation_letter_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        response=request.POST.get("text")
        request_id = request.POST.get("id")

        try:
            letter=Recommendation_letter(
                text = response,
                request_id = request_id
            )
            letter.save()

            send_mail(
                'Recommendation letter has been sent.',
                'For request:'+ str(request_id)+" Response:"+str(response),
                request.user.email,
                ['it@hua.gr'],
                fail_silently=False,
            )
 
            messages.success(request,"Successfully Added Application")
            return HttpResponseRedirect(reverse("teacher_home"))
        except:
            messages.error(request,"Failed to Add Application" )
            return HttpResponseRedirect(reverse("add_recommendation_letter"))  

def view_recommendation_letter(request) :
    requests = Request.objects.filter(sender_id = request.user.id)
    letters = []
    
    for(i=0 ; i<requests.len(); i++) {
     if (requests[i].status = 'pending') {
         requests.pop(i);
     }
    }

    for x in requests: letters.append(Recommendation_letter.objects.get(request_id = x.id))

    return render(request,"student_templates/view_recommendation_letter.html",{"letters":letters} )
