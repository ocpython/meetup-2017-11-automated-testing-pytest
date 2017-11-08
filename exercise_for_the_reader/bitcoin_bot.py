import requests


class BitcoinBot:
    
    def __init__(self):
        self.current_price = self.get_latest_price()
        self.yesterday_price = self.get_historical_price()

    def get_latest_price(self):
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        r.raise_for_status()

        return r.json()['bpi']['USD']['rate_float']

    def get_historical_price(self):
        r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday')
        r.raise_for_status()

        return r.json()['bpi']
    
    def price_alert(self):
        current_price = self.get_latest_price()
        yesterday_closing = self.get_historical_price()
        
        if current_price >= yesterday_closing * 1.10:
            print('SELL ALL BITCOINS')
            
        if current_price <= yesterday_closing * 0.90:
            print('BUY ALL BITCOINS')
