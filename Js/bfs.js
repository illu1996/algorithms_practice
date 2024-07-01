const bfs = function (G, v, visit) {
  q = [];
  q.push(v);
  visit[v] = 1;
  while (q.length) {
    now = q.shift();
    for (let i of G[now]) {
      if (!visit[i]) {
        visit[i] = 1;
        q.push(i);
      }
    }
  }
};
