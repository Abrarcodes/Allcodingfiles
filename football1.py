team1=input("enter the name of the home team")
team2=input("enter the name of the away team 2")
players1=["Marc-André ter Stegen",
"Sergi Roberto",
"Andreas Christensen",
"Ronald Araújo",
"Alejandro Balde",
"Frenkie de Jong",
"Pedri",
"Gavi",
"Robert Lewandowski",
"Raphinha",
"Ferran Torres"]
for i in players1:
    print(i)
players2=["Thibaut Courtois",
"Dani Carvajal",
"David Alaba",
"Éder Militão",
"Ferland Mendy",
"Luka Modrić",
"Toni Kroos",
"Federico Valverde",
"Vinícius Júnior",
"Rodrygo",
"Karim Benzema"]   
for k in players2:
    print(k)
    
print("MATCH STARTS NOW")
score_half_time_fcb=int(input("enter the score of the home team"))
score_half_time_rmfc=int(input("enter the score of the away team"))
score_half_time=print(score_half_time_fcb,"-", score_half_time_rmfc)
    
score_full_time_fcb=int(input("enter the score of the home team"))
score_full_time_rmfc=int(input("enter the score of the away team"))
score_full_time=print(score_full_time_fcb,"-", score_full_time_rmfc)

result=score_full_time

if score_full_time_fcb>score_full_time_rmfc:
    print(team1 ,"WON THE MATCH")
else:
    print(team2, "WON THE MATCH")
    
print("------------------------------------------------------------------")
