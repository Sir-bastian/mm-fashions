from django.db import models

# Create your models here.
'''Model For Product Categories (e.g Boots, Sneakers, Slides, Sandals)'''
class Category(models.Model):
    name = models.CharField(
        max_length = 100,
        unique = True, #Ensures no two categories have same exact name
        help_text = 'e.g, Sneakers, Sandals, Boots, slides' # Helpful hint for admin panel
    )
    description = models.TextField(
        blank = True,
        null = True
    )
    
class Meta:
    verbose_name = 'Category'
    verbose_name_plural = "Categories" #fixes "Categorys" to "Categories"

def __str__(self):
    """
    This method defines the string representation of an object
    It is what'll be seen in the admin panel & when we print model
    instances
    """ 
    return self.name

class Brand(models.Model):
    # Model for Brands (e.g., Niike, Adidas, Puma)
    name = models.CharField(
        max_length= 100,
        unique = True,
        help_text= "e.g., Nike, Adidas, Puma, Reebok, New_Balance"
    )
    description= models.TextField(
        null = True,
        blank = True
    )
    
def __str__(self):
    return self.name

class Product(models.Model):
    # Model for the actual product (e.g., a specific pair of shoes)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits =10, # Total number of digits allowed (e.g., 999999999)
        decimal_places = 2 #Number of digits after the decimal point
    )
    stock = models.IntegerField(default=0) #Current Quantity in stock
    # SKU = "Stock Keeping Unit"
    sku = models.CharField(
        max_length = 50,
        unique = True,
        blank = True,
        null = True,
        help_text = "Stock keeping Unit - Unique Identifier for Inventory"
    )
    image_url = models.URLField(
        max_length = 1024,
        blank = False,
        null = False,
        help_text = "URL to the product image"
        )

    # Foreign Keys: Link products to categories and brands.
    # Why ForeignKey: This creates the Many-to-One relationship.
    # on_delete=models.SET_NULL: If a Category is deleted, don't
    # delete products; just set their category to NULL.
    # null=True: Required if you use SET_NULL.
    # elated_name='products': Allows you to access products from.
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='store'
    )
    
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        related_name='store'
    )
    
    created_at = models.DateTimeField(
        auto_now_add = True #Automatically sets the date/time when the object is first created.
    )
    
    updated_at = models.DateTimeField(
        auto_now = True # Automatically updates date/time.
    )
    
class Meta():
    ordering = ['name'] #Default ordering for products when queried

def __str__(self):
    return self.name
