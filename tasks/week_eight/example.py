import pprint


### small json example
import json
import requests

def requrests_test():
    test = {
        "name": "John",
        "age": 30,
        "city": ["New York", "London", "Berlin"]
    }

    pprint.pprint(test)
    pprint.pprint(json.dumps(test))
    input("Press enter to continue...")


    ### API with requests

    import requests

    # Get the data from the API
    response = requests.get("https://api.github.com/events")

    if response.status_code == 200:
        # Print the response text
        pprint.pprint(response.text)
        input("Press enter to continue...")


    json_data = response.json()
    pprint.pprint(json_data)
    input("Press enter to continue...")

    pprint.pprint(json.dumps(json_data))


### Scrapy
def scrapy_test():
    import scrapy

    data = requests.get("https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-501010")

    pprint.pprint(data.text)
    input("Press enter to continue...")

    ## load the data into a scrapy selector
    sel = scrapy.Selector(text=data.text)
    response = sel.xpath("//html/body/div[1]/div/div/div[2]/div/main/div[3]/div[3]/div/*").getall()
    response = sel.xpath("//html/body/div[1]/div/div/div[2]/div/main/div[3]/div[3]/div/div/div/table/tbody/*").getall()

    pprint.pprint(len(response))

    for row in response:
        row_value = scrapy.Selector(text=row).xpath("//td/text()").getall()
        print(row_value[2])
        input("Press enter to continue...")


if __name__ == "__main__":
    # requrests_test()
    scrapy_test()