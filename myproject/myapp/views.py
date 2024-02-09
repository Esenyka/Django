#from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

about_html = """<!DOCTYPE html>
<html>
  <body>
    <header>
    <h1>This is the page about me</h1>
    <main>
        <h1>I am a student</h1>
    </main>
    </header>
  </body>
</html>"""

index_html = """<!DOCTYPE html>
<html>
  <body>
    <header>
    <h1>This page is the home page</h1>
    <main>
        <h1>You can visit a page about me</h1>
    </main>
    </header>
  </body>
</html>"""


def index(request):
    logger.info("Opened home page")
    return HttpResponse(index_html)


def about(request):
    logger.info("Opened page about")
    return HttpResponse(about_html)

