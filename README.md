<h1 align=center>F1 Standings API</h1>

<p> A simple API written in Python that scraps the F1 website for the current year drivers championship standings.</p>

<h3 align=center>Avaliable endpoints</h3>
<h4>GET /drivers</h4>
<p>Returns all drivers in the FIA Formula 1 Championship for the current year with their position, points, name and surname, team, team color (updated 2024) and picture</p>
<p>Example:</p>
<p align="center"><img src="https://github.com/rodrigodasilv/f1-standings-api/assets/55567123/9d85f165-a4a1-4bc9-a642-f93b8c70ca83" alt="GET /f1 return" style="width:50%;"/></p>

<h3 align=center>Instalation</h3>

<h4>Via Docker</h4>
<p>The installation via Docker is pretty easy:</p>
<ol>
<li>Make sure <a href="https://www.docker.com/">Docker</a> is installed;</li>
<li>Download the repository;</li>
<li>Open a terminal on the root folder of the repository;</li>
<li>Run <code>docker compose up --build</code> and the API should be ready to go;</li>
</ol>
<h4>Manually</h4>
<p>The manual installation can be done following the steps below:</p>
<ol>
<li>Make sure <a href="https://pip.pypa.io/en/stable/getting-started/">pip</a> is installed;</li>
<li>Download the repository;</li>
<li>Open a terminal on the root folder of the repository;</li>
<li>Run <code>pip install -r requirements.txt</code> and then <code>python app.py</code> and the API should be working;</li>
</ol>
