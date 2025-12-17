import pandas as pd
import datetime
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def show_books(request):
    books = Book.objects.all()
    return render(request, 'excel_data/book_list.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request, 'excel_data/add_book.html', {'form': form})


def upload_excel(request):
    if request.method == "POST" and request.FILES.get('file'):
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file)

        for index, row in df.iterrows():
            # --- entry_date safe parsing ---
            entry_date_value = row.get('entry_date')

            if pd.notnull(entry_date_value):
                if isinstance(entry_date_value, datetime.datetime):
                    entry_date_value = entry_date_value.date()
                elif hasattr(entry_date_value, 'to_pydatetime'):
                    entry_date_value = entry_date_value.to_pydatetime().date()
                else:
                    try:
                        entry_date_value = pd.to_datetime(entry_date_value).date()
                    except Exception:
                        entry_date_value = None
            else:
                entry_date_value = None

            Book.objects.create(
                entry_number=row.get('entry_number'),
                entry_date=entry_date_value,
                author=row.get('author'),
                koha_author=row.get('koha_author'),
                title=row.get('title'),
                publisher=row.get('publisher'),
                edition=row.get('edition'),
                publish_year=row.get('publish_year'),
                publish_place=row.get('publish_place'),
                shape=row.get('shape'),
                pages=row.get('pages'),
                volume=row.get('volume'),
                notes=row.get('notes'),
                isbn=row.get('isbn'),
                column1=row.get('column1'),
                column2=row.get('column2'),
            )

        return redirect('show_books')

    return render(request, 'excel_data/upload_excel.html')
