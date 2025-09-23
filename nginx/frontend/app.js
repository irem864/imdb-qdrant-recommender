const apiBase = "/"; 
document.getElementById("searchBtn").addEventListener("click", async () => {
  const q = document.getElementById("q").value;
  if(!q) return;
  const res = await fetch(`/search?q=${encodeURIComponent(q)}&limit=8`);
  if(!res.ok) {
    alert("API hatası: " + res.statusText);
    return;
  }
  const data = await res.json();
  const container = document.getElementById("results");
  container.innerHTML = "";
  data.results.forEach(m => {
    const div = document.createElement("div");
    div.className = "movie";
    div.innerHTML = `<div class="title">${m.title} (${m.year}) — score: ${m.score.toFixed(3)}</div>
                     <div class="genres">${m.genres || ""}</div>
                     <div class="plot">${m.plot ? m.plot.slice(0,300) + "..." : ""}</div>`;
    container.appendChild(div);
  });
});
