import streamlit as st
import numpy as np
import pandas as pd
import random

origin_roll_list = ["TOP","JG","MID","ADC","SUP"]

st.title("LOL自動ロール振り分け")
st.write("""
        #### 6人以上入力するとランダムに5人選ばれます
        """)

players = st.text_area("1人ずつ改行して入力",height=150)

if st.button("振り分け"):
    try:  
        player_list = []
        player_list=players.splitlines()
        random.shuffle(player_list)

        n = len(player_list)
        roll_list = random.sample(origin_roll_list,n)
        roll_list = sorted(roll_list,key=origin_roll_list.index)
        col_list=st.columns(n)
        for i in range(n):
            col_list[i].metric(label=roll_list[i],value=player_list[i])
    except:
        player_list = []
        player_list=players.splitlines()
        random.shuffle(player_list)
        player_list = random.sample(player_list,5)
        n = len(player_list)
        roll_list = random.sample(origin_roll_list,n)
        roll_list = sorted(roll_list,key=origin_roll_list.index)
        col_list=st.columns(n)
        for i in range(n):
            col_list[i].metric(label=roll_list[i],value=player_list[i])
