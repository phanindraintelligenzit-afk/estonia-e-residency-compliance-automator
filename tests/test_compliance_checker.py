"""Tests for compliance_checker."""
import pytest
from src.agents.compliance_checker import compliance_checker

def test_compliance_checker_basic():
    """Test compliance_checker processes input correctly."""
    input_data = {"test": True}
    result = compliance_checker(input_data)
    assert isinstance(result, dict)
    assert "compliance_checker_output" in result

def test_compliance_checker_empty_input():
    """Test compliance_checker handles empty input."""
    result = {aname}(dict())
    assert isinstance(result, dict)
