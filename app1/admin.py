from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
# Register your models here.
from .models import Staff,Expenses,Revenue, Match,Merchandise, Report, Fan, Player,Team, Purchases
admin.site.register(Staff)
admin.site.register(Expenses)
admin.site.register(Revenue)
admin.site.register(Report)
admin.site.register(Merchandise)
admin.site.register(Fan)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Purchases)


class  MatchAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Match, MatchAdmin)