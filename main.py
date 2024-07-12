
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
