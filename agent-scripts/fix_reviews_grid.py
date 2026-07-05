import re

def fix_reviews(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the Reviews block
    pattern = re.compile(r'(<!-- REVIEWS -->\s*<section id="reviews"><div class="wrap">\s*<div class="sec-head">.*?</div>)\s*<div style="max-width:800px; margin: 32px auto 0;">', re.DOTALL)
    
    html = pattern.sub(r'\1\n  <div class="grid-3" style="margin-top:32px;">', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_reviews('site/index.html')
# The Hindi page doesn't have a <!-- REVIEWS --> block normally, but let's just make sure.
import os
if os.path.exists('site/hi/index.html'):
    fix_reviews('site/hi/index.html')

print("Fixed reviews grid.")
