"""Main processing pipeline."""

from llm_client import LLMClient
from prompts import load_prompts, get_system_prompt


def run_pipeline(input_text: str, config_path: str = "config/prompts.yaml") -> str:
    """
    Run the main processing pipeline.
    
    Args:
        input_text: Input text to process
        config_path: Path to prompts configuration file
        
    Returns:
        Generated output
    """
    # Load prompts
    prompts_config = load_prompts(config_path)
    system_prompt = get_system_prompt(prompts_config)
    
    # Initialize LLM client
    client = LLMClient()
    
    # Construct full prompt
    full_prompt = f"{system_prompt}\n\nInput: {input_text}\nOutput:"
    
    # Generate response
    response = client.generate(full_prompt)
    
    return response

