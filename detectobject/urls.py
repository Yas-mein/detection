from django.urls import path
# from . import views
# from . import api 
# from .views import object_detection
# from .views import ObjectDetectionView
from .views import api2

urlpatterns = [
    # path('d/', ObjectDetectionView),
    path('a/',api2),

]



