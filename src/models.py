"""Data models and schemas."""


class Prompt:
    """Prompt data model."""
    
    def __init__(self, input_text: str, output_text: str = None):
        self.input_text = input_text
        self.output_text = output_text


class LLMResponse:
    """LLM response data model."""
    
    def __init__(self, text: str, model: str = None):
        self.text = text
        self.model = model

