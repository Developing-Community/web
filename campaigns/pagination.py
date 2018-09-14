from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )



class CampaignLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class CampaignPageNumberPagination(PageNumberPagination):
    page_size = 20