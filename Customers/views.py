from django.shortcuts import render,redirect
from  django.contrib.auth.models import User,auth
from django.contrib import messages
from app1.models import Product_Details


def Customers_registration_page(request):
    return render(request, 'Customers/Customers_registration_page.html')


def Customer_login_page(request):
    return render(request, 'Customers/login_page.html')


def Customer_Register_Request(request):
    if request.method == "POST":
        name = request.POST['cu1']
        l_name = request.POST['cu2']
        user_nme = request.POST['cu3']
        email_id = request.POST['cu4']
        Pwd = request.POST['cu5']
        Pwd2 = request.POST['cu6']
        Phone = request.POST['cu7']
        if Pwd == Pwd2:
            if User.objects.filter(username=user_nme).exists():
                messages.error(request, 'user name is alredy exists try with another username')
                return redirect('Customer_Register_Request')
            elif User.objects.filter(email=email_id).exists():
                messages.error(request, 'email is alredy exists try with another email')
                return redirect('Customer_Register_Request')
            else:
                users = User.objects.create_user(first_name=name, username=user_nme, email=email_id, password=Pwd,
                                                 last_name=l_name)
                users.save();
                messages.success(request, 'register successfully')
                return redirect('Customer_login_page')
        else:
            messages.error(request, 'password and confirm-password does not match')
            return redirect('Customer_Register_Request')
    return redirect('Customer_Register_Request')


def Customer_login_request(request):
    if request.method == "POST":
        usern = request.POST["cul1"]
        paswd = request.POST["cul2"]
        user = auth.authenticate(username=usern,password=paswd)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'invalid credensials')
            return redirect('Customer_login_page')
    return redirect('home')


def Customer_show_Products(request):
    Products = Product_Details.objects.all()
    return render(request,'Product/Customers_Show_Products.html',{'Products_list':Products})


def Click_Buy_Product(request):
    productid = request.GET.get('product')
    pr = Product_Details.objects.filter(Product_no=productid)
    return render(request,'Product/Click_Buy_Product.html',{'prd':pr})