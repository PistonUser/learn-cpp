def decode(binary):
    sep_binary = [str(binary)[i:i+1] for i in range(0, len(str(binary)), 1)]
    
    error = 0
    
    let_num = int(0)
    
    num_let = {
        "31": ' ',
        "1": 'a',
        "2": 'b',
        "3": 'c',
        "4": 'd',
        "5": 'e',
        "6": 'f',
        "7": 'g',
        "8": 'h',
        "9": 'i',
        "10": 'j',
        "11": 'k',
        "12": 'l',
        "13": 'm',
        "14": 'n',
        "15": 'o',
        "16": 'p',
        "17": 'q',
        "18": 'r',
        "19": 's',
        "20": 't', 
        "21": 'u',
        "22": 'p',
        "23": 'w',
        "24": 'x',
        "25": 'y',
        "26": 'z',
        "27": '',
        "28": '',
        "29": '',
        "30": '',
        "31": 'space'
        }
    
    if sep_binary[len(str(binary)) - 1] == '1':
        let_num = let_num + 1
    if sep_binary[len(str(binary)) - 2] == '1':
        let_num = let_num + 2
    if sep_binary[len(str(binary)) - 3] == '1':
        let_num = let_num + 4
    if sep_binary[len(str(binary)) - 4] == '1':
        let_num = let_num + 8
    if sep_binary[len(str(binary)) - 5] == '1':
        let_num = let_num + 16
    if sep_binary[len(str(binary)) - 6] == '0':
        cap = num_let[str(let_num)]
        print(cap.capitalize())
        error = 1
    if sep_binary[len(str(binary)) - 7] == '0':
        if let_num >= 10:
            print('error')
            error = 1
        else:
            print(let_num)
            error = 1
    if error == 0:
        print(num_let[str(let_num)])