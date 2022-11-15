import pytest


@pytest.fixture
def service_test_api_key():
    yield "secret", "bearer_token"


# def hello(service_test_api_key='123456'):
#     return (f'service_test_api_key: {service_test_api_key}')

# def test_hello(service_test_api_key):
#     service_test_api_key = "123"
#     out = hello(service_test_api_key)
#     assert out == 'service_test_api_key: secret'


def test_foo(service_test_api_key):
    # print("in test")
    # pytest.fail(f"Response did not reach desired status")

    assert False
