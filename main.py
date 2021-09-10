import requests  # api fetching
from bs4 import BeautifulSoup  # beautifulsoup
import smtplib  # email client

my_email = "USER_EMAIL"
my_password = "USER_PASSWORD"

url = "https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_2?dchild=1&keywords=phone&qid=1617621546&sr=8-2"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")


price = soup.find(id="priceblock_ourprice").get_text()
print(price)
price_without_currency = price.split("₹")[1]
price_as_float = float((price_without_currency.replace(",", "")))

title = soup.find(id="productTitle").get_text().strip()
print(title)
print(price)


BUY_PRICE = 7000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    message.encode("ascii", errors="ignore")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jasleen.e8943@cumail.in",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

# mam email
# snigdha.e8302@cumail.in
