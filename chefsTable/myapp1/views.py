from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp1.forms import LogForm
from .models import Logger

# html parameters
def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['AGE'] = 20

    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def say_hello(request):
    return HttpResponse("Welcome to Little Lemon!Yuanyuan")

def display_time(request):
    date_joined = datetime.today().ctime
    return HttpResponse(date_joined)

# Add http response
def menu(request):
    text = """"<h1 sytle = "color:#F4CE14;">   This is Littlt Lemon again!</h1>"""
    return HttpResponse(text)

# should pass a dish parameter in the function
def menuitems(request, dish):
    items = {
        'pasta':'Pasta is a type of noodle made from combination of wheat, water or eggs',
        'falafel': 'Falafel are deep fried patties or balls',
        'cheesecake': 'Cheesecake is type of dessert made with flour'
    }
    description = items[dish]  
    return HttpResponse(f"<h2> {dish} </h2>" + description)

# create a form page to enter firstname, lastname and submit
def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if(form.is_valid):
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

def Logger_by_name(request):
    new_logger = Logger.objects.all()
    logger_dict = {'logger' : new_logger}
    return render(request, 'logger.html', logger_dict)


def about(request):
    about_content = {'about': "Based in Atlanta, Illinois, Little Lemon"}
    return render(request, "about.html", about_content)

# template inheritance
def home_menu(request):
    return render(request, 'index.html')

def about_menu(request):
    return render(request, 'about_page.html')

def menu_page(request):
    return render(request, 'menu.html')
