
import subprocess
import tempfile

class TesterAgent:
    def run_tests(self, code: str) -> bool:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
            tmp.write(code)
            path = tmp.name

        result = subprocess.run(["python", path], capture_output=True, text=True)
        return result.returncode == 0
