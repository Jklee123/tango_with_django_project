<!DOCTYPE html>
<html>
    <head>
    <title>Rango</title>
    </head>

    <body>
        {% if category %}
        <h1>Add a Page to {{ category.name }} </h1>
        <div>
            <form id="page_form" method="post" action="/rango/category/{{ category.slug }}/add_page/">
                {% csrf_token %}
                {% for hidden in form.hidden_fields %}
                    {{ hidden }}
                {% endfor %}
                {% for field in form.visible_fields %}
                    {{ field.errors }}
                    {{ field.help_text }}
                    {{ field }}
                {% endfor %}
                <input type="submit" name="submit" value="Create Page" />
            </form>
        {% else %}
            A category by this name does not exist.
        {% endif %}
        </div>
    </body>
</html>
