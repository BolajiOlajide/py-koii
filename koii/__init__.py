"""Koii

Import the `Koii` class into your flask app and initialize:
    ```
    Koii(app)
    ```

See https://github.com/BolajiOlajide/koii-py/ for more information
"""
from colorama import init, Fore, Style
from tabulate import tabulate


init(autoreset=True)

__version__ = "1.0.0"
__author_name__ = "Bolaji Olajide"


class Koii(object):
    valid_verbs = ["GET", "POST", "PUT", "DELETE", "PATCH"]

    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        routes = Koii._normalize_routes(app.url_map)
        styled_routes = Koii._style_routes(routes)
        print(styled_routes)
        print(Style.RESET_ALL)

    @staticmethod
    def _normalize_routes(url_map):
        main_routes = []
        for rule in url_map._rules:
            routes = Koii._generate_routes(rule)
            main_routes.extend(routes)
        return main_routes

    @staticmethod
    def _generate_routes(route):
        return [
            [(Fore.GREEN + method), (Fore.WHITE + route.rule)]
            for method in route.methods
            if method in Koii.valid_verbs
        ]

    @staticmethod
    def _style_routes(routes):
        headers = [(Fore.CYAN + "METHOD"), (Fore.CYAN + "PATH")]
        routes = "\n" + tabulate(routes, headers=headers) + "\n"
        return routes
