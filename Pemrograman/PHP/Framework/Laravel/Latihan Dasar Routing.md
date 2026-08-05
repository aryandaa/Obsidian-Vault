#latihan 
### Latihan 1

Buat route sehingga ketika membuka:
```
/about
```

muncul:
```
Tentang Kami
```

---

### Latihan 2

Buat route:
```
/contact
```

yang mengembalikan View bernama:
```
contact.blade.php
```

---

### Latihan 3

Buat route:
```
/products
```

yang memanggil:
```
ProductController@index
```

# Jawaban Soal 1, 2, 3

Web.php
```php
use App\Http\Controllers\ProductController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
	return view('welcome');
});

Route::get('/about', function(){
	return "Tentang Kami";
});

Route::get('/contact', function(){
	return view('contact');
});

Route::get('/products', [
	ProductController::class, 'index'
]);
```

ProductController.php:
```php
namespace App\Http\Controllers;
use Illuminate\Http\Request;

class ProductController extends Controller
{
	public function index(){
		return "Hello World";
	}
}
```

contact.blade.php:
```php
<div>
	<p>Ini Halaman Contact</p>
</div>
```