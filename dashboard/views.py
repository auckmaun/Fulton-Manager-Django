from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def panel_principal(request):
    return render(request, 'dashboard/panel.html')

