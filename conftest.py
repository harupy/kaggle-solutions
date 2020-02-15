"""
Please make sure this file is in the root.
"""

import pytest


@pytest.fixture(autouse=True)
def inject_items(doctest_namespace):
    """
    Inject items into the namespace where doctests run so that they can be used directly.
    """
    import os
    import tempfile
    import json

    doctest_namespace['os'] = os
    doctest_namespace['tempfile'] = tempfile
    doctest_namespace['json'] = json
