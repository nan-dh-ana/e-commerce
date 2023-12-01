from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from .models import Product
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# Create your views here.
def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please login")
            return redirect('log')
    return inner

dec=[signin_required,never_cache]

# Create your views here.
# class LogView(View):
#     def get(self,request):
#         form=LogForm()
#         return render(request,"log.html",{"form":form})

class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        form=LogForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"login successfull")
                return redirect("home")
            else:
                messages.error(request,"invalid username or password ")
                return redirect('log')
        return render(request,"log.html",{"form":form})

# class RegView(View):
    # form_class=RegForm
    # template_name="reg.html"
    # model=User
    # success_url="log"
    # def get(self,request):
    #     form=self.form_class
    #     return render(request,self.template_name,{"form":form})
    # def post(self,request):
    #     form_data=self.form_class(data=request.POST)
    #     if form_data.is_valid():
    #         form_data.save()
    #         messages.success(request,"Registration Success!!!!")
    #         return redirect(self.success_url)
    #     messages.error(request,"Validation failed!!!!")
    #     return render(request,self.template_name,{"form":form_data})

class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy("log")
    def form_valid(self,form):
        messages.success(self.request,"Registeration Successfull")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"Registeration Failed")
        return super().form_valid(form)


# class HomeView(TemplateView):
    # template_name="home.html"

@method_decorator(dec,name='dispatch')
class HomeView(ListView):
    template_name="home.html"
    queryset=Product.objects.all()
    context_object_name="data"

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')