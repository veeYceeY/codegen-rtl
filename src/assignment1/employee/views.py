
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import employee
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html')
############################ LOGIN ###################################
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        admin=employee.objects.filter(username=username,password=password,usertype="admin")
        fromemp=employee.objects.all().filter(username=username,password=password,usertype="employee")
        if admin:
            for x in admin:
                request.session['id']=x.id

            print('success')
            empcount=employee.objects.filter(usertype="employee").count()
            return render(request,'admin-home.html',{'empcount':empcount})
        
        elif fromemp:
            print('success')
            return render(request,'employee-home.html',{'mydetail':fromemp})
        else:
            print('failed')
        return render(request,'login.html',{'msg':'Invalid username or password'})
    else:
        return render(request,'login.html',{'msg':'Invalid username or password'})

############################## ADMIN DASH #################################
def adminhome(request):
    if request.session['id']:
        empcount=employee.objects.filter(usertype="employee").count()
        return render(request,'admin-home.html',{'empcount':empcount})
    else:
        return render(request,'home.html')
############################ LOGOUT #######################################
def logout(request):
    if request.method=='POST':
        pass
    else:
        try:
            del request.session['id']
        except KeyError:
            pass
    return HttpResponseRedirect('/')


###################################### add employee #################################

def addemployee(request):
    if request.method=="POST":
        emp_name=request.POST['emp_name']
        image=request.FILES['photo']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        phone=request.POST['phone']
        address=request.POST['address']
        dob=request.POST['dob']
        doj=request.POST['doj']
        designation=request.POST['designation']
        salary=request.POST['salary']
        fromemp=employee.objects.filter(emp_name=emp_name,image=image,email=email,username=username,password=password,usertype="employee")
        if fromemp:
            return render(request,'add-employee.html',{'fail':'Already exists'})
        toemp=employee(emp_name=emp_name,image=image,email=email,username=username,password=password,usertype="employee",phone=phone,address=address,dob=dob,doj=doj,designation=designation,salary=salary)
        toemp.save()
        x=employee.objects.all()

        print("success",x)

        return render(request,'add-employee.html',{'success':'Successfully added'})
    else:
        print("failed")
        return render(request,'add-employee.html')


######################################################################
def viewemployee(request):
    fromemp=employee.objects.filter(usertype="employee")
    return render(request,'view-employees.html',{'employees':fromemp})
    


# print(&quot;get data to register&quot;)
# a=reguser.objects.all().filter(email=email)
# if not(re.search(&#39;[0-9]{10}&#39;,mob)):
# emailerror=&quot;Not valid mobilenumber&quot;
# return render(request,&#39;reg.html&#39;,{&#39;regForm&#39;:regFrm,&#39;moberror&#39;:emailerror})
# elif a:
# emailerror=&quot;Email Already Exist&quot;
# return render(request,&#39;reg.html&#39;,{&#39;regForm&#39;:regFrm,&#39;emailerror&#39;:emailerror})
# else:
# reg.email=email
# reg.mobile=mob

# if pwd1==pwd2:
# reg.password=pwd1
# print(&quot;Password match&quot;)
# reg.save()
# msg=&quot;Successfully inserted&quot;
# return render(request,&quot;reg.html&quot;,{&#39;regForm&#39;:regFrm,&quot;msgkey&quot;:msg})
# else:
# return

# render(request,&quot;reg.html&quot;,{&#39;regForm&#39;:regFrm,&quot;msgkey&quot;:&quot;Password missmatch&quot;})
# else:
# return render(request,&quot;reg.html&quot;,{&#39;regForm&#39;:regFrm,&quot;msgkey&quot;:&quot;Invalid

# Credentials&quot;})
# else:
# return render(request,&quot;reg.html&quot;,{&#39;regForm&#39;:regFrm})

# ############################################################# login
# ###############################################

# def log(request):
# logFrm=logForm()
# if request.method==&quot;POST&quot;:
# print(&quot;==============inside POST==================&quot;)
# form=logForm(request.POST)
# if form.is_valid():
# print(&quot;===================valid Form====================&quot;)
# email=form.cleaned_data[&#39;email&#39;]
# password=form.cleaned_data[&#39;password&#39;]
# fromReg=reguser.objects.all().filter(email=email,password=password)
# print(fromReg)
# if fromReg:
# print(&quot;=========================valid user===================&quot;)
# for x in fromReg:
# print(&quot;==============set session and loged

# in==========================&quot;)

# request.session[&#39;id&#39;]=x.id
# request.session[&#39;fname&#39;]=x.firstname
# request.session[&#39;lname&#39;]=x.lastname
# fromProp=propertyreg.objects.all()

# view1=propertyreg.objects.select_related(&#39;userid&#39;).filter(status=&#39;approved&#39;)

# print(&quot;view1====&quot;,view1)
# proptypes=plottype.objects.all()
# print(proptypes)
# return

# render(request,&#39;userhome.html&#39;,{&#39;property&#39;:fromProp,&#39;fname&#39;:x.firstname,&#39;lname&#39;:x.lastname,&#39;vi
# 1&#39;:view1,&#39;proptypes&#39;:proptypes})

# else:
# return render(request,&quot;log.html&quot;,{&#39;logForm&#39;:logFrm,&quot;msgkey&quot;:&#39;Invalid

# credentials&#39;})
# else:
# return render(request,&quot;log.html&quot;,{&#39;logForm&#39;:logFrm})

# ####################################################### user home
# ##################################################

# def userhome(request):
# fname=request.session[&#39;fname&#39;]
# lname=request.session[&#39;lname&#39;]
# fromProp=propertyreg.objects.all()
# view1=propertyreg.objects.select_related(&#39;userid&#39;).filter(status=&#39;approved&#39;)
# print(&quot;view1====&quot;,view1)
# proptypes=plottype.objects.all()
# print(proptypes)
# return
# render(request,&#39;userhome.html&#39;,{&#39;property&#39;:fromProp,&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;vi1&#39;:view1,&#39;
# proptypes&#39;:proptypes})
# # return render(request,&#39;userhome.html&#39;,{&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;vi1&#39;:fromProp})

# ###################################################### property registration
# ####################################

# def propertyRegister(request):
# propregForm=propRegForm()
# if request.method==&quot;POST&quot;:
# print(&quot;-----------------inside POST-------------------&quot;)
# form=propRegForm(request.POST,request.FILES)
# if form.is_valid():
# print(&quot;------------------ VALID FORM-------------------&quot;)
# prop=propertyreg()

# des=form.cleaned_data[&#39;description&#39;]
# prop.image=form.cleaned_data[&#39;image&#39;]
# prop.status=&quot;not approved&quot;
# area=form.cleaned_data[&#39;area&#39;]
# amount=form.cleaned_data[&#39;amount&#39;]

# recordexists=propertyreg.objects.all().filter(propertytype=pt,district=dt,location=loc,address=ad,
# description=des)

# ####################################################### logout
# #####################################################

# 

# ###############################################################################
# #########################################
# def userupdate(request):
# ids=request.session[&#39;id&#39;]
# fname=request.session[&#39;fname&#39;]
# lname=request.session[&#39;lname&#39;]
# if request.method==&#39;POST&#39;:
# print(&quot;-----------------post-----------------------&quot;)
# nfname=request.POST[&#39;fname&#39;]
# nlname=request.POST[&#39;lname&#39;]
# adr=request.POST[&#39;address&#39;]
# mob=request.POST[&#39;mob&#39;]
# email=request.POST[&#39;email&#39;]
# password=request.POST[&#39;pwd1&#39;]
# cpassword=request.POST[&#39;pwd2&#39;]
# print(&quot;-----------------get data--------------------&quot;,fname,lname,adr,mob)
# if (password==&quot;&quot;) and (cpassword==&quot;&quot;):
# print(&quot;-----------------null pwd fields-----------------------&quot;)

# reguser.objects.filter(id=ids).update(firstname=nfname,lastname=nlname,address=adr,mobile=
# mob,email=email)

# det=reguser.objects.all().filter(id=ids)
# return

# render(request,&#39;userdetails.html&#39;,{&#39;details&#39;:det,&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;msg&#39;:&#39;Successfully
# changed&#39;})
# elif password==cpassword:
# print(&quot;-----------------equal pwd fields-----------------------&quot;)

# reguser.objects.filter(id=ids).update(firstname=nfname,lastname=nlname,address=adr,mobile=
# mob,email=email,password=password)

# det=reguser.objects.all().filter(id=ids)
# return

# render(request,&#39;userdetails.html&#39;,{&#39;details&#39;:det,&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;msg&#39;:&#39;Successfully
# changed data with password&#39;})
# else:
# print(&quot;-----------------missmatch pwd fields-----------------------&quot;)
# det=reguser.objects.all().filter(id=ids)
# return

# render(request,&#39;userdetails.html&#39;,{&#39;details&#39;:det,&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;msg&#39;:&#39;Password
# missmatch&#39;})
# else:
# print(&quot;-----------------POST fail-----------------------&quot;)
# det=reguser.objects.all().filter(id=ids)
# return render(request,&#39;userdetails.html&#39;,{&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;details&#39;:det})

# ###############################################################################
# ####################

# def adhome(request):
# return render(request,&#39;admin-home.html&#39;)
# ###############################################################################
# #########################
# def adviewusers(request):
# users=reguser.objects.all()
# return render(request,&#39;admin-viewusers.html&#39;,{&#39;users&#39;:users})
# ###############################################################################
# ###################
# def adChangedt(request):
# ids=request.session[&#39;id&#39;]
# if request.method==&#39;POST&#39;:
# print(&quot;----------------POSTin --------------------------&quot;)
# password=request.POST[&#39;password&#39;]
# cpassword=request.POST[&#39;cpassword&#39;]
# if password!=cpassword:
# print(&quot;-----------------null pwd fields-----------------------&quot;)
# return render(request,&#39;admin-changedetails.html&#39;,{&#39;message&#39;:&#39;Password

# missmatch&#39;})
# elif password==cpassword:
# print(&quot;-----------------null pwd fields-----------------------&quot;)

# adminlog.objects.filter(id=ids).update(password=password)
# return render(request,&#39;admin-changedetails.html&#39;,{&#39;message&#39;:&#39;Password changed

# successfully&#39;})
# else:
# print(&quot;-----------------null pwd fields-----------------------&quot;)
# return render(request,&#39;admin-changedetails.html&#39;,{&#39;message&#39;:&#39;Error ocuured&#39;})
# else:
# print(&quot;----------------post fail ------------------&quot;)
# admindt=adminlog.objects.all().filter(id=ids)
# return render(request,&#39;admin-changedetails.html&#39;,{&#39;admindt&#39;:admindt})
# ###############################################################################
# #########################
# def typesearchad(request):
# if request.method==&#39;POST&#39;:
# ptype=request.POST[&#39;proptype&#39;]
# fromtype=plottype.objects.all().filter(id=ptype)
# for x in fromtype:
# ptypes=x.plottype
# fromProp=propertyreg.objects.all().filter(propertytype=ptypes)
# print(ptype)
# proptypes=plottype.objects.all()
# print(proptypes)
# fname=request.session[&#39;fname&#39;]
# lname=request.session[&#39;lname&#39;]
# return render(request,&#39;admin-
# searchview.html&#39;,{&#39;proptypeview&#39;:fromProp,&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;proptypes&#39;:proptypes,
# &#39;typename&#39;:ptypes})
# else:
# fromProp=propertyreg.objects.all().filter(propertytype=&#39;Plot&#39;)
# print(ptype)
# proptypes=plottype.objects.all()
# print(proptypes)
# fname=request.session[&#39;fname&#39;]
# lname=request.session[&#39;lname&#39;]
# return render(request,&#39;admin-
# searchview.html&#39;,{&#39;proptypeview&#39;:fromProp,&#39;fname&#39;:fname,&#39;lname&#39;:lname,&#39;proptypes&#39;:proptypes,
# &#39;typename&#39;:ptypes})
# ###############################################################################
# ###########################
