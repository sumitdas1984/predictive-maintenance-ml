from pathlib import Path

from src.data.validate_data import EXPECTED_COLUMNS, LEAKAGE_COLUMNS


def test_expected_schema_is_defined():
    assert "Machine failure" in EXPECTED_COLUMNS
    assert "Torque [Nm]" in EXPECTED_COLUMNS


def test_failure_mode_columns_are_marked_as_leakage():
    assert {"TWF", "HDF", "PWF", "OSF", "RNF"} == LEAKAGE_COLUMNS


def test_project_docs_exist():
    assert Path("README.md").exists()
    assert Path("docs/business-understanding.md").exists()
