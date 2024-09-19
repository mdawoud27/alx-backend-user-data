#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth function"""
        if not path or not excluded_paths:
            return True

        path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if (excluded_path.endswith('*')
                    and path.startswith(excluded_path[:-1])):
                return False

            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header function"""
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user function"""
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request"""
        if not request:
            return None

        return request.cookies.get(getenv("SESSION_NAME"))
