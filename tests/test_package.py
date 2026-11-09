import rca_agent


def test_version_is_defined() -> None:
    assert rca_agent.__version__ == "0.1.0"


def test_package_has_docstring() -> None:
    assert rca_agent.__doc__ is not None
    assert "incident" in rca_agent.__doc__.lower()
