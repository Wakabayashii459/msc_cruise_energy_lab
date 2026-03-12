from msc_energy_lab.settings import settings


def test_settings_loaded():
    assert settings.app_env in {"dev", "prod", "test"}
    assert settings.postgres_port == 5432
