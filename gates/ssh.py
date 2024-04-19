from utilsdf.functions import random_proxy, capture
from httpx import AsyncClient


async def ssh(us, ps, s):
    async with AsyncClient(
        follow_redirects=True, verify=False,
    ) as session:

        if s == "br":
            i = "14"
            server = "Brazil 🇧🇷"
        elif s == "br2" or s == "br_2":
            i = "15"
            server = "Brazil 🇧🇷 -» 2"
        elif s == "br3" or s == "br_3":
            i = "16"
            server = "Brazil 🇧🇷 -» 3"
        elif s == "br4" or s == "br_4":
            i = "17"
            server = "Brazil 🇧🇷 -» 4"
        elif s == "fr":
            i = "25"
            server = "France 🇫🇷"
        elif s == "fr2" or s == "fr_2":
            i = "26"
            server = "France 🇫🇷 -» 2"
        elif s == "nl":
            i = "28"
            server = "Netherlands 🇳🇱"
        elif s == "us":
            i = "13"
            server = "United States 🇺🇸"
        elif s == "us2" or s == "us_2":
            i = "24"
            server = "United States 🇺🇸 -» 2"

        r = await session.get(
            "https://hackkcah.com/gerar.php",
        )
        t = r.text
        fl = capture(
            t, f'<img longdesc="{i}" src="https://hackkcah.com/images/flags/', '.png"'
        )
        li = capture(
            t,
            f'<img longdesc="{i}" src="https://hackkcah.com/images/flags/{fl}.png" width="20" height="15"> ',
            " </li>",
        )
        tk = capture(t, '"token" value="', '"')

        h2 = {
            "Host": "hackkcah.com",
            "origin": "https://hackkcah.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://hackkcah.com/gerar.php",
        }

        p2 = f"loginssh={us}&senhassh={ps}&servidor={i}&dias=2&limite=1&op=1&token={tk}&diretorio=%2Fgerar.php&jagerado=off"

        r2 = await session.post(
            "https://hackkcah.com/php/waitroom.php",
            headers=h2,
            data=p2,
        )

        t2 = r2.text

        if "DEBUG: SERVIDOR OK!" in t2:
            status = "Approved! ✅"
            msg = "Success -»"
        else:
            status = "Dead! ❌"
            msg = capture(t2, '<script type="text/javascript">alert("', '")')

        h3 = {
            "Host": "hackkcah.com",
            "origin": "https://hackkcah.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://hackkcah.com/php/waitroom.php",
        }

        p3 = f"check=1&loginssh={us}&senhassh={ps}&limite=1&servidor={i}&dias=1&op=1&token={tk}&diretorio=%2Fgerar.php"

        r3 = await session.post(
            "https://hackkcah.com/php/waitroom2.php",
            headers=h3,
            data=p3,
        )

        h4 = {
            "Host": "hackkcah.com",
            "origin": "https://hackkcah.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://hackkcah.com/php/waitroom2.php",
        }

        p4 = f"check1=1&loginssh={us}&senhassh={ps}&limite=1&servidor={i}&dias=1&op=1&token={tk}&diretorio=%2Fgerar.php"

        r4 = await session.post(
            "https://hackkcah.com/php/gerar.php",
            headers=h4,
            data=p4,
        )

        h5 = {
            "Host": "hackkcah.com",
            "origin": "https://hackkcah.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://hackkcah.com/php/gerar.php",
        }

        r5 = await session.post(
            "https://hackkcah.com/php/gerou.php",
            headers=h5,
            data=p2,
        )

        h6 = {
            "Host": "hackkcah.com",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "referer": "https://hackkcah.com/php/gerou.php",
        }

        r6 = await session.get(
            "https://hackkcah.com/?u=1",
            headers=h6,
        )
        t6 = r6.text
        host = capture(t6, '"txt1">IP: </span>\n<b>', "</b>")
        exp = capture(t6, '"Validade">', "</b>")
        limit = capture(t6, '"txt1">Limit concurrent users: </span>\n<b>', "</b>")
        se = capture(t6, f'<div id="s{i}">', "</div>")
        ssh = capture(
            se, 'SSH: <button title="Copiar" class="copiar" data-clipboard-text="', '"'
        )
        ssl = capture(
            se, 'SSL: <button title="Copiar" class="copiar" data-clipboard-text="', '"'
        )
        websocket = capture(
            se,
            'WebSocket: <button title="Copiar" class="copiar" data-clipboard-text="',
            '"',
        )
        direct = capture(
            se,
            'Direct: <button title="Copiar" class="copiar" data-clipboard-text="',
            '"',
        )
        key_dns = capture(
            se,
            'Key DNS: <button title="Copiar" class="copiar" data-clipboard-text="',
            '"',
        )
        ns_dns = capture(
            se,
            'NS DNS: <button title="Copiar" class="copiar" data-clipboard-text="',
            '"',
        )

        if host == "bra.hackkcah.net":
            ip = "109.104.155.254"
        elif host == "bra2.hackkcah.net":
            ip = "200.98.80.176"
        elif host == "bra3.hackkcah.net":
            ip = "200.98.82.111"
        elif host == "bra4.hackkcah.net":
            ip = "109.104.155.41"
        elif host == "fra.hackkcah.net":
            ip = "195.154.250.209"
        elif host == "fra2..hackkcah.net":
            ip = "62.210.125.206"
        elif host == "nld.hackkcah.net":
            ip = "51.158.152.143"
        elif host == "usa.hackkcah.net":
            ip = "64.31.38.131"
        elif host == "usa2.hackkcah.net":
            ip = "64.31.55.61"

        return (
            status,
            msg,
            ip,
            host,
            us,
            ps,
            exp,
            limit,
            server,
            ssh,
            ssl,
            websocket,
            direct,
            key_dns,
            ns_dns,
        )
