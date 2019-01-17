<!DOCTYPE html>

{% load staticfiles %} <!-- New line -->

<html>

    <head>
    
        <title>Rango</title>
        
    </head>
    
    <body>
    
        <h1>Rango says...</h1>
        
        <div>
            hey there partner! <br />

            <strong>This tutorial has been put together by JK.</strong><br />

        </div>

        <div>
        
            <a href="/rango/">About</a><br />

            <img src="{% static "images/cat.jpg" %}"
                            alt="Picture of a cat" /> <!-- New line -->

        </div>

        </body>
</html>
