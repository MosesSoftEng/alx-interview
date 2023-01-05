# :book: 0x00. Pascal's Triangle
## Topics Covered
1. Python.
2. Pascal's Triangle.

# :computer: Tasks.
## [1. Don't make a promise...if you know you can't keep it](1-promise.js)
### Task requirements.
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

  *  Returns an empty list if n <= 0
  *  You can assume n will be always an integer
```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

### :wrench: Task setup.
```bash
# Create task file and set write permission.
touch ./0-pascal_triangle.py
chmod +x ./0-pascal_triangle.py
./0-pascal_triangle.py

pycodestyle ./0-pascal_triangle.py
pep8 ./0-pascal_triangle.py

# Create test file
touch ./0-main.py
chmod +x ./0-main.py
./0-main.py
```

### :heavy_check_mark: Solution.
> [:point_right: Go to 1-promise.js](1-promise.js)

# :books: References
1. [Pascal's Triangle](https://www.cuemath.com/algebra/pascals-triangle/)
2. [Python Lists](https://www.w3schools.com/python/python_lists.asp)

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhatsApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.
