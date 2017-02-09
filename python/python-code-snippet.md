# Python 기초 코드 패턴 snippets

### How to read an array of integers from single line of input
***
*I want to read an array of integers from single line of input in python3.*
```
1 3 5 7 9
```

``` 
arr = list(map(int, input.split())) 
```

- Return an iterator that applies function to every item of iterable, yielding the results.
- map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
- 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 반환하는 함수다.
*python 2.7에서는 map의 결과가 list
*int도 함수라는 것을 알 수 있다.

http://stackoverflow.com/questions/7132861/building-full-path-filename-in-python

```
directory_seq = int(directory_seq)
    targetpath = '%s/%s/%02d/%s/%02d/%02d' \
                 % (basedir, thirddir, directory_seq, \
                    int(date[0:4]), int(date[5:7]), int(date[8:10]))
    file_path = os.path.join(targetpath, 'merged.json')
    item_list = []
    filenames = glob.glob('%s/*.json' % targetpath)

    for filename in filenames:
        item = file_read(filename)
        item_list.append(item)

    with open(file_path, "w") as outfile:
        json.dump(item_list, outfile, sort_keys=True, indent=4, ensure_ascii=False)
```