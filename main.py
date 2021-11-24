import requests
import json

headers = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "access-control-allow-credentials": "true"
}


def data_shoes(money):
    s = requests.Session()
    response = s.get(url="https://prod.olympus.zappos.com/Search/zso/men-sneakers-athletic-shoes/CK_XARC81wHAAQLiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page=2&s=isNew%2Fdesc%2FgoLiveDate%2Fdesc%2FrecentSalesStyle%2Fdesc%2F", headers=headers)
    data = response.json()
    pagination_count = data.get("pageCount")
    result_data = []
    items_urls = []
    for page_count in range(1, pagination_count + 1):
        url = f"https://prod.olympus.zappos.com/Search/zso/men-shoes/CK_XAcABAuICAgEY.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page={page_count}&s=percentOff%2Fdesc%2F"
        r = s.get(url=url, headers=headers)
        data = r.json()
        products = data.get("results")
        for product in products:
            product_result = data.get("results")
            if products != None and product.get("productUrl") not in items_urls and float(product.get('price').replace("$","")) <=float("{}".format(money))  :
                items_urls.append(product.get("productUrl"))
                result_data.append(
                   {
                        "title": product.get("brandName"),
                        "link": f'https://www.6pm.com{product.get("productUrl")}',
                        "price_base": product.get("originalPrice"),
                        "price_sale": product.get("price"),
                        "discount_percent": product.get("percentOff"),
                        "onhand" : product.get("onHand"),
                        "img" : product.get("thumbnailImageUrl")
                    }
                    )
        print(f"{page_count}/{pagination_count}")
    with open("result_data_shoes.json", "w") as f:
        json.dump(result_data, f, indent=4, ensure_ascii=False)


def data_bags(money):
    s = requests.Session()
    response = s.get(url="https://prod.olympus.zappos.com/Search/zso/men-bags/COjWAcABAuICAgEY.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page=2&s=percentOff%2Fdesc%2F", headers=headers)
    data = response.json()
    pagination_count = data.get("pageCount")
    result_data = []
    items_urls = []
    for page_count in range(1, pagination_count + 1):
        url = f"https://prod.olympus.zappos.com/Search/zso/men-bags/COjWAcABAuICAgEY.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page={page_count}&s=percentOff%2Fdesc%2F"
        r = s.get(url=url, headers=headers)
        data = r.json()
        products = data.get("results")
        for product in products:
            product_result = data.get("results")
            if products != None and product.get("productUrl") not in items_urls and float(product.get('price').replace("$","")) <=float("{}".format(money))  :
                items_urls.append(product.get("productUrl"))
                result_data.append(
                   {
                        "title": product.get("brandName"),
                        "link": f'https://www.6pm.com{product.get("productUrl")}',
                        "price_base": product.get("originalPrice"),
                        "price_sale": product.get("price"),
                        "discount_percent": product.get("percentOff"),
                        "onhand" : product.get("onHand"),
                        "img" : product.get("thumbnailImageUrl")
                    }
        			)
        print(f"{page_count}/{pagination_count}")
    with open("result_data_bags.json", "w") as f:
        json.dump(result_data, f, indent=4, ensure_ascii=False)


def data_shoes_women(money):
    s = requests.Session()
    response = s.get(url="https://prod.olympus.zappos.com/Search/zso/women-sneakers-athletic-shoes/CK_XARC81wHAAQHiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%2C%22enableExplicitSizeFilterPreference%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page=2&s=percentOff%2Fdesc%2F", headers=headers)
    data = response.json()
    pagination_count = data.get("pageCount")
    result_data = []
    items_urls = []
    for page_count in range(1, pagination_count + 1):
        url = f"https://prod.olympus.zappos.com/Search/zso/women-sneakers-athletic-shoes/CK_XARC81wHAAQHiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%2C%22enableExplicitSizeFilterPreference%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page={page_count}&s=percentOff%2Fdesc%2F"
        r = s.get(url=url, headers=headers)
        data = r.json()
        products = data.get("results")
        for product in products:
            product_result = data.get("results")
            if products != None and product.get("productUrl") not in items_urls and float(product.get('price').replace("$","")) <=float("{}".format(money))  :
                items_urls.append(product.get("productUrl"))
                result_data.append(
                   {
                        "title": product.get("brandName"),
                        "link": f'https://www.6pm.com{product.get("productUrl")}',
                        "price_base": product.get("originalPrice"),
                        "price_sale": product.get("price"),
                        "discount_percent": product.get("percentOff"),
                        "onhand" : product.get("onHand"),
                        "img" : product.get("thumbnailImageUrl")
                    }
                    )
        print(f"{page_count}/{pagination_count}")
    with open("result_data_shoes_women.json", "w") as f:
        json.dump(result_data, f, indent=4, ensure_ascii=False)


def data_bags_women(money):
    s = requests.Session()
    response = s.get(url="https://prod.olympus.zappos.com/Search/zso/women-handbags/COjWARCS1wHAAQHiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%2C%22enableExplicitSizeFilterPreference%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page=2&s=percentOff%2Fdesc%2F", headers=headers)
    data = response.json()
    pagination_count = data.get("pageCount")
    result_data = []
    items_urls = []
    for page_count in range(1, pagination_count + 1):
        url = f"https://prod.olympus.zappos.com/Search/zso/women-handbags/COjWARCS1wHAAQHiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22brandRedirect%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22brandRedirectWithResults%22%2C%22onHand%22%2C%22imageMap%22%2C%22enableExplicitSizeFilterPreference%22%5D&relativeUrls=true&siteId=2&subsiteId=12&page={page_count}&s=percentOff%2Fdesc%2F"
        r = s.get(url=url, headers=headers)
        data = r.json()
        products = data.get("results")
        for product in products:
            product_result = data.get("results")
            if products != None and product.get("productUrl") not in items_urls and float(product.get('price').replace("$","")) <=float("{}".format(money))  :
                items_urls.append(product.get("productUrl"))
                result_data.append(
                   {
                        "title": product.get("brandName"),
                        "link": f'https://www.6pm.com{product.get("productUrl")}',
                        "price_base": product.get("originalPrice"),
                        "price_sale": product.get("price"),
                        "discount_percent": product.get("percentOff"),
                        "onhand" : product.get("onHand"),
                        "img" : product.get("thumbnailImageUrl")
                    }
                    )
        print(f"{page_count}/{pagination_count}")
    with open("result_data_bags_women.json", "w") as f:
        json.dump(result_data, f, indent=4, ensure_ascii=False)


if __name__=="__main__":
    main()