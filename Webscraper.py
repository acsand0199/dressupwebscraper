from bs4 import BeautifulSoup
import requests

def main():
    site = "https://shopdressup.com/collections/dresses"
    r = requests.get(site) #Send a HTTP request to the specified URL and save the response from server in r
    
    if r.status_code == 200: # Check if the request was successful
        soup = BeautifulSoup(r.content, 'html5lib') #creates a beautiful soup object named soup.  r.content retrieves the raw HTML content.  html5lib is the parser to parse the data.

        find_dress_price = soup.find_all('div', class_='grid-product__price') #.find_all method searches the HTML content for all <div> elements that have the CSS class attribute set to 'dress-price'.  This creates a list

        for dress_prices in find_dress_price:
            price_text = dress_prices.get_text() # Extract the text content of the element

            price = ''.join(filter(str.isdigit, price_text)) #uses the filter function to iterate over each character in price_text. It checks whether each character is a digit using the str.isdigit function. The filter function returns an iterator of characters that are digits.
            #''.join(...): The join method is used to concatenate all the characters returned by the filter function into a single string.

            price_float = float(price) / 100 # dividing by 100 converts a value for instance of 1200 to 12.00 to get correct values

            if price_float < 30:
                print("Good deal")
            else:
                print("Not a good deal.")
    else:
        print("Failed to load the page.")




if __name__ == "__main__":
    main()
