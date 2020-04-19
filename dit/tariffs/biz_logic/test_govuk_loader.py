import pytest


from .govuk_loader import GovUKLoader

@pytest.mark.django_db
def test_loader_runs_without_crashing():
    loader = GovUKLoader(heading='0708')
    loader.load_db_from_govUK_api_call()
