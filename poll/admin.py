from django.contrib import admin
from.models import*
# Register your models here.
admin.site.register(Electiontype)
admin.site.register(ControlVote)

@admin.register(positions)
class positionsAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)


@admin.register(candidate)
class candidateAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','position','total_votes')
    list_filter = ('position',)
    readonly_fields = ('total_votes',)



