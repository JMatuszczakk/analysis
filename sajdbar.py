import streamlit as st
import yfinance
import pytz
from datetime import datetime


def sidebar(ticker):
    try:    
        


        def truncate(n, decimals=0):
            multiplier = 10 ** decimals
            return int(n * multiplier) / multiplier
        #Pobiera dane z biblioteki yfinance i je kejszuje
        def get_stock(stock):
            if st.session_state['data'] is not None:
                data = st.session_state['data']
                st.session_state['ticker'] = ' '
                st.session_state['current_ticker'] = ' '
            else:
                try:
                    data = yfinance.download(tickers=ticker, period='7d', interval='30m')
                    if data.shape[0] == 0:
                        st.error("Coś poszło nie tak")
                        st.stop()
                except:
                    st.toast("Gówno ")
            return data

        with st.sidebar:
            with st.form(key='my_form'):
                #Poniżej znajduje się kod który wyświetl godzinę z strefy czasowej GMT-5
                tz = pytz.timezone('US/Eastern')
                st.title(f"Godzina w GTM -5 to :green[{datetime.now(tz).strftime('%H:%M')}]")
                st.subheader("Godzina otwarcia giełdy to :green[15:30] czasu polskiego")
                st.subheader("Godzina zamknięcia giełdy to :red[22:00] czasu polskiego")
                st.subheader("Godzina otwarcia giełdy polskiej to :green[9:00] czasu polskiego")
                st.subheader("Godzina zamknięcia giełdy polskiej to :red[17:00] czasu polskiego")
    except: pass