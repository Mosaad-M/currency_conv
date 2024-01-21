
import requests
from loguru import logger


def get_user_input() -> tuple | Exception :
    from_currency: str = input("What's the 3 letter code for the currency you wish to convert from? ").upper()

    if ( (not from_currency) or (not len(from_currency) == 3) or (not isinstance(from_currency, str)) ):
        return Exception("Invalid input for the currency to convert from.")
        
    
    to_currency: str = input("What's the 3 letter code for the currency you wish to convert to? ").upper()

    if ( (not to_currency) or (not len(to_currency) == 3) or (not isinstance(to_currency, str)) ):
        return Exception("Invalid input for the currency to convert to.")
    

    amount_to_conv_str: str  = input("How much would you like to convert? ")

    if ( (not amount_to_conv_str) or  (not amount_to_conv_str.isdigit()) ):
        return Exception("Invalid input for the the amount to convert.Input has to be numeric.")
    
    else :
        return (from_currency, to_currency, amount_to_conv_str)



def currency_conv(from_curr, to_curr, amount_to_conv, api_key) -> str | Exception: 

    base_url_string: str= "https://api.getgeoapi.com/v2/currency/convert"
    params = {"api_key": api_key,"from": from_curr.upper(),"to": to_curr.upper(),"amount": amount_to_conv,"format": "json"}

    resp = requests.get(base_url_string, params)

    if resp.status_code != 200:
        logger.info(resp)
        return Exception(f"Request to {base_url_string} was not successful. Status code: {resp.status_code}  Message: {resp.json().get('error').get('message') }")
    
    json_results = resp.json()

    rate_decimal = json_results.get('rates').get(to_curr.upper()).get('rate')

    converted_amount = json_results.get('rates').get(to_curr.upper()).get('rate_for_amount')

    message: str = f"With a rate of {rate_decimal} , converting {amount_to_conv} {from_curr} would result in {converted_amount} {to_curr} ."

    return message

