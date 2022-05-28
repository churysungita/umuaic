from django.contrib import admin

# Register your models here.
from .models import activities, gallery,projects

admin.site.register(gallery)
admin.site.register(projects)
admin.site.register(activities)



# To modify Django Site Administration
admin.site.site_header='UIAC Admininistration' # default Django Administration
admin.site.index_title='UIAC Panel'    # default Site Administration
admin.site.site_title='UIAC site Admin'  # default Django site admin

# username='admin123'
# password='123456'
