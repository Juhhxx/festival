# festival

## 1ª Alteração - Correção do ficheiro views

- Corrigi `from .model import Palco` para `from .models import *` de forma a importar todos os modelos existentes de uma vez.

- Corrigi em concerto_view `concerto =` para `concerto = Concerto.objects.get(id = id)`.

- Adicionei `dias_view` com o seguinte código:

    ```python
    def palcos_view(request):
        palcos = Palco.objects.all()

        context = {'palcos': palcos}

        return render(request, 'festival/palcos.html', context)
    ```

## 2ª Alteração - Correção do ficheiro urls

- Adicionei o path  path('dias/', views.dias_view, name='dias'), à lista `urlpatters`.

## 3ª Alteração - Criação do template dias

- Adicionei o template `dias.html` baseado em `palcos.html`, com o seguinte código:

    ```python
    {% extends 'festival/layout.html' %}

    {% block content %}
        
    {% for dia in dias %}
    <h3>{{dia}}</h3>

        {% for concerto in dia.concertos.all %}
            <article class="card">
                <a href="">{{ concerto.banda.nome }} - {{ concerto.palco }}</a>
            </article>
        {% endfor %}

    {% endfor %}

    {% endblock %}
    ```

## 4ª Alteração - Adição das hrefs corretas aos botões

- Adicionei a href `% url 'concerto' concerto.id %` aos botões dos concertos no template `dias.html` e `palcos.html`, de forma a redirecionar para o template `concerto.html`.