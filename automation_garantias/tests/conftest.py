import json
import pytest


@pytest.fixture()
def administrator_header():
    return {"natural-person-roles": json.dumps({"account": "administrator"})}


@pytest.fixture()
def administrator_header_escrow():
    return {"natural-person-roles": json.dumps({"account": "administrator"})}


@pytest.fixture()
def master_header():
    return {"natural-person-roles": json.dumps({"account": "master"})}

@pytest.fixture()
def roles_master_header():
    return {"roles": json.dumps({"roles": "master"})}