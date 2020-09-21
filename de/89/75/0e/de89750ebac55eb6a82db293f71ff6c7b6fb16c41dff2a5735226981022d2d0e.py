import aiohttp

import asyncio
import platform
import string
import random
import sys

# settings
base_str = string.ascii_lowercase + string.digits
connector = aiohttp.TCPConnector(limit=20)
loop = asyncio.get_event_loop()

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'NordVPN Desktop for ISAB Members',
}


async def visit(url: str, session: aiohttp.ClientSession):
    try:
        async with session.get(url) as response:
            status_code = response.status
            status_text = 'Success' if status_code == 200 else 'Failure'
            sys.stdout.write(
                f'url: {url}\nstatus: HTTP {status_code} {status_text}\n')
            return status_code
    except aiohttp.ClientError:
        sys.stdout.write(f'url: {url}\nstatus: aiohttp Error\n')


async def session_manager(url_list: list):
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        request_list = [visit(url, session) for url in url_list]
        return await asyncio.wait(request_list)


def random_visit(base_name: str, rand_gen, repeat: int = 200):
    url_list = [base_name.format(rand_gen()) for _ in range(repeat)]
    return loop.run_until_complete(session_manager(url_list))


base_name = 'https://{}.isab.top/'


def rand_gen():
    return 'nord' + ''.join(random.sample(base_str, random.randint(4, 32)))


random_visit(base_name, rand_gen, 400)
