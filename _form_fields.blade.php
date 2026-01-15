@csrf

<label>Αριθμός Πρωτοκόλλου</label>
<input type="number" name="protocol_number" value="{{ old('protocol_number') }}" required><br>

<label>Χρονολογία</label>
<input type="number" name="protocol_year" value="{{ old('protocol_year') }}" required><br>

<label>Ημερομηνία εγγράφου</label>
<input type="date" name="document_date" value="{{ old('document_date') }}" required><br>

<label>Περίληψη</label>
<textarea name="summary">{{ old('summary') }}</textarea><br>

<label>Αρχείο (path)</label>
<input type="text" name="file_path" value="{{ old('file_path') }}"><br>

<label>Παρατηρήσεις</label>
<textarea name="notes">{{ old('notes') }}</textarea><br>

<input type="hidden" name="user_id" value="1">
