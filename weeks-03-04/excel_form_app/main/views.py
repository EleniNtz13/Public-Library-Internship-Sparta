from django.contrib.auth.decorators import login_required  # Import decorator to require login
from django.contrib import messages  # Import Django messaging framework
from django.shortcuts import render, redirect, get_object_or_404  # Import shortcuts for views
import pandas as pd  # Import pandas for Excel processing
from .forms import UploadExcelForm, CustomUserCreationForm, PersonForm  # Import app-specific forms
from .models import Person, UploadLog  # Import models
from django.contrib.auth.forms import UserCreationForm  # Import Django's built-in user creation form
from django.urls import reverse_lazy, reverse  # Import functions to handle URL reversing
from django.views.generic import CreateView  # Import generic class-based views
from .forms import PersonManualForm  # Import manual person form
from django.db.models.functions import Cast  # Import Cast function to cast fields
from django.db.models import Func  # Import base function class for custom DB functions
from django.db.models import IntegerField, Value  # Import field types and constant values
from django.http import HttpResponse, JsonResponse  # Import HTTP response classes
from django.template.loader import render_to_string  # Import template rendering function


@login_required
def autocomplete_title(request):  # Autocomplete titles for AJAX requests
    q = request.GET.get('q', '')  # Get the query parameter
    results = (  # Query distinct titles containing the query
        Person.objects.filter(titlos__icontains=q)
        .values_list('titlos', flat=True)
        .distinct()[:10]
    )
    return JsonResponse({'results': list(results)})  # Return JSON response


@login_required
def autocomplete_ekdoths(request):  # Autocomplete publishers for AJAX
    q = request.GET.get('q', '')  # Get the query parameter
    results = (  # Query distinct publishers containing the query
        Person.objects.filter(ekdoths__icontains=q)
        .values_list('ekdoths', flat=True)
        .distinct()[:10]
    )
    return JsonResponse({'results': list(results)})  # Return JSON response


def home(request):  # Render home page
    return render(request, 'home.html')


class SignUpView(CreateView):  # Class-based view for user sign-up
    form_class = CustomUserCreationForm  # Form used for registration
    success_url = reverse_lazy('login')  # Redirect to login after successful signup
    template_name = 'registration/signup.html'  # Template for signup page


def clean(value):  # Clean a generic cell value from Excel
    if pd.isna(value):  # Check for NaN
        return None
    return str(value).strip()  # Convert to string and strip whitespace


def clean_ari8mos(value):  # Clean entry number
    if pd.isna(value):  # Check for NaN
        return None
    try:
        return str(int(value))  # Convert numeric values like 115011.0 → "115011"
    except (ValueError, TypeError):
        return str(value).strip()  # Fallback to string stripping


@login_required
def show_people(request):  # Display list of people
    people = (  # Query all Person objects with valid IDs and order numerically
        Person.objects
        .exclude(ari8mosEisagoghs__isnull=True)
        .exclude(ari8mosEisagoghs__exact='')
        .annotate(
            ari8mos_int=Cast('ari8mosEisagoghs', IntegerField())  # Cast entry number to integer for ordering
        )
        .order_by('ari8mos_int')
    )

    return render(request, 'main/people.html', {'people': people})  # Render template with context


def generate_koha_from_author(author):  # Generate KOHA code from "surname,name"
    """
    Converts 'surname,name' → 'name surname'
    """
    if not author or "," not in author:  # Check for invalid input
        return None

    parts = author.split(",")  # Split surname and name
    if len(parts) != 2:
        return None

    surname = parts[0].strip()  # Get surname
    name = parts[1].strip()  # Get name

    if not surname or not name:  # Check for missing parts
        return None

    return f"{name} {surname}"  # Return "name surname"


@login_required
def upload_excel(request):  # Upload Excel file and process records
    if request.method == 'POST':  # Check if POST
        form = UploadExcelForm(request.POST, request.FILES)  # Bind form with POST data

        if form.is_valid():  # Validate form
            excel_file = request.FILES['excel_file']  # Get uploaded file
            df = pd.read_excel(excel_file)  # Read Excel into pandas DataFrame

            existing_ids = set(  # Get existing entry numbers from DB
                Person.objects.values_list('ari8mosEisagoghs', flat=True)
            )

            seen_in_file = set()  # Track duplicates within the same Excel

            added = []  # Track added records
            skipped = []  # Track skipped rows
            duplicates = []  # Track duplicates for resolution
            new_objects = []  # Store Person objects for bulk insert

            for index, row in df.iterrows():  # Iterate rows
                ari8mos = clean_ari8mos(row.get('ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'))  # Clean entry number
                syggrafeas = clean(row.get('ΣΥΓΓΡΑΦΕΑΣ'))  # Clean author
                koha = clean(row.get('ΣΥΓΓΡΑΦΕΑΣ KOHA'))  # Clean KOHA code

                if not koha and syggrafeas:  # Generate KOHA if missing
                    koha = generate_koha_from_author(syggrafeas)

                if not ari8mos:  # Skip missing entry numbers
                    skipped.append({
                        'row': index + 2,
                        'reason': 'Missing ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'
                    })
                    continue

                if ari8mos in seen_in_file:  # Skip duplicates in Excel
                    skipped.append({
                        'row': index + 2,
                        'reason': 'Duplicate ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ inside Excel'
                    })
                    continue
                seen_in_file.add(ari8mos)  # Mark as seen

                if ari8mos in existing_ids:  # Check duplicates in DB
                    existing_person = Person.objects.filter(ari8mosEisagoghs=ari8mos).first()

                    if not existing_person:  # Rare edge case: insert safely
                        new_objects.append(Person(
                            ari8mosEisagoghs=ari8mos,
                            hmeromhnia_eis=clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                            syggrafeas=syggrafeas,
                            koha=koha,
                            titlos=clean(row.get('ΤΙΤΛΟΣ')),
                            ekdoths=clean(row.get('ΕΚΔΟΤΗΣ')),
                            ekdosh=clean(row.get('ΕΚΔΟΣΗ')),
                            etosEkdoshs=clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                            toposEkdoshs=clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                            sxhma=clean(row.get('ΣΧΗΜΑ')),
                            selides=clean(row.get('ΣΕΛΙΔΕΣ')),
                            tomos=clean(row.get('ΤΟΜΟΣ')),
                            troposPromPar=clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                            ISBN=clean(row.get('ISBN')),
                            sthlh1=clean(row.get('Στήλη1')),
                            sthlh2=clean(row.get('Στήλη2')),
                        ))
                        existing_ids.add(ari8mos)
                        continue

                    duplicates.append({  # Store actual duplicates for later resolution
                        "left": {  # Existing record
                            "ari8mos": existing_person.ari8mosEisagoghs,
                            "hmeromhnia_eis": existing_person.hmeromhnia_eis,
                            "syggrafeas": existing_person.syggrafeas,
                            "koha": existing_person.koha,
                            "titlos": existing_person.titlos,
                            "ekdoths": existing_person.ekdoths,
                            "ekdosh": existing_person.ekdosh,
                            "etosEkdoshs": existing_person.etosEkdoshs,
                            "toposEkdoshs": existing_person.toposEkdoshs,
                            "sxhma": existing_person.sxhma,
                            "selides": existing_person.selides,
                            "tomos": existing_person.tomos,
                            "troposPromPar": existing_person.troposPromPar,
                            "ISBN": existing_person.ISBN,
                            "sthlh1": existing_person.sthlh1,
                            "sthlh2": existing_person.sthlh2,
                        },
                        "right": {  # New record
                            "ari8mos": ari8mos,
                            "hmeromhnia_eis": clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                            "syggrafeas": syggrafeas,
                            "koha": koha,
                            "titlos": clean(row.get('ΤΙΤΛΟΣ')),
                            "ekdoths": clean(row.get('ΕΚΔΟΤΗΣ')),
                            "ekdosh": clean(row.get('ΕΚΔΟΣΗ')),
                            "etosEkdoshs": clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                            "toposEkdoshs": clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                            "sxhma": clean(row.get('ΣΧΗΜΑ')),
                            "selides": clean(row.get('ΣΕΛΙΔΕΣ')),
                            "tomos": clean(row.get('ΤΟΜΟΣ')),
                            "troposPromPar": clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                            "ISBN": clean(row.get('ISBN')),
                            "sthlh1": clean(row.get('Στήλη1')),
                            "sthlh2": clean(row.get('Στήλη2')),
                        },
                    })
                    continue

                new_objects.append(Person(  # Safe insert if no duplicates
                    ari8mosEisagoghs=ari8mos,
                    hmeromhnia_eis=clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                    syggrafeas=syggrafeas,
                    koha=koha,
                    titlos=clean(row.get('ΤΙΤΛΟΣ')),
                    ekdoths=clean(row.get('ΕΚΔΟΤΗΣ')),
                    ekdosh=clean(row.get('ΕΚΔΟΣΗ')),
                    etosEkdoshs=clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                    toposEkdoshs=clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                    sxhma=clean(row.get('ΣΧΗΜΑ')),
                    selides=clean(row.get('ΣΕΛΙΔΕΣ')),
                    tomos=clean(row.get('ΤΟΜΟΣ')),
                    troposPromPar=clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                    ISBN=clean(row.get('ISBN')),
                    sthlh1=clean(row.get('Στήλη1')),
                    sthlh2=clean(row.get('Στήλη2')),
                ))
                existing_ids.add(ari8mos)

                added.append({  # Track added record for reporting
                    'ari8mos': ari8mos,
                    'titlos': clean(row.get('ΤΙΤΛΟΣ')),
                    'syggrafeas': syggrafeas,
                })

            Person.objects.bulk_create(new_objects, batch_size=1000)  # Bulk insert new Person records

            request.session['duplicates'] = duplicates  # Store duplicates in session for next step

            UploadLog.objects.create(  # Log the upload
                user=request.user,
                filename=excel_file.name,
                rows_added=len(new_objects),
                rows_updated=0,
            )

            total_records = Person.objects.count()  # Total records after upload

            return render(request, 'upload_result.html', {  # Render upload results
                'added_count': len(new_objects),
                'duplicate_count': len(duplicates),
                'skipped_count': len(skipped),
                'total_records': total_records,
            })

    else:
        form = UploadExcelForm()  # Render empty form for GET

    return render(request, 'upload_excel.html', {'form': form})  # Render upload template

@login_required
def resolve_duplicates(request):  # Display the list of duplicates for resolution
    duplicates = request.session.get('duplicates', [])  # Get duplicates stored in session

    if not duplicates:  # If no duplicates remain
        return render(
            request,
            'main/duplicates_done.html'  # Show completion template
        )

    current = duplicates[0]  # Get the first duplicate for display
    return render(request, 'main/duplicates.html', {'duplicates': duplicates})  # Render duplicates template


@login_required
def handle_duplicate(request):  # Handle user's action on a single duplicate
    if request.method != "POST":  # Only allow POST
        return redirect("resolve_duplicates")  # Redirect if not POST

    ari8mos = request.POST.get("ari8mos")  # Get entry number of duplicate
    action = request.POST.get("action")  # Get action: edit or skip

    if not ari8mos or not action:  # Validate inputs
        return redirect("resolve_duplicates")

    duplicates = request.session.get("duplicates", [])  # Get current duplicates from session

    dup = next(  # Find the specific duplicate record
        (d for d in duplicates if str(d["left"]["ari8mos"]) == str(ari8mos)),
        None
    )

    if not dup:  # If duplicate not found, redirect
        return redirect("resolve_duplicates")

    duplicates.remove(dup)  # Remove the handled duplicate from session
    request.session["duplicates"] = duplicates  # Update session

    if action == "edit":  # If user chose to edit
        return redirect(
            f"{reverse('edit_person', args=[ari8mos])}?next=duplicates"  # Redirect to edit page with return flag
        )

    # If action is "skip"
    return redirect("resolve_duplicates")  # Continue resolving next duplicates


@login_required
def skip_all_duplicates(request):  # Skip all remaining duplicates
    if request.method == "POST":  # Only allow POST
        request.session['duplicates'] = []  # Clear duplicates in session
        return redirect('show_people')  # Redirect to people list
    return redirect('resolve_duplicates')  # Fallback redirect


@login_required
def edit_person(request, pk):  # Edit a Person record
    person = get_object_or_404(Person, pk=pk)  # Get person or 404
    next_url = request.GET.get('next')  # Optional redirect parameter

    if request.method == 'POST':  # Handle form submission
        form = PersonForm(request.POST, instance=person)  # Bind form to POST data
        if form.is_valid():  # Validate
            form.save()  # Save changes
            messages.success(request, "Record updated successfully.")  # Show success message
            if next_url == 'duplicates':  # Redirect back to duplicates if flagged
                return redirect('resolve_duplicates')
            return redirect('show_people')  # Otherwise go to people list
    else:
        form = PersonForm(instance=person)  # Render form with current instance

    return render(request, 'main/edit_person.html', {'form': form, 'person': person})  # Render edit template


class RegexpReplace(Func):  # Custom database function for regex replacement
    function = 'REGEXP_REPLACE'  # SQL function name
    arity = 3  # Number of arguments expected


@login_required
def add_person(request):  # Add a new Person manually
    last_number = (  # Determine the next available entry number
        Person.objects
        .exclude(ari8mosEisagoghs__isnull=True)
        .exclude(ari8mosEisagoghs__exact='')
        .annotate(
            clean_num=Cast(
                RegexpReplace(  # Remove decimal parts
                    'ari8mosEisagoghs',
                    Value(r'\..*$'),  # Regex pattern
                    Value('')  # Replace with empty string
                ),
                IntegerField()  # Cast result to integer
            )
        )
        .order_by('-clean_num')  # Get highest number
        .values_list('clean_num', flat=True)
        .first()
    )

    next_number = (last_number or 0) + 1  # Next entry number

    submitted = request.GET.get("submitted") == "1"  # Flag to show confirmation

    if request.method == 'POST':  # Handle form submission
        form = PersonManualForm(request.POST)
        if form.is_valid():  # Validate form
            person = form.save(commit=False)  # Create but don't save yet
            person.ari8mosEisagoghs = str(next_number)  # Assign next entry number
            person.save()  # Save new Person

            return redirect(f"{reverse('add_person')}?submitted=1")  # Redirect with confirmation flag
    else:
        form = PersonManualForm()  # Render empty form

    return render(  # Render template
        request,
        'main/add_person.html',
        {
            'form': form,  # Form instance
            'next_number': next_number,  # Display next entry number
            'submitted': submitted,  # Show confirmation message if submitted
        }
    )
