credits = ('TEV was created by LibertasMater aka NutmegLover in July 2022 using the Atom editor and Python3.10 after going through the py4e tutorials as part of a homeschool education in Computer Science.')
print ('Hello! I am TEV. That stands for Transgender Electronic Validation.')
#ask for info
nam = input ('What is your name?')
print ('Oh okay. What is your gender?')
gender = input ('Are you a man, woman, or enby?')
#print with info assigned to variables
print ('Welcome', nam, 'you are a very good-looking', gender)
print ('I am very pleased to meet you.')
#assign a string of text to a variable
validation = ('You are valid. Your feelings matter. What is between your ears is your gender, what is between your legs is immaterial to who you are.')
#give 2 choices with an if-else statement, and then react accordingly
yass = input ('Would you like some validation?')
if yass == ('yes'):
    print (validation)
else :
    print ('Maybe next time', nam)
    print ('You are valid either way.')
do = input ('Do you mind if we continue?')
if do == ('yes'):
    print ('My apologies my dear', gender)
    print ('My creator LibertasMater would be vexed if I overstayed my welcome.')
    print ('I bid you adieu my dear friend', nam)
    print (credits)
    print ('A Trans', gender, 'is a', gender)
    exit()
else :
    print ('Okey-dokey! Moving on.')
# an if-elif-else sequence
print ('Hey - I was wondering about your sexuality. It is a spectrum just like gender.')
print ('It really depends on who you are attracted to. If it is the same sex you are')
print ('a Homosexual. If it is the opposite to what you are it is Heterosexual. If it is')
print ('both and you have a favorite then you are Bisexual. If you lack a favorite you are')
print ('Pansexual. If you are not atracted to others sexually, then you are Asexual.')
print ('If you are transgender - then think of your gender - not your sex - for this.')
print ('Your attraction has nothing to do with your body. It is between your ears just like')
print ('your gender is.')
print ('Just to keep it easy the abbreviations are Homo Hetero Bi Pan and Ace. If you do')
print ('not know - then enter idk.')
sexuality = input ('What is your sexuality?')
if sexuality == ('Homo'):
    print ('Oh that is wonderful. You know what I think?')
    if gender == ('man'):
        print ('It is okay to be Gay.')
    elif gender == ('woman'):
        print ('Lesbians are super cool.')
    elif gender == ('enby'):
        print ('Gai people are valid too.')
elif sexuality == ('Hetero'):
    print ('It is okay to be straight')
elif sexuality == ('Bi'):
    print ('You do not pick a side, you pick a person.')
    print ('You are valid whether your relationship is with a man or a woman.')
elif sexuality == ('Pan'):
    print ('Just like how all genders are sexy to you - you are sexy too.')
    print ('Do not forget to love yourself.')
elif sexuality == ('Ace'):
    print ('You do not have to be a sex obsessed allo to be valid. It is perfectly')
    print ('okay to eat garlic bread and invade Denmark. I totally get it.')
else :
    print ('It is okay to not know. You will get it figured out some day.')
#wrap it up with this
print (credits)
print ('A Trans', gender, 'is a', gender)
print ('Terf tears are delicious - smile and make those fuckers cry.')
exit()
