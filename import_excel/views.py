from django.shortcuts import render

import pandas as pd
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from django.http import JsonResponse
from json_app.models import Theme, HighchartData
from .forms import UploadExcelStep1Form, ExcelColumnMappingForm

def importer_graphique(request, slug):
    theme = get_object_or_404(Theme, slug=slug)

    if request.method == 'POST':
        if request.POST.get('step') == '2':
            colonnes = request.session.get('colonnes_excel')
            chemin_fichier = request.session.get('chemin_fichier')

            form = ExcelColumnMappingForm(request.POST, colonnes=colonnes)
            if form.is_valid():
                df = pd.read_excel(chemin_fichier)
                x = form.cleaned_data['colonne_x']
                ys = form.cleaned_data['colonnes_y']
                chart_type = form.cleaned_data['type_graphique']

                labels = df[x].tolist()

                for y_col in ys:
                    values = df[y_col].tolist()
                    chart = HighchartData.objects.create(
                        theme=theme,
                        title=f"{y_col} (importé)",
                        chart_type=chart_type,
                        labels=json.dumps(labels),
                        values=json.dumps(values)
                    )

                default_storage.delete(chemin_fichier)
                for key in ['colonnes_excel', 'chemin_fichier']:
                    request.session.pop(key, None)

                return redirect('theme_charts', theme_slug=slug)
        else:
            form1 = UploadExcelStep1Form(request.POST, request.FILES)
            if form1.is_valid():
                fichier = form1.cleaned_data['fichier']
                chemin_fichier = default_storage.save(f'temp/{fichier.name}', fichier)
                df = pd.read_excel(default_storage.path(chemin_fichier))
                colonnes = df.columns.tolist()

                request.session['colonnes_excel'] = colonnes
                request.session['chemin_fichier'] = default_storage.path(chemin_fichier)

                form2 = ExcelColumnMappingForm(colonnes=colonnes)
                return render(request, 'import_excel/choix_colonnes.html', {'form': form2, 'theme': theme})

    else:
        form1 = UploadExcelStep1Form()

    return render(request, 'import_excel/upload_excel.html', {'form': form1, 'theme': theme})

def preview_graph_api(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        x_col = payload.get('colonne_x')
        y_cols = payload.get('colonnes_y', [])
        graph_type = payload.get('type_graphique')
        chemin_fichier = request.session.get('chemin_fichier')

        df = pd.read_excel(chemin_fichier)
        labels = df[x_col].tolist()
        datasets = [{
            'label': col,
            'data': df[col].tolist(),
            'type': graph_type
        } for col in y_cols]

        return JsonResponse({'labels': labels, 'datasets': datasets})

