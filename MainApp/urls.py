from django.urls import path

from . import views  # the period means to import from this same folder

app_name = "MainApp"

urlpatterns = [
    path(
        "", views.index, name="index"
    ),  # points to the default homepage because it is blank
    path("topics", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
