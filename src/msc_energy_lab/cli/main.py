import typer
from loguru import logger

from msc_energy_lab.logging_config import configure_logging
from msc_energy_lab.paths import ensure_project_dirs
from msc_energy_lab.settings import settings

app = typer.Typer(help="MSC Cruise Energy Lab CLI", no_args_is_help=False)


@app.command("demo")
def demo_command() -> None:
    configure_logging()
    ensure_project_dirs()
    logger.info("MSC Cruise Energy Lab demo bootstrap starting")
    logger.info(f"Environment: {settings.app_env}")
    logger.info(f"Postgres URL: {settings.postgres_url}")
    logger.info(f"DuckDB path: {settings.duckdb_file}")
    logger.info("Project directories are ready")
    logger.info("Next batches will generate fleet data and build the warehouse")


if __name__ == "__main__":
    app()
