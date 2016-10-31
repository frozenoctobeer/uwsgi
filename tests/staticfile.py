import sys

content_type = 'image/jpeg'
filename = 'logo_uWSGI.jpg'

try:
    filename = sys.argv[1]
except IndexError:
    pass

try:
    content_type = sys.argv[2]
except IndexError:
    pass


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', content_type)])
    fd = open(filename, 'r')
    yield environ['wsgi.file_wrapper'](fd, 1024*1024)
