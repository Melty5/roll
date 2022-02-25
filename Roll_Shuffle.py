import streamlit as st
import numpy as np
import pandas as pd
import random

roll_list = ["TOP","JG","MID","ADC","SUP"]

st.title("LOL自動ロール振り分け")

players = st.text_area("1人ずつ改行してプレイヤー入力しやがれ",height=140)

if st.button("振り分け"):  
    player_list = []
    player_list=players.splitlines()
    random.shuffle(player_list)

    n = len(player_list)
    roll_list = random.sample(roll_list,n)
    col_list=st.columns(n)
    for i in range(n):
        col_list[i].metric(label=roll_list[i],value=player_list[i])
            
