import pytest

if __name__ == "__main__":
    pytest.main([
        "-p", "no:cacheprovider",
        "-s",
        # "--environment", "dev",
        "./example.py"
    ])