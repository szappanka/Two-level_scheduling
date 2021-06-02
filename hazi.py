# sorba rakja a tömb elemeit beérkezés szerint

def sequence(temp):
    for x in range(0, len(temp)):
        for y in range(0, len(temp)-1):
            if temp[y][2]>temp[y+1][2]:
                help = temp[y]
                temp[y] = temp[y+1]
                temp[y+1] = help

def main():
    #beolvasás

    vegleges = []
    tasks = []
    meo = []

    for x in range(0, 10):
        try:
            
            task = input()
            if task == "":
                break
            task = task.split(",")
            
        except EOFError:
            break

        tasks.append(task)
        oneMeo = task[0]+","+task[2]+","+task[3]
        meo.append(oneMeo.split(","))

    for oneTask in tasks:
        oneTask[1] = int(oneTask[1])
        oneTask[2] = int(oneTask[2])
        oneTask[3] = int(oneTask[3])
        
    #szétválogatás és rendezés beérkezés szerint

    sjf = []
    rr = []

    for y in tasks:
        if y[1]==0:
            rr.append(y)
        else:
            sjf.append(y)
    
    sequence(rr)  #sorba rendezem beérkezés szerint a taszkokat
    sequence(sjf)

    #sjf taszkok beillesztése

    sjf_now = []    # adott időpillanatban várakozó taszkok löketidő sorrendjében
    sjf_kesz = 0    # sikeresen beillesztett sjf taszkok száma
    time = 1        # adott időpillanat(időegység)
    actual=""       # aktuális taszk, ami épp hozzáadás közben van

    while(sjf_kesz != len(sjf)):
        for z in range(0, len(sjf)):
            if sjf[z][2]==time-1:
                sjf_now.append(sjf[z])
            
        for x in range(0, len(sjf_now)):  # sorba rendezés
            for y in range(0, len(sjf_now)-1):
                if sjf_now[y][3]>sjf_now[y+1][3]:
                    help = sjf_now[y]
                    sjf_now[y] = sjf_now[y+1]
                    sjf_now[y+1] = help    

        if actual!="" and actual[3]!=0:
            actual[3] -= 1
            vegleges.append(actual[0])
            if actual[3]==0:
                sjf_kesz += 1
     
        elif sjf_now==[]:
            vegleges.append(0)
            

        elif sjf_now!=[]:
            actual = sjf_now[0]
            sjf_now.pop(0)
            actual[3] -= 1
            vegleges.append(actual[0])
            if actual[3]==0:
                sjf_kesz += 1

        time+=1
    
    #rr taskok beillesztése
    
    rr_now = []    # adott időpillanatban várakozó taszkok
    rr_kesz = 0    # sikeresen beillesztett rr taszkok száma
    time = 1        # adott időpillanat(időegység)
    lepett = False

    if vegleges == []:
        vegleges.append(0)
        vegleges.append(0)

    while(rr_kesz != len(rr)):
        
        if not lepett:
            for z in range(0, len(rr)):
                if rr[z][2]==time-1:
                    rr_now.append(rr[z])
        lepett = False

        if len(vegleges)==time:
            vegleges.append(0)

        if vegleges[time-1]==0 and vegleges[time]==0:
            if rr_now!=[] and rr_now[0][3]==1:
                vegleges[time-1]=rr_now[0][0]
                del rr_now[0]
                rr_kesz+=1
            elif rr_now!=[] and rr_now[0][3]>1:
                vegleges[time-1]=rr_now[0][0]
                rr_now[0][3]-=1
                time+=1
                vegleges.append(0)
                for z in range(0, len(rr)):
                    if rr[z][2]==time-1:
                        rr_now.append(rr[z])
                vegleges[time-1]=rr_now[0][0]
                rr_now[0][3]-=1

                if rr_now[0][3]==0:
                    del rr_now[0]
                    rr_kesz+=1
                else:
                    time += 1
                    for z in range(0, len(rr)):
                        if rr[z][2]==time-1:
                            rr_now.append(rr[z])
                    rr_now.append(rr_now[0])
                    lepett = True
                    del rr_now[0]

        elif vegleges[time-1]==0 and vegleges[time]!=0 and rr_now!=[]:
            if rr_now[0][3]==1:
                vegleges[time-1]=rr_now[0][0]
                del rr_now[0]
                rr_kesz+=1
            elif rr_now[0][3]>1:
                vegleges[time-1]=rr_now[0][0]
                rr_now[0][3]-=1
                time+=1
                for z in range(0, len(rr)):
                        if rr[z][2]==time-1:
                            rr_now.append(rr[z])

                rr_now.append(rr_now[0])
                lepett = True
                del rr_now[0]

        if not lepett:
            time+=1

    while vegleges[-1]==0:
        del vegleges[-1]

    # megfelelő adatok kiírása

    mo1 = []
    mo2 = []

    for x in range(0, len(vegleges)):
        if vegleges[x]!=0:
            if mo1 == []:
                mo1.append(vegleges[x])
            elif mo1[-1] != vegleges[x]:
                mo1.append(vegleges[x])
                
    print("".join(mo1))

    for x in range(0, len(meo)):
        for y in range(0, len(meo)-1):
            if int(meo[y][1])>int(meo[y+1][1]):
                help = meo[y]
                meo[y] = meo[y+1]
                meo[y+1] = help

    for t in meo:
        for v in range(len(vegleges)-1, -1,-1):
            if vegleges[v]==t[0]:
                break
        szam = v+1-int(t[1])-int(t[2])
        mo2.append(str(t[0])+":"+str(szam))

    print(",".join(mo2))
   
main()
