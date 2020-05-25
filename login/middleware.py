import re

from django.http import HttpResponse


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # print("自定义中间件！")
        path = request.path
        # print(path)
        exclude_path = ['/login/denglu/']

        if (re.match('/login/', path) or re.match('/article/', path)) and path not in exclude_path:
            userid = request.session.get('userid', None)
            if not userid:
                return HttpResponse("<script>alert('尚未登录！'); window.location='/login/denglu/'</script>")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response