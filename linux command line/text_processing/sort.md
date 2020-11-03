## Text Processing

### sort
* 설명
    - 정렬하여 출력
    - sort lines of text files
    - Write sorted concatenation of all FILE(s) to standard output  
    - https://man7.org/linux/man-pages/man1/sort.1.html

* 시놉시스
    - **sort** [*OPTION*] ... [*FILE*] ...
    - **sort** [*OPTION*] ... --files0-from=F

* 자주 사용되는 옵션
    - 위치 지정
        + -k, --key=*KEYDEF*  :key에 의한 정렬 수행; sort via a key(KEYDEF gives location and type)
        + -t, --field-seperator=*SEP* :필드 구분자(기본값은 공백 문자); use SEP instead of non-blank to blank transition

    - 정렬 기준
        + -f, --ignore-case :fold lower case to upper case characters
        + -g, --general-numeric-sort    :compare according to general numerical value
        + -n, --numeric-sort    :compare according to string numerical value
        + -r, --reverse :reverse the result of comparisons
        + -u, --unique  :with -c, check for strict ordering; without -c, output only the first of an equal run

    - 다른 옵션
        + --debug   :annotate the part of the line used to sort; sort 기준이 된 부분에 밑줄

    - KEYDEF
        + F[.C][OPTS][,F[.C][OPTS]]; start and stop position, where F is a field number and C a character position in the field

* 사용 예제
    - cat /etc/passwd | sort -t: -k 3 -n   # delimiter를 ':'로 설정, 3번째 컬럼, numeric-sorting
    - cat /etc/passwd | sort -t: -k 2,2 --debug
    - cat /etc/passwd | sort -t: -k 5,5 -k 1,1 --debug