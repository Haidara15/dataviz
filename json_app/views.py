# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Theme, HighchartData
from .forms import HighchartDataForm, ThemeForm
import json
from django.contrib import messages


def create_theme(request):
    if request.method == "POST":
        form = ThemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('theme_list')
    else:
        form = ThemeForm()
    return render(request, 'json_app/create_theme.html', {'form': form})

def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'json_app/theme_list.html', {'themes': themes})


def redirect_to_chart(request, theme_slug):
    theme = get_object_or_404(Theme, slug=theme_slug)
    charts = theme.charts.all()
    if charts.exists():
        first_chart = charts.first()
        return redirect('chart_detail', theme_slug=theme_slug, pk=first_chart.pk)
    else:
        return redirect('create_chart_data', theme_slug=theme_slug)
    


# views.py
def create_chart_data(request, theme_slug):
    theme = get_object_or_404(Theme, slug=theme_slug)
    if request.method == "POST":
        form = HighchartDataForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.theme = theme  # Assurez-vous de définir le thème
            instance.labels = form.cleaned_data['labels']
            instance.values = form.cleaned_data['values']
            instance.save()
            # return redirect('theme_charts', theme_slug=theme_slug, pk=instance.pk)
            return redirect('theme_charts', theme_slug=theme_slug)
    else:
        form = HighchartDataForm()
    return render(request, 'json_app/create_chart_data.html', {'form': form, 'theme': theme})






def edit_chart_data(request, theme_slug, pk):
    chart = get_object_or_404(HighchartData, pk=pk)
    if request.method == "POST":
        form = HighchartDataForm(request.POST, instance=chart)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.labels = form.cleaned_data['labels']
            instance.values = form.cleaned_data['values']
            instance.save()
            # return redirect('chart_detail', theme_slug=theme_slug, pk=chart.pk)
            return redirect('theme_charts', theme_slug=theme_slug)
    else:
        form = HighchartDataForm(instance=chart)
    return render(request, 'json_app/edit_chart_data.html', {'form': form, 'chart': chart})


def chart_detail(request, theme_slug, pk):
    chart = get_object_or_404(HighchartData, pk=pk)
    labels = json.loads(chart.labels)
    values = json.loads(chart.values)
    values = [float(value) for value in values]
    if chart.chart_type == 'pie':
        values = [{'name': label, 'y': value} for label, value in zip(labels, values)]
    labels_json = json.dumps(labels)
    data_json = json.dumps(values)
    return render(request, 'json_app/chart_detail.html', {
        'chart': chart,
        'labels_json': labels_json,
        'data_json': data_json
    })


def chart_list(request):
    charts = HighchartData.objects.all()
    return render(request, 'json_app/chart_list.html', {'charts': charts})


# views.py
import json
import ast
from django.shortcuts import render, get_object_or_404
from .models import Theme  # Assure-toi d'importer le bon modèle

def theme_charts(request, theme_slug):
    theme = get_object_or_404(Theme, slug=theme_slug)
    charts = theme.charts.all().order_by('-modified_at', '-id')
    charts_data = []

    for chart in charts:
        try:
            try:
                labels = json.loads(chart.labels)
            except json.JSONDecodeError:
                labels = ast.literal_eval(chart.labels)

            try:
                values = json.loads(chart.values)
            except json.JSONDecodeError:
                values = ast.literal_eval(chart.values)

            values = [float(value) for value in values]

            if chart.chart_type == 'pie':
                values = [{'name': label, 'y': value} for label, value in zip(labels, values)]

            charts_data.append({
                'chart': chart,
                'labels_json': json.dumps(labels),
                'data_json': json.dumps(values)
            })
        except Exception as e:
            print(f"Erreur lors du traitement du chart ID {chart.id} : {e}")
            continue  # Ignore ce chart s’il y a un souci

    return render(request, 'json_app/theme_charts.html', {
        'theme': theme,
        'charts_data': charts_data
    })








def delete_chart_data(request, theme_slug, pk):
    chart = get_object_or_404(HighchartData, pk=pk)
    chart.delete()
    messages.success(request, "La figure a été supprimée avec succès.")
    return redirect('theme_charts', theme_slug=theme_slug)







def delete_theme(request, theme_slug):
    theme = get_object_or_404(Theme, slug=theme_slug)
    theme.delete()
    messages.success(request, "Le thème et toutes ses figures associées ont été supprimés avec succès.")
    return redirect('theme_list')



def delete_theme(request, theme_slug):
    theme = get_object_or_404(Theme, slug=theme_slug)
    theme.delete()
    messages.success(request, "Le thème et toutes ses figures associées ont été supprimés avec succès.")
    return redirect('theme_list')




def edit_theme(request, theme_slug):
    theme = get_object_or_404(Theme, slug=theme_slug)
    if request.method == 'POST':
        form = ThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            messages.success(request, "Le thème a été modifié avec succès.")
            return redirect('theme_list')
    else:
        form = ThemeForm(instance=theme)
    return render(request, 'json_app/edit_theme.html', {'form': form})




