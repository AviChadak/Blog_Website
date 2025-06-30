from . models import Category

def get_catregory(request):
    categories = Category.objects.all()
    return dict(categories=categories)