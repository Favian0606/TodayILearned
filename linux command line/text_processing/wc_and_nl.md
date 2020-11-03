## Text Processing

### wc
* 설명
    - line/word/byte 단위의 count 출력
    - print newline, word, and byte counts for each file
    - Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.  A word is a non-zero-length sequence of characters delimited by white space.
    - https://man7.org/linux/man-pages/man1/wc.1.html

* 시놉시스
    - **wc** [*OPTION*] ... [*FILE*] ...
    - **wc** [*OPTION*] ... --files0-from=F

* 자주 사용되는 옵션
    - -l, --lines   :라인수 만 출력; print the newline counts

* 사용 예제
    - wc FILENAME   # line/word/byte 각각 다 formatting하여 출력됨
    - wc -l FILENAME
    - cat FILENAME | wc -l  # stdin으로부터 라인수만 획득
    - wc -l FILENAME | cut -d ' ' -f 1 # 라인수만 획득; cut으로 delimiter를 whitespace -> 첫번째것 획득
    - wc -l FILENAME | awk '{ print $1 }'   # 라인수만 획득
    - wc *.c # 여러 파일 입력 시 합계 출력

### nl
* 설명
    - 파일 내용을 라인 넘버와 함께 출력
    - number lines of files
    - Write each FILE to standard output, with line numbers added
    - https://man7.org/linux/man-pages/man1/nl.1.html

* 시놉시스
    - **nl** [*OPTION*] ... [*FILE*] ...

* 자주 사용되는 옵션
    - -b, --body-numbering=*STYLE*  :use STYLE for numbering body lines
    - STYLE
        + a     :number all lines
        + t     :number only nonempyt lines
        + n     :number no lines
        + ......
    - -ba   :모든 라인에 대해 라인 넘버링
    - -v, --starting-line-number=*NUMBER*   :first line number for each section
    - -v N :시작 라인 넘버를 N으로 지정
    - -s, --number-separator=*STRING*   :add STRING after (possible) line number; 라인 넘버 출력 후 출력할 separator 지정

* 사용 예제
    - nl FILENAME
    - nl -ba FILENAME
    - nl -ba -s ":    " FILENAME
    - nl -ba -s ":    " FILENAME | tail