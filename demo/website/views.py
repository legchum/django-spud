from django.shortcuts import get_object_or_404, redirect, render
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'index.html', context)

def newnote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = NoteForm()

    context = {
        'form': form
    }
    return render(request, 'newnote.html', context)


def cool_picture(request):
    context = {
        'title': 'Cool Picture',
        'description': 'This is a cool picture.'
    }
    return render(request, 'cool_picture.html', context)

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.delete()
        return redirect('')

    return redirect('')
