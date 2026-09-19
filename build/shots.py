#!/usr/bin/env python3
"""Screenshots every prototype page at desktop (1440) and mobile (390) for QA. Output: /tmp/shots/"""
import os, sys, glob, http.server, threading, socketserver
from playwright.sync_api import sync_playwright
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'prototype')
OUT = '/tmp/shots'; os.makedirs(OUT, exist_ok=True)
PORT = 8767
socketserver.TCPServer.allow_reuse_address = True
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*a,**k): super().__init__(*a,directory=ROOT,**k)
    def log_message(self,*a): pass
srv = socketserver.TCPServer(('127.0.0.1',PORT),H); threading.Thread(target=srv.serve_forever,daemon=True).start()
pages = sys.argv[1:] or sorted(os.path.basename(p) for p in glob.glob(ROOT+'/*.html'))
with sync_playwright() as p:
    b = p.chromium.launch()
    for vw,tag in ((1440,'d'),(390,'m')):
        ctx = b.new_context(viewport={'width':vw,'height':900}, device_scale_factor=1)
        pg = ctx.new_page()
        for f in pages:
            pg.goto(f'http://127.0.0.1:{PORT}/{f}', wait_until='networkidle')
            pg.evaluate("try{sessionStorage.setItem('rsx','1')}catch(e){}")
            pg.evaluate("(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));} window.scrollTo(0,0);})()"); pg.wait_for_timeout(900)
            pg.screenshot(path=f'{OUT}/{tag}-{f[:-5]}.png', full_page=True)
            print(tag, f, pg.evaluate('document.body.scrollWidth'), pg.evaluate('document.body.scrollHeight'))
        ctx.close()
    b.close()
srv.shutdown()
