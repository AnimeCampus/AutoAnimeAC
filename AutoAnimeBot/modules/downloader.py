import os
import shutil
import asyncio
import aiohttp
import aiofiles
from pyrogram.types import Message
from AutoAnimeBot.core.log import LOGGER
from AutoAnimeBot.modules.progress import progress_text
import time

logger = LOGGER("Downloader")

async def download_chunk(session, url, file_writer):
    async with session.get(url) as response:
        async for data in response.content.iter_chunked(1024):
            await file_writer.write(data)

async def downloader(message: Message, l, title, file_name):
    logger.info(f"Downloading {title}")
    
    try:
        shutil.rmtree("downloads")
    except:
        pass

    if not os.path.exists("downloads"):
        os.mkdir("downloads")

    file_name = f"downloads/{file_name}"

    t1 = time.time()
    dcount = 1  # Downloaded count in 10 sec

    try:
        t_out = aiohttp.ClientTimeout(
            total=7200.0, connect=7200.0, sock_read=7200.0, sock_connect=7200.0
        )
        
        connector = aiohttp.TCPConnector(limit_per_host=10)  # Adjust the limit as needed
        async with aiohttp.ClientSession(connector=connector, timeout=t_out) as session:
            response = await session.head(l)
            if response.content_length:
                total = response.content_length / 1024
            else:
                total = 1

            done = 0

            async with aiofiles.open(file_name, "wb") as f:
                tasks = []
                async with session.get(l) as response:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        done += 1
                        await f.write(chunk)

                        t2 = time.time()
                        if t2 - t1 > 10:
                            try:
                                t1 = t2
                                text = progress_text(
                                    "Downloading", title, done, total, dcount
                                )
                                await message.edit_caption(text)
                                dcount = done
                            except Exception as e:
                                logger.warning(str(e))
                        
            await asyncio.gather(*tasks)

    except Exception as e:
        logger.warning(str(e))
    
    logger.info(f"Downloaded {title}")
    return file_name

# Call the downloader function with appropriate arguments
