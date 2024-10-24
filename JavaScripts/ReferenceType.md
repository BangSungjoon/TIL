# 참조 자료형

## 함수

<aside>
💡

참조 자료형에 속하며 모든 함수는 **Function** object

</aside>

### 참조 자료형 Reference type

- objects
    - object, Array, Function
- 객체의 주소가 저장되는 자료형
    - 가변, 주소가 복사

### 함수 구조

```jsx
function name ([param[, param, [..., param]]]) {
	statements
	return value
}
```

- function 키워드
- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statements
- return 값이 없다면 undefined를 반환

### 함수 정의 2가지 방법

- **선언식** function declaration
    
    ```jsx
    function funcName () {
    	statements
    }
    ```
    
    ```jsx
    function add (num1, num2) {
    	return num1 + num2
    }
    
    add(1, 2) // 3
    ```
    
    - 호이스팅 됨
        
        ```jsx
        add(1, 2) // 3
        function add (num1, num2) {
        	return num1 + num2
        }
        ```
        
    - 코드의 구조와 가독성 면에서는 표현식에 비해 장점이 있음
- **표현식** function expression
    
    ```jsx
    const funcName = function () {
    	statements
    }
    ```
    
    ```jsx
    const sub = function (num1, num2) {
    	return num1 - num2
    }
    
    sub(2, 1) // 1
    ```
    
    - 호이스팅 되지 않음
        - 변수 선언만 호이스팅되고 함수 할당은 실행 시점에 이루어짐
    - 함수 이름이 없는 ‘익명 함수’를 사용할 수 있음
        
        ```jsx
        sub(2, 1) // ReferenceError: Cannot access 'sub' before initialization
        
        const sub = function (num1, num2) {
        	return num1 - num2
        }
        ```
        
- 함수 표현식 사용을 권장하는 이유
    - 예측 가능성
        - 호이스팅의 영향을 받지 않아 코드의 실행 흐름을 더 명확하게 예측할 수 있음
    - 유연성
        - 변수에 할당되므로 함수를 값으로 다루기 쉬움
    - 스코프 관리
        - 블록 스코프를 가지는 let이나 const와 함께 사용하여 더 엄격한 스코프 관리가 가능

---

### 매개변수 정의 방법

1. 기본 함수 매개변수
2. 나머지 매개변수

### 기본 함수 매개변수 (Default function parameter)

전달하는 인자가 없거나 undefiend가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

```jsx
const greeting = function (name = 'Anonymous') {
	return `Hi ${name}`
}

greeting()  // Hi Anonymous
```

### 나머지 매개변수 (Rest parameters)

- 임의의 수의 인자를 ‘배열’로 허용하여 가변 인자를 나타내는 방법
    - 파이썬에서는 튜플로 허용했다.
- 작성 규칙
    - 함수 정의 시 나머지 매개변수는 하나만 작성할 수 있음
    - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함
    
    ```jsx
    const myFunc = function (param1, param2, ...restPrams) {
    	return [param1, param2, restPrams]
    }
    
    myFunc(1, 2, 3, 4, 5)  // [1, 2, [3, 4, 5]]
    myFunc(1, 2)           // [1, 2, []]
    ```
    

### 매개변수와 인자 개수가 불일치 할 때

에러를 발생 시키지 않는다!

- 매개변수 개수 > 인자 개수
    - 누락된 인자는 undefined로 할당
    
    ```jsx
    const threeArgs = function (param1, param2, param3) {
    	return [param1, param2, param3]
    }
    
    threeArgs() // [undefiend, undefiend, undefiend]
    threeArgs(1) // [1, undefiend, undefiend]
    threeArgs(2, 3) // [2, 3, undefiend]
    ```
    
- 매개변수 개수 < 인자 개수
    - 초과 입력한 인자는 사용하지 않음
    
    ```jsx
    const noArgs = function () {
    	return 0
    }
    noArgs(1, 2, 3) // 0
    
    const twoArgs = function (param1, param2) {
    	return [param1, param2]
    }
    twoArgs(1, 2, 3) // [1, 2]
    ```
    

---

### Spread syntax

**‘…’**

- 전개 구문
- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것 (확장, 전개)
- 전개 대상에 따라 역할이 다름
    - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등

### 전개 구문 활용처

1. 함수와의 사용
    1. 함수 호출 시 인자 확장
        
        ```jsx
        // spread-syntax.html
        function myFunc(x, y, z) {
        	return x + y + z
        }
        
        let numbers = [1, 2, 3]
        
        console.log(myFunc(...numbers))  // 6
        ```
        
    2. 나머지 매개변수 (압축)
        
        ```jsx
        // spread-syntax.html
        function myFunc2(x, y, ...restArgs) {
        	return [x, y, restArgs]
        }
        
        console.log(myFunc2(1, 2, 3, 4, 5))  // [1, 2, [3, 4, 5]]
        console.log(myFunc2(1, 2))           // [1, 2, []]
        ```
        
2. 객체와의 사용 (객체 파트에서 진행)
3. 배열과의 활용 (배열 파트에서 진행)

---

### 화살표 함수 표현식

Arrow function expression

- 함수 표현식의 간결한 표현법
- 화살표 함수로 변경 결과
    - 변경 전
        
        ```jsx
        const arrow = function (name) {
        	return `hello, ${name}`
        }
        ```
        
    - 변경 후
        
        ```jsx
        const arrow = name => `hello, ${name}`
        ```
        

### 화살표 함수 작성 과정

1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
2. 함수의 매개변수가 하나 뿐이라면, 매개변수의 `()` 제거 가능
    - 단, 생략하지 않는 것을 권장
3. 함수 본문의 표현식이 한 줄이라면, `{}`와 `return` 제거 가능
    
    ```jsx
    const arrow1 = function (name) {
    	return `hello, ${name}`
    }
    
    // 1. function 키워드 삭제 후 화살표 작성
    const arrow2 = (name) => { return `hello, ${name}` }
    
    // 2. 인자의 소괄호 삭제 (인자가 1개일 경우에만 가능)
    const arrow3 = name => { return `hello, ${name}` }
    
    // 3. 중괄호와 return 삭제 (함수 본문이 return을 포함한 표현식 1개일 경우에만 가능)
    const arrow4 = name => `hello, ${name}`
    ```
    

## 객체 Object

키로 구분된 데이터 집합을 저장하는 자료형 (data collection)

### 객체 구조

- 중괄호(’{}’)를 이용해 작성
- 중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용
    
    ```jsx
    const user = {
    	name: 'Alice',   // js에선 key에 공백이 없다면 문자형으로 인식해준다.
    	'key with space': true,  // 공백이 있으니 ''로 감싸 문자형으로 넣어주기
    	greeting: function () {
    		return 'hello'
    	}
    }
    ```
    

### 속성 참조

- 점(’.’, chaining operator) 또는 대괄호(’[]’)로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
    
    ```jsx
    // 조회
    console.log(user.name) // Alice
    console.log(user['key with space']) // true
    
    // 추가
    user.address = 'korea'
    console.log(user) 
    // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}
    
    // 수정
    user.name = 'Bella'
    console.log(user.name) // Bella
    
    // 삭제
    delete user.name
    console.log(user) // {key with space: true, address: 'korea', greeting: ƒ}
    ```
    

### ‘in’ 연산자

- 속성이 객체에 존재하는지 여부를 확인
    
    ```jsx
    console.log('greeting' in user) // true
    console.log('country' in user) // false
    ```
    

### Method

객체 속성에 정의된 함수

- object.method() 방식으로 호출
- Method 사용 예시
    - 메서드는 객체를 ‘행동’ 할 수 있게 함
    
    ```jsx
    console.log(user.greeting()) // hello
    ```
    
- ‘this’ 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음

### ‘this’ keyword

함수나 메서드를 호출한 객체를 가리키는 키워드

- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
- Method & this 사용 예시
    
    ```jsx
    const person = {
    	name: 'Alice',
    	greeting: function () {
    		return `Hello my name is ${this.name}`
    	},
    }
    
    console.log(person.greeting()) // Hello my name is Alice
    ```
    
- JavaScript에서 this는 함수를 ‘호출하는 방법’에 따라 가리키는 대상이 다름
    
    
    | 호출 방법 | 대상 |
    | --- | --- |
    | 단순 호출 | 전역 객체 → window |
    | 메서드 호출 | 메서드를 호출한 객체 |
    1. 단순 호출 시 this
        - 가리키는 대상 ⇒ 전역 객체
        
        ```jsx
        const myFunc = function () {
        	return this
        }
        
        console.log(myFunc()) // window
        ```
        
    2. 메서드 호출 시 this
        - 가리키는 대상 ⇒ 메서드를 호출한 객체
        
        ```jsx
        const myObj = {
        	data: 1,
        	myFunc: function () {
        		return this
        	}
        }
        
        console.log(myObj.myFunc()) // myObj
        ```
        
- 중첩된 함수에서의 this 문제점과 해결책
    - forEach의 인자로 작성된 함수는 일반적인 함수 호출이기 때문에 this가 전역 객체를 가리킴
        
        ```jsx
        const myObj2 = {
        	numbers: [1, 2, 3],
        	myFunc: function () {
        		tihs.numbers.forEach(function (number) {
        			console.log(this) // window
        		})
        	}
        }
        
        console.log(myObj2.myFunc())
        ```
        
    - 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수(myFunc)에서의 this 값을 가져옴
        
        ```jsx
        const myObj3 = {
        	numbers: [1, 2, 3],
        	myFunc: function () {
        		this.numbers.forEach((number) => {
        			console.log(this) // myObj3
        		})
        	}
        }
        
        console.log(myObj3.myFunc())
        ```
        

<aside>
💡

JavaScript ‘this’ 정리

- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- JavaScript에서 this는 함수가 “호출되는 방식”에 따라 결정되는 현재 객체를 나타냄
- Python의 self와 Java의 this가 선언 시 이미 값이 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적 할당)
- this가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은
    - 장점
        - 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
    - 단점
        - 이런 유연함이 실수로 이어질 수 있다는 것

개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데에 집중 

</aside>

### 단축 속성

- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

```jsx
// 단축 속성 적용 전
const name = 'Alice'
const age = 30

const user = {
	name: name,
	age: age,
}
```

```jsx
// 단축 속성 적용 후
const name = 'Alice'
const age = 30

const user = {
	name,
	age,
}
```

### 단축 메서드

- 메서드 선언 시 function 키워드 생략 가능

```jsx
// function 키워드 생략 전
const myObj1 = {
	myFunc: function () {
		return 'Hello'
	}
}

// function 키워드 생략 후
const myObj2 = {
	myFunc() {
		return 'Hello'
	}
}
```

### 계산된 속성 (computed property name)

- 키가 대괄호([])로 둘러싸여 있는 속성
    - 고정된 값이 아닌 변수 값을 사용할 수 있음

```jsx
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
	[product]: 5,
	[prefix + suffix]: 'value',
}

console.log(bag) // {연필: 5, myproperty: 'value"}
```

### 구조 분해 할당 (destructing assignment)

- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법

```jsx
// 구조 분해 할당 전
const userInfo = {
	firstName: 'Alice',
	userId: 'alice123',
	email: 'alice123@gmail.com'
}

const firstName = userInfo.name
const userId = userInfo.userId
const email = userInfo.email
```

```jsx
// 구조 분해 할당 후
const userInfo = {
	firstName: 'Alice',
	userId: 'alice123',
	email: 'alice123@gmail.com'
}

const { firstName } = userInfo
const { firstName, userId } = userInfo
const { firstName, userId, email } = userInfo
```

- 구조 분해 할당 활용
    - ‘함수의 매개변수’로 객체 구조 분해 할당 활용 가능
    
    ```jsx
    const person = {
    	name: 'Bob',
    	age: 35,
    	city: 'London',
    }
    
    function printInfo({ name, age, city }) {
    	console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
    }
    
    // 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
    printInfo(person) // 이름: Bob, 나이: 35, 도시: London
    ```
    

### Object with ‘전개 구문’

- “객체 복사”
    - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```jsx
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj)  // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

### 유용한 객체 메서드

- Object.keys()
- Object.values()

```jsx
const profile = {
	name: 'Alice',
	age: 30,
}

console.log(Object.keys(profile))  // ['name', 'age']

console.log(Object.values(profile))  // ['Alice', 30]
```

### Optional chaining (’?.’)

- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

```jsx
const user = {
	name: 'Alice',
	greeting: function () {
		return 'hello'
	}
}
```

```jsx
console.log(user.address.street)  // Uncaught TypeError
console.log(user.address?.street)  // undefined

console.log(user.nonMethod())  // Uncaught TypeError
console.log(user.nonMethod?.())  // undefined
```

- 만약 Optional chaining을 사용하지 않는다면 다음과 같이 ‘&&’ 연산자를 사용해야 함
    
    ```jsx
    const user = {
    	name: 'Alice',
    	greeting: function () {
    		return 'hello'
    	}
    }
    
    console.log(user.address && user.address.street)  // undefined
    ```
    
- Optional chaining 장점
    - 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음
    - 어떤 속성이 필요한지에 대한 보증이 확실하지 않는 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음
- Optional chaining 주의사항
    1. Optional chaining은 존재하지 않아도 괜찮은 대상에서만 사용해야 함 (남용 X)
        - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용
        - 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문
        
        ```jsx
        // 이전 예시 코드에서 user 객체는 논리상 반드시 있어야 하지만 address는 필수 값이 아님
        // user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문
        
        // Bad
        user?.address?.street
        
        // Good
        user.address?.street
        ```
        
    2. Optional chaining 앞의 변수는 반드시 선언되어 있어야 함
        
        ```jsx
        console.log(myObj?.address) // Uncaught ReferenceError: myObj is not defined
        ```
        
- Optional chaining 정리
    1. obj?.prop
        - obj가 존재하면 obj.prop을 반환하고, 그렇지 않으면 undefined를 반환
    2. obj2.[prop]
        - obj가 존재하면 obj[prop]을 반환하고, 그렇지 않으면 undefined를 반환
    3. obj?.method()
        - obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined를 반환

### JSON

- “JavaScript Object Notation”
- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 ‘문자열’
- JavaScript의 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함
- Object ↔ JSON 변환하기
    
    ```jsx
    const jsObject = {
    	coffee: 'Americano',
    	iceCream: 'Cookie and cream',
    }
    ```
    
    ```jsx
    // Object -> JSON
    const objToJson = JSON.stringity(jsObject)
    console.log(objToJson)  // {"coffee": "Americano", "iceCream": "Cookie and cream"}
    console.log(typeof objToJson)  // string
    ```
    
    ```jsx
    // JSON -> Object
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
    console.log(typeof jsonToObj)  // object
    ```
    

## 참고

### 화살표 함수 심화

```jsx
// 1. 인자가 없다면 () or _ 로 표시 가능
const noArgs1 = () => 'No args'
const noArgs2 = _ => 'No args'

// 2-1. object를 return 한다면 return을 명시적으로 작성해야 함
const returnObject1 = () => { return { key: 'value' } }

// 2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함
const returnObject2 = () => ({ key: 'value' })
```

### 클래스

- 클래스의 필요성
    - 동일한 형태의 객체를 여러 개 만들 때 필요!
- 객체를 생성하기 위한 템플릿
    - 객체의 속성, 메서드를 정의하는 청사진 역할
- 클래스 기본 문법
    1. class 키워드
    2. 클래스 이름
    3. 생성자 메서드
        - constructor()
        
        ```jsx
        class MyClass {
        	// 여러 메서드를 정의할 수 있음
        	constructor() { ... }
        	method1() { ... }
        	method2() { ... }
        	method3() { ... }
        	...
        }
        ```
        
- 클래스 특징
    - ES6에서 도입
    - 생성자 함수를 사용하여 객체를 생성하는 이전의 방식을 객체 지향적으로 표현하고자 만들어짐
    - 그래서 클래스는 내부적으로 생성자 함수를 기반으로 동작함
    
    ```jsx
    // 생성자 함수
    
    function Member(name, age) {
    	this.name = name
    	this.age = age
    	this.sayHi = function () {
    		console.log(`Hi, I am ${this.name}`)
    	}
    }
    ```
    
    ```jsx
    // 클래스
    class Member {
    	constructor(name, age) {
    		this.name = name
    		this.age = age
    	}
    	sayHi() {
    		console.log(`Hi, I am ${this.name}`)
    	}
    }
    ```
    
- 클래스 활용
    
    ```jsx
    class Member {
    	constructor(name, age) {
    		this.name = name
    		this.age = age
    	}
    	sayHi() {
    		console.log(`Hi, I am ${this.name}`)
    	}
    }
    
    const member3 = new Member('Alice', 20)
    
    console.log(member3)  // Member { name: 'Alice', age: 20 }
    console.log(member3.name)  // Alice
    member3.sayHi()
    ```
    

### ‘new’ 연산자

클래스나 생성자 함수를 사용하여 새로운 객체를 생성

```jsx
const instance = new ClassName(arg1, arg2)
```

- 클래스의 constructor()는 new 연산자에 의해 자동으로 호출되며 특별한 절차 없이 객체를 초기화 할 수 있음
- new 없이 클래스를 호출하면 TypeError 발생