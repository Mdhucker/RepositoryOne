from django.shortcuts import render
from django.conf import settings
from .models import SocialMedia,MishanCompany, Destination

# Create your views here.


def Home(request):
    # Fetch company info (assuming you're only interested in the first entry)
    company_info = MishanCompany.objects.first()  # Retrieve the first entry
    destinations =  Destination.objects.all()  # Fetch all images

    context = {
    'company_info': company_info,
    'destinations': destinations,
    }

    return render(request, 'base/index.html', context)

def gallary(request):
    destinations =  Destination.objects.all()  # Fetch all images


    context = {
    'destinations': destinations,

    }
    return render(request,'base/gallary.html',context)


def About(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/about.html', context)




def services(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/service.html', context)



def packages(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/package.html', context)



def destination(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/destination.html', context)



def booking(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/booking.html', context)



def testimonial(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/testimonial.html', context)



def errorpage(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/404.html', context)






def team(request):
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    context = {
    'company_info': company_info,

    }
    return render(request,'base/team.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .models import SocialMedia
from django.http import Http404

def contact(request):
    # Fetch all social media links to pass to the template
    social_media_links = SocialMedia.objects.all()
    company_info = MishanCompany.objects.first()  # Retrieve the first entry

    socialmedia = {link.platform: link.link for link in social_media_links}

    context = {
        'company_info': company_info,
        'socialmedia':socialmedia,
        }


    return render(request, 'base/contact.html', context)

def social_media_redirect(request, platform):
    # Try to get the specific social media link
   try:
        social_media_link = SocialMedia.objects.get(platform=platform)
        if not social_media_link.link:
            # If the link is empty, show the error page with a custom message
            return render(request, 'base/404.html', {'message': f"The {platform} link is not available."})
        return redirect(social_media_link.link)
   except SocialMedia.DoesNotExist:
        # If the social media platform does not exist, show the error page with a custom message
        return render(request, 'base/404.html', {'message': f"The {platform} link does not exist."})