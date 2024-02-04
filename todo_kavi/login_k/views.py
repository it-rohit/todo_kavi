from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Register
from myapp.models import Task,TeamMember,ChatMessage
# Create your views here.



def login (request,methods=["GET","POST"]):
    # data = Register.objects.get(username=username) 
    # id = data.id 
    if request.method == "POST":    
        username = request.POST["username"] 
        password = request.POST["password"]
        # print(password)
        data= Register.objects.get(username=username) 
        # print(data)
        # id = data.id 
        # print(id)
        
        if username == data.username and password == data.password :
            team_member_instance = TeamMember.objects.get(name=username)
            print((team_member_instance)) 

            # Retrieve tasks assigned to the specific TeamMember

            data_a = Task.objects.filter(assigned_members=team_member_instance)
            print(data_a)

            # Now, you can access the tasks assigned to the specific TeamMember
            # for task in tasks_assigned_to_member:
            #     print(task.title)        
            context= {
                "data_html" : data_a,"member":team_member_instance
            }

            return render (request,"tasks.html",context)
        return HttpResponse ("username or password in valid")
    
    return render(request,"login.html")


def taskdetails(request,id,title,methods=["GET","POST"]):
    # print("hajjk")
    print(title)
    v=title
    a=TeamMember.objects.get(name="dinesh")
    b=Task.objects.get(id=id)
    if request.method=="POST":
        # d_username=request.POST.get("username")
        # d_id=request.POST.get("room_id")
        d__message=request.POST.get("message")
        new_message=ChatMessage.objects.create(sender=a,task=b,message=d__message)
        new_message.save()
        return redirect("taskdetails",id=id)

        # print(data)
    x=User.objects.get(is_superuser=True)  
    # a=TeamMember.objects.get(name="kavi")
    # b=Task.objects.get(id=id)
    # print(b.id)
    # print(a.id)
    
    task1=ChatMessage.objects.filter(Q(sender=a.id) & Q(task=b.id) )
    # print(task1)
    # task1=ChatMessage.objects.filter(sender=a) 
    # for i in task1:
    #     print(i.task.id)
    #     h=i
    context={"msg":task1,"name":a,"user":x,}
    return render(request,"chat.html",context)
        