### 문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

    1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한 사항

- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예

genres | plays | return
:-------------------------:|:-------------------------:|:-------------------------:
["classic", "pop", "classic", "classic", "pop"] | [500, 600, 150, 800, 2500] | [4, 1, 3, 0]

### 입출력 예 설명

classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

    * 고유 번호 3: 800회 재생
    * 고유 번호 0: 500회 재생
    * 고유 번호 2: 150회 재생

pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

    * 고유 번호 4: 2,500회 재생
    * 고유 번호 1: 600회 재생

따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

---

### Solution code

```python
def solution(genres, plays):
    answer = []
    
    genre_total_play = {}
    genre_item = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_total_play:
            genre_total_play[genre]['total_play'] += play
            genre_total_play[genre]['songs'].append((play, -1 * i))
        else:
            genre_total_play[genre] = {'total_play': play,
                                       'songs': [(play, -1 * i)]}
    
    genre_total_play_sorted = sorted(genre_total_play.items(), key=lambda x: x[1]['total_play'], reverse=True)
    
    for genre_item in genre_total_play_sorted:
        cur_genre_songs = genre_item[1]['songs']
        cur_genre_songs.sort(reverse=True)
        for i, song in enumerate(cur_genre_songs):
            if i > 1: break
            answer.append(song[1] * -1)
    
    return answer
```

---

### Notes

- Hash 문제
- genres와 plays 리스트를 순회하면서 dict 생성
- 각 장르별 노래 list 생성 시, 이후 재생수 정렬을 우선순위로 두기 위해 `(play, -1 * i)`
- list of tuples를 sort시에 각 element 순서대로 정렬
- 내림차순 정렬(reverse=True)을 위해서 노래의 고유번호에 -1 곱하기
- https://stackoverflow.com/questions/28668738/sort-list-of-tuples-with-multiple-criteria
