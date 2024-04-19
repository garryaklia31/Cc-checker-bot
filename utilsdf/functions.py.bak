import re, datetime, sqlite3, random, string, asyncio, json, asyncio, re, asyncio, os, traceback
import io
from multicolorcaptcha import CaptchaGenerator
from pyromod.exceptions import ListenerTimeout
from huepy import red
from datetime import date
from utilsdf.generator import Generator
from httpx import AsyncClient
from time import time
from pyromod import Client, Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Languages = {
    "ENGLISH": "en",
    "SPANISH": "es",
    "PORTUGES": "pt",
    "SIMPLIFIED_CHINESE": "zh-CN",
    "RUSSIAN": "ru",
    "GERMAN": "de",
    "JAPANESE": "ja",
}

times = {}
users_info = {}
buy_button = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Buy Now", url="https://t.me/qqdhq")]]
)
db_bins = sqlite3.connect("assets/bins.db")
cursor_bins = db_bins.cursor()


def generate_captcha() -> tuple:
    CAPCTHA_SIZE_NUM = 3

    generator = CaptchaGenerator(CAPCTHA_SIZE_NUM)

    captcha = generator.gen_captcha_image(difficult_level=3)

    image = captcha.image
    characters = captcha.characters

    with io.BytesIO() as buffer:
        image.save(buffer, format="PNG")
        image = io.BytesIO(buffer.getvalue())
    return image, characters


async def anti_bots_telegram(m: Message, client: Client):
    user_id = m.from_user.id
    if not user_id in users_info:
        users_info[user_id] = {"checks": 1}
        return True
    if not users_info[user_id]["checks"] == 2:
        users_info[user_id]["checks"] += 1
        return True

    chat_id = m.chat.id
    image, captcha_text = generate_captcha()
    captcha_message = await m.reply_photo(image)

    try:
        response = await client.ask(
            chat_id=chat_id,
            text="<b>Enter the captcha text:</b>",
            timeout=15,
            user_id=user_id,
        )
    except ListenerTimeout:
        await m.reply("<b>Time is up. Please try again.</b>", quote=True)
        return False
    finally:
        await captcha_message.delete()
    captcha_by_user = response.text
    if captcha_by_user.strip().lower() == captcha_text.lower():
        del users_info[user_id]
        return True
    await m.reply("<b>Incorrect</b>", quote=True)

    return False


async def two_captcha(api_key, url, site_key, en):
    async with AsyncClient(follow_redirects=True, verify=False) as session:
        if en:
            url = f"https://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl={url}&enterprise=1"
        else:
            url = f"https://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl={url}"

        r = await session.get(url)
        t = r.text
        task_id = t.split("|")[1]

        await asyncio.sleep(30)

        attempts = 0

        while True:
            r2 = await session.get(
                f"https://2captcha.com/res.php?key={api_key}&action=get&id={task_id}"
            )
            t2 = r2.text
            st = t2.split("|")[0]

            if st == "OK":
                captcha = t2.split("|")[1]
                return captcha
            else:
                attempts += 1
                if attempts >= 50:
                    raise RuntimeError("error bypass...")

                await asyncio.sleep(5)


async def solve_captcha(api_key, url, captcha_key):
    async with AsyncClient(follow_redirects=True, verify=False) as session:
        h = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        task_payload = {
            "clientKey": api_key,
            "task": {
                "type": "RecaptchaV2EnterpriseTaskProxyless",
                "websiteURL": url,
                "websiteKey": captcha_key,
            },
        }

        create_task_response = await session.post(
            "https://api.anti-captcha.com/createTask", headers=h, json=task_payload
        )
        create_task_data = create_task_response.json
        task_id = create_task_data["taskId"]

        attempts = 0

        while True:
            task_result_payload = {"clientKey": api_key, "taskId": task_id}

            get_task_result_response = await session.get(
                "https://api.anti-captcha.com/getTaskResult",
                headers=h,
                json=task_result_payload,
            )
            task_result_data = get_task_result_response.json

            if "status" in task_result_data and task_result_data["status"] == "ready":
                return task_result_data["solution"]["gRecaptchaResponse"]
            else:
                attempts += 1
                if attempts >= 20:
                    return "xD"
                    # raise Exception("Número máximo de intentos alcanzado")

                await asyncio.sleep(5)


def random_street():
    return f"{random.randint(1, 999)} W {random.randint(10, 999)}nd St"


def random_phone():
    return f'+1{"%010d" % random.randint(0, 9999999999)}'


def random_word(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )


def clean_text(text):
    text_cleaned = " ".join(re.sub(r"<.*?>|\n", " ", text).split())
    return text_cleaned


def antispam(user: int, limit: int, free_user=False, times: dict = times) -> bool | int:
    assert isinstance(user, int) and isinstance(
        limit, int
    ), "Both arguments must be integers"

    now = time()

    user_info = times.get(user, {"last": 0, "checks": 0})

    last = user_info["last"]
    checks = user_info["checks"]

    diff = now - last

    if diff >= limit:
        checks = 0

    if free_user and checks >= 1:
        return int(limit - diff)

    if not free_user and checks >= 2:
        return int(limit - diff)

    checks += 1

    times[user] = {"last": now, "checks": checks}

    return False


def bot_on() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(
        red(
            """
 /$$$$$$$   /$$$$$$  /$$$$$$$$        /$$$$$$  /$$   /$$
| $$__  $$ /$$__  $$|__  $$__/       /$$__  $$| $$$ | $$
| $$  \ $$| $$  \ $$   | $$         | $$  \ $$| $$$$| $$
| $$$$$$$ | $$  | $$   | $$         | $$  | $$| $$ $$ $$
| $$__  $$| $$  | $$   | $$         | $$  | $$| $$  $$$$
| $$  \ $$| $$  | $$   | $$         | $$  | $$| $$\  $$$
| $$$$$$$/|  $$$$$$/   | $$         |  $$$$$$/| $$ \  $$
|_______/  \______/    |__/          \______/ |__/  \__/
                                                           
"""
        )
    )


def symbol(symbol: str) -> str:
    href = f"<a href='https://t.me/bosascsdctcascsscsacacsvbotbot?start=start'>{symbol}</a>"
    return href


# refactorizar
def get_bin_info_of_database(bin: str) -> dict | None:
    bin = bin[0:6]

    result = cursor_bins.execute("SELECT * FROM bins WHERE bin=?", (bin,))
    result = result.fetchone()
    if result is None:
        return None
    banned_bins = json.load(open("assets/banned_bins.json", "r"))
    banned = False
    if str(bin) in banned_bins:
        banned = True
    return {
        "bin": result[0],
        "brand": result[1],
        "country_name": result[5],
        "country_flag": result[6].strip(),
        "bank": result[4],
        "level": result[3],
        "type": result[2],
        "banned": banned,
    }


# refactorizar
async def get_bin_info(bin: str) -> dict | None:
    bin = bin[0:6]
    async with AsyncClient(follow_redirects=True, verify=False) as s:
        response = await s.get(
            f"https://bincheck.io/details/{bin}",
        )
        if response.status_code != 200:
            return get_bin_info_of_database(bin)
        response = response.text
        banned_bins = json.load(open("assets/banned_bins.json", "r"))

        banned = False
        if str(bin) in banned_bins or "BRAZIL" in response["country_name"]:
            banned = True
        response["banned"] = banned
        return response


async def get_extras(bin: str) -> dict | None:
    bin = bin[0:6]
    async with AsyncClient(follow_redirects=True, verify=False) as client:
        response = await client.get(
            "https://akatsukichk.com/api/extra/index.php", params={"bin": bin}
        )
        response_json = response.json()
        if response.status_code != 200 or response_json["success"] != True:
            return None
        ccs = response_json["result"].split("\n")
        return [cc.strip() for cc in ccs]


# mover a generator
def get_cc(text: str) -> bool | list:
    assert isinstance(text, str), "Parameter text must be an instance of str"
    text = text.strip()
    finds = re.findall(r"\d+", text)
    current_year = datetime.datetime.now().year
    short_year = int(str(current_year)[:2])
    invalid_cc = lambda cc: (
        (cc[0] == "3" and len(cc) != 15) or (cc[0] != "3" and len(cc) != 16)
    ) or not Generator.is_luhn_valid(cc)
    if len(finds) == 4:
        cc = finds[0]
        mes = finds[1]
        ano = finds[2]
        cvv = finds[3]
    elif len(finds) > 4:
        cc, mes, ano, cvv = ("", "", "", "")
        for num in finds:
            if cc and mes and ano and cvv:
                break
            if cc == "" and not invalid_cc(num):
                cc = num
            elif mes == "" and int(num) in range(1, 13):
                mes = num
            elif ano == "" and (
                len(num) == 4
                and int(num) in range(current_year, current_year + 30)
                or len(num) == 2
                and int(num) in range(short_year, short_year + 20)
            ):
                ano = num
            elif num in Generator.generate_cvv("000", "9999"):
                cvv = num
    else:
        return False

    if len(ano) == 2:
        ano = "20" + ano

    if cc[0] not in ["3", "4", "5", "6"]:
        return False
    elif invalid_cc(cc):
        return False
    elif (
        len(ano) == 4
        and ano == str(current_year)
        and int(mes) not in range(date.today().month, 13)
    ) or (
        len(ano) == 2
        and ano == str(current_year)[2:]
        and int(mes) not in range(date.today().month, 13)
    ):
        return False
    elif len(ano) != 4 or (
        len(ano) == 4 and int(ano) not in range(current_year, current_year + 31)
    ):
        return False
    elif (cc[0] == "3" and len(cvv) != 4) or (cc[0] != "3" and len(cvv) != 3):
        return False
    else:
        return cc, mes, ano, cvv


# refactorizar
async def get_rand_info(country: str) -> dict | bool:
    countrys = json.load(open("assets/countrys.json", "r"))
    if not country in countrys:
        return False
    async with AsyncClient(follow_redirects=True, verify=False) as s:
        response = await s.get(
            "https://sachio.itbbarquisimeto.com/aa/rnd/rnd2.php",
            params={"domain": country},
        )
        response = response.json()
        return response


# mover a comando /sk
async def get_info_sk(key) -> dict | None:
    url = "https://api.stripe.com/v1/balance"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "authorization": f"Basic {key}",
    }

    async with AsyncClient(follow_redirects=True, verify=False) as client:
        response = await client.get(url, headers=headers)
        token_data = response.json()
        return token_data


def get_text_from_pyrogram(m: Message, no_command: bool = False) -> str:
    "Returns the text used in the command if no message is being responded to"
    text = m.text
    if hasattr(m.reply_to_message, "text") and m.reply_to_message.text:
        text = m.reply_to_message.text
    if no_command:
        text = text[len(m.command[0]) + 2 :].strip()
    return text


def get_message_from_pyrogram(m: Message) -> Message:
    "Return the message if no message is being responded to"
    message = m
    if (
        m.reply_to_message
        and (hasattr(m.reply_to_message, "text") and m.reply_to_message.text)
        or (hasattr(m.reply_to_message, "media") and m.reply_to_message.media)
    ):
        message = m.reply_to_message
    return message


def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"


# refactorizar
def random_proxy() -> dict:
    with open("assets/proxies.txt") as a:
        prox1 = f"{random.choice(a.read().splitlines()).strip()}:http"

    proxy_parts = prox1.split(":")
    proxy = f"{proxy_parts[-1]}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"

    return {"http://": proxy, "https://": proxy}


def random_proxy_sh() -> dict:
    with open("assets/proxies_sh.txt") as a:
        prox1 = f"{random.choice(a.read().splitlines()).strip()}:http"

    proxy_parts = prox1.split(":")
    proxy = f"{proxy_parts[-1]}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"

    return {"http://": proxy, "https://": proxy}


async def user_not_premium(m: Message) -> Message:
    return await m.reply(
        "𝑶𝒉! 𝒀𝒐𝒖 𝒂𝒓𝒆 𝒏𝒐𝒕 𝑷𝒓𝒆𝒎𝒊𝒖𝒎?\n𝑨𝒓𝒆 𝒚𝒐𝒖 𝒑𝒐𝒐𝒓? 𝑷𝒂𝒚!",
        quote=True,
        reply_markup=buy_button,
    )


async def adyen_encrypt(v, cc, month, year, cvv, key):
    async with AsyncClient(follow_redirects=True, verify=False) as session:
        p = {
            "card": f"{cc}|{month}|{year}|{cvv}",
            "adyen_key": key,
            "adyen_version": v.upper(),
        }

        r = await session.post(
            "https://boss.alwaysdata.net/api/adyen-encrypt/index.php", data=p
        )
        t = r.text
        cc_ = capture(t, '"encryptedCardNumber":"', '"')
        month_ = capture(t, '"encryptedExpiryMonth":"', '"')
        year_ = capture(t, '"encryptedExpiryYear":"', '"')
        cvv_ = capture(t, '"encryptedSecurityCode":"', '"')
        return cc_, month_, year_, cvv_


def get_gate_by_cmd(cmd_to_find: str, gates_data) -> dict | None:
    for gate in gates_data:
        if gate["cmd"] == cmd_to_find:
            return gate
    return None


async def handler_gate(gate, shopify: bool, *args) -> str | bool | Exception:
    try:
        if shopify:
            response = await gate(*args)
        else:
            response = await gate(*args)
        if not response:
            return False
        return response
    except Exception as e:
        return e


async def translate(text: str, translate_to: str = Languages["SPANISH"]) -> str:
    """
    Translate the input text to the specified language using Google Translate API.

    Args:
        text (str): The text to be translated.
        translate_to (Languages, optional): The target language for translation.
            Defaults to Languages.SPANISH.

    Returns:
        str: The translated text in the target language.

    Raises:
        ValueError: If the input text has a length less than or equal to 2.
    """
    if len(text) <= 2:
        raise ValueError("Input text must be longer than 2 characters.")
    params = {
        "client": "dict-chrome-ex",
        "sl": "auto",
        "tl": translate_to,
        "q": str(text),
        "tbb": "1",
        "ie": "UTF-8",
        "oe": "UTF-8",
    }

    async with AsyncClient(verify=False, follow_redirects=True, timeout=40) as session:
        response = await session.get(
            url="https://translate.google.com/translate_a/t?",
            params=params,
        )
        response = response.json()
        return response[0][0]
