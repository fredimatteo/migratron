from dataclasses import dataclass

@dataclass
class DbConfig:
    host: str
    port: str | int
    user: str
    password: str
    database: str

    def __post_init__(self):
        if isinstance(self.port, str):
            self.port = int(self.port)