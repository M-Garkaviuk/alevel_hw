
const employeeArr = [
    {
        id: 1,
        name: 'Денис',
        surname: 'Хрущ',
        salary: 1010, 
        workExperience: 10, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 2,
        name: 'Сергей',
        surname: 'Войлов',
        salary: 1200, 
        workExperience: 12, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 3,
        name: 'Татьяна',
        surname: 'Коваленко',
        salary: 480, 
        workExperience: 3, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'female'
    },
    {
        id: 4,
        name: 'Анна',
        surname: 'Кугир',
        salary: 2430, 
        workExperience: 20, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'female'
    },
    {
        id: 5,
        name: 'Татьяна',
        surname: 'Капустник',
        salary: 3150, 
        workExperience: 30, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'female'
    },
    {
        id: 6,
        name: 'Станислав',
        surname: 'Щелоков',
        salary: 1730, 
        workExperience: 15, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 7,
        name: 'Денис',
        surname: 'Марченко',
        salary: 5730, 
        workExperience: 45, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'male'
    },
    {
        id: 8,
        name: 'Максим',
        surname: 'Меженский',
        salary: 4190, 
        workExperience: 39, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 9,
        name: 'Антон',
        surname: 'Завадский',
        salary: 790, 
        workExperience: 7, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
    {
        id: 10,
        name: 'Инна',
        surname: 'Скакунова',
        salary: 5260, 
        workExperience: 49, /// стаж работы (1 = один месяц)
        isPrivileges: true, /// льготы
        gender: 'female'
    },
    {
        id: 11,
        name: 'Игорь',
        surname: 'Куштым',
        salary: 300, 
        workExperience: 1, /// стаж работы (1 = один месяц)
        isPrivileges: false, /// льготы
        gender: 'male'
    },
];

//1

const employee = [0, 'Valeriy', 'Zhmishenko', 1000, 10, true, 'male']

class Employee {
    constructor (id, name, surname, salary, workExperience, isPrivelages, gender) {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.salary = salary;
        this.workExperience = workExperience;
        this. isPrivelages = isPrivelages;
        this.gender = gender;
    }
    getFullName() {
        return `${this.name} ${this.surname}`
    }

    getSalary() {
        return this.salary
    }
}
//2
const employeeObj = new Employee(...employee);
console.log(employeeObj.getFullName());

//3

let createEmployesFromArr = (arr) => {
    return arr.map((employeeData) => {
    const {
        id,
        name,
        surname,
        salary,
        workExperience,
        isPrivileges,
        gender,
      } = employeeData;
  
      return new Employee(
        id,
        name,
        surname,
        salary,
        workExperience,
        isPrivileges,
        gender
      );
  })
}
  
const employeeConstructArr = createEmployesFromArr(employeeArr);
console.log(emplyeeConstructArr);

//4
const getFullNamesFromArr = (arr) => {
    const fullNames = []
    for(i = 0; i < arr.length; i++) {
    const fullName = arr[i].getFullName();
    fullNames.push(fullName);
    };
    return fullNames;
};

getFullNamesFromArr(employeeConstructArr)

//5
const getMiddleSalary = (arr) => {
    let totalSalary = 0
    
    for(i = 0; i < arr.length; i++) {
        totalSalary += arr[i].getSalary();
    }
    const middleSalary = (totalSalary / arr.length).toFixed(2);
    return middleSalary;
};

getMiddleSalary(employeeConstructArr) /// 2388.18

//6
const getRandomEmployee = (arr) => {
    randomNumber = Math.round(Math.random() * arr.length);
    return arr[randomNumber].getFullName();
    };
    
    getRandomEmployee(emplyeeConstructArr) 