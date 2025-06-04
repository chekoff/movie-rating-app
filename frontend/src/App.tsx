
import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:5000';

function App() {
  const [users, setUsers] = useState<any[]>([]);
  const [movies, setMovies] = useState<any[]>([]);
  const [selectedUser, setSelectedUser] = useState('');
  const [ratings, setRatings] = useState<{ [key: number]: number }>({});

  useEffect(() => {
    fetch(`${API_URL}/users`).then(res => res.json()).then(setUsers);
    fetch(`${API_URL}/movies`).then(res => res.json()).then(setMovies);
  }, []);

  const rateMovie = (movieId: number) => {
    if (!selectedUser) return alert('Select a user');
    const userId = users.find(u => u.name === selectedUser)?.id;
    const rating = ratings[movieId];

    fetch(`${API_URL}/rate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ movie_id: movieId, user_id: userId, rating })
    })
      .then(res => res.json())
      .then(data => alert(`Rating saved: ${JSON.stringify(data)}`));
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Movie Rating App</h1>
      <label>Select user: </label>
      <select value={selectedUser} onChange={e => setSelectedUser(e.target.value)}>
        <option value="">--</option>
        {users.map(user => <option key={user.id} value={user.name}>{user.name}</option>)}
      </select>

      {movies.map(movie => (
        <div key={movie.id} className="mt-4">
          <span>{movie.title}</span>
          <input
            type="number"
            min="1"
            max="5"
            value={ratings[movie.id] || ''}
            onChange={e => setRatings({ ...ratings, [movie.id]: parseInt(e.target.value) })}
            className="ml-2 border"
          />
          <button onClick={() => rateMovie(movie.id)} className="ml-2 bg-blue-500 text-white px-2">Rate</button>
        </div>
      ))}
    </div>
  );
}

export default App;
