from selenium import webdriver

class Parser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_something()

    def go_to_something(self):
        self.driver.get("https://coderlessons.com/articles")
        posts = self.driver.find_elements_by_class_name("post-title")

        for elem in posts:
            print(elem.find_element_by_tag_name("a").get_attribute('href'))


def main():
    driver = webdriver.Chrome()
    p = Parser(driver, "python")
    p.parse()

if __name__ == "__main__":
    main()

