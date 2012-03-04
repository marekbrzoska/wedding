#-*- coding=utf-8 -*-                                                                                                                                                                                                                        
import sys, os
import django.core.handlers.wsgi
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
 
 

# zapamiętaj katalog bieżącego pliku w ścieżce
this_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(this_dir)
#przejdź do fizzer
os.chdir(this_dir)
os.chdir('..')
# żeby można było pisać fizzer.cośtam
sys.path.append(os.getcwd())
 
application = django.core.handlers.wsgi.WSGIHandler() 
