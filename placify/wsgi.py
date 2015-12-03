"""
WSGI config for placify project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# activate_this = '/home/vagrant/project/placify/bin/activate_this.py'

# exec(open(activate_this).read())

import os, sys, time, signal

from django.core.wsgi import get_wsgi_application

path = '/home/vagrant/project/placify/lib/python-3.4/site-packages'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "placify.settings")

application = get_wsgi_application()

# try:
#     application = get_wsgi_application()
# except Exception:
#     time.sleep(0.25)
#     os.kill(os.getpid(), signal.SIGINT)

# if path not in sys.path:
#     sys.path.append(path)
#
# if os.environ['mod_wsgi.process_group'] != '':
#    import signal, os
#    os.kill(os.getpid(), signal.SIGINT)
#
