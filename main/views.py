from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNoteForm, AddTwoNumbersForm

# Create your views here.

def home(response):
    return render(response, "main/base.html", {})

def calc(response):
    if response.method == "POST":
        print(response.POST)
        a = int(response.POST["a"])
        b = int(response.POST["b"])
        form = AddTwoNumbersForm(response.POST)
        if response.POST["operation"] == "Add":
            c = a + b
        elif response.POST["operation"] == "Subtract":
            c = a - b
        elif response.POST["operation"] == "Multiply":
            c = a * b
        elif response.POST["operation"] == "Divide":
            c = a / b
        elif response.POST["operation"] == "Clear":
            form = AddTwoNumbersForm()
            return render(response, "main/calc.html", {"form": form})
        
        return render(response, "main/calc.html", {"result": c, "a": a, "b": b, "form": form})
    else:
        form = AddTwoNumbersForm()
        return render(response, "main/calc.html", {"form": form})
    
def notes(response):
    notes = Note.objects.all()
    print(notes)
    if response.method == "GET":
        form = AddNoteForm()
        return render(response, "main/notes.html", {"notes": notes, "form": form})
    elif response.method == "POST":
        form = AddNoteForm(response.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if response.POST["operation"] == "Add Note":
                note = Note(title=title, content=content)
                note.save()
                form = AddNoteForm()
                return render(response, "main/notes.html", {"notes": notes, "form": form})
            elif response.POST["operation"] == "Update Note":
                print(response.POST)
                note = Note.objects.get(id=response.POST["id"])
                note.title = title
                note.content = content
                note.save()
                form = AddNoteForm()
                return render(response, "main/notes.html", {"notes": notes, "form": form})
        else:
            return render(response, "main/notes.html", {"notes": notes, "form": form, "error": "Invalid form"})
       
def deleteNote (response, id):
    if response.method == "POST":
        form = AddNoteForm()
        note = Note.objects.get(id=id)
        note.delete()
        notes = Note.objects.all()
        return render(response, "main/notes.html", {"notes": notes, "form": form})
    else:
        return redirect("notes")
    
def editNote (response, id):
    if response.method == "GET":
        notes = Note.objects.all()
        note = Note.objects.get(id=id)
        form = AddNoteForm(initial={"title": note.title, "content": note.content})
        return render(response, "main/notes.html", {"note": note, "form": form, "id": id, "notes": notes})