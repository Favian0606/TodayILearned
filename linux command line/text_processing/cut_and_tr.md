## Text Processing

### cut
* 설명
    - 컬럼 잘라내기
    - remove sections from each line of files
    - Print selected parts of lines from each FILE to standard output
    - https://man7.org/linux/man-pages/man1/cut.1.html

* 시놉시스
    - **cut** [*OPTION*] ... [*FILE*] ...

* 자주 사용되는 옵션
    - -b, --bytes=LIST  :byte 선택
    - -c, --characters=LIST :character 선택
    - -f, --fields=LIST :필드(컬럼) 선택
    - -d, --delimiter=DELIM :tab 대신 사용할 구분자 지정; use DELIM instead of TAB for field delimiter
    - --complement  :선택 반전; complement the set of selected bytes
    - --output-delimiter=STRING :출력시 사용할 구분자 지정

* 사용 예제
    - head /etc/passwd | cut -d ':' -f 1,7
    - head /etc/passwd | cut -d ':' -f 1,7 --output-delimiter=': '
    - ls -al | cut -b -10
    - ls -al | cut -b -10 --complement

### tr
* 설명
    - 어떤 내용을 변환(translate)한다
    - Translate, squeeze, and/or delete characters from standard input, writing to standard output
    - https://man7.org/linux/man-pages/man1/tr.1.html

* 시놉시스
    - **tr** [*OPTION*] ... *SET1*[*SET2*] ...

* 자주 사용되는 옵션
    - -c, -C, --complement
    - -d, --delete  :delete characters in SET1, do not translate
    - SET
        + CHAR1-CHAR2   :CHAR1부터 CHAR2까지(예:'a-z')
        + [:alnum:] :문자 + 숫자
        + [:alpha:] :문자
        + [:blank:] :공백
        + [:space:] :공백 + newline
        + [:digit] / [:xdigit]  :10진수 숫자 / 16진수 숫자
        + [:lower:] / [:upper:] :소문자 / 대문자

* 사용 예제
    - head /etc/passwd | tr -d '/'
    - head /etc/passwd | tr ':' '%'
    - head /etc/passwd | tr [:lower:] [:upper:]
