from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import EncryptedFile, FileTransfer
from .forms import FileUploadForm, FileTransferForm
from .services.encryption_service import EncryptionService

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_type = form.cleaned_data['file_type']
            
            try:
                # Read file data
                file_data = uploaded_file.read()
                
                # Generate encryption key and encrypt file
                key = EncryptionService.generate_key()
                encrypted_data = EncryptionService.encrypt_file(file_data, key)
                
                # Create encrypted file record
                encrypted_file = EncryptedFile(
                    user=request.user,
                    original_filename=uploaded_file.name,
                    encrypted_file=encrypted_data,
                    file_type=file_type,
                    file_size=uploaded_file.size,
                    encryption_key=key
                )
                encrypted_file.save()
                
                messages.success(request, f'File "{uploaded_file.name}" uploaded and encrypted successfully!')
                return redirect('files:file_list')
                
            except Exception as e:
                messages.error(request, f'Error uploading file: {str(e)}')
    else:
        form = FileUploadForm()
    
    return render(request, 'files/upload.html', {'form': form})

@login_required
def file_list(request):
    files = EncryptedFile.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'files/file_list.html', {'files': files})

@login_required
def file_detail(request, file_id):
    file = get_object_or_404(EncryptedFile, id=file_id, user=request.user)
    return render(request, 'files/file_detail.html', {'file': file})

@login_required
def download_file(request, file_id):
    file = get_object_or_404(EncryptedFile, id=file_id, user=request.user)
    
    try:
        # Decrypt the file
        decrypted_data = EncryptionService.decrypt_file(
            file.encrypted_file, 
            file.encryption_key
        )
        
        # Create response with decrypted file
        response = HttpResponse(decrypted_data, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file.original_filename}"'
        return response
        
    except Exception as e:
        messages.error(request, f'Error downloading file: {str(e)}')
        return redirect('files:file_list')