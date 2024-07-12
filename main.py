
import extra_streamlit_components as stx
import streamlit as st

# funkcja inicjalizująca cookie managera
def get_manager():
    return stx.CookieManager()

if 't' not in st.session_state:
    st.session_state['t'] = 0
#inicjalizacja cookie managera
cookie_manager = get_manager()
#pobranie wszystkich ciasteczek
cookies = cookie_manager.get_all()
#sprawdzenie czy jest ciasteczko o nazwie pomelojekebaba i przypisanie bool'a do zmiennej czyJestKuki
czyJestKuki = 'pomelojekebaba' in cookies

# Jeśli nie ma ciesteczka pomelojekebaba
if czyJestKuki is not True:
    # Wyświetl pole do wpisania hasła w sidebarze
    hasło = st.sidebar.text_input("Podaj hasło", type='password')
else: # jeśli jest ciasteczko pomelojekebaba
    # przypisz do zmiennej hasło wartość pomelojekebaba
    hasło = "pomelojekebaba"
    # wyświetl powiadomienie o zalogowaniu automatycznym
    #st.toast("Zalogowano automatycznie", icon="🍪")
    
if 'data' not in st.session_state:
    st.session_state['data'] = None
# Jeśli hasło to nie pomelojekebaba
if hasło != "pomelojekebaba" and czyJestKuki is not True:
    # Jeśli hasło nie jest puste
    if hasło != "": 
        # Wyświetl 50 razy 'nieprawidłowe hasło'
        for i in range(50):
            st.error("Nieprawidłowe hasło", icon="🔑")
            st.sidebar.error("Nieprawidłowe hasło", icon="🔑")
    else: # jeśli hasło jest puste
        # wyświetl 50 razy 'podaj hasło'
        for i in range(50): 
            st.info("Podaj hasło", icon="🧑") 
            st.sidebar.info("Podaj hasło", icon="🧑")
    st.stop() # jeśli hasło jest puste lub nie jest pomelojekebaba, zatrzymaj program
# Jeśli hasło to pomelojekebaba i nie ma ciasteczka pomelojekebaba
if hasło == "pomelojekebaba" and czyJestKuki is not True: 
    # Ustaw ciasteczko pomelojekebaba na pomelojekebaba
    cookie_manager.set('pomelojekebaba', 'pomelojekebaba')
    # Wyświetl powiadomienie o dodaniu ciasteczka
    st.toast("Dodano plik kuki", icon="🍪")
# Sprawdzanie czy akcja jest w obecnej sesji, jeśli nie, przypisywanie AAPL
if 'current_ticker' not in st.session_state:
    st.session_state.current_ticker = 'AAPL'
#Zaokrąglanie
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
#Pobiera dane z biblioteki yfinance i je kejszuje
źródło = st.sidebar.selectbox(label='Źródło danych', options=['yfinance', 'csv'])
miejsce_na_file_uploader2 = st.sidebar.empty()
miejsce_na_file_uploader = st.sidebar.empty()
if źródło == 'csv':
    plik_csv = miejsce_na_file_uploader.file_uploader("Wybierz plik csv", type=['csv']) # wyświetl przycisk do wybrania pliku csv

def get_stock(stock):
    if źródło == 'yfinance':
    # spróbuj
        try:
            # pobierz dane z biblioteki yfinance i przypisuje je do zmiennej data
            data = yfinance.download(tickers=ticker, period='5d', interval='30m', timeout=5)
            # jeśli data jest pusta
            if data.shape[0] == 0:
                # wyświetl error i zatrzymaj program
                st.error("Coś poszło nie tak")
                st.stop()
        except:
            pass
    elif źródło == 'csv':
        plik_csv =stock
        if plik_csv is not None:
            data = pd.read_csv(plik_csv)
            data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
            data = data.set_index('Datetime')
            data = data.drop(['Date', 'Time'], axis=1)
            #set st.session_state['ticker'] to filename without .csv
            st.session_state['current_ticker'] = plik_csv.name[:-7].upper()
            

            
        else:
            # wyświetl error i zatrzymaj program
            miejsce_na_file_uploader2.success("Wybierz plik csv")
            st.stop()
    st.session_state['data'] = data
    return data # zwróć data jeśli nie było błędu
ticker='AAPL' # przypisz AAPL do ticker na wszelki wypadek jakby się nie wczytał ticker z sidebaru
#wyświetla makapaka 
print("makapaka")
ticker = 'AAPL'
if źródło == 'csv':
    get_stock(plik_csv)
fromSidebar = sidebar(st.session_state['current_ticker'])
try: # próba przypisania zmiennych lokalnych do zrzutu z sidebaru z pliku sajdbar.py 
    ticker = fromSidebar['ticker']
    st.session_state['ticker'] = fromSidebar['ticker']
    doRSI = fromSidebar['doRSI']
    doATR = fromSidebar['doATR']
    doNATR = fromSidebar['doNATR']
    doAVGPRICE = fromSidebar['doAVGPRICE']
    doADX = fromSidebar['doADX']
    doMACD = fromSidebar['doMACD']
    doSMA = fromSidebar['doSMA']
    doBollingerBands = fromSidebar['doBollingerBands']
    atr_color = fromSidebar['atr_color']
    natr_color = fromSidebar['natr_color']
    rsi_color = fromSidebar['rsi_color']
    avgprice_color = fromSidebar['avgprice_color']
    sma_color = fromSidebar['sma_color']
    sma_color2 = fromSidebar['sma_color2']
    macd_color = fromSidebar['macd_color']
    adx_color = fromSidebar['ADX_color']
    bollinger_bands_color = fromSidebar['bollinger_color']
    podsumowanie = fromSidebar['podsumowanie']
    świeczuszki = fromSidebar['świeczuszki']
    doStochastic = fromSidebar['doStochastic']
    stochasticColor = fromSidebar['stochastic_color']
#    st.balloons()
except:
    # w przypadku błędu - zatrzymaj program
    #st.stop()
    pass