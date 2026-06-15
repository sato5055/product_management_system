from django.shortcuts import render
from myapp.models import Shopping_Category
from myapp.models import Shopping_Item
from myapp.models import Account_User


# Create your views here.
def index(request):
    queryset = Shopping_Category.objects.all()
    context = {
        "shopping_list":queryset
    }
    return render(request, 'myapp/main.html', context)

def login(request):
    return render(request, 'myapp/login.html')

def registerUser(request):
    return render(request, "myapp/registerUser.html")

def registerUserConfirm(request):
    context = {
        "name":request.POST["name"],
        "address":request.POST["address"],
        "user_id":request.POST["user_id"],
        "password":request.POST["password"]
    }
    return render(request, "myapp/registerUserConfirm.html", context)

def registerUserCommit(request):
    new_user = Account_User()
    new_user.name = request.POST["name"]
    new_user.address = request.POST["address"]
    new_user.user_id = request.POST["user_id"]
    new_user.password = request.POST["password"]

    print(new_user.user_id)

    new_user.save()
    context = {
        "name":new_user.name,
        "address":new_user.address,
        "userID":new_user.user_id,
        "password":new_user.password
    }
    return render(request, "myapp/registerUserCommit.html", context)

def show_search(request):
    user_keyword = request.POST["search"]
    user_category = request.POST["category"]
    if(user_category == "all"):
        queryset = Shopping_Item.objects.filter(name__icontains=user_keyword)
        specific_item = "すべて"
    else:
        queryset = Shopping_Item.objects.filter(category_id=user_category, name__icontains=user_keyword)
        specific_item = (Shopping_Category.objects.get(category_id=user_category)).name

    context = {
        "search":request.POST["search"],
        "category":request.POST.get("category", "q"),
        "shopping_item_list":queryset,
        "category_name": specific_item
    }
    return render(request, "myapp/searchResult.html", context)
