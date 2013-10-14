from django.contrib import admin
from kitchen.models import (
        Topic,
        Member,
        Resource,
        Session,
        NewsItem,
        )

admin.site.register(Topic)
admin.site.register(Member)
admin.site.register(Resource)
admin.site.register(Session)
admin.site.register(NewsItem)




