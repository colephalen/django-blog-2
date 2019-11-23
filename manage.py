#!/usr/bin/env python
# django_blog_2/manage.py
# google client id:
# 852917162048-1l90v70mp7hmksci88iqpq8o1agut1ih.apps.googleusercontent.com
# google secret client
# ybYWCGjvQpxRDWWeb_Qz4oQU
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
