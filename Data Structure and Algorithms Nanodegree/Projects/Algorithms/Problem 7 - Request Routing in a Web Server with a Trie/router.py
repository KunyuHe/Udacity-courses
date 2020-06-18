from typing import Union, List

from router_trie import RouteTrie


class Router:
    def __init__(self, root_handler: str,
                 not_found_handler: str = "404 Page Not Found"):
        self.routes = RouteTrie()
        self.routes.insert("/", root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path: str, handler: str):
        paths = self.split_path(path)
        if paths:
            self.routes.insert(paths, handler)

    def lookup(self, path: str) -> str:
        paths = self.split_path(path)
        if not paths:
            return self.not_found_handler

        res = self.routes.find(paths)
        if not res:
            return self.not_found_handler
        return res

    @staticmethod
    def split_path(path: str) -> Union[List[str], None]:
        if not isinstance(path, str):
            raise TypeError("Inputs path should be a sting.")

        # Empty string
        if not path:
            return

        if path == "/":
            return ["/"]
        return path.strip("/").split("/")
