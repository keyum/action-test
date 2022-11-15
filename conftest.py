import pytest


def pytest_runtest_logreport(report):
    if report.longrepr is None:
        return
    for tb_repr, *_ in report.longrepr.chain:
        for entry in tb_repr.reprentries:
            if entry.reprfuncargs is not None:
                args = entry.reprfuncargs.args
                print(f"args->{args}")
                for idx, (name, value) in enumerate(args):
                    print("name:{}---value:{}".format(name, value))
                    if "service_test_api_key" in name:
                        args[idx] = (name, "********")
            if entry.reprlocals is not None:
                lines = entry.reprlocals.lines
                for idx, line in enumerate(lines):
                    if line.startswith("service_test_api_key"):
                        lines[idx] = "service_test_api_key          = '*********'"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()
    report.session = item.session
