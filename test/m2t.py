# -*- coding = utf-8 -*-
# @Time : 5/12/2022 10:17 PM
# @Author : yaowei
# @File : m2t.py
# @Software : PyCharm

import asyncio
from magnet2torrent import Magnet2Torrent, FailedToFetchException
magnet ="magnet:?xt=urn:btih:3CC26648164293DE290F22D7C6AC3856DD699D1A"

m2t = Magnet2Torrent(magnet)
print(m2t.torrent_cache_folder)
# asyncio.run(m2t))
