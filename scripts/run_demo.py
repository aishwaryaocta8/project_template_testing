"""Demo script to run the pipeline."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pipeline import run_pipeline


def main():
    """Run demo pipeline."""
    print("Running LLM Application Demo...")
    
    # Example input
    input_text = "What is context engineering?"
    
    # Run pipeline
    result = run_pipeline(input_text)
    
    print(f"\nInput: {input_text}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()

