with open('input.txt','r') as f:
    urls=f.read().splitlines()
    print(urls)

with open('output.txt','a') as f:
    x='QWERTYUIOPASDFGHJJKKLZXCVBNMqwertyuiopasdfghjklzxcvbnm.-/'
    for url in urls:
        if not url.startswith('https://'):
            f.write(f'{url}-Invalid\n')
        else:
            url=url[8:]
            if all(c in x for c in url):
                f.write(f'https://{url}-valid\n')
         