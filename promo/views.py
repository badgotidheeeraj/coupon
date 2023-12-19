from django.shortcuts import render


from .models import *


def profile(request):
    start=masterdata.objects.all()
    if request.method=='POST':
        brand=request.POST.get('brand')
        category=request.POST.get('category')
        File_name = request.FILES['File_name'] 
        text=request.POST.get('text')
        data=Post( user=request.user, brand=brand,category=category,File_name=File_name,text=text).save()



    return render(request, 'promo/blog_single.html',{'start':start ,"postdata":Post.objects.filter(user=request.user).order_by('created_at')})

def create_post(request):
    # start=masterdata,object.all()



    return render(request, 'promo/blog_single.html',{'start':start})


'''
def index(request):
    page = None
    document = None
    if request.method == 'POST' and request.FILES:
        document = request.FILES['upload']
        sve = Files(File_name=document)
        sve.save()
        content = {
            'data': ref_deteducation(document)
        }
        return render(request, "index.html", content)
    else:
        context = {'form': page, }
    return render(request, "index.html", context)
'''