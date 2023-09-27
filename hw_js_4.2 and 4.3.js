// Реализуйте класс CustomString, который будет иметь следующие методы:
//  метод reverse(), который параметром принимает строку, а возвращает ее в перевернутом виде,
//  метод ucFirst(), который параметром принимает строку, а возвращает эту же строку, 
//  сделав ее первую букву заглавной и метод 
//  ucWords, который принимает строку и делает заглавной первую букву каждого слова этой строки.


class CustomString {
    constructor() {
        this.string = '' 
    }

    reverse (string) {
                
        return string.split('')
                     .reverse()
                    .join('');

    };
    ucFirst(string) {
        const res = string.split('')
        res[0] = res[0].toUpperCase()
        return res.join('')   
    }

    ucWords(string) {
        const words = string.split(' ');
        const capitalizedWords = words.map(word => this.ucFirst(word));
        return capitalizedWords.join(' ');
    }
}    
 const myString = new CustomString();

myString.reverse('qwerty'); //выведет 'ytrewq'
myString.ucFirst('qwerty'); //выведет 'Qwerty'
myString.ucWords('qwerty qwerty qwerty'); //выведет 'Qwerty Qwerty Qwerty


/* Реализуйте класс Validator, который будет проверять строки.
К примеру, у него будет метод checkIsEmail() параметром принимает строку и проверяет,
 является ли она емейлом или нет.
 Если является - возвращает true, если не является - то false. Кроме того, класс будет иметь следующие методы: метод checkIsDomain для проверки домена, метод checkIsDate для проверки даты и метод checkIsPhone для проверки телефона:
var validator = new Validator(); */

class Validator {
    checkIsEmail(email) {        
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        return emailRegex.test(email);
    }

    checkIsDomain(domain) {
        const domainRegex = /^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        return domainRegex.test(domain);
    }


    checkIsPhone(phone, country = 'UA') {       
        const uaPhoneRegex = /^\+38\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/;
      
        if (country === 'UA') {
            return uaPhoneRegex.test(phone);
        }
       
        return false;
    }
}

var validator = new Validator();

validator.checkIsEmail('vasya.pupkin@gmail.com'); // true
validator.checkIsDomain('google.com'); // true
validator.checkIsPhone('+38 (066) 937-99-92'); // // true