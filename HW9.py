s='лениво дышит полдень мглистый, лениво катится река'
count={}
for key in s.split():
    count[key] = count.setdefault(key, 0) +1
print (count)