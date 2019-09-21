
import pickle, sys

class cMember:
    def __init__(self,fio,adres,telephon):
        self.id         =   len(m_list)
        self.fio        =   fio
        self.adres      =   adres
        self.telephon   =   telephon
        m_list.append(self)

        print(' Create :{0}'.format(self.fio))

    def tell(self):
        print('id:{0}'.format(self.id),'Fio:{0}; Adress:{1}; Tel:{2}'.format(self.fio,self.adres,self.telephon))

def read_ab():    
    try:
        f=open(fileName,'rb')
        ablist=pickle.load(f)
        f.close()
    except FileNotFoundError:
        ablist  =   []

    return ablist

def write_ab():
    f=open(fileName,'wb')
    pickle.dump(m_list,f)
    print('write in base-date: ',f.name)
    f.close()
      
def print_list(m_list):
    print('*'*20)
    print('Записей в БД: ',len(m_list))
    for item in m_list:
        item.tell()
    print('*'*20)
        

#ОСНОВНОЙ БЛОК ПРОГРАММЫ
#jjkkklklk
fileName    =   'ab2.znc'
work        =   True
flagMode    =   ''
cmd_mode    =   False
m_list      =   read_ab()


if __name__ == "__main__":
    if len (sys.argv) == 5:
        flagMode    =    sys.argv[1]
        fio         =    sys.argv[2]
        adress      =    sys.argv[3]
        telephone   =    sys.argv[4]   
        cmd_mode    =   True
    elif len (sys.argv) == 2:
        flagMode    =    sys.argv[1]
        cmd_mode    =   True


while work:
    if flagMode =='':
        flagMode    =   input('Укажите режим работы (input или print)')

    if flagMode ==  'input':
        if not cmd_mode:         
            fio         =   input('Введите Фамилию Имя Отчество:')
            adress      =   input('Введите адрес:')
            telephone   =   input('Введите телефон:')
        
        cMember(fio,adress ,telephone)
        write_ab()        

    elif flagMode ==  'print':
        print_list(m_list)

    elif flagMode ==  'help':   
        print('Mode = ["help", "input", "print"];"FIO";"Adress";"Telephone"')

    else:
        print('Неизвестный параметр: <{0}> выход из программы'.format(flagMode))
        work    =   False
    

    if cmd_mode: #В режиме командной строки просто выходим
        work    =   False
    else:
        flagMode    =   ''    

    
