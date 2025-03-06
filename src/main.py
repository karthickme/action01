# src/get_num_square.py
import os

# get the input and convert it to int
num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))
else:
    num = 1

# to set output, print to shell in following syntax
print(f"::set-output name=num_squared::{num ** 2}")
print("**"*50)
print("num", os.environ.get("INPUT_NUM"))
print("to", os.environ.get("INPUT_TO_ID"))
print("cc", os.environ.get("INPUT_CC_ID"))
print("starttime", os.environ.get("INPUT_START_TIME"))
print("endtime", os.environ.get("INPUT_END_TIME"))
print("content", os.environ.get("INPUT_CONTENT"))
print("failure", os.environ.get("INPUT_FAILURE"))
