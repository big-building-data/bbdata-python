from dataclasses import dataclass


@dataclass
class Info:
    server_time: str
    build_date: str
    version: float
