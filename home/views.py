from django.shortcuts import render



def home(request):
    return render(request, "home/index.html", {})

# class HomeView(TemplateView):
#     template_name = "home/index.html"
