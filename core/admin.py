from django.contrib import admin

from .models import Post, LeaderBoard

admin.site.register(Post)


@admin.register(LeaderBoard)
class LeaderBoard2(admin.ModelAdmin):
    list_display = ("contributor", "department", "count", "update_leader_board")
