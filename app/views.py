from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note
from django.shortcuts import get_object_or_404


def lpu(req):
    return HttpResponse("LPU is a university")
def aboutlpu(req):
    return HttpResponse("LPU is located in Jalandhar")
def home(req):
    note = Note.objects.all()
    return render(req, 'index.html', context={"notes": note})

def saveDataView(req):
    print(req.POST)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
            messages.error(req, "Fill all details")
            return redirect("/")
    note = Note(title=title, description=description)
    note.save()


    messages.success(req, "Details saved")
    return redirect("/")


def deleteView(req, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    messages.success(req, "Note deleted successfully")
    return redirect("/")

