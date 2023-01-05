# :book: Interview Questions.
## Topics Covered.
1. Python List, List Comprehession.

## Project setup.
```bash
# Create project directory.
mkdir ./alx-interview
cd ./alx-interview

# Create new repo.
git init

# Install python linter.
pip install pycodestyle==2.8.0
pip install pep8==1.7.0
```

# :computer: Projects.
## [0x00. Pascal's Triangle](0x00-pascal_triangle)
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

### :heavy_check_mark: Solution.
> [:point_right: task_5](task_5)

# :books: References.
1. []()

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhatsApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.