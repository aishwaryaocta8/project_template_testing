# LLM Application Project Template

A standard project template for Data & AI organization focused on context engineering and LLM applications.

## Project Structure

```
project-template/
├── .github/workflows/    # CI/CD workflows
├── config/               # Configuration files
├── data/                 # Data directories
├── notebooks/            # Jupyter notebooks
├── src/                  # Source code
├── scripts/              # Utility scripts
├── tests/                # Test files
└── docker/               # Docker configuration
```

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run demo:
```bash
python scripts/run_demo.py
```

3. Run evaluation:
```bash
python scripts/run_evaluation.py
```

4. Run tests:
```bash
python -m pytest tests/
```

### Docker

1. Build Docker image:
```bash
docker build -f docker/Dockerfile -t llm-app .
```

2. Run container:
```bash
docker run llm-app
```

The container will automatically run `scripts/run_demo.py` by default.

## Configuration

- `config/settings.yaml` - Project settings and LLM configuration
- `config/prompts.yaml` - System prompts and few-shot examples

## Development

- Source code: `src/`
- Scripts: `scripts/`
- Tests: `tests/`
- Notebooks: `notebooks/`

## License

MIT

