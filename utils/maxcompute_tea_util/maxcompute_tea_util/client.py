import base64
import hmac
import json
import time
from datetime import datetime
from hashlib import sha1
from typing import Any, Dict
from typing import Optional

from Tea.model import TeaModel

_process_start_time = int(time.time() * 1000)
_seqId = 0


class Client:
    """
    This is a utility module
    """

    class __ModelEncoder(json.JSONEncoder):
        def default(self, o: Any) -> Any:
            if isinstance(o, TeaModel):
                return o.to_map()
            elif isinstance(o, bytes):
                return o.decode('utf-8')
            super().default(o)

    CONTENT_MD5 = "Content-MD5"
    CONTENT_TYPE = "Content-Type"
    DATE = "Date"
    PREFIX = "x-odps-"

    @staticmethod
    def get_api_timestamp() -> str:
        return datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    @staticmethod
    def build_canonical_string(
            method: str,
            resource: str,
            params: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None
    ) -> str:
        headers = headers or {}
        params = params or {}
        builder = []
        builder.append(f"{method.upper()}\n")

        headers_to_sign = {}
        for key, value in headers.items():
            if not key:
                continue
            lower_key = key.lower()
            if (lower_key in (Client.CONTENT_MD5.lower(), Client.CONTENT_TYPE.lower(), Client.DATE.lower()) or
                    lower_key.startswith(Client.PREFIX)):
                headers_to_sign[lower_key] = value

        # Ensure mandatory headers exist
        for header in (Client.CONTENT_TYPE, Client.CONTENT_MD5):
            if header.lower() not in headers_to_sign:
                headers_to_sign[header.lower()] = ""

        # Add x-odps- params from query parameters
        for key, value in params.items():
            if key.startswith(Client.PREFIX):
                headers_to_sign[key] = value

        # Sort and append headers
        for key in sorted(headers_to_sign.keys()):
            value = headers_to_sign[key]
            if key.startswith(Client.PREFIX):
                builder.append(f"{key}:{value}\n")
            else:
                builder.append(f"{value}\n")

        # Append canonical resource
        builder.append(Client.build_canonical_resource(resource, params))
        return "".join(builder)

    @staticmethod
    def build_canonical_resource(
            resource: str,
            params: Optional[Dict[str, str]] = None
    ) -> str:
        params = params or {}
        if not params:
            return resource

        sorted_params = sorted(params.items(), key=lambda x: x[0])
        query = []
        separator = "?"
        for key, value in sorted_params:
            query.append(separator)
            query.append(key)
            if value:
                query.append(f"={value}")
            separator = "&"

        return resource + "".join(query)

    @staticmethod
    def get_signature(
            str_to_sign: str,
            access_key_id: str,
            access_key_secret: str
    ) -> str:
        key = access_key_secret.encode('utf-8')
        data = str_to_sign.encode('utf-8')
        signature = hmac.new(key, data, sha1).digest()
        encoded_signature = base64.b64encode(signature).decode('utf-8').strip()
        return f"ODPS {access_key_id}:{encoded_signature}"

    @staticmethod
    def to_string(val: Any) -> str:
        return str(val) if val is not None else 'null'
