
# To know robot version
robot --version

# To run particular test case and Test cases 
    robot -t "Add Two Values" first_test.txt
    robot -t Addition -t "Test Case 3" first_test.txt
    robot -t  Add* first_test.txt

# paasing values to variable through command line =>
    robot -v ONE:10 -v TWO:34 Loop.txt

# validate the test data
    robot --dryrun test2_list.robot

# TO run a test case based on tag
    robot -i test2 first_test.txt

# TO run all test cases except given tag
    robot -e test2 first_test.txt

# Change logs path ==> 
    robot -d C:\ON-LINE\COURSES\2_ROBOT\Logs TEST_SUITE.robot
    robot -d LOGS TEST_SUITE.robot
                'OR' 
    robot --outputdir LOGS TEST_SUITE.robot


