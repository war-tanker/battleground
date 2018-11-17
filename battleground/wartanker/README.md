# WARTANKER

서울여자대학교 정보보호영재교육원 중등심화 집중교육 3일차 프로젝트 : 엄서훈, 여준호

```python
>>> from wartanker import *
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

<!-- wartanker.crypto -->
## `wartanker.crypto`
```python
>>> from wartanker import crypto
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.crypto.b16encode`
```python
>>> crypto.b16encode('flag{wartanker}')
'666C61677B77617274616E6B65727D'
>>> crypto.b16encode('flag{wartanker}', 'UTF-8')
'666C61677B77617274616E6B65727D'
>>> crypto.b16encode('flag{wartanker}', encoding='UTF-8')
'666C61677B77617274616E6B65727D'
```

`wartanker.crypto.b16encode`는 문자열을 `base16`으로 인코딩한 값을 `str` 형으로 반환합니다. 이것은 Python의 `base64` 모듈을 확장한 것으로, `str`형의 데이터를 인코딩할 때 `bytes`로 변환한 후 `decode()` 메소드를 호출하는 귀찮은 과정을 알아서 처리해 줍니다.

두 번째 인수이자 선택적 인수 `encoding`으로 문자열을 `bytes` 형으로 변환할 때 사용할 인코딩을 지정할 수 있습니다.

### `wartanker.crypto.b16decode`

```python
>>> crypto.b16decode('666C61677B77617274616E6B65727D')
'flag{wartanker}'
```

`wartanker.crypto.b16decode`는 `base16`으로 인코딩된 문자열을 디코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b32encode`
```python
>>> crypto.b32encode('flag{wartanker}')
'MZWGCZ33O5QXE5DBNZVWK4T5'
>>> crypto.b32encode('flag{wartanker}', 'UTF-8')
'MZWGCZ33O5QXE5DBNZVWK4T5'
```

`wartanker.crypto.b32encode`는 문자열을 `base32`으로 인코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b32decode`

```python
>>> crypto.b32decode('MZWGCZ33O5QXE5DBNZVWK4T5')
'flag{wartanker}'
```

`wartanker.crypto.b32decode`는 `base32`으로 인코딩된 문자열을 디코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b64encode`

```python
>>> crypto.b64encode('flag{wartanker}')
'ZmxhZ3t3YXJ0YW5rZXJ9'
>>> crypto.b64encode('flag{wartanker}', 'UTF-8')
'ZmxhZ3t3YXJ0YW5rZXJ9'
```

`wartanker.crypto.b64encode`는 문자열을 `base64`으로 인코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.b64decode`

```python
>>> crypto.b64decode('ZmxhZ3t3YXJ0YW5rZXJ9')
'flag{wartanker}'
```

`wartanker.crypto.b64decode`는 `base64`으로 인코딩된 문자열을 디코딩한 값을 `str` 형으로 반환합니다.

### `wartanker.crypto.base_encode`

```python
>>> crypto.base_encode(16, 'flag{wartanker}')
'666C61677B77617274616E6B65727D'
>>> crypto.base_encode(32, 'flag{wartanker}')
'MZWGCZ33O5QXE5DBNZVWK4T5'
>>> crypto.base_encode(64, 'flag{wartanker}')
'ZmxhZ3t3YXJ0YW5rZXJ9'
>>> crypto.base_encode(64, 'flag{wartanker}', encoding='UTF-8')
'ZmxhZ3t3YXJ0YW5rZXJ9'
```

`wartanker.crypto.base_encode`는 `base`에 따라 문자열을 인코딩합니다. 역시 두 번째 선택적 인수 `encoding`을 통하여 인코딩을 지정할 수 있습니다.

### `wartanker.crypto.base_decode`

```python
>>> crypto.base_decode('ZmxhZ3t3YXJ0YW5rZXJ9', base=64)
'flag{wartanker}'
>>> crypto.base_decode('MZWGCZ33O5QXE5DBNZVWK4T5', base=32)
'flag{wartanker}'
>>> crypto.base_decode('666C61677B77617274616E6B65727D', base=16)
'flag{wartanker}'
```

`wartanker.crypto.base_decode`는 `base`에 따라 문자열을 디코딩한 값을 반환합니다.

```python
>>> crypto.base_decode('ZmxhZ3t3YXJ0YW5rZXJ9')
'flag{wartanker}'
>>> crypto.base_decode('MZWGCZ33O5QXE5DBNZVWK4T5')
'flag{wartanker}'
>>> crypto.base_decode('666C61677B77617274616E6B65727D')
'flag{wartanker}'
```

`base`가 지정되지 않은 경우, `b64decode`, `b32decode`, `b16decode`를 차례로 시도하여 자동으로 문자열을 디코딩합니다. 만약 어느 것으로도 디코딩할 수 없으면, `UnknownBaseError`를 raise합니다.

### `wartanker.crypto.str2hex`

### `wartanker.crypto.hex2str`

### `wartanker.crypto.caesar_encrypt`
```python
>>> crypto.caesar_encrypt('The quick brown fox jumps over the lazy dog', 5)
'Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl'
```
### `wartanker.crypto.caesar_decrypt`

```python
>>> crypto.caesar_decrypt('Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl', 5)
[*] key: 5  =>  The quick brown fox jumps over the lazy dog
```

```python
>>> crypto.caesar_decrypt('Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl')
[*] key: 0  =>  Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl
[*] key: 1  =>  Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk
[*] key: 2  =>  Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj
[*] key: 3  =>  Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi
[*] key: 4  =>  Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph
[*] key: 5  =>  The quick brown fox jumps over the lazy dog
[*] key: 6  =>  Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf
[*] key: 7  =>  Rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme
[*] key: 8  =>  Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald
[*] key: 9  =>  Pda mqeyg xnksj bkt fqilo kran pda hwvu zkc
[*] key: 10  =>  Ocz lpdxf wmjri ajs ephkn jqzm ocz gvut yjb
[*] key: 11  =>  Nby kocwe vliqh zir dogjm ipyl nby futs xia
[*] key: 12  =>  Max jnbvd ukhpg yhq cnfil hoxk max etsr whz
[*] key: 13  =>  Lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy
[*] key: 14  =>  Kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx
[*] key: 15  =>  Jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew
[*] key: 16  =>  Iwt fjxrz qgdlc udm yjbeh dktg iwt apon sdv
[*] key: 17  =>  Hvs eiwqy pfckb tcl xiadg cjsf hvs zonm rcu
[*] key: 18  =>  Gur dhvpx oebja sbk whzcf bire gur ynml qbt
[*] key: 19  =>  Ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas
[*] key: 20  =>  Esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr
[*] key: 21  =>  Dro aesmu lbygx pyh tewzc yfob dro vkji nyq
[*] key: 22  =>  Cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp
[*] key: 23  =>  Bpm ycqks jzwev nwf rcuxa wdmz bpm tihg lwo
[*] key: 24  =>  Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn
[*] key: 25  =>  Znk waoiq hxuct lud pasvy ubkx znk rgfe jum
```

<!-- wartanker.forensic -->
## `wartanker.forensic`

```python
>>> from wartanker import forensic
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.forensic.get_fileinfo`

```python
>>> forensic.get_fileinfo('./examples/dump')
'./examples/dump: ASCII text'
```
```python
>>> forensic.get_fileinfo('./examples/file_a')
'./examples/a: PNG image data, 1472 x 702, 8-bit/color RGBA, non-interlaced'
```
```python
>>> forensic.get_fileinfo('./examples/file_b')
'./examples/b: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=0b9532aeba00a8b33aa9d296ec424970e3bf67b9, stripped'
```
```python
>>> forensic.get_fileinfo('./examples/file_c')
'./examples/c: Zip archive data, at least v1.0 to extract'
```
```python
>>> forensic.get_fileinfo('./examples/file_d')
'./examples/d: PE32 executable (GUI) Intel 80386, for MS Windows'
```

파일에 대한 정보를 불러옵니다.

### `wartanker.forensic.find_flag`

```python
>>> forensic.find_flag('W4RT4NK3R', './examples/dump')
['W4RT4NK3R{fake}', 'W4RT4NK3R{real_flag}']
```

플래그 형식을 정규표현식으로 입력받아 파일에서의 검색 결과를 리스트로 반환합니다.

<!-- wartanker.hash -->
## `wartanker.hash`
```python
>>> from wartanker import hash
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.hash.sha256encode`

### `wartanker.hash.sha384encode`

### `wartanker.hash.sha512encode`

### `wartanker.hash.sha_encode`

### `wartanker.hash.md5encode`

<!-- wartanker.pwnable -->
## `wartanker.pwnable`
```python
>>> from wartanker import pwnable
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.pwnable.terminal`

```python
>>> pwnable.terminal('id')
'uid=501(junhoyeo) gid=20(staff) groups=20(staff),501(access_bpf),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin),701(1),33(_appstore),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh)'
```

커맨드를 터미널에서 실행하고 그 결과를 문자열로 반환합니다.

<!-- wartanker.reversing -->
## `wartanker.reversing`
```python
>>> from wartanker import reversing
[*] Wartanker, the Python3 toolkit for solving CTF problems
```

### `wartanker.reversing.crypto_solver`

```python
>>> f = '''
... def one(num, size):
...     r = num + size
...     r += 915
...     return r
...
... def two(num, size):
...     r = num - size
...     r -= 372
...     return r
...
... def three(num, size):
...     r = num ^ size
...     r ^= 826
...     return r
...
... def four(num, size):
...     size %= 32
...     r = num >> (32 - size)
...     b = (num << size) - (r << 32)
...     return b + r
... '''
>>> result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328,7360, 4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
>>> reversing.crypto_solver('four(three(two(one(j, 100), 100), 100), 100)', result, functions=f)
'FLAG{Rev3rse_P1us_M1nus_X0R_R0L}'
```

Exploit of ROOTCTF 2017 prob `Calculate`

<!-- wartanker.web -->
## `wartanker.web`
```python
>>> from wartanker import web
[*] Wartanker, the Python3 toolkit for solving CTF problems
```
### `wartanker.web.xss_exploit`
```python
>>> web.xss_exploit('post', 'https://www.uhmtoto.xyz/board/write.php', 'content', {}, {'user':'aa', 'PHPSESSID':'**************************'}, 'https://www.uhmtoto.xyz/board/board')
[*] trying 0 of 68
[*] trying 1 of 68
[*] trying 2 of 68
[*] trying 3 of 68
[*] trying 4 of 68
[*] trying 5 of 68
[*] How about trying '<IMG SRC=javascript:alert(&quot;XSS&quot;)>'?
[*] Do you want more? [Y / N] y
[*] trying 6 of 68
[*] trying 7 of 68
[*] How about trying '<IMG """><SCRIPT>alert("XSS")</SCRIPT>">'?
[*] Do you want more? [Y / N] y
[*] trying 8 of 68
[*] How about trying '<a onmouseover=alert(document.cookie)>xxs link</a>'?
[*] Do you want more? [Y / N] n
```
`wartanker.web.xss_exploit`은 미리 저장된 XSS 페이로드 들을 이용해 Stored XSS 공격을 자동으로 수행해줍니다. 함수의 인자값은 `web.xss_exploit(method, URL, name, param, cookie, testURL)`으로, `method`에는 XSS Payload를 포함한 글을 올릴때 사용할 방법을 지정해야합니다. ( `get`이나 `post` ) `URL`에는 게시글을 올려줄 URL을 지정해야합니다. `name`에는 게시글 내용이 담길 변수를 지정해야 합니다. `param`에는 게시글을 올릴 때 게시글 내용을 제외하고 필요한 다른 파라미터들을 딕셔너리 형식으로 지정해야합니다. `cookie`에는 게시글을 올릴 때 필요한 세션값 등 쿠키값을 딕셔너리 형식으로 지정해야합니다. 마지막으로 `testURL`에는 XSS Payload를 포함할 게시글이 올라올 페이지의 URL을 지정해야 합니다.

#### 사용 예
```python
web.xss_exploit('post', 'https://www.uhmtoto.xyz/board/write.php', 'content', {}, {'user':'aa', 'PHPSESSID':'**************************'}, 'https://www.uhmtoto.xyz/board/board')
```
`https://www.uhmtoto.xyz/board`
