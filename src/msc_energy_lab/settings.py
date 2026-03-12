from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "dev"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "msc_energy"
    postgres_user: str = "msc_user"
    postgres_password: str = "msc_pass"
    duckdb_path: str = "data/msc_energy.duckdb"
    log_level: str = "INFO"
    data_root: str = "data"
    export_root: str = "data/exports"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def postgres_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def duckdb_file(self) -> Path:
        return Path(self.duckdb_path)


settings = Settings()
