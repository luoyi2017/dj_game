from django.contrib import admin
from .models import Player, Player_gold_log

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['playerid', 'playername', 'level', 'experience', 'regtime']

class GoldAdmin(admin.ModelAdmin):
    list_display = ['playerid', 'serverid', 'gold_change', 'gold', 'gold_change_time']

admin.site.register(Player, PlayerAdmin)
admin.site.register(Player_gold_log, GoldAdmin)


