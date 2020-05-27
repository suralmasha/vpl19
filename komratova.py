def page():
    import re
    with open('антракт.html', 'r', encoding='utf-8') as f:
        new= open('new.txt', 'w')
        text = f.read()
        full = re.findall(r'[А-Яа-я]+[,]?\s+\w+\s*', text)
        s = ' '.join(full)
        new.write(s)
page()
