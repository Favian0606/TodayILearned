# Python string

### String Formatting

- "%" 연산자는 "tuple"로 감싸여진 변수 세트를 포매팅하는데 이용된다.

```
name = 'kwanhong'
age = 27
print("%s is $d years old." % (name, age))
```

```
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
```

Basic argument specifiers
- %s - String (or any object with a string representation, like numbers)
- %d - Integers
- %f - Floating point numbers
- %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
- %x/%X - Integers in hex representations

```
targetpath = '%s/%s/%02d/%s/%02d/%02d' \
                 % (basedir, thirddir, directory_seq, \
                    int(date[0:4]), int(date[5:7]), int(date[8:10]))
```
