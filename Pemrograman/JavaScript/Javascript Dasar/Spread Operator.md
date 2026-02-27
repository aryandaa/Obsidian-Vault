#programming 

## Spread Operator
_Spread_, memiliki arti sesuai dengan namanya, yaitu menyebarkan. Spread operator digunakan untuk menyebarkan nilai yang ada pada object dan array. Spread operator yang ditandai dengan sintaks tiga titik  (...) adalah fitur yang menarik dan membantu dalam pengelolaan object dan array. Dengan menggunakan spread operator, nilai object dan array dapat di-_iterable_ menjadi beberapa element.

### Object
```js
const obj1 = { name: 'Dicoding' };
const obj2 = { lastName: 'Indonesia', address: 'Jl. Batik Kumeli No 50' };
const newObj = { ...obj1, ...obj2 };

console.log(newObj); // Output: { name: 'Dicoding', lastName: 'Indonesia', address: 'Jl. Batik Kumeli No 50' }
```

### Array
```js
const array1 = ['Dicoding'];
const array2 = ['Indonesia', 'Jl. Batik Kumeli No 50'];
const newArray = [...array1, ...array2];

console.log(newArray); // Output: ['Dicoding', 'Indonesia', 'Jl. Batik Kumeli No 50']
```


Spread operator juga dapat digunakan untuk menyalin sebuah array seperti berikut.
```js
const original = ['apple', 'banana', 'cherry'];
const copy = [...original];

console.log(copy); // Output: ['apple', 'banana', 'cherry']
```
