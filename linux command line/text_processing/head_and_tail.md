## Text Processing

### head
* 설명
    - 문서 내용의 앞 부분 출력
    - output the first part of files
    - Print the first 10 lines of each FILE to standard output.
    - With no FILE, or when FILE is -, read standard input.
    - https://man7.org/linux/man-pages/man1/head.1.html

* 시놉시스
    - **head** [*OPTION*] ... [*FILE*] ...

* 자주 사용되는 옵션
    - -c, --bytes=*[-]NUM*  :NUM bytes만 출력
    - -n, --lines=*[-]NUM*  :NUM line만 출력
    - **NUM**
        + NUM may have a multiplier suffix: b 512, kB 1000, K 1024, MB 1000*1000 ...
        + byte 입력 시 K, M, G, T 입력 가능
        + 옵션의 NUM 값을 '-'(마이너스)로 주면, 파일의 마지막부터 해당 NUM 만큼 제외하고 출력

* 사용 예제
    - head /etc/passwd
    - head -n 1 /etc/passwd
    - cat /etc/passwd | head -n 15
    - cat /etc/passwd | head - n -5

### tail
* 설명
    - 문서 내용의 뒷 부분 출력
    - output the last part of files
    - Print the last 10 lines of each FILE to standard output.
    - With no FILE, or when FILE is -, read standard input.
    - https://man7.org/linux/man-pages/man1/tail.1.html

* 시놉시스
    - **tail** [*OPTION*] ... [*FILE*] ...

* 자주 사용되는 옵션
    - -c, --bytes=*[-]NUM*  :NUM bytes만 출력
    - -n, --lines=*[-]NUM*  :NUM line만 출력
    - -f, --follow[={name|descr}]   :output appended data as the file grows; 파일에 추가되는 내용 append하도록 대기
    - -F, same as --follow=name --retry : 파일이 truncate 되는 경우 open 시도하여 follow
    - --retry   :keep trying to open a file if it is inaccessible
    - **NUM**
        + byte 입력 시 K, M, G, T 입력 가능
        + 옵션의 NUM 값을 '+'(플러스)로 주면, 문서 시작으로부터 NUM byte/line 지점에서 출력 시작

* 사용 예제
    - tail /etc/passwd -n 1
    - tail /etc/passwd -n +5
    - cat /etc/passwd | tail -n 15
    - cat /etc/passwd | tail -n +5