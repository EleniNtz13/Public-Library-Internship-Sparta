@extends('layouts.app')

@section('content')

<h1 class="mb-4 text-center">Εισαγωγή Εγγράφων</h1>

@if(session('success'))
<div class="alert alert-success">{{ session('success') }}</div>
@endif

<!-- Εισερχόμενα -->
<div class="card mb-4">
    <div class="card-header bg-primary text-white">
        Εισερχόμενα Έγγραφα
    </div>
    <div class="card-body">
        <form action="/documents/incoming" method="POST">
            @include('documents._incoming_fields')
            <button type="submit" class="btn btn-primary mt-2">Αποθήκευση Εισερχόμενου</button>
        </form>
    </div>
</div>

<!-- Εξερχόμενα -->
<div class="card mb-4">
    <div class="card-header bg-success text-white">
        Εξερχόμενα Έγγραφα
    </div>
    <div class="card-body">
        <form action="/documents/outgoing" method="POST">
            @include('documents._outgoing_fields')
            <button type="submit" class="btn btn-success mt-2">Αποθήκευση Εξερχόμενου</button>
        </form>
    </div>
</div>

@endsection
