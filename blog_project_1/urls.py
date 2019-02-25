"""bg_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import app_1.views 
import portfolio.views

from django.conf import settings # media를 사용하기 위해 import해야 하는 것 1(setting.py를 사용해야하기 때문)
from django.conf.urls.static import static # media를 사용하기 위해 import해야 하는 것 2
# 위의 2개의 코드는 media를 활용하기 위해서 써야하는 코드로, 습관처럼 암기할 것!


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_1.views.home, name = 'home'),
    path('blog/', include('app_1.urls')),
    
    path('portfolio/', portfolio.views.portfolio, name = 'portfolio'),
    path('certificate/', portfolio.views.certificate, name='certificate'),

    path('account/', include('account.urls')), # account/로 들어오고, account폴더의 urls.py라는 새로운 파일을 참조하면 된다.
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 얘도 MEDIA파일 쓸 때 써야하는 코드이므로, 암기할 것!

