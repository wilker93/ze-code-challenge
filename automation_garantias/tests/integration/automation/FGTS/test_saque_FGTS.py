import time
from datetime import datetime, timedelta
import json
from .env_auth import post_test, get_test, patch_test, delete_test
from .payload_saque_FGTS import payload_fgts_simulation, payload_fgts_simulation_guess, payload_debt_fgts, payload_debt_signed, payload_fgts, payload_fgts_simulation_guess_number_of_installments, payload_debt_fgts_invalid_disbursement_account, payload_debt_fgts_past_disbursement_date, payload_debt_fgts_installments_after_dibursement_date, payload_fgts_simulation_impossible_settler, payload_fgts_simulation_guess_disbursement_date_past, payload_fgts_wrong_characters, payload_fgts_simulation_guess_target_disbursed_amount_max, payload_fgts_simulation_past_disbursement_date, payload_debt_fgts_not_workday_disbursement_date

class TestFGTS:
    def test_post_available_balance(self, payload_fgts):
        endpoint = "/baas/fgts/available_balance"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts)

        if resp.status_code == 201:
            assert response["document_number"] == "04113929130"
            assert response["reference_date"] == str(datetime.now().date())
        else:
            assert False

    def test_post_fgts_simulation(self, payload_fgts_simulation):
        endpoint = "/baas/fgts_simulation"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation)
        assert resp.status_code == 201
        if resp.status_code == 201:
            assert response["data"]["disbursement_date"] == str(datetime.now().date())
            assert response["status"] == "finished"
            assert response["data"]["assignment_amount"] == 67364.0
        else:
            assert False

    def test_post_fgts_simulation_guess(self, payload_fgts_simulation_guess):
        endpoint = "/baas/fgts_simulation_guess"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation_guess)
        global disbursed_issue_amount
        disbursed_issue_amount = response["data"]["disbursed_issue_amount"]

        assert resp.status_code == 201

        if resp.status_code == 201:
            assert response["data"]["issue_date"] == str(datetime.now().date())
            assert response["status"] == "finished"

        else:
            assert False

    def test_post_debt_fgts(self, payload_debt_fgts):
        endpoint = "/baas/debt_fgts"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_fgts)
        global key
        global disbursed_issue_amount_debt
        assert resp.status_code == 201
        key = response["key"]
        disbursed_issue_amount_debt = response["data"]["disbursed_issue_amount"]
        if resp.status_code == 201:
            assert response["status"] == "waiting_signature"
            assert response["data"]["iof_charge_method"] == "financed"
            assert response["data"]["number_of_installments"] == 1
            assert response["data"]["collaterals"][0]["collateral_data"]["document_number"] == "04113929130"
            # assert f"{disbursed_issue_amount_debt}" == f"{disbursed_issue_amount}"

        else:
            assert False

    def test_post_debt_signed(self, payload_debt_signed):
        endpoint = f"/debt/{key}/signed"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_signed)

        assert resp.status_code == 201
        if resp.status_code == 201:
            assert response["key"] == f"{key}"
            assert response["status"] == "signature_received"
            assert response["webhook_type"] == "debt"
        else:
            assert False

    def test_get_debt(self):
        time.sleep(20)
        endpoint = f"/debt?key={key}"
        response, resp = get_test(endpoint=endpoint)

        assert resp.status_code == 200
        if resp.status_code == 200:
            assert response["operation_key"] == f"{key}"
            assert response["data"]["collateral_type"] == "fgts_balance"
            assert response["data"]["credit_operation_key"] == f"{key}"
            assert response["data"]["disbursement_date"] == str(datetime.now().date())
            assert response["data"]["issuer_document_number"] == "04113929130"
            assert response["data"]["disbursed_issue_amount"] == disbursed_issue_amount_debt
            assert response["status"] == "waiting_disbursement" or 'disbursing'

        else:
            assert False

class TestFGTSNegativeCase:
    def test_post_available_balance_erro(self, payload_fgts_wrong_characters):
        endpoint = "/baas/fgts/available_balance"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_wrong_characters)
        assert resp.status_code == 404
        if resp.status_code == 404:
            assert json.loads(response.get("data")).get("title") == "Invalid Document Number Format"
        else:
            assert False

    def test_post_fgts_simulation_impossible_settler(self, payload_fgts_simulation_impossible_settler):
        endpoint = "/baas/fgts_simulation"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation_impossible_settler)

        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "COP000170"
        else:
            assert False

    def test_post_fgts_simulation_past_disbursement_date(self, payload_fgts_simulation_past_disbursement_date):
        endpoint = "/baas/fgts_simulation"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation_past_disbursement_date)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "COP000090"
        else:
            assert False

    def test_post_fgts_simulation_guess_target_disbursed_amount_max(self, payload_fgts_simulation_guess_target_disbursed_amount_max):
        endpoint = "/baas/fgts_simulation_guess"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation_guess_target_disbursed_amount_max)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "LEG000071"
        else:
            assert False

    def test_post_fgts_simulation_guess_disbursement_date_past(self, payload_fgts_simulation_guess_disbursement_date_past):
        endpoint = "/baas/fgts_simulation_guess"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation_guess_disbursement_date_past)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "COP000090"
        else:
            assert False

    def test_post_fgts_simulation_guess_number_of_installments(self, payload_fgts_simulation_guess_number_of_installments):
        endpoint = "/baas/fgts_simulation_guess"
        response, resp = post_test(endpoint=endpoint, payload=payload_fgts_simulation_guess_number_of_installments)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "LEG000099"
        else:
            assert False

    def test_post_debt_fgts_past_disbursement_date(self, payload_debt_fgts_past_disbursement_date):
        endpoint = "/baas/debt_fgts"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_fgts_past_disbursement_date)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "COP000090"
        else:
            assert False

    def test_post_debt_fgts_installments_after_dibursement_date(self, payload_debt_fgts_installments_after_dibursement_date):
        endpoint = "/baas/debt_fgts"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_fgts_installments_after_dibursement_date)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "COP000203"
        else:
            assert False

    def test_post_debt_fgts_invalid_disbursement_account(self, payload_debt_fgts_invalid_disbursement_account):
        endpoint = "/baas/debt_fgts"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_fgts_invalid_disbursement_account)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "COP000157"
        else:
            assert False

    def test_post_debt_signed_already_signed_key(self, payload_debt_signed):
        endpoint = "/debt/e6070f5b-7524-418a-84ed-47c36378b613/signed"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_signed)
        assert resp.status_code == 400
        if resp.status_code == 400:
            assert json.loads(response.get("data")).get("code") == "LEG0000117"
        else:
            assert False

    def test_post_debt_signed_wrong_key(self, payload_debt_signed):
        endpoint = "/debt/de65d062-b53c-4ffa-830e-a2f3de8406/signed"
        response, resp = post_test(endpoint=endpoint, payload=payload_debt_signed)
        assert resp.status_code == 404
        if resp.status_code == 404:
            assert json.loads(response.get("data")).get("code") == "LEG000013"
        else:
            assert False

