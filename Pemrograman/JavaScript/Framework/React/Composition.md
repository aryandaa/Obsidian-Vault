#programming 
 Anda mungkin sudah terbiasa memecah kode yang kompleks menjadi fungsi terpisah agar kode lebih mudah dibaca. Jika fungsi mengembalikan sebuah data, Anda juga mungkin terbiasa menggabungkan beberapa fungsi untuk menciptakan data yang lebih kompleks. Contohnya seperti ini.
```js
function getProfilePicture(userId) {
  return `https://avatars.githubusercontent.com/u/${userId}`;
}

function getProfileLink(username) {
  return `https://github.com/${username}`;
}


function getGithubInfo(username, userId) {
  return {
    profilePicture: getProfilePicture(userId),
    profileLink: getProfileLink(username),
  };
}

console.log(getGithubInfo('dimasmds', 25724809));

/**
* output:
 {
    profilePicture: 'https://avatars.githubusercontent.com/u/25724809',
    profileLink: 'https://github.com/dimasmds'
 }
*/
```

Proses menggabungkan banyak fungsi untuk menciptakan data yang lebih kompleks dinamakan _composition_ (komposisi). Di React, praktik komposisi seperti ini menjadi fondasi dan membuatnya menjadi sangat luar biasa.

Praktik komposisi di React biasa ditemukkan ketika pembuatan dan penggunaan sebuah component. Component di React bersifat _reusable_ dan dapat dikomposisikan untuk menciptakan component yang lebih kompleks.
```jsx
function ProfilePicture({ userId }) {
  return (
    <img
      src={"https://avatars.githubusercontent.com/u/" + userId}
      alt="GitHub Profile"
    />
  );
}

function ProfileLink({ username }) {
  return <a href={"https://github.com/" + username}>{username}</a>;
}

function GithubInfo({ username, userId }) {
  return (
    <div className="github-info">
      <ProfilePicture userId={userId} />
      <ProfileLink username={username} />
    </div>
  );
}

export default GithubInfo;
```

```js
import GithubInfo from "./GithubInfo";

export default function App() {
  return <GithubInfo username={"dimasmds"} userId={25724809} />;
}
```

Komposisi merupakan _language agnostic_ dan menjadi konsep umum pada dunia pemrograman. Intuisi dalam mempraktikkan komposisi secara alami akan sama dengan bahasa pemrograman apa pun. Jika Anda berpengalaman mempraktikkan komposisi pada bahasa pemrograman Python, intuisi Anda bisa digunakan juga ketika membuat React component.