from django.core.management.base import BaseCommand
import pandas as pd
from main.models import Book

def parse_date(value):
    if pd.isna(value):
        return None
    try:
        if isinstance(value, pd.Timestamp):
            return value.date()
        return pd.to_datetime(value).date()
    except Exception:
        return None

def safe_int(value):
    try:
        if pd.isna(value):
            return None
        return int(value)
    except Exception:
        return None

class Command(BaseCommand):
    help = "Import books data from Excel into PostgreSQL"

    def handle(self, *args, **options):
        df = pd.read_excel('main/excel_data/data.xlsx')

        print("Columns:", df.columns.tolist())
        print(df.head())

        books = []
        for _, row in df.iterrows():
            book = Book(
                entry_number=safe_int(row.get('entry_number')),
                entry_date=parse_date(row.get('entry_date')),
                author=row.get('author') if not pd.isna(row.get('author')) else None,
                koha_author=row.get('koha_author') if not pd.isna(row.get('koha_author')) else None,
                title=row.get('title') if not pd.isna(row.get('title')) else None,
                publisher=row.get('publisher') if not pd.isna(row.get('publisher')) else None,
                edition=row.get('edition') if not pd.isna(row.get('edition')) else None,
                publish_year=safe_int(row.get('publish_year')),
                publish_place=row.get('publish_place') if not pd.isna(row.get('publish_place')) else None,
                shape=row.get('shape') if not pd.isna(row.get('shape')) else None,
                pages=str(row.get('pages')) if not pd.isna(row.get('pages')) else None,
                volume=row.get('volume') if not pd.isna(row.get('volume')) else None,
                notes=row.get('notes') if not pd.isna(row.get('notes')) else None,
                isbn=row.get('isbn') if not pd.isna(row.get('isbn')) else None,
                column1=row.get('column1') if not pd.isna(row.get('column1')) else None,
                column2=row.get('column2') if not pd.isna(row.get('column2')) else None
            )
            books.append(book)

        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS("✔ Successfully imported all books!"))
