from django import forms

class UploadExcelStep1Form(forms.Form):
    fichier = forms.FileField()

GRAPH_TYPES = [
    ('line', 'Ligne'),
    ('bar', 'Barres'),
    ('pie', 'Camembert'),
]

class ExcelColumnMappingForm(forms.Form):
    colonne_x = forms.ChoiceField(label="Colonne des labels (X)")
    colonnes_y = forms.MultipleChoiceField(label="Colonnes des valeurs (Y)", widget=forms.CheckboxSelectMultiple)
    type_graphique = forms.ChoiceField(choices=GRAPH_TYPES)

    def __init__(self, *args, **kwargs):
        colonnes = kwargs.pop('colonnes', [])
        super().__init__(*args, **kwargs)
        self.fields['colonne_x'].choices = [(col, col) for col in colonnes]
        self.fields['colonnes_y'].choices = [(col, col) for col in colonnes]
