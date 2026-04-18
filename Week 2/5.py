# 'if' statement:

birth_year=int(input('Please enter your date of birth:'))

current_year=2025

age= current_year - birth_year

if(age<13):
    print('You are under age, you cannot watch this movie.')
    print('Wait until you are old enough to watch the movie.')
else:
    print('You are old enough to watch Avengers, Enjoy!')
    print('Don\'t forget to watch sequels and prequels')
    
print('Have a nice time!')