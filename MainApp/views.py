from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "MainApp/index.html")


@login_required  # this is a decorator, that requires it to be done before the action can be taken
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")

    context = {"topics": topics}

    return render(request, "MainApp/topics.html", context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}

    return render(request, "MainApp/topic.html", context)


@login_required
def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect("MainApp:topics")

    context = {"form": form}

    return render(request, "MainApp/new_topic.html", context)


@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():

            new_entry = form.save(commit=False)

            new_entry.topic = topic

            new_entry.save()

            return redirect("MainApp:topic", topic_id=topic_id)

    context = {"form": form, "topic": topic}

    return render(request, "MainApp/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        # This argument tells Django to create the form prefilled
        # with information from the existing entry object.
        form = EntryForm(instance=entry)
    else:
        # POST the submitted data and update the database
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("MainApp:topic", topic_id=topic.id)

    context = {"topic": topic, "entry": entry, "form": form}

    return render(request, "MainApp/edit_entry.html", context)


# Normally you have a whole bunch of code here in order to change the views of the website
