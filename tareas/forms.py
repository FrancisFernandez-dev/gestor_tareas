from django import forms

class TareaForm(forms.Form):
    titulo = forms.CharField(max_length=100, label="Título")
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label="Descripción",
        required=False
    )