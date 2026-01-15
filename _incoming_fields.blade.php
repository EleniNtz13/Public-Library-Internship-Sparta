@csrf

<div class="mb-3">
    <label>Α/Α</label>
    <input type="number" class="form-control" name="id_number" value="{{ old('id_number') }}" required>
</div>

<div class="mb-3">
    <label>Ημερομηνία παραλαβής</label>
    <input type="date" class="form-control" name="received_date" value="{{ old('received_date') }}" required>
</div>

<div class="mb-3">
    <label>Αριθμός εισερχομένου εγγράφου</label>
    <input type="text" class="form-control" name="protocol_number" value="{{ old('protocol_number') }}" required>
</div>

<div class="mb-3">
    <label>Τόπος που εκδόθηκε</label>
    <input type="text" class="form-control" name="place_issued" value="{{ old('place_issued') }}">
</div>

<div class="mb-3">
    <label>Αρχή που το έχει εκδόσει</label>
    <input type="text" class="form-control" name="issuing_authority" value="{{ old('issuing_authority') }}">
</div>

<div class="mb-3">
    <label>Χρονολογία εγγράφου</label>
    <input type="number" class="form-control" name="document_year" value="{{ old('document_year') }}" required>
</div>

<div class="mb-3">
    <label>Περίληψη</label>
    <textarea class="form-control" name="summary">{{ old('summary') }}</textarea>
</div>

<div class="mb-3">
    <label>Φάκελος αρχείου</label>
    <input type="text" class="form-control" name="file_folder" value="{{ old('file_folder') }}">
</div>
