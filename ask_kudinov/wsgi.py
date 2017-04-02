

def simple_app(environ, start_response):
    param = environ['QUERY_STRING'].split('&')
    d = {y[0] : y[1] for y in [ x.split('=') for x in param ] }
    for x in param: y = x.split('=')
    d[y[0]] = y[1]
    resp = "<html><body><h3>GET</h3><table>"
    for k,v in d.items():
        resp += "<tr><td>"+k+"</td><td>"+v+"</td></tr>"
    resp+="</table></body></html>"
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [ bytes(resp) ]

class AppClass:
    """Produce the same output, but using a class

    (Note: 'AppClass' is the "application" here, so calling it
    returns an instance of 'AppClass', which is then the iterable
    return value of the "application callable" as required by
    the spec.

    If we wanted to use *instances* of 'AppClass' as application
    objects instead, we would have to implement a '__call__'
    method, which would be invoked to execute the application,
    and we would need to create an instance for use by the
    server or gateway.
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
