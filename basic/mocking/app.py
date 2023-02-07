"""
    This module represents my training with mocking objects
    https://realpython.com/python-mock-library

    Interesting library for mocking time https://github.com/spulec/freezegun
"""

from datetime import datetime
from unittest.mock import Mock, patch, create_autospec

import requests
from requests import Timeout


def is_weekend():
    today = datetime.now()
    return 4 < today.weekday() < 7


def get_holidays():
    print("ID", id(requests.get))
    resp = requests.get("http://www.google.com")
    if resp.status_code == 200:
        return resp.json()
    return None


if __name__ == "__main__":
    mock = Mock()
    print(mock.some_atrr)
    print(mock.do_something("arg1"))
    print(mock)

    json: Mock = Mock()
    json_loads = json.loads
    json_loads('{"key": "value"}')

    json.dump("filename")
    json_loads.assert_called()
    json_loads.assert_called_once()
    json_loads.assert_called_with('{"key": "value"}')
    json_loads.assert_called_once_with('{"key": "value"}')

    json_loads("{'key1': 'value1'}")

    try:
        json_loads.assert_called_once()
    except AssertionError as err:
        print(f"Error: {err}")

    print("Method calls of an object itself =>", json.method_calls)
    print("Call args list of LOADS method =>", json.loads.call_args_list)
    print("Call args of LOADS method =>", json.loads.call_args)
    print("=" * 70)
    print("Manage Mock's return value")
    tuesday = datetime(year=2023, month=2, day=7)
    saturday = datetime(year=2023, month=2, day=11)

    datetime = Mock()
    print("Mock .now() to return Tuesday")
    datetime.now.return_value = tuesday
    assert not is_weekend()
    print("Mock .now() to return Saturday")
    datetime.now.return_value = saturday
    assert is_weekend()

    print("=" * 70)
    print("Mock's side effects")

    requests = Mock()
    req_get: Mock = requests.get

    resp_mock = Mock()
    resp_mock.status_code = 200
    resp_mock.json.return_value = "{'key': 'value'}"

    req_get.side_effect = [Timeout, resp_mock]

    try:
        get_holidays()
    except Timeout as err:
        print(f"Expected timeout error {err}")
    assert get_holidays() == "{'key': 'value'}"
    assert requests.get.call_count == 2

    print("=" * 70)
    print("Configuring Your Mock")

    mock = Mock(side_effect=AttributeError)
    try:
        mock()
    except AttributeError as err:
        print(f"Expected {err}")

    mock = Mock(name="Real Python Mock")
    print(mock)
    mock = Mock(return_value=False)
    print(mock.return_value)
    assert not mock()
    mock = Mock()
    mock.configure_mock(name="Dmitro")
    mock.configure_mock(return_value=True)
    print(mock.name)
    print(mock())
    assert mock.name == "Dmitro"
    assert mock()

    # Verbose, old Mock
    response_mock = Mock()
    response_mock.json.return_value = {
        "12/25": "Christmas",
        "7/4": "Independence Day",
    }

    # Shiny, new .configure_mock()
    holidays = {"12/25": "Christmas", "7/4": "Independence Day"}
    response_mock = Mock(**{"json.return_value": holidays, "price": 100})
    print(response_mock.json())
    print(response_mock.price)

    print("=" * 70)
    print("Method patch()")
    #     with patch("__main__.requests.get") as mock_req_get:
    with patch.object(requests, "get") as mock_req_get:
        resp_moc = Mock()
        resp_moc.status_code = 200
        resp_moc.json.return_value = {"key2": "value2"}
        mock_req_get.side_effect = [Timeout, resp_moc]
        try:
            get_holidays()
        except Timeout:
            print("Expected timeout")
        print(get_holidays())
        assert mock_req_get.call_count == 2

    print("=" * 70)
    print("Avoiding Common Problems Using Specifications")
    calendar = Mock(spec=["is_weekday", "get_holidays"])
    print(calendar.is_weekday())
    try:
        calendar.get_some_method()
    except AttributeError as err:
        print(f"Expected attr error {err}")

    calendar = create_autospec(object)
