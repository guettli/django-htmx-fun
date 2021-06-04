from django.http import HttpResponse
from django.utils.html import format_html

def page(content):
    return HttpResponse(format_html('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Diary</title>
    <style>
        input, textarea {{
            display: block;
        }}
    </style>
</head>

<body>
{content}
</body>

<script src="https://unpkg.com/htmx.org@1.4.1/dist/htmx.min.js" 
    integrity="sha384-1P2DfVFAJH2XsYTakfc6eNhTVtyio74YNA1tc6waJ0bO+IfaexSWXc2x62TgBcXe" 
    crossorigin="anonymous"></script>

</html>
''', content=content))