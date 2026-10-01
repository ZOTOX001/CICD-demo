from app import get_message

def test_message():
    # The CI pipeline will run this. If it doesn't match exactly, the pipeline halts.
    assert get_message() == "Hello World! The CI/CD Pipeline is working perfectly."
    print("All tests passed!")