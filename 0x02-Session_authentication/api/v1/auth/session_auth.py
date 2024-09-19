#!/usr/bin/env python3
"""SessionAuth Module"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """SessionAuth Class"""
    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session id for a user"""
        if not user_id or type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
