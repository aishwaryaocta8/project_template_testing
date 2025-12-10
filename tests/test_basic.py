"""Basic smoke tests."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from llm_client import LLMClient


def test_llm_client_mock():
    """Smoke test for LLM client mock."""
    client = LLMClient()
    response = client.generate("Test prompt")
    
    assert response is not None
    assert isinstance(response, str)
    assert len(response) > 0
    assert "Mock LLM Response" in response


if __name__ == "__main__":
    test_llm_client_mock()
    print("All tests passed!")

