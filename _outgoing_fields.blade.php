@csrf

<div class="mb-3">
    <label>Α/Α</label>
    <input type="number" class="form-control" name="id_number" value="{{ old('id_number') }}" required>
</div>

<div class="mb-3">
    <label>Αρχή στην οποία απευθύνεται</label>
    <input type="text" class="form-control" name="destination_authority" value="{{ old('destination_authority') }}" required>
</div>

<div class="mb-3">
    <label>Περίληψη εξερχομένου εγγράφου</label>
    <textarea class="form-control" name="summary">{{ old('summary') }}</textarea>
</div>

<div class="mb-3">
    <label>Χρονολογία</label>
    <input type="number" class="form-control" name="document_year" value="{{ old('document_year') }}" required>
</div>

<div class="mb-3">
    <label>Σχετικοί αριθμοί</label>
    <input type="text" class="form-control" name="related_numbers" value="{{ old('related_numbers') }}">
</div>

<div class="mb-3">
    <label>Φάκελος αρχείου</label>
    <input type="text" class="form-control" name="file_folder" value="{{ old('file_folder') }}">
</div>

<div class="mb-3">
    <label>Παρατηρήσεις</label>
    <textarea class="form-control" name="notes">{{ old('notes') }}</textarea>
</div>
