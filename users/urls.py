from django.urls import path
from users.views import CreateUserView, UpdateUserView

app_name = 'user'
urlpatterns = [
    path("create-user/",CreateUserView.as_view(), name="create_user"),
    path("update-user/",UpdateUserView.as_view(), name="update_user"),
]

