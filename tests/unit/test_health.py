from lambdas import health
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass
import pytest

def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:us-gov-west-1:123456789012:function:test"
        aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

    return LambdaContext()

def test_get_since_time():
    interval = 15
    now = datetime.now(timezone.utc)
    ago = health.get_past_time(interval)
    assert (now.minute-ago.minute)==interval

