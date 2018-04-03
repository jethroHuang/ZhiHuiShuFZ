from selenium import webdriver
import time
from PIL import Image


im = Image.open("请勿删除此文件")
im.show()

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
browser = webdriver.Chrome(chrome_options=options)

browser.get("http://zhihuishu.com")
print("====欢迎使用智慧树辅助程序====")
r = input("\n登陆您的账号,打开课程播放页面并开始播放后,关闭其他所有网页,点此窗口按回车后程序开始运行")
windows = browser.window_handles
browser.switch_to_window(windows[-1])
print("\n智慧树辅助程序开始运行")
# 切换到最新打开的页面

# 进入下一课
def click_next():
    browser.execute_script('document.getElementsByClassName("controlsBar")[0].style.display="block";')
    time.sleep(2)
    nextButton = browser.find_element_by_xpath('//div[@id="nextBtn"]')
    nextButton.click()


def check_end():
    playBtn = browser.find_element_by_id("playButton")
    if "playButton" in playBtn.get_attribute("class"):
        return True


def close_tanti():
    try:
        nextButton = browser.find_element_by_xpath('//a[@class="popbtn_cancel"]')
        time.sleep(3)
        nextButton.click()
        return True
    except:
        return False


if __name__ == '__main__':
    while True:
        try:
            if check_end():
                if close_tanti():
                    print(time.strftime("[%H:%M] ")+"已自动关闭弹题")
                    continue
                click_next()
                print(time.strftime("[%H:%M] ")+"已自动进入下一集")
                print("======辅助程序持续运行中======")
        except:
            time.sleep(5)
        time.sleep(5)
