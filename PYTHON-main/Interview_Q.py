

* Fibanacci Series
def fib(n):
    a = 0
    b = 1
    if n == 1:
    print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)

* Factoral for given number
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result)
    
* Remove duplicate values from list
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i)

* How to know given number is even or odd
list1 = [10, 21, 4, 45, 66, 93, 1] 
  
even_count, odd_count = 0, 0
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if num % 2 == 0: 
        even_count += 1
  
    else: 
        odd_count += 1
          
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 

* How to list prime numbers in range of 1 to 20
for num in range(1,20):
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            print(num)
        
* How to know given numbers is prime number or not

num = int(input("enter the number"))
for num in range(1,20):
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            print("the given number is a prime number")
* Prime number in list comprihence
* Gmail id matching using regular expressions
* IP address matching using regular expressions
* Use of re.sub()
* MAC address matching using regular expressions

* Reverse a string
By using [::-1] we can reverse the string.

* Anagram logic
the two strings have same set of characters but the sequence of the those strings are different is known as anagrams
def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
s1 ="listen"
s2 ="silent" 
check(s1, s2) 
* Palindrome Logic
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
    
* Swap 2 values of 2 variables without using a third variable
a=2
b=3
a,b=b,a
print('the value of a:'a)
print('the value of b:'b)

* Find Max and Min values without max and min functions
* Convert two lists into one dictionary and list into dictionary
# initializing lists 
test_keys = ["Rash", "Kil", "Varsha"] 
test_values = [1, 4, 5] 
  
# Printing original keys-value lists 
print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  
# using naive method 
# to convert lists to dictionary 
res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break  
  
# Printing resultant dictionary  
print ("Resultant dictionary is : " +  str(res)) 

* remove duplicate characters in string
def removeDuplicate(str): 
    s=set(str) 
    s="".join(s) 
    print("Without Order:",s) 
    t="" 
    for i in str: 
        if(i in t): 
            pass
        else: 
            t=t+i 
        print("With Order:",t) 
      
str="geeksforgeeks"
removeDuplicate(str) 
* Get duplicate lines count in a file
* Get only number words count in a file
* Get repeated words count in a file
* Get each character count in a string 
* write one file data into another file 
* write 3files data into one file
data = data2 = "" 
  
# Reading data from file1 
with open('file1.txt') as fp: 
    data = fp.read() 
  
# Reading data from file2 
with open('file2.txt') as fp: 
    data2 = fp.read() 
  
# Merging 2 files 
# To add the data of file2 
# from next line 
data += "\n"
data += data2 
  
with open ('file3.txt', 'w') as fp: 
    fp.write(data)  
* Use of *args and **kwargs 
1.)*args (Non-Keyword Arguments)
2.)**kwargs (Keyword Arguments)
* How to find given string is lower or not ?
ch = input("Please Enter Your Own Character : ")

if(ch.isupper()):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
elif(ch.islower()):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
    
* D/B extend and append in list methods ?
Python append() method adds an element to a list, and the extend() method concatenates the first list with another list 
(or another iterable). ... Whereas extend() method iterates over its argument adding each element to the list, extending the list.
A string is an iterable, so if you extend a list with a string, you’ll append each character as you iterate over the string.

my_list = ['geeks', 'for', 'geeks'] 
another_list = [6, 0, 4, 1] 
my_list.append(another_list) 
print my_list 
['geeks', 'for', 'geeks', [6, 0, 4, 1]]

my_list = ['geeks', 'for', 6, 0, 4, 1] 
my_list.extend('geeks') 
print my_list 
Output:
['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']

my_list = ['geeks', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 
print my_list 
Output:
['geeks', 'for', 6, 0, 4, 1]

* D/B remove and pop ?
list.remove(value)
Yes, remove() removes the first matching value/object. It does not do anything with the indexing.
myList = [1, 2, 3, 2]
myList.remove(2) 
myList 
#[1, 3, 2]
If you want to remove all the occurrences of an element in the list, you need to loop over all elements. Check the element and remove if it is present.

del list[index]
del removes the item at a specific index.
myList = [3, 2, 2, 1]
del myList[1]
myList 
#[3, 2, 1]
list.pop(index)
And pop removes the item at a specific index and returns it.
myList = [4, 3, 5]
myList.pop(1) 
#3 
myList 
#[4, 5]
* D/B list and tuple ?

SL.     LIST	                                        TUPLE
1	Lists are mutable	                            Tuple are immutable
2	Implication of iterations is Time-consuming     Implication of iterations is comparatively Faster
3	The list is better for performing operations,   Tuple data type is appropriate for accessing the elements
such as insertion and deletion.	
4	Lists consume more memory                       Tuple consume less memory as compared to the list
5	Lists have several built-in methods	            Tuple does no have must built-in methods.
6	The unexpected changes and errors are more      In tuple, it is hard to take place.
likely to occur	

* D/B open and with open to open a file ?
* D/B match and search methods in re module ?
* How to handle exceptions in python ?
* Use of break, pass and continue ?
* Use of type() and dir() functions ?
* Use of self in class method.
* Use of __init__ method in class ?
* Use of dir() function ?
dir() is a powerful inbuilt function in Python3, which returns list of the attributes 
and methods of any object (say functions , modules, strings, lists, dictionaries etc.)

* What is inheritance and D/B multi inheritance and multi-level ?
* Types of parameters for function ?
There are three types of Python function arguments using which we can call a function.
Default Arguments
Keyword Arguments
Variable-length Arguments
In this particular example, the function took three arbitrary variables using one variable with either asterisk(*) or double asterisk(**),
but using variable length arguments we can take any number of arbitrary arguments.
* Use of map() and reduce() functions ?
def cube(y): 
    return y*y*y; 
  
g = lambda x: x*x*x 
print(g(7)) 
  
print(cube(5)) 

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 

from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 

* Use of decorator ?
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
Wrappers around the function are also known as Decorators. 

# defining a decorator 
def hello_decorator(func): 
  
    # inner1 is a Wrapper function in  
    # which the argument is called 
      
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
  
        # calling the actual function now 
        # inside the wrapper function. 
        func() 
  
        print("This is after function execution") 
          
    return inner1 
  
  
# defining a function, to be called inside wrapper 
def function_to_be_used(): 
    print("This is inside the function !!") 
  
  
# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 
  
  
# calling the function 
function_to_be_used() 
Output:

Hello, this is before function execution
This is inside the function !!
This is after function execution

* Use of len() function?
len() function is an inbuilt function in Python programming language that returns the length of the string.
# Length of below string is 15 
string = "geeks for geeks" 
print(len(string)) 

* How to convert list values into string ?
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join([str(elem) for elem in s]) 
  
print(listToStr)  

* How to match date using regx
* Use of re.sub ?
* Use of id() function.
The id() function returns a unique id for the specified object. All objects in Python has its own unique id.
The id is assigned to the object when it is created.
* Use of update method in dictionary.
* Get a even numbers from 1 to 100 using map

* How to add new value to set ?
* how to know list length ?
* Use os super function ? 


            ####      ROBOT FRAMEWORK       ####
1) What is robot framework.
2) How to develop keywords 
3) How to import python file 
4) What are the predefine keywords you have used.
5) How to import variable file
6) Use of resourse file
7) How to run particular test case
8) How to run test cases based on tag
9) Use of dryrun option 
10) How to define setup ?
11) Use of tags
12) How to import resourse file.
13) How to pass values to variable through command line


           ###      SELENIUM       ####
1) What is selenium 
2) Types of waits and difference
3) How to open new tab ?
4) How to select dropdown values 
5) How to click on element 
6) How to take screenshot 
7) How to get text 
8) How to get window title
9) How to do mouse operations 
10) How to do double click operations 
11) How to handle popups 
12) How to refresh page
13) How to do scroll down
14) How to enter text into text box
15) What are the element identifiers


                ###          REST API         ###
1) Use of REST API 

REPRESENTATIONAL STATE TRASFER APPLICATION PROGRAMMING INTERFACE

How to Use Python Requests with REST APIs. The GET method is used to access data for a specific resource from a REST API; 
Python Requests includes a function to do exactly this. The response object contains all the data sent from the server in response
 to your GET request, including headers and the data payload.
 
2) Use of put
Replaces all current representations of the target resource with the uploaded content.
PUT /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Connection: Keep-Alive
Content-type: text/html
Content-Length: 182

3) Use of post
A POST request is used to send data to the server, for example, customer information, file upload, etc. using HTML forms.
POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: text/xml; charset=utf-8
Content-Length: 88
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

4) Which module you gave used for automate rest API ?
REST or RESTful API using JSON format has been very popular now because of its simplicity I believe. In this article,
I am going to show you how to use Python to create a REST automation test suite using requests and flask modules.
5) What is the status code 200 indicate
The HTTP 200 OK success status response code indicates that the request has succeeded. A 200 response is cacheable by default.
The meaning of a success depends on the HTTP request method: GET : The resource has been fetched and is transmitted
in the message body
200 OK
The request is OK.

6) Use of get method
The GET method is used to retrieve information from the given server using a given URI.
Requests using GET should only retrieve data and should have no other effect on the data.

GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

7) What are the HTTP methods

The set of common methods for HTTP/1.1 is defined below and this set can be expanded based on requirements.
These method names are case sensitive and they must be used in uppercase.

S.N.	Method and Description
1	GET
The GET method is used to retrieve information from the given server using a given URI.
Requests using GET should only retrieve data and should have no other effect on the data.

2	HEAD
Same as GET, but transfers the status line and header section only.

3	POST
A POST request is used to send data to the server, for example, customer information, file upload, etc. using HTML forms.

4	PUT
Replaces all current representations of the target resource with the uploaded content.

5	DELETE
Removes all current representations of the target resource given by a URI.

6	CONNECT
Establishes a tunnel to the server identified by a given URI.

7	OPTIONS
Describes the communication options for the target resource.

8	TRACE
Performs a message loop-back test along the path to the target resource.

8) How did you automated REST calls ?
9) What is the status code 201 indicate
HTTP Status 201 indicates that as a result of HTTP POST request, one or more new resources have been successfully created on server.

201 created
The request is complete, and a new resource is created .

10) What is the status code 400 indicate
400 (Bad Request)
This is a list of Hypertext Transfer Protocol (HTTP) response status codes.
Status codes are issued by a server in response to a client's request made to the server. ... The first digit of the status code defines the class of response,
while the last two digits do not have any classifying or categorization role.
400 (Bad Request)
The server did not understand the request.

11) What is the status code 404 indicate
404 (Not Found client error)
The 404 error status code indicates that the REST API can't map the client's URI to a resource but may be available in the future.
Subsequent requests by the client are permissible.
404 Not Found
The server can not find the requested page.

12) What is the status code 500 indicate
The HyperText Transfer Protocol (HTTP) 500 Internal Server Error server error response code indicates that the server encountered
an unexpected condition that prevented it from fulfilling the request.

500 Internal Server Error	
The request was not completed. The server met an unexpected condition.

Learn HTTP:- https://www.tutorialspoint.com/http/http_status_codes.htm

def reverseWordSentence(Sentence): 
  
    # All in One line 
    return ' '.join(word[::-1] for word in Sentence.split(" ")) 
  
# Driver's Code  
Sentence = "Geeks for Geeks"
print(reverseWordSentence(Sentence))     
Output:
 
skeeG rof skeeG

def bubbleSort(arr): 
    n = len(arr)  
    for i in range(n):      
        for j in range(0, n-i-1): 
              if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]   
  
print(bubbleSort(arr))  

'''Deepcopy'''
In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect 
in the original object. In python, this is implemented using “deepcopy()” function.
'''Shallowcopy'''
In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do 
reflect in the original object. In python, this is implemented using “copy()” function.

a Python class is for defining a particular type of object. Because Python objects can have both function and data elements,
Python classes define what methods can be used to change the state of an object. 
They also indicate what attributes the object can have.

An object is simply a collection of data (variables) and methods (functions) that act on those data.
An object is created using the constructor of the class. This object will then be called the instance of the class.


'''Format'''	
Initialization, condition checking, iteration statement are written at the top of the loop.	
Only initialization and condition checking is done at the top of the loop.
'''Use'''	
The 'for' loop used only when we already knew the number of iterations.	
The 'while' loop used only when the number of iteration are not exactly known.
'''Condition'''
If the condition is not put up in 'for' loop, then loop iterates infinite times.
If the condition is not put up in 'while' loop, it provides compilation error.

200 - OK, shows success.
201 - CREATED, when a resource is successful created using POST or PUT request. 
Return link to newly created resource using location header.
304 - NOT MODIFIED, used to reduce network bandwidth usage in case of conditional GET requests. Response body should be empty. 
Headers should have date, location etc.
400 - BAD REQUEST, states that invalid input is provided e.g. validation error, missing data.
401 - FORBIDDEN, states that user is not having access to method being used for example, delete access without admin rights.
404 - NOT FOUND, states that method is not available.
409 - CONFLICT, states conflict situation while executing the method for example, adding duplicate entry.
500 - INTERNAL SERVER ERROR, states that server has thrown some exception while executing the method.

def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
triangle(n)


