## Text Processing

### awk
* 설명
    - 텍스트 처리 script language
    - syntax: awk options 'selection _criteria {action }' input-file
    - https://man7.org/linux/man-pages/man1/awk.1p.html

* 시놉시스
    - **awk** [−F *sepstring*] [−v *assignment*]... *program* [*argument*...]...

* 자주 사용되는 옵션
    - -F    :field seperator 지정

* 주요 내장 변수
    - $1, $2, $3, ...   :Nth field
    - NR                :nmber of records
    - NF                :number of fields
    - FS                :field separator(default 'white space')
    - RS                :record separator(default 'new line')
    - OF                :Output field separator
    - ORS               :Output record separator

* 사용 예제
    - wc /etc/passwd | awk '{ print $1 }'
    - head /etc/passwd | awk -F: '{ print $1 }'  # field seperator ':'
    - head /etc/passwd | awk -F: '/sy/ { print $1 }'  # pattern search
    - head /etc/passwd | awk -F: '/sy/ { print }'  # pattern search and print whole line
    - head /etc/passwd | awk -F: '{ print NR, $1 }'
    - head /etc/passwd | awk -F: '{ print NR "==> " $1,NF }'
