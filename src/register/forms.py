from django import forms
#from distutils.tests.test_archive_util import UID_GID_SUPPORT


class UploadFileForm(forms.Form):
    docfile = forms.FileField(
        label='upload a file',
        help_text='unzip your file to .txt before uploading'
    )
    
