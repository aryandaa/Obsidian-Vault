#programming 
JavaScript hanyalah bahasa pemrograman. Ia tidak mengetahui apakah Anda menjalankannya menggunakan browser atau Node.js. Di browser, JavaScript dapat mengontrol fungsionalitas browser seperti mengunjungi halaman, memuat ulang, menutup tabs, serta menampilkan _alert dialog_. JavaScript mampu melakukan itu karena browser menambahkan objek `window` pada JavaScript.

Di Node.js pun demikian, ia menambahkan objek `global` guna memberikan fungsionalitas lebih pada JavaScript. Hal ini bertujuan untuk mendukung pengembangan pada environment-nya. Contoh, melalui objek global kita dapat melihat berapa CPU yang digunakan pada komputer, modularisasi berkas JavaScript, menampilkan nilai pada console, dan hal lainnya.

Objek `window` pada browser dan objek `global` pada Node.js merupakan _Global Object_. Seluruh fungsi atau properti yang menjadi member dari global object dapat diakses di mana saja alias memiliki cakupan global. Pada Node.js Anda bisa melihat apa saja yang termasuk member dari global objek dengan menggunakan kode berikut:

`Object.getOwnPropertyNames(global);`

Coba jalankan pada REPL. Ia akan mengembalikan semua _member_-nya.
```json
[
  'Object',
  'Function',
  'Array',
  'Number',
  'parseFloat',
  'parseInt',
  'Infinity',
  'NaN',
  'undefined',
  'Boolean',
  'String',
  'Symbol',
  'Date',
  'Promise',
  'RegExp',
  'Error',
  'AggregateError',
  'EvalError',
  'RangeError',
  'ReferenceError',
  'SyntaxError',
  'TypeError',
  'URIError',
  'globalThis',
  'JSON',
  'Math',
  'Intl',
  'ArrayBuffer',
  'Atomics',
  'Uint8Array',
  'Int8Array',
  'Uint16Array',
  'Int16Array',
  'Uint32Array',
  'Int32Array',
  'Float32Array',
  'Float64Array',
  'Uint8ClampedArray',
  'BigUint64Array',
  'BigInt64Array',
  'DataView',
  'Map',
  'BigInt',
  'Set',
  'WeakMap',
  'WeakSet',
  'Proxy',
  'Reflect',
  'FinalizationRegistry',
  'WeakRef',
  'decodeURI',
  'decodeURIComponent',
  'encodeURI',
  'encodeURIComponent',
  'escape',
  'unescape',
  'eval',
  'isFinite',
  'isNaN',
  'console',
  'process',
  'global',
  'Buffer',
  'clearImmediate',
  'setImmediate',
  'URL',
  'URLSearchParams',
  'DOMException',
  'AbortController',
  'AbortSignal',
  'Event',
  'EventTarget',
  'TextEncoder',
  'TextDecoder',
  'TransformStream',
  'TransformStreamDefaultController',
  'WritableStream',
  'WritableStreamDefaultController',
  'WritableStreamDefaultWriter',
  'ReadableStream',
  'ReadableStreamDefaultReader',
  'ReadableStreamBYOBReader',
  'ReadableStreamBYOBRequest',
  'ReadableByteStreamController',
  'ReadableStreamDefaultController',
  'ByteLengthQueuingStrategy',
  'CountQueuingStrategy',
  'TextEncoderStream',
  'TextDecoderStream',
  'CompressionStream',
  'DecompressionStream',
  'clearInterval',
  'clearTimeout',
  'setInterval',
  'setTimeout',
  'queueMicrotask',
  'structuredClone',
  'atob',
  'btoa',
  'BroadcastChannel',
  ... 71 more items
]
```

Banyak sekali yah member dari global objek. Namun dilansir dari website Node.js, sebenarnya mereka hanya menambahkan beberapa objek saja. Objek tersebut dinamakan dengan ‘true globals’. [[]](https://nodejs.org/api/globals.html#:~:text=Class%3A%20WritableStreamDefaultWriter-,global%20objects)  
Berikut adalah daftarnya:

- `global` : Global namespace. Member apa pun di dalam object ini dapat diakses pada cakupan global.
- `process` : menyediakan interaksi dengan proses Node.js yang berjalan.
- `console` : menyediakan berbagai fungsionalitas [STDIO](http://www.cplusplus.com/reference/cstdio/).
- `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`.

