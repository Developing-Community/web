from django.contrib import admin

# Register your models here.


from .models import Product, Campaign, CampaignTermRelation, CampaignPartyRelation, CampaignContentRelation, \
    CampaignEnrollmentRequest

admin.site.register(Campaign)
admin.site.register(CampaignPartyRelation)
admin.site.register(CampaignEnrollmentRequest)
admin.site.register(CampaignTermRelation)
admin.site.register(CampaignContentRelation)
admin.site.register(Product)
