
# middleware.py
class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # List of domains allowed to embed the website in an iframe
        allowed_domains = [
            "https://kpyx.co",
            "https://www.kpyx.co",
            "https://185.100.87.158:8000",
            "https://kpyx.io",
            "https://www.kpyx.io",
            "https://www.krmp.io",
            "https://krmp.io",
            "https://2krk.site",
            "https://portfolio-gzbf.onrender.com",
            "https://krm.gg",
            "https://knm.st",
            "https://2kkm.co",
            "https://2kk.site",
            "https://2kramp.site",
            "https://2kk.ac",
            "https://2kkn.ac",
            "https://2kkm.st",
            "https://torkrn.cc",
            "https://torkrn.co",
            "https://2krk.in",
            "https://2krm.st",
            "https://2knmp.cc",
            "https://kkn.st",
            "https://2kkn.st",
            "https://2kkn.top",
            "https://tkm.ac",
            "https://tkm.cx",
            "https://tkm.gg",
            "https://2kkm.mx",
            "https://2kn.io",
            "https://dkm.gg",
            "https://2kk.to",
            "https://2kk.is",
            "https://2kk.ai",
            "https://2kk.cx",
            "https://2kk.mx",
            "https://2kk.sh",
            "https://2kk.so",
            "https://knmp.cc",
            "https://KNMP.IO",
            "https://KNMP.ST",
            "https://zerkalo-kra.cc",
            "https://zerkalokrn.cc",
            "https://dkm.ac"
        ]

        # Generate the frame-ancestors directive for the Content-Security-Policy header
        frame_ancestors = ' '.join(allowed_domains)

        # Set the Content-Security-Policy header
        response['Content-Security-Policy'] = f"frame-ancestors {frame_ancestors}"

        return response