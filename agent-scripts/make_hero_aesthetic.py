import re

def aesthetic_english():
    with open('site/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The current H1 is: <h1>Trusted multispeciality care in Jaipur, available 24x7</h1>
    html = html.replace(
        '<h1>Trusted multispeciality care in Jaipur, available 24x7</h1>',
        '<h1>Trusted multispeciality care in Jaipur, available<br><span style="color:var(--magenta)">24x7</span></h1>'
    )
    
    with open('site/index.html', 'w', encoding='utf-8') as f:
        f.write(html)


def aesthetic_hindi():
    with open('site/hi/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The current H1 is: <h1>जयपुर में भरोसेमंद मल्टीस्पेशलिटी केयर, 24x7 उपलब्ध</h1>
    html = html.replace(
        '<h1>जयपुर में भरोसेमंद मल्टीस्पेशलिटी केयर, 24x7 उपलब्ध</h1>',
        '<h1>जयपुर में भरोसेमंद मल्टीस्पेशलिटी केयर,<br><span style="color:var(--magenta)">24x7 उपलब्ध</span></h1>'
    )
    
    with open('site/hi/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

aesthetic_english()
aesthetic_hindi()
print("Made hero aesthetic.")
