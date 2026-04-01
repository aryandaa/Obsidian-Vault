#programming 
“Mengapa tidak menggunakan hooks?” -- Materi ini kami sajikan untuk menjawab pertanyaan tersebut.

React--_begitu juga dengan cara mempelajarinya_--berada di tahap yang “aneh” saat ini. Hal ini dikarenakan hadirnya fitur “Hooks” sejak React versi 16.8. Hooks mengubah konsep komponen dalam mengelola _state_. Sebelum hadirnya hooks, state hanya dapat dimanfaatkan oleh class component, tetapi sekarang dapat juga dimanfaatkan oleh functional component. Lantas apa dampaknya bagi Anda yang hendak belajar React saat ini?

Oke, kami rasa kasus ini mirip dengan penambahan _arrow function_ yang dilakukan oleh JavaScript. Ketika arrow function hadir, tidak berarti seluruh pengetahuan yang kita miliki terkait _regular function_ sudah tidak relevan, bukan? Alih-alih menggantikan, arrow function sebenarnya hanya cara lain dalam mendefinisikan fungsi di JavaScript. React hooks pun demikian.

Seluruh konsep dan cara mempelajari React akan tetap sama, walau dengan hooks Anda bisa memanfaatkan component _state_ dengan cara lain. Hal ini ditegaskan oleh React melalui dokumentasi hooks yang mengatakan “Hooks tidak mengubah pengetahuan dari konsep React.” [[7](https://reactjs.org/docs/hooks-intro.html)]. Hooks hanya menawarkan API yang dapat mempercepat penggunaan konsep-konsep React (salah satunya state) yang sebenarnya sudah Anda ketahui.

React team juga membuat pernyataan yang jelas untuk tidak mengubah implementasi class component yang ada dengan menuliskan ulang menggunakan hooks. Namun, Anda bisa menerapkan hooks pada kode baru yang hendak dituliskan, itu pun jika Anda mau.

Namun, ingat ya! Jika Anda ingin menggunakan hooks, bukan berarti Anda boleh melewati proses memahami dasar dari state itu sendiri. Sialnya, Anda harus mempelajari keduanya. Karena jika Anda bekerja pada industri yang sudah lama menggunakan React dan kodenya belum menerapkan hooks, kami khawatir Anda kebingungan.

Tidak perlu sedih bila kelas ini tidak mengajarkan atau mengimplementasikan hooks karena kami ingin di awal pembelajaran Anda fokus untuk mengenal konsep dasar dari React itu sendiri. Hooks akan kami ajarkan di kelas terpisah setelah Anda memahami bagaimana implementasi React sebelum hadirnya hooks.