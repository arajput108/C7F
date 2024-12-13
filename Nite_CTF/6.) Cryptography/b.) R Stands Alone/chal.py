from Crypto.Util.number import *

def gen_keys():
    while True:
        a = getPrime(128)
        b = getPrime(128)
        A = a+b
        B = a-b 
        
        p = ((17*A*A*A) - (15*B*B*B) - (45*A*A*B) + (51*A*B*B)) // 8

        if isPrime(p) :
            return a, b, p
    
p, q, r = gen_keys()
e = 65537
n = p*q*r

flag = b"nite{REDACTED}"

ct = pow(bytes_to_long(flag), e, n)
print(f"{r =}")
print(f"{ct =}")

"""OUTPUT :
r =17089720847522532186100904495372954796086523439343401190123572243129905753474678094845069878902485935983903151003792259885100719816542256646921114782358850654669422154056281086124314106159053995410679203972646861293990837092569959353563829625357193304859110289832087486433404114502776367901058316568043039359702726129176232071380909102959487599545443427656477659826199871583221432635475944633756787715120625352578949312795012083097635951710463898749012187679742033
ct =583923134770560329725969597854974954817875793223201855918544947864454662723867635785399659016709076642873878052382188776671557362982072671970362761186980877612369359390225243415378728776179883524295537607691571827283702387054497203051018081864728864347679606523298343320899830775463739426749812898275755128789910670953110189932506526059469355433776101712047677552367319451519452937737920833262802366767252338882535122186363375773646527797807010023406069837153015954208184298026280412545487298238972141277859462877659870292921806358086551087265080944696281740241711972141761164084554737925380675988550525333416462830465453346649622004827486255797343201397171878952840759670675361040051881542149839523371605515944524102331865520667005772313885253113470374005334182380501000
"""