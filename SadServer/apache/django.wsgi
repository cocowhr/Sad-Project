# coding=gbk
import os
import sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)

sys.path.append("E:/SAD/Sad-Project/SadServer") #这个路径是项目主目录，如F:/mysite，一定要加上

os.environ['DJANGO_SETTINGS_MODULE'] = 'SadServer.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()