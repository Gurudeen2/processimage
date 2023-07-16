from django.shortcuts import render
from .models import WaterMarkRemove, RemoveBackground
from PIL import Image, ImageDraw, ImageFont
import os
from django.core.files import File


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')


def remove_img_background(request):
    if request.method == "POST":
        img = request.FILES['removeimg']

        # filename = str(img).split(".")
        # img_path = Image.open(img)


        # img_path.save("media/photo/"+filename[0]+"."+img_path.format)
        
        
        # output = Image.open(f'media/photo/{filename[0]}.{img_path.format}')
        # imgregb = remove(output)
        # # # removedbg = open(img_path, "rb")
        # imgregb = imgregb.convert("RGB")
        # imgregb.save(f'media/photo/{filename[0]}.{img_path.format}')
        # l_img = open(f'media/photo/{filename[0]}.{img_path.format}', "rb")
        # convert_img_to_file = File(l_img)
        
        # # save image to database
        # remove_db = RemoveBackground.objects.create()
        # remove_db.photo.save(filename[0]+"."+img_path.format,convert_img_to_file)


        # return render(request, "page/removebg.html", {"removebg":RemoveBackground.objects.all().first().photo})
    return render(request, "pages/removebg.html")
