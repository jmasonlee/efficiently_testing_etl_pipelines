# Efficiencies of Right-Sizing Tests
This exercise is meant to give you a practical example on how the number of inputs to a test affect the number of tests you need to write and maintain in order to fully cover your system.


## The Assignment
When they are sold, diamonds are priced based on clarity, cut and color. Pretty Coal Diamonds sets their price based on the prices of diamonds worldwide. They have access to a worldwide system that records information about every diamond sold. Sometimes the price of a diamond is missing. In order for the missing price to not skew their data, Pretty Coal Diamonds fills in that field with the average price of a diamond of the same clarity, cut and color for that day.

For example, if this is the input dataset:
|carat|      cut|color|clarity|depth|table|price|   x|   y|   z|
|-----|---------|-----|-------|-----|-----|-----|----|----|----|
| 0.23|     Good|    E|    SI2| 61.5| 55.0|  200|3.95|3.98|2.43|
| 0.23|     Good|    E|    VS1| 56.9| 65.0| null|4.05|4.07|2.31|
| 0.23|     Good|    E|    VS2| 62.4| 58.0|  202| 4.2|4.23|2.63|

The null value in the middle row would be replaced with 201, as it is the average of the price of the other two diamonds of the same cut and color.

The piece of code that imputes the average price is in the src directory. Your task is to test it providing all possible combinations of values for each variable that affects the price.

### File Structure

There are 2 directories in this module. The src directory contains the code you are testing and the tests directory contains the test code you will be writing.

Inside of the tests directory is a file called diamond_pricing_test.py. This is the file you will be changing for this exercise. 

### 1. Run Your Tests

There is only one test inside of `diamond_pricing_test.py`. You should be able to run it from your terminal using the following command:

```
pytest efficiencies_of_right_sizing_tests/tests/diamond_pricing_test.py
```

If the run is successful, you will see output that looks like this:
```
================================================ test session starts ================================================
platform linux -- Python 3.8.16, pytest-7.3.0, pluggy-1.0.0
rootdir: /workspace/efficiently_testing_etl_pipelines
configfile: pyproject.toml
collected 1 item                                                                                                    

efficiencies_of_right_sizing_tests/tests/diamond_pricing_test.py .                                            [100%]

================================================ 1 passed in 13.15s =================================================
```

If you get an error like this:
```
bash: pytest: command not found
```

You will need to run the `./setup.sh` script manually by typing 
```
./setup.sh
```
From the root directory of the repository.

### 2. Add a price of None
The tests in `diamond_pricing_test.py` are set up to make it especially easy to add a new variation. Right now, we only have one test for a diamond with a price of 327.

![Starting Test](images/initial_test.png)

The price is wrapped in an array. We add a new test by adding a new item to that array.

![Two Tests](images/test_with_none.png)

When we run the tests, they will fail, because we haven't specified what the output should be.
```
============================================== short test summary info ==============================================
FAILED efficiencies_of_right_sizing_tests/tests/diamond_pricing_test.py::test_will_replace_null_prices_with_floating_averages - approvaltests.approval_exception.ApprovalException: Approval Mismatch, received != approved
================================================ 1 failed in 10.06s =================================================
```
The special setup to make it easier to add a new variation records the expected output in a file with the extension `.approved.txt`. In this case, the file recording our expected output is `diamond_pricing_test.test_will_replace_null_prices_with_floating_averages.approved.txt`. If the output doesn't match what we expected, our special test setup will record the actual output in a file with the extension `recieved.txt`. In this case, it has written out the new output to `diamond_pricing_test.test_will_replace_null_prices_with_floating_averages.received.txt`. A diff of the two files should pop up automatically. In gitpod, it looks like this:

![First Diff](images/first_diff.png)

Each line represents a test case. The portion before the `=>` represents the inputs. You can see a test case for a price of 327, and a test case for a price of None in the `received.txt` file. The portion after the `=>` represents the output of each test case. The test case with a price of None is highlighted in red because it doesn't exist in the `approved.txt` file.

The new test case in the `received.txt` file looks good. Let's approve it by clicking the arrow in between the two files. 

![arrow](images/arrow.png)

If you don't see a diff like the one above, you can also run:

```
mv diamond_pricing_test.test_will_replace_null_prices_with_floating_averages.received.txt diamond_pricing_test.test_will_replace_null_prices_with_floating_averages.approved.txt
```

If we run our tests again, the `.recieved.txt` file goes away, and the tests pass.

### 3. Let's increase the number of inputs - Add a variable for diamond cut



#### 3.a. Add all of the possible variations for diamond cut
### 4. Add a variable for diamond clarity
### 5. Add a variable for diamond color
### 6. Add a variable for the prices of other matching diamonds
## Conclusions and Questions