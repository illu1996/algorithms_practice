const dfs = function (G, v, visit) {
  visit[v] = 1;
  console.log(v);
  for (let i of G[v]) {
    if (!visit[i]) {
      dfs(G, i, visit);
    }
  }
};
