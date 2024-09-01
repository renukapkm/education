from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from .models import Course,Contacts,Registration,Reviews,Order,Wishlist,Dashregistration
from django.db import transaction
# Create your views here.
def index(request):
    revi=Reviews.objects.all()
    context={
        'revi':revi
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context,request))
def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render({},request))
def contact(request):
    if request.method == 'POST':
        conname = request.POST['contact_name']
        conemail = request.POST['contact_email']
        conmsg = request.POST['contact_message']
        

        contact =Contacts(con_name=conname,con_email = conemail,con_message=conmsg )
        
        contact.save()

    template = loader.get_template("contact.html")
    return HttpResponse(template.render({},request))
def course(request):
    co= Course.objects.all().values()
    context ={
        'co':co
    }
    template = loader.get_template("course.html")
    return HttpResponse(template.render(context,request))
# def details(request):
   
#     template = loader.get_template("details.html")
#     return HttpResponse(template.render())
def services(request):
    template = loader.get_template("services.html")
    return HttpResponse(template.render({},request))
def details(request,id):
    course=Course.objects.filter(id=id)
    context ={
        'course':course,
    }

    template = loader.get_template("details.html")
    return HttpResponse(template.render(context,request))
def login(request):
    if "user" in request.session:
        return HttpResponseRedirect("/course")
    if request.method == 'POST':
        logname = request.POST['log_name']
        logpassword = request.POST['log_password']
        log = Registration(reg_password = logpassword,reg_username = logname)  
        if log:
            request.session["user"]=logname
            return HttpResponseRedirect("/course")
        else:
            return HttpResponseRedirect("/contact")
    template = loader.get_template("login.html")
    return HttpResponse(template.render({},request))
def logout(request):
     if "user" in request.session:
        del request.session["user"]
        return HttpResponseRedirect("/login")
def registration(request):
    if "user" in request.session:
        return HttpResponseRedirect("/account")
    if request.method == 'POST':
        regemail = request.POST['reg_email']
        regpassword = request.POST['reg_passwd']
        reguser = request.POST['reg_usrname']
        regphnumber = request.POST['reg_ph']


        regi = Registration(reg_email = regemail,reg_password = regpassword,reg_username = reguser,reg_phnum = regphnumber)  
        regi.save()

    template=loader.get_template("registration.html")
    return HttpResponse(template.render({},request))


# dashboard pages 

def dashboardlogin(request):
    
    if "adminuser" not in request.session:
       
        
       if request.method == 'POST':
        log_user = request.POST['log_user']
        
        log_pass = request.POST['log_passwd']

        log = Dashregistration.objects.filter(dash_username = log_user,dash_password=log_pass)
        if log:
            request.session["adminuser"] = log_user
           
            return HttpResponseRedirect("/dashboard")
        
    template=loader.get_template("dashboard/dashboardlogin.html")
    return HttpResponse(template.render({},request))


def dashlogout(request):
    if "adminuser" in request.session:
        del request.session["adminuser"]
        return HttpResponseRedirect("/dashboardlogin")

def dashboard(request):
    if "adminuser" not in request.session:
        return HttpResponseRedirect("/dashboardlogin")
        
    template = loader.get_template("dashboard/dashboard.html")
    return HttpResponse(template.render())

def addcourse(request):
    if "adminuser" not in request.session:
        return HttpResponseRedirect("/dashboardlogin")
        
    if request.method == 'POST':
        couname = request.POST['course_name']
        coutext = request.POST['text']
        coutext1 = request.POST['text1']
        couimage = request.FILES['course_image']
        # procat = request.POST['cat']

        course =Course(cou_name=couname,cou_image = couimage,cou_text=coutext,cou_descri=coutext1)
        
        course.save()
   
    template = loader.get_template("dashboard/addcourse.html")
    return HttpResponse(template.render({},request))
def contacts(request):
    if "adminuser" not in request.session:
        return HttpResponseRedirect("/dashboardlogin")
        
    
    cons = Contacts.objects.all().values()
    context = {
        'contacts':cons
    }
    template=loader.get_template("dashboard/contacts.html")  
    return HttpResponse(template.render(context,request))

def dashregistration(request):
    if "adminuser" not in request.session:
        return HttpResponseRedirect("/dashboardlogin")
        
    dashreg = Registration.objects.all().values()
    context = {
        'dashregistration':dashreg 
    }
    template=loader.get_template("dashboard/dashregistration.html")  
    return HttpResponse(template.render(context,request))

def editcourse(request,id):
    if "adminuser" not in request.session:
        return HttpResponseRedirect("/dashboardlogin")
        
    editcourse=Course.objects.filter(id=id).values()
    if request.method == "POST":
        editname=request.POST['edit_name']
        # editimage=request.FILES['edit_image']
        edittext=request.POST['edit_text']


        updatecourse=Course.objects.filter(id=id)[0]
        updatecourse.cou_name=editname
        updatecourse.cou_text=edittext
        if len(request.FILES) !=0:
            editimage=request.FILES['edit_image']

            updatecourse.cou_image=editimage
        updatecourse.save()
        return HttpResponseRedirect("/course")
    context = {
        'editcourse':editcourse,
        
    }

    template=loader.get_template("dashboard/editcourse.html")  
    return HttpResponse(template.render(context,request))
def viewcourse(request):
    if "adminuser" not in request.session:
        return HttpResponseRedirect("/dashboardlogin")
        
    if 'del' in request.GET:
        id = request.GET['del']
        delcou = Course.objects.filter(id=id)[0]
        delcou.delete()
        return HttpResponseRedirect("/viewcourse")
    viewcourse=Course.objects.all().values()
    context ={
        'viewcourse': viewcourse,
    }
    
    template=loader.get_template("dashboard/viewcourse.html")  
    return HttpResponse(template.render(context,request))


def checkout(request,id):

    if 'user'  not in request.session:
        return HttpResponseRedirect('/login')
    co=0
    adrs=dtype = ""

    # after order submit

    if 'dlv_adrs' in request.POST:
        adrs = request.POST["dlv_adrs"]
        dtype = request.POST["dlv_type"]
        co=1
    user = request.session["user"]

    # delete old data from order
    oldoder = Order.objects.filter(order_user=user,order_status=0) 
    oldoder.delete()


    # add cart data to order table

    course=Course.objects.filter(id=id)[0]
    course1=Course.objects.filter(id=id).values()

    
    order=Order(order_user=user,order_name=course.cou_name,order_image = course.cou_image, order_price =course.cou_price,order_address=  adrs,order_dlvtype=dtype)
        
    order.save()
   
    
# display order status
    order1=Order.objects.filter(order_user = user,order_status=0).values()

    # tot=request.session["tot"]
    # gst=request.session['gst']
    # shp=request.session['shp']
    # gtot=request.session['gtot']
    
    context={
        'order1':order1,
        # 'tot':tot,
        # 'shp':shp,
        # 'gst':gst,
        # 'gtot':gtot,
        'co':co,
        'course':course,
        'course1':course1,

    }
    template = loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))




def confirmorder(request):
    user = request.session["user"]
    order = Order.objects.filter( order_user=user,order_status=0)
    for x in order:
        x.order_status=1
        x.save()

    template = loader.get_template("confirmorder.html")
    return HttpResponse(template.render({},request))

def myorder(request):
    user = request.session["user"]
    order = Order.objects.filter(order_user=user,order_status=1)
    context = {
        'order':order

    }

    template = loader.get_template("myorder.html")
    return HttpResponse(template.render(context,request))

def wish(request):
    if  'user' not in request.session:
        return HttpResponseRedirect('/login')
    if 'del' in request.GET:
        id = request.GET['del']
        delwish = Wishlist.objects.filter(id=id)
        delwish.delete()
        # user =request.session["user"]
    
        # wish =Wishlist.objects.filter( wish_user =user)
        # wishcount = wish.count()
        # request.session["wish"]=wishcount
       
    user = request.session["user"]
    wish = Wishlist.objects.filter(wish_user = user).values()
   
    context = {
            'wish' : wish,
            }
    template=loader.get_template("wish.html")
    return HttpResponse(template.render(context,request))
    
 


def addtowish(request,id):
    # wishcount=0
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    exist = Wishlist.objects.filter(wish_proid=id, wish_user = request.session["user"])
    if exist:
        HttpResponseRedirect("/wish")
    else:
        pro=Course.objects.filter(id=id)[0]
        wish =Wishlist(wish_user =request.session["user"],
                       wish_proid= id,
                       wish_name = pro.cou_name,wish_price =pro.cou_price,wish_image=pro.cou_image)
        wish.save()
        # user =request.session["user"]
    
        # wish =Wishlist.objects.filter( wish_user =user)
        # wishcount = wish.count()
        # request.session["wish"]=wishcount
    return HttpResponseRedirect("/wish")