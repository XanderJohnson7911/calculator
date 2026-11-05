The README file for the calculator (DevOps)

The calculator

A Python 3 calculator used from the Terminal, built step by step in SCCM4910 (DevOps)

Functionality
It will be able to add, subtract, multiply and divide two number and display the result

Running it
Make sure you have python3 installed
Run : ~/h-drive/DevOps/calculator/run.sh

When prompted:
Enter the first number, then an operator (+,-,*,/), then a second number
The program will then print 
"Result : " then the answer

Testing
We can run a test program called check.sh to test the calculator
It will run 5 tests, testing each of the add, sub, multiply and divide
functions, then testing adding with negative numbers.
Firstly, run 
source /opt/python-venv/sccm-4910/bin/activate
This will create an environment with the tools with need to run the test
Then inside the calculator folder, run ./check.sh
It will output "QUALITY GATE PASSED" if the checks pass, it will also output 0
which can be seen when running echo $? after the test.
We can also run the check.sh from elsewhere in the computer, by running
~/h-drive/DevOps/calculator/check.sh
