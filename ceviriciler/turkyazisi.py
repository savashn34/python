def cevir():
    
    while True:
        sessizler = ["b","c","ç","d","e","f","g","ğ","h","j","k","l","m","n","p","r","s","ş","t","v","y","z"]
        tumce = []
        girdi = input(">>> ").lower()

        if girdi == 'kapat':
            return

        girdi += ' '

        for i in range(len(girdi)):

            ## A-E SESLİSİ

            if girdi[i] in ['a', 'e'] and girdi[i+1] == 'm' and girdi[i+2] == 'a' and girdi[i+3] == 'm' and not girdi[i-1] == 'y':
                tumce += '𐰀'
            elif girdi[i] in ['a', 'e'] and girdi[i+1] == 'm' and girdi[i+2] == 'a' and girdi[i+3] == 'z':
                tumce += '𐰀'
            elif girdi[i] in ['a', 'e'] and girdi[i+1] == 'm' and girdi[i+3] == 'y' and girdi[i+5] == 'z':
                tumce += '𐰀'
            elif girdi[i] in ['a', 'e'] and girdi[i+1] == ' ':
                tumce += '𐰀'

            ## DİĞER SESLİLER
                
            # İLK ADIM SÖZCÜK SONUNA DEĞİNİR.
            # İKİNCİ ADIM SÖZCÜK BAŞINA DEĞİNİR. SONRAKİ SESİN K OLMADIĞINI YOKLAR.
            # ÜÇÜNCÜ ADIM İLK SESSİZDEN SONRA GELEN Ö-Ü SESİNİ YOKLAR. BİR ADIM ÖNCESİ SESSİZSE, SESSİZDEN ÖNCE DE BOŞLUK GELİYORSA YAZ DER.
                
            elif girdi[i] in ['ö', 'ü'] and girdi[i+1] == ' ' or girdi[i] in ['ö', 'ü'] and girdi[i-1] == ' ' and not girdi[i+1] == 'k' or girdi[i] in ['ö', 'ü'] and girdi[i-1] in sessizler and girdi[i-2] == ' ':
                tumce += '𐰇'
            elif girdi[i] in ['o', 'u'] and girdi[i+1] == ' ' or girdi[i] in ['o', 'u'] and girdi[i-1] == ' ' and not girdi[i+1] == 'k' or girdi[i] in ['o', 'u'] and girdi[i-1] in sessizler and girdi[i-2] == ' ':
                tumce += '𐰆'
            elif girdi[i] == 'ı' and girdi[i+1] == ' ' or girdi[i] == 'ı' and girdi[i-1] == ' ' and not girdi[i+1] == 'k' or girdi[i] == 'ı' and girdi[i-1] in sessizler and girdi[i-2] == ' ' and not girdi[i+1] == 'k':
                tumce += '𐰃'
            elif girdi[i] == 'i' and girdi[i+1] == ' ' or girdi[i] == 'i' and girdi[i-1] == ' ' and not girdi[i+1] == 'ç' or girdi[i] == 'i' and girdi[i-1] in sessizler and girdi[i-2] == ' ' and not girdi[i+1] == 'ç':
                tumce += '𐰃'
            elif girdi[i] in ['o', 'u'] and girdi[i-1] == 'y' and girdi[i+1] == 'r':
                tumce += '𐰆'

            ## İKİLİ SESSİZLER
                
            elif girdi[i] == 'l' and girdi[i+1] in ['d', 't']:
                tumce += '𐰡'
            elif girdi[i] == 'n' and girdi[i+1] in ['d', 't']:
                tumce += '𐰦'
            elif girdi[i] == 'n' and girdi[i+1] in ['c', 'ç']:
                tumce += '𐰨'
            
            ## BİLEŞİK ÜNSÜZLER
                
            # BİRİNCİ DURUM i'DEN ÖNCE ç GELİP GELMEDİĞİNİ YOKLAR.
            # İKİNCİ DURUM ç'NİN SÖZ BAŞINDA OLUP OLMADIĞINI YOKLAR.
            # ÜÇÜNCÜ DURUM ç'NİN SÖZCÜK BAŞINDA OLUP OLMADIĞINI YOKLAR.
            # DÖRDÜNCÜ DURUM i'NİN SÖZCÜK BAŞINDA OLUP OLMADIĞINI YOKLAR.
            
            elif girdi[i] in ['o', 'u'] and girdi[i+1] in ['k', 'h'] or girdi[i] in ['k', 'h'] and girdi[i+1] in ['o', 'u'] and girdi[i-1] == ' ' or girdi[i] in ['k', 'h'] and girdi[i+1] in ['o', 'u'] and girdi[i] == girdi[0]:
                tumce += '𐰸'
            elif girdi[i] in ['ö', 'ü'] and girdi[i+1] in ['k', 'h'] or girdi[i] in ['k', 'h'] and girdi[i+1] in ['ö', 'ü'] and girdi[i-1] == ' ' or girdi[i] in ['k', 'h'] and girdi[i+1] in ['ö', 'ü'] and girdi[i] == girdi[0]:
                tumce += '𐰰'
            elif girdi[i] == 'ı' and girdi[i+1] in ['k', 'h'] or girdi[i] in ['k', 'h'] and girdi[i+1] == 'ı' and girdi[i-1] == ' ' or girdi[i] == 'ı' and girdi[i+1] == 'ı' and girdi[i] == girdi[0]:
                tumce += '𐰶'
            elif girdi[i] == 'i' and girdi[i+1] == 'ç' or girdi[i] == 'ç' and girdi[0] == 'ç' and girdi[i+1] == 'i' or girdi[i] == 'ç' and girdi[i+1] == 'i' and girdi[i-1] == ' ': # İÇ SORUNSUZ ÇALIŞMAKTADIR.
                tumce += '𐰱'

            ## SESSİZLER

            elif girdi[i] == ' ':
                tumce += ' '
            elif girdi[i] in ['b', 'v'] and girdi[0] in ['b', 'v'] and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['b', 'v'] and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['b', 'v'] and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['b', 'v'] and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰋'
            elif girdi[i] in ['b', 'v'] and girdi[0] in ['b', 'v'] and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['b', 'v'] and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['b', 'v'] and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['b', 'v'] and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰉'
            elif girdi[i] == 'd' and girdi[0] == 'd' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'd' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'd' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] and not girdi[i-1] in ['l', 'n'] or girdi[i] == 'd' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰓'
            elif girdi[i] == 'd' and girdi[0] == 'd' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'd' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'd' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] and not girdi[i-1] in ['l', 'n'] or girdi[i] == 'd' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰑'
            elif girdi[i] in ['g','ğ'] and girdi[0] in ['g','ğ'] and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['g','ğ'] and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['g','ğ'] and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['g','ğ'] and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰏'
            elif girdi[i] in ['g','ğ'] and girdi[0] in ['g','ğ'] and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['g','ğ'] and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['g','ğ'] and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['g','ğ'] and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰍'
            elif girdi[i] == 'l' and girdi[0] == 'l' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'l' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'l' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'l' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰠'
            elif girdi[i] == 'l' and girdi[0] == 'l' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'l' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'l' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'l' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰞'
            elif girdi[i] == 'n' and girdi[0] == 'n' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'n' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'n' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'n' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰤'
            elif girdi[i] == 'n' and girdi[0] == 'n' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'n' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'n' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'n' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰣'
            elif girdi[i] == 'r' and girdi[0] == 'r' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'r' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'r' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'r' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰼'
            elif girdi[i] == 'r' and girdi[0] == 'r' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'r' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'r' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'r' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰺'
            elif girdi[i] == 's' and girdi[0] == 's' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 's' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 's' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 's' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰾'
            elif girdi[i] == 's' and girdi[0] == 's' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 's' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 's' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 's' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰽'
            elif girdi[i] == 't' and girdi[0] == 't' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 't' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 't' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] and not girdi[i-1] in ['l', 'n'] or girdi[i] == 't' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐱅'
            elif girdi[i] == 't' and girdi[0] == 't' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 't' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 't' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] and not girdi[i-1] in ['l', 'n'] or girdi[i] == 't' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐱃'
            elif girdi[i] == 'y' and girdi[0] == 'y' and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'y' and girdi[i-1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'y' and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] == 'y' and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰘'
            elif girdi[i] == 'y' and girdi[0] == 'y' and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'y' and girdi[i-1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'y' and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] == 'y' and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰖'
            elif girdi[i] in ['k', 'h'] and girdi[0] in ['k', 'h'] and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['k', 'h'] and girdi[i-1] in ['e', 'i'] or girdi[i] in ['k', 'h'] and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['k', 'h'] and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i', 'ö', 'ü']:
                tumce += '𐰚'
            elif girdi[i] in ['k', 'h'] and girdi[0] in ['k', 'h'] and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['k', 'h'] and girdi[i-1] == 'a' or girdi[i] in ['k', 'h'] and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['k', 'h'] and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı', 'o', 'u']:
                tumce += '𐰴'

            # elif girdi[i] in ['k', 'h'] and girdi[i] == girdi[0] and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['k', 'h'] and girdi[i-1] == ' ' and girdi[i+1] in ['e', 'i'] or girdi[i] in ['k', 'h'] and girdi[i-1] in sessizler and girdi[i+1] in ['e', 'i', 'ö', 'ü'] or girdi[i] in ['k', 'h'] and girdi[i-1] in ['e', 'i', 'ö', 'ü'] and girdi[i+1] == ' ':
            #     tumce += '𐰚'
            # elif girdi[i] in ['k', 'h'] and girdi[i] == girdi[0] and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['k', 'h'] and girdi[i-1] == ' ' and girdi[i+1] in ['a', 'ı'] or girdi[i] in ['k', 'h'] and girdi[i-1] in sessizler and girdi[i+1] in ['a', 'ı', 'o', 'u'] or girdi[i] in ['k', 'h'] and girdi[i-1] in ['e', 'i', 'ö', 'ü'] and girdi[i+1] == ' ':
            #     tumce += '𐰴'

            # İLK ADIM TÜMCE BAŞINI YOKLAR.
            # İKİNCİ ADIM SÖZCÜK BAŞINI YOKLAR.
            # ÜÇÜNCÜ ADIM İKİ SESSİZİN YAN YANA GELME DURUMUNU YOKLAR

            ## DEĞİŞMEZLER

            elif girdi[i] == 'm':
                tumce += '𐰢'
            elif girdi[i] in ['c', 'ç'] and not girdi[i-1] in ['i', 'n']:
                tumce += '𐰲'
            elif girdi[i] in ['p', 'f']:
                tumce += '𐰯'
            elif girdi[i] == 'ş':
                tumce += '𐱁'
            elif girdi[i] == 'z':
                tumce += '𐰕'

        tumce.pop()
        tumce = tumce[::-1]
        tumce = "".join(tumce)
        print(tumce)
cevir()