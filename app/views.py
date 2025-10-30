from django.shortcuts import render

from django.views import View


# Create your views here.

class HomeView(View):

    def get(self, request, *args, **kwargs):

        data={'title':'Home','page':'home'}

        return render(request, 'app/home.html',context=data)
    
class AboutView(View):

    def get(self, request, *args, **kwargs):

        data={'title':'Home','page':'home'}

        return render(request, 'app/about.html',context=data)
    
class MenuView(View):

    def get(self, request, *args, **kwargs):

        data={'title':'Home','page':'home'}

        return render(request, 'app/menu.html',context=data)
    
class ContactView(View):

    def get(self, request, *args, **kwargs):

        data={'title':'Home','page':'home'}

        return render(request, 'app/contact.html',context=data)
    
class BookingView(View):

    def get(self, request, *args, **kwargs):
        
        service = request.GET.get('service')

        data = {
            'title': 'Booking',
            'page': 'booking',
            'service': service
        }
        return render(request, 'app/booking.html', context=data)

    def post(self, request, *args, **kwargs):
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')

        
        confirmation = f"Booking confirmed for {name} on {date} for {service}"

        data = {
            'confirmation': confirmation,
            'name': name,
            'email': email,
            'service': service,
            'date': date
        }
        return render(request, 'app/booking.html', context=data)
