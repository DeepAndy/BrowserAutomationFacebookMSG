from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC

#Todo implement timeout exception
# browser.page_source
#init the webdriver from a folder in this case Chrome
class Facebook:
    def __init__(self, email, password):

        option = webdriver.ChromeOptions()
        option.add_argument('--disable-notifications')
        path = (r'C:\Users\elvir\Documents\123\Pythonagain\Selenium\chromedriver.exe')
        self.browser = webdriver.Chrome(path, chrome_options=option)
        #This has to be changed to your location of the chromedriver!!!
        #Look at the comment on the right-up side !
        self.email = email
        self.password = password
        ''' Initializes the email and the password, browser and it's arguments ,
        can add --incognito, notifications disabled because they can
        mess with the software, (script unable to execute
        when chrome-notification popup (displays a layer)'''

    def getpage(self):
        self.browser.get('https://www.facebook.com')
        '''Only useful for this page ,
        static / hardcoded for now but made it a function for simpicity '''

    def login(self):
        self.browser.find_element_by_xpath('''//*[@id="email"]''').send_keys(self.email)
        self.browser.find_element_by_xpath('''//*[@id="pass"]''').send_keys(self.password)
        self.browser.find_element_by_xpath('''//*[@id="loginbutton"]''').click()
        'Types in the email/username and password then clicks the sumbit button to post the data.'

    def findfriends(self, name):
        # 4everalone
        '''Once we do all of the above
        we'rere gonna wait 5sec no matter what *implicit*'''
        self.browser.implicitly_wait(5) #
        # Sometimes facebook chat is not openned by default,
        # this ensures that it will be opened otherways it throws an error that's handeled
        try:
            self.browser.find_element_by_xpath('''//*[@id="fbDockChatBuddylistNub"]/a/i''')
        except:
            print('An Error occurred.')
        friends = self.browser.find_elements_by_xpath('''//*[@id]/div/div[2]/span/label/input''')
        for i in friends:
            if i.is_displayed():
                i.send_keys(str(name))
            else:
                continue
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath('''//*[@id]/a/div/div/div/div[contains(text(),"{}")]'''.format(name)).click()
        self.browser.implicitly_wait(5)
    def sendmessage(self, text):
        #Very unreliable way of sending a message *no verification of username
        #Just sends the message to the opened chat-box.(>findfriends)
        joke = self.browser.find_element_by_xpath('''//*[@id]/div[5]/div/div/div/span/div/div[2]/div''')
        joke.send_keys(str(text))
        joke.send_keys(Keys.RETURN)
        joke.click()




def main():
    email = str(input('Type in your username or email for Facebook : '))

    ime = input(str('Type in your friends Name and Surname: '))
    poruka = input(str('Type in the message you want to send : '))
    password = 'Elvirpatka1337Tiberz1144'
    user = Facebook(email, password)
    user.getpage()
    user.login()
    user.findfriends(ime)
    user.sendmessage(poruka)
    input('Press Enter to continue')



if __name__ == '__main__':
    main()
