from django.shortcuts import render
from myapp.models import Shopping_Category
from myapp.models import Shopping_Item


# Create your views here.
def index(request):
    queryset = Shopping_Category.objects.all()
    context = {
        "shopping_list":queryset
    }
    return render(request, 'myapp/main.html', context)

# def search(request):
#     query = request.POST()

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
