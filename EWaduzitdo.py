import os
import sys

########################################################################
#   Original Implementation by Larry Kheriaty in 1978                  #
#   JavaScript and DHTML in 2006 by Hans Franke                        #
#   Written by Petar Jovanovic 2024                                    #
#   Special thanks to Tyler Zahnke                                     #
########################################################################

def Cls():
    os.system('cls');

def PrChar(c):
    print(c,end='')

def PrNL():
    print()

def GetChar():
    str = input('?');
    ch=str[0];
    return ch;

def GetString():
    str = input('?');
    return str;

def Waduzitdo(source):
    Loc=0;
    End = len(source)-1;
    CBUF= " ";
    line=1
    VAcc = [0,0,0,0,0,0,0,0,0,0];
    Acc=" ";
    Flg=" ";
    Last=0;

    while(Loc<End):
        CBUF=source[Loc]
        if(CBUF>"*"):
            if CBUF=="Y" or CBUF=="N" :
                if(CBUF!=Flg):
                    while Loc<End and CBUF!="\r" and CBUF!="\n":
                         Loc+=1
                         CBUF = source[Loc]
            elif CBUF=="A" :
                
                Acc = GetString()
                Last=Loc
                Loc+=1
                tmp=""
                while Loc<End and source[Loc]!="\r" and source[Loc]!="\n":
                    Loc+=1
                    if source[Loc]!="\r" and source[Loc] !="\n":
                        tmp+=source[Loc]
                        CBUF=source[Loc]
                if tmp.isnumeric():
                    VAcc[int(tmp)]=Acc
                    

            elif CBUF=="M":
                Loc+=1
                if source[Loc].isnumeric():
                    Flg="Y" if VAcc[int(source[Loc])]==VAcc[int(source[Loc+2])] else "N"
                else:
                    tmp=""
                    while Loc<End and CBUF!="\r" and CBUF!="\n":
                        Loc+=1
                        if source[Loc]!="\r" and source[Loc] !="\n":
                            tmp+=source[Loc]
                        CBUF=source[Loc]
                    Flg= "Y" if tmp==Acc else "N"

            elif CBUF=="J":
                Loc+=2
                cl=Loc
                nstr=""
                while cl<End and source[cl]!="\r" and source[cl]!="\n":
                    if source[cl]!="\r" and source[cl] !="\n":
                        nstr+=source[cl]
                    cl+=1 
                if not nstr.isnumeric():
                    print("Error at line "+line+" : expecting numeric literal.")
                i=int(nstr)
                if i==0:
                    Loc = Last-1
                else:
                    cl=0
                    while cl<End and i>0:
                        if source[cl]=="*":
                            i-=1
                        cl+=1
                    Loc=cl
                    continue
            elif CBUF=="S":
                Loc=End

            elif CBUF=="T":
                Loc+=2
                CBUF=source[Loc]
                while Loc<End and CBUF!="\r" and CBUF!="\n":
                    PrChar(source[Loc])
                    Loc+=1
                    CBUF=source[Loc]
                PrNL()
            elif CBUF>="0" and CBUF<="9":
                op="asg"
                if source[Loc+1]=="+":
                    Loc+=3
                    op="+"
                elif source[Loc+1]=="-":
                    Loc+=3
                    op="-"
                elif source[Loc+1]=="*":
                    Loc+=3
                    op="*"
                elif source[Loc+1]=="/":
                    Loc+=3
                    op="/"
                else:
                    Loc+=2
                    op="asg"

                nstr="";
                while Loc<End and source[Loc]!="\r" and source[Loc]!="\n":
                    if source[Loc]=="$":
                        if source[Loc+1]=="$":
                            nstr+="$"
                            Loc+=1
                        else:
                            Loc+=1
                            nstr=source[Loc]
                            if nstr.isnumeric():
                                nstr=VAcc[int(nstr)]
                            elif nstr=="A":
                                nstr=Acc;
                    else:
                        nstr+=source[Loc]
                    Loc+=1
                if op=="asg":
                    if nstr.isnumeric():
                        VAcc[int(CBUF)]=int(nstr)
                    else:
                        VAcc[int(CBUF)]=nstr
                elif op=="+":
                    if nstr.isnumeric():
                        VAcc[int(CBUF)]+=int(nstr)
                    else:
                        VAcc[int(CBUF)]+=nstr
                elif op=="-":
                    if nstr.isnumeric():
                        VAcc[int(CBUF)]-=int(nstr)
                    else:
                        print("Error : Type mismatch.")
                        return
                elif op=="*":
                    if nstr.isnumeric():
                        VAcc[int(CBUF)]*=int(nstr)
                    else:
                        print("Error : Type mismatch.")
                        return
                elif op=="/":
                    if nstr.isnumeric():
                        if nstr==0:
                            print("Error: Divide by zero.")
                            return
                        VAcc[int(CBUF)]/=int(nstr)
                    else:
                        print("Error : Type mismatch.")
                        return
                
            elif CBUF=="I":
                Loc+=2;
                CBUF=source[Loc]
                if CBUF.isnumeric():
                    if type(VAcc[int(CBUF)]) is int:
                        VAcc[int(CBUF)]=VAcc[int(CBUF)]+1;
                    else:
                        print("Error : cannot increment string.")
                        return
                else:
                    print("Error : expecting numeric literal.")
                    return
            elif CBUF=="D":
                Loc+=2;
                CBUF=source[Loc]
                if CBUF.isnumeric():
                    if type(VAcc[int(CBUF)]) is int:
                        VAcc[int(CBUF)]=VAcc[int(CBUF)]-1;
                    else:
                        print("Error : cannot decrement string.")
                else:
                    print("Error : expecting numeric literal.")
                    return
            elif CBUF=="P":
                Loc+=2;
                CBUF=source[Loc]
                if CBUF.isnumeric():
                    print(VAcc[int(CBUF)],end='');
                else:
                    if CBUF=="A":
                        print(Acc,end='')
                    else:
                        print("Error : expecting numeric literal.")
                        return

            else:
                CBUF=source[Loc]
                while Loc<End and CBUF!="\r" and CBUF!="\n":
                    PrChar(source[Loc])
                    Loc+=1
                    CBUF=source[Loc]
                Loc-=1
                PrNL()
        Loc+=1

def editor():
    ret = ""
    print("EWaduzitdo-PY / WaduzitdoNow V 1.0.")
    print("<c> 2024-2030 JP Programi")
    print("Input commands. Type 'EOF' to run.")
    uns = ""
    while uns!="EOF":
        uns=input('>')
        if uns!="EOF":
            ret+=uns+"\n"
    return ret

def main():
    source = """T:,-------------,
T:| Hallo Welt! |
T:'-------------'
T:
T:Bitte 'A' eingeben
A:
M:A
YT:Danke
NT:Nö, so nicht
NJ:0
T:Ende
S:"""
    if len(sys.argv)>1:
        try:
            f=open(sys.argv[1])
            source = f.read()
            Waduzitdo(source)
        except:
            print("Error reading file. File is not presend and/or corrupt.")
    else:
        source = editor()
        Waduzitdo(source)

if __name__ == "__main__":
    main()