# Usage Guide

This document explains how to use the CLI and library in `ollama-gemma-chat`.

## 1. Environment Configuration

The package respects the following environment variables (defaults shown in parentheses):

- `GEMMA_MODEL` (`gemma:2b`): Model identifier to query.
- `GEMMA_TEMP` (`0.7`): Sampling temperature. (No usage for now)
- `GEMMA_MAX_TOKENS` (`512`): Maximum tokens in response. (No usage for now)

You can set these in a `.env` file at project root or via shell:

```bash
GEMMA_MODEL=gemma:2b
GEMMA_TEMP=0.5
GEMMA_MAX_TOKENS=256
```

## 2. CLI Usage

Once installed (poetry install) and configured, use:

```bash
# Interactive prompt flag
poetry run ollama-gemma-chat chat -p 'Hello, Gemma!'

# Without prompt flag (will ask interactively)
poetry run ollama-gemma-chat chat
```

Options:

- `-p, --prompt` (required): The prompt to send to the model.

## 3. Library Usage

Import the client and call directly:

```python
from gemma_chat import OllamaClient, load_config

# Load config or override manually
cfg = load_config()
client = OllamaClient(model=cfg['model'])
response = client.query(prompt="What is the weather today?",)
print(response)
```

## 4. Example Workflow

### 1. Clone repo and install:

```bash
git clone ...
cd poc-ollama-chat
poetry install
```

### 2.Configure .env (optional).

### 3. Run tests:

```bash
pytest
```

### 4. Chat:

```bash
poetry run ollama-gemma-chat chat -p "Tell me a story."
```
