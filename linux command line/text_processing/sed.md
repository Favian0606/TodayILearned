## Text Processing

### sed
* 설명
    - stream editor
    - stream editor for filtering and transforming text
    - A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline).
    - https://man7.org/linux/man-pages/man1/sed.1.html

* 시놉시스
    - **sed** [*OPTION*]... {*script-only-if-no-other-script*} [*input-file*]...

* 자주 사용되는 옵션
    - {RANGE}p  :range 내의 라인을 출력
    - {RANGE}d  :range 내의 라인을 삭제
    - /SEARCHPATTERN/p    :SEARCHPATTERN과 매치되는 라인을 출력
    - /SEARCHPATTERN/d    :SEARCHPATTERN과 매치되는 라인을 삭제
    - s/REGEX/REPLACE    :REGEX에 매치되는 부분을 REPLACE로 교체 (subsitute)

* 사용 예제
    - head /etc/passwd | sed -n '1, 3p'
    - head /etc/passwd | sed '1, 3d'
    - head /etc/passwd | sed -n '/nologin/p'
    - head /etc/passwd | sed 's/daemon/DAEMON/'
    - head /etc/passwd | sed 's/daemon/DAEMON/g'
    - head /etc/passwd | sed '3,5 s/:/^/g'
    - head /etc/passwd | sed -n '/games/,+2p'  # 패턴매칭으로부터 상대적으로 2번째 이후까지 출력