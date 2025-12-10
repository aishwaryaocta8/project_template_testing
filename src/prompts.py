"""Prompt management utilities."""

import yaml
from pathlib import Path


def load_prompts(config_path: str = "config/prompts.yaml") -> dict:
    """Load prompts from YAML configuration file."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_system_prompt(prompts_config: dict) -> str:
    """Extract system prompt from prompts configuration."""
    return prompts_config.get('system_prompt', '')


def get_few_shot_examples(prompts_config: dict) -> list:
    """Extract few-shot examples from prompts configuration."""
    return prompts_config.get('few_shot_examples', [])

