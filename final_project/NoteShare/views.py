from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from .form import NoteForm, ShareForm

@login_required
def dashboard(request):
    user_notes = Note.objects.filter(creator=request.user)
    shared_notes = Note.objects.filter(shared_with=request.user)
    note_shares = {}
    for n in user_notes:
        shares = Note.shared_with.through.objects.filter(note_id=n.id)
        note_shares[n] = []
        for s in shares:
            note_shares[n].append(s)
    data = {
        'user': request.user,
        'notes': user_notes,
        'shared': shared_notes,
        'users_shared_with': note_shares
    }
    return render(request, 'dashboard.html', data)

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            message_text = form.cleaned_data.get('message')
            note = Note()
            note.message = message_text
            note.title = title
            note.creator = request.user
            note.save()

            return redirect('NoteShare:dashboard')
    else:
        form = NoteForm()

    return render(request, 'create_note.html', {'form': form})

@login_required
def edit_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        print(form)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            message_text = form.cleaned_data.get('message')
            #shared_user = form.cleaned_data.get('shared_with')
            note.message = message_text
            note.title = title
            note.creator = request.user
            #note.shared_with = shared_user
            note.save()

            return redirect('NoteShare:dashboard')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})

@login_required
def share_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            shared_users = form.cleaned_data.get('shared_with')
            for e in shared_users:
                note.shared_with.add(e.id)
        return redirect('NoteShare:dashboard')
    else:
        form = ShareForm(user=request.user)

    return render(request, 'share_note.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        note.delete()

        return redirect('NoteShare:dashboard')
    else:
        shares = Note.shared_with.through.objects.filter(note_id=note_id)
        note_shares = []
        for s in shares:
            note_shares.append(s)
        data = {
            'title': note.title,
            'message': note.message,
            'users_shared_with': note_shares
        }
        return render(request, 'delete_note.html', data)

@login_required
def hide_note(request, note_id):
    shared_note = Note.shared_with.through.objects.filter(note_id=note_id, user=request.user)
    shared_note.delete()

    return redirect('NoteShare:dashboard')



