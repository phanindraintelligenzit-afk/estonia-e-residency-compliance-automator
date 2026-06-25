"""Tests for contract_parser."""
import pytest
from src.agents.contract_parser import contract_parser

def test_contract_parser_basic():
    """Test contract_parser processes input correctly."""
    input_data = {"test": True}
    result = contract_parser(input_data)
    assert isinstance(result, dict)
    assert "contract_parser_output" in result

def test_contract_parser_empty_input():
    """Test contract_parser handles empty input."""
    result = contract_parser(dict())
    assert isinstance(result, dict)
