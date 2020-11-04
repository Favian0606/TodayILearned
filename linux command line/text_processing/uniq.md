## Text Processing

### uniq
* 설명
    - 중복된 내용 제거하고 출력
    - sort와 자주 같이 쓰임 (uniq가 연속된 중복 그룹 안에서만 체크하기 때문)
    - report or omit repeated lines
    - https://man7.org/linux/man-pages/man1/uniq.1.html

* 시놉시스
    - **uniq** [*OPTION*] ... [*FILE*[*OUTPUT*]] ...

* 자주 사용되는 옵션
    - -d, --repeated    :중복된 내용만 출력; only print duplicate lines, one for each group
    - -u, --unique  :중복되지 않은 내용만 출력
    - -i, --ignore-case :대소문자 무시

* 사용 예제
    - uniq uniq_sample | nl
    - sort uniq_sample | uniq | nl
    - sort uniq_sample | uniq -i | nl
    - sort uniq_sample | uniq -d | nl
    - sort uniq_sample | uniq -u | nl
    - grep "shm_open" *.c | awk -F: '{ print $1 }' | uniq