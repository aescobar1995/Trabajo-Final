from django import forms


class FormSerie(forms.Form):
    codserie = forms.CharField(max_length=25)
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=30)
    plataforma = forms.CharField(max_length=30)
    fecha = forms.DateField()
    episodio = forms.IntegerField()
    temporada = forms.IntegerField()
    terminada = forms.BooleanField(required=False)
    sinopsis = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()