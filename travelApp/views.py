from django.shortcuts import render
from django.conf import settings
from .models import SocialMedia

# Create your views here.

def Home(request):
    
    return render(request,'base/index.html', {'settings': settings})



def About(request):
    
    return render(request,'base/about.html')




def services(request):
    
    return render(request,'base/service.html')



def packages(request):
    
    return render(request,'base/package.html')



def destination(request):
    
    return render(request,'base/destination.html')



def booking(request):
    
    return render(request,'base/booking.html')



def testimonial(request):
    
    return render(request,'base/testimonial.html')



def errorpage(request):
    
    return render(request,'base/404.html')


# from django.shortcuts import render
# from .models import SocialMedia
# from django.http import Http404  # Import Http404 for raising errors

# def contact(request):
#     twitter_link = SocialMedia.objects.filter(platform='Twitter').first()
#     facebook_link = SocialMedia.objects.filter(platform='Facebook').first()
#     youtube_link = SocialMedia.objects.filter(platform='YouTube').first()
#     linkedin_link = SocialMedia.objects.filter(platform='LinkedIn').first()
    
#     # Check if any of the required links are missing
#     if not twitter_link or not facebook_link or not youtube_link or not linkedin_link:
#         raise Http404("One or more social media links are missing.")

#     context = {
#         'twitter_link': twitter_link.link,
#         'facebook_link': facebook_link.link,
#         'youtube_link': youtube_link.link,
#         'linkedin_link': linkedin_link.link,
#     }
    
#     return render(request, 'base/contact.html', context)






def team(request):
    
    return render(request,'base/team.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import SocialMedia
from django.http import Http404

def contact(request):
    # Fetch all social media links to pass to the template
    social_media_links = SocialMedia.objects.all()
    context = {link.platform: link.link for link in social_media_links}

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