"""Evaluation utilities."""


def evaluate_response(response: str, expected: str) -> dict:
    """
    Evaluate LLM response against expected output.
    
    Args:
        response: Generated response
        expected: Expected response
        
    Returns:
        Evaluation metrics dictionary
    """
    return {
        "exact_match": response.strip() == expected.strip(),
        "response_length": len(response),
        "expected_length": len(expected)
    }

