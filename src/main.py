from loguru import logger
import os
import currency_conv_helpers as curr_helpers


def main():
    try:

        
        API_KEY = os.getenv('APIKEY')

        if not API_KEY:
            raise Exception("Could not read API key from env vars.")
        
        input_results = curr_helpers.get_user_input()

        if isinstance(input_results, Exception):
            raise input_results

        from_currency, to_currency, amount_to_conv  = input_results

        logger.info(f"from_currency: {from_currency}, to_currency: {to_currency}, amount_to_conv: {amount_to_conv}")

        api_results = curr_helpers.currency_conv(from_currency, to_currency, amount_to_conv, API_KEY)
        
        if isinstance(api_results, Exception):
            raise api_results
        
        logger.info(api_results)


    except Exception as e:
        logger.error(f"Error: {e}")
        raise
if __name__ == "__main__":
    main()
