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
        routes = self._normalize_routes(app.url_map)
        self._print_routes(routes)

    def _normalize_routes(self, url_map):
        main_routes = []
        for rule in url_map._rules:
            routes = self._generate_routes(rule)
            main_routes.extend(routes)
        return main_routes

    def _generate_routes(self, route):
        return [
            [(Fore.GREEN + method), (Fore.WHITE + route.rule)]
            for method in route.methods
            if method in self.valid_verbs
        ]

    def _print_routes(self, routes):
        headers = [(Fore.CYAN + "METHOD"), (Fore.CYAN + "PATH")]
        routes = "\n" + tabulate(routes, headers=headers) + "\n"
        print(routes)
        print(Style.RESET_ALL)
