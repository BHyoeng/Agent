
from agents.coordinator import CoordinatorAgent

if __name__ == "__main__":
    sample_code = '''
def example():
    x = 1
    y = 2
    print(x+y)

example()
'''
    coordinator = CoordinatorAgent()
    final_code = coordinator.run(sample_code)

    print("\nFinal Code:\n")
    print(final_code)
