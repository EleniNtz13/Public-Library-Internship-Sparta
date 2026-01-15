<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Document extends Model
{
    use HasFactory;

    protected $fillable = [
        'protocol_number',
        'protocol_year',
        'received_date',
        'document_number',
        'issued_place',
        'issued_by',
        'document_year',
        'summary',
        'addressed_to',
        'file_path',
        'notes',
        'user_id',
    ];
}
