import subprocess


class OllamaClient:
    def __init__(self, model: str):
        self.model = model

    def query(self, prompt: str) -> str:
        try:
            # Construct command with args (still using flags as context, but they might be ignored in some versions)
            command = [
                "ollama",
                "run",
                self.model,
            ]
            # Run process and pass prompt via stdin
            result = subprocess.run(
                command,
                input=prompt.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return result.stdout.decode("utf-8").strip()
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode("utf-8") if e.stderr else str(e)
            raise RuntimeError(f"Ollama failed: {error_msg}")
