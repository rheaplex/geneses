import BeautifulSoup as bs
import urllib2

BASE_URL = 'http://coinmarketcap.com'

# BitShares???
# stellar?

GENESIS_PATHS = ['block-height/1',
                 '?hi=0',
                 'block/0'
                 'block.dws?1.htm',
                 'tx.dws?1.htm',
                 'block/info/1']

source = open('index.html').read()
soup = bs.BeautifulSoup(source)

currencies = soup.findAll('td', {'class': 'no-wrap currency-name'})
currencies_links = [BASE_URL + currency.find('a')['href']
                    for currency in currencies]

def fetchExplorerLink (page_url):
    response = urllib2.urlopen(page_url)
    source = response.read()
    soup = bs.BeautifulSoup(source)
    a_text = soup.find(text='Explorer')
    try:
        href = a_text.parent['href']
    except AttributeError:
        href = None
    return href

explorer_links = [fetchExplorerLink(page_url) for page_url in currencies_links]

def fetchGenesisPage (page_url):
    genesis = None
    for genesis_path in GENESIS_PATHS:
        url = page_url + genesis_path
        
    return genesis
