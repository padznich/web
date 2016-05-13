
def application(environ, start_response):

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

    body = environ['QUERY_STRING']

    # return ["%s=%s<br/>" % (k, body[k][0]) for k in body]
    return ["\n".join(item for item in body.split('&'))]
