# school-project1
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>student-cli — README</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

  :root{
    --bg:#12181b;
    --bg-raised:#171e22;
    --panel:#1b2327;
    --line:#2a3438;
    --text:#e8e1d3;
    --text-dim:#9aa5a8;
    --gold:#c9a227;
    --gold-soft:#e6c15c;
    --rose:#c1666b;
    --green:#7fae6f;
  }

  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:var(--bg);
    color:var(--text);
    font-family:'IBM Plex Mono', monospace;
    line-height:1.65;
    -webkit-font-smoothing:antialiased;
  }
  h1,h2,h3,.brand{
    font-family:'Space Grotesk', sans-serif;
    font-weight:700;
    letter-spacing:-0.01em;
  }
  a{color:var(--gold-soft);}

  .wrap{max-width:860px;margin:0 auto;padding:0 24px 80px;}

  /* ---------- HERO ---------- */
  .hero{
    border-bottom:1px solid var(--line);
    padding:64px 0 40px;
  }
  .eyebrow{
    color:var(--gold);
    font-size:13px;
    letter-spacing:0.14em;
    text-transform:uppercase;
    margin-bottom:14px;
  }
  h1{
    font-size:clamp(32px,5vw,46px);
    margin:0 0 10px;
    color:var(--text);
  }
  .tagline{
    color:var(--text-dim);
    font-size:16px;
    max-width:560px;
    margin:0 0 32px;
  }

  /* terminal mockup — signature element */
  .terminal{
    background:var(--bg-raised);
    border:1px solid var(--line);
    border-radius:10px;
    overflow:hidden;
    box-shadow:0 20px 50px -20px rgba(0,0,0,0.6);
  }
  .terminal-bar{
    display:flex;
    align-items:center;
    gap:8px;
    padding:11px 14px;
    background:#161c1f;
    border-bottom:1px solid var(--line);
  }
  .dot{width:10px;height:10px;border-radius:50%;}
  .dot.r{background:#c1666b;}
  .dot.y{background:#c9a227;}
  .dot.g{background:#7fae6f;}
  .terminal-title{
    margin-left:8px;
    font-size:12px;
    color:var(--text-dim);
  }
  .terminal-body{
    padding:20px 22px 24px;
    font-size:13.5px;
    color:#c9d1cf;
  }
  .terminal-body .prompt{color:var(--gold-soft);}
  .terminal-body .muted{color:var(--text-dim);}
  .cursor{
    display:inline-block;
    width:7px;height:14px;
    background:var(--gold-soft);
    margin-left:2px;
    vertical-align:middle;
    animation:blink 1.1s steps(1) infinite;
  }
  @keyframes blink{50%{opacity:0;}}

  /* ---------- SECTIONS ---------- */
  section{padding:44px 0;border-bottom:1px solid var(--line);}
  section:last-child{border-bottom:none;}
  h2{
    font-size:14px;
    letter-spacing:0.12em;
    text-transform:uppercase;
    color:var(--text-dim);
    margin:0 0 20px;
  }
  h2 .num{color:var(--gold);margin-right:10px;}

  p{margin:0 0 14px;color:#cfd6d2;}

  ul.plain{list-style:none;padding:0;margin:0;}
  ul.plain li{
    padding:10px 0;
    border-bottom:1px dashed var(--line);
    display:flex;
    gap:14px;
  }
  ul.plain li:last-child{border-bottom:none;}
  ul.plain .k{
    color:var(--gold-soft);
    min-width:96px;
    flex-shrink:0;
    font-weight:600;
  }

  .grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:14px;
  }
  .card{
    background:var(--panel);
    border:1px solid var(--line);
    border-radius:8px;
    padding:16px 18px;
  }
  .card .n{color:var(--gold);font-size:12px;letter-spacing:0.08em;}
  .card p{margin:6px 0 0;font-size:13.5px;color:var(--text-dim);}

  pre{
    background:var(--panel);
    border:1px solid var(--line);
    border-radius:8px;
    padding:16px 18px;
    overflow-x:auto;
    font-size:13px;
    color:#c9d1cf;
  }
  code{
    font-family:'IBM Plex Mono', monospace;
    background:rgba(201,162,39,0.1);
    padding:1px 6px;
    border-radius:4px;
    font-size:0.92em;
    color:var(--gold-soft);
  }
  pre code{background:none;padding:0;color:inherit;}

  .changelog li{align-items:flex-start;}
  .fixed{color:var(--green);font-weight:600;font-size:12px;letter-spacing:0.05em;text-transform:uppercase;}

  .roadmap{
    background:linear-gradient(180deg, rgba(201,162,39,0.06), transparent);
    border:1px solid var(--line);
    border-radius:10px;
    padding:22px 24px;
  }
  .roadmap p:last-child{margin-bottom:0;}
  .roadmap .arrow{color:var(--gold);}

  footer{
    padding:36px 0 0;
    color:var(--text-dim);
    font-size:12.5px;
  }

  @media (max-width:600px){
    ul.plain li{flex-direction:column;gap:2px;}
    ul.plain .k{min-width:0;}
  }
</style>
</head>
<body>
<div class="wrap">

  <div class="hero">
    <div class="eyebrow">practice project · sqlite + python</div>
    <h1>student-cli</h1>
    <p class="tagline">A command-line student management system with admin login and a SQLite backend — built to practice core Python and SQL before moving on to FastAPI.</p>

    <div class="terminal">
      <div class="terminal-bar">
        <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
        <span class="terminal-title">python admin.py</span>
      </div>
      <div class="terminal-body">
<span class="muted">gave your username: </span>admin1234<br>
<span class="muted">enter password: </span>••••<br>
<br>
school grade 7 to 9<br>
&nbsp;1. add student<br>
&nbsp;2. show student<br>
&nbsp;3. find student by name<br>
&nbsp;4. update students<br>
&nbsp;5. delete students<br>
&nbsp;6. exit<br>
<span class="prompt">type the number: </span><span class="cursor"></span>
      </div>
    </div>
  </div>

  <section>
    <h2><span class="num">01</span>About</h2>
    <p>This project is a small CLI tool for managing student records: names, grades, and a running grade history, stored in a local SQLite database. Access is gated behind a simple admin login. It's a deliberately hands-on exercise — reading input, validating it, and talking to a real database — rather than a polished product.</p>
  </section>

  <section>
    <h2><span class="num">02</span>Features</h2>
    <div class="grid">
      <div class="card"><div class="n">ADD</div><p>Register a new student with a name and grade level (7–9), rejecting duplicates.</p></div>
      <div class="card"><div class="n">SHOW</div><p>List all students, or filter by grade level.</p></div>
      <div class="card"><div class="n">FIND</div><p>Look up a single student by name.</p></div>
      <div class="card"><div class="n">UPDATE</div><p>Edit a student's grade history, name, or grade level.</p></div>
      <div class="card"><div class="n">DELETE</div><p>Remove a student record.</p></div>
      <div class="card"><div class="n">AUTH</div><p>A separate <code>admin.py</code> entry point gates access before <code>start()</code> runs.</p></div>
    </div>
  </section>

  <section>
    <h2><span class="num">03</span>Project structure</h2>
    <pre><code>.
├── admin.py     # login gate, then calls start() from main.py
├── main.py      # CLI menu loop + all SQLite operations
└── full.db      # SQLite database (created on first run)</code></pre>
  </section>

  <section>
    <h2><span class="num">04</span>Running it</h2>
    <pre><code>python admin.py</code></pre>
    <p>Log in with the admin credentials, then use the numbered menu to manage student records. The database file is created automatically on first run if it doesn't exist.</p>
  </section>

  <section class="changelog">
    <h2><span class="num">05</span>Fixed while building</h2>
    <ul class="plain">
      <li><span class="k fixed">fixed</span><span>Database connection was being closed immediately after table creation, breaking every later menu option.</span></li>
      <li><span class="k fixed">fixed</span><span>Changes weren't committed after insert/update/delete — calls were left incomplete instead of calling <code>commit()</code>.</span></li>
      <li><span class="k fixed">fixed</span><span>Result rows were being indexed incorrectly, so records printed as scrambled fragments instead of full rows.</span></li>
      <li><span class="k fixed">fixed</span><span>A stray comma in an <code>INSERT</code> statement and a couple of typos in column names and method calls.</span></li>
      <li><span class="k fixed">fixed</span><span>A login check in <code>admin.py</code> used <code>and</code> where it needed <code>or</code>, letting a wrong password slip through silently.</span></li>
    </ul>
  </section>

  <section>
    <h2><span class="num">06</span>What's next</h2>
    <div class="roadmap">
      <p><span class="arrow">→</span> Keep extending this CLI as practice: cleaner error handling, maybe a proper class-based structure around the database logic.</p>
      <p><span class="arrow">→</span> Once this feels solid, move on to <strong>learning FastAPI</strong> — likely by rebuilding this same student-management idea as a real API with endpoints instead of a menu loop.</p>
    </div>
  </section>

  <footer>
    A learning project — built to practice Python, SQL, and debugging real (self-inflicted) bugs.
  </footer>

</div>
</body>
</html>
