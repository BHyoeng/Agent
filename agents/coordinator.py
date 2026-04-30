
from .reviewer import ReviewerAgent
from .refactor import RefactorAgent
from .tester import TesterAgent

class CoordinatorAgent:
    def __init__(self):
        self.reviewer = ReviewerAgent()
        self.refactorer = RefactorAgent()
        self.tester = TesterAgent()

    def run(self, code: str, max_iter=2):
        current = code
        for _ in range(max_iter):
            review = self.reviewer.review(current)
            if not review.issues:
                break
            current = self.refactorer.refactor(current, review)
            if not self.tester.run_tests(current):
                break
        return current
