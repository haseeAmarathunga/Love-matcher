#This is support only Python 2.7 Version deveoped by Hasee Amarathunga

print ("*****Hasee's Art  © developed by Hasee Amarathunga******")
print ("Welcome To Hasee's love Magic Converter")
print ('<<<හසී>>> ගේ මැජික් ආදරලන්තය ට ආදරයෙන් පිළිගනිමි.')
print ("ඔබගේ ආදරය ට ජය....(Congrats for your Love!)")


while True:
    print (" ")
    male=input("Input Your Name"+\
"(කරැණාකර ඔබගේ නම ඇතුලත් කරන්න) : ")
    print " "
    female=input("Input Your Lover Name"+\
"(ඔබගේ ආදරවන්තයාගේ හෝ වන්තියගේ නම ඇතුලත් කරන්න) : ")
    if male=='' :
        print ('your name is not inputed \කර නොමැත.)'
 ඔබගේ නම ඇතුලත් කර නොමැත

    else:
        n=len(male)
        m=len(female)

        dic1=[]
        dic2=[]

        try:

            for i in range(0,n):
                dic1=dic1+[male[i]]
                
                
               
            for j in range(0,m):
                dic2=dic2+[female[j]]
                


                    
            y=len(dic1)
            z=len(dic2)
            #print y,z

            newdic1=(dic1+dic2)
            newdic2=(dic2+dic1)
            diction=dic1
            #print newdic1
            #print newdic2
            k=len(newdic1)
            ni=[]


            for l in range(0,y):
                if newdic1[l] in dic2:
                    dic1.remove(newdic1[l])
                    dic2.remove(newdic1[l])

            final= dic1+dic2
            #print final

            #FLAME Magic
            l1=len(final)
            flame=['F','L','A','M','E']
            l2=len(flame)

            for w in range(0,l2):
                if l1%l2==w:
                    magic= flame[w+1]

            if magic=='F':
                print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>your result is here')
                print ("You TRYING TO {0}. ඔබ {1} ට උත්සාහ කරයි.\
කෙසේ හෝ උත්සාහ කරන්න. ඔබට ආදරය ජය ගත හැක ".format(female,female))
                print (' ')
                print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                
            elif magic=='L':
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
                print ' '
                print ("You LOVE {0}. ඔබ {1} ට ආදරය කරයි. \
ඔබගේ ආදරය පරම පිවිතුරැ අවංක ආදරයකි".format(female,female))
                print ' '
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

                
            elif magic=='A':
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>your result is here'
                print ' '
                print ("You ATTRACTION {0}.ඔබ {1} ට ආකර්ෂණය වී ඇත.\
කරැණාකර හැගීමි වලට වහල් නොවී සැබෑ ආදරය පිටුපස හඹා යන්න.".format(female,female))
                print ' '
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

            elif magic=='M':
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>your result is here'
                print ' '
                print ("You MARIAGE {0}.ඔබ {1} ගේ අනාගත සහකරැයි.\
ඔබ දෙදෙනාට සාර්ථක යුග දිවියක් ගත කළ හැකිය පුංචි පුංචි ගැටලු මතු වුවද ඔබ \
දෙදෙනාගේ ජීවිතය ආදරණියව ගෙවීමට හැකියාව ඇත".format(female,female))
                print ' '
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

            elif magic=='E':
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>your result is here'
                print ' '
                print ("Your and {0} are the INTIMATER. \
ඔබ හා {1} ආත්මීය බැදීමකින් එක්ව ඇත. ඔබ වෙන් කිරීමට කිසිවෙකුට නොහැක. \
 පුංචි පුංචි ගැටලු මතු වුවද ඔබ දෙදෙනාගේ  එක්වීම ඉර හද මෙන් සථීරය.".format(female,female))
                print ' '
                print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

        except:
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>your result is here'
            print ' '
            print ("Your Love is One side Love.Try and Try.One day you can Fly.\
ඔබගේ ආදරය ඒක පාර්ශවීය ආදරයකි. උත්සාහ කරන්න දිනෙක {0}  \
ඔබෙ වනු ඇත".format(female))
            print '                                                '

#All result based on Sinhalese and English languages developed by Hasee Amarathunga










