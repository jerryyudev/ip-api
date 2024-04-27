import webbrowser

def search_flights(origin, destination, departure_date, return_date, adult_count, child_count, infant_count):
    url = f"https://www.bing.com/travel/flight-search?q=flights+from+{origin}-{destination}&src={origin}&des={destination}&rdate={return_date}&isr=1&ddate={departure_date}&cls=0&adult={adult_count}&child={child_count}&infant={infant_count}&form=FLAFLI&entrypoint=UNKHUB"
    webbrowser.open(url)
    print("正在打开网站，请稍候...")

def main():
    origin = input("请输入出发地：")
    destination = input("请输入目的地：")
    departure_date = input("请输入出发日期（YYYY-MM-DD）：")
    return_date = input("请输入返回日期（YYYY-MM-DD）：")
    adult_count = input("请输入成人数量：")
    child_count = input("请输入儿童数量：")
    infant_count = input("请输入婴儿数量：")
    
    search_flights(origin, destination, departure_date, return_date, adult_count, child_count, infant_count)

if __name__ == "__main__":
    main()
