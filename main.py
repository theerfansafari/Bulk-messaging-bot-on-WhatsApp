from selenium import webdriver
from time import sleep

# شماره‌های واتساپ مورد نظر را در لیست زیر قرار دهید
numbers = ["+1234567890", "+9876543210"]  # مثال: ["+989123456789", "+989098765432"]

# پیام مورد نظر را در متغیر زیر قرار دهید
message = "سلام، این یک پیام تستی از طریق پایتون است."

# مسیر فایل chromedriver.exe را تعیین کنید
driver_path = "مسیر_فایل_chromedriver.exe"

# مرورگر Chrome را با کتابخانه Selenium باز کنید
driver = webdriver.Chrome(executable_path=driver_path)

# صفحه وب واتساپ را باز کنید
driver.get("https://web.whatsapp.com/")
input("لطفاً بعد از ورود به واتساپ، Enter را بزنید.")

# تابعی برای ارسال پیام به شماره‌های مورد نظر
def send_message(numbers, message):
    for number in numbers:
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(url)
        sleep(5)  # یک مدت زمان مناسب برای بارگذاری صفحه
        button = driver.find_element_by_xpath("//button[@class='_4sWnG']")
        button.click()
        sleep(5)  # یک مدت زمان مناسب برای ارسال پیام

# پیام را به شماره‌های مورد نظر ارسال کنید
send_message(numbers, message)

# مرورگر را ببندید
driver.quit()
