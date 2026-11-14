from pathlib import Path

import pytest

from rca_agent.config import Settings, get_settings


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in (
        "RCA_LOKI_URL",
        "RCA_PROMETHEUS_URL",
        "RCA_KUBE_CONTEXT",
        "RCA_KUBE_NAMESPACE",
        "RCA_CHROMA_PATH",
        "RCA_SLACK_WEBHOOK_URL",
        "RCA_LOG_LEVEL",
    ):
        monkeypatch.delenv(name, raising=False)
    get_settings.cache_clear()


def test_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.loki_url == "http://localhost:3100"
    assert settings.prometheus_url == "http://localhost:9090"
    assert settings.kube_context is None
    assert settings.kube_namespace == "default"
    assert settings.chroma_path == Path(".chroma")
    assert settings.slack_webhook_url is None
    assert settings.log_level == "INFO"


def test_environment_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RCA_LOKI_URL", "http://loki.example:3100")
    monkeypatch.setenv("RCA_KUBE_CONTEXT", "kind-rca")
    monkeypatch.setenv("RCA_CHROMA_PATH", "/tmp/chroma")

    settings = Settings(_env_file=None)

    assert settings.loki_url == "http://loki.example:3100"
    assert settings.kube_context == "kind-rca"
    assert settings.chroma_path == Path("/tmp/chroma")


def test_slack_webhook_is_not_exposed_in_repr(monkeypatch: pytest.MonkeyPatch) -> None:
    secret = "https://hooks.slack.com/services/T000/B000/abcdef"
    monkeypatch.setenv("RCA_SLACK_WEBHOOK_URL", secret)

    settings = Settings(_env_file=None)

    assert settings.slack_webhook_url is not None
    assert settings.slack_webhook_url.get_secret_value() == secret
    assert secret not in repr(settings)


def test_get_settings_is_cached() -> None:
    assert get_settings() is get_settings()
