import pytest
import time
from datetime import datetime, timedelta

@pytest.fixture()
def payload_fgts():
    return {"document_number": "04113929130"}

@pytest.fixture()
def payload_fgts_simulation():
    return {
        "borrower": {
            "person_type": "natural"
        },
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-07-01",
                    "total_amount": 11119
                },
                {
                    "due_date": "2023-07-01",
                    "total_amount": 10120
                },
                {
                    "due_date": "2024-07-01",
                    "total_amount": 9121
                },
                {
                    "due_date": "2025-07-01",
                    "total_amount": 8122
                },
                {
                    "due_date": "2026-07-01",
                    "total_amount": 7123
                },
                {
                    "due_date": "2027-07-01",
                    "total_amount": 6124
                },
                {
                    "due_date": "2028-07-01",
                    "total_amount": 5125
                },
                {
                    "due_date": "2029-07-01",
                    "total_amount": 4126
                },
                {
                    "due_date": "2030-07-01",
                    "total_amount": 3127
                },
                {
                    "due_date": "2031-07-01",
                    "total_amount": 2128
                },
                {
                    "due_date": "2032-07-01",
                    "total_amount": 1129
                }
            ],
            "interest_type": "pre_price_days",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "principal_grace_period": 0,
            "number_of_installments": 11,
            "monthly_interest_rate": 0,
            "disbursement_date": str(datetime.now().date()),
        }
    }


@pytest.fixture()
def payload_fgts_simulation_guess():
    return {
            "borrower": {
                "person_type": "natural"
            },
            "financial": {
                "desired_installments": [
                    {
                        "due_date": "2022-09-01",
                        "total_amount": 11119
                    },
                    {
                        "due_date": "2023-09-01",
                        "total_amount": 10120
                    },
                    {
                        "due_date": "2024-09-01",
                        "total_amount": 9121
                    },
                    {
                        "due_date": "2025-09-01",
                        "total_amount": 8122
                    },
                    {
                        "due_date": "2026-09-01",
                        "total_amount": 7123
                    },
                    {
                        "due_date": "2027-09-01",
                        "total_amount": 6124
                    },
                    {
                        "due_date": "2028-09-01",
                        "total_amount": 5125
                    },
                    {
                        "due_date": "2029-09-01",
                        "total_amount": 4126
                    },
                    {
                        "due_date": "2030-09-01",
                        "total_amount": 3127
                    },
                    {
                        "due_date": "2031-09-01",
                        "total_amount": 2128
                    },
                    {
                        "due_date": "2032-09-01",
                        "total_amount": 1129
                    }
                ],
                "interest_type": "pre_price_days",
                "fine_configuration": {
                    "monthly_rate": 0,
                    "interest_base": "calendar_days",
                    "contract_fine_rate": 0
                },
                "credit_operation_type": "ccb",
                "interest_grace_period": 0,
                "principal_grace_period": 0,
                "number_of_installments": 11,
                "monthly_interest_rate": 0.0001,
                "disbursement_date": str(datetime.now().date())

            },
            "target_disbursed_amount": 1000
        }

@pytest.fixture()
def payload_debt_fgts():
    return {
        "borrower": {
            "person_type": "natural",
            "name": "wilker",
            "mother_name": "maria",
            "birth_date": "2000-12-12",
            "profession": "tester",
            "nationality": "Bras",
            "marital_status": "single",
            "is_pep": False,
            "individual_document_number": "04113929130",
            "document_identification_number": "32323",
            "email": "tete@teste.com",
            "phone": {
                "country_code": "055",
                "area_code": "61",
                "number": "99605152"
            },
            "address": {
                "street": "Avenida das Castanheiras",
                "state": "RN",
                "city": "Brasília",
                "neighborhood": "tes",
                "number": "12",
                "postal_code": "71900100",
                "complement": ""
            },
            "document_identification": "8456e1e3-e0bc-4f4c-b3a8-329ca8856703",
            "proof_of_residence": "e271ef45-ee68-42d0-81f3-ea4d1396bffb",
            "wedding_certificate": None,
            "spouse": None
        },
        "collaterals": [{
            "percentage": 1,
            "collateral_data": {
                "periods": [{
                    "due_date": str(datetime.now().date() + timedelta(2)),
                    "amount": 1024.49
                }]
            },
            "collateral_type": "fgts_balance"
        }],
        "financial": {
            "desired_installments": [{
                "due_date": str(datetime.now().date() + timedelta(2)),
                "total_amount": 1024.49
            }],
            "interest_type": "pre_price_days",
            "disbursement_date": str(datetime.now().date()),
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "monthly_interest_rate": 0.01,
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "number_of_installments": 1,
            "principal_grace_period": 0
        },
        "disbursement_bank_accounts": [{
            "bank_code": "081",
            "branch_number": "1222",
            "account_number": "21212",
            "account_digit": "2",
            "document_number": "04113929130",
            "name": "wilker"
        }]
    }


@pytest.fixture()
def payload_debt_signed():
    return {
        "type": "data-signature"
    }





@pytest.fixture()
def payload_fgts_wrong_characters():
    return {"document_number": "04113929ABC"}


@pytest.fixture()
def payload_fgts_simulation_impossible_settler():
    return {
        "borrower": {"person_type": "legal"},
        "financial": {
            "desired_installments": [
                {"due_date": "2021-08-09", "total_amount": 800},
            ],
            "interest_type": "pre_price_days",
            "disbursement_date": "2032-07-09",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0,
            },
            "annual_interest_rate": 50.05,
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "number_of_installments": 2,
            "principal_grace_period": 0,
        },
    }


@pytest.fixture()
def payload_fgts_simulation_past_disbursement_date():
    return {
        "borrower": {"person_type": "legal"},
        "financial": {
            "desired_installments": [
                {"due_date": "2021-08-09", "total_amount": 800},
                {"due_date": "2022-08-09", "total_amount": 758},
            ],
            "interest_type": "pre_price",
            "disbursement_date": "2020-07-09",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0,
            },
            "annual_interest_rate": 0.05,
            "credit_operation_type": "nce",
            "interest_grace_period": 0,
            "number_of_installments": 2,
            "principal_grace_period": 0,
        },
    }



@pytest.fixture()
def payload_fgts_simulation_guess_target_disbursed_amount_max():
    return {
        "borrower": {
            "person_type": "natural"
        },
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-12-01",
                    "total_amount": 10000000
                }
            ],
            "interest_type": "pre_price_days",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "principal_grace_period": 0,
            "number_of_installments": 1,
            "monthly_interest_rate": 0.015,
            "disbursement_date": str(datetime.now().date()),

        },
        "target_disbursed_amount": 10000000
    }


@pytest.fixture()
def payload_fgts_simulation_guess_disbursement_date_past():
    return {
        "borrower": {
            "person_type": "natural"
        },
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-07-01",
                    "total_amount": 11119
                }
            ],
            "interest_type": "pre_price_days",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "principal_grace_period": 0,
            "number_of_installments": 1,
            "monthly_interest_rate": 0.015,
            "disbursement_date": "2022-05-01",
            "rebates": [
                {
                    "fee_type": "tac",
                    "amount_type": "absolute",
                    "amount": 0
                },
                {
                    "fee_type": "spread",
                    "amount_type": "percentage",
                    "amount": 0.5
                },
                {
                    "fee_type": "spread_ted_fee",
                    "amount_type": "percentage",
                    "amount": 0.345
                },
                {
                    "fee_type": "ted_fee",
                    "amount_type": "absolute",
                    "amount": 5
                }
            ]
        },
        "target_disbursed_amount": 1000
    }


@pytest.fixture()
def payload_fgts_simulation_guess_number_of_installments():
    return {
        "borrower": {
            "person_type": "natural"
        },
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-07-01",
                    "total_amount": 11119
                }
            ],
            "interest_type": "pre_price_days",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "principal_grace_period": 0,
            "number_of_installments": 2,
            "monthly_interest_rate": 0.015,
            "disbursement_date": str(datetime.now().date())
        },
        "target_disbursed_amount": 1000
    }


@pytest.fixture()
def payload_debt_fgts_not_workday_disbursement_date():
    return {
        "borrower": {
            "person_type": "natural",
            "name": "Wilker Sant",
            "mother_name": "maria",
            "birth_date": "2000-10-10",
            "profession": "QA",
            "nationality": "Brasil",
            "marital_status": "single",
            "is_pep": False,
            "individual_document_number": "04113929130",
            "document_identification_number": "23223423",
            "email": "wilker.oliveira@qitech.com.br",
            "phone": {
                "country_code": "055",
                "area_code": "61",
                "number": "99605152"
            },
            "address": {
                "street": "Avenida das Castanheiras",
                "state": "DF",
                "city": "Brasília",
                "neighborhood": "teste",
                "number": "12",
                "postal_code": "71900100",
                "complement": "teste"
            },
            "document_identification": "f93a63a6-464f-4ae7-8d30-3dc1e6691d80",
            "wedding_certificate": None,
            "spouse": None
        },
        "collaterals": [
            {
                "percentage": 1,
                "collateral_data": {
                    "periods": [
                        {
                            "due_date": "2022-07-01",
                            "amount": 108.5
                        }
                    ]
                },
                "collateral_type": "fgts_balance"
            }
        ],
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-07-01",
                    "total_amount": 108.5
                }
            ],
            "interest_type": "pre_price_days",
            "disbursement_date": "2022-05-01",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "monthly_interest_rate": 0.015,
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "number_of_installments": 1,
            "principal_grace_period": 0
        },
        "disbursement_bank_accounts": [
            {
                "bank_code": "081",
                "branch_number": "0001",
                "account_number": "12346",
                "account_digit": "5",
                "document_number": "04113929130",
                "name": "Wilker Sant"
            }
        ]
    }


@pytest.fixture()
def payload_debt_fgts_past_disbursement_date():
    return {
        "borrower": {
            "person_type": "natural",
            "name": "Wilker Sant",
            "mother_name": "maria",
            "birth_date": "2000-10-10",
            "profession": "QA",
            "nationality": "Brasil",
            "marital_status": "single",
            "is_pep": False,
            "individual_document_number": "04113929130",
            "document_identification_number": "23223423",
            "email": "wilker.oliveira@qitech.com.br",
            "phone": {
                "country_code": "055",
                "area_code": "61",
                "number": "99605152"
            },
            "address": {
                "street": "Avenida das Castanheiras",
                "state": "DF",
                "city": "Brasília",
                "neighborhood": "teste",
                "number": "12",
                "postal_code": "71900100",
                "complement": "teste"
            },
            "document_identification": "f93a63a6-464f-4ae7-8d30-3dc1e6691d80",
            "wedding_certificate": None,
            "spouse": None
        },
        "collaterals": [
            {
                "percentage": 1,
                "collateral_data": {
                    "periods": [
                        {
                            "due_date": "2022-07-01",
                            "amount": 108.5
                        }
                    ]
                },
                "collateral_type": "fgts_balance"
            }
        ],
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-07-01",
                    "total_amount": 108.5
                }
            ],
            "interest_type": "pre_price_days",
            "disbursement_date": "2022-05-01",
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "monthly_interest_rate": 0.015,
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "number_of_installments": 1,
            "principal_grace_period": 0
        },
        "disbursement_bank_accounts": [
            {
                "bank_code": "081",
                "branch_number": "0001",
                "account_number": "12346",
                "account_digit": "5",
                "document_number": "04113929130",
                "name": "Wilker Sant"
            }
        ]
    }


@pytest.fixture()
def payload_debt_fgts_installments_after_dibursement_date():
    return {
        "borrower": {
            "person_type": "natural",
            "name": "Wilker Sant",
            "mother_name": "maria",
            "birth_date": "2000-10-10",
            "profession": "QA",
            "nationality": "Brasil",
            "marital_status": "single",
            "is_pep": False,
            "individual_document_number": "04113929130",
            "document_identification_number": "23223423",
            "email": "wilker.oliveira@qitech.com.br",
            "phone": {
                "country_code": "055",
                "area_code": "61",
                "number": "99605152"
            },
            "address": {
                "street": "Avenida das Castanheiras",
                "state": "DF",
                "city": "Brasília",
                "neighborhood": "teste",
                "number": "12",
                "postal_code": "71900100",
                "complement": "teste"
            },
            "document_identification": "f93a63a6-464f-4ae7-8d30-3dc1e6691d80",
            "wedding_certificate": None,
            "spouse": None
        },
        "collaterals": [
            {
                "percentage": 1,
                "collateral_data": {
                    "periods": [
                        {
                            "due_date": "2022-07-01",
                            "amount": 108.5
                        }
                    ]
                },
                "collateral_type": "fgts_balance"
            }
        ],
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-07-01",
                    "total_amount": 108.5
                }
            ],
            "interest_type": "pre_price_days",
            "disbursement_date": str(datetime.now().date()),
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "monthly_interest_rate": 0.015,
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "number_of_installments": 1,
            "principal_grace_period": 0
        },
        "disbursement_bank_accounts": [
            {
            }
        ]
    }

@pytest.fixture()
def payload_debt_fgts_invalid_disbursement_account():
    return {
        "borrower": {
            "person_type": "natural",
            "name": "Wilker Sant",
            "mother_name": "maria",
            "birth_date": "2000-10-10",
            "profession": "QA",
            "nationality": "Brasil",
            "marital_status": "single",
            "is_pep": False,
            "individual_document_number": "04113929130",
            "document_identification_number": "23223423",
            "email": "wilker.oliveira@qitech.com.br",
            "phone": {
                "country_code": "055",
                "area_code": "61",
                "number": "99605152"
            },
            "address": {
                "street": "Avenida das Castanheiras",
                "state": "DF",
                "city": "Brasília",
                "neighborhood": "teste",
                "number": "12",
                "postal_code": "71900100",
                "complement": "teste"
            },
            "document_identification": "f93a63a6-464f-4ae7-8d30-3dc1e6691d80",
            "wedding_certificate": None,
            "spouse": None
        },
        "collaterals": [
            {
                "percentage": 1,
                "collateral_data": {
                    "periods": [
                        {
                            "due_date": "2022-12-01",
                            "amount": 108.5
                        }
                    ]
                },
                "collateral_type": "fgts_balance"
            }
        ],
        "financial": {
            "desired_installments": [
                {
                    "due_date": "2022-12-01",
                    "total_amount": 108.5
                }
            ],
            "interest_type": "pre_price_days",
            "disbursement_date": str(datetime.now().date()),
            "fine_configuration": {
                "monthly_rate": 0,
                "interest_base": "calendar_days",
                "contract_fine_rate": 0
            },
            "monthly_interest_rate": 0.015,
            "credit_operation_type": "ccb",
            "interest_grace_period": 0,
            "number_of_installments": 1,
            "principal_grace_period": 0
        },
        "disbursement_bank_accounts": [
            {
            }
        ]
    }
