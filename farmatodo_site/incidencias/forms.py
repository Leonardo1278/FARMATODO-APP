from django import forms
from .models import FactIncidences, DimSection

class formularioF(forms.ModelForm):
    main_section = forms.CharField(max_length=20, required=False)
    inner_section = forms.CharField(max_length=40, required=False)

    def __init__(self, *args, user_sections=None, **kwargs):
        super(formularioF, self).__init__(*args, **kwargs)
        # No es necesario filtrar por id_section aquí ya que se manejará en la vista

    def save(self, commit=True):
        instance = super(formularioF, self).save(commit=False)
        main_section = self.cleaned_data.get('main_section')
        inner_section = self.cleaned_data.get('inner_section')
        # Encuentra el DimSection correspondiente basado en main_section e inner_section
        dim_section = DimSection.objects.filter(main_section=main_section, inner_section=inner_section).first()
        if dim_section:
            instance.id_section = dim_section
        if commit:
            instance.save()
        return instance

    class Meta:
        model = FactIncidences
        fields = ('descrip', 'photo_1', 'photo_2', 'photo_3', 'urgency')
        labels = {
            'photo_1': 'Foto 1',
            'photo_2': 'Foto 2',
            'photo_3': 'Foto 3',
            'urgency': 'Urgencia',  # Asegúrate de que la etiqueta es lo que quieres mostrar
        }