import React, { useEffect, useState } from 'react';

const endpoint = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboards/`
  : 'http://localhost:8000/api/leaderboards/';

export default function Leaderboard() {
  const [leaderboards, setLeaderboards] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboards(results);
        console.log('Fetched leaderboards:', results);
      })
      .catch(err => console.error('Error fetching leaderboards:', err));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title mb-4">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>Team</th>
                <th>Total Points</th>
              </tr>
            </thead>
            <tbody>
              {leaderboards.map((l, i) => (
                <tr key={l.id || i}>
                  <td>{i + 1}</td>
                  <td>{l.team?.name || 'Unknown Team'}</td>
                  <td>{l.total_points}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
