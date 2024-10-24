from django.db import models
from django.contrib.auth.models import User

# Services provided by the companies
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Destinations offered by the tour companies
class Destination(models.Model):
    name = models.CharField(max_length=255)  # Changed from destin_location
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage discount
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)

    def __str__(self):
        return self.name

# Offers or promotions by the companies
class Offer(models.Model):
    offer_name = models.CharField(max_length=255)
    description = models.TextField()
    offer_amount = models.DecimalField(max_digits=5, decimal_places=2)  # Offer price 
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage discount
    valid_until = models.DateField()
    valid_days = models.IntegerField(null=True, blank=True)  # Number of valid days or None for no limit
    start_date = models.DateField()  # Start date of the offer
    end_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.offer_name  # Changed from self.title

   
# Testimonials for the companies
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)  # Fixed typo
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.text[:20]}...'  # Show a preview of the text

# Team members for the companies
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_members/', blank=True, null=True)

    def __str__(self):
        return self.name

# Mishan Company Model
class MishanCompany(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  # Allow blank
    founded = models.DateField(blank=True, null=True)  # Allow blank and null
    service_type = models.CharField(max_length=255, blank=True)  # Allow blank
    location = models.CharField(max_length=255, blank=True)  # Allow blank
    phone_number = models.CharField(max_length=20, blank=True)  # Allow blank
    contact_email = models.EmailField(blank=True,null=True)  # Allow blank
    destinations = models.ManyToManyField('Destination', blank=True)  # Allow blank
    established_date = models.DateField(blank=True, null=True)  # Allow blank and null
    services = models.ManyToManyField('Service', blank=True)  # Allow blank
    offers = models.ManyToManyField('Offer', blank=True)  # Allow blank
    team = models.ManyToManyField('TeamMember', blank=True)  # Allow blank

    def __str__(self):
        return self.location if self.location else "Company Name Not Provided"

class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)  # Changed to use ForeignKey
    description = models.TextField()
    price_per_person = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return self.destination.name  # Adjusted to show destination name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start_date = models.DateField()  # Date when the journey starts
    number_of_people = models.IntegerField()
    special_requests = models.TextField(null=True, blank=True)  # Optional special requests
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"Booking for {self.user.username} to {self.tour.destination.name}"  # Show destination name


# from django.db import models

# class Gallery(models.Model):
#     title = models.CharField(max_length=255, blank=True)  # Optional title for the image
#     image = models.ImageField(upload_to='gallery/')  # Path where images are stored
#     destination = models.ForeignKey('Destination', on_delete=models.CASCADE, null=True, blank=True)
#     offer = models.ForeignKey('Offer', on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.title if self.title else 'Gallery Image'


class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('YouTube', 'YouTube'),
        ('TikTok', 'TikTok'),
        ('Other', 'Other'),  # Add more platforms as needed
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    link = models.URLField(max_length=200)  # URL field for the social media link

    def __str__(self):
        return f"{self.platform}: {self.link}"
