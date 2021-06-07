#!/usr/bin/env python
# -*- coding: utf-8 -*

kekka1 = 5 + 5   # 5+5 の結果をkekka1にコピー 
print(kekka1)    # kekka1 を表示

for i in range(6):          # 6回繰り返す
    kekka1 = kekka1 + 10        # kekka1 + 10の結果をkekka1にコピー 
    print(kekka1)               # kekka1を表示

if kekka1 == 100:
    print("おわり")

if kekka1 < 100:
    print("100に足りていない")