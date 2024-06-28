x = {"name": "Somkiat",
     "Age":35,
     "Wt":75,
     "H":175
     
     }
print(x)
print("สวัสดีครับคุณ %s" % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["Age"], x["Age"]))
print("นํ้าหนัก %d ส่วนสูง %d" % (x["Wt"], x["H"]))