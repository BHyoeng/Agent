
import ast
from dataclasses import dataclass
from typing import List

@dataclass
class ReviewIssue:
    line: int
    message: str
    severity: str

@dataclass
class ReviewResult:
    issues: List[ReviewIssue]

class ReviewerAgent:
    def review(self, code: str) -> ReviewResult:
        issues = []
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            issues.append(ReviewIssue(e.lineno, str(e), "critical"))
            return ReviewResult(issues)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 10:
                    issues.append(ReviewIssue(node.lineno, "Function too long", "warning"))

        return ReviewResult(issues)
