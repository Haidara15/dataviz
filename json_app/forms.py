# forms.py
from django import forms
from .models import HighchartData, Theme

class HighchartDataForm(forms.ModelForm):
    labels = forms.CharField(label="Labels",
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                              help_text="Exemple de liste de modalités à saisir :  ['A','B','C'] avec les crochets")

    values = forms.CharField(label="Valeurs",
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                              help_text="Exemple de liste de valeurs à saisir : [100,200,300] avec les crochets")

    show_legend = forms.BooleanField(label="Afficher la légende", required=False)

    
    legend_position = forms.ChoiceField(label="Position de la légende : haut, bas ..",  
                                     choices=[('top', 'Haut'), ('bottom', 'Bas')],
                                     widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = HighchartData
        fields = ['title', 'chart_type', 'labels', 'values', 'x_axis_title', 'y_axis_title', 'show_legend','legend_position']
        labels = {
            'title': 'Titre',
            'chart_type': 'Type de graphique',
            'x_axis_title': 'Titre des abscisses',
            'y_axis_title': 'Titre des ordonnées',
            'show_legend': 'Afficher la légende',
            'legend_position':'Positon : haut, bas ..'
            
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'chart_type': forms.Select(attrs={'class': 'form-control'}),
            'x_axis_title': forms.TextInput(attrs={'class': 'form-control'}),
            'y_axis_title': forms.TextInput(attrs={'class': 'form-control'}),
        }


        







class ThemeForm(forms.ModelForm):
    title = forms.CharField(label="Titre de la thématique ",
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = Theme
        fields = ['title']
