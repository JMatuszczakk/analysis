import talib as ta
import pandas as pd
import numpy as np
import streamlit as st





def Świeczuszki(świeczuszki, data, czy_pokazać = False):
    świeczki = pd.DataFrame(index=data.index)
    świeczki['Doji'] = ta.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Doji Star'] = ta.CDLDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Dragonfly Doji'] = ta.CDLDRAGONFLYDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Two Crows'] = ta.CDL2CROWS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Black Crows'] = ta.CDL3BLACKCROWS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Inside Up/Down'] = ta.CDL3INSIDE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Line Strike'] = ta.CDL3LINESTRIKE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Outside Up/Down'] = ta.CDL3OUTSIDE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Stars In The South'] = ta.CDL3STARSINSOUTH(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three White Soldiers'] = ta.CDL3WHITESOLDIERS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Abandoned Baby'] = ta.CDLABANDONEDBABY(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
    świeczki['Advance Block'] = ta.CDLADVANCEBLOCK(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Belt Hold'] = ta.CDLBELTHOLD(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Breakaway'] = ta.CDLBREAKAWAY(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Closing Marubozu'] = ta.CDLCLOSINGMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Concealing Baby Swallow'] = ta.CDLCONCEALBABYSWALL(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Engulfing'] = ta.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Evening Doji Star'] = ta.CDLEVENINGDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
    świeczki['Evening Star'] = ta.CDLEVENINGSTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
    świeczki['Gaps Side-by-Side White'] = ta.CDLGAPSIDESIDEWHITE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Gravestone Doji'] = ta.CDLGRAVESTONEDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Hammer'] = ta.CDLHAMMER(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Hanging Man'] = ta.CDLHANGINGMAN(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Harami'] = ta.CDLHARAMI(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Harami Cross'] = ta.CDLHARAMICROSS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['High-Wave'] = ta.CDLHIGHWAVE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Hikkake'] = ta.CDLHIKKAKE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Homing Pigeon'] = ta.CDLHOMINGPIGEON(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Identical Three Crows'] = ta.CDLIDENTICAL3CROWS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['In-Neck'] = ta.CDLINNECK(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Inverted Hammer'] = ta.CDLINVERTEDHAMMER(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Kicking'] = ta.CDLKICKING(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Kicking by Length'] = ta.CDLKICKINGBYLENGTH(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Ladder Bottom'] = ta.CDLLADDERBOTTOM(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Long Legged Doji'] = ta.CDLLONGLEGGEDDOJI(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Long Line'] = ta.CDLLONGLINE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Marubozu'] = ta.CDLMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Matching Low'] = ta.CDLMATCHINGLOW(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Mat Hold'] = ta.CDLMATHOLD(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  
    świeczki['Morning Doji Star'] = ta.CDLMORNINGDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  
    świeczki['Morning Star'] = ta.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  
    świeczki['On-Neck'] = ta.CDLONNECK(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Piercing'] = ta.CDLPIERCING(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Rickshaw Man'] = ta.CDLRICKSHAWMAN(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Rising/Falling Three Methods'] = ta.CDLRISEFALL3METHODS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Separating Lines'] = ta.CDLSEPARATINGLINES(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Shooting Star'] = ta.CDLSHOOTINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Short Line'] = ta.CDLSHORTLINE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Spinning Top'] = ta.CDLSPINNINGTOP(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Stalled Pattern'] = ta.CDLSTALLEDPATTERN(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Stick Sandwich'] = ta.CDLSTICKSANDWICH(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Takuri'] = ta.CDLTAKURI(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Tasuki Gap'] = ta.CDLTASUKIGAP(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Thrusting'] = ta.CDLTHRUSTING(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Tristar'] = ta.CDLTRISTAR(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Unique 3 River'] = ta.CDLUNIQUE3RIVER(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Upside Gap Two Crows'] = ta.CDLUPSIDEGAP2CROWS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Upside/Downside Gap Three Methods'] = ta.CDLXSIDEGAP3METHODS(data['Open'], data['High'], data['Low'], data['Close'])    
    print(świeczki)
    
    lista = []
    wykryte2 = []
    if czy_pokazać:
        st.dataframe(świeczki.tail())
    st.sidebar.subheader("Świeczki które są: ")
    for i in świeczki.columns:
        for y in świeczki[i][-4:]:
            if y != 0:
                lista.append(i)
                wykryte2.append((i, y))
                

    
    na_plus = 0
    na_minus = 0
    na_odwrócenie = 0
    kontynuacja = 0


    wykryte = []



    if 'Doji' in lista:
        st.sidebar.write(":green[Doji] - odwórcenie ceny")
        na_odwrócenie += 1
        wykryte.append(('Doji', świeczki['Doji'][-1]))
    if 'Doji Star' in lista:
        st.sidebar.write(":green[Doji Star] - odwórcenie ceny")
        na_odwrócenie += 1
        wykryte.append(('Doji Star', świeczki['Doji Star'][-1]))
    if 'Dragonfly Doji' in lista:
        st.sidebar.write(":green[Dragonfly Doji] - odwórcenie ceny")
        na_odwrócenie += 1
        wykryte.append(('Dragonfly Doji', świeczki['Dragonfly Doji'][-1]))
    if 'Two Crows' in lista:
        st.sidebar.write(":green[Two Crows] - odwórcenie ceny")
        na_minus += 1
        wykryte.append(('Two Crows', świeczki['Two Crows'][-1]))
    if 'Three Black Crows' in lista:
        st.sidebar.write(":green[Three Black Crows] - mocny sygnał spadkowy zazwyczaj się nie myli")
        na_minus += 1
        wykryte.append(('Three Black Crows', świeczki['Three Black Crows'][-1]))
    # if 'Three Inside Up/Down' in lista:
    #     st.sidebar.write(":green[Three Inside Up/Down - sugeruje spadek]")
    #     na_minus += 1
    if 'Three Line Strike' in lista:
        st.sidebar.write(":green[Three Line Strike] - sygnał wzrostowy po uprzednich spadkach")
        na_minus += 1
        na_odwrócenie += 1
        wykryte.append(('Three Line Strike', świeczki['Three Line Strike'][-1]))
    # if 'Three Outside Up/Down' in lista:
    #     st.sidebar.write(":green[Three Outside Up/Down - na odwrócenie]")
    #     na_odwrócenie += 1

    if 'Three Stars In The South' in lista:
        st.sidebar.write(":green[Three Stars In The South] - sygnał koniec trendu bessy")
        na_odwrócenie += 1
        na_plus += 1
        wykryte.append(('Three Stars In The South', świeczki['Three Stars In The South'][-1]))
    if 'Three White Soldiers' in lista:
        st.sidebar.write(":green[Three White Soldiers] - przewiduje odwrócenie się rynku spadkowego w stronę wzrostową")
        na_plus += 1
        na_odwrócenie += 1
        wykryte.append(('Three White Soldiers', świeczki['Three White Soldiers'][-1]))