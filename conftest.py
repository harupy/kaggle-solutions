"""
Put this file in the root to make pytest append the root to PYTHONPATH when running the tests.
"""

import pytest


@pytest.fixture(autouse=True)
def inject_items(doctest_namespace):
    import os
    import tempfile
    import json

    doctest_namespace['os'] = os
    doctest_namespace['tempfile'] = tempfile
    doctest_namespace['json'] = json
