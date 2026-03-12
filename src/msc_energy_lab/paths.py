from pathlib import Path
from .settings import settings


DATA_ROOT = Path(settings.data_root)
RAW_ROOT = DATA_ROOT / "raw"
STAGED_ROOT = DATA_ROOT / "staged"
CURATED_ROOT = DATA_ROOT / "curated"
FEATURE_ROOT = DATA_ROOT / "features"
EXPORT_ROOT = Path(settings.export_root)


def ensure_project_dirs() -> None:
    for path in [
        DATA_ROOT,
        RAW_ROOT,
        STAGED_ROOT,
        CURATED_ROOT,
        FEATURE_ROOT,
        EXPORT_ROOT,
    ]:
        path.mkdir(parents=True, exist_ok=True)
