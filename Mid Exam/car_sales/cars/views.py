from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Car, Brand, Order
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.

class HomeView(View):
    def get(self, request):
        selected_brand_id = request.GET.get('brand')
        brands = Brand.objects.all()
        if selected_brand_id:
            cars = Car.objects.filter(brand_id=selected_brand_id)
        else:
            cars = Car.objects.all()
        return render(request, 'home.html', {'brands': brands, 'cars': cars, 'selected_brand_id': selected_brand_id})

class CarDetailView(View):
    
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        comments = car.comments.all()
        comment_form = CommentForm()
        return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'comment_form': comment_form})
    
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
        
        return redirect('car_detail', pk=car.pk)




@method_decorator(login_required, name='dispatch')
class BuyCarView(View):
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car.quantity > 0:
            Order.objects.create(user=request.user, car=car)
            car.quantity -= 1
            car.save()
            messages.success(request, 'You Have Successfully Buy a Car')
            return redirect('profile')
        return redirect('car_detail', pk=car.pk)


