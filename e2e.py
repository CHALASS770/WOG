from selenium import webdriver
from time import sleep

print("test")


def test_score_webservice():
    print(1)


    Url = "http://127.0.0.1:8777"
    print(3)
    driver = webdriver.Firefox(executable_path='../WOG/geckodriver')
    print(2)

    driver.get(Url)
    sleep(3)
    res = driver.find_element_by_id("score")
    test = int(res.text)
    print(4)

    if test >= 1 and test <= 1000:
        print("True")
        return True
    else:
        print("False")
        return False
def main_test() :

        test = test_score_webservice()
        print(0)


main_test()
