from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize= value.size
    
    if filesize >  5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')