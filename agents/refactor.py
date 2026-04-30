
class RefactorAgent:
    def refactor(self, code: str, review):
        lines = code.split("\n")
        for issue in review.issues:
            if "Function too long" in issue.message:
                lines.insert(issue.line, "# TODO: Refactor function")
        return "\n".join(lines)
