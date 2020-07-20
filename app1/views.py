from django.shortcuts import render,redirect
from django.contrib import messages
from app1.forms import Stocker_Register_forms,Product_Details_Form,Dispatcher_Register_Form
from app1.models import StockerRegister,Dispatcher_Register,Product_Details
# Create your views here.
def showIndex(request):
    return render(request,'index.html')


def Admin_log_in(request):
    user_nam = request.POST.get('adminusername')
    passw = request.POST.get('adminpassword')
    if user_nam == "admin":
        if passw == "12345":
            return render(request,'Admin_log_in.html')
        else:
            return render(request, 'index.html', {"mess": "invalid password"})
    else:
        return render(request,'index.html',{"mess":"invalid user name"})


def Stocker_page(request):
    return render(request,'Stocker/Stocker_page.html',{"Stocker_register":Stocker_Register_forms})


def Dispacher_page(request):
    return render(request,'Dispacher/Dispacher_page.html',{'Dispacher_form':Dispatcher_Register_Form})


def Add_Stocker(request):
    Stocker_details = Stocker_Register_forms(request.POST)
    if Stocker_details.is_valid():
        Stocker_details.save()
        return render(request,'Stocker/Stocker_page.html',{'Stocker_register':Stocker_Register_forms})
    else:
        return render(request,'Stocker/Stocker_page.html',{'Stocker_register':Stocker_details})


def Display_Stockers(request):
    return render(request,'Stocker/Stocker_page.html',{"stocker_details":StockerRegister.objects.all()})


def Dispacher_registers(request):
    frm = Dispatcher_Register_Form(request.POST)
    if frm.is_valid():
        frm.save()
        return render(request,'Dispacher/Dispacher_page.html',{'Dispacher_form':Dispatcher_Register_Form})
    else:
        return render(request,'Dispacher/Dispacher_page.html',{'Dispacher_form':frm})


def Display_Dispachers(request):
    return render(request,'Dispacher/Dispacher_page.html',{'Display':Dispatcher_Register.objects.all()})


def delete_Dispacher(request):
    idn = request.GET.get('delete_D')
    Dispatcher_Register.objects.filter(idno=idn).delete()
    return render(request, 'Dispacher/Dispacher_page.html', {'Display': Dispatcher_Register.objects.all()})


def Delete_Stocker(request):
    idnom = request.GET.get('delete_s')
    StockerRegister.objects.filter(idn=idnom).delete()
    return render(request, 'Dispacher/Dispacher_page.html', {'Dispacher_form': Dispatcher_Register_Form})


def Stocker_login(request):
    return render(request,'Stocker/Stocker_login_page.html')


def Stocker_log_test(request):
   username =  request.POST.get('Stockusername')
   password = request.POST.get('Stockuserpassword')
   user = StockerRegister.objects.filter(contact_Number=username)
   if user:
       pas = StockerRegister.objects.filter(Password=password)
       if pas:
           return render(request, 'Stocker/Stocker_log_success.html')
       else:
           return render(request, 'Stocker/Stocker_login_page.html',{'mess':'invalid password'})
   else:
       return render(request, 'Stocker/Stocker_login_page.html',{'mess':'invalid username'})


def Dispatcher_login(request):
    return render(request,'Dispacher/Dispatcher_login.html')


def Dispatchar_login_success(request):
    usern = request.POST.get('Dispatcharuser')
    passw = request.POST.get('Dispatcharpassword')
    usrn = Dispatcher_Register.objects.filter(Contact_Number=usern)
    if usrn:
        passwor = Dispatcher_Register.objects.filter(password=passw)
        if passwor:
            return render(request,'Dispacher/Dispatchar_login_success.html')
        else:
            return render(request,'Dispacher/Dispatcher_login.html',{'mess':"wrong password"})
    else:
        return render(request,'Dispacher/Dispatcher_login.html',{'messs':"wrong username"})


def Stocker_Add_Products(request):
    return render(request,'Product/Product_Details.html',{'ProductForm':Product_Details_Form})


def Stocker_Add_Products_save(request):
    Prod = Product_Details_Form(request.POST)
    if Prod.is_valid():
        Prod.save()
        return render(request,'Product/Product_Details.html',{"mes":"saved sucessfull"})
    else:
        return render(request,'Stocker/Stoker_Change_Password.html')


def Show_All_Products(request):
    return render(request,'Product/Product_Details.html',{'All_Products':Product_Details.objects.all()})


def Stocker_Change_Password(request):
    return render(request,'Stocker/Stoker_Change_Password.html',{'Stocker_Form':Stocker_Register_forms})


def Delete_Product(request):
    return render(request,'Delete_Product.html')


def Delete_Search_idnumber(request):
    Productno = request.GET.get('DeleteSearch')
    prn = Product_Details.objects.filter(Product_no=Productno)
    if prn:
        return render(request,'Delete_Product.html',{'PrDetails':prn})
    else:
        return render(request,'Delete_Product.html',{'noidmes':'Invalid Id'})


def Deleted_Product(request):
    idn = request.GET.get('DelProduct')
    Product_Details.objects.filter(Product_no=idn).delete()
    return render(request,'Delete_Product.html',{'delm':'deleted successfull'})


def Stacker_Changed_Password(request):
    new  = StockerRegister.objects.filter(Password=Passsword)
    up = StockerRegister.objects.filter(new).update()
    if up:
        return render(request, 'Stocker/Stoker_Change_Password.html')
    else:
        return render(request,'Stocker/Stoker_Change_Password.html',{"umes":"invalid old password"})


def Dispacher_Add_Products(request):
    return render(request,'Dispacher/Dispacher_Add_Products.html')


def Dispacher_Add_Products_sucess(request):
    Prod = Product_Details_Form(request.POST)
    if Prod.is_valid():
        Prod.save()
        return render(request, 'Product/Product_Details.html', {"mes": "saved sucessfull"})
    else:
        return render(request, 'Stocker/Stoker_Change_Password.html')