"""Evaluation script."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pipeline import run_pipeline
from evaluation import evaluate_response


def main():
    """Run evaluation."""
    print("Running Evaluation...")
    
    # Example test case
    input_text = "What is context engineering?"
    expected_output = "Context engineering is the practice of designing and optimizing the context provided to LLMs."
    
    # Generate response
    response = run_pipeline(input_text)
    
    # Evaluate
    metrics = evaluate_response(response, expected_output)
    
    print(f"\nInput: {input_text}")
    print(f"Generated: {response}")
    print(f"Expected: {expected_output}")
    print(f"\nMetrics: {metrics}")


if __name__ == "__main__":
    main()

