from django.shortcuts import render,redirect
from .models import property_detail
# Create your views here.
def home(request):
    property_objs=property_detail.objects.all()
    context={'propertys':property_objs}
    return render(request,"index.html",context)

def aboutus(request):
    return render(request,"aboutus.html")


def house(request):
    property_objs=property_detail.objects.all()
    context={'propertys':property_objs}
    return render(request,"house.html",context)

def land(request):
    property_objs=property_detail.objects.all()
    context={'propertys':property_objs}
    return render(request,"land.html",context)

def post(request):
    if request.method=="POST":
        title=request.POST.get("title")
        location=request.POST.get("location")
        contact=request.POST.get("contact")
        alternative_contact=request.POST.get("alternative-contact")
        facilities=request.POST.get("facilities")
        property_details=request.POST.get("property_details")
        property_area=request.POST.get("property-area")
        property_type=request.POST.get("property-type")
        furnishing=request.POST.get("furnishing")
        bedroom=request.POST.get("bedroom",)
        try:
            bedroom = int(bedroom)
        except ValueError:
            bedroom = 0
        Kitchen=request.POST.get("Kitchen")
        try:
            Kitchen = int(Kitchen)
        except ValueError:
            Kitchen = 0
        living_room=request.POST.get("living_room")
        try:
            living_room = int(living_room)
        except ValueError:
            living_room = 0
        bathroom=request.POST.get("bathroom")
        try:
            bathroom = int(bathroom)
        except ValueError:
            bathroom = 0
        carparking=request.POST.get("carparking")
        try:
            carparking = int(carparking)
        except ValueError:
            carparking = 0
        image_upload=request.POST.get("image-upload")
        price=request.POST.get("price")
        

        property_detail.objects.create(title=title,location=location,contact=contact,alternative_contact=alternative_contact,facilities=facilities,property_details=property_details,property_area=property_area,price=price,property_type=property_type,image=image_upload,furnishing=furnishing,bedroom=bedroom,kitchen=Kitchen,living_room=living_room,bathroom=bathroom,car_parking=carparking)
        return redirect("home")

    return render(request,"post-property.html")