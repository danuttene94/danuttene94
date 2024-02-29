1. The purpose of test_positive_login.py is to save time, at each new release we must do a regression testing on the WEB interface of the switch. Better said, we have to log in using the switch IP, pass over a security warnining, check if the 5 main buttons work as expected.
I also added a search&screenshot at the end to search for the release we need.

2. The purpose of test_negative_log_in.py is an addition for the test_positive_login.py, just to check if you can log in the WEB interface of the switch with a wrong password.
