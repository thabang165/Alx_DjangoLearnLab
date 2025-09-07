# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page or another page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
# LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# LibraryProject/relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Make sure you have a ModelForm for Book

# List books (no permission needed)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Add book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# Delete book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
