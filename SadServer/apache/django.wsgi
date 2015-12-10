# coding=gbk
import os
import sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)

sys.path.append("E:/SAD/Sad-Project/SadServer")

os.environ['DJANGO_SETTINGS_MODULE'] = 'SadServer.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()